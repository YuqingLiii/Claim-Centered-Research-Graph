#!/usr/bin/env python3
"""w11.py -- independent re-verification of the  d_ext <= 11  half of the verdict on the
CANDIDATE assignment, in both sectors.

Two things, in order:

 (A) RE-DERIVE, not re-read.  Independently search for a weight-11 witness the way the upper-bound
     argument says one must exist: a weight-12 non-trivial logical L that contains a weight-2
     residual r of some check c; then  E = L,  R = {(c,k)},  d = L xor r  has
     |d| + |R| = 10 + 1 = 11.  Report how many such (L, c, k) exist, not just the first.

 (B) VERIFY the recorded anchor3.json witness, three independent ways:
       (1) dext.verify_witness       -- the project's own F2 checker
       (2) F2 algebra written here   -- shares no code with (1)
       (3) weight bookkeeping        -- |d| + |R| = 11 and |E| = 12
"""
import sys, os, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gross import HX, HZ, N, NG, Reducer
from sched import make_phi
from cert import tiled_orders
import dext
import pool as poolmod

CAND = {'Z': (1, 2, 62), 'X': (14, 0, 2)}
rec = json.load(open(os.path.join(HERE, 'anchor3.json')))
PZ, PX, LX, LZ = poolmod.get()

print("=" * 96)
print("d_ext <= 11 on the CANDIDATE, independently re-derived and re-verified")
print("=" * 96)
allok = True
for sector in ('Z', 'X'):
    triple = CAND[sector]
    phi = make_phi(1, 1)
    orders, Hstab0 = tiled_orders(sector, phi, triple)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    Hdet = HX if sector == 'Z' else HZ
    P = PZ if sector == 'Z' else PX

    # ---------------------------------------------------------------- (A) re-derive
    hits = []
    for Li, L in enumerate(P):
        for c in range(NG):
            for k in (0, 2):                 # the two weight-2 residuals r1, r3
                r = ctx.res[c][k]
                if len(r) == 2 and all(L[q] for q in r):
                    hits.append((Li, c, k))
    print()
    print("[%s]  candidate triple %s" % (sector, str(triple)))
    print("  (A) re-derivation: weight-12 logicals in the pool containing a weight-2 residual")
    print("      pool size %d;  (L, check, k) hits: %d;  distinct logicals L: %d;  distinct checks: %d"
          % (len(P), len(hits), len({h[0] for h in hits}), len({h[1] for h in hits})))
    # verify the FIRST hit end-to-end, from scratch
    Li, c, k = hits[0]
    L = P[Li]
    r = ctx.res[c][k]
    D0 = L.copy()
    for q in r:
        D0[q] ^= 1
    i0 = dext.verify_witness(ctx, L, [(c, k)], D0, Hstab)
    print("      first hit: logical #%d, check %d, k %d, r = %s" % (Li, c, k, sorted(r)))
    print("      -> weight %d = %d data + %d hook, |E| = %d, decomposition_ok=%s zero_syndrome=%s nontrivial_logical=%s"
          % (i0['weight'], i0['n_data'], i0['n_res'], i0['Ewt'], i0['decomposition_ok'],
             i0['zero_syndrome'], i0['nontrivial_logical']))
    derive_ok = (i0['weight'] == 11 and i0['Ewt'] == 12 and i0['decomposition_ok']
                 and i0['zero_syndrome'] and i0['nontrivial_logical'])

    # ---------------------------------------------------------------- (B) verify the record
    w = rec[sector]['w11']
    chk, kk = w['check'], w['k']
    Eset, Dset, rset = set(w['E']), set(w['D']), set(w['r'])
    r_derived = set(ctx.res[chk][kk])
    r_match = (r_derived == rset)

    E = np.zeros(N, np.uint8)
    for j in Eset:
        E[j] = 1
    D = np.zeros(N, np.uint8)
    for j in Dset:
        D[j] = 1

    info = dext.verify_witness(ctx, E, [(chk, kk)], D, Hstab)          # (1)

    rr = np.zeros(N, np.uint8)                                          # (2)
    for j in rset:
        rr[j] = 1
    decomp = bool(((D ^ rr) == E).all())
    zero_syn = not ((Hdet @ E) % 2).any()
    nontriv = not Reducer(Hstab).inspan(E)

    bk = (len(Dset) + 1 == 11 and len(Eset) == 12 and Dset == Eset - rset)   # (3)

    ok = (r_match and decomp and zero_syn and nontriv and bk and derive_ok
          and info['weight'] == 11 and info['decomposition_ok']
          and info['zero_syndrome'] and info['nontrivial_logical'])
    allok &= ok
    print("  (B) the recorded anchor3 witness: check %d, k %d, residual r = %s   (r re-derived from ctx.res: %s)"
          % (chk, kk, sorted(rset), r_match))
    print("      E = %s" % sorted(Eset))
    print("      d = %s" % sorted(Dset))
    print("      (1) dext.verify_witness : weight=%d = %d data + %d hook, |E|=%d, decomposition_ok=%s zero_syndrome=%s nontrivial_logical=%s"
          % (info['weight'], info['n_data'], info['n_res'], info['Ewt'],
             info['decomposition_ok'], info['zero_syndrome'], info['nontrivial_logical']))
    print("      (2) independent F2      : E = d xor r : %s    H_det.E = 0 : %s    E not in rowspace(H_stab) : %s"
          % (decomp, zero_syn, nontriv))
    print("      (3) bookkeeping         : |d| + |R| = %d + 1 = %d,  |E| = %d  -> %s"
          % (len(Dset), len(Dset) + 1, len(Eset), bk))
    print("      ==> %s :  d_ext(candidate, sector %s) <= 11" % ("PASS" if ok else "*** FAIL ***", sector))
print()
print("=" * 96)
print("BOTH SECTORS: %s" % ("PASS -- d_ext <= 11 on the candidate in both sectors, by explicit witness"
                            if allok else "*** FAILURE ***"))
