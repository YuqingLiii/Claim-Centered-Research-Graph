"""GROUND-TRUTH VALIDATION of the lift decider on a small code.

Builds the actual R-round memory circuit DEM of a small CSS code from the frozen fault
inventory, computes d_circ by exhaustive minimum-weight search, computes d_eff and
repair(gamma) from ONE round, and checks the criterion
        d_circ = d_eff  <=>  some minimum-weight gamma has repair(gamma) = 0
plus the sandwich  |g| + min(repair,2) <= d_circ_contribution <= |g| + repair.
"""
import itertools, sys, random
from lift import CSS, Schedule, Sector, popc

random.seed(20260823)


# ---------------------------------------------------------------- residual columns
def residuals(sec):
    """distinct residuals E != empty, with their s, lambda, and voltage spectrum U(E)."""
    css = sec.css
    out = {}                        # frozenset(E) -> [s, U set]
    for q in range(css.n):
        key = frozenset([q])
        out.setdefault(key, [sec.s_of([q]), set()])
        for u in sec.Uq[q]:
            out[key][1].add(u)
    for a in range(len(sec.hook_checks)):
        w = len(sec.order[a])
        for k in range(1, w + 1):           # suffix length k  (k=w is the full support)
            S = sec.hook(a, k)
            key = frozenset(S)
            out.setdefault(key, [sec.s_of(S), set()])
            out[key][1].add(sec.u_hook(a, S))
    return out


def lam_of(E, Lmask):
    return popc(Lmask & sum(1 << q for q in E)) % 2


# ---------------------------------------------------------------- d_eff
def d_eff(res, Lmask, wmax=6):
    """min |gamma| with sum s = 0 and lambda != 0."""
    keys = list(res.keys())
    cols = [(res[k][0], lam_of(k, Lmask)) for k in keys]
    best = None
    bestg = []
    for w in range(1, wmax + 1):
        for comb in itertools.combinations(range(len(cols)), w):
            s = 0
            l = 0
            for i in comb:
                s ^= cols[i][0]
                l ^= cols[i][1]
            if s == 0 and l == 1:
                if best is None:
                    best = w
                if w == best:
                    bestg.append([keys[i] for i in comb])
        if best is not None:
            return best, bestg
    return None, []


# ---------------------------------------------------------------- repair (general)
def repair(res, gamma, window=4):
    """Definition 5.2, exhaustive over round assignments in a window and voltages."""
    items = [(res[E][0], sorted(res[E][1])) for E in gamma]
    w = len(items)
    best = 10 ** 9
    for rounds in itertools.product(range(window), repeat=w):
        if min(rounds) != 0:
            continue
        # C = B/(1+x): c(r) = sum_{r_i <= r} s_i ; xC has coefficient c(r-1) at x^r
        cacc = {}
        acc = 0
        for r in range(window + 1):
            acc ^= 0
            for (s, _), ri in zip(items, rounds):
                pass
            cacc[r] = None
        # recompute properly
        c = [0] * (window + 2)
        run = 0
        for r in range(window + 2):
            for (s, _), ri in zip(items, rounds):
                if ri == r:
                    run ^= s
            c[r] = run
        for volts in itertools.product(*[u for (_, u) in items]):
            tot = 0
            for r in range(window + 2):
                A = 0
                for v, ri in zip(volts, rounds):
                    if ri == r:
                        A ^= v
                xc = c[r - 1] if r >= 1 else 0
                tot += popc(A ^ xc)
                if tot >= best:
                    break
            if tot < best:
                best = tot
                if best == 0:
                    return 0
    return best


# ---------------------------------------------------------------- brute force d_circ
def d_circ_bruteforce(sec, res, Lmask, R, wmax=4):
    """columns of the R-round DEM: (f,r) -> [u]_r + [u+s]_{r+1} over B x {0..R}."""
    nd = sec.ndet
    cols = []
    for E, (s, U) in res.items():
        lam = lam_of(E, Lmask)
        for u in U:
            for r in range(R):
                v = 0
                for b in range(nd):
                    if (u >> b) & 1:
                        v |= 1 << (b * (R + 1) + r)
                    if ((u ^ s) >> b) & 1:
                        v ^= 1 << (b * (R + 1) + r + 1)
                cols.append((v, lam))
    # empty-residual faults: (E=empty, u=e_b, s=0)  -- classical flips / Z-ancilla X
    for b in range(nd):
        for r in range(R):
            v = (1 << (b * (R + 1) + r)) | (1 << (b * (R + 1) + r + 1))
            cols.append((v, 0))
    cols = list(set(cols))
    # meet in the middle: min |F| with xor 0 and lam 1, |F| <= wmax
    half = wmax // 2
    tab = {}
    for w in range(0, half + 1):
        for comb in itertools.combinations(range(len(cols)), w):
            v = 0
            l = 0
            for i in comb:
                v ^= cols[i][0]
                l ^= cols[i][1]
            cur = tab.get((v, l))
            if cur is None or w < cur:
                tab[(v, l)] = w
    best = 10 ** 9
    for w in range(0, wmax - half + 1):
        for comb in itertools.combinations(range(len(cols)), w):
            v = 0
            l = 0
            for i in comb:
                v ^= cols[i][0]
                l ^= cols[i][1]
            o = tab.get((v, l ^ 1))
            if o is not None and o + w < best:
                best = o + w
    return best if best < 10 ** 9 else None


