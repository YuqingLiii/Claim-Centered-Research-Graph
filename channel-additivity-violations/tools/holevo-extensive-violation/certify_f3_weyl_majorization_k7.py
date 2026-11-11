#!/usr/bin/env python3
"""Exact KKT-face certificate for cumulative k=7 of the F_3^2 Weyl majorization.

After an affine symmetry, a maximum-mass affine line is row zero and the
three row masses obey a>=b>=c.  The resulting compact polytope has eight free
probabilities and twenty affine inequalities.  The k=7 condition is equivalent
to

    2 q_g >= c(b+c)

for one nonzero representative g in each of the four projective directions.
For every quadratic, the checker enumerates every linearly independent active
set of size at most eight and solves the exact KKT equations.  Singular KKT
systems need not be retained: a stationary minimum on such a face is constant
along a nonzero tangent direction and is also attained on a proper subface,
which appears later in the enumeration.
"""

import argparse
from fractions import Fraction
from itertools import combinations


Q = 3
VARIABLES = 8
NORMALS = ((1, 0), (0, 1), (1, 1), (1, 2))
SHIFTS = ((0, 1), (1, 0), (1, 2), (1, 1))


def add_forms(forms):
    forms = tuple(forms)
    return (
        sum(form[0] for form in forms),
        tuple(sum(form[1][i] for form in forms) for i in range(VARIABLES)),
    )


def subtract_forms(left, right):
    return left[0] - right[0], tuple(x - y for x, y in zip(left[1], right[1]))


def build_points_constraints_and_rows():
    points = []
    for point in range(9):
        if point < VARIABLES:
            coefficients = [0] * VARIABLES
            coefficients[point] = 1
            points.append((0, tuple(coefficients)))
        else:
            points.append((1, tuple([-1] * VARIABLES)))

    rows = tuple(add_forms(points[Q * row + column] for column in range(Q)) for row in range(Q))
    a, b, c = rows
    constraints = list(points)
    constraints.append(subtract_forms(a, b))
    constraints.append(subtract_forms(b, c))

    # Every affine line outside the selected parallel class has mass at most a.
    for u, v in NORMALS[1:]:
        for value in range(Q):
            line = [
                Q * i + j
                for i in range(Q)
                for j in range(Q)
                if (u * i + v * j) % Q == value
            ]
            constraints.append(subtract_forms(a, add_forms(points[index] for index in line)))
    assert len(constraints) == 20
    return tuple(points), tuple(constraints), rows


def add_product(hessian, linear, constant, left, right, weight):
    left_c, left_v = left
    right_c, right_v = right
    constant += weight * left_c * right_c
    for i in range(VARIABLES):
        linear[i] += weight * (left_c * right_v[i] + right_c * left_v[i])
        for j in range(VARIABLES):
            hessian[i][j] += weight * (
                left_v[i] * right_v[j] + right_v[i] * left_v[j]
            )
    return constant


def build_k7_objective(points, rows, shift):
    # f=2 q_shift-c(b+c), represented as
    # f(x)=constant+linear.x+(1/2)x^T hessian x.
    hessian = [[0] * VARIABLES for _ in range(VARIABLES)]
    linear = [0] * VARIABLES
    constant = 0
    di, dj = shift
    for i in range(Q):
        for j in range(Q):
            left = points[Q * i + j]
            right = points[Q * ((i - di) % Q) + ((j - dj) % Q)]
            constant = add_product(hessian, linear, constant, left, right, 2)
    _, b, c = rows
    constant = add_product(hessian, linear, constant, c, b, -1)
    constant = add_product(hessian, linear, constant, c, c, -1)
    return tuple(tuple(row) for row in hessian), tuple(linear), constant


