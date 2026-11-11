"""Full stage-2 audit of a corrected-filter tiled schedule: the wave-38 replacement candidate."""
import collections, itertools, json, sys, time
import core2 as C
from orderlib import OrderSector

T = json.load(open(sys.argv[1]))['t'] if sys.argv[1].endswith('.json') else json.loads(sys.argv[1])
(pz, _, _), (px, _, _) = C.pools()
tX, tZ = C.build_tiled(T)
print("t =", T)
print("legal =", C.legal(tX, tZ), " (MC) violations =", len(C.mc_violations(tX, tZ)))
pi, si, gi_ = C.interleave_stats(tX, tZ)
print("overlap-interleaved %d/648 ; whole-check interleaved %d/648 ; globally interleaved %s"
      % (pi, si, gi_))


def family(sec, pool, W, jmax=3):
    opts = [[(C.opt_mask(sec, a, P), n, K) for (K, P, n, cn) in C.OPTS] for a in range(C.NG)]
    need = 12 - W
    fam = []
    for V in pool:
        cand = []
        for a in range(C.NG):
            if not (C.msk(sec.hchk[a]) & V):
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


for lab, mir, pool in (('Zmem', False, pz), ('Xmem', True, px)):
    sec = C.Sector(tX, tZ, mirror=mir)
    kinds = {l: dict(collections.Counter(sec.classify(a, sec.suffix(a, l)) for a in range(C.NG)))
             for l in (2, 3, 4, 5)}
    print("\n%s hook classification by suffix length: %s" % (lab, kinds))
    t0 = time.time()
    f10 = family(sec, pool, 10)
    print("  |V|=12 stratum, j<=3, W=10: %d configurations   -> d_eff %s 11 in this stratum  (%.0fs)"
          % (len(f10), '<= 10, DEAD' if f10 else '= 11 (|V|=12 part clean)', time.time() - t0))
    if f10:
        continue
    t0 = time.time()
    f11 = family(sec, pool, 11)
    n0 = mr0 = 0
    firsthit = None
    for (V, ch) in f11:
        hooks, D = [], 0
        for (a, K) in ch:
            for l in K:
                S = sec.suffix(a, l)
                hooks.append((a, S))
                D ^= C.msk(S)
        singles = C.bits(V ^ D)
        if C.sameround_repair0(sec, hooks, singles) is not None:
            n0 += 1
            if firsthit is None:
                firsthit = (C.bits(V), ch)
        elif C.multiround_repair0(sec, hooks, singles, maxg=2) is not None:
            mr0 += 1
    print("  minimum-weight (11) |V|=12 family: %d gammas ; SAME-ROUND repair-0 on %d ; "
          "2-group MULTI-ROUND repair-0 on %d more   (%.0fs)" % (len(f11), n0, mr0, time.time() - t0))
    if firsthit:
        print("    first repair-0 gamma:", firsthit)
    else:
        print("    -> every minimum-weight gamma in this family has repair >= 1")
