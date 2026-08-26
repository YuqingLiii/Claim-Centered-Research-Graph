"""D1 completion for the n=4 3x2 block (5,2,1;(3,1),(3,1)):
  (i)  swap operators on rows & columns; parity-aligned gauge; verify the
       block support form [[a,0],[b,0],[0,c]] for EVERY orbit image B_o;
  (ii) class-refined sigma at my Kelley optimum (float pencil on W_N),
       for (3,1),(3,1) and (3,1),(2,1,1);
  (iii) cross-check parity split against CY/CN targets' Z2 bookkeeping.
"""
import sys, json, math
from fractions import Fraction
import numpy as np
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
from mdh_engine import CosetSpace, partitions, syt_list, F0, F1
from mdh_blocks import BlockEngine
from mdh_fast import FastSE, hmap

def eig_parity(S):
    """Exact eigenbasis of a 2x2 involution with eigenvalues +1,-1."""
    S = [[Fraction(x) for x in row] for row in S]
    # v+ = column of (S + I), v- = column of (S - I) (nonzero ones)
    vp = [S[0][0] + 1, S[1][0]] if (S[0][0] + 1, S[1][0]) != (0, 0) else [S[0][1], S[1][1] + 1]
    vm = [S[0][0] - 1, S[1][0]] if (S[0][0] - 1, S[1][0]) != (0, 0) else [S[0][1], S[1][1] - 1]
    return vp, vm

