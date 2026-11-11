"""One (sector, tiled-assignment, weight-bound, column-orbit) SAT subproblem."""
import sys, time
import numpy as np
from gross import NG
from sched import make_phi
from cert import tiled_orders
import dext, dext2

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3])
oi = int(sys.argv[4])
s_par, t_par = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (1, 2)
phi = make_phi(s_par, t_par)
tag = f"{sector} {triple} W={W} orbit {oi}"

orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
S, orbits = dext2.column_orbits(phi, triple)
if oi >= len(orbits):
    print(f"{tag}: NO SUCH ORBIT (only {len(orbits)})"); sys.exit(0)
c = dext2.Cert(ctx, W)
rep, orb = orbits[oi]
t0 = time.time()
sat, wit, el = c.run([orbits[oi]], Hstab, verbose=False)
if sat:
    E, R, D, info = wit
    print(f"{tag} rep={rep}: SAT  {el:.1f}s  {info}")
    print(f"   E={sorted(int(i) for i in np.nonzero(E)[0])}")
    print(f"   R={R}")
    print(f"   D={sorted(int(i) for i in np.nonzero(D)[0])}")
else:
    print(f"{tag} rep={rep}: UNSAT  {el:.1f}s   (|orbit|={len(orb)}, |stab|={len(S)}, "
          f"{len(c.cls)} clauses)")
