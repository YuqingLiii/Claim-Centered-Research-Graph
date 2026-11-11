"""Is there a legal, measurement-consistent gross-code SEC of depth T in which EVERY check avoids
the 45 residual classes that force d_ext <= 10?

The stage-1 condition is local and order-theoretic: a check forces d_ext <= 10 as soon as the
3-element slot set occupying its last three CNOT positions is a *covered* triple, i.e. lies in a
weight-12 logical.  Exactly 10 of the 20 triples of a check support are covered, and coverage is
complement-closed, so the condition to avoid is:  "the last three positions carry a covered triple".

UNSAT at depth T  =>  EVERY legal, measurement-consistent gross SEC with T CNOT layers has a check
whose single-check residual subset already yields an extended-code codeword of weight 10, hence
(SBB Thm. 1)  d_circ <= 10  for it if it is non-interleaved.
"""
import sys, time, itertools
import numpy as np
from pysat.solvers import Cadical153
from gross import NG, N, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
from sched import check_legal, mc_violations
from cascade import sector_data

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


def covered_triples(sector):
    """slot-triples of a check that lie inside some weight-12 logical (same for every check by
    translation transitivity -- asserted)."""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    S = np.array([[L[slots[0][k]] for k in range(6)] for L in Pl], bool)
    cov = [t for t in itertools.combinations(range(6), 3) if S[:, list(t)].all(1).any()]
    for c in (1, 2, 37):
        Sc = np.array([[L[slots[c][k]] for k in range(6)] for L in Pl], bool)
        covc = [t for t in itertools.combinations(range(6), 3) if Sc[:, list(t)].all(1).any()]
        assert covc == cov, (c, covc, cov)
    return cov


def solve(T, use_mc=True, use_nogo=True, quiet=False):
    def V(e, l):
        return e * T + l + 1
    nxt = NE * T + 1
    cls = []
    for e in range(NE):
        cls.append([V(e, l) for l in range(T)])
        for l1, l2 in itertools.combinations(range(T), 2):
            cls.append([-V(e, l1), -V(e, l2)])
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
    if use_nogo:
        covZ = covered_triples('Z'); covX = covered_triples('X')
        if not quiet:
            print(f"   covered triples: Z {len(covZ)}/20, X {len(covX)}/20")
        for typ, nb_fn, cov in (('X', xcheck_nb, covX), ('Z', zcheck_nb, covZ)):
            for g in range(NG):
                e_of = [EID[(typ, g, s, i)] for q, s, i in nb_fn(g)]
                y = {}
                for a, b in itertools.combinations(range(6), 2):
                    v = nxt; nxt += 1
                    y[(a, b)] = v
                    ea, eb = e_of[a], e_of[b]
                    for l1 in range(T):
                        for l2 in range(T):
                            if l1 == l2:
                                continue
                            cls.append([-V(ea, l1), -V(eb, l2), v if l1 < l2 else -v])

                def yy(a, b):          # [layer(a) < layer(b)]
                    return y[(a, b)] if a < b else -y[(b, a)]
                for Tr in cov:
                    comp = [k for k in range(6) if k not in Tr]
                    # forbid "all of comp precede all of Tr"
                    cls.append([yy(t, tp) for t in Tr for tp in comp])
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


if __name__ == "__main__":
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (6, 12)
    for T in range(lo, hi + 1):
        res, ncls, el = solve(T)
        if res is None:
            print(f"legal + MC + no-covered-triple-last, T={T}: UNSAT ({ncls} clauses, {el:.1f}s)")
        else:
            tX, tZ = res
            print(f"legal + MC + no-covered-triple-last, T={T}: SAT ({ncls} clauses, {el:.1f}s) "
                  f"legal={check_legal(tX, tZ, T)} MCviol={mc_violations(tX, tZ)[0]}")
            np.save(f"nogo_T{T}_tX.npy", np.array([[tX[g][(s, i)] for s in ('L', 'R')
                                                   for i in range(3)] for g in range(NG)]))
            np.save(f"nogo_T{T}_tZ.npy", np.array([[tZ[g][(s, i)] for s in ('L', 'R')
                                                   for i in range(3)] for g in range(NG)]))
            break
        sys.stdout.flush()