def main():
    n = 4
    lam, mu, nu = (5, 2, 1), (3, 1), (3, 1)
    d = json.load(open(PROJECT / "artifacts" / "mdh_n4_521_block.json"))
    Sc = [[Fraction(x) for x in row] for row in d["S_col"]]
    B = [[[Fraction(x) for x in row_] for row_ in Bo] for Bo in
         [[[d["B"][o][r][c] for c in range(2)] for r in range(3)]
          for o in range(51)]]
    # row swap: rows are (mu x nu x V)-invariant tensors; the factor swap
    # requires recomputing; instead use equivariance: find S_row from
    # S_row B_o = B_o S_col solved over all orbits (exact least squares).
    # Stack: for each orbit, 3x2 equation; unknown S_row 3x3.
    rows = []
    rhs = []
    for o in range(51):
        for i in range(3):
            for j in range(2):
                # (S_row B_o)[i][j] = sum_k S_row[i][k] B_o[k][j]
                # equation: sum_k S_row[i][k] B_o[k][j] = (B_o S_col)[i][j]
                row = [F0] * 9
                for k in range(3):
                    row[i * 3 + k] = B[o][k][j]
                rows.append(row)
                rhs.append(sum(B[o][i][c] * Sc[c][j] for c in range(2)))
    # solve exact least-squares (consistent system expected): use rref on aug
    from mdh_engine import rref
    aug = [r + [v] for r, v in zip(rows, rhs)]
    R, piv = rref(aug, 10)
    if any(p == 9 for p in piv):
        print("S_row: system INCONSISTENT -> no equivariant row swap (BUG)")
        return
    sol = [F0] * 9
    for ri, p in enumerate(piv):
        sol[p] = R[ri][9]
    Sr = [[sol[i * 3 + k] for k in range(3)] for i in range(3)]
    print("S_row (solved from equivariance S_row B_o = B_o S_col):")
    for r in Sr: print("  ", [str(x) for x in r])
    # involution check
    sq = [[sum(Sr[i][k] * Sr[k][j] for k in range(3)) for j in range(3)]
          for i in range(3)]
    print("S_row^2 = I:", all(sq[i][j] == (1 if i == j else 0)
                              for i in range(3) for j in range(3)))
    tr = sum(Sr[i][i] for i in range(3))
    print("trace S_row =", tr, "(expect +1: two even rows, one odd)")
    # parity-aligned gauge: eigenvectors
    # columns: 2x2
    vp, vm = eig_parity([[Sc[0][0], Sc[0][1]], [Sc[1][0], Sc[1][1]]])
    print("col parity vectors: +", [str(x) for x in vp], " -", [str(x) for x in vm])
    # rows: exact eigenvectors of Sr^T? rows transform by S_row: parity basis
    # for ROW INDEX: diagonalize Sr (3x3, eigenvalues +1,+1,-1)
    import itertools
    # nullspaces of (Sr -+ I)
    from mdh_engine import nullspace
    Mp = [[Sr[i][j] - (1 if i == j else 0) for j in range(3)] for i in range(3)]
    Mm = [[Sr[i][j] + (1 if i == j else 0) for j in range(3)] for i in range(3)]
    Vp = nullspace(Mp, 3)   # even rows (eigval +1)
    Vm = nullspace(Mm, 3)
    print("row parity: dim(+1) =", len(Vp), " dim(-1) =", len(Vm))
    # transform every B_o: rows -> parity basis (coords), cols -> parity basis
    # B'_o = P_row^{-1}?? rows: cell index transforms contravariantly; use
    # basis change: B'_o[i'][j'] = (row-parity-basis expansion) ... easiest:
    # solve linear: B'_o = R^{-1} B_o C where R columns = row parity basis,
    # C columns = col parity basis.
    Rmat = [[Vp[0][i], Vp[1][i], Vm[0][i]] for i in range(3)]
    Cmat = [[vp[0], vm[0]], [vp[1], vm[1]]]
    from mdh_engine import solve_linear
    ok_form = True
    for o in range(51):
        # X = R^{-1} B_o C : solve R X = B_o C
        BC = [[sum(B[o][i][c] * Cmat[c][j] for c in range(2)) for j in range(2)]
              for i in range(3)]
        X = []
        for j in range(2):
            col = solve_linear([row[:] for row in Rmat],
                               [BC[i][j] for i in range(3)])
            X.append(col)
        Xm = [[X[j][i] for j in range(2)] for i in range(3)]
        # expected form: [[*,0],[*,0],[0,*]]
        if not (Xm[0][1] == 0 and Xm[1][1] == 0 and Xm[2][0] == 0):
            ok_form = False
            print(f"  orbit {o}: parity form VIOLATED:",
                  [[str(x) for x in r] for r in Xm])
    print("parity form [[a,0],[b,0],[0,c]] for ALL 51 orbit images:",
          "OK" if ok_form else "FAIL")

    # ---- class-refined sigma at my optimum -----------------------------
    t = np.load(PROJECT / "artifacts" / "mdh_opt_t_n4.npy")
    fs = FastSE(4, lams=[(5, 2, 1)], verbose=False)
    f = fs.fl[0]
    # build K (khat with G-right-form) as in pencil_max
    K = np.zeros((f.d, f.d))
    for si in range(len(f.slist)):
        W = np.tensordot(t, f.Q[si], axes=(0, 0))
        K += W @ f.SVinv @ W.T
    K *= f.fact
    cs = fs.cs
    eng = BlockEngine(4, lam, cs)
    for (m2, n2) in [((3, 1), (3, 1)), ((3, 1), (2, 1, 1)), ((2, 1, 1), (3, 1))]:
        cols = eng.columns(m2, n2)
        if not cols: continue
        Wn = np.array([[float(x) for x in w] for w in cols]).T  # d x mN
        Gd = f.G
        # khat = K*G (right Gram); class pencil: M = Wn^T G khat Wn
        M = Wn.T @ (Gd[:, None] * (K @ (Gd[:, None] * Wn)))
        S = Wn.T @ (Gd[:, None] * Wn)
        ev = np.linalg.eigvals(np.linalg.solve(S, M))
        sig = sorted([math.sqrt(max(x.real, 0)) for x in ev], reverse=True)
        print(f"my-optimum sigma for (5,2,1;{m2},{n2}):",
              ["%.6f" % s for s in sig])

if __name__ == "__main__":
    main()
