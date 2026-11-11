"""THE REPRICING EXPERIMENT.

Wave 37 annealed the 36-slot three-colour-tiled time family against
    1000*(MC) + 20*(weight-<=10 configurations) + 10*(horizontal hooks) + (repair-0 count)
and reached cost 0 -- but its "weight-<=10 configurations" term was the INCOMPLETE disqualifier
(3-suffix-in-V and disjoint 2-SUFFIX pairs only).  Re-run the same anneal with the CORRECTED term,
which also charges the 2-PREFIX {i1,i2} (= the 4-suffix modulo the stabiliser supp(a)).

Question: is a three-colour-tiled schedule with
    (MC) clean  AND  corrected-d_eff-<=10 count 0  AND  no horizontal hook
reachable at all?  Wave 37's answer (with the wrong filter) was yes.  With the right filter this
is the live question, and it is the thing that prices the D* = 12 direction.
"""
import collections, itertools, json, random, sys, time
import core2 as C

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
NPROP = int(sys.argv[2]) if len(sys.argv) > 2 else 120000
(pz, _, _), (px, _, _) = C.pools()

# ---------- precomputed pair / triple -> logical-index lists, per sector -------------------
def index_sector(chks, pool):
    pidx, tidx = {}, {}
    for a in range(C.NG):
        sup = chks[a]
        for pr in itertools.combinations(sup, 2):
            m = C.msk(pr)
            pidx[(a, pr)] = [i for i, V in enumerate(pool) if V & m == m]
        for tr in itertools.combinations(sup, 3):
            m = C.msk(tr)
            l = [i for i, V in enumerate(pool) if V & m == m]
            if l:
                tidx[(a, tr)] = l
    return pidx, tidx


t0 = time.time()
IDXZ = index_sector(C.Xchk, pz)      # Z-memory: hooks on X-checks
IDXX = index_sector(C.Zchk, px)      # X-memory: hooks on Z-checks
print("pair/triple index built in %.0fs; nonempty triples: Z %d/1440, X %d/1440"
      % (time.time() - t0, len(IDXZ[1]), len(IDXX[1])))


def dext10_count(orders, idx):
    """corrected |V|=12 disqualifier count: 3-suffix-in-V hits + disjoint gain-1 pairs."""
    pidx, tidx = idx
    n = 0
    hot = collections.defaultdict(list)
    for a, o in enumerate(orders):
        n += len(tidx.get((a, tuple(sorted(o[3:]))), ()))
        for pr in (tuple(sorted(o[4:])), tuple(sorted(o[:2]))):
            m = C.msk(pr)
            for vi in pidx[(a, pr)]:
                hot[vi].append(m)
    for vi, ms in hot.items():
        if len(ms) < 2:
            continue
        for m1, m2 in itertools.combinations(ms, 2):
            if not (m1 & m2):
                n += 1
    return n


def tiled(t):
    XL = [t[3 * c:3 * c + 3] for c in range(3)]
    XR = [t[9 + 3 * c:12 + 3 * c] for c in range(3)]
    ZL = [t[18 + 3 * c:21 + 3 * c] for c in range(3)]
    ZR = [t[27 + 3 * c:30 + 3 * c] for c in range(3)]
    tX, tZ = {}, {}
    for g in range(C.NG):
        c = C.cls(g)
        for i, m in enumerate(C.Amon):
            tX[(g, C.gadd(g, m))] = XL[c][i]
        for j, m in enumerate(C.Bmon):
            tX[(g, C.NG + C.gadd(g, m))] = XR[c][j]
        for j, m in enumerate(C.Bmon):
            tZ[(C.gadd(g, (-m[0], -m[1])), g)] = ZL[c][j]
        for i, m in enumerate(C.Amon):
            tZ[(C.NG + C.gadd(g, (-m[0], -m[1])), g)] = ZR[c][i]
    return tX, tZ


def cost(t, detail=False):
    tX, tZ = tiled(t)
    mc = len(C.mc_violations(tX, tZ))
    secZ = C.Sector(tX, tZ, mirror=False)
    secX = C.Sector(tX, tZ, mirror=True)
    d10 = dext10_count(secZ.order, IDXZ) + dext10_count(secX.order, IDXX)
    horiz = 0
    for sec in (secZ, secX):
        for a in range(C.NG):
            for l in (2, 3, 4):
                if sec.classify(a, sec.suffix(a, l)) in ('trivial', 'horizontal'):
                    horiz += 1
    gint = C.interleave_stats(tX, tZ)[2]
    c = 1000 * mc + 50 * d10 + 10 * horiz + (0 if gint else 500)
    if detail:
        return c, dict(mc=mc, dext10=d10, horiz=horiz, glob_int=gint)
    return c


rng = random.Random(SEED)
t = list(range(36))
rng.shuffle(t)
cur = cost(t)
best, bestt = cur, list(t)
T0, T1 = 40.0, 0.5
t0 = time.time()
for it in range(NPROP):
    if best == 0:
        break
    i, j = rng.randrange(36), rng.randrange(36)
    if i == j:
        continue
    t[i], t[j] = t[j], t[i]
    c = cost(t)
    Temp = T0 * (T1 / T0) ** (it / NPROP)
    if c <= cur or rng.random() < pow(2.718281828, -(c - cur) / Temp):
        cur = c
        if c < best:
            best, bestt = c, list(t)
    else:
        t[i], t[j] = t[j], t[i]
    if it % 4000 == 0:
        print("  seed %d it %6d  cur %6d  best %6d  (%.0fs)" % (SEED, it, cur, best, time.time() - t0))
        sys.stdout.flush()
c, d = cost(bestt, detail=True)
print("SEED %d  BEST COST %d  %s  t=%s  (%.0fs, %d proposals)"
      % (SEED, c, d, bestt, time.time() - t0, it))
json.dump({'seed': SEED, 'cost': c, 'detail': d, 't': bestt}, open('anneal_seed%d.json' % SEED, 'w'))
