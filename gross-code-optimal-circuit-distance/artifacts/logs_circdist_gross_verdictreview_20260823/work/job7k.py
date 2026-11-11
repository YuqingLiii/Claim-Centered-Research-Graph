
"""job7.py with a selectable solver.  CNF construction is byte-identical to job7.py, so
cnf_sha256 is comparable across solvers.

usage: job7k.py <sector> <a,b,c> <W> <K> <Ew> <orbit> <solver>
       solver in {cd15, cd19, cd30, kissat, g42, mgh, cms}
"""
import sys, time, json, hashlib
import numpy as np
from pysat.solvers import (Cadical153, Cadical195, Cadical300, Glucose42,
                           MinisatGH, Kissat404)
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert7

SOLVERS = dict(cd15=Cadical153, cd19=Cadical195, cd30=Cadical300,
               kissat=Kissat404, g42=Glucose42, mgh=MinisatGH)

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3]); K = int(sys.argv[4]); Ew = int(sys.argv[5])
oi = int(sys.argv[6]); sname = sys.argv[7]
s_par, t_par = 1, 1

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = cert7.Cert7(ctx, W, K, Ew)
cls = list(c.cls)
rec = dict(sector=sector, triple=list(triple), W=W, K=K, Ew=Ew, orbit=oi,
           phi=[s_par, t_par], nclauses=len(cls), nvars=c.top, solver=sname)
if oi >= 0:
    assert K >= 1, "residual-orbit split requires K >= 1"
    S, orbits = dext2.column_orbits(phi, triple)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    rec['norbits'] = len(rorb); rec['stab'] = len(S)
    assert all(len(o) == len(S) for _, o in rorb)
    if oi >= len(rorb):
        rec.update(verdict='NOORBIT'); print(json.dumps(rec)); sys.exit(0)
    rep, orb = rorb[oi]
    rec['rep'] = str(rep)
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
h = hashlib.sha256()
for cl in cls:
    h.update((" ".join(map(str, cl)) + "\n").encode())
rec['cnf_sha256'] = h.hexdigest()[:32]
rec['nclauses_final'] = len(cls)
t0 = time.time()
with SOLVERS[sname](bootstrap_with=cls) as S2:
    sat = S2.solve()
    m = S2.get_model() if sat else None
rec['seconds'] = round(time.time() - t0, 1)
if sat:
    E, R, D = c.decode(m)
    info = dext.verify_witness(ctx, E, R, D, Hstab)
    rec.update(verdict='SAT',
               info={k2: (bool(v) if isinstance(v, bool) else int(v)) for k2, v in info.items()},
               R=[[int(a), int(b)] for a, b in R],
               D=[int(i) for i in np.nonzero(D)[0]],
               E=[int(i) for i in np.nonzero(E)[0]])
else:
    rec.update(verdict='UNSAT')
print(json.dumps(rec))
