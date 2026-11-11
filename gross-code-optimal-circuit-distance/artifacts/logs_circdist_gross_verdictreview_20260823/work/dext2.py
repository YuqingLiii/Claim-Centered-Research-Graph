"""Faster exact d_ext certifier.

Three additions over dext.py:
  (1) the implied cut  |E| >= 12  (the gross code's own minimum logical weight, itself certified
      by validate1.py: UNSAT at 11 with the residual set switched off);
  (2) translation symmetry: the tiled assignment is invariant under the subgroup
      S <= G = Z_12 x Z_6 that preserves the colouring, so a minimum-weight solution may be assumed
      to use one of the |columns|/|S| orbit representatives.  Each representative is a separate
      incremental SAT call under one assumption literal;
  (3) incremental solving, so learnt clauses are shared across the orbit subproblems.

UNSAT on all orbit representatives at weight W  =>  d_ext > W   (certificate = the UNSAT proofs).
"""
import numpy as np, itertools, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, ELL, EM, gidx, Reducer
from dext import RES_POS, residual_sets, Ctx, xor_chain, xor_zero_direct, verify_witness


def group_elements():
    return [(a, b) for a in range(ELL) for b in range(EM)]


def data_perm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
            p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p


def check_perm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p


def stabiliser(phi, triple):
    """translations g with colour-class assignment preserved: triple[phi[c+g]] == triple[phi[c]]"""
    out = []
    for (a, b) in group_elements():
        cp = check_perm(a, b)
        if all(triple[int(phi[cp[c]])] == triple[int(phi[c])] for c in range(NG)):
            out.append((a, b))
    return out


def column_orbits(phi, triple):
    """orbits of the 360 extended-code columns (144 data + 72*3 residual) under the stabiliser"""
    S = stabiliser(phi, triple)
    lab = {}
    cols = [('d', j) for j in range(N)] + [('r', c, k) for c in range(NG) for k in range(3)]
    idx = {c: i for i, c in enumerate(cols)}
    seen = set(); orbits = []
    for col in cols:
        if col in seen:
            continue
        orb = set()
        for (a, b) in S:
            dp = data_perm(a, b); cp = check_perm(a, b)
            orb.add(('d', int(dp[col[1]])) if col[0] == 'd' else ('r', int(cp[col[1]]), col[2]))
        seen |= orb
        orbits.append((col, sorted(orb)))
    return S, orbits


class Cert:
    def __init__(self, ctx, W, emin=12):
        pool = IDPool()
        self.z = [pool.id(('z', j)) for j in range(N)]
        self.u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
        self.d = [pool.id(('d', j)) for j in range(N)]
        cls = []
        for e in range(ctx.Hdet.shape[0]):
            xor_zero_direct([self.z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]], cls)
        ys = []
        for i in range(ctx.Lrows.shape[0]):
            ys.append(xor_chain(pool, [self.z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]], cls))
        cls.append(ys)
        lits = []
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                v = xor_chain(pool, terms, cls)
                cls.append([-v])
            lits.append(self.d[j])
        for c in range(ctx.ncheck):
            for k in range(3):
                lits.append(self.u[c][k])
        # dominance cut (equisatisfiable): a check never needs both r2 = {i4,i5,i6} and
        # r3 = {i5,i6}.  Their net is {i4} at cost 2, strictly dominated by a single data fault
        # on i4 at cost 1; the same replacement removes the {r1,r2,r3} case.
        for c in range(ctx.ncheck):
            cls.append([-self.u[c][1], -self.u[c][2]])
        self.lits = lits
        top = pool.top
        c1 = CardEnc.atmost(lits=lits, bound=W, top_id=top, encoding=EncType.seqcounter)
        cls += c1.clauses
        top = max([top] + [abs(l) for cl in c1.clauses for l in cl])
        if emin:
            c2 = CardEnc.atleast(lits=self.z, bound=emin, top_id=top,
                                 encoding=EncType.seqcounter)
            cls += c2.clauses
            top = max([top] + [abs(l) for cl in c2.clauses for l in cl])
        self.top = top
        self.cls = cls
        self.ctx = ctx
        self.pool = pool

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def run(self, orbits, Hstab, budget=None, verbose=True):
        t0 = time.time()
        res = []
        with Cadical153(bootstrap_with=self.cls) as S:
            for oi, (rep, orb) in enumerate(orbits):
                # forbid all columns strictly "before" this orbit in the ordering (optional
                # strengthening is unsound in general; we only assume the representative is used)
                a = self.col_lit(rep)
                t1 = time.time()
                sat = S.solve(assumptions=[a])
                el = time.time() - t1
                if sat:
                    m = S.get_model()
                    ms = set(x for x in m if x > 0)
                    E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
                    R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3)
                         if self.u[c][k] in ms]
                    D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
                    info = verify_witness(self.ctx, E, R, D, Hstab)
                    if verbose:
                        print(f"      orbit {oi} rep {rep}: SAT in {el:.1f}s  {info}")
                    return True, (E, R, D, info), time.time() - t0
                if verbose:
                    print(f"      orbit {oi} rep {rep}: UNSAT in {el:.1f}s")
                res.append(el)
                if budget and time.time() - t0 > budget:
                    return None, ('timeout after orbit', oi), time.time() - t0
        return False, None, time.time() - t0
