"""cert4 plus the LEX-MINIMALITY cut, which is what actually makes the |E| >= 14 strata cheap.

Take the decision question "is there a solution of weight <= W?".  If the answer is yes, there is a
solution x* = (E, R, d) minimising (weight, |R|) lexicographically among all solutions of weight
<= W.  Fix any r in R and drop it: x' = (E, R \\ {r}, d xor r) is again a solution (E is unchanged,
so the syndrome is still zero and the logical still non-trivial), with |R'| = |R| - 1 and
weight' = |d xor r| + |R| - 1.  Since |R'| < |R|, x' beats x* lexicographically as soon as
weight' <= weight, so minimality forces weight' > weight, i.e.

        |d xor r| >= |d| + 2   <=>   |r| - 2 |d cap r| >= 2 .

Residual weights are 2, 3, 2, so in both cases this forces |d cap r| = 0:

  (c8)   u_{c,k}  =>  d_q = 0   for every q in r_k(c)          (~500 binary clauses)

and hence, since d_j = 1 now implies that no used residual covers j and therefore rho_j = 0,

  (c9)   d_j  =>  z_j                                          (144 binary clauses)

i.e. d is DISJOINT from every used residual and CONTAINED in E, so E = d (disjoint union) rho and
|E| = |d| + |rho| exactly.

Soundness for the decision question: (c8)/(c9) can remove solutions, but never all of them -- the
lex-minimal solution survives, and it lies in the cell (K, Ew) given by its own |R| and |E|, both of
which the sweep enumerates.  So UNSAT on every cell still certifies d_ext > W.  (Validated on real
data in redwit.py: every known weight-10 witness reduces, by iterating the drop step above, to a
weight-<=10 solution that satisfies (c8) and (c9).)

Everything else is cert4.Cert4 verbatim.
"""
import numpy as np
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import N
from dext import xor_chain, xor_zero_direct


class Cert6:
    def __init__(self, ctx, W, K, Ew, dominance=True, lexmin=True):
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
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                cls.append([-xor_chain(pool, terms, cls)])
        if dominance:
            for c in range(ctx.ncheck):
                cls.append([-self.u[c][1], -self.u[c][2]])
        if lexmin:
            for c in range(ctx.ncheck):
                for k in range(3):
                    for q in ctx.res[c][k]:
                        cls.append([-self.u[c][k], -self.d[int(q)]])          # (c8)
            for j in range(N):
                cls.append([-self.d[j], self.z[j]])                            # (c9)
        ulits = [self.u[c][k] for c in range(ctx.ncheck) for k in range(3)]
        u3lits = [self.u[c][1] for c in range(ctx.ncheck)]
        self.rho = []
        for j in range(N):
            r = pool.id(('r', j))
            a, b = self.z[j], self.d[j]
            cls += [[-r, a, b], [-r, -a, -b], [r, -a, b], [r, a, -b]]
            self.rho.append(r)
        top = pool.top

        def add(enc):
            nonlocal cls, top
            cls += enc.clauses
            top = max([top] + [abs(l) for cl in enc.clauses for l in cl])

        add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
        lo = Ew - (W - K)
        if lo > 0:
            add(CardEnc.atleast(lits=self.rho, bound=lo, top_id=top, encoding=EncType.seqcounter))
        if 3 * K < N:
            add(CardEnc.atmost(lits=self.rho, bound=3 * K, top_id=top, encoding=EncType.seqcounter))
        n3lo = Ew - W - K
        if n3lo > 0:
            add(CardEnc.atleast(lits=u3lits, bound=n3lo, top_id=top, encoding=EncType.seqcounter))
        self.cls = cls
        self.top = top
        self.ctx = ctx

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def decode(self, model):
        ms = set(x for x in model if x > 0)
        E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
        R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3) if self.u[c][k] in ms]
        D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
        return E, R, D
