"""Block extraction for the SE(n,2n) invariant algebra in the t-picture.

For each lam |- 2n and ordered pair (mu, nu) of partitions of n:
  columns:  W_N(mu,nu) = joint JM eigenspace  (dim = c^lam_{mu,nu}, LR side)
  rows:     (mu (x) nu (x) V)^{S_n-diag}      (dim = m_Y, Kronecker+Pieri side)
  B_o[r,c] = z_r^T G  ( sum_{l in orbit o} rho(x_l) P_V w_c )

Swap operators:
  S_col = rho(omega) restricted to W_N  (omega = prod (i, n+i)); maps
          W_N(mu,nu) -> W_N(nu,mu).
  S_row = factor swap Phi[p,q,m] -> Phi[q,p,m] (mu=nu), possibly x V-side twist.
"""
import math
from fractions import Fraction
from mdh_engine import (YSN, CosetSpace, LambdaData, partitions, hs, level,
                        syt_list, nullspace, rref, solve_linear, F0, F1,
                        perm_word, compose, inv_perm)

# ------------------------------------------------------------------ characters
def char_table_Sn(n):
    """chi^lam(class) for lam |- n, classes = partitions of n (cycle types).
       Computed as YSN traces of class representatives. Returns dict
       lam -> dict cycletype -> int, plus class sizes."""
    import math
    parts = list(partitions(n))
    # class representative permutation for cycle type ct (0-indexed)
    def rep_perm(ct):
        p = []
        start = 0
        for c in ct:
            cyc = list(range(start, start + c))
            for i in range(c):
                p.append(cyc[(i + 1) % c] + 0)
            start += c
        # p currently maps position start.. within blocks; build proper tuple
        out = [0] * n
        start = 0
        for c in ct:
            for i in range(c):
                out[start + i] = start + (i + 1) % c
            start += c
        return tuple(out)
    def class_size(ct):
        cnt = {}
        for c in ct: cnt[c] = cnt.get(c, 0) + 1
        denom = 1
        for c, k in cnt.items():
            denom *= (c ** k) * math.factorial(k)
        return math.factorial(n) // denom
    table = {}
    for lam in parts:
        rep = YSN(lam)
        row = {}
        for ct in parts:
            p = rep_perm(ct)
            w = perm_word(p)
            tr = F0
            for i in range(rep.dim):
                v = [F0] * rep.dim; v[i] = F1
                v = rep.apply_word(w, v)
                tr += v[i]
            assert tr.denominator == 1
            row[ct] = int(tr)
        table[lam] = row
    sizes = {ct: class_size(ct) for ct in parts}
    return table, sizes

def kronecker_g(table, sizes, n, a, mu, nu):
    import math
    s = 0
    for ct, sz in sizes.items():
        s += sz * table[a][ct] * table[mu][ct] * table[nu][ct]
    q, r = divmod(s, math.factorial(n))
    assert r == 0
    return q

