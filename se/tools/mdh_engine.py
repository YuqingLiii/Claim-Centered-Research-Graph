"""Exact engine for the SE(n,2n) matrix dual-Hahn construction.

THE FRAME (gauge-fixed "t-picture", Rosmanis move):
  - NO instances  X_N = bijections [2n]->[2n]  (positions = [n] |_| [n], symbols = [2n]).
  - YES instances X_Y = pairs (f,g), injective [n]->[2n], im f = im g.
  - G = S_{2n}(symbols) x (S_n x S_n)(positions) x Z2(half swap).
  - Gauge fix: YES matching sigma_y = g^{-1} f = id  and NO column x0 = id.
    Then every G-equivariant Gamma <-> one function t on
        X_L = Inj([n] -> [2n])  ~  S_{2n} / S_n^{(2)},
    invariant under R = < l |-> (a,a)^{-1} o l o a  (a in S_n),   l |-> w o l >,
    where w = prod_i (i, n+i) swaps the two symbol halves.
  - Fourier blocks: for lam |- 2n,  t_hat(lam) = sum_l t(l) rho^lam(x_l) P_V,
    P_V = projector onto S_n^{(2)}-invariants V of S^lam.
    Contract columns against the Jucys-Murphy joint eigenspace
        W_N(mu,nu) = {w supported on SYT with first-n part = T0^mu,
                      X'_k w = content_{T0^nu}(k-n) w}          (dim = c^lam_{mu nu})
    and rows against  (mu (x) nu (x) V)^{S_n-diag}               (dim = m_Y)
    to get the m_Y x m_N block of Gamma at (lam; mu, nu).
  - The matrix dual-Hahn family = block-Jacobi data of M_phi, multiplication by
        phi(l) = #{i: l(i)=i} + #{i: l(i)=n+i}   (agreement count with x0),
    block-tridiagonal in level k(lam) = |lam| - lam_1.

All arithmetic exact (Fraction).  Representation: Young seminormal form (YSN).
"""
from fractions import Fraction
from itertools import permutations
import sys, json

F0 = Fraction(0)
F1 = Fraction(1)

# ---------------------------------------------------------------- partitions
def partitions(m, cap=None):
    if cap is None: cap = m
    if m == 0:
        yield ()
        return
    for first in range(min(m, cap), 0, -1):
        for rest in partitions(m - first, first):
            yield (first,) + rest

def hs(lam, a):
    """Is lam/a a horizontal strip?  (a inside lam, at most one box per column):
       lam_1 >= a_1 >= lam_2 >= a_2 >= ..."""
    la = list(lam); aa = list(a) + [0]*(len(lam)-len(a))
    if len(a) > len(lam): return False
    for i in range(len(la)):
        if not (la[i] >= aa[i]): return False
        if i+1 < len(la) and not (aa[i] >= la[i+1]): return False
    return True

def level(lam):
    return sum(lam) - lam[0]

# ---------------------------------------------------------------- SYT and YSN
def syt_list(lam):
    """All standard Young tableaux of shape lam; tableau = tuple of row-tuples."""
    m = sum(lam)
    res = []
    def rec(t, k):
        if k > m:
            res.append(tuple(tuple(r) for r in t)); return
        for r in range(len(lam)):
            c = len(t[r])
            if c < lam[r] and (r == 0 or len(t[r-1]) > c):
                t[r].append(k); rec(t, k+1); t[r].pop()
    rec([[] for _ in lam], 1)
    return res

