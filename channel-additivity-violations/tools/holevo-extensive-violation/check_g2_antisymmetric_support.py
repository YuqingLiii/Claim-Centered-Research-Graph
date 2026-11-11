#!/usr/bin/env python3
"""Exact integer checks for the seven-dimensional G2 cross-product support.

The script deliberately avoids numerical eigensolvers.  It builds six times the
support channel as an integer 49-by-49 matrix, verifies its annihilating
polynomial and the nullities at all four rational eigenvalues, and checks the
null-vector output spectrum through an exact realification.
"""

from fractions import Fraction
from itertools import permutations


DIM = 7


def zeros(n, m=None):
    return [[0 for _ in range(n if m is None else m)] for _ in range(n)]


def identity(n):
    out = zeros(n)
    for i in range(n):
        out[i][i] = 1
    return out


def matmul(a, b):
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    out = zeros(rows, cols)
    for i in range(rows):
        for k in range(inner):
            aik = a[i][k]
            if aik:
                for j in range(cols):
                    out[i][j] += aik * b[k][j]
    return out


def shifted(a, scalar):
    out = [row[:] for row in a]
    for i in range(len(out)):
        out[i][i] -= scalar
    return out


def rank_over_q(a):
    work = [[Fraction(value) for value in row] for row in a]
    rows = len(work)
    cols = len(work[0])
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
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def build_phi():
    # phi = e127+e347+e567+e135-e146-e236-e245, with zero-based indices.
    triples = [
        (0, 1, 6, 1),
        (2, 3, 6, 1),
        (4, 5, 6, 1),
        (0, 2, 4, 1),
        (0, 3, 5, -1),
        (1, 2, 5, -1),
        (1, 3, 4, -1),
    ]
    phi = [[[0 for _ in range(DIM)] for _ in range(DIM)] for _ in range(DIM)]
    for a, b, c, sign in triples:
        base = (a, b, c)
        for perm in permutations(range(3)):
            inversions = sum(
                perm[i] > perm[j]
                for i in range(3)
                for j in range(i + 1, 3)
            )
            i, j, k = (base[perm[t]] for t in range(3))
            phi[i][j][k] = sign * (-1) ** inversions
    return phi


def build_six_times_channel(phi):
    # V|a> = 6^{-1/2} sum_{b,e} phi[a,b,e]|b,e>.
    # Therefore (6 T)_{bd,ac}=sum_e phi[a,b,e] phi[c,d,e].
    size = DIM * DIM
    out = zeros(size)
    for b in range(DIM):
        for d in range(DIM):
            row = b * DIM + d
            for a in range(DIM):
                for c in range(DIM):
                    col = a * DIM + c
                    out[row][col] = sum(
                        phi[a][b][e] * phi[c][d][e] for e in range(DIM)
                    )
    return out


def realified_null_output(phi):
    # For x=(e_0+i e_1)/sqrt(2), rho_B=H/12 with
    # H=(J_0+iJ_1)(J_0+iJ_1)^dagger.  Return the exact 14-by-14
    # realification of H; every complex eigenvalue is then doubled.
    real = zeros(DIM)
    imag = zeros(DIM)
    for b in range(DIM):
        for d in range(DIM):
            real[b][d] = sum(
                phi[0][b][e] * phi[0][d][e]
                + phi[1][b][e] * phi[1][d][e]
                for e in range(DIM)
            )
            imag[b][d] = sum(
                -phi[0][b][e] * phi[1][d][e]
                + phi[1][b][e] * phi[0][d][e]
                for e in range(DIM)
            )
    out = zeros(2 * DIM)
    for i in range(DIM):
        for j in range(DIM):
            out[i][j] = real[i][j]
            out[i][j + DIM] = -imag[i][j]
            out[i + DIM][j] = imag[i][j]
            out[i + DIM][j + DIM] = real[i][j]
    return out


def assert_zero_matrix(a):
    assert all(value == 0 for row in a for value in row)


def main():
    phi = build_phi()

    contraction = [
        [
            sum(phi[a][b][e] * phi[c][b][e] for b in range(DIM) for e in range(DIM))
            for c in range(DIM)
        ]
        for a in range(DIM)
    ]
    assert contraction == [[6 * (a == c) for c in range(DIM)] for a in range(DIM)]

    channel = build_six_times_channel(phi)
    assert channel == [list(row) for row in zip(*channel)]

    for a in range(DIM):
        for c in range(DIM):
            trace_value = sum(channel[b * DIM + b][a * DIM + c] for b in range(DIM))
            assert trace_value == 6 * (a == c)
    for b in range(DIM):
        for d in range(DIM):
            unital_value = sum(channel[b * DIM + d][a * DIM + a] for a in range(DIM))
            assert unital_value == 6 * (b == d)

    polynomial = identity(DIM * DIM)
    for eigenvalue in (6, -3, 3, -1):
        polynomial = matmul(polynomial, shifted(channel, eigenvalue))
    assert_zero_matrix(polynomial)

    expected_nullities = {6: 1, -3: 7, 3: 14, -1: 27}
    observed_nullities = {
        eigenvalue: DIM * DIM - rank_over_q(shifted(channel, eigenvalue))
        for eigenvalue in expected_nullities
    }
    assert observed_nullities == expected_nullities

    null_output = realified_null_output(phi)
    null_polynomial = identity(2 * DIM)
    for eigenvalue in (0, 2, 4):
        null_polynomial = matmul(null_polynomial, shifted(null_output, eigenvalue))
    assert_zero_matrix(null_polynomial)
    expected_real_nullities = {0: 6, 2: 4, 4: 4}
    observed_real_nullities = {
        eigenvalue: 2 * DIM - rank_over_q(shifted(null_output, eigenvalue))
        for eigenvalue in expected_real_nullities
    }
    assert observed_real_nullities == expected_real_nullities

    print("G2 support exact checks passed")
    print("spectrum(6T): 6^1, (-3)^7, 3^14, (-1)^27")
    print("spectrum(rho_null): 0^3, (1/6)^2, (1/3)^2")


if __name__ == "__main__":
    main()