def full_rank_mod_prime(matrix, prime=1_000_003):
    size = len(matrix)
    work = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(size):
        pivot = next((row for row in range(rank, size) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(rank + 1, size):
            factor = work[row][column]
            if factor:
                work[row] = [
                    (x - factor * y) % prime for x, y in zip(work[row], work[rank])
                ]
        rank += 1
    return rank == size


def solve_integer_system(matrix, right_side):
    size = len(matrix)
    augmented = [list(matrix[row]) + [right_side[row]] for row in range(size)]
    previous = 1
    for column in range(size - 1):
        pivot_row = next((row for row in range(column, size) if augmented[row][column]), None)
        if pivot_row is None:
            return None
        if pivot_row != column:
            augmented[column], augmented[pivot_row] = augmented[pivot_row], augmented[column]
        pivot = augmented[column][column]
        for row in range(column + 1, size):
            entry = augmented[row][column]
            for target in range(column + 1, size + 1):
                numerator = augmented[row][target] * pivot - entry * augmented[column][target]
                assert numerator % previous == 0
                augmented[row][target] = numerator // previous
            augmented[row][column] = 0
        previous = pivot
    if augmented[-1][size - 1] == 0:
        return None
    answer = [Fraction(0)] * size
    for row in range(size - 1, -1, -1):
        residual = Fraction(augmented[row][-1]) - sum(
            Fraction(augmented[row][column]) * answer[column]
            for column in range(row + 1, size)
        )
        answer[row] = residual / augmented[row][row]
    return tuple(answer)


def independent_rows(rows):
    if not rows:
        return True
    # A nonzero modular minor is a rigorous independence certificate.  If the
    # first prime is inconclusive, exact fraction elimination decides.
    work = [[entry % 1_000_003 for entry in row] for row in rows]
    rank = 0
    for column in range(VARIABLES):
        pivot = next((index for index in range(rank, len(rows)) if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], 1_000_001, 1_000_003)
        work[rank] = [(value * inverse) % 1_000_003 for value in work[rank]]
        for index in range(rank + 1, len(rows)):
            factor = work[index][column]
            if factor:
                work[index] = [
                    (x - factor * y) % 1_000_003 for x, y in zip(work[index], work[rank])
                ]
        rank += 1
    if rank == len(rows):
        return True

    exact = [[Fraction(entry) for entry in row] for row in rows]
    rank = 0
    for column in range(VARIABLES):
        pivot = next((index for index in range(rank, len(rows)) if exact[index][column]), None)
        if pivot is None:
            continue
        exact[rank], exact[pivot] = exact[pivot], exact[rank]
        pivot_value = exact[rank][column]
        exact[rank] = [value / pivot_value for value in exact[rank]]
        for index in range(rank + 1, len(rows)):
            factor = exact[index][column]
            if factor:
                exact[index] = [x - factor * y for x, y in zip(exact[index], exact[rank])]
        rank += 1
    return rank == len(rows)


def kkt_system(hessian, linear, constraints, active):
    active_rows = [constraints[index][1] for index in active]
    size = VARIABLES + len(active)
    matrix = [[0] * size for _ in range(size)]
    right_side = [0] * size
    for i in range(VARIABLES):
        right_side[i] = -linear[i]
        for j in range(VARIABLES):
            matrix[i][j] = hessian[i][j]
        for j, row in enumerate(active_rows):
            matrix[i][VARIABLES + j] = -row[i]
    for i, row in enumerate(active_rows):
        matrix[VARIABLES + i][:VARIABLES] = row
        right_side[VARIABLES + i] = -constraints[active[i]][0]
    return matrix, right_side


def feasible(point, constraints):
    return all(
        Fraction(constant) + sum(Fraction(value) * coordinate for value, coordinate in zip(row, point)) >= 0
        for constant, row in constraints
    )


def evaluate(objective, point):
    hessian, linear, constant = objective
    return (
        Fraction(constant)
        + sum(Fraction(value) * coordinate for value, coordinate in zip(linear, point))
        + Fraction(1, 2)
        * sum(
            Fraction(hessian[i][j]) * point[i] * point[j]
            for i in range(VARIABLES)
            for j in range(VARIABLES)
        )
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-active-sets", type=int, default=None)
    parser.add_argument("--progress-every", type=int, default=25_000)
    args = parser.parse_args()

    points, constraints, rows = build_points_constraints_and_rows()
    objectives = tuple(build_k7_objective(points, rows, shift) for shift in SHIFTS)
    total_active_sets = sum(1 for size in range(VARIABLES + 1) for _ in combinations(range(len(constraints)), size))
    assert total_active_sets == 263_950

    processed = 0
    independent = 0
    nonsingular = 0
    feasible_candidates = 0
    nonnegative_multiplier_candidates = 0
    smallest = None
    smallest_record = None
    stop = False
    for active_size in range(VARIABLES + 1):
        for active in combinations(range(len(constraints)), active_size):
            if args.max_active_sets is not None and processed >= args.max_active_sets:
                stop = True
                break
            processed += 1
            active_rows = [constraints[index][1] for index in active]
            if not independent_rows(active_rows):
                continue
            independent += 1
            for direction_index, objective in enumerate(objectives):
                matrix, right_side = kkt_system(objective[0], objective[1], constraints, active)
                # Nonzero modular determinant certifies nonsingularity.  A zero
                # residue is resolved by the exact solver rather than skipped.
                modular_full_rank = full_rank_mod_prime(matrix)
                solution = solve_integer_system(matrix, right_side)
                if solution is None:
                    assert not modular_full_rank
                    continue
                nonsingular += 1
                point = solution[:VARIABLES]
                multipliers = solution[VARIABLES:]
                if not feasible(point, constraints):
                    continue
                feasible_candidates += 1
                if any(multiplier < 0 for multiplier in multipliers):
                    continue
                nonnegative_multiplier_candidates += 1
                value = evaluate(objective, point)
                if smallest is None or value < smallest:
                    smallest = value
                    smallest_record = (active, direction_index, point, multipliers)
                assert value >= 0, (value, active, direction_index, point, multipliers)
            if args.progress_every and processed % args.progress_every == 0:
                print(
                    f"active_sets={processed}; independent={independent}; "
                    f"nonsingular_kkt={nonsingular}; feasible={feasible_candidates}; "
                    f"dual_feasible={nonnegative_multiplier_candidates}",
                    flush=True,
                )
        if stop:
            break

    complete = args.max_active_sets is None
    print(f"active sets enumerated: {processed}")
    print(f"independent active sets: {independent}")
    print(f"nonsingular KKT systems: {nonsingular}")
    print(f"feasible KKT candidates: {feasible_candidates}")
    print(f"dual-feasible KKT candidates: {nonnegative_multiplier_candidates}")
    print(f"smallest exact k=7 gap: {smallest}")
    print(f"smallest-gap record: {smallest_record}")
    if complete:
        print("F_3^2 selected-line Weyl majorization certified at cumulative k=7")
    else:
        print("SMOKE TEST ONLY: active-set enumeration was truncated")


if __name__ == "__main__":
    main()