class YSN:
    """Young seminormal representation of S_m for shape lam, over Fraction.
       Permutations are 0-indexed tuples p with p[i] = image of i.
       s_k (k = 0..m-2) is the transposition of {k, k+1} (0-indexed)."""
    def __init__(self, lam):
        self.lam = lam
        self.m = sum(lam)
        self.tabs = syt_list(lam)
        self.dim = len(self.tabs)
        self.idx = {t: i for i, t in enumerate(self.tabs)}
        # pos[t][e] = (row, col) of entry e+1 in tableau index t
        self.pos = []
        for t in self.tabs:
            p = {}
            for r, row in enumerate(t):
                for c, e in enumerate(row):
                    p[e] = (r, c)
            self.pos.append(p)
        # Sparse action of each adjacent transposition:
        # act[k][i] = list of (j, coeff): rho(s_k) e_i = sum coeff * e_j
        self.act = [self._build_s(k) for k in range(self.m - 1)]
        self.gram = self._build_gram()

    def _swap_tab(self, ti, k):
        """Tableau with entries k+1,k+2 swapped (1-indexed k+1,k+2 = s_k)."""
        t = [list(r) for r in self.tabs[ti]]
        (r1, c1) = self.pos[ti][k+1]; (r2, c2) = self.pos[ti][k+2]
        t[r1][c1], t[r2][c2] = t[r2][c2], t[r1][c1]
        return tuple(tuple(r) for r in t)

    def _build_s(self, k):
        cols = [None] * self.dim
        for i in range(self.dim):
            if cols[i] is not None: continue
            (r1, c1) = self.pos[i][k+1]; (r2, c2) = self.pos[i][k+2]
            d = (c2 - r2) - (c1 - r1)   # content(k+2) - content(k+1)
            if d == 1:      # same row, adjacent
                cols[i] = [(i, F1)]
            elif d == -1:   # same column
                cols[i] = [(i, -F1)]
            else:
                tj = self._swap_tab(i, k)
                j = self.idx[tj]
                # canonical member of the pair: the one where k+2 sits in a
                # strictly lower row than k+1
                if r2 > r1:
                    ci, cj, dd = i, j, Fraction(d)
                else:
                    ci, cj = j, i
                    (rr1, cc1) = self.pos[j][k+1]; (rr2, cc2) = self.pos[j][k+2]
                    dd = Fraction((cc2 - rr2) - (cc1 - rr1))
                inv = F1 / dd
                # e_ci -> inv e_ci + (1 - inv^2) e_cj ;  e_cj -> e_ci - inv e_cj
                cols[ci] = [(ci, inv), (cj, F1 - inv * inv)]
                cols[cj] = [(ci, F1), (cj, -inv)]
        return cols

    def _build_gram(self):
        """Diagonal invariant Gram: g_j = g_i * d^2/(d^2-1) across pair edges."""
        g = [None] * self.dim
        g[0] = F1
        stack = [0]
        while stack:
            i = stack.pop()
            for k in range(self.m - 1):
                col = self.act[k][i]
                if len(col) == 2:
                    (a, ca), (b, cb) = col
                    j = a if a != i else b
                    if g[j] is None:
                        # determine via orthogonality col_i^T G col_j = 0
                        # col_i = [(i,inv),(j,1-inv^2)] or [(i',1),(j',-inv)]
                        ci = dict(col); cj = dict(self.act[k][j])
                        # g_i*ci[i]*cj[i] + g_j*ci[j]*cj[j] = 0
                        num = g[i] * ci[i] * cj.get(i, F0)
                        den = ci[j] * cj.get(j, F0)
                        g[j] = -num / den
                        stack.append(j)
        assert all(x is not None and x > 0 for x in g), "Gram propagation failed"
        return g

    def apply_s(self, k, vec):
        """rho(s_k) @ vec for a dense Fraction vector."""
        out = [F0] * self.dim
        for i, v in enumerate(vec):
            if v:
                for j, c in self.act[k][i]:
                    out[j] += c * v
        return out

    def apply_s_mat(self, k, M):
        """rho(s_k) @ M for M = list of rows? We store M as list of column vectors."""
        return [self.apply_s(k, col) for col in M]

    def apply_word(self, word, vec):
        """Apply rho(s_{w[-1]}) ... rho(s_{w[0]})?  Convention: word w such that
           the permutation is p = s_{w[0]} o s_{w[1]} o ... (left to right compose),
           and rho(p) = rho(s_{w[0]}) @ rho(s_{w[1]}) @ ...  So apply reversed."""
        for k in reversed(word):
            vec = self.apply_s(k, vec)
        return vec

    def transposition_word(self, a, b):
        """Word for the transposition (a b), a<b, as adjacent transpositions:
           (a b) = s_a s_{a+1} ... s_{b-2} s_{b-1} s_{b-2} ... s_a  (0-indexed s)."""
        if a > b: a, b = b, a
        return list(range(a, b - 1)) + [b - 1] + list(range(b - 2, a - 1, -1))

