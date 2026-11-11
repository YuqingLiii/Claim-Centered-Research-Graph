"""KNOWN-CELL REPRODUCTION + the decoupling lemma.

LEMMA D (proposer level, proof by inspection of the frozen model).  The residual set E(M) is
{suffixes of the hook checks' CNOT ORDERS} u {singletons} u {empty}.  Every column of the extended
code is therefore a function of the 72 within-check ORDERS alone; the absolute CNOT TIMES enter
only through those orders.  Hence d_eff = d_ext(E(M)) depends only on the within-check orders and
is INVARIANT under any re-timing that preserves them -- interleaving included.

KNOWN CELL.  artifacts/circdist_gross_verdict_20260823.md certifies d_ext(E(M_cand)) = 11 in both
sectors for the reconstructed [SBB26] candidate (990 sub-queries, all UNSAT, ~160 CPU-hours,
cadical/kissat).  M_cand is the phi = a+b three-colour tiling with within-check order-class
triples Z = (1,2,62), X = (14,0,2), whose slot orders are written out verbatim in
artifacts/circdist_gross_phicert_20260822.md section 2.4.  This session's |V| = 12 stratum search
is a sub-query of that decision, so it MUST return zero weight-<=10 configurations on M_cand's
orders.  That is the encoding validation.
"""
import itertools, sys
import core2 as C

# phicert section 2.4, verbatim.  slots 0,1,2 = left-half neighbours, 3,4,5 = right-half.
MCAND_Z = {0: (0, 1, 2, 4, 3, 5), 1: (0, 1, 2, 5, 3, 4), 2: (1, 2, 0, 5, 3, 4)}   # triple (1,2,62)
MCAND_X = {0: (0, 2, 1, 5, 3, 4), 1: (0, 1, 2, 3, 4, 5), 2: (0, 1, 2, 5, 3, 4)}   # triple (14,0,2)


def orders_from_slotorders(slotorders, kind):
    """kind 'X' -> Xslots (A-monomial left, B-monomial right); 'Z' -> Zslots."""
    slots = C.Xslots if kind == 'X' else C.Zslots
    return [[slots[g][s] for s in slotorders[C.cls(g)]] for g in range(C.NG)]


def hot_report(orders, pool, tag):
    """the corrected |V| = 12 disqualifier, computed from ORDERS only."""
    suf3 = 0
    hot = {}
    for a, o in enumerate(orders):
        m_s3, m_s2, m_p2 = C.msk(o[3:]), C.msk(o[4:]), C.msk(o[:2])
        for V in pool:
            if V & m_s3 == m_s3:
                suf3 += 1
            if V & m_s2 == m_s2:
                hot.setdefault(V, []).append((a, m_s2, '2suf'))
            if V & m_p2 == m_p2:
                hot.setdefault(V, []).append((a, m_p2, '2pre'))
    npair = 0
    ex = []
    for V, l in hot.items():
        for (a1, m1, k1), (a2, m2, k2) in itertools.combinations(l, 2):
            if not (m1 & m2):
                npair += 1
                if len(ex) < 1:
                    ex.append((k1, a1, k2, a2))
    n2s = sum(1 for l in hot.values() for x in l if x[2] == '2suf')
    n2p = sum(1 for l in hot.values() for x in l if x[2] == '2pre')
    print("  %-34s 3-suffix-in-V %3d | 2-suffix-in-V %4d | 2-prefix-in-V %4d | DISJOINT gain-1 "
          "pairs %4d %s" % (tag, suf3, n2s, n2p, npair, ex if ex else ''))
    return suf3 + npair


class OrderSector:
    """the parts of core2.Sector that depend only on the orders (enough for the d_ext stratum)."""

    def __init__(self, orders, mirror):
        self.order = orders
        self.hchk = C.Zchk if mirror else C.Xchk
        self.hm = [C.msk(c) for c in self.hchk]


def strat_from_orders(orders, pool, mirror, W, jmax=3):
    sec = OrderSector(orders, mirror)
    opts = [[(C.opt_mask(sec, a, P), n, K) for (K, P, n, cn) in C.OPTS] for a in range(C.NG)]
    need = 12 - W
    total = 0
    firstex = []
    for V in pool:
        cand = []
        for a in range(C.NG):
            if not (sec.hm[a] & V):
                continue
            for (m, n, K) in opts[a]:
                cand.append((C.popc(m & V) - n, a, m, n, K))
        cand.sort(key=lambda x: -x[0])
        Ln = len(cand)
        res = []

        def rec(start, depth, gsum, Ku, D, chosen):
            if chosen and Ku + C.popc(V ^ D) <= W:
                res.append((Ku + C.popc(V ^ D), list(chosen)))
            if depth == jmax:
                return
            for i in range(start, Ln):
                g, a, m, n, K = cand[i]
                if Ku + n > W:
                    continue
                if gsum + g * (jmax - depth) < need:
                    break
                chosen.append((a, K))
                rec(i + 1, depth + 1, gsum + g, Ku + n, D ^ m, chosen)
                chosen.pop()

        rec(0, 0, 0, 0, 0, [])
        total += len(res)
        if res and not firstex:
            firstex = res[:1]
    return total, firstex


(pz, _, _), (px, _, _) = C.pools()
(tX, tZ), T = C.load_candidate()

print("=" * 96)
print("KNOWN CELL: the campaign's own reconstructed [SBB26] candidate M_cand")
print("  Z-sector order-class triple (1,2,62), X-sector (14,0,2), phi = a+b")
print("  campaign verdict (990/990 UNSAT at W = 10): d_ext = 11 in BOTH sectors")
print("=" * 96)
oZm = orders_from_slotorders(MCAND_Z, 'Z')   # Z-triple -> Z-CHECK orders -> X-memory hooks
oXm = orders_from_slotorders(MCAND_X, 'X')   # X-triple -> X-CHECK orders -> Z-memory hooks
print("  M_cand Z-check 0 CNOT order (qubits):", oZm[0], " (phicert prints 3,6,12,73,90,74)")
print("  M_cand X-check 0 CNOT order (qubits):", oXm[0], " (phicert prints 54,4,5,132,75,138)")
print()
hot_report(oXm, pz, "M_cand  Z-memory (X-check hooks)")
hot_report(oZm, px, "M_cand  X-memory (Z-check hooks)")
for W in (10, 11):
    nz, ez = strat_from_orders(oXm, pz, False, W)
    nx, ex = strat_from_orders(oZm, px, True, W)
    print("  M_cand  |V|=12 stratum, j<=3, W=%d :  Z-memory %d configurations, X-memory %d "
          "configurations   %s" % (W, nz, nx, ('' if W == 10 else 'ex ' + str(ez[:1] + ex[:1]))))

print()
print("=" * 96)
print("THE WAVE-37 CANDIDATE, same report, for contrast")
print("=" * 96)
secZ = C.Sector(tX, tZ, mirror=False)
secX = C.Sector(tX, tZ, mirror=True)
hot_report(secZ.order, pz, "wave-37 cand  Z-memory")
hot_report(secX.order, px, "wave-37 cand  X-memory")

