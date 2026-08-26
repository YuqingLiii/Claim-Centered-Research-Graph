"""The matrix-valued OP family for SE(n,2n): exact extraction of

  (a) the block table  P: orbit o -> B_o(lam; mu,nu)[r,c]   (exact, certified)
  (b) orthogonality:   sum_o w_o B_o[cell] B_o[cell'] = delta H   (G1 / 6.1)
  (c) three-term recurrence in the level k for the generator
        x = a(o) := folded overlap statistic  (Johnson variable):
        a(o) * P_k(o) = A_k P_{k+1}(o) + B_k P_k(o) + C_k P_{k-1}(o)   (6.2)
      per (mu,nu)-class tower  [a has trivial position content => classes
      closed; PROVED via Pieri],
  (d) the second operator: phi(o) = agreement count (level-1 with position
      content: moves (lam, mu, nu) jointly by <= 1 box) -- the Delta-side
      generator; its closure over the full block lattice is checked too.

  The 'difference equation' (6.3) is the statement dual to (c): the NO-side
  central element C2 (transposition class sum) acts diagonally per lam with
  eigenvalue = content sum c2(lam) -- second-order in the orbit variable.

All arithmetic exact. Certification: cells at n=2 (5x5 table), n=3 (26 cells).
"""
import sys, math, json, time
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
from mdh_engine import (CosetSpace, LambdaData, partitions, syt_list, F0, F1,
                        rref)
from mdh_blocks import BlockEngine

def content_sum(lam):
    return sum(Fraction(c - r) for r in range(len(lam)) for c in range(lam[r]))

def orbit_stats(cs):
    """per orbit: folded overlap multiset a(o) (as sorted pair), phi range."""
    n = cs.n
    stats = []
    for o_rep in cs.ell:
        pass
    return stats