def perm_word(p):
    """Decompose permutation p (0-indexed tuple) into adjacent transpositions:
       returns word w with p = s_{w[0]} o s_{w[1]} o ... o s_{w[-1]}  under
       composition (p o q)(i) = p[q[i]].  Built by sorting from the right."""
    arr = list(p)
    word = []
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                word.append(i)
                changed = True
    # After bubble sort, s_{w[last]} o ... o s_{w[0]} o p = id
    # => p = s_{w[0]}^{-1} o ... = s_{w[0]} o s_{w[1]} ... reversed order:
    return word[::-1]

def compose(p, q):
    """(p o q)(i) = p[q[i]]"""
    return tuple(p[q[i]] for i in range(len(p)))

def inv_perm(p):
    out = [0] * len(p)
    for i, v in enumerate(p): out[v] = i
    return tuple(out)

# -------------------------------------------------------------- linear algebra
def rref(rows, ncols):
    """Reduced row echelon form over Fraction. rows: list of lists. Returns
       (rref_rows, pivot_cols)."""
    rows = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        # find pivot
        pr = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0: pr = i; break
        if pr is None: continue
        rows[r], rows[pr] = rows[pr], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
        if r == len(rows): break
    return rows[:r], piv

def nullspace(mat, ncols):
    """Nullspace basis (canonical, from RREF) of mat (list of rows) over Fraction."""
    R, piv = rref(mat, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F0] * ncols
        v[fc] = F1
        for ri, pc in enumerate(piv):
            v[pc] = -R[ri][fc]
        basis.append(v)
    return basis

def mat_vec(M_rows, v):
    return [sum(a * b for a, b in zip(row, v) if b) for row in M_rows]

# --------------------------------------------------------------- coset space
class CosetSpace:
    """X_L = injections [n] -> [2n], as cosets x S_n^{(2)} with BFS tree."""
    def __init__(self, n):
        self.n = n
        m = 2 * n
        self.m = m
        # enumerate cosets by BFS from the identity injection
        start = tuple(range(n))
        self.ell = [start]
        self.index = {start: 0}
        # tree[i] = (parent, k) meaning x_i = s_k * x_parent  (left mult)
        self.tree = [None]
        frontier = [start]
        while frontier:
            nf = []
            for l in frontier:
                i = self.index[l]
                for k in range(m - 1):
                    # left multiply by s_k = transposition of symbols (k,k+1)
                    l2 = tuple(k + 1 if v == k else (k if v == k + 1 else v)
                               for v in l)
                    if l2 not in self.index:
                        self.index[l2] = len(self.ell)
                        self.ell.append(l2)
                        self.tree.append((i, k))
                        nf.append(l2)
            frontier = nf
        self.size = len(self.ell)

    def phi(self, l):
        n = self.n
        return sum(1 for i in range(n) if l[i] == i) + \
               sum(1 for i in range(n) if l[i] == n + i)

    def orbits(self):
        """R-orbits: generators conj-alpha (alpha adjacent transposition in S_n)
           and left-w."""
        n = self.n
        seen = {}
        orbs = []
        for l0 in self.ell:
            if l0 in seen: continue
            orb = [l0]; seen[l0] = len(orbs)
            stack = [l0]
            while stack:
                l = stack.pop()
                imgs = []
                # w o l
                imgs.append(tuple(v + n if v < n else v - n for v in l))
                for a in range(n - 1):
                    # alpha = s_a in S_n positions; (alpha,alpha)^{-1} o l o alpha
                    # symbol map: swap a<->a+1 and n+a <-> n+a+1
                    def sym(v):
                        if v == a: return a + 1
                        if v == a + 1: return a
                        if v == n + a: return n + a + 1
                        if v == n + a + 1: return n + a
                        return v
                    l2 = list(l)
                    l2[a], l2[a + 1] = l2[a + 1], l2[a]  # l o alpha
                    imgs.append(tuple(sym(v) for v in l2))
                for l2 in imgs:
                    if l2 not in seen:
                        seen[l2] = len(orbs); orb.append(l2); stack.append(l2)
            orbs.append(orb)
        return orbs, seen

