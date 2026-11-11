"""Exact |V| = 12 stratum of the d_ext decision for the wave-37 candidate.

For a fixed nontrivial logical V, a residual configuration is
    hooks: for each hook check a a set K_a of suffix LENGTHS (subset of {2,3,4,5}, lemmas R1/R2),
           contributing C_a = XOR of those suffixes, n_a = |K_a| faults;
    singles: T = V XOR D  where D = XOR_a C_a, one fault per qubit.
    cost(config) = sum_a n_a + |V XOR D|.
d_ext = min over nontrivial logicals V and configurations of cost.  This module decides the
|V| = 12 stratum, which is COMPLETE because the 1884-element weight-12 pool per sector is the
complete set of weight-12 nontrivial logicals (wave 36 exhaustive enumeration, re-expanded here).

Exact cost identity used for pruning (rho_a = |C_a cap V|):
    cost = 12 + sum_a (n_a - rho_a) + loss_in + gain_out,     loss_in, gain_out >= 0,
so a configuration of cost <= W must satisfy  sum_a (rho_a - n_a) >= 12 - W.
Per check the "V-gain" gamma_a = rho_a - n_a is at most 2 (Bound 1: |V cap supp(a)| <= 3), and
gamma_a <= 2*n_a, which gives the admissible pruning bound used in the search.

SCOPE of this search: at most JMAX distinct contributing hook checks, and only checks a with
|V cap supp(a)| >= 1.  Both restrictions are stated in the artifact; nothing is claimed beyond.
"""
import itertools, json, sys, time
import core2 as C

JMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 3
W = int(sys.argv[2]) if len(sys.argv) > 2 else 10
SECT = sys.argv[1] if len(sys.argv) > 1 else 'Z'


def build_options(sec):
    """per hook check: list of (mask, n, positions) for the 7 drop-lemma-surviving options."""
    out = []
    for a in range(C.NG):
        lst = []
        for (K, P, n, cn) in C.OPTS:
            lst.append((C.opt_mask(sec, a, P), n, K, P))
        out.append(lst)
    return out


def search_V(sec, opts, V, W, jmax):
    """all configurations with cost <= W for this V.  Returns list of (cost, [(a,K)...])."""
    # option list restricted to checks meeting V
    cand = []
    for a in range(C.NG):
        if not (sec.hm[a] & V):
            continue
        for (m, n, K, P) in opts[a]:
            rho = C.popc(m & V)
            cand.append((rho - n, a, m, n, K))
    cand.sort(key=lambda x: -x[0])
    need = 12 - W
    res = []
    L = len(cand)

    def rec(start, depth, gsum, K_used, D, chosen):
        # exact cost of the current (already complete) configuration
        cost = K_used + C.popc(V ^ D)
        if cost <= W and chosen:
            res.append((cost, list(chosen)))
        if depth == jmax:
            return
        for i in range(start, L):
            g, a, m, n, K = cand[i]
            if K_used + n > W:
                continue
            # admissible bound: every further check adds gamma <= 2 and cand is gamma-sorted
            if gsum + g * (jmax - depth) < need:
                break
            chosen.append((a, K))
            rec(i + 1, depth + 1, gsum + g, K_used + n, D ^ m, chosen)
            chosen.pop()

    rec(0, 0, 0, 0, 0, [])
    return res


def main():
    (tX, tZ), T = C.load_candidate()
    (pz, _, _), (px, _, _) = C.pools()
    mir = (SECT == 'X')
    pool = px if mir else pz
    sec = C.Sector(tX, tZ, mirror=mir)
    opts = build_options(sec)
    t0 = time.time()
    hits = []
    nconf = 0
    for vi, V in enumerate(pool):
        r = search_V(sec, opts, V, W, JMAX)
        nconf += len(r)
        for (cost, ch) in r:
            hits.append((cost, vi, ch))
    print("sector=%s  W=%d  JMAX=%d  pool=%d  configurations found=%d  time=%.1fs"
          % (SECT, W, JMAX, len(pool), nconf, time.time() - t0))
    bycost = {}
    for (cost, vi, ch) in hits:
        bycost[cost] = bycost.get(cost, 0) + 1
    print("cost histogram:", dict(sorted(bycost.items())))
    if hits:
        mn = min(h[0] for h in hits)
        ex = [h for h in hits if h[0] == mn][:3]
        print("minimum cost in this stratum =", mn, " examples:", ex)
    out = sys.argv[4] if len(sys.argv) > 4 else None
    if out:
        json.dump([[c, vi, [[a, list(K)] for (a, K) in ch]] for (c, vi, ch) in hits],
                  open(out, 'w'))
        print("wrote", out)


if __name__ == '__main__':
    main()
