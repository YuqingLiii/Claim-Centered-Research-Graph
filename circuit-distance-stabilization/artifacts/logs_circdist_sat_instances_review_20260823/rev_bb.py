"""qLDPC arm: independent rebuild of the bivariate-bicycle [[18,4,4]] code from the PRINTED
algebra (l=m=3, A = 1+y+x, B = 1+y+x^2 y, H_X=[A|B], H_Z=[B^T|A^T]), the non-interleaved
depth-12 schedule NI, and the exhaustive depth-6 (MC) by-product."""
import sys, os, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rev_core as C

L, M = 3, 3
AMON = [(0, 0), (0, 1), (1, 0)]          # A = 1 + y + x
BMON = [(0, 0), (0, 1), (2, 1)]          # B = 1 + y + x^2 y


def gidx(i, j):
    return (i % L) * M + (j % M)


def build_code():
    """qubit index: left block  q = gidx(i,j)  in 0..8 ; right block q = 9 + gidx(i,j).
    X-check indexed by group element g=(i,j): controls CNOT onto
       left  qubit (i+a, j+b) for each (a,b) in AMON   [row of A]
       right qubit (i+a, j+b) for each (a,b) in BMON   [row of B]
    Z-check indexed by g: targets of CNOTs from
       left  qubit reached by B^T  -> (i-a, j-b) for (a,b) in BMON
       right qubit reached by A^T  -> (i-a, j-b) for (a,b) in AMON
    """
    n = 2 * L * M
    xchecks, zchecks = [], []
    for i in range(L):
        for j in range(M):
            xs, xrole = [], {}
            for k, (a, b) in enumerate(AMON):
                q = gidx(i + a, j + b); xs.append(q); xrole["A%d" % (k + 1)] = q
            for k, (a, b) in enumerate(BMON):
                q = 9 + gidx(i + a, j + b); xs.append(q); xrole["B%d" % (k + 1)] = q
            xchecks.append((tuple(sorted(xs)), xrole))
            zs, zrole = [], {}
            for k, (a, b) in enumerate(BMON):
                q = gidx(i - a, j - b); zs.append(q); zrole["Bt%d" % (k + 1)] = q
            for k, (a, b) in enumerate(AMON):
                q = 9 + gidx(i - a, j - b); zs.append(q); zrole["At%d" % (k + 1)] = q
            zchecks.append((tuple(sorted(zs)), zrole))
    code = C.Code(n, xchecks, zchecks, [], [], "BB_l3m3")
    hx, hz = code.hx_rows(), code.hz_rows()
    # logical representatives: complete bases of ker/S
    kerHZ = C.kernel_basis(hz, n)
    kerHX = C.kernel_basis(hx, n)
    code.xlog = pick_logicals(kerHZ, hx, n)
    code.zlog = pick_logicals(kerHX, hz, n)
    return code


def pick_logicals(ker, stab_rows, n):
    """extend rowsp(stab) to a basis of ker; return the k added vectors."""
    basis = list(stab_rows)
    out = []
    for v in ker:
        if not C.in_span(v, basis, n):
            basis.append(v)
            out.append(v)
    return out


def report_code(code):
    n = code.n
    hx, hz = code.hx_rows(), code.hz_rows()
    bad = sum(1 for a in hx for b in hz if C.popcount(a & b) % 2)
    rx, rz = C.rank_f2(hx, n), C.rank_f2(hz, n)
    k = n - rx - rz
    from collections import Counter
    print("BB: n=%d  #X-checks=%d #Z-checks=%d  rank H_X=%d rank H_Z=%d  k=%d  anticommuting pairs=%d"
          % (n, len(hx), len(hz), rx, rz, k, bad))
    print("    check weights X=%s Z=%s" % (dict(Counter(C.popcount(a) for a in hx)),
                                           dict(Counter(C.popcount(b) for b in hz))))
    degX = [sum(1 for a in hx if (a >> q) & 1) for q in range(n)]
    degZ = [sum(1 for b in hz if (b >> q) & 1) for q in range(n)]
    print("    qubit degrees in H_X: %s ; in H_Z: %s"
          % (dict(Counter(degX)), dict(Counter(degZ))))
    print("    #logical reps: X=%d Z=%d" % (len(code.xlog), len(code.zlog)))
    # exhaustive distances over the 2^(n - rank) kernels
    kerHZ = C.kernel_basis(hz, n)
    kerHX = C.kernel_basis(hx, n)
    dX = C.min_weight_coset(kerHZ, n, lambda v: any(C.popcount(v & Z) % 2 for Z in code.zlog))
    dZ = C.min_weight_coset(kerHX, n, lambda v: any(C.popcount(v & X) % 2 for X in code.xlog))
    print("    EXHAUSTIVE over 2^%d and 2^%d: d_X=%d d_Z=%d  ->  [[%d,%d,%d]]"
          % (len(kerHZ), len(kerHX), dX, dZ, n, k, min(dX, dZ)))
    # Standing fact 2.2 check, exhaustively over ker H_Z
    mism = 0
    for m in range(1 << len(kerHZ)):
        v = 0; mm = m; t = 0
        while mm:
            if mm & 1:
                v ^= kerHZ[t]
            mm >>= 1; t += 1
        lam = any(C.popcount(v & Z) % 2 for Z in code.zlog)
        instab = C.in_span(v, hx, n)
        if lam == instab:
            mism += 1
    print("    Standing fact 2.2 exhaustive over all 2^%d of ker H_Z: mismatches=%d"
          % (len(kerHZ), mism))
    return k, min(dX, dZ)


