"""(a) the |E| >= 12 anchor in the X sector: d(gross) = 12, re-certified with the residual columns
       switched off (UNSAT at W = 11, SAT at W = 12);
   (b) an EXPLICIT weight-11 solution of the full extended-code model for the candidate, in both
       sectors, built combinatorially from the complete weight-12 logical enumeration: take any
       weight-12 logical L containing a weight-2 residual r of some check, put E = L, R = {r},
       d = L xor r; then |d| + |R| = 10 + 1 = 11.  This gives d_ext(E(candidate)) <= 11 by witness,
       which with UNSAT at W = 10 pins d_ext = 11 exactly.
"""
import json, time, sys
import numpy as np
from gross import NG, N
from sched import make_phi
from cert import tiled_orders
import dext, pool as poolmod

out = {}
phi = make_phi(1, 1)
# (b) first: cheap and it is the load-bearing half
PZ, PX, LX, LZ = poolmod.get()
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    orders, Hstab0 = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    P = PZ if sector == 'Z' else PX
    found = None
    for L in P:
        for c in range(NG):
            for k in (0, 2):                      # the two weight-2 residuals r1, r3
                r = ctx.res[c][k]
                if all(L[q] for q in r):
                    D = L.copy()
                    for q in r:
                        D[q] ^= 1
                    info = dext.verify_witness(ctx, L, [(c, k)], D, Hstab)
                    if info['weight'] == 11 and info['decomposition_ok'] and \
                       info['zero_syndrome'] and info['nontrivial_logical']:
                        found = dict(info=info, check=int(c), k=int(k),
                                     r=[int(q) for q in r],
                                     E=[int(i) for i in np.nonzero(L)[0]],
                                     D=[int(i) for i in np.nonzero(D)[0]])
                        break
            if found: break
        if found: break
    print(f"[{sector}] explicit weight-11 extended-code solution: {found['info']}  "
          f"(check {found['check']}, residual r{found['k']+1} = {found['r']})")
    sys.stdout.flush()
    out[sector] = dict(w11=found)
# (a) the X-sector |E| >= 12 anchor
for sector, tr in (('X', (14, 0, 2)),):
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    for W in (11, 12):
        sat, wit, el, ncls = dext.query(ctx, W, Hstab, use_residuals=False)
        print(f"[{sector}] residuals OFF, W={W}: {'SAT' if sat else 'UNSAT'} ({el:.1f}s)",
              wit[3] if sat else "")
        sys.stdout.flush()
        out[sector][f'no_residuals_W{W}'] = dict(verdict='SAT' if sat else 'UNSAT',
                                                 seconds=round(el, 1),
                                                 info=(wit[3] if sat else None))
json.dump(out, open("anchor3.json", "w"), indent=1)
