"""One (sector, tiled triple, W, |R| = K) exact d_ext subproblem, with the two cardinality cuts
that K makes available.  Both are sound, not heuristic:

  |d| <= W - K            since  weight = |d| + |R| <= W  and  |R| = K;
  |E| <= W + 2K           since  E = d xor (xor of the K residuals), every residual has weight <= 3,
                          so |E| <= |d| + 3K <= (W-K) + 3K.

Together with the standing cut |E| >= 12 (the code's own minimum logical weight, certified by
reproducing d(gross) = 12 with the residual set switched off) these pin |E| into a narrow window --
for K = 1 they force |E| = 12 exactly.  K ranges over 0..W; the subproblems are exhaustive, so
UNSAT for every K certifies d_ext > W."""
import sys, time, json
import numpy as np
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from sched import make_phi
from cert import tiled_orders
import dext, dext2

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W      = int(sys.argv[3])
K      = int(sys.argv[4])
oi     = int(sys.argv[5]) if len(sys.argv) > 5 else -1
s_par, t_par = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (1, 1)

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = dext2.Cert(ctx, W)
ulits = [c.u[cc][k] for cc in range(72) for k in range(3)]
cls = list(c.cls); top = c.top
def add(enc):
    global cls, top
    cls += enc.clauses
    top = max([top] + [abs(l) for cl in enc.clauses for l in cl])
add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
if K > 0:
    add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
add(CardEnc.atmost(lits=c.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
add(CardEnc.atmost(lits=c.z, bound=W + 2*K, top_id=top, encoding=EncType.seqcounter))
rec = dict(sector=sector, triple=list(triple), W=W, K=K, orbit=oi, phi=[s_par, t_par],
           nclauses=len(cls))
assumptions = []
if oi >= 0:
    S, orbits = dext2.column_orbits(phi, triple)
    rec['norbits'] = len(orbits); rec['stab'] = len(S)
    if oi >= len(orbits):
        rec.update(verdict='NOORBIT'); print(json.dumps(rec)); sys.exit(0)
    rec['rep'] = str(orbits[oi][0])
    assumptions = [c.col_lit(orbits[oi][0])]
t0 = time.time()
with Cadical153(bootstrap_with=cls) as S2:
    sat = S2.solve(assumptions=assumptions)
    m = S2.get_model() if sat else None
rec['seconds'] = round(time.time() - t0, 1)
if sat:
    ms = set(x for x in m if x > 0)
    E = np.array([1 if c.z[j] in ms else 0 for j in range(144)], np.uint8)
    R = [(cc, k) for cc in range(72) for k in range(3) if c.u[cc][k] in ms]
    D = np.array([1 if c.d[j] in ms else 0 for j in range(144)], np.uint8)
    info = dext.verify_witness(ctx, E, R, D, Hstab)
    rec.update(verdict='SAT',
               info={k2: (int(v) if not isinstance(v, bool) else bool(v)) for k2, v in info.items()},
               R=[[int(a), int(b)] for a, b in R],
               D=[int(i) for i in np.nonzero(D)[0]],
               E=[int(i) for i in np.nonzero(E)[0]])
else:
    rec.update(verdict='UNSAT')
print(json.dumps(rec))
