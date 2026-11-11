"""Reading A of Figure 12 (labels taken as the ancilla instance's own consecutive times, no
straddle): what are the order-class triples, do they survive the cascade, and if not, exhibit the
weight-10 witness."""
import numpy as np, itertools
from sched import make_phi
from cascade import REPS, collect_rules, survivors, CLS_OF
from cascade_check import audit
from fig12 import XPANEL, ZPANEL, COLS, xmaps, zmaps, slot_times, order_class

phi = make_phi(1, 1)
SURV = {}
for sector in ('X', 'Z'):
    r1, r2 = collect_rules(sector, phi)
    alive, _, _ = survivors(r1, r2)
    SURV[sector] = {tuple(int(x) for x in v) for v in np.argwhere(alive)}

for name, panel, mps, sector in (('X', XPANEL, xmaps(), 'X'), ('Z', ZPANEL, zmaps(), 'Z')):
    print(f"--- {sector} sector, Reading A (as drawn, white = LEFT half) ---")
    for i, mp in enumerate(mps):
        T = slot_times(panel, mp)
        cls = {c: order_class(T[c]) for c in COLS}
        for perm in itertools.permutations(range(3)):
            tr = tuple(cls[COLS[perm[c]]] for c in range(3))
            if tr in SURV[sector]:
                print(f"   map{i} perm{perm}: triple {tr}  SURVIVES")
                break
        else:
            tr = tuple(cls[COLS[c]] for c in range(3))
            a = audit(sector, phi, tr)
            print(f"   map{i}: triple {tr}  ELIMINATED -> witness {a}")
