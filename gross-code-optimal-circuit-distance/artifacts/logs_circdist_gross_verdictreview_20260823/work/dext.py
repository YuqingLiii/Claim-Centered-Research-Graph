"""EXACT certification of d_ext(E(M)) for the gross code, by SAT decision queries.

d_ext(E(M)) = min { |x| : H^ext x = 0 , L^ext x != 0 }  where the extended code appends one column
per residual error (SBB Def. 2).  Written in the equivalent "net error" form:

    d_ext = min over  E in ker(H_det) \\ rowspace(H_stab)  and  R subset of the residual set  of
            | E  xor  (xor_{r in R} r) |  +  |R| .

Boolean model (Z-sector; X-sector is the mirror):
    z_j      j = 0..143     the net data error E
    u_{c,k}  c = 0..71, k = 0,1,2   residual k of check c is used
    d_j      j = 0..143     the data-fault part x_data = E xor (xor of used residuals)
constraints
    H_det z = 0                                   (72 XORs of weight 6)
    OR_i ( L_i . z = 1 )                          (12 XOR chains + one clause)
    d_j = z_j xor (xor of u_{c,k} with j in r_k(c))
    |d| + |u| <= W                                (cardinality)
UNSAT at W  =>  d_ext > W.   SAT at W  =>  an explicit witness of weight <= W.
"""
import numpy as np, itertools, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, Reducer, rref
import pool as poolmod

RES_POS = [(0, 1), (3, 4, 5), (4, 5)]     # r1 = {i1,i2}, r2 = {i4,i5,i6}, r3 = {i5,i6}


def residual_sets(orders):
    """orders: list of 72 within-check CNOT orders (each a list of 6 data-qubit indices).
    Returns res[c][k] = tuple of data qubits."""
    return [[tuple(o[p] for p in RES_POS[k]) for k in range(3)] for o in orders]


class Ctx:
    def __init__(self, orders, Hdet, Lrows):
        self.res = residual_sets(orders)
        self.Hdet = Hdet
        self.Lrows = Lrows
        # per data qubit: which (c,k) residuals contain it
        self.hit = [[] for _ in range(N)]
        for c in range(len(self.res)):
            for k in range(3):
                for q in self.res[c][k]:
                    self.hit[q].append((c, k))
        self.ncheck = len(self.res)


def xor_chain(pool, lits, cls):
    acc = lits[0]
    for x in lits[1:]:
        nv = pool.id()
        cls += [[-nv, acc, x], [-nv, -acc, -x], [nv, -acc, x], [nv, acc, -x]]
        acc = nv
    return acc


def xor_zero_direct(lits, cls):
    """forbid every odd-parity assignment (use only for short XORs)"""
    k = len(lits)
    for bits in itertools.product([0, 1], repeat=k):
        if sum(bits) % 2 == 1:
            cls.append([(-lits[i] if bits[i] else lits[i]) for i in range(k)])


def build(ctx, W, pin=None, use_residuals=True):
    pool = IDPool()
    z = [pool.id(('z', j)) for j in range(N)]
    u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
    d = [pool.id(('d', j)) for j in range(N)]
    cls = []
    # detector constraints
    for e in range(ctx.Hdet.shape[0]):
        supp = [z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]]
        xor_zero_direct(supp, cls)
    # logical nontriviality
    ys = []
    for i in range(ctx.Lrows.shape[0]):
        supp = [z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]]
        ys.append(xor_chain(pool, supp, cls))
    cls.append(ys)
    # data-fault definition
    lits_card = []
    for j in range(N):
        terms = [d[j], z[j]]
        if use_residuals:
            terms += [u[c][k] for (c, k) in ctx.hit[j]]
        if len(terms) <= 6:
            xor_zero_direct(terms, cls)
        else:
            v = xor_chain(pool, terms, cls)
            cls.append([-v])
        lits_card.append(d[j])
    if use_residuals:
        for c in range(ctx.ncheck):
            for k in range(3):
                lits_card.append(u[c][k])
    else:
        for c in range(ctx.ncheck):
            for k in range(3):
                cls.append([-u[c][k]])
    if pin is not None:
        cls.append([pin(z, u, d)])
    # cardinality
    top = pool.top
    cnf = CardEnc.atmost(lits=lits_card, bound=W, top_id=top, encoding=EncType.seqcounter)
    cls += cnf.clauses
    return cls, z, u, d, lits_card


def decode(model, z, u, d, ctx):
    ms = set(x for x in model if x > 0)
    E = np.array([1 if z[j] in ms else 0 for j in range(N)], np.uint8)
    R = [(c, k) for c in range(ctx.ncheck) for k in range(3) if u[c][k] in ms]
    D = np.array([1 if d[j] in ms else 0 for j in range(N)], np.uint8)
    return E, R, D


def verify_witness(ctx, E, R, D, Hstab):
    """independent re-verification of a SAT witness, from the definitions."""
    chk = np.zeros(N, np.uint8)
    for (c, k) in R:
        for q in ctx.res[c][k]:
            chk[q] ^= 1
    ok_d = np.array_equal((D ^ chk) % 2, E)
    ok_syn = not ((ctx.Hdet @ E) % 2).any()
    red = Reducer(Hstab)
    ok_log = not red.inspan(E)
    return dict(weight=int(D.sum()) + len(R), n_data=int(D.sum()), n_res=len(R),
                Ewt=int(E.sum()), decomposition_ok=bool(ok_d), zero_syndrome=bool(ok_syn),
                nontrivial_logical=bool(ok_log))


def query(ctx, W, Hstab, pin=None, use_residuals=True, verbose=False):
    cls, z, u, d, lc = build(ctx, W, pin=pin, use_residuals=use_residuals)
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        sat = S.solve()
        m = S.get_model() if sat else None
    el = time.time() - t0
    if not sat:
        return False, None, el, len(cls)
    E, R, D = decode(m, z, u, d, ctx)
    return True, (E, R, D, verify_witness(ctx, E, R, D, Hstab)), el, len(cls)


def sector_ctx(orders, sector):
    PZ, PX, LX, LZ = poolmod.get()
    if sector == 'Z':      # Z-type data errors, X-check detectors, Z-check hooks
        return Ctx(orders, HX, LX), HZ
    else:                  # X-type data errors, Z-check detectors, X-check hooks
        return Ctx(orders, HZ, LZ), HX
