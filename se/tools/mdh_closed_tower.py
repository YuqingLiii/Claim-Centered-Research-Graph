"""Closed recurrence certificate for the ((n-1,1),(n)) SE tower.

The structural derivation is documented in
``artifacts/mdh_tower_closed_form_derivation.md``.  This file contains only
the resulting exact formulas and independent checks.  It deliberately does
not perform interpolation.

Write

    A_j = (2n-j,j),       B_j = (2n-j-1,j,1),   1 <= j < n.

The intrinsic projection gauge is v_lambda = E_lambda v_0.  In that gauge
the squared norm is

    h_lambda = dim(S^lambda) / (n * binom(2n,n)).

Multiplication by a=|S intersect [n]| is block tridiagonal.  Multiplication
by x=a(n-a) is then obtained exactly as M_x = n M_a - M_a^2.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import comb

from mdh_marked_subset_d1 import (
    hook_dimension,
    multiplication_recurrence,
)


F = Fraction


def cells(n):
    return [(branch, j) for j in range(1, n) for branch in ("A", "B")]


def shape(n, branch, j):
    if branch == "A":
        return 2 * n - j, j
    if branch == "B":
        return 2 * n - j - 1, j, 1
    raise ValueError(branch)


def norm(n, branch, j):
    return F(hook_dimension(shape(n, branch, j)), n * comb(2 * n, n))


def diagonal_a(n, branch, j):
    """Diagonal of M_a in either projection or orthonormal gauge."""
    r = n - j
    if branch == "A":
        return F(n, 2) + F(n**3, 2 * j * r * (r + 1) * (j + 2 * r + 1))
    if branch == "B":
        numerator = (
            2 * j**3 * r**2
            + 6 * j**2 * r**3
            + 5 * j**2 * r**2
            + 4 * j * r**4
            + 10 * j * r**3
            + 2 * j * r**2
            + 4 * r**4
            + 2 * r**3
            + 2 * r**2
            - 1
        )
        denominator = (j + 1) * (2 * r - 1) * (2 * r + 1) * (j + 2 * r + 1)
        return F(numerator, denominator)
    raise ValueError(branch)


def same_level_projection(n, j):
    """Return (R[B_j,A_j], R[A_j,B_j]) in the projection gauge."""
    r = n - j
    ba = F(n * (r + 1), 2 * j * r * (2 * n - j + 1))
    ab = F(n * (2 * n - j) * (r + 1),
           (j + 1) * (2 * n - j + 1) * (2 * r + 1))
    return ba, ab


def raising_projection(n, j):
    """Rows (A_{j+1},B_{j+1}), columns (A_j,B_j).

    This is the upper triangular raising block of M_a in the projection
    gauge.  It is zero when j=n-1.
    """
    if j >= n - 1:
        return ((F(0), F(0)), (F(0), F(0)))
    r = n - j
    aa = F(j * (2 * n - j) * (r + 1) * (r - 1),
           2 * r * (2 * n - j + 1) * (2 * r - 1))
    ab = F(j * n * (r - 1),
           (j + 1) * (2 * n - j + 1) * (2 * r - 1))
    bb = F(j * (j + 2) * r,
           2 * (j + 1) * (2 * r - 1))
    return ((aa, ab), (F(0), bb))


def closed_a_projection(n):
    """Full exact M_a matrix, with target rows and source columns."""
    labels = cells(n)
    index = {label: pos for pos, label in enumerate(labels)}
    size = len(labels)
    matrix = [[F(0) for _ in range(size)] for _ in range(size)]

    for j in range(1, n):
        ai = index["A", j]
        bi = index["B", j]
        matrix[ai][ai] = diagonal_a(n, "A", j)
        matrix[bi][bi] = diagonal_a(n, "B", j)
        ba, ab = same_level_projection(n, j)
        matrix[bi][ai] = ba
        matrix[ai][bi] = ab

        if j == n - 1:
            continue
        an = index["A", j + 1]
        bn = index["B", j + 1]
        upper = raising_projection(n, j)
        matrix[an][ai], matrix[an][bi] = upper[0]
        matrix[bn][ai], matrix[bn][bi] = upper[1]

        # Self-adjointness: h_target R[target,source]
        # = h_source R[source,target].
        for target, source in ((an, ai), (an, bi), (bn, bi)):
            target_label = labels[target]
            source_label = labels[source]
            h_target = norm(n, *target_label)
            h_source = norm(n, *source_label)
            matrix[source][target] = matrix[target][source] * h_target / h_source
    return labels, matrix


def matmul(left, right):
    return [[sum(left[row][mid] * right[mid][col]
                 for mid in range(len(right)))
             for col in range(len(right[0]))]
            for row in range(len(left))]


def closed_x_projection(n):
    labels, a_matrix = closed_a_projection(n)
    square = matmul(a_matrix, a_matrix)
    x_matrix = [[n * a_matrix[row][col] - square[row][col]
                 for col in range(len(labels))]
                for row in range(len(labels))]
    return labels, x_matrix


def orthonormal_parameters(n, j):
    """Return dA,dB and the four nonnegative squared radical entries.

    In the orthonormal basis the diagonal block is

        D_j = [[dA, sqrt(beta2)], [sqrt(beta2), dB]],

    and the raising block (rows j+1, columns j) is

        U_j = [[sqrt(alpha2), sqrt(gamma2)], [0, sqrt(delta2)]].
    """
    r = n - j
    ba, ab = same_level_projection(n, j)
    beta2 = ba * ab
    if j == n - 1:
        alpha2 = gamma2 = delta2 = F(0)
    else:
        upper = raising_projection(n, j)
        uaa, uab, ubb = upper[0][0], upper[0][1], upper[1][1]
        alpha2 = uaa * uaa * norm(n, "A", j + 1) / norm(n, "A", j)
        gamma2 = uab * uab * norm(n, "A", j + 1) / norm(n, "B", j)
        delta2 = ubb * ubb * norm(n, "B", j + 1) / norm(n, "B", j)
    return {
        "dA": diagonal_a(n, "A", j),
        "dB": diagonal_a(n, "B", j),
        "beta2": beta2,
        "alpha2": alpha2,
        "gamma2": gamma2,
        "delta2": delta2,
    }


def reorder_marked_matrix(n, statistic):
    marked_shapes, marked, _ = multiplication_recurrence(n, statistic)
    marked_index = {(branch, j): pos
                    for pos, (branch, j, _) in enumerate(marked_shapes)}
    labels = cells(n)
    return [[marked[marked_index[target]][marked_index[source]]
             for source in labels] for target in labels]


def diagonal_similarity(matrix, labels, scales):
    """P_label=scales[label]*v_label, so E_ts=s_s/s_t R_ts."""
    return [[matrix[row][col] * scales[labels[col]] / scales[labels[row]]
             for col in range(len(labels))]
            for row in range(len(labels))]


def expected_rref_n3():
    labels = cells(3)
    index = {label: pos for pos, label in enumerate(labels)}
    matrix = [[F(0) for _ in labels] for _ in labels]
    columns = {
        ("A", 1): {("A", 1): F(7, 4), ("A", 2): F(-5, 24),
                   ("B", 1): F(-15, 64), ("B", 2): F(-225, 1024)},
        ("A", 2): {("A", 1): F(-27, 50), ("A", 2): F(31, 20),
                   ("B", 1): F(-81, 160), ("B", 2): F(-243, 512)},
        ("B", 1): {("A", 1): F(-8, 15), ("A", 2): F(-4, 9),
                   ("B", 1): F(3, 2), ("B", 2): F(-15, 32)},
        ("B", 2): {("A", 1): F(-1024, 1125), ("A", 2): F(-512, 675),
                   ("B", 1): F(-64, 75), ("B", 2): F(6, 5)},
    }
    for source, terms in columns.items():
        for target, value in terms.items():
            matrix[index[target]][index[source]] = value
    return labels, matrix


def expected_rref_n4():
    labels = cells(4)
    index = {label: pos for pos, label in enumerate(labels)}
    matrix = [[F(0) for _ in labels] for _ in labels]
    columns = {
        ("A", 1): {("A", 1): F(17, 5), ("B", 1): F(-28, 125),
                   ("A", 2): F(-7, 30), ("B", 2): F(-49, 150),
                   ("A", 3): F(-7, 54)},
        ("B", 1): {("A", 1): F(-15, 28), ("B", 1): F(3),
                   ("A", 2): F(-5, 8), ("B", 2): F(-35, 96),
                   ("A", 3): F(-25, 216), ("B", 3): F(-2, 3)},
        ("A", 2): {("A", 1): F(-24, 49), ("B", 1): F(-96, 175),
                   ("A", 2): F(23, 7), ("B", 2): F(-3, 10),
                   ("A", 3): F(-40, 63), ("B", 3): F(-16, 35)},
        ("B", 2): {("A", 1): F(-384, 343), ("B", 1): F(-128, 245),
                   ("A", 2): F(-24, 49), ("B", 2): F(143, 63),
                   ("A", 3): F(-2960, 3969), ("B", 3): F(-2752, 2205)},
        ("A", 3): {("A", 1): F(-54, 175), ("B", 1): F(-72, 625),
                   ("A", 2): F(-18, 25), ("B", 2): F(-259, 500),
                   ("A", 3): F(127, 45), ("B", 3): F(-16, 25)},
        ("B", 3): {("B", 1): F(-4, 5), ("A", 2): F(-5, 8),
                   ("B", 2): F(-301, 288), ("A", 3): F(-125, 162),
                   ("B", 3): F(20, 9)},
    }
    for source, terms in columns.items():
        for target, value in terms.items():
            matrix[index[target]][index[source]] = value
    return labels, matrix


def certify(limit=8):
    for n in range(2, limit + 1):
        labels, a_matrix = closed_a_projection(n)
        assert a_matrix == reorder_marked_matrix(n, "a"), n
        _, x_matrix = closed_x_projection(n)
        assert x_matrix == reorder_marked_matrix(n, "x"), n

        # The spectrum of a is 1,n once and every interior point twice.
        trace = sum(a_matrix[pos][pos] for pos in range(len(labels)))
        expected_trace = F(1 + n + 2 * sum(range(2, n)))
        assert trace == expected_trace

    labels3, expected3 = expected_rref_n3()
    labels, x3 = closed_x_projection(3)
    assert labels == labels3
    scales3 = {
        ("A", 1): F(1), ("B", 1): F(16, 15),
        ("A", 2): F(6, 5), ("B", 2): F(256, 225),
    }
    assert diagonal_similarity(x3, labels, scales3) == expected3

    labels4, expected4 = expected_rref_n4()
    labels, x4 = closed_x_projection(4)
    assert labels == labels4
    scales4 = {
        ("A", 1): F(1), ("B", 1): F(25, 28),
        ("A", 2): F(6, 7), ("B", 2): F(30, 49),
        ("A", 3): F(27, 35), ("B", 3): F(15, 28),
    }
    assert diagonal_similarity(x4, labels, scales4) == expected4


def print_diagonals(n):
    labels, matrix = closed_x_projection(n)
    print(f"n={n} M_x diagonals:")
    for pos, label in enumerate(labels):
        print(f"  {label[0]}{label[1]} = {matrix[pos][pos]}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certify-through", type=int, default=8)
    parser.add_argument("--predict", type=int, default=6)
    args = parser.parse_args()
    certify(args.certify_through)
    print(f"closed recurrence certified independently for 2 <= n <= "
          f"{args.certify_through}")
    print_diagonals(args.predict)


if __name__ == "__main__":
    main()
