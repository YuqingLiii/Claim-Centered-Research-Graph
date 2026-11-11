#!/usr/bin/env python3
"""Reviewer-independent EXHAUSTIVE decision of the |E| = 12 stratum for K = 1,2,3.

Claim under test: for |E| = 12 there is NO extended-code solution of weight <= 10, i.e. no
(L, R) with L a weight-12 non-trivial logical, |R| = K distinct residual instances, and
|L xor rho_R| + K <= 10.  If none exists for a given (sector, K), then ALL NINE orbit slots of
that cell are UNSAT regardless of how the orbit decomposition is defined -- which is a strictly
stronger statement than the per-orbit certificates, and independent of the orbit machinery.

Written from scratch; uses the project only for H, the pool, and the residual sets.
"""
import sys, os, itertools, time, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'work'))
import gross as G
from sched import make_phi
from cert import tiled_orders
import dext, pool as poolmod

CAND = {'Z': (1, 2, 62), 'X': (14, 0, 2)}
W = 10
phi = make_phi(1, 1)
PZ, PX, LX, LZ = poolmod.get()

for sector in ('Z', 'X'):
    orders, _ = tiled_orders(sector, phi, CAND[sector])
    ctx, Hstab = dext.sector_ctx(orders, sector)
    P = (PZ if sector == 'Z' else PX)
    # all residual instances (check, k) as 0/1 vectors
    inst = []
    for c in range(G.NG):
        for k in range(3):
            v = np.zeros(G.N, np.uint8)
            for q in ctx.res[c][k]: v[q] = 1
            inst.append(v)
    INST = np.array(inst, np.uint8)
    print("\n=== sector %s  triple %s ===" % (sector, CAND[sector]))
    print("residual instances: %d ; weights %s"
          % (len(INST), dict(sorted(collections.Counter(int(v.sum()) for v in INST).items()))))
    print("pool: %d weight-12 logicals" % len(P))

    for K in (1, 2, 3):
        need = W - K                    # |d| must be <= need
        t0 = time.time(); found = []; combos = 0
        for Li, Lv in enumerate(P):
            ov = (INST & Lv).sum(1)                 # |r cap L| per instance
            rel = np.nonzero(ov >= 1)[0]
            if K == 1:
                cand = [(i,) for i in rel]
            elif K == 2:
                cand = [t for t in itertools.combinations(rel, 2)
                        if ov[list(t)].sum() >= 2 + K]
            else:
                cand = [t for t in itertools.combinations(rel, 3)
                        if ov[list(t)].sum() >= 2 + K]
            combos += len(cand)
            for t in cand:
                rho = INST[list(t)].sum(0) % 2
                if int(((Lv + rho) % 2).sum()) + K <= W:
                    found.append((Li, t))
        print("  K=%d  |d| must be <= %d : combinations examined %d ; SOLUTIONS FOUND %d   (%.1fs)"
              % (K, need, combos, len(found), time.time() - t0))
        if found:
            print("     EXAMPLE:", found[0])
    # the sharp K=1 statement
    w3 = [i for i in range(len(INST)) if int(INST[i].sum()) == 3]
    cnt = sum(1 for Lv in P for i in w3 if int((INST[i] & Lv).sum()) == 3)
    print("  [K=1 sharp form] a weight-10 solution at K=1 exists iff some weight-12 logical "
          "CONTAINS a whole weight-3 residual set.  Such (L, r) pairs: %d" % cnt)
