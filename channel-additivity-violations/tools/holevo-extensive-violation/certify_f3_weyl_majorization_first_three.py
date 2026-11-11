#!/usr/bin/env python3
"""Exact certificate for cumulative indices k=1,2,3 of the F_3^2 Weyl majorization.

The k=1 result is supplied by certify_f3_affine_line_l2_maximal.py.  This
checker proves k=3 after fixing a maximum affine line and ordering the three
parallel-line masses a>=b>=c.  The k=2 condition is the arithmetic mean of
k=1 and k=3.
"""

import argparse
from fractions import Fraction
from itertools import combinations


Q = 3
VARIABLES = 6


def add_forms(forms):
    forms = tuple(forms)
    return (
        sum(form[0] for form in forms),
        sum(form[1] for form in forms),
        sum(form[2] for form in forms),
        tuple(sum(form[3][i] for form in forms) for i in range(VARIABLES)),
    )


def subtract_forms(left, right):
    return (
        left[0] - right[0],
        left[1] - right[1],
        left[2] - right[2],
        tuple(x - y for x, y in zip(left[3], right[3])),
    )


def build_points_and_constraints():
    # Free variables: p00,p01,p10,p11,p20,p21.
    variable_for_point = {0: 0, 1: 1, 3: 2, 4: 3, 6: 4, 7: 5}
    points = []
    for point in range(9):
        coefficients = [0] * VARIABLES
        if point in variable_for_point:
            coefficients[variable_for_point[point]] = 1
            points.append((0, 0, 0, tuple(coefficients)))
        elif point == 2:  # p02=a-p00-p01
            coefficients[0] = coefficients[1] = -1
            points.append((0, 1, 0, tuple(coefficients)))
        elif point == 5:  # p12=b-p10-p11
            coefficients[2] = coefficients[3] = -1
            points.append((0, 0, 1, tuple(coefficients)))
        else:  # p22=1-a-b-p20-p21
            coefficients[4] = coefficients[5] = -1
            points.append((1, -1, -1, tuple(coefficients)))

    constraints = list(points)
    a_form = (0, 1, 0, tuple([0] * VARIABLES))
    directions = ((1, 0), (0, 1), (1, 1), (1, 2))
    lines = []
    for u, v in directions:
        direction_lines = []
        for value in range(Q):
            line = [
                Q * i + j
                for i in range(Q)
                for j in range(Q)
                if (u * i + v * j) % Q == value
            ]
            direction_lines.append(line)
        lines.append(direction_lines)

    # Direction zero is the selected row partition and is handled by the
    # parameter-domain constraints.  The other nine affine lines obey mass<=a.
    for direction_lines in lines[1:]:
        for line in direction_lines:
            constraints.append(
                subtract_forms(a_form, add_forms(points[index] for index in line))
            )
    assert len(constraints) == 18
    return points, constraints, lines


def full_rank_mod_prime(matrix, prime=1_000_003):
    work = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for column in range(VARIABLES):
        pivot = next((row for row in range(rank, VARIABLES) if work[row][column]), None)
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


def solve_integer_system(matrix, right_sides):
    size = len(matrix)
    rhs_count = len(right_sides)
    augmented = [
        list(matrix[row]) + [right_sides[j][row] for j in range(rhs_count)]
        for row in range(size)
    ]
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
            for target in range(column + 1, size + rhs_count):
                numerator = augmented[row][target] * pivot - entry * augmented[column][target]
                assert numerator % previous == 0
                augmented[row][target] = numerator // previous
            augmented[row][column] = 0
        previous = pivot
    if augmented[-1][size - 1] == 0:
        return None

    answers = []
    for rhs_column in range(size, size + rhs_count):
        answer = [Fraction(0) for _ in range(size)]
        for row in range(size - 1, -1, -1):
            residual = Fraction(augmented[row][rhs_column]) - sum(
                Fraction(augmented[row][column]) * answer[column]
                for column in range(row + 1, size)
            )
            answer[row] = residual / augmented[row][row]
        answers.append(tuple(answer))
    return tuple(answers)


def substituted_halfplane(form, u, v, w):
    c0, c_a, c_b, coefficients = form
    return (
        Fraction(c0) + sum(Fraction(x) * y for x, y in zip(coefficients, u)),
        Fraction(c_a) + sum(Fraction(x) * y for x, y in zip(coefficients, v)),
        Fraction(c_b) + sum(Fraction(x) * y for x, y in zip(coefficients, w)),
    )


def base_parameter_halfplanes():
    # c+h_a a+h_b b>=0, encoding 1/3<=a<=1, a>=b>=c>=0.
    return (
        (Fraction(-1, 3), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(-1)),       # a-b>=0
        (Fraction(-1), Fraction(1), Fraction(2)),      # b-c=a+2b-1>=0
        (Fraction(1), Fraction(-1), Fraction(-1)),     # c=1-a-b>=0
    )


def intersection(first, second):
    c1, a1, b1 = first
    c2, a2, b2 = second
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    a = (-c1 * b2 + c2 * b1) / determinant
    b = (-a1 * c2 + a2 * c1) / determinant
    return a, b


def satisfies(point, halfplanes):
    a, b = point
    return all(c + h_a * a + h_b * b >= 0 for c, h_a, h_b in halfplanes)


def polygon_vertices(halfplanes):
    vertices = set()
    for first, second in combinations(halfplanes, 2):
        point = intersection(first, second)
        if point is not None and satisfies(point, halfplanes):
            vertices.add(point)
    return tuple(vertices)


