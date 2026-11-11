"""Realisability, done correctly: only the RESIDUAL SET of each check is prescribed, not a
particular representative of its order class.

A within-check order class is fixed by  (P, s3, s4, Q)  up to the reversal  (P,s3,s4,Q) -> (Q,s4,s3,P),
where P = {positions 1,2}, Q = {positions 5,6} as unordered slot pairs.  So the schedule is free to
choose the order inside P, the order inside Q, and the orientation.  Constraints:

  legality  : each check's 6 CNOTs in 6 distinct layers; each data qubit's 6 CNOTs in 6 distinct layers
  class     : the precedence pattern above, with a per-check orientation selector
  (MC)      : the even back-propagation parity condition on all 648 overlapping (X,Z) check pairs
"""
import sys, time, itertools
import numpy as np
from pysat.solvers import Cadical153
from gross import NG, N, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
from sched import make_phi, check_legal, mc_violations
from cascade import REPS
from cert import tiled_orders

EID = {}; EDGES = []
for g in range(NG):
    for q, s, i in xcheck_nb(g):
        EID[('X', g, s, i)] = len(EDGES); EDGES.append(('X', g, s, i, q))
for g in range(NG):
    for q, s, i in zcheck_nb(g):
        EID[('Z', g, s, i)] = len(EDGES); EDGES.append(('Z', g, s, i, q))
XSLOT = [{q: (s, i) for q, s, i in xcheck_nb(g)} for g in range(NG)]
ZSLOT = [{q: (s, i) for q, s, i in zcheck_nb(g)} for g in range(NG)]
NE = len(EDGES)


def prec_pairs(sig):
    """pairwise precedences that pin the residual class of the order `sig` (slot tuple)."""
    P = [sig[0], sig[1]]; s3, s4 = sig[2], sig[3]; Q = [sig[4], sig[5]]
    out = []
    for p in P:
        for b in [s3, s4] + Q:
            out.append((p, b))
    out += [(s3, s4)] + [(s3, q) for q in Q] + [(s4, q) for q in Q]
    return out


def solve(sigZ, sigX, T, use_mc=True, use_class=True):
    """sigZ[g], sigX[g] : the slot order whose residual CLASS the check must realise."""
    nv = NE * T

    def V(e, l):
        return e * T + l + 1
    sel = {}
    nxt = nv + 1
    cls = []
    for e in range(NE):
        cls.append([V(e, l) for l in range(T)])
        for l1, l2 in itertools.combinations(range(T), 2):
            cls.append([-V(e, l1), -V(e, l2)])
    if use_class:
        for typ, sigs, slot in (('X', sigX, XSLOT), ('Z', sigZ, ZSLOT)):
            for g in range(NG):
                f = nxt; nxt += 1
                sel[(typ, g)] = f
                nb = xcheck_nb(g) if typ == 'X' else zcheck_nb(g)
                e_of = [EID[(typ, g, s, i)] for q, s, i in nb]     # slot index -> edge id
                sig = sigs[g]
                rev = tuple(reversed(sig))
                for orient, lit in ((sig, -f), (rev, f)):
                    for (a, b) in prec_pairs(orient):
                        ea, eb = e_of[a], e_of[b]
                        for l1 in range(T):
                            for l2 in range(T):
                                if l1 >= l2:
                                    cls.append([lit, -V(ea, l1), -V(eb, l2)])
    for g in range(NG):
        for typ, nb in (('X', xcheck_nb(g)), ('Z', zcheck_nb(g))):
            grp = [EID[(typ, g, s, i)] for q, s, i in nb]
            for l in range(T):
                for e1, e2 in itertools.combinations(grp, 2):
                    cls.append([-V(e1, l), -V(e2, l)])
    for q in range(N):
        grp = [EID[('X', c, s, i)] for c, s, i in xchecks_of(q)] + \
              [EID[('Z', c, s, i)] for c, s, i in zchecks_of(q)]
        for l in range(T):
            for e1, e2 in itertools.combinations(grp, 2):
                cls.append([-V(e1, l), -V(e2, l)])
    if use_mc:
        for a in range(NG):
            for b in range(NG):
                sh = sorted(set(XSLOT[a]) & set(ZSLOT[b]))
                if not sh:
                    continue
                qL, qR = sh
                eA = EID[('X', a) + XSLOT[a][qL]]; eP = EID[('Z', b) + ZSLOT[b][qL]]
                eB = EID[('X', a) + XSLOT[a][qR]]; eQ = EID[('Z', b) + ZSLOT[b][qR]]
                for l1 in range(T):
                    for l2 in range(T):
                        if l1 == l2:
                            continue
                        for l3 in range(T):
                            for l4 in range(T):
                                if l3 == l4:
                                    continue
                                if (l1 < l2) != (l3 < l4):
                                    cls.append([-V(eP, l1), -V(eA, l2), -V(eQ, l3), -V(eB, l4)])
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        sat = S.solve(); m = S.get_model() if sat else None
    el = time.time() - t0
    if not sat:
        return None, len(cls), el
    ms = set(x for x in m if x > 0)
    tX = [dict() for _ in range(NG)]; tZ = [dict() for _ in range(NG)]
    for e, (typ, g, s, i, q) in enumerate(EDGES):
        for l in range(T):
            if V(e, l) in ms:
                (tX if typ == 'X' else tZ)[g][(s, i)] = l + 1
    return (tX, tZ), len(cls), el


def residual_class(order, slots_of_check):
    from cascade import CLS_OF
    inv = {q: k for k, q in enumerate(slots_of_check)}
    return CLS_OF[tuple(inv[q] for q in order)]


if __name__ == "__main__":
    phi = make_phi(1, 2)
    trip = tuple(int(c) for c in sys.argv[1].split(',')) if len(sys.argv) > 1 else (2, 2, 9)
    sigZ = [REPS[trip[int(phi[g])]] for g in range(NG)]
    sigX = [REPS[trip[int(phi[g])]] for g in range(NG)]
    for mc in (False, True):
        for T in (6, 7, 8, 9, 10):
            res, ncls, el = solve(sigZ, sigX, T, use_mc=mc)
            tag = "legality+class" + ("+MC" if mc else "")
            if res is None:
                print(f"{tag}, T={T}: UNSAT ({ncls} clauses, {el:.1f}s)")
            else:
                tX, tZ = res
                oX = [[q for q, s, i in sorted(xcheck_nb(g), key=lambda z: tX[g][(z[1], z[2])])]
                      for g in range(NG)]
                oZ = [[q for q, s, i in sorted(zcheck_nb(g), key=lambda z: tZ[g][(z[1], z[2])])]
                      for g in range(NG)]
                clsZ = {residual_class(oZ[g], [q for q, s, i in zcheck_nb(g)]) for g in range(NG)}
                clsX = {residual_class(oX[g], [q for q, s, i in xcheck_nb(g)]) for g in range(NG)}
                print(f"{tag}, T={T}: SAT ({ncls} clauses, {el:.1f}s) legal="
                      f"{check_legal(tX, tZ, T)} MCviol={mc_violations(tX, tZ)[0]} "
                      f"realised Z-classes={sorted(clsZ)} X-classes={sorted(clsX)}")
                break
            sys.stdout.flush()
