"""Machine check of the three things the (K,|E|) cell decomposition rests on, on the candidate's
own residual sets, by randomised sampling over the actual model:

 (A) the cut inequalities (c3)-(c6) of cert4.py hold for EVERY assignment of the unsplit model with
     |d| + |R| <= W;
 (B) the dominance cut is weight-non-increasing and E-preserving: a solution using both r2(c) and
     r3(c) maps to a solution of strictly smaller weight with the same E;
 (C) the cells are exhaustive: every weight-<=W assignment with |E| >= 12 and |E| even falls into
     one of cert4.cells(W).

(A) and (B) are checked on 200 000 random (R, d) draws per sector; (C) follows from (A) plus the
two facts certified elsewhere (|E| even -- all-ones lies in rowspace(H_det), anchor1.py; |E| >= 12
-- d(gross) = 12, re-certified in anchor2.py).
"""
import numpy as np, itertools, sys
from gross import N, NG
from sched import make_phi
from cert import tiled_orders
import dext, cert4

W = 10
rng = np.random.default_rng(20260822)
phi = make_phi(1, 1)
allcells = set(cert4.cells(W))
report = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    orders, _ = tiled_orders(sector, phi, tr)
    res = dext.residual_sets(orders)
    cols = [(c, k) for c in range(NG) for k in range(3)]
    bad = dict(c3=0, c4=0, c5=0, c6=0, ub=0, dom=0, cell=0)
    nsamp = 200000
    for _ in range(nsamp):
        K = int(rng.integers(1, W + 1))
        idx = rng.choice(len(cols), size=K, replace=False)
        R = [cols[i] for i in idx]
        rho = np.zeros(N, np.uint8)
        for (c, k) in R:
            for q in res[c][k]:
                rho[q] ^= 1
        nd = int(rng.integers(0, W - K + 1))
        d = np.zeros(N, np.uint8)
        d[rng.choice(N, size=nd, replace=False)] = 1
        E = d ^ rho
        Ew = int(E.sum()); rw = int(rho.sum()); n3 = sum(1 for (c, k) in R if k == 1)
        if nd + K > W:
            continue
        # (A) the cuts, as they are added in cert4.Cert4 for the cell (K, Ew)
        if not nd <= W - K:
            bad['c3'] += 1
        if not rw >= Ew - (W - K):
            bad['c4'] += 1
        if not rw <= 3 * K:
            bad['c5'] += 1
        if not n3 >= Ew - W - K:
            bad['c6'] += 1
        if not Ew <= W + 2 * K:
            bad['ub'] += 1
        # (C) cell membership, for the assignments that could be genuine solutions
        if Ew >= 12 and Ew % 2 == 0 and (K, Ew) not in allcells:
            bad['cell'] += 1
        # (B) dominance repair, when applicable
        dbl = [c for c in range(NG) if (c, 1) in R and (c, 2) in R]
        if dbl:
            c0 = dbl[0]
            R2 = [x for x in R if x not in ((c0, 1), (c0, 2))]
            i4 = res[c0][1][0]                      # r2 = {i4,i5,i6}, r3 = {i5,i6}
            assert set(res[c0][1]) - set(res[c0][2]) == {i4}
            d2 = d.copy(); d2[i4] ^= 1
            rho2 = np.zeros(N, np.uint8)
            for (c, k) in R2:
                for q in res[c][k]:
                    rho2[q] ^= 1
            if not (np.array_equal(d2 ^ rho2, E) and int(d2.sum()) + len(R2) < nd + K):
                bad['dom'] += 1
    report[sector] = bad
    print(f"sector {sector} triple {tr}: {nsamp} random (R,d) draws, violations {bad}")
print("cells(W=10):", len(allcells), "  all violation counters zero:",
      all(v == 0 for b in report.values() for v in b.values()))
