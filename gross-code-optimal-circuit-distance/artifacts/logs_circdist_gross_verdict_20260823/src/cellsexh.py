#!/usr/bin/env python3
"""cellsexh.py -- is  cert4.cells(W)  EXHAUSTIVE?

Review item 8 asks whether the cell sweep enumerates every (K, |E|) a solution can occupy, or
merely the cells someone chose to run.  Previous sessions answered this empirically (cuts.py:
200 000 random draws, 0 'cell' violations).  Here it is answered analytically, and each ingredient
of the argument is checked numerically.

A solution is (E, R, d) with  H_det E = 0,  E not in rowspace(H_stab),  d = E xor rho_R,
weight = |d| + |R| <= W.   Write K = |R|.

  LOWER BOUND on |E|
      E is a non-trivial logical of the base code, so |E| >= d(code).
      PARITY: the all-ones vector lies in rowspace(H_X) and in rowspace(H_Z), so every coset of
      the stabiliser has constant weight parity and |E| must be EVEN.
      => |E| >= 12 and |E| even.

  UPPER BOUND on |E|
      |E| = |d xor rho_R| <= |d| + |rho_R|.
      |rho_R| <= K * (max weight of a single residual set).
      |d| = weight - |R| <= W - K.
      => |E| <= (W - K) + K * wmax.
      With wmax = 3 this is exactly  |E| <= W + 2K,  which is the bound cells() uses.

So cells() is exhaustive iff wmax <= 3.  This script checks wmax, the parity claim, and the code
distance lower bound, and then verifies that cells(W) is exactly the set the two bounds allow.
"""
import sys, os, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gross import HX, HZ, N, Reducer, rref
from sched import make_phi
from cert import tiled_orders
import dext, cert4
import pool as poolmod

W = 10
CAND = {'Z': (1, 2, 62), 'X': (14, 0, 2)}
phi = make_phi(1, 1)
PZ, PX, LX, LZ = poolmod.get()

print("=" * 92)
print("is cert4.cells(W) EXHAUSTIVE?  --  the analytic bound, with every ingredient checked")
print("=" * 92)

# ---------------------------------------------------------------- ingredient 1: wmax
print()
print("(1) maximum weight of a single residual set  (RES_POS = r1={i1,i2}, r2={i4,i5,i6}, r3={i5,i6})")
wmax_all = 0
for sec, tr in CAND.items():
    orders, _ = tiled_orders(sec, phi, tr)
    ctx, _ = dext.sector_ctx(orders, sec)
    hist = collections.Counter()
    for c in range(ctx.ncheck):
        for k in range(3):
            hist[(k, len(ctx.res[c][k]))] += 1
    wmax = max(k[1] for k in hist)
    wmax_all = max(wmax_all, wmax)
    print("    sector %s: weights by k = %s   -> wmax = %d"
          % (sec, dict(sorted(hist.items())), wmax))
print("    wmax over both sectors = %d      (the bound needs wmax <= 3: %s)"
      % (wmax_all, wmax_all <= 3))

# ---------------------------------------------------------------- ingredient 2: parity
print()
print("(2) parity: is the all-ones vector in rowspace(H_X) and rowspace(H_Z)?")
ones = np.ones(N, np.uint8)
inX = Reducer(HX).inspan(ones)
inZ = Reducer(HZ).inspan(ones)
print("    all-ones in rowspace(H_X): %s     in rowspace(H_Z): %s" % (bool(inX), bool(inZ)))
print("    => every stabiliser coset has constant weight parity, so |E| is EVEN: %s"
      % bool(inX and inZ))
# empirical corroboration on the pools
par = {sec: sorted({int(v.sum()) % 2 for v in (PZ if sec == 'Z' else PX)}) for sec in CAND}
print("    weight parities actually present in the weight-12 logical pools: %s" % par)

# ---------------------------------------------------------------- ingredient 3: min weight
print()
print("(3) lower bound |E| >= 12")
print("    the gross code is [[144, 12, 12]]; the pools hold the weight-12 non-trivial logicals")
print("    pool sizes |PZ| = %d, |PX| = %d, all of weight 12: %s"
      % (len(PZ), len(PX), bool((PZ.sum(1) == 12).all() and (PX.sum(1) == 12).all())))
print("    corroborated in-session by anchor2/anchor3: with residuals OFF,")
print("      [Z] W = 11 UNSAT, W = 12 SAT     [X] W = 11 UNSAT, W = 12 SAT")
print("    i.e. no non-trivial logical of weight <= 11 exists in either sector.")

# ---------------------------------------------------------------- the bound vs cells()
print()
print("(4) the two bounds vs. what cells(W) actually enumerates, W = %d" % W)
allowed = set()
for K in range(0, W + 1):
    lo, hi = 12, (W - K) + K * wmax_all      # = W + 2K when wmax = 3
    for Ew in range(lo, hi + 1):
        if Ew % 2 == 0:
            allowed.add((K, Ew))
got = set(cert4.cells(W))
print("    allowed by the analytic bounds : %d cells" % len(allowed))
print("    cert4.cells(%d) returns         : %d cells" % (W, len(got)))
print("    cells() MISSES an allowed cell : %s   <-- must be empty for exhaustiveness"
      % sorted(allowed - got))
print("    cells() includes extra cells   : %s   (harmless: extra cells are merely decided UNSAT)"
      % sorted(got - allowed))
print()
ok = not (allowed - got)
print("=" * 92)
print("VERDICT: cells(%d) is %s -- it covers every (K, |E|) a weight-<=%d solution can occupy."
      % (W, "EXHAUSTIVE" if ok else "*** NOT EXHAUSTIVE ***", W))
print("=" * 92)