class FamilyData:
    """All exact block cells for one n."""
    def __init__(self, n, verbose=True):
        self.n = n
        self.cs = CosetSpace(n)
        self.orbs = self.cs.orbits()
        self.orb_list, self.seen = self.orbs
        self.norb = len(self.orb_list)
        # orbit invariants
        self.osize = [len(o) for o in self.orb_list]
        # folded overlap: a-value multiset over the orbit is {a, n-a} mix; the
        # R-invariant scalar is s(o) = mean of a(l) over the orbit = n/2 iff
        # folded; better: use the SYMMETRIC function a(l)(n - a(l)) which is
        # R-invariant pointwise!  x(o) := a(1-a/n)-type: take x = a*(n-a).
        self.xval = []
        self.phival = []
        for o in self.orb_list:
            l0 = sorted(o)[0]
            a = sum(1 for v in l0 if v < n)
            assert all((lambda aa: aa * (n - aa) == a * (n - a))(
                sum(1 for v in l if v < n)) for l in o)
            self.xval.append(Fraction(a * (n - a)))
            self.phival.append(Fraction(self.cs.phi(l0)))
            assert all(self.cs.phi(l) == self.phival[-1] for l in o) or True
        # phi is NOT constant on orbits? phi(l) IS R-invariant (proved).
        for oi, o in enumerate(self.orb_list):
            for l in o:
                assert self.cs.phi(l) == self.phival[oi], "phi not invariant!"
        self.cells = []   # (lam, mu, nu, r, c, level)
        self.table = {}   # (lam,mu,nu) -> B list
        self.dims = {}
        t0 = time.time()
        for lam in partitions(2 * n):
            ld = LambdaData(lam, n, self.cs)
            if ld.dV == 0: continue
            eng = BlockEngine(n, lam, self.cs)
            for mu in partitions(n):
                for nu in partitions(n):
                    B, mY, mN, ex = eng.orbit_blocks(mu, nu, self.orbs,
                                                     variant="full")
                    if B is None: continue
                    self.table[(lam, mu, nu)] = B
                    self.dims[(lam, mu, nu)] = (mY, mN)
                    lev = sum(lam) - lam[0]
                    for r in range(mY):
                        for c in range(mN):
                            self.cells.append((lam, mu, nu, r, c, lev))
            if verbose:
                print(f"  lam {lam} done ({time.time()-t0:.0f}s)", flush=True)

    def cell_fn(self, cell):
        lam, mu, nu, r, c, lev = cell
        B = self.table[(lam, mu, nu)]
        return [B[o][r][c] for o in range(self.norb)]

    # ---------------- G1: orthogonality / weight ---------------------------
    def gram_cells(self, cells=None):
        """M[cell,cell'] = sum_o (1/|o|) B_o[cell] B_o[cell']  (Plancherel of
           the R-averaged matrix-coefficient functions)."""
        cells = cells if cells is not None else self.cells
        fns = [self.cell_fn(c) for c in cells]
        m = len(fns)
        return [[sum(fns[i][o] * fns[j][o] / Fraction(self.osize[o])
                     for o in range(self.norb)) for j in range(m)]
                for i in range(m)]

    def canonical_cells(self):
        """One orientation per coupled pair: keep mu <= nu (lex on tuples)."""
        return [c for c in self.cells if c[1] <= c[2]]

    def weight_at_x(self, cells=None):
        """W(x)[cell,cell'] = sum_{o: x(o)=x} (1/|o|) B_o B_o'  per x-value."""
        cells = cells if cells is not None else self.canonical_cells()
        fns = [self.cell_fn(c) for c in cells]
        xs = sorted(set(self.xval))
        W = {}
        for x in xs:
            idx = [o for o in range(self.norb) if self.xval[o] == x]
            W[x] = [[sum(fns[i][o] * fns[j][o] / Fraction(self.osize[o])
                         for o in idx) for j in range(len(cells))]
                    for i in range(len(cells))]
        return W, xs

    # ---------------- G2: recurrence for x = a(n-a) ------------------------
    def recurrence(self, gen="x", cells=None):
        """For each cell, solve  gen(o)*cell(o) = sum_cells coeff * cell'(o)
           exactly; report support pattern (which (lam',mu',nu') needed)."""
        g = self.xval if gen == "x" else self.phival
        cols = list(cells) if cells is not None else list(self.cells)
        fns = {c: self.cell_fn(c) for c in cols}
        A = [[fns[c][o] for c in cols] for o in range(self.norb)]
        results = {}
        for cell in cols:
            target = [g[o] * fns[cell][o] for o in range(self.norb)]
            # exact least-... must be exactly solvable iff table spans; solve
            # A coef = target  (norb x ncells); use rref on augmented
            aug = [row[:] + [target[i]] for i, row in enumerate(A)]
            R, piv = rref(aug, len(cols) + 1)
            # check consistency: no pivot in last column
            ok = all(p != len(cols) for p in piv)
            if not ok:
                results[cell] = None
                continue
            # extract one solution (free vars = 0 in RREF param.)
            coef = [F0] * len(cols)
            for ri, p in enumerate(piv):
                coef[p] = R[ri][len(cols)]
            results[cell] = coef
        return results, cols

    def print_recurrence_support(self, results, cols, gen_name="x"):
        print(f"recurrence support for {gen_name}:")
        for cell, coef in results.items():
            if coef is None:
                print(f"  {cell}: NOT in span!")
                continue
            lam, mu, nu, r, c, lev = cell
            supp = {}
            for cc, co in zip(cols, coef):
                if co != 0:
                    key = (cc[0], cc[1], cc[2], cc[5])
                    supp.setdefault(key, []).append((cc[3], cc[4], co))
            lev_moves = sorted(set(k[3] - lev for k in supp))
            class_moves = sorted(set((k[1] != mu) or (k[2] != nu) for k in supp))
            print(f"  cell lam={lam} ({mu},{nu})[{r}{c}] k={lev}: "
                  f"level moves {lev_moves}, class change {class_moves}")

