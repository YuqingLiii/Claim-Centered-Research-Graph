"""Verify: cyclic colour rotation of a tiled assignment is realised by a TRANSLATION of the code,
hence rotated triples have identical extended codes up to relabelling and identical d_ext."""
import numpy as np, itertools
from gross import NG, N, ELL, EM, gidx, HX, HZ, Reducer, rref
from sched import make_phi
from cert import tiled_orders
import dext

phi = make_phi(1, 1)
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

# a translation g with phi(g) = 1
g = next((a, b) for a in range(ELL) for b in range(EM) if (a + b) % 3 == 1)
print("translation with phi(g)=1 :", g)
dp, cp = dperm(*g), cperm(*g)
# it is a code automorphism: preserves rowspace(HX), rowspace(HZ), ker, and logical triviality
RX, RZ = Reducer(HX), Reducer(HZ)
print("  permutes rowspace(HX):", all(RX.inspan(HX[r][np.argsort(dp)]) for r in range(NG)))
print("  permutes rowspace(HZ):", all(RZ.inspan(HZ[r][np.argsort(dp)]) for r in range(NG)))

bad = 0
for sector in ('Z', 'X'):
    for tr in itertools.product([1, 2, 9, 62] if sector == 'Z' else [0, 2, 9, 14], repeat=3):
        rot = (tr[1], tr[2], tr[0])
        o1, _ = tiled_orders(sector, phi, tr)
        o2, _ = tiled_orders(sector, phi, rot)
        r1 = dext.residual_sets(o1); r2 = dext.residual_sets(o2)
        # translating assignment `tr` by g must give exactly assignment `rot`
        for c in range(NG):
            for k in range(3):
                if tuple(sorted(int(dp[q]) for q in r1[c][k])) != tuple(sorted(r2[int(cp[c])][k])):
                    bad += 1
print("residual-set equivariance failures over all 64 triples per sector, both sectors:", bad)
