"""Audit the cascade: every elimination must come with a real weight-10 witness.
For a sample of eliminated tiled assignments, materialise the witness the rule claims and verify it
end to end (F2 algebra + independent Pauli-frame circuit simulation)."""
import numpy as np, itertools, random
from gross import NG, N, HX, HZ, Reducer
from sched import make_phi
from cascade import REPS, sector_data, ACT2, ACT3, PAIRS, TRIPS, PIDX, TIDX, NCLS
from cert import tiled_orders
import simverify

RES_POS = [(0, 1), (3, 4, 5), (4, 5)]


def find_witness(sector, phi, triple):
    """search the weight-12 pool for a stage-1 or stage-2 witness of weight 10"""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    for L in Pl:
        hits = []
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) < 2:
                continue
            sig = REPS[triple[int(phi[c])]]
            # stage 1: r2 = positions 4,5,6 of the order, as slots
            r2 = tuple(sorted(sig[3:6]))
            if len(S) == 3 and r2 == tuple(S):
                return ('stage1', L, [(c, 1)])
            # stage 2 candidates: r1 (positions 1,2) and r3 (positions 5,6)
            for k, pos in ((0, (0, 1)), (2, (4, 5))):
                P = tuple(sorted(sig[p] for p in pos))
                if all(p in S for p in P):
                    hits.append((c, k, frozenset(slots[c][p] for p in P)))
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                if not (hits[i][2] & hits[j][2]):
                    return ('stage2', L, [(hits[i][0], hits[i][1]), (hits[j][0], hits[j][1])])
    return None


def audit(sector, phi, triple):
    res = find_witness(sector, phi, triple)
    if res is None:
        return None
    kind, L, R = res
    orders, _ = tiled_orders(sector, phi, triple)
    nets = np.zeros(N, np.uint8)
    for (c, k) in R:
        for p in RES_POS[k]:
            nets[orders[c][p]] ^= 1
    D = (L ^ nets) % 2
    w = int(D.sum()) + len(R)
    Hdet = HX if sector == 'Z' else HZ
    Hstab = HZ if sector == 'Z' else HX
    ok = dict(kind=kind, weight=w, Ewt=int(L.sum()),
              zero_syndrome=not ((Hdet @ L) % 2).any(),
              nontrivial=not Reducer(Hstab).inspan(L))
    if sector == 'Z':
        ok['circuit'] = simverify.verify(orders, R, [int(i) for i in np.nonzero(D)[0]],
                                         verbose=False)
    return ok


if __name__ == "__main__":
    phi = make_phi(1, 2)
    random.seed(0)
    trips = [(a, b, c) for a in range(NCLS) for b in range(NCLS) for c in range(NCLS)]
    alive = {(2, 2, 2), (2, 2, 9), (2, 9, 2), (2, 9, 9), (9, 2, 2), (9, 2, 9), (9, 9, 2), (9, 9, 9)}
    sample = [t for t in random.sample(trips, 400) if t not in alive][:10]
    for t in sample:
        print(t, audit('Z', phi, t))