def main(n):
    fd = FamilyData(n)
    cc = fd.canonical_cells()
    print(f"n={n}: {len(fd.cells)} cells ({len(cc)} canonical), {fd.norb} orbits")
    print("x values per orbit:", [str(x) for x in fd.xval])
    print("phi values per orbit:", [str(x) for x in fd.phival])
    # G1 with 1/|o| weights on canonical cells
    Gm = fd.gram_cells(cc)
    m = len(cc)
    viol = []
    for i in range(m):
        for j in range(i + 1, m):
            if Gm[i][j] != 0:
                ci, cj = cc[i], cc[j]
                if (ci[0], ci[1], ci[2]) != (cj[0], cj[1], cj[2]):
                    viol.append((ci, cj, Gm[i][j]))
    print(f"G1 (weights 1/|o|): cross-class violations: {len(viol)}")
    for v in viol[:8]: print("   ", v)
    print("G1 diagonal (cell norms^2):")
    for i, c in enumerate(cc):
        print(f"   {c[0]} ({c[1]},{c[2]})[{c[3]}{c[4]}] k={c[5]}: {Gm[i][i]}")
    # G2 for x and phi on canonical cells
    for gen in ["x", "phi"]:
        res, cols = fd.recurrence(gen, cells=cc)
        fd.print_recurrence_support(res, cols, gen)
        if gen == "x":
            print("x-recurrence coefficients (per cell):")
            for cell, coef in res.items():
                if coef is None: continue
                nz = [(cols[i], coef[i]) for i in range(len(cols)) if coef[i]]
                s = " + ".join(f"[{str(co)}] {c2[0]}({c2[1]},{c2[2]})"
                               f"[{c2[3]}{c2[4]}]" for c2, co in nz)
                print(f"   x*{cell[0]}({cell[1]},{cell[2]})[{cell[3]}{cell[4]}] = {s}")
    return fd

def difference_operator(fd):
    """D = left multiplication by the transposition class sum C2 of S_{2n}:
       (Dt)(l) = sum_{transpositions tau} t(tau o l).  On the block table:
       D(cell) = c2(lam) * cell  EXACTLY (bispectral partner of M_x).
       D is a <=1-step operator in the a-variable (second order in x)."""
    n = fd.n
    cs = fd.cs
    # orbit-level matrix of D
    import itertools
    Dm = [[F0] * fd.norb for _ in range(fd.norb)]
    for oi, orb in enumerate(fd.orb_list):
        rep = sorted(orb)[0]
        for i in range(2 * n):
            for j in range(i + 1, 2 * n):
                img = tuple(j if v == i else (i if v == j else v) for v in rep)
                Dm[fd.seen[img]][oi] += 1
    # verify eigen-relation on every canonical cell
    print("difference operator D (transposition class-sum):")
    allok = True
    for cell in fd.canonical_cells():
        f = fd.cell_fn(cell)
        # (D^T f)(o)?  D acts on functions: (Df)(o) = sum_{o'} D[o',o]-careful:
        # (Dt)(l) = sum_tau t(tau l): as matrix on orbit-functions:
        # (Dt)_o = sum_{o'} N(o -> o') t_{o'}, N = count over tau for rep of o.
        # D acts on functions; the cell VALUES are orbit sums: F(o) = f[o]/|o|
        g = [F0] * fd.norb
        for o in range(fd.norb):
            rep = sorted(fd.orb_list[o])[0]
            s = F0
            for i in range(2 * n):
                for j in range(i + 1, 2 * n):
                    img = tuple(j if v == i else (i if v == j else v) for v in rep)
                    oo = fd.seen[img]
                    s += f[oo] / Fraction(fd.osize[oo])
            g[o] = s
        lam = cell[0]
        c2 = content_sum(lam)
        ok = all(g[o] == c2 * f[o] / Fraction(fd.osize[o])
                 for o in range(fd.norb))
        allok = allok and ok
        if not all(v == 0 for v in f):
            print(f"   {lam}({cell[1]},{cell[2]})[{cell[3]}{cell[4]}]: "
                  f"D = {c2} * id : {'OK' if ok else 'FAIL'}")
    print("   bispectrality:", "ALL OK" if allok else "FAILURES")

def weight_report(fd):
    cc = fd.canonical_cells()
    W, xs = fd.weight_at_x(cc)
    print("matrix weight W(x) on canonical cells (x = a(n-a) folded overlap):")
    for x in xs:
        M = W[x]
        nz = sum(1 for r in M for v in r if v != 0)
        print(f"  x={x}: nnz={nz}")
        for i, c in enumerate(cc):
            row = " ".join(str(M[i][j]) for j in range(len(cc)))
            print(f"    {c[0]}({c[1]},{c[2]})[{c[3]}{c[4]}]: {row}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=2)
    a = ap.parse_args()
    main(a.n)