def schedule_NI(code):
    """X-check CNOTs layers 0..5 in monomial order A1,A2,A3,B1,B2,B3;
    Z-check CNOTs layers 6..11 in order Bt1,Bt2,Bt3,At1,At2,At3."""
    tX = {"A1": 0, "A2": 1, "A3": 2, "B1": 3, "B2": 4, "B3": 5}
    tZ = {"Bt1": 6, "Bt2": 7, "Bt3": 8, "At1": 9, "At2": 10, "At3": 11}
    return build_sched(code, tX, tZ, 12, "NI")


def build_sched(code, tX, tZ, T, tag):
    layers = [[] for _ in range(T)]
    na = len(code.xchecks)
    for i, (supp, role) in enumerate(code.xchecks):
        a = code.n + i
        for nm, q in role.items():
            layers[tX[nm]].append((a, q, "X", i))
    for i, (supp, role) in enumerate(code.zchecks):
        b = code.n + na + i
        for nm, q in role.items():
            layers[tZ[nm]].append((q, b, "Z", i))
    return C.Schedule(code, layers, T, tag)


def depth6_scan(code):
    """exhaustive over the stated family |6! x 6!| = 518400."""
    xnames = ["A1", "A2", "A3", "B1", "B2", "B3"]
    znames = ["Bt1", "Bt2", "Bt3", "At1", "At2", "At3"]
    legal = 0; legal_mc = 0; tot = 0
    t0 = time.time()
    for px in itertools.permutations(range(6)):
        tX = {xnames[i]: px[i] for i in range(6)}
        for pz in itertools.permutations(range(6)):
            tot += 1
            tZ = {znames[i]: pz[i] for i in range(6)}
            sch = build_sched(code, tX, tZ, 6, "d6")
            if not C.is_legal(sch):
                continue
            legal += 1
            ok, _ = C.mc_holds(sch)
            if ok:
                legal_mc += 1
    print("DEPTH-6 EXHAUSTIVE SCAN: %d candidates -> %d legal -> %d legal AND (MC)   [%.0fs]"
          % (tot, legal, legal_mc, time.time() - t0))
    return tot, legal, legal_mc


if __name__ == "__main__":
    code = build_code()
    k, dd = report_code(code)
    sch = schedule_NI(code)
    ok, info = C.mc_holds(sch)
    ncn = sum(len(l) for l in sch.layers)
    print("schedule NI: T=%d legal=%s (MC)=%s  total CNOTs=%d  per-layer=%s"
          % (sch.T, C.is_legal(sch), ok, ncn, [len(l) for l in sch.layers]))
    mode = sys.argv[1] if len(sys.argv) > 1 else "dist"
    if mode == "scan":
        depth6_scan(code)
    else:
        for R in range(1, 7):
            for sector in ("Z", "X"):
                inst = C.Instance(sch, R, sector)
                w, wit = C.min_weight_exhaustive(inst, 3)
                res = str(w) if w is not None else ">3"
                print("  R=%d %s classes=%d detectors=%d  EXHAUSTIVE<=3: %s"
                      % (R, sector, C.count_classes(inst), inst.ndet, res), flush=True)
                if wit:
                    silent, obs, nloc, _ = C.audit_witness(sch, R, sector, wit)
                    print("     AUDIT w=%d distinct_loc=%d silent=%s obs=%s" % (w, nloc, silent, obs))
                    for lab in wit:
                        print("       ", lab)