# ------------------------------------------------------- lambda-block machinery
class BlockEngine:
    def __init__(self, n, lam, cosets=None):
        self.n = n
        self.lam = lam
        self.cs = cosets if cosets is not None else CosetSpace(n)
        self.ld = LambdaData(lam, n, self.cs)
        self.rep = self.ld.rep
        ok, want = self.ld.check_dV()
        assert ok, f"dV mismatch for {lam}"
        self._build_V_action()

    def _build_V_action(self):
        """A_k (dV x dV) with rho(s_k) Vb = Vb A_k for k = 0..n-2 (first-half
           adjacent transpositions), and the V-Gram S = Vb^T G Vb."""
        rep, ld = self.rep, self.ld
        Vb = ld.Vbasis
        dV, d = ld.dV, rep.dim
        G = rep.gram
        S = [[sum(Vb[r][i] * G[i] * Vb[s][i] for i in range(d))
              for s in range(dV)] for r in range(dV)]
        self.VGram = S
        self.Vact = []
        for k in range(self.n - 1):
            cols = []
            for r in range(dV):
                w = rep.apply_s(k, Vb[r])
                tv = [sum(Vb[q][i] * G[i] * w[i] for i in range(d)) for q in range(dV)]
                x = solve_linear([row[:] for row in S], tv)
                cols.append(x)   # coordinates of rho(s_k) Vb[r] in Vb
            # A_k[i][j] = coeff of Vb[i] in rho(s_k)Vb[j]
            self.Vact.append([[cols[j][i] for j in range(dV)] for i in range(dV)])

    # ---------------- columns: W_N(mu,nu) --------------------------------
    def columns(self, mu, nu):
        """Canonical basis (RREF) of W_N(mu,nu) inside S^lam."""
        rep, n = self.rep, self.n
        Tmu = syt_list(mu)[0]   # superstandard (row-reading) tableau
        Tnu = syt_list(nu)[0]
        # entry e (1-indexed) of T0^mu sits at pos -> content
        posmu = {}
        for r, row in enumerate(Tmu):
            for c, e in enumerate(row):
                posmu[e] = c - r
        posnu = {}
        for r, row in enumerate(Tnu):
            for c, e in enumerate(row):
                posnu[e] = c - r
        # coordinate subset: SYT whose entries 1..n form exactly T0^mu
        Ssub = []
        for ti, t in enumerate(rep.tabs):
            sub = tuple(tuple(e for e in row if e <= n) for row in t)
            sub = tuple(r for r in sub if r)
            if sub == Tmu:
                Ssub.append(ti)
        if not Ssub:
            return []
        # build X'_e restricted to span(Ssub) for e = n+1..2n-1 (1-indexed
        # elements n+2..2n <-> 0-indexed e0 = n+1..2n-1)
        pos_in_sub = {ti: i for i, ti in enumerate(Ssub)}
        ds = len(Ssub)
        conds = []
        for e0 in range(n + 1, 2 * n):        # 0-indexed element
            target = Fraction(posnu[e0 - n + 1])
            M = [[F0] * ds for _ in range(ds)]
            for ci, ti in enumerate(Ssub):
                v = [F0] * rep.dim; v[ti] = F1
                acc = [F0] * rep.dim
                for i0 in range(n, e0):
                    w = rep.transposition_word(i0, e0)
                    acc2 = rep.apply_word(w, v[:])
                    acc = [a + b for a, b in zip(acc, acc2)]
                for tj, val in enumerate(acc):
                    if val:
                        assert tj in pos_in_sub, "X' left the subspace!"
                        M[pos_in_sub[tj]][ci] += val
                M[ci][ci] -= target
            conds.extend(M)
        sol = nullspace(conds, ds)
        # lift back to S^lam coordinates
        out = []
        for v in sol:
            w = [F0] * rep.dim
            for i, ti in enumerate(Ssub):
                w[ti] = v[i]
            out.append(w)
        return out

    # ---------------- rows: (mu x nu x V)^Delta ---------------------------
    def rows(self, mu, nu, repmu=None, repnu=None):
        n = self.n
        rmu = repmu if repmu is not None else YSN(mu)
        rnu = repnu if repnu is not None else YSN(nu)
        dm, dn, dV = rmu.dim, rnu.dim, self.ld.dV
        N = dm * dn * dV
        conds = []
        for k in range(n - 1):
            # (rho_mu(s_k) x rho_nu(s_k) x A_k) Phi = Phi
            Ak = self.Vact[k]
            M = [[F0] * N for _ in range(N)]
            for p in range(dm):
                colp = rmu.act[k][p]
                for q in range(dn):
                    colq = rnu.act[k][q]
                    for m in range(dV):
                        src = (p * dn + q) * dV + m
                        for (pp, cp) in colp:
                            for (qq, cq) in colq:
                                for mm in range(dV):
                                    cA = Ak[mm][m]
                                    if cA:
                                        dst = (pp * dn + qq) * dV + mm
                                        M[dst][src] += cp * cq * cA
                        M[src][src] -= F1
            conds.extend(M)
        sol = nullspace(conds, N)
        return sol, rmu, rnu

    # ---------------- orbit block images ---------------------------------
    def _row_seed_vectors(self, mu, nu, rowsol, rnu):
        """z_r = sum_m Phi_r[0,0,m] Vb[m]  (seed = first tableau of mu, nu)."""
        rep, ld = self.rep, self.ld
        d, dV = rep.dim, ld.dV
        Vb = ld.Vbasis
        dn = rnu.dim
        zs = []
        for Phi in rowsol:
            z = [F0] * d
            for m in range(dV):
                coeff = Phi[(0 * dn + 0) * dV + m]
                if coeff:
                    for i in range(d):
                        z[i] += coeff * Vb[m][i]
            zs.append(z)
        return zs

    def _column_components(self, mu, nu, cols, rmu, rnu):
        """Schur transfer: for each column copy c (seeded at the (T0mu,T0nu)
           GT-component w_c), reconstruct ALL components
             w^{pq}_c = (dmu*dnu/(n!)^2) sum_{al,be} [rho_mu(al^-1)]_{0p}
                        [rho_nu(be^-1)]_{0q} rho_lam(iota(al,be)) w_c .
           Returns comp[c][p][q] = vector in S^lam."""
        import itertools as it
        from mdh_engine import perm_word
        rep, n = self.rep, self.n
        d = rep.dim
        dm, dn = rmu.dim, rnu.dim
        fact = math.factorial(n)
        comp = [[[[F0] * d for _ in range(dn)] for _ in range(dm)]
                for _ in cols]
        # precompute small-rep matrices for all alpha in S_n
        perms_n = list(it.permutations(range(n)))
        def rep_mat(r, p):
            w = perm_word(p)
            M = []
            for i in range(r.dim):
                v = [F0] * r.dim; v[i] = F1
                M.append(r.apply_word(w, v))
            # M[i] = rho(p) e_i  (columns); entry [j][i]
            return [[M[i][j] for i in range(r.dim)] for j in range(r.dim)]
        mu_mats = {p: rep_mat(rmu, p) for p in perms_n}
        nu_mats = {p: rep_mat(rnu, p) for p in perms_n}
        def inv(p):
            o = [0] * len(p)
            for i, v in enumerate(p): o[v] = i
            return tuple(o)
        # The two subgroup actions commute.  Factor the S_n x S_n average
        # into two successive S_n averages instead of paying an (n!)^2
        # double loop.  This is the same Schur projector exactly.
        beta_components = [[[F0] * d for _ in range(dn)] for _ in cols]
        beta_prefactor = Fraction(dn, fact)
        identity = tuple(range(n))
        for be in perms_n:
            Mb = nu_mats[inv(be)]
            big = tuple(identity + tuple(n + be[j] for j in range(n)))
            wbig = perm_word(big)
            for ci, w in enumerate(cols):
                v = rep.apply_word(wbig, list(w))
                for q in range(dn):
                    coefficient = beta_prefactor * Mb[0][q]
                    if not coefficient:
                        continue
                    target = beta_components[ci][q]
                    for i in range(d):
                        if v[i]:
                            target[i] += coefficient * v[i]

        alpha_prefactor = Fraction(dm, fact)
        second_identity = tuple(range(n, 2 * n))
        for al in perms_n:
            Ma = mu_mats[inv(al)]
            big = tuple(tuple(al) + second_identity)
            wbig = perm_word(big)
            for ci in range(len(cols)):
                for q in range(dn):
                    v = rep.apply_word(wbig, beta_components[ci][q][:])
                    for p in range(dm):
                        coefficient = alpha_prefactor * Ma[0][p]
                        if not coefficient:
                            continue
                        target = comp[ci][p][q]
                        for i in range(d):
                            if v[i]:
                                target[i] += coefficient * v[i]
        return comp

    def orbit_blocks_full(self, mu, nu, orbs):
        """Faithful block images: full invariant contraction (fixes the mu=nu
           antisymmetric-copy loss of the seed variant).
             B_o[r][c] = sum_{l in o} sum_{p,q} 1/(Gmu[p] Gnu[q]) *
                         (w^{pq}_c)^T G_lam rho(x_l) z^{pq}_r ,
             z^{pq}_r = sum_m Phi_r[p,q,m] Vb[m]."""
        cols = self.columns(mu, nu)
        rowsol, rmu, rnu = self.rows(mu, nu)
        mN, mY = len(cols), len(rowsol)
        extras = {"cols": cols, "rowsol": rowsol, "rmu": rmu, "rnu": rnu}
        if mN == 0 or mY == 0:
            return None, mY, mN, extras
        rep, ld, cs = self.rep, self.ld, self.cs
        d, dV = rep.dim, ld.dV
        G = rep.gram
        Vb = ld.Vbasis
        dm, dn = rmu.dim, rnu.dim
        Gm, Gn = rmu.gram, rnu.gram
        comp = self._column_components(mu, nu, cols, rmu, rnu)
        # dress with G_lam once
        compG = [[[[comp[c][p][q][i] * G[i] for i in range(d)]
                   for q in range(dn)] for p in range(dm)] for c in range(mN)]
        # row vectors z^{pq}_r with dual-basis weights folded in
        zpq = []
        for Phi in rowsol:
            zr = [[[F0] * d for _ in range(dn)] for _ in range(dm)]
            for p in range(dm):
                for q in range(dn):
                    wgt = F1 / (Gm[p] * Gn[q])
                    base = (p * dn + q) * dV
                    for m in range(dV):
                        cf = Phi[base + m]
                        if cf:
                            cfw = cf * wgt
                            for i in range(d):
                                if Vb[m][i]:
                                    zr[p][q][i] += cfw * Vb[m][i]
            zpq.append(zr)
        orb_list, seen = orbs
        norb = len(orb_list)
        B = [[[F0] * mN for _ in range(mY)] for _ in range(norb)]
        # propagate all (r,p,q) vectors through the BFS tree
        vecs = []
        tags = []
        for r in range(mY):
            for p in range(dm):
                for q in range(dn):
                    v = zpq[r][p][q]
                    if any(v):
                        vecs.append(list(v)); tags.append((r, p, q))
        store = [None] * cs.size
        store[0] = vecs
        for i in range(cs.size):
            if i > 0:
                par, k = cs.tree[i]
                store[i] = [rep.apply_s(k, v) for v in store[par]]
            oi = seen[cs.ell[i]]
            for vi, (r, p, q) in enumerate(tags):
                vec = store[i][vi]
                for c in range(mN):
                    wg = compG[c][p][q]
                    B[oi][r][c] += sum(wg[j] * vec[j] for j in range(d) if vec[j])
            # free parent storage when no longer needed (children are contiguous
            # in BFS order after parent; simple heuristic: keep all for n<=4)
        return B, mY, mN, extras

    def orbit_blocks(self, mu, nu, orbs, variant="zprop"):
        if variant == "full":
            return self.orbit_blocks_full(mu, nu, orbs)
        """Returns (B, mY, mN, extras): B[o] = m_Y x m_N matrix of Fractions,
           the image of the orbit-indicator delta_o in block (lam; mu, nu).

           variant 'zprop'  : B[o][r][c] = sum_{l in o} w_c^T G rho(x_l) z_r
                              (propagate the V-side row seeds through the tree,
                               contract against Gram-dressed LR columns)
           variant 'colprop': B[o][r][c] = sum_{l in o} z_r^T G rho(x_l) P_V w_c
                              (the transposed-side alternative)
           The n=2 ground truth decides which is the faithful encoding."""
        cols = self.columns(mu, nu)
        rowsol, rmu, rnu = self.rows(mu, nu)
        mN, mY = len(cols), len(rowsol)
        extras = {"cols": cols, "rowsol": rowsol, "rmu": rmu, "rnu": rnu}
        if mN == 0 or mY == 0:
            return None, mY, mN, extras
        rep, ld, cs = self.rep, self.ld, self.cs
        d = rep.dim
        G = rep.gram
        zs = self._row_seed_vectors(mu, nu, rowsol, rnu)
        extras["zs"] = zs
        orb_list, seen = orbs
        norb = len(orb_list)
        B = [[[F0] * mN for _ in range(mY)] for _ in range(norb)]
        if variant == "zprop":
            # dress columns with Gram once
            wg = [[w[i] * G[i] for i in range(d)] for w in cols]
            store = [None] * cs.size
            store[0] = [list(z) for z in zs]
            for i in range(cs.size):
                if i > 0:
                    par, k = cs.tree[i]
                    store[i] = [rep.apply_s(k, v) for v in store[par]]
                oi = seen[cs.ell[i]]
                for r in range(mY):
                    vec = store[i][r]
                    for c in range(mN):
                        B[oi][r][c] += sum(wg[c][j] * vec[j]
                                           for j in range(d) if vec[j])
        else:
            vc = [ld.PV_apply(w) for w in cols]
            zg = [[z[i] * G[i] for i in range(d)] for z in zs]
            store = [None] * cs.size
            store[0] = [list(v) for v in vc]
            for i in range(cs.size):
                if i > 0:
                    par, k = cs.tree[i]
                    store[i] = [rep.apply_s(k, v) for v in store[par]]
                oi = seen[cs.ell[i]]
                for c in range(mN):
                    vec = store[i][c]
                    for r in range(mY):
                        B[oi][r][c] += sum(zg[r][j] * vec[j]
                                           for j in range(d) if vec[j])
        return B, mY, mN, extras

    def gram_cols(self, cols):
        """Gram matrix w_c^T G w_c' of the LR column basis."""
        rep = self.rep
        G = rep.gram
        d = rep.dim
        return [[sum(a[i] * G[i] * b[i] for i in range(d)) for b in cols]
                for a in cols]

    def gram_rows(self, rowsol, rmu, rnu):
        """Invariant Gram of the row maps Phi: mu(x)nu -> V, i.e.
           tr(Phi^dag Phi') = sum_{p,q} 1/(Gmu[p] Gnu[q]) *
                              sum_{m1,m2} Phi[p,q,m1] S_V[m1,m2] Phi'[p,q,m2],
           matching the dual-basis weights of the block contraction."""
        dV = self.ld.dV
        dm, dn = rmu.dim, rnu.dim
        Gm, Gn = rmu.gram, rnu.gram
        SV = self.VGram
        out = []
        for A in rowsol:
            row = []
            for Bt in rowsol:
                s = F0
                for p in range(dm):
                    for q in range(dn):
                        w = F1 / (Gm[p] * Gn[q])
                        base = (p * dn + q) * dV
                        for m1 in range(dV):
                            a = A[base + m1]
                            if not a: continue
                            for m2 in range(dV):
                                b = Bt[base + m2]
                                if b:
                                    s += a * w * SV[m1][m2] * b
                row.append(s)
            out.append(row)
        return out

    def swap_col_matrix(self, mu, nu, cols_mn, cols_nm):
        """Matrix of rho(omega): W_N(mu,nu) -> W_N(nu,mu) in the RREF bases."""
        rep, n = self.rep, self.n
        d = rep.dim
        omega = tuple(list(range(n, 2 * n)) + list(range(n)))
        w = perm_word(omega)
        G = rep.gram
        # Gram matrix of target basis
        S = [[sum(a[i] * G[i] * b[i] for i in range(d)) for b in cols_nm]
             for a in cols_nm]
        M = []
        for v in cols_mn:
            img = rep.apply_word(w, list(v))
            tv = [sum(b[i] * G[i] * img[i] for i in range(d)) for b in cols_nm]
            x = solve_linear([row[:] for row in S], tv)
            M.append(x)   # coords of image in cols_nm basis
        # M[j][i]: coeff of basis i in image of j -> return as matrix [i][j]
        return [[M[j][i] for j in range(len(cols_mn))] for i in range(len(cols_nm))]
