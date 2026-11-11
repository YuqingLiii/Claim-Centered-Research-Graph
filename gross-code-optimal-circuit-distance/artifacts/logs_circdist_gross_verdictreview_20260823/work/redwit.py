"""Validate the lex-minimality cut (c8)/(c9) of cert6.py on real weight-10 witnesses.

For every witness in logs/val.jsonl, iterate the drop step
    (E, R, d) -> (E, R \\ {r}, d xor r)   whenever it does not increase (weight, |R|) lex,
which must terminate (|R| strictly decreases each time).  The fixed point must
  * still be a valid solution of the same E, verified by dext.verify_witness,
  * still have weight <= 10,
  * satisfy (c8): d is disjoint from every used residual,
  * satisfy (c9): d is contained in E, and |E| = |d| + |rho| exactly,
and it tells us which cell (K, Ew) the lex-minimal representative of that witness lives in.
"""
import json
import numpy as np
from gross import N, NG
from sched import make_phi
from cert import tiled_orders
import dext

phi = make_phi(1, 1)
nbad = 0; n = 0
for line in open('logs/val.jsonl'):
    r0 = json.loads(line)
    if r0['verdict'] != 'SAT':
        continue
    sector, tr = r0['sector'], tuple(r0['triple'])
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    R = [tuple(x) for x in r0['R']]
    E = np.zeros(N, np.uint8); E[r0['E']] = 1
    D = np.zeros(N, np.uint8); D[r0['D']] = 1
    w0 = int(D.sum()) + len(R)
    import itertools as _it
    changed = True
    while changed:
        changed = False
        for m in range(1, len(R) + 1):
            for T in _it.combinations(R, m):
                D2 = D.copy()
                for (c, k) in T:
                    for q in ctx.res[c][k]:
                        D2[q] ^= 1
                if int(D2.sum()) + len(R) - m <= int(D.sum()) + len(R):
                    D = D2; R = [x for x in R if x not in T]; changed = True
                    break
            if changed:
                break
    info = dext.verify_witness(ctx, E, R, D, Hstab)
    rho = np.zeros(N, np.uint8)
    for (c, k) in R:
        for q in ctx.res[c][k]:
            rho[q] ^= 1
    c8 = all(D[q] == 0 for (c, k) in R for q in ctx.res[c][k])
    import itertools as _it
    sub_ok = True
    for m in range(1, len(R) + 1):
        for T in _it.combinations(R, m):
            s_ = np.zeros(N, np.uint8)
            for (c, k) in T:
                for q in ctx.res[c][k]:
                    s_[q] ^= 1
            if int(s_.sum()) < m + 1:
                sub_ok = False
    c9 = bool(((D & ~E) == 0).all())
    add = (int(E.sum()) == int(D.sum()) + int(rho.sum()))
    ok = (info['weight'] <= 10 and info['decomposition_ok'] and info['zero_syndrome']
          and info['nontrivial_logical'] and c8 and c9 and add and sub_ok)
    n += 1; nbad += (0 if ok else 1)
    print(f"{sector} {tr}: weight {w0} (K={len(r0['R'])}) -> lex-min weight {info['weight']} "
          f"(K={info['n_res']}), cell (K={info['n_res']}, Ew={info['Ewt']}); "
          f"(c8) {c8}  (c9) {c9}  |E|=|d|+|rho| {add}  "
          f"(c10/c11, all 2^K-1 subsets) {sub_ok}  valid {ok}")
print(f"\nreduced {n} witnesses, failures {nbad}")
