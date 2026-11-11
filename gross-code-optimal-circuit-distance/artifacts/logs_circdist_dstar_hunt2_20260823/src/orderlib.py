"""Order-only helpers shared by the stratum scripts (extracted verbatim from v2_knowncell.py)."""
import itertools
import core2 as C


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


