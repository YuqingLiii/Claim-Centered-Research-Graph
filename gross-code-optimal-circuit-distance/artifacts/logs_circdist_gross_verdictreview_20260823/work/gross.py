"""Gross code [[144,12,12]] : construction, F2 linear algebra, Tanner incidences.
Exact numpy uint8 arithmetic only.  Independently written for the SBB certification session.
"""
import numpy as np, itertools

ELL, EM = 12, 6
NG = ELL * EM            # 72 group elements
N = 2 * NG               # 144 data qubits: left 0..71, right 72..143


def gidx(i, j):
    return (i % ELL) * EM + (j % EM)


def gsum(g, m):
    i, j = divmod(g, EM)
    return gidx(i + m[0], j + m[1])


def mono(a, b):
    P = np.zeros((NG, NG), np.uint8)
    for i in range(ELL):
        for j in range(EM):
            P[gidx(i + a, j + b), gidx(i, j)] = 1
    return P


A_MONOS = [(3, 0), (0, 1), (0, 2)]      # A = x^3 + y + y^2
B_MONOS = [(0, 3), (1, 0), (2, 0)]      # B = y^3 + x + x^2
A = sum(mono(*m) for m in A_MONOS) % 2
B = sum(mono(*m) for m in B_MONOS) % 2
HX = np.concatenate([A, B], 1).astype(np.uint8)
HZ = np.concatenate([B.T, A.T], 1).astype(np.uint8)


# ---------------- F2 linear algebra ----------------
def rref(Mat):
    Mat = Mat.copy() % 2
    rows, cols = Mat.shape
    piv = []; r = 0
    for c in range(cols):
        pr = None
        for rr in range(r, rows):
            if Mat[rr, c]:
                pr = rr; break
        if pr is None:
            continue
        if pr != r:
            Mat[[r, pr]] = Mat[[pr, r]]
        sel = (Mat[:, c] == 1); sel[r] = False
        Mat[sel] ^= Mat[r]
        piv.append(c); r += 1
        if r == rows:
            break
    return Mat[:r], piv


def nullspace(Mat):
    R, piv = rref(Mat)
    cols = Mat.shape[1]
    pset = set(piv)
    free = [c for c in range(cols) if c not in pset]
    basis = []
    for f in free:
        v = np.zeros(cols, np.uint8); v[f] = 1
        for r, p in enumerate(piv):
            if R[r, f]:
                v[p] = 1
        basis.append(v)
    return np.array(basis, np.uint8) if basis else np.zeros((0, cols), np.uint8)


class Reducer:
    def __init__(self, Mat):
        self.R, self.piv = rref(Mat)

    def red(self, v):
        w = v.copy() % 2
        for r, p in enumerate(self.piv):
            if w[p]:
                w ^= self.R[r]
        return w

    def inspan(self, v):
        return not self.red(v).any()


# ---------------- Tanner incidences (derived, verified below) ----------------
# X-check g touches left data  g - A_i  (monomial A_i)  and right data NG + (g - B_i)
# Z-check g touches left data  g + B_i  (monomial B_i)  and right data NG + (g + A_i)
def xcheck_nb(g):
    out = [(gsum(g, (-m[0], -m[1])), 'L', i) for i, m in enumerate(A_MONOS)]
    out += [(NG + gsum(g, (-m[0], -m[1])), 'R', i) for i, m in enumerate(B_MONOS)]
    return out


def zcheck_nb(g):
    out = [(gsum(g, m), 'L', i) for i, m in enumerate(B_MONOS)]
    out += [(NG + gsum(g, m), 'R', i) for i, m in enumerate(A_MONOS)]
    return out


def xchecks_of(q):
    if q < NG:
        return [(gsum(q, m), 'L', i) for i, m in enumerate(A_MONOS)]
    g = q - NG
    return [(gsum(g, m), 'R', i) for i, m in enumerate(B_MONOS)]


def zchecks_of(q):
    if q < NG:
        return [(gsum(q, (-m[0], -m[1])), 'L', i) for i, m in enumerate(B_MONOS)]
    g = q - NG
    return [(gsum(g, (-m[0], -m[1])), 'R', i) for i, m in enumerate(A_MONOS)]


def verify_incidences():
    for g in range(NG):
        assert sorted(q for q, _, _ in xcheck_nb(g)) == sorted(map(int, np.nonzero(HX[g])[0])), g
        assert sorted(q for q, _, _ in zcheck_nb(g)) == sorted(map(int, np.nonzero(HZ[g])[0])), g
    for q in range(N):
        assert sorted(c for c, _, _ in xchecks_of(q)) == sorted(map(int, np.nonzero(HX[:, q])[0])), q
        assert sorted(c for c, _, _ in zchecks_of(q)) == sorted(map(int, np.nonzero(HZ[:, q])[0])), q
    for g in range(NG):
        for q, s, i in xcheck_nb(g):
            assert (g, s, i) in xchecks_of(q)
        for q, s, i in zcheck_nb(g):
            assert (g, s, i) in zchecks_of(q)
    return True


# ---------------- translations (code automorphisms) ----------------
def tperm_data(a, b):
    """data permutation p with (T v)[p_target] ; new[gidx(i+a,j+b)] = old[gidx(i,j)]"""
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i + a, j + b)] = gidx(i, j)
            p[NG + gidx(i + a, j + b)] = NG + gidx(i, j)
    return p


TRANS = [tperm_data(a, b) for a in range(ELL) for b in range(EM)]


def sanity():
    assert ((HX @ HZ.T) % 2 == 0).all()
    assert set(HX.sum(1)) == {6} and set(HZ.sum(1)) == {6}
    assert set(HX.sum(0)) == {3} and set(HZ.sum(0)) == {3}
    rx = len(rref(HX)[1]); rz = len(rref(HZ)[1])
    ov = set()
    for i in range(NG):
        for j in range(NG):
            ov.add(int((HX[i] & HZ[j]).sum()))
    # overlap halves: for each overlapping (X,Z) pair, where do the 2 shared qubits sit?
    halves = set()
    for i in range(NG):
        for j in range(NG):
            sh = np.nonzero(HX[i] & HZ[j])[0]
            if len(sh):
                halves.add(tuple(sorted(int(q >= NG) for q in sh)))
    return dict(rankHX=rx, rankHZ=rz, k=N - rx - rz, overlaps=sorted(ov),
                overlap_halves=sorted(halves), incidences=verify_incidences())


if __name__ == "__main__":
    print(sanity())