# ------------------------------------------------------- per-lambda machinery
class LambdaData:
    """All exact block data for one lam |- 2n."""
    def __init__(self, lam, n, cosets):
        self.lam = lam
        self.n = n
        self.rep = YSN(lam)
        self.cosets = cosets
        self._build_V()

    def _build_V(self):
        """V = S_n^{(2)}-invariants of S^lam: kernel of rho(s_j)-I for
           j = n..2n-2 (0-indexed adjacent transpositions within the 2nd half)."""
        rep = self.rep; n = self.n
        rows = []
        d = rep.dim
        for j in range(n, 2 * n - 1):
            # rows of (rho(s_j) - I): build from columns
            M = [[F0] * d for _ in range(d)]
            for i in range(d):
                for jj, c in rep.act[j][i]:
                    M[jj][i] += c
                M[i][i] -= F1
            rows.extend(M)
        self.Vbasis = nullspace(rows, d)   # list of vectors (columns of Vb)
        self.dV = len(self.Vbasis)

    def check_dV(self):
        """dim V should be sum over a |- n with lam/a horizontal strip of dim(a)."""
        n = self.n
        tot = 0
        for a in partitions(n):
            if hs(self.lam, a):
                tot += len(syt_list(a))
        return tot == self.dV, tot

    def coset_slices(self, cols):
        """For a list of Fraction vectors cols (in S^lam), compute for every
           coset l the vectors rho(x_l) @ col, via the BFS tree.
           Returns per-coset list of per-col vectors? Too big; instead this is a
           generator: yields (coset_index, [vec for each col])."""
        rep = self.rep; cs = self.cosets
        store = [None] * cs.size
        store[0] = [list(c) for c in cols]
        yield 0, store[0]
        # BFS order = enumeration order (tree parents always earlier)
        for i in range(1, cs.size):
            par, k = cs.tree[i]
            store[i] = [rep.apply_s(k, v) for v in store[par]]
            yield i, store[i]
        # NOTE: keeps all slices in memory; fine for n<=4 (1680 x dim x #cols)

    def PV_apply(self, vec):
        """Project onto V: average over S_n^{(2)} = perms of symbols n..2n-1.
           Uses BFS over the subgroup with adjacent transpositions s_j, j>=n."""
        rep = self.rep; n = self.n
        # enumerate subgroup elements as words via BFS on permutations of [n..2n)
        # cheaper: solve linear projection: express via Vbasis using Gram.
        # P_V = Vb (Vb^T G Vb)^{-1} Vb^T G
        G = rep.gram
        Vb = self.Vbasis
        # compute M = Vb^T G vec  and  S = Vb^T G Vb
        tv = [sum(Vb[r][i] * G[i] * vec[i] for i in range(rep.dim)) for r in range(self.dV)]
        S = [[sum(Vb[r][i] * G[i] * Vb[s][i] for i in range(rep.dim))
              for s in range(self.dV)] for r in range(self.dV)]
        # solve S x = tv
        x = solve_linear(S, tv)
        out = [F0] * rep.dim
        for r, xr in enumerate(x):
            if xr:
                for i in range(rep.dim):
                    out[i] += xr * Vb[r][i]
        return out

