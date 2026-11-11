#!/usr/bin/env python3
"""CORRECTED reviewer-independent EXHAUSTIVE decision of the |E| = 12 stratum.

A solution needs  |L xor rho_R| + K <= W = 10  with |L| = 12.
Write a = |rho cap L|, b = |rho \ L|.  Then |L xor rho| = 12 - a + b, so the requirement is
        a - b >= 2 + K,   hence   a >= 2 + K.
Since rho is contained in the union of the chosen instances,  a <= sum_i |r_i cap L| =: SUM_OV.
So  SUM_OV >= 2 + K  is a SOUND necessary condition -- and it is applied over ALL C(216,K)
combinations, including instances disjoint from L (which cannot raise a but CAN lower b by
cancelling out-of-L weight, so they must not be dropped a priori).  My first pass dropped them;
this version does not.
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
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4

for sector in ('Z', 'X'):
    orders, _ = tiled_orders(sector, phi, CAND[sector])
    ctx, Hstab = dext.sector_ctx(orders, sector)
    P = (PZ if sector == 'Z' else PX)
    INST = np.zeros((216, G.N), np.uint8)
    idx = 0
    for c in range(G.NG):
        for k in range(3):
            for q in ctx.res[c][k]: INST[idx, q] = 1
            idx += 1
    print("\n=== sector %s  triple %s ===" % (sector, CAND[sector]))
    OV = (INST[None, :, :] & np.array(P, np.uint8)[:, None, :]).sum(2)   # (1884, 216)
    print("max |r cap L| over all (logical, residual instance) pairs: %d" % OV.max())
    print("distribution of |r cap L|:", dict(sorted(collections.Counter(OV.ravel().tolist()).items())))
    OVMAX = int(OV.max())
    for K in range(1, KMAX + 1):
        thresh = 2 + K
        if K * OVMAX < thresh:
            print("  K=%d : SUM_OV can be at most %d < %d  =>  NO SOLUTION, proved without search"
                  % (K, K * OVMAX, thresh)); continue
        t0 = time.time(); found = []; cnt = [0]
        for Li in range(len(P)):
            Lv = P[Li]; ov = OV[Li]
            order = np.argsort(-ov)                       # descending overlap
            ovs = ov[order]
            pre = np.concatenate([[0], np.cumsum(ovs)])
            # DFS over combinations in descending-overlap order with the SUM_OV bound
            n = len(order)
            def rec(start, s, chosen, rho):
                d = len(chosen)
                if d == K:
                    cnt[0] += 1
                    if s >= thresh and int(((Lv + rho) % 2).sum()) + K <= W:
                        found.append((Li, tuple(int(order[i]) for i in chosen)))
                    return
                rem = K - d
                # best possible additional overlap: the rem largest remaining
                if s + int(pre[min(start + rem, n)] - pre[start]) < thresh: return
                for i in range(start, n - rem + 1):
                    if s + int(pre[min(i + rem, n)] - pre[i]) < thresh: break
                    rec(i + 1, s + int(ovs[i]), chosen + [i], (rho + INST[order[i]]) % 2)
            rec(0, 0, [], np.zeros(G.N, np.uint8))
        print("  K=%d  need SUM_OV >= %d : full combinations reaching the bound = %d ; "
              "SOLUTIONS FOUND %d   (%.1fs)" % (K, thresh, cnt[0], len(found), time.time() - t0))
        if found: print("     EXAMPLE:", found[0])
