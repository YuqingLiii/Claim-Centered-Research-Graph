"""One (sector, tiled triple, W) exact d_ext decision query, UNQUOTIENTED (full 360 columns).
SAT -> explicit witness (re-verified from the definitions).  UNSAT -> certified d_ext > W.
Optional 5th arg: orbit index (uses the translation quotient of dext2)."""
import sys, time, json
import numpy as np
from pysat.solvers import Cadical153
from sched import make_phi
from cert import tiled_orders
import dext, dext2

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W      = int(sys.argv[3])
s_par, t_par = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1, 1)
oi     = int(sys.argv[6]) if len(sys.argv) > 6 else -1

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = dext2.Cert(ctx, W)
rec = dict(sector=sector, triple=list(triple), W=W, phi=[s_par, t_par], orbit=oi,
           nclauses=len(c.cls))
t0 = time.time()
if oi < 0:
    with Cadical153(bootstrap_with=c.cls) as S:
        sat = S.solve()
        m = S.get_model() if sat else None
    rec['seconds'] = round(time.time() - t0, 1)
    if sat:
        ms = set(x for x in m if x > 0)
        E = np.array([1 if c.z[j] in ms else 0 for j in range(144)], np.uint8)
        R = [(cc, k) for cc in range(72) for k in range(3) if c.u[cc][k] in ms]
        D = np.array([1 if c.d[j] in ms else 0 for j in range(144)], np.uint8)
        info = dext.verify_witness(ctx, E, R, D, Hstab)
        rec.update(verdict='SAT', info={k: (int(v) if not isinstance(v, bool) else bool(v))
                                        for k, v in info.items()},
                   R=[[int(a), int(b)] for a, b in R],
                   D=[int(i) for i in np.nonzero(D)[0]],
                   E=[int(i) for i in np.nonzero(E)[0]])
    else:
        rec.update(verdict='UNSAT')
else:
    S, orbits = dext2.column_orbits(phi, triple)
    rec['norbits'] = len(orbits); rec['stab'] = len(S)
    if oi >= len(orbits):
        rec.update(verdict='NOORBIT'); print(json.dumps(rec)); sys.exit(0)
    sat, wit, el = c.run([orbits[oi]], Hstab, verbose=False)
    rec['seconds'] = round(el, 1)
    rec['rep'] = str(orbits[oi][0])
    if sat:
        E, R, D, info = wit
        rec.update(verdict='SAT', info={k: (int(v) if not isinstance(v, bool) else bool(v))
                                        for k, v in info.items()},
                   R=[[int(a), int(b)] for a, b in R],
                   D=[int(i) for i in np.nonzero(D)[0]],
                   E=[int(i) for i in np.nonzero(E)[0]])
    else:
        rec.update(verdict='UNSAT')
print(json.dumps(rec))
