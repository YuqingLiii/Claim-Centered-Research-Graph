"""Independent stim emission + search.  The circuit is emitted from MY Schedule object and MY
detector convention (Def 2.7); stim then supplies its own Pauli propagation, DEM extraction and
graph search.  Third method, different codebase."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rev_core as C
import stim


def emit(sch, R, sector, order=None):
    if order is None:
        order = []
    code = sch.code
    n = code.n
    na, nb = sch.na, sch.nb
    c = stim.Circuit()
    if sector == "Z":
        c.append("R", list(range(n)))
    else:
        c.append("RX", list(range(n)))
    rec = {}           # (fam, i, r) -> absolute measurement index
    nmeas = 0
    for r in range(R):
        c.append("RX", [sch.anc_x(i) for i in range(na)])
        c.append("R", [sch.anc_z(i) for i in range(nb)])
        c.append("DEPOLARIZE1", [sch.anc_x(i) for i in range(na)], 0.001)
        c.append("DEPOLARIZE1", [sch.anc_z(i) for i in range(nb)], 0.001)
        for t in range(sch.T):
            pairs = []
            busy = set()
            for (ctl, tgt, kind, ci) in sch.layers[t]:
                pairs += [ctl, tgt]
                busy.add(ctl); busy.add(tgt)
            c.append("CX", pairs)
            c.append("DEPOLARIZE2", pairs, 0.001)
            idle = [q for q in range(sch.nq) if q not in busy]
            if idle:
                c.append("DEPOLARIZE1", idle, 0.001)
        c.append("MX", [sch.anc_x(i) for i in range(na)], 0.001)
        for i in range(na):
            rec[("a", i, r)] = nmeas; nmeas += 1
        c.append("M", [sch.anc_z(i) for i in range(nb)], 0.001)
        for i in range(nb):
            rec[("b", i, r)] = nmeas; nmeas += 1
        # detectors available so far
        full = "b" if sector == "Z" else "a"
        part = "a" if sector == "Z" else "b"
        nfull = nb if sector == "Z" else na
        npart = na if sector == "Z" else nb
        for i in range(nfull):
            tg = [stim.target_rec(rec[(full, i, r)] - nmeas)]
            if r >= 1:
                tg.append(stim.target_rec(rec[(full, i, r - 1)] - nmeas))
            c.append("DETECTOR", tg)
            order.append((full, i, r))
        if r >= 1:                      # Def 2.7: D_{a,r} for r = 1..R-1
            for i in range(npart):
                c.append("DETECTOR", [stim.target_rec(rec[(part, i, r)] - nmeas),
                                      stim.target_rec(rec[(part, i, r - 1)] - nmeas)])
                order.append((part, i, r))
    # terminal ideal readout
    c.append("MX" if sector == "X" else "M", list(range(n)))
    for q in range(n):
        rec[("d", q, R)] = nmeas; nmeas += 1
    full = "b" if sector == "Z" else "a"
    fullchecks = code.zchecks if sector == "Z" else code.xchecks
    for i, (supp, _) in enumerate(fullchecks):
        tg = [stim.target_rec(rec[("d", q, R)] - nmeas) for q in supp]
        tg.append(stim.target_rec(rec[(full, i, R - 1)] - nmeas))
        c.append("DETECTOR", tg)
        order.append((full, i, R))
    logs = code.zlog if sector == "Z" else code.xlog
    for j, L in enumerate(logs):
        tg = [stim.target_rec(rec[("d", q, R)] - nmeas) for q in range(n) if (L >> q) & 1]
        c.append("OBSERVABLE_INCLUDE", tg, j)
    return c


def stim_distance(sch, R, sector, cap=6):
    c = emit(sch, R, sector)
    try:
        errs = c.search_for_undetectable_logical_errors(
            dont_explore_detection_event_sets_with_size_above=8,
            dont_explore_edges_with_degree_above=6,
            dont_explore_edges_increasing_symptom_degree=False,
            canonicalize_circuit_errors=True)
        return len(errs), c
    except Exception as e:
        return ("ERR:%s" % type(e).__name__, c)


def dem_signature_set(sch, R, sector):
    """set of (frozenset detector KEYS, frozenset observables) over stim's own DEM."""
    order = []
    c = emit(sch, R, sector, order)
    dem = c.detector_error_model(decompose_errors=False, allow_gauge_detectors=True)
    sigs = set()
    for inst in dem.flattened():
        if inst.type != "error":
            continue
        ds, os_ = [], []
        for tg in inst.targets_copy():
            if tg.is_relative_detector_id():
                ds.append(order[tg.val])
            elif tg.is_logical_observable_id():
                os_.append(tg.val)
        if ds or os_:
            sigs.add((frozenset(ds), frozenset(os_)))
    return sigs


def my_signature_set(sch, R, sector):
    inst = C.Instance(sch, R, sector)
    inv = {v: k for k, v in inst.det_id.items()}
    sigs = set()
    for (dm, om) in inst.classes().keys():
        ds = frozenset(inv[i] for i in range(inst.ndet) if (dm >> i) & 1)
        os_ = frozenset(j for j in range(inst.nobs) if (om >> j) & 1)
        sigs.add((ds, os_))
    return sigs


if __name__ == "__main__":
    SCHEDS = {"classD": (("NW", "SW", "NE", "SE"), ("NW", "NE", "SW", "SE")),
              "standard": (("NW", "NE", "SW", "SE"), ("NW", "SW", "NE", "SE"))}
    d = int(sys.argv[1]); name = sys.argv[2]
    Rs = [int(x) for x in sys.argv[3].split(",")]
    code = C.rotated_surface(d)
    piX, piZ = SCHEDS[name]
    sch = C.uniform_schedule(code, piX, piZ)
    print("=== stim arm: d=%d %s  legal=%s (MC)=%s" % (d, name, C.is_legal(sch), C.mc_holds(sch)[0]))
    for R in Rs:
        for sector in ("Z", "X"):
            a = my_signature_set(sch, R, sector)
            b = dem_signature_set(sch, R, sector)
            same = (a == b)
            print("  R=%d %s  MODEL-EQUALITY my_matrix vs stim DEM: %s  (|mine|=%d |stim|=%d, "
                  "mine-only=%d stim-only=%d)" % (R, sector, same, len(a), len(b),
                                                  len(a - b), len(b - a)))
            w, _ = stim_distance(sch, R, sector)
            print("  R=%d %s  STIM search min undetectable logical = %s" % (R, sector, w))
