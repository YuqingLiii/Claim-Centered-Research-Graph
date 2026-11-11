"""Exact ILP feasibility at a weight cap: decides d_R > cap (infeasible) or exhibits a witness.
Much cheaper than proving optimality, and it is exactly the shape of the claims under review.
Also constructs the canonical weight-d spatial witness so that d_R <= d is exhibited, not imported.
"""
import sys, os
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rev_core as C


def feasible_at_most(inst, cap, obs_index=None, time_limit=600.0, restrict=None):
    """returns (status, weight, witness). status in {'FEASIBLE','INFEASIBLE','TIMEOUT'}."""
    cls = inst.classes()
    items = list(cls.items())
    if restrict is not None:
        items = [it for it in items if restrict(it)]
    N = len(items)
    ndet = inst.ndet
    targets = [obs_index] if obs_index is not None else list(range(inst.nobs))
    best = None; bestwit = None; anytimeout = False
    for j in targets:
        nrows = ndet + 2
        nvars = N + ndet + 1
        A = lil_matrix((nrows, nvars))
        lo = np.zeros(nrows); hi = np.zeros(nrows)
        for i, ((dm, om), lab) in enumerate(items):
            d = dm
            while d:
                b = (d & -d).bit_length() - 1
                A[b, i] = 1
                d &= d - 1
            if (om >> j) & 1:
                A[ndet, i] = 1
            A[ndet + 1, i] = 1
        for rr in range(ndet + 1):
            A[rr, N + rr] = -2
        lo[ndet] = hi[ndet] = 1
        lo[ndet + 1] = 0; hi[ndet + 1] = cap
        c = np.zeros(nvars); c[:N] = 1.0
        ub = np.ones(nvars); ub[N:] = np.inf
        res = milp(c=c, constraints=LinearConstraint(A.tocsr(), lo, hi),
                   integrality=np.ones(nvars), bounds=Bounds(np.zeros(nvars), ub),
                   options={"mip_rel_gap": 0.0, "presolve": True, "time_limit": time_limit})
        if res.status == 2:
            continue                      # infeasible for this observable
        if res.status == 1:
            anytimeout = True
            continue
        if res.x is None:
            continue
        w = int(round(res.fun))
        if best is None or w < best:
            best = w
            bestwit = [items[i][1] for i in range(N) if res.x[i] > 0.5]
    if best is not None:
        return "FEASIBLE", best, bestwit
    return ("TIMEOUT" if anytimeout else "INFEASIBLE"), None, None


def spatial_witness(sch, R, sector):
    """weight-d_X (resp d_Z) undetectable logical placed after the LAST layer of the last round:
    exhibits d_R <= d without importing anything."""
    code = sch.code
    hx, hz = code.hx_rows(), code.hz_rows()
    if sector == "Z":
        ker = C.kernel_basis(hz, code.n); L = code.zlog[0]
    else:
        ker = C.kernel_basis(hx, code.n); L = code.xlog[0]
    best = None
    k = len(ker)
    for m in range(1, 1 << k):
        v = 0; mm = m; i = 0
        while mm:
            if mm & 1:
                v ^= ker[i]
            mm >>= 1; i += 1
        if C.popcount(v & L) % 2 == 1:
            if best is None or C.popcount(v) < C.popcount(best):
                best = v
    supp = [q for q in range(code.n) if (best >> q) & 1]
    t = sch.T - 1
    labels = []
    busy = {}
    for (ctl, tgt, kind, ci) in sch.layers[t]:
        busy[ctl] = (ctl, tgt, "c"); busy[tgt] = (ctl, tgt, "t")
    p = 1 if sector == "Z" else 2          # X-type fault for Z-memory, Z-type for X-memory
    for q in supp:
        if q in busy:
            ctl, tgt, role = busy[q]
            pc = p if role == "c" else 0
            pt = p if role == "t" else 0
            labels.append(("cnot", R - 1, t, (ctl, tgt), (pc, pt)))
        else:
            labels.append(("idle", R - 1, t, q, p))
    return len(supp), labels


if __name__ == "__main__":
    SCHEDS = {"classD": (("NW", "SW", "NE", "SE"), ("NW", "NE", "SW", "SE")),
              "standard": (("NW", "NE", "SW", "SE"), ("NW", "SW", "NE", "SE"))}
    d = int(sys.argv[1]); name = sys.argv[2]
    Rs = [int(x) for x in sys.argv[3].split(",")]
    cap = int(sys.argv[4])
    sectors = sys.argv[5].split(",") if len(sys.argv) > 5 else ["Z", "X"]
    tl = float(sys.argv[6]) if len(sys.argv) > 6 else 600.0
    code = C.rotated_surface(d)
    piX, piZ = SCHEDS[name]
    sch = C.uniform_schedule(code, piX, piZ)
    print("=== ILP-cap arm: d=%d %s legal=%s (MC)=%s  cap=%d" %
          (d, name, C.is_legal(sch), C.mc_holds(sch)[0], cap), flush=True)
    for sector in sectors:
        w, labs = spatial_witness(sch, 1, sector)
        print("  spatial witness weight %d exists in every R (exhibits d_R <= %d)" % (w, w), flush=True)
        for R in Rs:
            inst = C.Instance(sch, R, sector)
            st, w2, wit = feasible_at_most(inst, cap, time_limit=tl)
            print("  R=%d %s  classes=%d  ILP with sum x <= %d : %s%s"
                  % (R, sector, C.count_classes(inst), cap, st,
                     ("  weight=%d" % w2) if w2 is not None else ""), flush=True)
            if wit:
                silent, obs, nloc, _ = C.audit_witness(sch, R, sector, wit)
                print("     AUDIT w=%d distinct_loc=%d silent=%s obs=%s" % (w2, nloc, silent, obs),
                      flush=True)
                for lab in wit:
                    print("       ", lab, flush=True)
            # also audit the spatial witness at this R
            wsp, labsp = spatial_witness(sch, R, sector)
            silent, obs, nloc, _ = C.audit_witness(sch, R, sector, labsp)
            print("     SPATIAL-WITNESS AUDIT R=%d w=%d silent=%s obs=%s" % (R, wsp, silent, obs),
                  flush=True)
