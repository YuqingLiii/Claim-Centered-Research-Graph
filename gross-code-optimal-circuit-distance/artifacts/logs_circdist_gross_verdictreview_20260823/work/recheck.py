"""Independent re-decision of one cell with a DIFFERENT SAT solver, on a CNF rebuilt from scratch
and checked to have the same SHA-256 as the one job4.py decided.

usage: recheck.py <sector> <a,b,c> <W> <K> <Ew> <orbit> <solver>
       solver in {cd15, cd19, cd30, g4, g42, m22, mgh}
"""
import sys, time, json, hashlib
import numpy as np
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4

SOLVERS = {}
from pysat.solvers import (Cadical153, Cadical195, Cadical300, Glucose4, Glucose42,
                           Minisat22, MinisatGH)
SOLVERS = dict(cd15=Cadical153, cd19=Cadical195, cd30=Cadical300, g4=Glucose4,
               g42=Glucose42, m22=Minisat22, mgh=MinisatGH)

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3]); K = int(sys.argv[4]); Ew = int(sys.argv[5]); oi = int(sys.argv[6])
sname = sys.argv[7]

phi = make_phi(1, 1)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = cert4.Cert4(ctx, W, K, Ew)
cls = list(c.cls)
if oi >= 0:
    S, orbits = dext2.column_orbits(phi, triple)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    rep, orb = rorb[oi]
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
h = hashlib.sha256()
for cl in cls:
    h.update((" ".join(map(str, cl)) + "\n").encode())
t0 = time.time()
with SOLVERS[sname](bootstrap_with=cls) as S2:
    sat = S2.solve()
print(json.dumps(dict(sector=sector, triple=list(triple), W=W, K=K, Ew=Ew, orbit=oi,
                      solver=sname, cnf_sha256=h.hexdigest()[:32],
                      verdict='SAT' if sat else 'UNSAT', seconds=round(time.time() - t0, 1))))
