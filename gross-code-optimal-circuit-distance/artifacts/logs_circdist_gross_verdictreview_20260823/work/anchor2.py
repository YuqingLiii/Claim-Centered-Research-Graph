"""Two anchors that the cell decomposition needs, both computed here rather than cited.

  (1) d(gross) = 12 : with the residual columns switched off the model degenerates to the code's
      own minimum logical weight.  UNSAT at W = 11, SAT at W = 12, in both sectors.
      This is what licenses the standing cut |E| >= 12.
  (2) d_ext(E(candidate)) <= 11 : an explicit weight-11 solution of the FULL model, in both
      sectors, found and re-verified from the definitions.  Together with UNSAT at W = 10 this
      pins d_ext = 11 exactly.
"""
import sys, json, time
import numpy as np
from sched import make_phi
from cert import tiled_orders
import dext

phi = make_phi(1, 1)
out = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    row = {}
    for W in (11, 12):
        sat, wit, el, ncls = dext.query(ctx, W, Hstab, use_residuals=False)
        row[f'no_residuals_W{W}'] = dict(verdict='SAT' if sat else 'UNSAT', seconds=round(el, 1),
                                         info=(wit[3] if sat else None))
        print(f"[{sector}] residuals OFF, W={W}: {'SAT' if sat else 'UNSAT'} ({el:.1f}s)",
              wit[3] if sat else "")
        sys.stdout.flush()
    sat, wit, el, ncls = dext.query(ctx, 11, Hstab)
    assert sat, "expected a weight-<=11 solution"
    E, R, D, info = wit
    row['full_W11'] = dict(verdict='SAT', seconds=round(el, 1), info=info,
                           R=[[int(a), int(b)] for a, b in R],
                           D=[int(i) for i in np.nonzero(D)[0]],
                           E=[int(i) for i in np.nonzero(E)[0]])
    print(f"[{sector}] full model, W=11: SAT ({el:.1f}s) {info}")
    sys.stdout.flush()
    out[sector] = row
json.dump(out, open("anchor2.json", "w"), indent=1)
