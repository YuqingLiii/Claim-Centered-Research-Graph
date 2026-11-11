"""Replacement-candidate hunt built on LEMMA D.

Fix M_cand's within-check ORDERS (order-class triples Z = (1,62,2), X = (14,2,0) in this build's
labelling; the campaign certified d_ext = 11 for that orbit with 990 all-UNSAT sub-queries).  By
Lemma D every legal + (MC) re-timing of those orders has the SAME d_eff = 11, in both sectors, for
free.  Only the repair side then remains, and repair DOES depend on the times.

So: enumerate the minimum-weight (weight-11) effective-logical family ONCE -- it too depends only
on the orders -- and then sweep re-timings, rejecting any schedule in which some minimum-weight
gamma admits a same-round repair-0 certificate.

SCOPE: the weight-11 family enumerated here is the complete |V| = 12, j <= 3 stratum.  The
|V| >= 14 minimum-weight shapes are NOT enumerated (this is wave 37's section 6.2(2) gap, unchanged);
a surviving schedule is therefore a CANDIDATE, never a witness.
"""
import itertools, json, os, sys, time
import core2 as C
from orderlib import orders_from_slotorders, strat_from_orders, OrderSector
_argv = sys.argv; sys.argv = ['v3_retime', '1,62,2', '14,2,0']   # v3_retime reads argv at import
from v3_retime import (CLS, iXL, iXR, iZL, iZR, CHAINS, mc_ok, build, random_linext, oZ, oX)
sys.argv = _argv

NTRY = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
(pz, _, _), (px, _, _) = C.pools()


def enumerate_family(orders, pool, mirror, W=11, jmax=3):
    """every weight-W configuration with |V| = 12: (V, [(check, suffix-lengths)...])."""
    sec = OrderSector(orders, mirror)
    opts = [[(C.opt_mask(sec, a, P), n, K) for (K, P, n, cn) in C.OPTS] for a in range(C.NG)]
    need = 12 - W
    fam = []
    for V in pool:
        cand = []
        for a in range(C.NG):
            if not (sec.hm[a] & V):
                continue
            for (m, n, K) in opts[a]:
                cand.append((C.popc(m & V) - n, a, m, n, K))
        cand.sort(key=lambda x: -x[0])
        Ln = len(cand)

        def rec(start, depth, gsum, Ku, D, chosen):
            if chosen and Ku + C.popc(V ^ D) <= W:
                fam.append((V, list(chosen)))
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
    return fam


t0 = time.time()
FAMZ = enumerate_family(oX, pz, False)     # Z-memory: hooks on X-checks
FAMX = enumerate_family(oZ, px, True)      # X-memory: hooks on Z-checks
print("minimum-weight (11) |V|=12 family for M_cand's orders:  Z-memory %d, X-memory %d   (%.0fs)"
      % (len(FAMZ), len(FAMX), time.time() - t0))


def repair_clean(sec, fam):
    """False as soon as one gamma admits a same-round repair-0 certificate."""
    for (V, ch) in fam:
        hooks, D = [], 0
        for (a, K) in ch:
            for l in K:
                S = sec.suffix(a, l)
                hooks.append((a, S))
                D ^= C.msk(S)
        singles = C.bits(V ^ D)
        if C.sameround_repair0(sec, hooks, singles) is not None:
            return False
    return True


if __name__ == '__main__':
    import random
    rng = random.Random(777)
    t0 = time.time()
    nmc = 0
    survivors = []
    tested = 0
    for it in range(NTRY):
        t = random_linext(rng)
        if not mc_ok(t):
            continue
        nmc += 1
        tX, tZ = build(t)
        pi, si, gint = C.interleave_stats(tX, tZ)
        if not gint:
            continue
        tested += 1
        secZ = C.Sector(tX, tZ, mirror=False)
        if not repair_clean(secZ, FAMZ):
            continue
        secX = C.Sector(tX, tZ, mirror=True)
        if not repair_clean(secX, FAMX):
            continue
        survivors.append((pi, si, list(t)))
        print("  SURVIVOR: overlap-interleaved %d/648  whole-check %d/648  t=%s" % (pi, si, t))
        sys.stdout.flush()
    print("re-timings tried %d ; legal+(MC) %d ; globally interleaved and repair-tested %d ; "
          "survivors %d   (%.0fs)" % (NTRY, nmc, tested, len(survivors), time.time() - t0))
    if survivors:
        survivors.sort(key=lambda s: -s[0])
        json.dump(survivors[:20], open('newcand_survivors.json', 'w'))
        print("best survivor: overlap-interleaved %d/648, whole-check %d/648" % survivors[0][:2])
