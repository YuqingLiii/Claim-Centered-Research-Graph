#!/usr/bin/env python3
"""Exact six-dimensional certificate for the input-centered SU(3) three-face triangle."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

import certify_su3_highest_edge_adjacent_faces as bernstein_core
from certify_su3_adjacent_elementary_faces import component_entropy_upper
from certify_su3_all_elementary_cycles import (
    entropy_bounds,
    isotropic_probabilities,
    log_bounds,
)
from certify_su3_triangular_three_face_clusters import (
    Configuration,
    add_dense_controls,
    binary_interval_entropy_upper,
    build_union,
    compact_q_tail_parameter_upper,
    endpoint_patterns,
    gram_t,
    retained_side_distributions,
    shifted_offsets,
)
from su3_common_den_controls import (
    CommonDenControls,
    common_den_controls,
    rational_range_common,
    split_common_controls,
)


F = Fraction
NVAR = 6
bernstein_core.NVAR = NVAR
Poly = dict[tuple[int, ...], F]
MAX_DEPTH_PER_AXIS = 6
CONFIG = Configuration(
    "input-centered-four-side",
    ((-2, 1), (-1, -1), (0, 0)),
    (
        ((-2, 0), "binary"),
        ((-1, 1), "binary"),
        ((1, 0), "binary"),
        ((2, -2), "binary"),
    ),
    12,
)

constant = bernstein_core.constant
linear = bernstein_core.linear
poly_add = bernstein_core.poly_add
poly_mul = bernstein_core.poly_mul
scaled = bernstein_core.scaled
poly_evaluate = bernstein_core.poly_evaluate
polynomial_degrees = bernstein_core.polynomial_degrees
tensor_interpolate = bernstein_core.tensor_interpolate
bernstein_coefficients = bernstein_core.bernstein_coefficients
split_controls = split_common_controls
rational_range = rational_range_common


def compactify(poly, p_degree, q_degree):
    result = {}
    from math import comb
    for monomial, coefficient in poly.items():
        p_power, q_power = monomial[:2]
        for p_tail in range(p_degree - p_power + 1):
            p_coefficient = F(comb(p_degree - p_power, p_tail)) * (-1) ** p_tail
            for q_tail in range(q_degree - q_power + 1):
                q_coefficient = F(comb(q_degree - q_power, q_tail)) * (-1) ** q_tail
                target = (p_power + p_tail, q_power + q_tail) + monomial[2:]
                result[target] = result.get(target, F(0)) + (
                    coefficient * p_coefficient * q_coefficient
                )
    return {monomial: value for monomial, value in result.items() if value}


def dimension_poly(offset):
    r, s = offset
    first = linear(0, F(r + 1))
    second = linear(1, F(s + 1))
    third = poly_add(
        poly_add(linear(0, F(0)), linear(1, F(0))),
        constant(F(r + s + 2)),
    )
    return scaled(poly_mul(poly_mul(first, second), third), F(1, 2))


def factor_poly(key):
    p_coefficient, q_coefficient, constant_value = key
    result = constant(F(constant_value))
    if p_coefficient:
        result = poly_add(result, linear(0, F(0)))
    if q_coefficient:
        result = poly_add(result, linear(1, F(0)))
    return result


def gram_denominator(union):
    environment_offsets, input_offsets = shifted_offsets(CONFIG, union)
    total_input = constant(F(0))
    for offset in input_offsets:
        total_input = poly_add(total_input, dimension_poly(offset))
    factor_keys = set()
    for r, s in environment_offsets:
        factor_keys.update(((1, 0, r + 1), (0, 1, s + 1), (1, 1, r + s + 2)))
    result = scaled(total_input, F(8))
    for key in sorted(factor_keys):
        result = poly_mul(result, factor_poly(key))
    return result


def reconstruct_gram_numerator(union, pattern, denominator, degrees):
    values = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        P, Q, x, y, z, w = map(F, index)
        point = (P, Q, x, y, z, w)
        values[index] = (
            gram_t(CONFIG, union, pattern, P, Q, point[2:])
            * poly_evaluate(denominator, point)
        )
    numerator = tensor_interpolate(values, degrees)
    for test in (
        (F(1, 3), F(2, 5), F(3, 7), F(4, 9), F(5, 11), F(6, 13)),
        (F(7, 4), F(8, 3), F(2, 3), F(5, 8), F(7, 10), F(9, 11)),
    ):
        direct = gram_t(CONFIG, union, pattern, test[0], test[1], test[2:])
        reconstructed = poly_evaluate(numerator, test) / poly_evaluate(denominator, test)
        if direct != reconstructed:
            raise AssertionError(("Gram interpolation mismatch", pattern))
    return numerator


def side_denominator(union):
    shifted_inputs = dict(zip(union[1], shifted_offsets(CONFIG, union)[1]))
    factors = set()
    for offset, _ in CONFIG.retained:
        r, s = shifted_inputs[offset]
        factors.update(((1, 0, r + 2), (0, 1, s + 2), (1, 1, r + s + 3)))
    result = constant(F(1))
    for key in sorted(factors):
        result = poly_mul(result, factor_poly(key))
    return result


def reconstruct_side_numerators(union, denominator, degrees):
    tables = [[{} for _ in range(3)] for _ in CONFIG.retained]
    for index in product(*(range(degree + 1) for degree in degrees)):
        P, Q, x, y, z, w = map(F, index)
        point = (P, Q, x, y, z, w)
        distributions = retained_side_distributions(CONFIG, union, P, Q, point[2:])
        denominator_value = poly_evaluate(denominator, point)
        for side_index, distribution in enumerate(distributions):
            for component, probability in enumerate(distribution):
                tables[side_index][component][index] = probability * denominator_value
    numerators = tuple(
        tuple(tensor_interpolate(table, degrees) for table in group)
        for group in tables
    )
    test = (F(4, 3), F(5, 2), F(2, 7), F(3, 8), F(5, 9), F(7, 11))
    direct = retained_side_distributions(CONFIG, union, test[0], test[1], test[2:])
    denominator_value = poly_evaluate(denominator, test)
    reconstructed = tuple(
        tuple(poly_evaluate(numerator, test) / denominator_value for numerator in group)
        for group in numerators
    )
    if direct != reconstructed:
        raise AssertionError("side interpolation mismatch")
    return numerators


def retained_side_entropy_upper(
    side_groups, denominator, bounds, branch_sets, q_constants
):
    candidates = []
    for group, branches, q_constant in zip(side_groups, branch_sets, q_constants):
        if set(branches) == {"h", "m"}:
            low, high = rational_range(group[0], denominator, bounds)
            candidates.append(binary_interval_entropy_upper(low, high))
            continue
        if set(branches) == {"h", "c"}:
            low, high = rational_range(group[0], denominator, bounds)
            binary_part = binary_interval_entropy_upper(low, high)
            tail = add_dense_controls(group[1], group[2], denominator)
            _, tail_high = rational_range(tail, denominator, bounds)
            conditional = compact_q_tail_parameter_upper(bounds[1][0], q_constant)
            candidates.append(
                binary_part
                + tail_high * entropy_bounds((conditional, 1 - conditional))[1]
            )
            continue
        intervals = [rational_range(value, denominator, bounds) for value in group]
        candidates.append(min(
            sum(component_entropy_upper(low, high) for low, high in intervals),
            log_bounds(F(3))[1],
        ))
    return min(candidates)


@dataclass(frozen=True)
class Box:
    gram_numerators: tuple[CommonDenControls, ...]
    gram_denominator: CommonDenControls
    side_groups: tuple[tuple[CommonDenControls, CommonDenControls, CommonDenControls], ...]
    side_denominator: CommonDenControls
    bounds: tuple[tuple[F, F], ...]
    depths: tuple[int, ...]


def main():
    union = build_union(CONFIG.cluster)
    eliminated, patterns = endpoint_patterns(union[1], union[2], dict(CONFIG.retained))
    if len(patterns) != CONFIG.expected_patterns:
        raise AssertionError(len(patterns))

    gram_den = gram_denominator(union)
    base_degrees = polynomial_degrees(gram_den)
    gram_degrees = (base_degrees[0], base_degrees[1], 2, 2, 2, 2)
    gram_nums = tuple(
        reconstruct_gram_numerator(union, pattern, gram_den, gram_degrees)
        for pattern in patterns
    )
    print(
        f"endpoint Gram branches reconstructed: {len(gram_nums)}; degrees={gram_degrees}",
        flush=True,
    )

    side_den = side_denominator(union)
    side_base_degrees = polynomial_degrees(side_den)
    side_degrees = (side_base_degrees[0], side_base_degrees[1], 1, 1, 1, 1)
    side_nums = reconstruct_side_numerators(union, side_den, side_degrees)
    print(
        f"retained side distributions reconstructed: {len(side_nums)}; degrees={side_degrees}",
        flush=True,
    )

    retained_offsets = dict(CONFIG.retained)
    shifted_inputs = dict(zip(union[1], shifted_offsets(CONFIG, union)[1]))
    branch_sets = tuple(
        tuple(branch for _, branch in incidence)
        for offset, incidence in zip(union[1], union[2])
        if offset in retained_offsets
    )
    q_constants = tuple(
        shifted_inputs[offset][1] for offset in union[1] if offset in retained_offsets
    )

    compact_gram_nums = tuple(
        common_den_controls(bernstein_coefficients(
            compactify(value, gram_degrees[0], gram_degrees[1]), gram_degrees
        ))
        for value in gram_nums
    )
    compact_gram_den = common_den_controls(bernstein_coefficients(
        compactify(gram_den, gram_degrees[0], gram_degrees[1]), gram_degrees
    ))
    compact_side_groups = tuple(
        tuple(
            common_den_controls(bernstein_coefficients(
                compactify(value, side_degrees[0], side_degrees[1]), side_degrees
            ))
            for value in group
        )
        for group in side_nums
    )
    compact_side_den = common_den_controls(bernstein_coefficients(
        compactify(side_den, side_degrees[0], side_degrees[1]), side_degrees
    ))

    stack = [Box(
        compact_gram_nums, compact_gram_den, compact_side_groups, compact_side_den,
        tuple((F(0), F(1)) for _ in range(NVAR)), (0,) * NVAR,
    )]
    certified = 0
    processed = 0
    smallest_margin = None
    smallest_box = None
    while stack:
        box = stack.pop()
        processed += 1
        if processed % 1000 == 0:
            print(
                f"{CONFIG.name}: processed={processed}, certified={certified}, "
                f"pending={len(stack)}",
                flush=True,
            )
        t_upper = max(
            rational_range(value, box.gram_denominator, box.bounds)[1]
            for value in box.gram_numerators
        )
        margin = None
        if F(0) <= t_upper < F(1):
            bell_lower = entropy_bounds(isotropic_probabilities(t_upper))[0]
            side_upper = retained_side_entropy_upper(
                box.side_groups, box.side_denominator, box.bounds,
                branch_sets, q_constants,
            )
            margin = bell_lower - 2 * side_upper
        if margin is not None and margin > 0:
            certified += 1
            if smallest_margin is None or margin < smallest_margin:
                smallest_margin, smallest_box = margin, box.bounds
            continue
        available = [
            axis for axis in range(NVAR) if box.depths[axis] < MAX_DEPTH_PER_AXIS
        ]
        if not available:
            raise AssertionError((
                "uncertified box", box.bounds, float(t_upper),
                None if margin is None else float(margin),
            ))
        axis = min(available, key=lambda candidate: (box.depths[candidate], candidate))
        gram_num_splits = [
            split_controls(value, gram_degrees, axis) for value in box.gram_numerators
        ]
        gram_den_splits = split_controls(box.gram_denominator, gram_degrees, axis)
        side_group_splits = [
            [split_controls(value, side_degrees, axis) for value in group]
            for group in box.side_groups
        ]
        side_den_splits = split_controls(box.side_denominator, side_degrees, axis)
        low, high = box.bounds[axis]
        midpoint = (low + high) / 2
        depths = list(box.depths)
        depths[axis] += 1
        for side in (0, 1):
            bounds = list(box.bounds)
            bounds[axis] = (low, midpoint) if side == 0 else (midpoint, high)
            stack.append(Box(
                tuple(pair[side] for pair in gram_num_splits), gram_den_splits[side],
                tuple(tuple(pair[side] for pair in group) for group in side_group_splits),
                side_den_splits[side], tuple(bounds), tuple(depths),
            ))

    print(f"adaptive compact boxes certified: {certified}")
    print(
        "smallest certified natural-log margin > "
        f"{float(smallest_margin):.12e} at {smallest_box}"
    )
    print("input-centered triangular SU(3) face cluster is Bell-no-go")


if __name__ == "__main__":
    main()
