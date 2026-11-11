#!/usr/bin/env python3
"""Exact parametric-vertex certificate for the F_3^2 affine-line L2 bound.

For a probability distribution p on the nine points of F_3^2, let M be an
upper bound on every affine-line mass.  The checker proves

    sum_x p_x^2 <= M^2,   1/3 <= M <= 1.

It eliminates p_8, enumerates every eight-constraint basis of the resulting
eight-dimensional parametric polytope, reconstructs each affine vertex over
the rationals, computes its exact feasible M interval, and minimizes the
quadratic gap on that interval.  Convexity of sum p_x^2 ensures that a maximum
over each fixed-M polytope occurs at a vertex.
"""

import argparse
from fractions import Fraction
from itertools import combinations


Q = 3
VARIABLES = 8


def point_form(index):
    """Return c0,cM,coefficients for p_index after eliminating p_8."""
    if index < VARIABLES:
        coefficients = [0] * VARIABLES
        coefficients[index] = 1
        return 0, 0, tuple(coefficients)
    return 1, 0, tuple([-1] * VARIABLES)


def add_forms(forms):
    forms = tuple(forms)
    c0 = sum(form[0] for form in forms)
    c_m = sum(form[1] for form in forms)
    coefficients = tuple(
        sum(form[2][index] for form in forms)
        for index in range(VARIABLES)
    )
    return c0, c_m, coefficients


