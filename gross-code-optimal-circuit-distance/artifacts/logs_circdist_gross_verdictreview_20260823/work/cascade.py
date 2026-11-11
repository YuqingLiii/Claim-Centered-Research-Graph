"""Reproduce SBB's pruning cascade 90 -> 45 -> ... -> 3 over THREE-COLOUR-TILED within-check
CNOT-order assignments, and identify the surviving assignment(s).

A tiled assignment is a triple (s_0, s_1, s_2) of within-check slot orders, one per colour class of
the checks.  Two orders give the same residual set iff they differ by the order-8 group
<swap(pos1,pos2), swap(pos5,pos6), global reversal>, so there are 6!/8 = 90 classes per colour and
90^3 = 729000 tiled assignments per sector -- exactly the count [SBB26 Prop. 6] prunes.

Every elimination below EXHIBITS a witness (a weight-12 logical plus one or two residual columns
whose total extended-code weight is <= 10), so the pruning is one-sided-sound: a surviving
assignment is a candidate, an eliminated one provably has d_ext <= 10.
"""
import numpy as np, itertools, sys
from collections import defaultdict
from gross import NG, N, zcheck_nb, xcheck_nb, HX, HZ, Reducer
from sched import make_phi, colour_valid
import pool as poolmod

PERMS = list(itertools.permutations(range(6)))


def order8(p):
    """the 8 orders with the same residual set as p"""
    out = set()
    for sw01 in (0, 1):
        for sw45 in (0, 1):
            q = list(p)
            if sw01:
                q[0], q[1] = q[1], q[0]
            if sw45:
                q[4], q[5] = q[5], q[4]
            out.add(tuple(q)); out.add(tuple(reversed(q)))
    return out


def build_classes():
    seen = set(); reps = []; cls_of = {}
    for p in PERMS:
        if p in seen:
            continue
        orb = order8(p)
        assert len(orb) == 8, (p, len(orb))
        idx = len(reps); reps.append(p)
        for q in orb:
            cls_of[q] = idx
        seen |= orb
    return reps, cls_of


REPS, CLS_OF = build_classes()
NCLS = len(REPS)
PAIRS = list(itertools.combinations(range(6), 2))          # slot pairs
TRIPS = list(itertools.combinations(range(6), 3))          # slot triples
PIDX = {p: i for i, p in enumerate(PAIRS)}
TIDX = {t: i for i, t in enumerate(TRIPS)}


def act_tables():
    """ACT2[class][pair]  : the order puts that slot-pair in positions {1,2} or {5,6}
       ACT3[class][triple]: the order puts that slot-triple in positions {4,5,6} or {1,2,3}"""
    A2 = np.zeros((NCLS, len(PAIRS)), bool)
    A3 = np.zeros((NCLS, len(TRIPS)), bool)
    for ci, p in enumerate(REPS):
        A2[ci, PIDX[tuple(sorted(p[0:2]))]] = True
        A2[ci, PIDX[tuple(sorted(p[4:6]))]] = True
        A3[ci, TIDX[tuple(sorted(p[3:6]))]] = True
        A3[ci, TIDX[tuple(sorted(p[0:3]))]] = True
    return A2, A3


ACT2, ACT3 = act_tables()


def sector_data(sector):
    PZ, PX, LX, LZ = poolmod.get()
    if sector == 'Z':
        nb = [zcheck_nb(g) for g in range(NG)]        # Z-check hooks, Z-type logicals
        Pl, Hstab, Hdet = PZ, HZ, HX
    else:
        nb = [xcheck_nb(g) for g in range(NG)]
        Pl, Hstab, Hdet = PX, HX, HZ
    slots = [[q for q, s, i in nb[g]] for g in range(NG)]   # canonical slot -> qubit
    return slots, Pl, Hstab, Hdet


def check_pool_closure(slots, Pl, Hstab):
    """for every pool logical L and check c with |L cap c| = 3, L+c must again be in the pool"""
    key = {v.tobytes() for v in Pl}
    red = Reducer(Hstab)
    bad = 0
    for L in Pl:
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) == 3:
                M = L.copy()
                for q in slots[c]:
                    M[q] ^= 1
                if M.tobytes() not in key:
                    bad += 1
    return bad


def collect_rules(sector, phi):
    slots, Pl, Hstab, Hdet = sector_data(sector)
    rules1 = set()      # (colour, triple-index)               -> gain 2, weight 10
    rules2 = set()      # ((c1,p1),(c2,p2)) sorted             -> gain 1+1 disjoint, weight 10
    for L in Pl:
        hits = []       # (colour, pair-index, frozenset of qubits)
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) < 2:
                continue
            col = int(phi[c])
            if len(S) == 3:
                rules1.add((col, TIDX[tuple(S)]))
            for P in itertools.combinations(S, 2):
                hits.append((col, PIDX[P], frozenset(slots[c][k] for k in P)))
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                if hits[i][2] & hits[j][2]:
                    continue
                a = (hits[i][0], hits[i][1]); b = (hits[j][0], hits[j][1])
                rules2.add((a, b) if a <= b else (b, a))
    return rules1, rules2


def survivors(rules1, rules2):
    alive = np.ones((NCLS, NCLS, NCLS), bool)
    # stage 1
    per_colour_ok = [np.ones(NCLS, bool) for _ in range(3)]
    for (col, ti) in rules1:
        per_colour_ok[col] &= ~ACT3[:, ti]
    for col in range(3):
        sh = [1, 1, 1]; sh[col] = NCLS
        alive &= per_colour_ok[col].reshape(sh)
    stage1 = [int(v.sum()) for v in per_colour_ok]
    after1 = int(alive.sum())
    # stage 2
    for (a, b) in rules2:
        (c1, p1), (c2, p2) = a, b
        m1 = ACT2[:, p1]; m2 = ACT2[:, p2]
        sh1 = [1, 1, 1]; sh1[c1] = NCLS
        sh2 = [1, 1, 1]; sh2[c2] = NCLS
        alive &= ~(m1.reshape(sh1) & m2.reshape(sh2))
    return alive, stage1, after1


if __name__ == "__main__":
    for sector in ('Z', 'X'):
        slots, Pl, Hstab, Hdet = sector_data(sector)
        print(f"=== sector {sector} ===  order classes: {NCLS}   pool: {len(Pl)}")
        print("   pool coset-closure violations (L, L+c for |L cap c|=3):",
              check_pool_closure(slots, Pl, Hstab))
        for (s, t) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            phi = make_phi(s, t)
            assert colour_valid(phi)
            r1, r2 = collect_rules(sector, phi)
            alive, stage1, after1 = survivors(r1, r2)
            idx = np.argwhere(alive)
            print(f"   phi={s}a+{t}b: per-colour survivors after stage 1 = {stage1} "
                  f"(=> {after1} triples), after stage 2 = {int(alive.sum())}"
                  f"   [{len(r1)} single-check rules, {len(r2)} pair rules]")
            if 0 < int(alive.sum()) <= 12:
                for v in idx:
                    print("        surviving assignment (order classes):", tuple(int(x) for x in v),
                          "orders:", [REPS[int(x)] for x in v])