def affine_after_substitution(form, u, v, w):
    return substituted_halfplane(form, u, v, w)


def add_quadratics(left, right):
    return tuple(x + y for x, y in zip(left, right))


def negate_quadratic(value):
    return tuple(-x for x in value)


def square_affine(form):
    c, a, b = form
    # A a^2+B ab+C b^2+D a+E b+F
    return (a * a, 2 * a * b, b * b, 2 * c * a, 2 * c * b, c * c)


def collision_quadratic(direction_lines, points, u, v, w):
    result = (Fraction(0),) * 6
    for line in direction_lines:
        mass = add_forms(points[index] for index in line)
        result = add_quadratics(result, square_affine(affine_after_substitution(mass, u, v, w)))
    return result


def gap_quadratic(collision):
    # a^2+2ab-C_L
    target = (Fraction(1), Fraction(2), Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    return add_quadratics(target, negate_quadratic(collision))


def evaluate(poly, point):
    a, b = point
    aa, ab, bb, la, lb, constant = poly
    return aa * a * a + ab * a * b + bb * b * b + la * a + lb * b + constant


def segment_stationary(poly, first, second):
    da = second[0] - first[0]
    db = second[1] - first[1]
    aa, ab, bb, la, lb, _ = poly
    quadratic = aa * da * da + ab * da * db + bb * db * db
    linear = (
        2 * aa * first[0] * da
        + ab * (first[0] * db + first[1] * da)
        + 2 * bb * first[1] * db
        + la * da
        + lb * db
    )
    if quadratic <= 0:
        return None
    parameter = -linear / (2 * quadratic)
    if 0 <= parameter <= 1:
        return first[0] + parameter * da, first[1] + parameter * db
    return None


def interior_stationary(poly, halfplanes):
    aa, ab, bb, la, lb, _ = poly
    determinant = 4 * aa * bb - ab * ab
    if determinant == 0:
        return None
    a = (-2 * bb * la + ab * lb) / determinant
    b = (ab * la - 2 * aa * lb) / determinant
    point = (a, b)
    return point if satisfies(point, halfplanes) else None


def minimum_on_polygon(poly, vertices, halfplanes):
    candidates = list(vertices)
    for first, second in combinations(vertices, 2):
        stationary = segment_stationary(poly, first, second)
        if stationary is not None:
            candidates.append(stationary)
    stationary = interior_stationary(poly, halfplanes)
    if stationary is not None:
        candidates.append(stationary)
    assert candidates
    return min((evaluate(poly, point), point) for point in candidates)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-bases", type=int, default=None)
    parser.add_argument("--progress-every", type=int, default=5_000)
    args = parser.parse_args()

    points, constraints, lines = build_points_and_constraints()
    families = {}
    bases_seen = 0
    nonsingular = 0
    feasible = 0

    for active in combinations(range(len(constraints)), VARIABLES):
        if args.max_bases is not None and bases_seen >= args.max_bases:
            break
        bases_seen += 1
        matrix = [constraints[index][3] for index in active]
        if not full_rank_mod_prime(matrix):
            continue
        nonsingular += 1
        right_sides = [
            [-constraints[index][coordinate] for index in active]
            for coordinate in (0, 1, 2)
        ]
        solved = solve_integer_system(matrix, right_sides)
        assert solved is not None
        u, v, w = solved
        halfplanes = list(base_parameter_halfplanes())
        halfplanes.extend(substituted_halfplane(form, u, v, w) for form in constraints)
        vertices = polygon_vertices(halfplanes)
        if not vertices:
            continue
        feasible += 1
        key = u + v + w
        vertex_set = frozenset(vertices)
        if key in families:
            assert families[key] == vertex_set
        else:
            families[key] = vertex_set
        if args.progress_every and bases_seen % args.progress_every == 0:
            print(
                f"bases={bases_seen}; nonsingular={nonsingular}; feasible={feasible}; "
                f"unique_families={len(families)}",
                flush=True,
            )

    complete = args.max_bases is None
    if complete:
        assert bases_seen == 18_564

    smallest = None
    smallest_record = None
    for key, vertex_set in families.items():
        u = key[:VARIABLES]
        v = key[VARIABLES:2 * VARIABLES]
        w = key[2 * VARIABLES:]
        halfplanes = list(base_parameter_halfplanes())
        halfplanes.extend(substituted_halfplane(form, u, v, w) for form in constraints)
        vertices = tuple(vertex_set)
        for direction_index, direction_lines in enumerate(lines):
            collision = collision_quadratic(direction_lines, points, u, v, w)
            gap = gap_quadratic(collision)
            value, location = minimum_on_polygon(gap, vertices, halfplanes)
            if smallest is None or value < smallest:
                smallest = value
                smallest_record = (direction_index, location, gap)
            assert value >= 0

    print(f"bases enumerated: {bases_seen}")
    print(f"nonsingular active bases: {nonsingular}")
    print(f"feasible active bases: {feasible}")
    print(f"unique affine vertex families: {len(families)}")
    print(f"smallest exact k=3 gap: {smallest}")
    print(f"smallest-gap direction/location/polynomial: {smallest_record}")
    if complete:
        print("F_3^2 selected-line Weyl majorization certified for cumulative k=1,2,3")
    else:
        print("SMOKE TEST ONLY: active-basis enumeration was truncated")


if __name__ == "__main__":
    main()
