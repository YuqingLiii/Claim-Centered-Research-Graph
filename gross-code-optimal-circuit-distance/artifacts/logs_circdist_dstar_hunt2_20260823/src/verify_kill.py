"""Independent, from-first-principles verification of a claimed weight-<=10 effective logical.

Nothing in this file uses core2's Sector/option helpers: residual supports are rebuilt directly
from the raw CNOT times tX / tZ, membership tests are recomputed from H_X / H_Z, and the fault
count is counted item by item.
"""
import json, sys
import core2 as C

SECT = sys.argv[1]
CONF = sys.argv[2]          # json produced by strat12.py
NSHOW = int(sys.argv[3]) if len(sys.argv) > 3 else 4

(tX, tZ), T = C.load_candidate()
(pz, _, _), (px, _, _) = C.pools()
mir = (SECT == 'X')
pool = px if mir else pz

# raw CNOT time of the hook gate  ancilla(a) -> q   (Z-memory)  /  q -> ancilla(a)  (X-memory)
if not mir:
    hchk, stab_rows, kern_rows = C.Xchk, C.HXm, C.HZm
    def th(a, q):
        return tX[(a, q)]
else:
    hchk, stab_rows, kern_rows = C.Zchk, C.HZm, C.HXm
    def th(a, q):
        return tZ[(q, a)]

RS, RP = C.rref(stab_rows)          # rowspace of the sector's stabiliser generators

conf = json.load(open(CONF))
conf.sort(key=lambda x: x[0])
print("sector=%s   configurations in file: %d   min cost: %d" % (SECT, len(conf), conf[0][0]))
ok = 0
for (cost, vi, ch) in conf:
    V = pool[vi]
    # --- (1) V really is a nontrivial logical of this sector
    assert C.popc(V) == 12
    assert all(C.popc(V & h) % 2 == 0 for h in kern_rows), "V not in the kernel"
    assert not C.inspan(V, RS, RP), "V is a stabiliser"
    # --- (2) rebuild every residual support from the RAW times
    residuals = []
    for (a, K) in ch:
        order = sorted(hchk[a], key=lambda q: th(a, q))       # earliest CNOT first
        assert len(order) == 6
        for l in K:
            residuals.append(('hook', a, l, order[6 - l:]))   # suffix = the LAST l CNOTs
    D = 0
    for (_, _, _, S) in residuals:
        for q in S:
            D ^= 1 << q
    Tset = C.bits(V ^ D)
    for q in Tset:
        residuals.append(('single', None, 1, [q]))
    # --- (3) XOR of all residual supports is exactly V
    tot = 0
    for (_, _, _, S) in residuals:
        for q in S:
            tot ^= 1 << q
    assert tot == V, "residual XOR != V"
    assert len(residuals) == cost, "fault count mismatch %d vs %d" % (len(residuals), cost)
    ok += 1
    if ok <= NSHOW:
        print("\n--- witness %d : cost %d, |V| = %d, logical index %d" % (ok, cost, C.popc(V), vi))
        print("    V = %s" % C.bits(V))
        for (kind, a, l, S) in residuals:
            if kind == 'hook':
                order = sorted(hchk[a], key=lambda q: th(a, q))
                print("    hook  check %2d  %d-suffix  qubits %-22s times %s   (full order %s / times %s)"
                      % (a, l, S, [th(a, q) for q in S], order, [th(a, q) for q in order]))
        print("    singletons (%d): %s" % (len(Tset), Tset))
        print("    fault count = %d hooks + %d singletons = %d" %
              (len(residuals) - len(Tset), len(Tset), len(residuals)))
print("\nVERIFIED %d / %d configurations (all assertions passed)" % (ok, len(conf)))
mn = conf[0][0]
print("minimum verified fault count in this file: %d  ->  d_eff(%s-memory) <= %d" % (mn, SECT, mn))
