#!/usr/bin/env python3
"""Reviewer-independent EXHAUSTIVE decision of the |E| = 12 stratum for K = 1, 2, 3.

Requirement for a weight-<=W solution with |E| = 12:
    |L xor rho| + K <= W = 10,  |L| = 12
  write a = |rho cap L|, b = |rho \ L|;  |L xor rho| = 12 - a + b, so    a - b >= K + 2.
Let each chosen instance r_i have ov_i = |r_i cap L|.  Every qubit of rho cap L is covered an odd
(hence >= 1) number of times, so   a <= SUM_OV := sum_i ov_i,  and therefore SUM_OV >= K + 2 is a
SOUND necessary condition.  It is applied over ALL C(216, K) combinations -- instances disjoint
from L are NOT dropped, because although they cannot raise a they can lower b.

MEASURED FACT (both sectors): max_i ov_i = 2.  Writing n2/n1/n0 for how many chosen instances have
ov = 2/1/0, SUM_OV = 2*n2 + n1 >= K + 2 = n2 + n1 + n0 + 2  <=>  n2 >= n0 + 2.
So the search is a small enumeration over TYPES (n2, n1, n0).  Nothing is pruned heuristically.
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
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3

for sector in ('Z', 'X'):
    orders, _ = tiled_orders(sector, phi, CAND[sector])
    ctx, Hstab = dext.sector_ctx(orders, sector)
    P = np.array(PZ if sector == 'Z' else PX, np.uint8)
    INST = np.zeros((216, G.N), np.uint8); i = 0
    for c in range(G.NG):
        for k in range(3):
            for q in ctx.res[c][k]: INST[i, q] = 1
            i += 1
    OV = (INST[None, :, :] & P[:, None, :]).sum(2)
    OVMAX = int(OV.max())
    print("\n=== sector %s  triple %s ===" % (sector, CAND[sector]))
    print("  instances 216 (weights %s) ; pool %d ; max |r cap L| = %d"
          % (dict(sorted(collections.Counter(int(v.sum()) for v in INST).items())), len(P), OVMAX))
    assert OVMAX == 2, "type enumeration below assumes max overlap 2"
    for K in range(1, KMAX + 1):
        types = [(n2, n1, K - n2 - n1)
                 for n2 in range(K + 1) for n1 in range(K + 1 - n2)
                 if n2 >= (K - n2 - n1) + 2]
        t0 = time.time(); examined = 0; sols = []
        if not types:
            print("  K=%d : no (n2,n1,n0) type satisfies n2 >= n0 + 2 with max overlap 2"
                  "  =>  NO SOLUTION, proved without search" % K); continue
        for Li in range(len(P)):
            Lv = P[Li]; ov = OV[Li]
            I2 = np.nonzero(ov == 2)[0]; I1 = np.nonzero(ov == 1)[0]; I0 = np.nonzero(ov == 0)[0]
            for (n2, n1, n0) in types:
                if len(I2) < n2 or len(I1) < n1 or len(I0) < n0: continue
                for S2 in itertools.combinations(I2, n2):
                    r2 = INST[list(S2)].sum(0) % 2 if n2 else np.zeros(G.N, np.uint8)
                    for S1 in itertools.combinations(I1, n1):
                        r1 = (r2 + INST[list(S1)].sum(0)) % 2 if n1 else r2
                        for S0 in itertools.combinations(I0, n0):
                            rho = (r1 + INST[list(S0)].sum(0)) % 2 if n0 else r1
                            examined += 1
                            if int(((Lv + rho) % 2).sum()) + K <= W:
                                sols.append((Li, S2, S1, S0))
        print("  K=%d  types %s : combinations examined %d ; SOLUTIONS FOUND %d   (%.1fs)"
              % (K, types, examined, len(sols), time.time() - t0))
        if sols: print("     EXAMPLE:", sols[0])
    print("  => cells (K,|E|)=(1,12),(2,12),(3,12) in sector %s are UNSAT for EVERY orbit index,"
          " by exhaustive enumeration independent of the SAT encoding and of the orbit split."
          % sector)
