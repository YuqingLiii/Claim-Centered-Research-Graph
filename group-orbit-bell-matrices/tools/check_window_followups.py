"""Exact finite sanity checks for registered C17/C18; not universal proofs.

Run with Python 3.9+ and assertions enabled. Arithmetic is integer/Fraction.
The root section checks a witness's affine coefficients, not optimality
outside the known window. The PSD section exhausts all ordered full signs
for a stated finite list of Gram matrices and one strict-interior lambda.
"""
from fractions import Fraction as F
from itertools import product


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def quadratic(a, c, b):
    return sum(a[i]*c[i][j]*b[j] for i in range(len(a)) for j in range(len(b)))


def root_witness(r):
    roots = []
    for i in range(r):
        for j in range(i+1, r):
            for eps, eta in product((-1, 1), repeat=2):
                w = [0]*r
                w[i], w[j] = eps, eta
                roots.append(tuple(w))
    n = 2*r*(r-1)
    assert len(roots) == len(set(roots)) == n
    h = tuple(1 if k == r-2 else -1 if k == r-1 else 0 for k in range(r))
    s0 = [next(x for x in w if x) for w in roots]
    a, b = s0[:], s0[:]
    a[roots.index(tuple(-x for x in h))] *= -1
    b[roots.index(h)] *= -1
    va = [sum(a[i]*w[k] for i, w in enumerate(roots)) for k in range(r)]
    vb = [sum(b[i]*w[k] for i, w in enumerate(roots)) for k in range(r)]
    rho = list(range(r-1, -1, -1))
    assert va == vb == [4*rho[k]-2*h[k] for k in range(r)]
    base = F(2*r*(2*r-1), 3)
    intercept = F(dot(va, vb), 4*(r-1))
    overlap = dot(a, b)
    assert intercept == base-F(2, r-1)
    assert overlap == n-4
    endpoint = F(1, 2*(r-1))
    assert intercept-endpoint*overlap == base-n*endpoint
    for step in (F(1, 1000), F(1, r), F(1), F(10)):
        lam = endpoint+step
        assert (intercept-lam*overlap)-(base-n*lam) == 4*step > 0
    print('C17 r=%d n=%d witness intercept=%s overlap=%d endpoint=%s PASS'
          % (r, n, intercept, overlap, endpoint))


def psd_optimizers(columns):
    n = len(columns)
    c = [[dot(columns[i], columns[j]) for j in range(n)] for i in range(n)]
    d = min(c[i][i] for i in range(n))
    assert d > 0
    signs = list(product((-1, 1), repeat=n))
    k = max(quadratic(z, c, z) for z in signs)
    zs = [z for z in signs if quadratic(z, c, z) == k]
    expected = {(z+tuple(-v for v in z),)*2 for z in zs}
    lam = F(d, 4)
    full = list(product((-1, 1), repeat=2*n))
    duplicated = [[F(c[i % n][j % n], 2)*(1 if (i < n) == (j < n) else -1)
                   -(lam if i == j else 0) for j in range(2*n)] for i in range(2*n)]
    best, actual = None, set()
    for a in full:
        for b in full:
            value = quadratic(a, duplicated, b)
            if best is None or value > best:
                best, actual = value, {(a, b)}
            elif value == best:
                actual.add((a, b))
    assert best == 2*k-2*n*lam
    assert actual == expected
    print('C18 columns=%s lambda=%s ordered_pairs=%d optimizers=%d PASS'
          % (columns, lam, len(full)**2, len(actual)))


if __name__ == '__main__':
    for dimension in range(3, 13):
        root_witness(dimension)
    for gram_columns in (
        ((1,),), ((2,),), ((1,), (1,)), ((1,), (-1,)),
        ((1, 0), (0, 1)), ((1, 0), (1, 1)),
        ((1,), (1,), (1,)), ((1, 0), (0, 1), (1, 1)),
    ):
        psd_optimizers(gram_columns)
    print('Scope: finite exact witness/equality sanity checks only; universal claims require proofs and independent reviews.')