def solve_linear(A, b):
    """Solve A x = b exactly (A square nonsingular list of rows)."""
    nn = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(nn):
        pr = next(i for i in range(c, nn) if M[i][c] != 0)
        M[c], M[pr] = M[pr], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(nn):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[c])]
    return [M[i][nn] for i in range(nn)]

# ------------------------------------------------------------------ self tests
def test_ysn(lam):
    rep = YSN(lam)
    m = rep.m; d = rep.dim
    # s_k^2 = 1
    for k in range(m - 1):
        for i in range(d):
            v = [F0] * d; v[i] = F1
            w = rep.apply_s(k, rep.apply_s(k, v))
            assert w == v, f"s_{k}^2 != 1 for {lam}"
    # braid
    for k in range(m - 2):
        for i in range(d):
            v = [F0] * d; v[i] = F1
            a = rep.apply_s(k, rep.apply_s(k + 1, rep.apply_s(k, v)))
            b = rep.apply_s(k + 1, rep.apply_s(k, rep.apply_s(k + 1, v)))
            assert a == b, f"braid fails for {lam} at {k}"
    # commuting
    for k in range(m - 1):
        for j in range(k + 2, m - 1):
            for i in range(min(d, 4)):
                v = [F0] * d; v[i] = F1
                a = rep.apply_s(k, rep.apply_s(j, v))
                b = rep.apply_s(j, rep.apply_s(k, v))
                assert a == b
    # Jucys-Murphy diagonality with content eigenvalues:
    # X_e = sum_{i<e} rho((i,e)) should be diagonal with eigenvalue content(e+1) in T
    for e in range(1, m):
        for ti in range(d):
            v = [F0] * d; v[ti] = F1
            acc = [F0] * d
            for i in range(e):
                w = rep.transposition_word(i, e)
                acc = [a + b for a, b in zip(acc, rep.apply_word(w, v[:]))]
            r, c = rep.pos[ti][e + 1]
            want = Fraction(c - r)
            ok = all(acc[j] == (want if j == ti else 0) or
                     (j == ti and acc[j] == want) for j in range(d))
            assert acc[ti] == want and all(acc[j] == 0 for j in range(d) if j != ti), \
                f"JM fails for {lam}, e={e}, T={ti}: got {acc}"
    # Gram invariance
    G = rep.gram
    for k in range(m - 1):
        for i in range(d):
            for j in range(i, d):
                # col_i^T G col_j
                ci = rep.act[k][i]; cj = rep.act[k][j]
                s = F0
                dj = dict(cj)
                for (a, ca) in ci:
                    if a in dj: s += ca * G[a] * dj[a]
                want = G[i] if i == j else F0
                assert s == want, f"Gram not invariant {lam} k={k}"
    return d

def run_basic_tests():
    print("YSN self-tests...")
    for lam in [(2,), (1, 1), (3,), (2, 1), (2, 2), (3, 1), (2, 1, 1),
                (4, 2), (3, 2, 1), (5, 2, 1)]:
        d = test_ysn(lam)
        print(f"  {lam}: dim {d} OK")
    print("Coset spaces / orbit counts:")
    for n, expect in [(2, 5), (3, 13), (4, 51)]:
        cs = CosetSpace(n)
        orbs, _ = cs.orbits()
        print(f"  n={n}: |X_L|={cs.size}, R-orbits={len(orbs)} (expect {expect})",
              "OK" if len(orbs) == expect else "MISMATCH")
    print("dim V checks (n=2,3):")
    for n in [2, 3]:
        cs = CosetSpace(n)
        for lam in partitions(2 * n):
            ld = LambdaData(lam, n, cs)
            ok, want = ld.check_dV()
            status = "OK" if ok else f"MISMATCH want {want} got {ld.dV}"
            print(f"  n={n} lam={lam}: dV={ld.dV} {status}")

if __name__ == "__main__":
    run_basic_tests()
