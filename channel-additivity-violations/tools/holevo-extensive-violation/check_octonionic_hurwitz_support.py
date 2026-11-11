#!/usr/bin/env python3
"""Exact checks for the rank-eight octonionic Hurwitz support.

All channel calculations use the integer matrix 8T.  Rational Gaussian
elimination verifies eigenspace multiplicities and proves that the positive
21-dimensional skew eigenspace has no common vector kernel.
"""

from fractions import Fraction
from itertools import permutations


DIM = 8


def zeros(rows, cols=None):
    return [[0 for _ in range(rows if cols is None else cols)] for _ in range(rows)]


def identity(n):
    out = zeros(n)
    for i in range(n):
        out[i][i] = 1
    return out


def shifted(a, scalar):
    out = [row[:] for row in a]
    for i in range(len(out)):
        out[i][i] -= scalar
    return out


def matmul(a, b):
    out = zeros(len(a), len(b[0]))
    for i in range(len(a)):
        for k in range(len(b)):
            if a[i][k]:
                for j in range(len(b[0])):
                    out[i][j] += a[i][k] * b[k][j]
    return out


def rref_over_q(a):
    work = [[Fraction(value) for value in row] for row in a]
    rows = len(work)
    cols = len(work[0])
    pivots = []
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row or not work[r][col]:
                continue
            factor = work[r][col]
            work[r] = [x - factor * y for x, y in zip(work[r], work[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return work, pivots


def rank_over_q(a):
    return len(rref_over_q(a)[1])


def nullspace_over_q(a):
    rref, pivots = rref_over_q(a)
    free = [col for col in range(len(a[0])) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [Fraction(0) for _ in range(len(a[0]))]
        vector[free_col] = 1
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -rref[row][free_col]
        basis.append(vector)
    return basis


def octonion_left_multiplications():
    # Imaginary multiplication from the same oriented Fano triples as the G2 checker.
    triples = [
        (1, 2, 7, 1),
        (3, 4, 7, 1),
        (5, 6, 7, 1),
        (1, 3, 5, 1),
        (1, 4, 6, -1),
        (2, 3, 6, -1),
        (2, 4, 5, -1),
    ]
    oriented = {}
    for a, b, c, sign in triples:
        base = (a, b, c)
        for perm in permutations(range(3)):
            inversions = sum(
                perm[i] > perm[j]
                for i in range(3)
                for j in range(i + 1, 3)
            )
            oriented[tuple(base[perm[t]] for t in range(3))] = sign * (-1) ** inversions

    def multiply(a, b):
        if a == 0:
            return b, 1
        if b == 0:
            return a, 1
        if a == b:
            return 0, -1
        for c in range(1, DIM):
            if (a, b, c) in oriented:
                return c, oriented[(a, b, c)]
        raise AssertionError((a, b))

    left = []
    for a in range(DIM):
        matrix = zeros(DIM)
        for e in range(DIM):
            b, sign = multiply(a, e)
            matrix[b][e] = sign
        left.append(matrix)
    return left


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scalar(a, value):
    return [[value * x for x in row] for row in a]


def build_eight_times_channel(left):
    out = zeros(DIM * DIM)
    for b in range(DIM):
        for d in range(DIM):
            row = b * DIM + d
            for a in range(DIM):
                for c in range(DIM):
                    col = a * DIM + c
                    out[row][col] = sum(left[a][b][e] * left[c][d][e] for e in range(DIM))
    return out


def realified_null_output(left):
    # x=(e_0+i e_1)/sqrt(2), rho=H/16,
    # H=(L_0+iL_1)(L_0+iL_1)^dagger.
    l0 = left[0]
    l1 = left[1]
    real = add(matmul(l0, transpose(l0)), matmul(l1, transpose(l1)))
    imag = add(scalar(matmul(l0, transpose(l1)), -1), matmul(l1, transpose(l0)))
    out = zeros(2 * DIM)
    for i in range(DIM):
        for j in range(DIM):
            out[i][j] = real[i][j]
            out[i][j + DIM] = -imag[i][j]
            out[i + DIM][j] = imag[i][j]
            out[i + DIM][j + DIM] = real[i][j]
    return out


def assert_zero_matrix(a):
    assert all(entry == 0 for row in a for entry in row)


def main():
    left = octonion_left_multiplications()
    eye = identity(DIM)
    for a in range(DIM):
        for b in range(DIM):
            polarized = add(
                matmul(transpose(left[a]), left[b]),
                matmul(transpose(left[b]), left[a]),
            )
            assert polarized == scalar(eye, 2 * (a == b))

    channel = build_eight_times_channel(left)
    assert channel == transpose(channel)
    for a in range(DIM):
        for c in range(DIM):
            assert sum(channel[b * DIM + b][a * DIM + c] for b in range(DIM)) == 8 * (a == c)
    for b in range(DIM):
        for d in range(DIM):
            assert sum(channel[b * DIM + d][a * DIM + a] for a in range(DIM)) == 8 * (b == d)

    polynomial = identity(DIM * DIM)
    for eigenvalue in (8, -4, 4, 0):
        polynomial = matmul(polynomial, shifted(channel, eigenvalue))
    assert_zero_matrix(polynomial)
    expected_nullities = {8: 1, -4: 7, 4: 21, 0: 35}
    observed_nullities = {
        value: DIM * DIM - rank_over_q(shifted(channel, value))
        for value in expected_nullities
    }
    assert observed_nullities == expected_nullities

    # The zero eigenspace is exactly the symmetric traceless sector.
    symmetric_traceless = []
    for i in range(1, DIM):
        vector = [0] * (DIM * DIM)
        vector[0] = -1
        vector[i * DIM + i] = 1
        symmetric_traceless.append(vector)
    for i in range(DIM):
        for j in range(i + 1, DIM):
            vector = [0] * (DIM * DIM)
            vector[i * DIM + j] = 1
            vector[j * DIM + i] = 1
            symmetric_traceless.append(vector)
    assert len(symmetric_traceless) == 35
    for vector in symmetric_traceless:
        assert all(
            sum(channel[row][col] * vector[col] for col in range(DIM * DIM)) == 0
            for row in range(DIM * DIM)
        )

    # The +1/2 eigenspace is a 21-dimensional skew algebra with no common
    # vector kernel.  This distinguishes it from a reflection-fixed so(7),
    # which necessarily annihilates the reflected axis.
    positive_basis = nullspace_over_q(shifted(channel, 4))
    assert len(positive_basis) == 21
    stacked = []
    for vector in positive_basis:
        matrix = [vector[i * DIM:(i + 1) * DIM] for i in range(DIM)]
        assert matrix == scalar(transpose(matrix), -1)
        stacked.extend(matrix)
    assert rank_over_q(stacked) == DIM

    null_output = realified_null_output(left)
    null_polynomial = matmul(null_output, shifted(null_output, 4))
    assert_zero_matrix(null_polynomial)
    expected_real_nullities = {0: 8, 4: 8}
    observed_real_nullities = {
        value: 2 * DIM - rank_over_q(shifted(null_output, value))
        for value in expected_real_nullities
    }
    assert observed_real_nullities == expected_real_nullities

    print("octonionic Hurwitz support exact checks passed")
    print("spectrum(8T): 8^1, (-4)^7, 4^21, 0^35")
    print("positive 21-space common kernel dimension: 0")
    print("spectrum(rho_null): 0^4, (1/4)^4")


if __name__ == "__main__":
    main()
