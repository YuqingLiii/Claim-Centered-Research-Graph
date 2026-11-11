"""
bb.py -- bivariate-bicycle qLDPC instance for ARM 2 (task-002).

n = 2*l*m qubits, left block L and right block R, each indexed by (i,j) in
Z_l x Z_m.  x = cyclic shift of i, y = cyclic shift of j.
A = sum of three monomials, B = sum of three monomials,
H_X = [A | B], H_Z = [B^T | A^T].  CSS holds because A and B commute.
Check weight 6, qubit degree 6 (3 X-checks and 3 Z-checks per qubit).

Schedule family searched (recorded as the search space):
  T = 6 time slots; every X-check sends its three L-CNOTs at the slots given by
  a bijection sigma_X on {A1,A2,A3,B1,B2,B3} -> {0..5} (monomial -> slot), and
  every Z-check likewise with sigma_Z on {B1^T,B2^T,B3^T,A1^T,A2^T,A3^T}.
  |family| = 6! * 6! = 518400.  Legality and (MC) are checked exactly.
"""

import itertools
import sat_core as S


def nullspace(rows, n):
    """basis of { v : <row,v> = 0 for all rows } as bitmasks."""
    basis_rows, pivots = S.rref(list(rows))          # reduced row echelon form
    pivset = set(pivots)
    free = [c for c in range(n) if c not in pivset]
    basis = []
    for fc in free:
        v = 1 << fc
        for r, p in zip(basis_rows, pivots):
            if (r >> fc) & 1:
                v |= 1 << p
        basis.append(v)
    for r in rows:
        for v in basis:
            assert S.popcount(r & v) % 2 == 0
    return basis


def independent_mod(vs, sub, n):
    """subset of vs independent modulo span(sub)."""
    Q = S.Quotient(sub, n)
    out, piv = [], {}
    for v in vs:
        cur = Q.cls(v)
        while cur:
            p = cur.bit_length() - 1
            if p in piv:
                cur ^= piv[p]
            else:
                piv[p] = cur
                out.append(v)
                break
    return out


def bb_code(l, m, Amon, Bmon):
    n2 = l * m
    n = 2 * n2
    idx = lambda i, j: (i % l) * m + (j % m)

    def mono(e, f, base):
        """image of basis vector under x^e y^f, as a permutation function"""
        return lambda i, j: (( i + e) % l, (j + f) % m)

    xchecks, zchecks = [], []
    for a in range(n2):
        i, j = divmod(a, m)
        s = 0
        for (e, f) in Amon:
            s |= 1 << idx(i + e, j + f)                  # L block
        for (e, f) in Bmon:
            s |= 1 << (n2 + idx(i + e, j + f))           # R block
        xchecks.append(s)
    for b in range(n2):
        i, j = divmod(b, m)
        s = 0
        for (e, f) in Bmon:
            s |= 1 << idx(i - e, j - f)                  # B^T on L
        for (e, f) in Amon:
            s |= 1 << (n2 + idx(i - e, j - f))           # A^T on R
        zchecks.append(s)
    kerZ = nullspace(zchecks, n)
    kerX = nullspace(xchecks, n)
    xl = independent_mod(kerZ, xchecks, n)
    zl = independent_mod(kerX, zchecks, n)
    code = S.Code(n, xchecks, zchecks, xl, zl, "BB_l%d_m%d" % (l, m))
    return code


def brute_distance(code, which="X"):
    """min weight in ker H_(other) \\ rowspace H_(this).  Exhaustive over the
    kernel, so exact (n small)."""
    checks = code.zchecks if which == "X" else code.xchecks
    sub = code.xchecks if which == "X" else code.zchecks
    ker = nullspace(checks, code.n)
    Q = S.Quotient(sub, code.n)
    best = 10 ** 9
    for msk in range(1, 1 << len(ker)):
        v = 0
        t = msk
        i = 0
        while t:
            if t & 1:
                v ^= ker[i]
            t >>= 1
            i += 1
        if Q.cls(v) != 0:
            best = min(best, S.popcount(v))
    return best


def build_schedule(code, l, m, Amon, Bmon, sigX, sigZ, name):
    """sigX: dict monomial-tag -> slot for X-checks ('A0','A1','A2','B0','B1','B2')
       sigZ: dict tag -> slot for Z-checks ('Bt0','Bt1','Bt2','At0','At1','At2')"""
    n2 = l * m
    idx = lambda i, j: (i % l) * m + (j % m)
    cn = []
    for a in range(n2):
        i, j = divmod(a, m)
        for s, (e, f) in enumerate(Amon):
            cn.append((sigX["A%d" % s], "X", a, idx(i + e, j + f)))
        for s, (e, f) in enumerate(Bmon):
            cn.append((sigX["B%d" % s], "X", a, n2 + idx(i + e, j + f)))
    for b in range(n2):
        i, j = divmod(b, m)
        for s, (e, f) in enumerate(Bmon):
            cn.append((sigZ["Bt%d" % s], "Z", b, idx(i - e, j - f)))
        for s, (e, f) in enumerate(Amon):
            cn.append((sigZ["At%d" % s], "Z", b, n2 + idx(i - e, j - f)))
    return S.Schedule(code, cn, name)


def search_schedules(code, l, m, Amon, Bmon, want=None, verbose=False):
    """Exhaustive scan of the 6!x6! family; returns (n_legal, n_legal_mc, list)."""
    tagsX = ["A0", "A1", "A2", "B0", "B1", "B2"]
    tagsZ = ["Bt0", "Bt1", "Bt2", "At0", "At1", "At2"]
    nlegal = nmc = 0
    keep = []
    for permX in itertools.permutations(range(6)):
        sigX = dict(zip(tagsX, permX))
        SA = {sigX["A0"], sigX["A1"], sigX["A2"]}
        SB = {sigX["B0"], sigX["B1"], sigX["B2"]}
        for permZ in itertools.permutations(range(6)):
            sigZ = dict(zip(tagsZ, permZ))
            TB = {sigZ["Bt0"], sigZ["Bt1"], sigZ["Bt2"]}
            TA = {sigZ["At0"], sigZ["At1"], sigZ["At2"]}
            if SA & TB or SB & TA:
                continue
            nlegal += 1
            sch = build_schedule(code, l, m, Amon, Bmon, sigX, sigZ, "cand")
            assert sch.legal_ok
            if sch.mc_ok:
                nmc += 1
                if want is None or len(keep) < want:
                    keep.append((dict(sigX), dict(sigZ)))
    return nlegal, nmc, keep
