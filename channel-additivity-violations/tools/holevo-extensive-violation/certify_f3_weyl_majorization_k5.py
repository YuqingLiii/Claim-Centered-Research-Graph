#!/usr/bin/env python3
"""Exact KKT-face certificate for cumulative k=5 of the F_3^2 Weyl majorization.

The checker proves the stronger uniform inequality

    C_i+C_j-q_0 <= 2a-a^2

for every pair of projective directions.  Here a is the mass of a selected
maximum affine line and C_i is the collision probability of the corresponding
three-line quotient.  The left side is the candidate top-five autocorrelation
sum, while ``2a-a^2`` is one of the two algebraic branches of the top-five
product sum and never exceeds that sorted sum.

The exact active-face/KKT completeness argument and polytope conventions are
shared with ``certify_f3_weyl_majorization_k7.py``.
"""

import argparse
from fractions import Fraction
from itertools import combinations

from certify_f3_weyl_majorization_k7 import (
    NORMALS,
    VARIABLES,
    add_forms,
    add_product,
    build_points_constraints_and_rows,
    evaluate,
    feasible,
    full_rank_mod_prime,
    independent_rows,
    kkt_system,
    solve_integer_system,
)


def add_affine(linear, constant, form, weight):
    form_constant, coefficients = form
    constant += weight * form_constant
    for index, coefficient in enumerate(coefficients):
        linear[index] += weight * coefficient
    return constant


def quotient_lines(points, normal):
    u, v = normal
    return tuple(
        add_forms(
            points[3 * i + j]
            for i in range(3)
            for j in range(3)
            if (u * i + v * j) % 3 == value
        )
        for value in range(3)
    )


def build_k5_objective(points, rows, pair):
    # f=2a-a^2-C_i-C_j+q_0.
    hessian = [[0] * VARIABLES for _ in range(VARIABLES)]
    linear = [0] * VARIABLES
    constant = 0
    a = rows[0]
    constant = add_affine(linear, constant, a, 2)
    constant = add_product(hessian, linear, constant, a, a, -1)
    for direction_index in pair:
        for line_mass in quotient_lines(points, NORMALS[direction_index]):
            constant = add_product(hessian, linear, constant, line_mass, line_mass, -1)
    for point in points:
        constant = add_product(hessian, linear, constant, point, point, 1)
    return tuple(tuple(row) for row in hessian), tuple(linear), constant


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-active-sets", type=int, default=None)
    parser.add_argument("--progress-every", type=int, default=25_000)
    args = parser.parse_args()

    points, constraints, rows = build_points_constraints_and_rows()
    pairs = tuple(combinations(range(len(NORMALS)), 2))
    objectives = tuple(build_k5_objective(points, rows, pair) for pair in pairs)
    total_active_sets = sum(
        1
        for size in range(VARIABLES + 1)
        for _ in combinations(range(len(constraints)), size)
    )
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
            for pair, objective in zip(pairs, objectives):
                matrix, right_side = kkt_system(objective[0], objective[1], constraints, active)
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
                    smallest_record = (active, pair, point, multipliers)
                assert value >= 0, (value, active, pair, point, multipliers)
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
    print(f"smallest exact stronger k=5 gap: {smallest}")
    print(f"smallest-gap record: {smallest_record}")
    if complete:
        print("F_3^2 selected-line Weyl majorization certified at cumulative k=5")
    else:
        print("SMOKE TEST ONLY: active-set enumeration was truncated")


if __name__ == "__main__":
    main()
