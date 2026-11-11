"""An independent, solver-light route to every cell with |E| = 12.

Step 1 -- COMPLETE enumeration of the weight-12 non-trivial logicals of the gross code, by
incremental SAT with blocking clauses: constraints H_det z = 0, OR_i (L_i . z = 1), |z| = 12;
after each model v the 12-literal clause  OR_{j in supp(v)} ~z_j  is added, which under |z| = 12
blocks exactly v and nothing else.  The loop ends in UNSAT, so the list is exhaustive by
construction (no reliance on pool.py's randomised ISD search).

Step 2 -- for every enumerated E, decide exactly whether  min_R ( |E xor rho_R| + |R| ) <= W.
With E fixed this is a tiny CNF (216 u-variables, d determined bitwise), so the whole |E| = 12
half of the certification is decided without any of the big queries.

The output is compared against pool.py's pool and against the cell-(K,12) SAT verdicts.
"""
import sys, time, json
import numpy as np
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, Reducer
from sched import make_phi
from cert import tiled_orders
from dext import xor_chain, xor_zero_direct, residual_sets
import dext, pool as poolmod

W = 10
phi = make_phi(1, 1)
PZ, PX, LX, LZ = poolmod.get()
out = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    Hdet, Lrows, Hstab = (HX, LX, HZ) if sector == 'Z' else (HZ, LZ, HX)
    Pref = PZ if sector == 'Z' else PX
    # ---- step 1
    p = IDPool()
    z = [p.id(('z', j)) for j in range(N)]
    cls = []
    for e in range(Hdet.shape[0]):
        xor_zero_direct([z[int(j)] for j in np.nonzero(Hdet[e])[0]], cls)
    ys = []
    for i in range(Lrows.shape[0]):
        ys.append(xor_chain(p, [z[int(j)] for j in np.nonzero(Lrows[i])[0]], cls))
    cls.append(ys)
    top = p.top
    for enc in (CardEnc.atmost(lits=z, bound=12, top_id=top, encoding=EncType.seqcounter),):
        cls += enc.clauses; top = max([top] + [abs(l) for c2 in enc.clauses for l in c2])
    for enc in (CardEnc.atleast(lits=z, bound=12, top_id=top, encoding=EncType.seqcounter),):
        cls += enc.clauses; top = max([top] + [abs(l) for c2 in enc.clauses for l in c2])
    t0 = time.time()
    words = []
    with Cadical153(bootstrap_with=cls) as S:
        while S.solve():
            m = set(x for x in S.get_model() if x > 0)
            supp = [j for j in range(N) if z[j] in m]
            assert len(supp) == 12
            v = np.zeros(N, np.uint8); v[supp] = 1
            words.append(v)
            S.add_clause([-z[j] for j in supp])
    t1 = time.time()
    Wds = np.array(words, np.uint8)
    red = Reducer(Hstab)
    ok = (((Hdet @ Wds.T) % 2 == 0).all() and (Wds.sum(1) == 12).all()
          and all(not red.inspan(v) for v in Wds))
    same = (sorted(v.tobytes() for v in Wds) == sorted(v.tobytes() for v in Pref))
    print(f"[{sector}] complete weight-12 logical enumeration: {len(Wds)} words in {t1-t0:.1f}s; "
          f"all valid: {ok}; identical to pool.py's pool: {same}")
    sys.stdout.flush()
    # ---- step 2
    orders, _ = tiled_orders(sector, phi, tr)
    res = residual_sets(orders)
    hit = [[] for _ in range(N)]
    for c in range(NG):
        for k in range(3):
            for q in res[c][k]:
                hit[q].append((c, k))
    best = None; nsat = 0
    t2 = time.time()
    for wi, E in enumerate(Wds):
        p2 = IDPool()
        u = [[p2.id(('u', c, k)) for k in range(3)] for c in range(NG)]
        d = [p2.id(('d', j)) for j in range(N)]
        cl = []
        for c in range(NG):
            cl.append([-u[c][1], -u[c][2]])
        for j in range(N):
            terms = [d[j]] + [u[c][k] for (c, k) in hit[j]]
            # d_j = E_j xor (xor of used residuals hitting j)
            lits = terms
            k = len(lits)
            par = int(E[j])
            for bits in np.ndindex(*([2] * k)):
                if sum(bits) % 2 != par:
                    cl.append([(-lits[i] if bits[i] else lits[i]) for i in range(k)])
        card = [d[j] for j in range(N)] + [u[c][k] for c in range(NG) for k in range(3)]
        enc = CardEnc.atmost(lits=card, bound=W, top_id=p2.top, encoding=EncType.seqcounter)
        cl += enc.clauses
        with Cadical153(bootstrap_with=cl) as S:
            if S.solve():
                nsat += 1
                if best is None:
                    best = wi
    t3 = time.time()
    print(f"[{sector}] |E| = 12 decision over all {len(Wds)} logicals: "
          f"{nsat} admit a weight-<={W} extended-code solution ({t3-t2:.1f}s)")
    sys.stdout.flush()
    out[sector] = dict(n12=len(Wds), valid=bool(ok), same_as_pool=bool(same),
                       enum_seconds=round(t1 - t0, 1), nsat=nsat,
                       decide_seconds=round(t3 - t2, 1))
json.dump(out, open("enum12.json", "w"), indent=1)
