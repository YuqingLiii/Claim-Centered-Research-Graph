"""(K, |E|)-split exact certifier for d_ext of a three-colour-tiled gross-code assignment.

Model (Z sector; X is the mirror), identical to dext.py/dext2.py:
    z_j      j=0..143      the net data error E
    u_{c,k}  c=0..71,k=0..2  residual k of check c used   (weights 2,3,2)
    d_j      j=0..143      the data-fault part,  d = E xor rho,  rho = xor of the used residuals
    weight   = |d| + |u|  <= W
constraints  H_det z = 0 ;  OR_i (L_i . z = 1) ;  d_j = z_j xor (xor of u hitting j).

The split adds, for a cell (K, Ew) with K = |u| and Ew = |E| :

  (c1)  |u| = K                                      (definition of the cell)
  (c2)  |z| = Ew                                     (definition of the cell)
  (c3)  |d| <= W - K                                 (from |d| + |u| <= W)
  (c4)  |rho| >= Ew - (W - K)                        (from |E| <= |d| + |rho|)
  (c5)  |rho| <= 3K                                  (each residual has weight <= 3)
  (c6)  n3 := #{c : u_{c,1}} >= Ew - W - K           (from |rho| <= 2K + n3 and (c4))
  (c7)  ~(u_{c,1} and u_{c,2})                       (dominance cut, as in dext2.Cert)

(c4)-(c6) are semantic consequences of the model, hence sound to add: every satisfying
assignment of the unsplit model with |u| = K and |z| = Ew satisfies them.  Cells are exhaustive:
Ew is even (all-ones lies in rowspace(H_det), so every E in ker(H_det) has even weight -- checked
in anchor1.py), Ew >= 12 (E is a nontrivial logical and d(gross) = 12, re-certified here), and
Ew <= W + 2K by (c4)+(c5).  K ranges over 0..W.  UNSAT on every cell certifies d_ext > W.
"""
import numpy as np, itertools, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, Reducer
from dext import xor_chain, xor_zero_direct, verify_witness


class Cert4:
    def __init__(self, ctx, W, K, Ew, dominance=True, use_rho=True):
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
        u3lits = [self.u[c][1] for c in range(ctx.ncheck)]
        # rho_j = z_j xor d_j
        self.rho = []
        if use_rho:
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

        # (c1)
        add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        if K > 0:
            add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        else:
            cls += [[-l] for l in ulits]
        # (c2)
        add(CardEnc.atmost(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        # (c3)
        add(CardEnc.atmost(lits=self.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
        # (c4), (c5)
        if use_rho:
            lo = Ew - (W - K)
            if lo > 0:
                add(CardEnc.atleast(lits=self.rho, bound=lo, top_id=top,
                                    encoding=EncType.seqcounter))
            if 3 * K < N:
                add(CardEnc.atmost(lits=self.rho, bound=3 * K, top_id=top,
                                   encoding=EncType.seqcounter))
        # (c6)
        n3lo = Ew - W - K
        if n3lo > 0:
            add(CardEnc.atleast(lits=u3lits, bound=n3lo, top_id=top,
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


def cells(W, Kmax=None):
    """all (K, Ew) cells that are arithmetically feasible."""
    out = []
    for K in range(0, (Kmax if Kmax is not None else W) + 1):
        for Ew in range(12, W + 2 * K + 1, 2):
            if Ew - W - K > K:          # (c6) with n3 <= K
                continue
            out.append((K, Ew))
    return out
