"""One (sector, triple, W, K, |E|) cell of the split certification, optionally restricted to one
column orbit of the assignment's translation stabiliser.

usage:  job4.py <sector> <a,b,c> <W> <K> <Ew> [orbit_index] [s t]
        orbit_index = -1 : no orbit restriction
        orbit_index >= 0 : index into the RESIDUAL column orbits of the assignment's translation
                           stabiliser S (9 of them: one per (colour, residual type); each has
                           |S| = 24 members).  The cell forces the orbit representative to be USED
                           and every residual column of a strictly earlier orbit to be UNUSED.

                           Sound cover, given K >= 1 (true in every cell we run, since K = 0 is
                           arithmetically empty): let x be a solution and let i be the least
                           residual-orbit index it uses.  Pick g in S carrying one of x's columns
                           in orbit i to rep_i; g.x is a solution of the same weight (S consists of
                           code translations that preserve the tiled assignment, hence the extended
                           code, its logical functional and every column weight), it uses rep_i,
                           and it uses no residual column of an orbit < i because orbits are
                           S-invariant.  So the 9 restricted queries cover all solutions.
"""
import sys, time, json, hashlib
import numpy as np
from pysat.solvers import Cadical153
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3]); K = int(sys.argv[4]); Ew = int(sys.argv[5])
oi = int(sys.argv[6]) if len(sys.argv) > 6 else -1
s_par, t_par = (int(sys.argv[7]), int(sys.argv[8])) if len(sys.argv) > 8 else (1, 1)

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = cert4.Cert4(ctx, W, K, Ew)
cls = list(c.cls)
rec = dict(sector=sector, triple=list(triple), W=W, K=K, Ew=Ew, orbit=oi,
           phi=[s_par, t_par], nclauses=len(cls), nvars=c.top)
if oi >= 0:
    assert K >= 1, "residual-orbit split requires K >= 1"
    S, orbits = dext2.column_orbits(phi, triple)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    rec['norbits'] = len(rorb); rec['stab'] = len(S)
    assert all(len(o) == len(S) for _, o in rorb)   # free action: every orbit has |S| members
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
with Cadical153(bootstrap_with=cls) as S2:
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
