"""Verify, element by element, that the translation stabiliser S of a tiled assignment acts on the
extended code as a weight-preserving automorphism, and that column_orbits' orbit structure is the
true orbit structure of that action.

For every g = (a,b) in S with data permutation dp and check permutation cp we check
  (1) g permutes the ROWS of H_X as a set, and the rows of H_Z as a set
      => ker(H_X), ker(H_Z), rowspace(H_X), rowspace(H_Z) are all preserved, so g preserves both
         "zero syndrome" and "non-trivial logical";
  (2) dp(r_k(c)) = r_k(cp(c)) for every check c and residual index k
      => g maps extended-code column ('r',c,k) to ('r',cp(c),k) and ('d',j) to ('d',dp[j]),
         bijectively and weight-preservingly.
Together: x -> g.x is a weight-preserving bijection of the solution set of every (W,K,Ew) cell.
"""
import numpy as np, itertools, sys, json
from gross import HX, HZ, N, NG, ELL, EM, gidx
from sched import make_phi
from cert import tiled_orders
import dext, dext2


def dperm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
            p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p


def cperm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p


def rows_permuted(H, dp):
    """H[i] pushed forward by dp must again be a row of H, bijectively."""
    keys = {H[i].tobytes(): i for i in range(H.shape[0])}
    img = set()
    for i in range(H.shape[0]):
        v = np.zeros(N, np.uint8)
        v[dp[np.nonzero(H[i])[0]]] = 1
        k = v.tobytes()
        if k not in keys:
            return False
        img.add(keys[k])
    return len(img) == H.shape[0]


phi = make_phi(1, 1)
out = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    S, orbits = dext2.column_orbits(phi, tr)
    orders, _ = tiled_orders(sector, phi, tr)
    res = dext.residual_sets(orders)
    badrow = badres = 0
    for (a, b) in S:
        dp, cp = dperm(a, b), cperm(a, b)
        if not (rows_permuted(HX, dp) and rows_permuted(HZ, dp)):
            badrow += 1
        for c in range(NG):
            for k in range(3):
                if tuple(sorted(int(dp[q]) for q in res[c][k])) != tuple(sorted(res[int(cp[c])][k])):
                    badres += 1
    # orbit structure, recomputed independently from the verified action
    cols = [('d', j) for j in range(N)] + [('r', c, k) for c in range(NG) for k in range(3)]
    seen = set(); orbs = []
    for col in cols:
        if col in seen:
            continue
        o = set()
        for (a, b) in S:
            dp, cp = dperm(a, b), cperm(a, b)
            o.add(('d', int(dp[col[1]])) if col[0] == 'd' else ('r', int(cp[col[1]]), col[2]))
        seen |= o; orbs.append(sorted(o))
    same = (sorted(tuple(sorted(o)) for _, o in orbits) == sorted(tuple(o) for o in orbs))
    rorb = [o for o in orbs if o[0][0] == 'r']
    print(f"sector {sector} triple {tr}: |S| = {len(S)}; row-permutation failures {badrow}; "
          f"residual-equivariance failures {badres}; orbits {len(orbs)} "
          f"(residual orbits {len(rorb)}, sizes {sorted({len(o) for o in orbs})}); "
          f"matches column_orbits: {same}")
    out[sector] = dict(nS=len(S), badrow=badrow, badres=badres, norb=len(orbs),
                       nres_orb=len(rorb), same=bool(same))
json.dump(out, open("stabcheck.json", "w"), indent=1)
