"""cert4 with the residual-weight cut in its exact, joint form.

Write n2 = #{(c,k) in R : k in {0,2}} (the weight-2 residuals r1, r3) and n3 = #{(c,k) in R : k = 1}
(the weight-3 residual r2), so K = n2 + n3.  Then

     |rho| = | XOR of the chosen residuals |  <=  2 n2 + 3 n3  =  2K + n3  =  3K - n2 ,

i.e. the single cardinality constraint

  (c4')   sum_j rho_j  +  sum_c ( u_{c,0} + u_{c,2} )   <=   3K            [144 + 144 literals]

which is exact, subsumes cert4's (c5) |rho| <= 3K and (c6) n3 >= Ew - W - K, and -- unlike (c6) --
keeps biting for every value of |rho|, not only the extreme one.  Its encoding is small because the
bound 3K <= 30 is small.

Everything else is cert4.Cert4 verbatim: (c1) |u| = K, (c2) |z| = Ew, (c3) |d| <= W - K,
(c5') |rho| >= Ew - (W - K), (c7) the dominance cut.
"""
import numpy as np
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import N
from dext import xor_chain, xor_zero_direct


class Cert5:
    def __init__(self, ctx, W, K, Ew, dominance=True):
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
        ulits = [self.u[c][k] for c in range(ctx.ncheck) for k in range(3)]
        u2lits = [self.u[c][k] for c in range(ctx.ncheck) for k in (0, 2)]
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
        add(CardEnc.atmost(lits=self.rho + u2lits, bound=3 * K, top_id=top,
                           encoding=EncType.seqcounter))
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
