#!/usr/bin/env python3
"""Small exact examples for the registered balance-rigidity/root-frame nodes.

Python standard library only. All matrix arithmetic uses fractions.Fraction.
Finite checks support these examples, not the universal author-level proofs.
"""

from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import platform


def matrix(rows):
    return [[F(x) for x in row] for row in rows]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt]
            for row in a]


def scale(a, factor):
    return [[x * factor for x in row] for row in a]


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def diagonal(a):
    return [a[i][i] for i in range(len(a))]


def trace(a):
    return sum(diagonal(a), F(0))


def rank(a):
    a = [row[:] for row in a]
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        leading = a[pivot_row][col]
        a[pivot_row] = [x / leading for x in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                multiple = a[i][col]
                a[i] = [x - multiple * y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def quadratic_map(rows):
    """Coefficients of diag(R B R^T) in upper-triangular entries of B."""
    r = len(rows[0])
    positions = [(i, j) for i in range(r) for j in range(i, r)]
    return matrix([[(1 if i == j else 2) * row[i] * row[j]
                    for i, j in positions] for row in rows])


def assert_simultaneous_symmetry(a, permutation):
    assert [[a[permutation[i]][permutation[j]] for j in range(len(a))]
            for i in range(len(a))] == a


def simplex_example():
    rows = matrix([[1, 1], [-1, 1], [0, -2]])
    gram = multiply(transpose(rows), rows)
    assert gram == matrix([[2, 0], [0, 6]])
    inverse_gram = matrix([[F(1, 2), 0], [0, F(1, 6)]])
    a = multiply(multiply(rows, inverse_gram), transpose(rows))
    expected = matrix([[F(int(i == j)) - F(1, 3) for j in range(3)]
                       for i in range(3)])
    assert a == expected
    assert multiply(a, a) == a and rank(a) == 2
    for permutation in permutations(range(3)):
        assert_simultaneous_symmetry(a, permutation)
    # Congruence B=C^-1 H C^-1, C=diag(sqrt(2),sqrt(6)).
    b0 = matrix([[F(3, 4), 0], [0, F(1, 4)]])
    strategy_gram = multiply(multiply(rows, b0), transpose(rows))
    assert diagonal(strategy_gram) == [F(1)] * 3
    assert trace(multiply(a, strategy_gram)) == 3
    map_rank = rank(quadratic_map(rows))
    assert map_rank == 3
    return {"matrix": "I_3-J_3/3", "n": 3, "top_rank": 2,
            "balance_map_rank": map_rank, "kernel_dimension": 0,
            "exact_strategy_gram_rank": rank(strategy_gram), "objective": 3,
            "checked_simultaneous_permutations": 6}


def identity_example():
    a = identity(3)
    k = matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    endpoint = matrix([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    factor = matrix([[1, 0], [1, 0], [0, 1]])
    assert endpoint == multiply(factor, transpose(factor))
    assert diagonal(k) == [F(0)] * 3
    assert diagonal(endpoint) == [F(1)] * 3 and rank(endpoint) == 2
    all_ones = matrix([[1] * 3 for _ in range(3)])
    assert all_ones == multiply(matrix([[1], [1], [1]]), matrix([[1, 1, 1]]))
    assert diagonal(all_ones) == [F(1)] * 3 and rank(all_ones) == 1
    for permutation in permutations(range(3)):
        assert_simultaneous_symmetry(a, permutation)
    map_rank = rank(quadratic_map(a))
    assert map_rank == 3
    assert trace(multiply(a, all_ones)) == 3
    return {"matrix": "I_3", "n": 3, "top_rank": 3,
            "balance_map_rank": map_rank, "kernel_dimension": 6 - map_rank,
            "endpoint_rank": 2, "smaller_feasible_rank": 1, "objective": 3,
            "checked_simultaneous_permutations": 6}


def root_example(r):
    roots = []
    for i, j in combinations(range(r), 2):
        for first, second in product((-1, 1), repeat=2):
            row = [0] * r
            row[i], row[j] = first, second
            roots.append(tuple(row))
    n = 2 * r * (r - 1)
    assert len(roots) == len(set(roots)) == n
    w = matrix(roots)
    frame_constant = 4 * (r - 1)
    assert multiply(transpose(w), w) == scale(identity(r), frame_constant)
    a = scale(multiply(w, transpose(w)), F(1, frame_constant))
    assert multiply(a, a) == a and a == transpose(a)
    assert rank(a) == trace(a) == r
    assert diagonal(a) == [F(1, 2 * (r - 1))] * n
    index = {root: i for i, root in enumerate(roots)}
    generators = []
    # Adjacent coordinate swaps and a sign flip generate signed permutations.
    for i in range(r - 1):
        permutation = []
        for root in roots:
            transformed = list(root)
            transformed[i], transformed[i + 1] = transformed[i + 1], transformed[i]
            permutation.append(index[tuple(transformed)])
        generators.append(permutation)
    generators.append([index[(-root[0], *root[1:])] for root in roots])
    for permutation in generators:
        assert sorted(permutation) == list(range(n))
        assert_simultaneous_symmetry(a, permutation)
    reached, frontier = {0}, [0]
    while frontier:
        i = frontier.pop()
        for permutation in generators:
            j = permutation[i]
            if j not in reached:
                reached.add(j)
                frontier.append(j)
    assert len(reached) == n
    map_rank = rank(quadratic_map(w))
    assert map_rank == r * (r + 1) // 2
    # Exact Gram of the unit-row strategy X=Y=W/sqrt(2).
    strategy_gram = scale(multiply(w, transpose(w)), F(1, 2))
    assert diagonal(strategy_gram) == [F(1)] * n
    assert rank(strategy_gram) == r
    assert trace(multiply(a, strategy_gram)) == n
    return {"r": r, "n": n, "frame_constant": frame_constant,
            "projection_rank": r, "balance_map_rank": map_rank,
            "kernel_dimension": 0, "generator_count": len(generators),
            "orbit_size": len(reached), "exact_strategy_gram_rank": r,
            "objective": n}


def main():
    result = {"python_version": platform.python_version(),
              "arithmetic": "fractions.Fraction; no floating-point arithmetic",
              "scope": "Finite exact example checks; universal proofs require separate review",
              "simplex_example": simplex_example(),
              "identity_example": identity_example(),
              "root_frame_examples": [root_example(r) for r in (3, 4, 5)],
              "status": "all assertions passed"}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
