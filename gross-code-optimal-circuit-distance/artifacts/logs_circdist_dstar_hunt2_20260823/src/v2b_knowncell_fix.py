"""KNOWN-CELL REPRODUCTION, with the labelling conjugation resolved.

phicert prints M_cand's Z-check 0 support as  {3, 6, 12} u {73, 90, 74}.  This session's build
gives  {3, 66, 60} u {77, 126, 76}.  The two are related by the group inversion g -> -g:
  gi(0,3)->3, gi(11,0)->gi(1,0)=6, gi(10,0)->gi(2,0)=12, gi(0,5)->gi(0,1)=73, gi(9,0)->gi(3,0)=90,
  gi(0,4)->gi(0,2)=74  -- all six match, and inversion preserves the SLOT index.
Inversion sends colour c = (i+j) mod 3 to 2c mod 3, i.e. it swaps colours 1 and 2.  So their
order-class triple (t0, t1, t2) is realised in THIS build as (t0, t2, t1).  Both readings are run
below; the campaign's certification is d_ext = 11 for the (1,2,62)/(14,0,2) orbit, so BOTH must
return zero weight-<=10 configurations in the |V| = 12 stratum.
"""
import itertools, sys, time
import core2 as C
from orderlib import orders_from_slotorders, strat_from_orders, hot_report

CLS = {0: (0, 1, 2, 3, 4, 5), 1: (0, 1, 2, 4, 3, 5), 2: (0, 1, 2, 5, 3, 4),
       14: (0, 2, 1, 5, 3, 4), 62: (1, 2, 0, 5, 3, 4)}
(pz, _, _), (px, _, _) = C.pools()

READINGS = [
    ("as printed          Z=(1,2,62)  X=(14,0,2)", (1, 2, 62), (14, 0, 2)),
    ("inversion-corrected Z=(1,62,2)  X=(14,2,0)", (1, 62, 2), (14, 2, 0)),
]
for tag, trZ, trX in READINGS:
    soZ = {c: CLS[trZ[c]] for c in range(3)}
    soX = {c: CLS[trX[c]] for c in range(3)}
    oZ = orders_from_slotorders(soZ, 'Z')       # Z-check orders -> X-memory hooks
    oX = orders_from_slotorders(soX, 'X')       # X-check orders -> Z-memory hooks
    print("=" * 96)
    print("M_cand reading: %s" % tag)
    hot_report(oX, pz, "  Z-memory (X-check hooks)")
    hot_report(oZ, px, "  X-memory (Z-check hooks)")
    t0 = time.time()
    nz, _ = strat_from_orders(oX, pz, False, 10)
    nx, _ = strat_from_orders(oZ, px, True, 10)
    print("  |V|=12 stratum, j<=3, W=10 :  Z-memory %d configurations, X-memory %d configurations"
          "   -> %s   (%.0fs)"
          % (nz, nx, "CONSISTENT with the campaign's certified d_ext = 11"
             if nz == 0 and nx == 0 else "*** CONFLICT WITH THE CAMPAIGN ***", time.time() - t0))
