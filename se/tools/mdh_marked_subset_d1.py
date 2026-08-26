"""Exact marked-subset model for the ((n-1,1),(n)) SE tower.

Let Omega consist of pairs (S,s), where S is an n-subset of [2n] and s is
marked in S.  The fiber-zero-sum submodule is

    Ind_{S_n x S_n}^{S_{2n}} (S^(n-1,1) tensor 1).

It is the target tower.  This script works on the orbit quotient for

    H = S_{A-{0}} x S_B,  A=[n], B=[n,2n),

and projects the base vector e_(A,0) - (1/n) sum_{s in A} e_(A,s) onto the
two multiplicity-free branches

    A_j = (2n-j,j),             1 <= j < n,
    B_j = (2n-j-1,j,1),         1 <= j < n.

The projection uses a separating central element C2 + 97*C3.  On S^lambda,

    C2 = sum(contents),
    C3 = sum(contents^2) - binom(2n,2).

All calculations use Fraction.  This is an independent exact certificate for
the gauge-invariant M_x diagonals; it does not call the MDH block engine.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


F = Fraction
C3_SCALE = 97


def content_moment(lam, power):
    return sum((col - row) ** power
               for row, width in enumerate(lam)
               for col in range(width))


def central_eigenvalue(lam, total):
    c2 = content_moment(lam, 1)
    c3 = content_moment(lam, 2) - comb(total, 2)
    return c2 + C3_SCALE * c3


def orbit_label(n, subset, mark):
    a = sum(value < n for value in subset)
    contains_zero = int(0 in subset)
    mark_class = 0 if mark == 0 else (1 if mark < n else 2)
    return a, contains_zero, mark_class


def orbit_data(n):
    """Return (label, representative, orbit size) for every H-orbit."""
    data = []
    for a in range(n + 1):
        for contains_zero in (0, 1):
            a_other = a - contains_zero
            if not 0 <= a_other <= n - 1:
                continue
            subset = set(([0] if contains_zero else []))
            subset.update(range(1, 1 + a_other))
            subset.update(range(n, 2 * n - a))
            for mark_class in (0, 1, 2):
                marks = [value for value in subset
                         if (0 if value == 0 else
                             (1 if value < n else 2)) == mark_class]
                if not marks:
                    continue
                mark_count = (1 if mark_class == 0 else
                              a_other if mark_class == 1 else n - a)
                size = (mark_count * comb(n - 1, a_other) *
                        comb(n, n - a))
                label = a, contains_zero, mark_class
                data.append((label, (frozenset(subset), marks[0]), size))
    return data


def apply_permutation(subset, mark, permutation):
    image = frozenset(permutation.get(value, value) for value in subset)
    return image, permutation.get(mark, mark)


def central_quotient(n, orbits):
    """Quotient matrix of C2 + C3_SCALE*C3 on H-invariant functions."""
    index = {label: pos for pos, (label, _, _) in enumerate(orbits)}
    matrix = [[0] * len(orbits) for _ in orbits]

    def add_image(row, subset, mark, permutation, weight):
        image, image_mark = apply_permutation(subset, mark, permutation)
        col = index[orbit_label(n, image, image_mark)]
        matrix[row][col] += weight

    for row, (_, (subset, mark), _) in enumerate(orbits):
        for left, right in combinations(range(2 * n), 2):
            add_image(row, subset, mark,
                      {left: right, right: left}, 1)

        for first, second, third in combinations(range(2 * n), 3):
            add_image(row, subset, mark,
                      {first: second, second: third, third: first},
                      C3_SCALE)
            add_image(row, subset, mark,
                      {first: third, third: second, second: first},
                      C3_SCALE)
    return matrix


def matvec(matrix, vector):
    return [sum(F(entry) * value for entry, value in zip(row, vector))
            for row in matrix]


def spectral_projection(matrix, vector, eigenvalue, spectrum):
    result = list(vector)
    for other in spectrum:
        if other == eigenvalue:
            continue
        image = matvec(matrix, result)
        result = [(left - other * right) / F(eigenvalue - other)
                  for left, right in zip(image, result)]
    return result


def tower_shapes(n):
    shapes = [("A", j, (2 * n - j, j)) for j in range(1, n)]
    shapes += [("B", j, (2 * n - j - 1, j, 1))
               for j in range(1, n)]
    return shapes


def hook_dimension(lam):
    """Dimension of the Specht module S^lam by the hook-length formula."""
    total = sum(lam)
    denominator = 1
    for row, width in enumerate(lam):
        for col in range(width):
            below = sum(col < lower_width for lower_width in lam[row + 1:])
            denominator *= width - col + below
    return factorial(total) // denominator


def tower_projection_data(n):
    """Return the exact projected vectors and their canonical squared norms.

    The vectors are E_lambda v_0, with E_lambda the central primitive
    idempotent and v_0 the distinguished (n-1,1)-vector at the base subset.
    Their normalization is intrinsic, unlike the block engine's RREF gauge.
    """
    orbits = orbit_data(n)
    quotient = central_quotient(n, orbits)
    shapes = tower_shapes(n)
    spectrum = [central_eigenvalue(lam, 2 * n) for _, _, lam in shapes]
    if len(spectrum) != len(set(spectrum)):
        raise AssertionError("C2 + 97*C3 did not separate the tower")

    base = [F(0) for _ in orbits]
    for pos, (label, _, _) in enumerate(orbits):
        if label == (n, 1, 0):
            base[pos] = F(n - 1, n)
        elif label == (n, 1, 1):
            base[pos] = F(-1, n)

    sizes = [size for _, _, size in orbits]
    vectors = []
    norms = []
    for _, _, lam in shapes:
        eigenvalue = central_eigenvalue(lam, 2 * n)
        vector = spectral_projection(quotient, base, eigenvalue, spectrum)
        assert matvec(quotient, vector) == [eigenvalue * value
                                            for value in vector]
        norm = sum(F(size) * value * value
                   for size, value in zip(sizes, vector))
        expected = F(hook_dimension(lam), n * comb(2 * n, n))
        assert norm == expected, (n, lam, norm, expected)
        vectors.append(vector)
        norms.append(norm)
    return orbits, shapes, vectors, norms


def multiplication_recurrence(n, statistic="x"):
    """Exact recurrence in the central-projection gauge.

    The returned matrix uses ``matrix[target][source]`` so that its source
    column contains the coefficients of M P_source.  ``statistic='a'`` uses
    a=|S intersect [n]|; ``statistic='x'`` uses x=a(n-a).
    """
    if statistic not in {"a", "x"}:
        raise ValueError("statistic must be 'a' or 'x'")
    orbits, shapes, vectors, norms = tower_projection_data(n)
    sizes = [size for _, _, size in orbits]
    a_values = [label[0] for label, _, _ in orbits]
    values = (a_values if statistic == "a" else
              [a * (n - a) for a in a_values])

    matrix = []
    for target, target_vector in enumerate(vectors):
        row = []
        for source_vector in vectors:
            numerator = sum(F(size) * value * left * right
                            for size, value, left, right in
                            zip(sizes, values, target_vector, source_vector))
            row.append(numerator / norms[target])
        matrix.append(row)

    # Multiplication by x is exactly n M_a - M_a^2 in this common basis.
    if statistic == "x":
        a_matrix = multiplication_recurrence(n, "a")[1]
        square = [[sum(a_matrix[row][mid] * a_matrix[mid][col]
                       for mid in range(len(shapes)))
                   for col in range(len(shapes))]
                  for row in range(len(shapes))]
        expected = [[n * a_matrix[row][col] - square[row][col]
                     for col in range(len(shapes))]
                    for row in range(len(shapes))]
        assert matrix == expected
    return shapes, matrix, norms


def tower_diagonals(n):
    orbits, shapes, vectors, norms = tower_projection_data(n)
    sizes = [size for _, _, size in orbits]
    x_values = [label[0] * (n - label[0]) for label, _, _ in orbits]
    answer = {}
    for (branch, j, _), vector, norm in zip(shapes, vectors, norms):
        numerator = sum(F(size) * x * value * value
                        for size, x, value in zip(sizes, x_values, vector))
        answer[(branch, j)] = numerator / norm
    return answer


def certified_closed_forms(n):
    """The two D1 formulas currently derived independently of interpolation."""
    return {
        ("A", 1): F(n * (2 * n * n - 4 * n + 1), 4 * (2 * n - 3)),
        ("B", 1): F(n * (n - 1), 4),
    }


KNOWN = {
    2: {("A", 1): F(1, 2), ("B", 1): F(1, 2)},
    3: {
        ("A", 1): F(7, 4), ("A", 2): F(31, 20),
        ("B", 1): F(3, 2), ("B", 2): F(6, 5),
    },
    4: {
        ("A", 1): F(17, 5), ("A", 2): F(23, 7),
        ("A", 3): F(127, 45), ("B", 1): F(3),
        ("B", 2): F(143, 63), ("B", 3): F(20, 9),
    },
    5: {
        ("A", 1): F(155, 28), ("A", 2): F(2857, 540),
        ("B", 1): F(5),
    },
}


def certify(n, diagonals):
    for key, expected in KNOWN.get(n, {}).items():
        assert diagonals[key] == expected, (n, key, diagonals[key], expected)
    for key, expected in certified_closed_forms(n).items():
        assert diagonals[key] == expected, (n, key, diagonals[key], expected)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="*", type=int, default=[2, 3, 4, 5, 6])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--recurrence", choices=("a", "x"))
    args = parser.parse_args()

    payload = {}
    for n in args.n:
        if n < 2:
            raise ValueError("n must be at least 2")
        diagonals = tower_diagonals(n)
        certify(n, diagonals)
        payload[str(n)] = {f"{branch}{j}": str(value)
                           for (branch, j), value in sorted(diagonals.items())}
        if not args.json:
            print(f"n={n}: " + "  ".join(
                f"{branch}{j}={value}"
                for (branch, j), value in sorted(diagonals.items())))
            if args.recurrence:
                shapes, matrix, norms = multiplication_recurrence(
                    n, args.recurrence)
                print(f"  M_{args.recurrence} recurrence "
                      "(target rows, source columns):")
                for source, (branch, j, _) in enumerate(shapes):
                    terms = []
                    for target, (out_branch, out_j, _) in enumerate(shapes):
                        coefficient = matrix[target][source]
                        if coefficient:
                            terms.append(f"{coefficient} {out_branch}{out_j}")
                    print(f"    {branch}{j} -> " + " + ".join(terms))
                print("  norms: " + "  ".join(
                    f"{branch}{j}={norm}"
                    for (branch, j, _), norm in zip(shapes, norms)))
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