# ---------------------------------------------------------------- instances
def steane():
    ch = [[3, 4, 5, 6], [1, 2, 5, 6], [0, 2, 4, 6]]
    return CSS(7, ch, ch), 0b0111000 | 0  # placeholder logical, fixed below


def make_sched(css, kind, rng=None):
    """kind: 'nonint-X' (X block first), 'nonint-Z', 'random-mc' (legal, random, MC filtered)"""
    tX, tZ = {}, {}
    if kind in ('nonint-X', 'nonint-Z'):
        t = 0
        first = css.Xchecks if kind == 'nonint-X' else css.Zchecks
        for i, c in enumerate(first):
            for q in c:
                if kind == 'nonint-X':
                    tX[(i, q)] = t
                else:
                    tZ[(q, i)] = t
                t += 1
        for i, c in enumerate(css.Zchecks if kind == 'nonint-X' else css.Xchecks):
            for q in c:
                if kind == 'nonint-X':
                    tZ[(q, i)] = t
                else:
                    tX[(i, q)] = t
                t += 1
        return Schedule(css, tX, tZ)
    # random serial order over all gates (always legal: one gate per step)
    gates = [('X', i, q) for i, c in enumerate(css.Xchecks) for q in c] + \
            [('Z', i, q) for i, c in enumerate(css.Zchecks) for q in c]
    rng.shuffle(gates)
    for t, g in enumerate(gates):
        if g[0] == 'X':
            tX[(g[1], g[2])] = t
        else:
            tZ[(g[2], g[1])] = t
    return Schedule(css, tX, tZ)


def check_serial(css, rng):
    """serial CHECK order: every check does all its CNOTs consecutively -> always (MC)."""
    tX, tZ = {}, {}
    order = [('X', i) for i in range(css.nA)] + [('Z', i) for i in range(css.nB)]
    rng.shuffle(order)
    t = 0
    for typ, i in order:
        qs = list(css.Xchecks[i] if typ == 'X' else css.Zchecks[i])
        rng.shuffle(qs)
        for q in qs:
            if typ == 'X':
                tX[(i, q)] = t
            else:
                tZ[(q, i)] = t
            t += 1
    return Schedule(css, tX, tZ)


if __name__ == '__main__':
    ch = [[3, 4, 5, 6], [1, 2, 5, 6], [0, 2, 4, 6]]
    css = CSS(7, ch, ch)
    assert css.commutes()
    # Z_L: a weight-3 representative of the Z-logical class (in ker(H) \ rowspace(H))
    # Hamming code words of weight 3: e.g. {0,1,2}? check parity with all three checks.
    cands = []
    for comb in itertools.combinations(range(7), 3):
        m = sum(1 << q for q in comb)
        if all(popc(m & c) % 2 == 0 for c in css.Zmask):
            cands.append(m)
    Lmask = cands[0]
    print("logical rep (weight 3):", bin(Lmask), " count of wt-3 codewords:", len(cands))

    rng = random.Random(7)
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    NRAND = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
    rows = []
    tested = 0
    kinds = ['nonint-X', 'nonint-Z'] + ['serial'] * 6 + ['rand'] * NRAND
    nmc = 0
    ngappred = 0
    for ki, kind in enumerate(kinds):
        if kind == 'serial':
            sch = check_serial(css, rng)
        elif kind == 'rand':
            sch = make_sched(css, 'random-mc', rng)
        else:
            sch = make_sched(css, kind)
        if not sch.legal():
            continue
        mcv = sch.mc_violations()
        if mcv:
            continue
        nmc += 1
        sec0 = Sector(css, sch)
        res0 = residuals(sec0)
        de0, gam0 = d_eff(res0, Lmask, wmax=5)
        rp0 = [repair(res0, g, window=4) for g in gam0]
        predgap = (0 not in rp0)
        if predgap:
            ngappred += 1
        if kind == 'rand' and tested >= 20 and not predgap:
            continue
        if kind == 'rand' and predgap and tested >= 40:
            continue
        sec = Sector(css, sch)
        res = residuals(sec)
        de, gammas = d_eff(res, Lmask, wmax=5)
        reps = [repair(res, g, window=4) for g in gammas]
        pred_eq = (0 in reps)
        dc = d_circ_bruteforce(sec, res, Lmask, R, wmax=min(de + 2, 5))
        ok = (dc == de) == pred_eq
        lb = de + min(min(reps), 2)
        ub = de + min(reps)
        sand = (lb <= dc <= ub)
        tested += 1
        rows.append((kind, sch.globally_interleaved(), sch.interleaved_pairs(), de,
                     sorted(set(reps)), dc, ok, sand))
        print("%-9s glob-int=%-5s pairint=%2d  d_eff=%d  repairs=%s  d_circ=%s  "
              "criterion_ok=%s sandwich_ok=%s"
              % (kind, sch.globally_interleaved(), sch.interleaved_pairs(), de,
                 sorted(set(reps)), dc, ok, sand))
    print()
    print("draws=%d  legal+MC=%d  predicted-gap(min repair>=1)=%d" % (len(kinds), nmc, ngappred))
    print("TESTED %d legal+MC schedules at R=%d : criterion agreements %d/%d, sandwich %d/%d"
          % (tested, R, sum(1 for r in rows if r[6]), len(rows),
             sum(1 for r in rows if r[7]), len(rows)))
    gaps = [r for r in rows if r[5] != r[3]]
    print("instances with a genuine completion gap d_circ > d_eff:", len(gaps))
    for r in gaps:
        print("   ", r)