def full_rank_mod_prime(matrix, prime=1_000_003):
    """Exact rank gate; Hadamard bounds every nonzero determinant below prime."""
    work = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(VARIABLES):
        pivot = next(
            (row for row in range(rank, VARIABLES) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(rank + 1, VARIABLES):
            factor = work[row][column]
            if factor:
                work[row] = [
                    (x - factor * y) % prime
                    for x, y in zip(work[row], work[rank])
                ]
        rank += 1
    return rank == VARIABLES


def subtract_forms(left, right):
    return (
        left[0] - right[0],
        left[1] - right[1],
        tuple(x - y for x, y in zip(left[2], right[2])),
    )


def build_constraints():
    points = [point_form(index) for index in range(Q * Q)]
    constraints = list(points)  # p_x >= 0
    m_form = (0, 1, tuple([0] * VARIABLES))
    directions = ((1, 0), (0, 1), (1, 1), (1, 2))
    for u, v in directions:
        for value in range(Q):
            line = [
                Q * i + j
                for i in range(Q)
                for j in range(Q)
                if (u * i + v * j) % Q == value
            ]
            line_form = add_forms(points[index] for index in line)
            constraints.append(subtract_forms(m_form, line_form))
    assert len(constraints) == 21
    return points, constraints


def solve_two_integer_system(matrix, rhs_zero, rhs_m):
    """Fraction-free elimination for A u=rhs_zero and A v=rhs_m."""
    size = len(matrix)
    augmented = [
        list(matrix[row]) + [rhs_zero[row], rhs_m[row]]
        for row in range(size)
    ]
    previous = 1
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot_row is None:
            return None
        if pivot_row != column:
            augmented[column], augmented[pivot_row] = augmented[pivot_row], augmented[column]
        pivot = augmented[column][column]
        for row in range(column + 1, size):
            entry = augmented[row][column]
            for target in range(column + 1, size + 2):
                numerator = augmented[row][target] * pivot - entry * augmented[column][target]
                assert numerator % previous == 0
                augmented[row][target] = numerator // previous
            augmented[row][column] = 0
        previous = pivot
    if augmented[-1][-3] == 0:
        return None

    solutions = []
    for rhs_column in (size, size + 1):
        solution = [Fraction(0) for _ in range(size)]
        for row in range(size - 1, -1, -1):
            residual = Fraction(augmented[row][rhs_column]) - sum(
                Fraction(augmented[row][column]) * solution[column]
                for column in range(row + 1, size)
            )
            solution[row] = residual / augmented[row][row]
        solutions.append(tuple(solution))
    return tuple(solutions)


def feasible_interval(u, v, constraints):
    lower = Fraction(1, 3)
    upper = Fraction(1)
    for c0, c_m, coefficients in constraints:
        alpha = Fraction(c0) + sum(Fraction(a) * x for a, x in zip(coefficients, u))
        beta = Fraction(c_m) + sum(Fraction(a) * x for a, x in zip(coefficients, v))
        if beta > 0:
            lower = max(lower, -alpha / beta)
        elif beta < 0:
            upper = min(upper, -alpha / beta)
        elif alpha < 0:
            return None
        if lower > upper:
            return None
    return lower, upper


def gap_coefficients(u, v):
    full_u = tuple(u) + (Fraction(1) - sum(u),)
    full_v = tuple(v) + (-sum(v),)
    quadratic = Fraction(1) - sum(value * value for value in full_v)
    linear = -2 * sum(x * y for x, y in zip(full_u, full_v))
    constant = -sum(value * value for value in full_u)
    return quadratic, linear, constant


def evaluate_quadratic(coefficients, value):
    quadratic, linear, constant = coefficients
    return quadratic * value * value + linear * value + constant


def minimum_on_interval(coefficients, interval):
    lower, upper = interval
    candidates = [lower, upper]
    quadratic, linear, _ = coefficients
    if quadratic > 0:
        stationary = -linear / (2 * quadratic)
        if lower <= stationary <= upper:
            candidates.append(stationary)
    values = [(evaluate_quadratic(coefficients, point), point) for point in candidates]
    return min(values, key=lambda item: item[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max-bases",
        type=int,
        default=None,
        help="smoke-test prefix only; omission is required for a complete certificate",
    )
    parser.add_argument("--progress-every", type=int, default=50_000)
    args = parser.parse_args()

    _, constraints = build_constraints()
    vertices = {}
    bases_seen = 0
    nonsingular_bases = 0
    feasible_bases = 0

    for active in combinations(range(len(constraints)), VARIABLES):
        if args.max_bases is not None and bases_seen >= args.max_bases:
            break
        bases_seen += 1
        matrix = [constraints[index][2] for index in active]
        if not full_rank_mod_prime(matrix):
            continue
        rhs_zero = [-constraints[index][0] for index in active]
        rhs_m = [-constraints[index][1] for index in active]
        solved = solve_two_integer_system(matrix, rhs_zero, rhs_m)
        assert solved is not None
        nonsingular_bases += 1
        u, v = solved
        interval = feasible_interval(u, v, constraints)
        if interval is None:
            continue
        feasible_bases += 1
        key = u + v
        if key in vertices:
            assert vertices[key] == interval
        else:
            vertices[key] = interval
        if args.progress_every and bases_seen % args.progress_every == 0:
            print(
                f"bases={bases_seen}; nonsingular={nonsingular_bases}; "
                f"feasible={feasible_bases}; unique_vertices={len(vertices)}",
                flush=True,
            )

    complete = args.max_bases is None
    if complete:
        assert bases_seen == 203_490

    smallest_gap = None
    smallest_record = None
    for key, interval in vertices.items():
        u = key[:VARIABLES]
        v = key[VARIABLES:]
        coefficients = gap_coefficients(u, v)
        gap, location = minimum_on_interval(coefficients, interval)
        if smallest_gap is None or gap < smallest_gap:
            smallest_gap = gap
            smallest_record = (interval, location, coefficients)
        assert gap >= 0

    print(f"bases enumerated: {bases_seen}")
    print(f"nonsingular active bases: {nonsingular_bases}")
    print(f"feasible active bases: {feasible_bases}")
    print(f"unique affine vertex families: {len(vertices)}")
    print(f"smallest exact vertex gap: {smallest_gap}")
    print(f"smallest-gap interval/location/coefficients: {smallest_record}")
    if complete:
        print("F_3^2 affine-line L2 maximal inequality certified for all M in [1/3,1]")
    else:
        print("SMOKE TEST ONLY: active-basis enumeration was truncated")


if __name__ == "__main__":
    main()
