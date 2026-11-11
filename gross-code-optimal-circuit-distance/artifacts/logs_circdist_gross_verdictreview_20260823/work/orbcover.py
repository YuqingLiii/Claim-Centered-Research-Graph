"""Demonstrate the residual-orbit cover on real solutions, combinatorially (no solver).

For every weight-10 witness recorded in logs/val.jsonl (found by the UNRESTRICTED cell query), let
i be the least residual-orbit index the witness uses, pick a stabiliser element g carrying one of
its orbit-i columns to that orbit's representative, and check that g.(E,R,d) is again a solution of
the SAME cell (K, Ew) which uses the representative and no residual column of an orbit < i.  That
is exactly the claim the 9-way orbit split rests on, verified on real data.
"""
import json, sys
import numpy as np
from gross import N, NG, ELL, EM, gidx, Reducer
from sched import make_phi
from cert import tiled_orders
import dext, dext2


def dperm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b); p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p


def cperm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p


phi = make_phi(1, 1)
nchecked = nbad = 0
for line in open('logs/val.jsonl'):
    r = json.loads(line)
    if r['verdict'] != 'SAT':
        continue
    sector = r['sector']; tr = tuple(r['triple'])
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    S, orbits = dext2.column_orbits(phi, tr)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    oidx = {}
    for i, (rep, orb) in enumerate(rorb):
        for col in orb:
            oidx[col] = i
    R = [(a, b) for a, b in r['R']]
    E = np.zeros(N, np.uint8); E[r['E']] = 1
    D = np.zeros(N, np.uint8); D[r['D']] = 1
    used = sorted({oidx[('r', c, k)] for (c, k) in R})
    i0 = used[0]
    rep = rorb[i0][0]
    src = next((c, k) for (c, k) in R if oidx[('r', c, k)] == i0)
    g = next(gg for gg in S if (int(cperm(*gg)[src[0]]), src[1]) == (rep[1], rep[2]))
    dp, cp = dperm(*g), cperm(*g)
    E2 = np.zeros(N, np.uint8); E2[dp[np.nonzero(E)[0]]] = 1
    D2 = np.zeros(N, np.uint8); D2[dp[np.nonzero(D)[0]]] = 1
    R2 = [(int(cp[c]), k) for (c, k) in R]
    info = dext.verify_witness(ctx, E2, R2, D2, Hstab)
    used2 = sorted({oidx[('r', c, k)] for (c, k) in R2})
    ok = (info['weight'] == r['info']['weight'] and info['Ewt'] == r['info']['Ewt']
          and info['decomposition_ok'] and info['zero_syndrome'] and info['nontrivial_logical']
          and (rep[1], rep[2]) in [(c, k) for (c, k) in R2] and used2 == used
          and min(used2) == i0)
    nchecked += 1; nbad += (0 if ok else 1)
    print(f"{sector} {tr}: witness uses residual orbits {used}; g = {g} maps it to a solution "
          f"using rep {rep}; same cell (K={info['n_res']}, |E|={info['Ewt']}), "
          f"weight {info['weight']}; orbits after = {used2}; OK = {ok}")
print(f"\nchecked {nchecked} witnesses, failures {nbad}")
