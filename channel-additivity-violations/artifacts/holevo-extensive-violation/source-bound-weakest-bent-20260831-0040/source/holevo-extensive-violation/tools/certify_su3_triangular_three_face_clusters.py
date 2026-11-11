#!/usr/bin/env python3
"""Exact compact certificates for the two triangular three-face SU(3) clusters."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

from certify_su3_adjacent_elementary_faces import component_entropy_upper
from certify_su3_all_elementary_cycles import (
    cross_numerator,
    dimension,
    entropy_bounds,
    environment_barycenter,
    isotropic_probabilities,
    log_bounds,
)
from certify_su3_highest_edge_adjacent_faces import (
    NVAR,
    Poly,
    bernstein_coefficients,
    compactify,
    constant,
    linear,
    poly_add,
    poly_evaluate,
    poly_mul,
    polynomial_degrees,
    scaled,
    tensor_interpolate,
)
from su3_common_den_controls import (
    CommonDenControls,
    add_common_controls,
    common_den_controls,
    rational_range_common as rational_range,
    split_common_controls as split_controls,
)


F = Fraction
MAX_DEPTH_PER_AXIS = 7
ENVIRONMENT_OFFSETS = ((0, 0), (2, -1), (1, -2))
INPUT_OFFSETS = ((1, 0), (2, -2), (0, -1))
FACE_EDGES = (
    (0, 0, "h"), (0, 2, "c"),
    (1, 0, "m"), (1, 1, "c"),
    (2, 1, "h"), (2, 2, "m"),
)


@dataclass(frozen=True)
class Configuration:
    name: str
    cluster: tuple[tuple[int, int], ...]
    retained: tuple[tuple[tuple[int, int], str], ...]
    expected_patterns: int


CONFIGURATIONS = (
    Configuration(
        "environment-centered",
        ((-2, 1), (-1, 2), (0, 0)),
        (((0, 2), "binary"), ((1, 0), "ternary")),
        36,
    ),
)


def add(first, second):
    return first[0] + second[0], first[1] + second[1]


def build_union(cluster):
    environments = sorted(
        {add(base, offset) for base in cluster for offset in ENVIRONMENT_OFFSETS}
    )
    inputs = sorted({add(base, offset) for base in cluster for offset in INPUT_OFFSETS})
    environment_index = {label: index for index, label in enumerate(environments)}
    input_index = {label: index for index, label in enumerate(inputs)}
    edges = sorted(
        {
            (
                input_index[add(base, INPUT_OFFSETS[input_slot])],
                environment_index[add(base, ENVIRONMENT_OFFSETS[environment_slot])],
                branch,
            )
            for base in cluster
            for environment_slot, input_slot, branch in FACE_EDGES
        }
    )
    incidences = [[] for _ in inputs]
    attached = [[] for _ in environments]
    for input_index_value, environment_index_value, branch in edges:
        incidences[input_index_value].append((environment_index_value, branch))
        attached[environment_index_value].append((input_index_value, branch))
    return environments, inputs, incidences, attached


def minimum_base(environments, inputs):
    labels = environments + inputs
    return -min(label[0] for label in labels), -min(label[1] for label in labels)


def endpoint_patterns(inputs, incidences, retained_offsets):
    eliminated = [
        index for index, offset in enumerate(inputs) if offset not in retained_offsets
    ]
    patterns = tuple(product(*(range(len(incidences[index])) for index in eliminated)))
    return eliminated, patterns


def retained_weights(kind, incidence, variables):
    branches = [branch for _, branch in incidence]
    if kind == "binary":
        value = variables[0]
        return {branches[0]: value, branches[1]: 1 - value}
    if kind == "ternary":
        first, second = variables
        return {
            branches[0]: first,
            branches[1]: (1 - first) * second,
            branches[2]: (1 - first) * (1 - second),
        }
    raise AssertionError(kind)


def retained_coordinate_count(config):
    return sum(1 if kind == "binary" else 2 for _, kind in config.retained)


def all_weights(config, inputs, incidences, eliminated, pattern, coordinates):
    retained_map = dict(config.retained)
    axis = 0
    weights = [None] * len(inputs)
    for index, offset in enumerate(inputs):
        if offset not in retained_map:
            continue
        kind = retained_map[offset]
        count = 1 if kind == "binary" else 2
        weights[index] = retained_weights(kind, incidences[index], coordinates[axis:axis + count])
        axis += count
    if axis != retained_coordinate_count(config):
        raise AssertionError((config.name, axis))
    for input_index, chosen in zip(eliminated, pattern):
        branch = incidences[input_index][chosen][1]
        weights[input_index] = {
            candidate_branch: F(candidate_branch == branch)
            for _, candidate_branch in incidences[input_index]
        }
    return weights


def mixture_t(input_label, weights):
    center = environment_barycenter(*input_label)
    return (sum(weights[branch] ** 2 / center[branch] for branch in weights) - 1) / 8


def gram_t(config, union, pattern, P, Q, coordinates):
    environments, inputs, incidences, attached = union
    p_min, q_min = minimum_base(environments, inputs)
    base = P + p_min, Q + q_min
    input_labels = [add(base, offset) for offset in inputs]
    environment_labels = [add(base, offset) for offset in environments]
    eliminated, _ = endpoint_patterns(inputs, incidences, dict(config.retained))
    weights = all_weights(config, inputs, incidences, eliminated, pattern, coordinates)
    numerator = sum(
        dimension(*input_label) * mixture_t(input_label, block_weights)
        for input_label, block_weights in zip(input_labels, weights)
    )
    for environment_label, environment_attached in zip(environment_labels, attached):
        for first_index in range(len(environment_attached)):
            first_input, first_branch = environment_attached[first_index]
            for second_index in range(first_index + 1, len(environment_attached)):
                second_input, second_branch = environment_attached[second_index]
                numerator += (
                    weights[first_input][first_branch]
                    * weights[second_input][second_branch]
                    * cross_numerator(
                        *environment_label, first_branch, second_branch
                    )
                )
    return numerator / sum(dimension(*input_label) for input_label in input_labels)


def dimension_poly(offset):
    r, s = offset
    first = linear(0, F(r + 1))
    second = linear(1, F(s + 1))
    third = poly_add(poly_add(linear(0, F(0)), linear(1, F(0))), constant(F(r + s + 2)))
    return scaled(poly_mul(poly_mul(first, second), third), F(1, 2))


def shifted_offsets(config, union):
    environments, inputs, _, _ = union
    p_min, q_min = minimum_base(environments, inputs)
    shift = (p_min, q_min)
    return (
        [add(shift, offset) for offset in environments],
        [add(shift, offset) for offset in inputs],
    )


def gram_denominator(config, union):
    environment_offsets, input_offsets = shifted_offsets(config, union)
    total_input = constant(F(0))
    for offset in input_offsets:
        total_input = poly_add(total_input, dimension_poly(offset))
    factor_keys = set()
    for r, s in environment_offsets:
        factor_keys.add((1, 0, r + 1))
        factor_keys.add((0, 1, s + 1))
        factor_keys.add((1, 1, r + s + 2))
    result = scaled(total_input, F(8))
    for p_coefficient, q_coefficient, constant_value in sorted(factor_keys):
        factor = constant(F(constant_value))
        if p_coefficient:
            factor = poly_add(factor, linear(0, F(0)))
        if q_coefficient:
            factor = poly_add(factor, linear(1, F(0)))
        result = poly_mul(result, factor)
    return result


def reconstruct_gram_numerator(config, union, pattern, denominator, degrees):
    values = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        P, Q, x, y, z = map(F, index)
        value = gram_t(config, union, pattern, P, Q, (x, y, z))
        value *= poly_evaluate(denominator, (P, Q, x, y, z))
        values[index] = value
    numerator = tensor_interpolate(values, degrees)
    tests = (
        (F(1, 3), F(2, 5), F(3, 7), F(4, 9), F(5, 11)),
        (F(7, 4), F(8, 3), F(2, 3), F(5, 8), F(7, 10)),
    )
    for test in tests:
        direct = gram_t(config, union, pattern, test[0], test[1], test[2:])
        reconstructed = poly_evaluate(numerator, test) / poly_evaluate(denominator, test)
        if direct != reconstructed:
            raise AssertionError(("Gram interpolation mismatch", config.name, pattern))
    return numerator


def side_rows(r, s):
    return {
        "h": (F(1), F(0), F(0)),
        "m": (F(1, 1) / (r + 2), (r + 1) / (r + 2), F(0)),
        "c": (
            F(1, 1) / (r + s + 3),
            (r + s + 2) / ((s + 2) * (r + s + 3)),
            (s + 1) * (r + s + 2) / ((s + 2) * (r + s + 3)),
        ),
    }


def retained_side_distributions(config, union, P, Q, coordinates):
    environments, inputs, incidences, _ = union
    p_min, q_min = minimum_base(environments, inputs)
    base = P + p_min, Q + q_min
    result = []
    axis = 0
    retained_map = dict(config.retained)
    for input_offset, incidence in zip(inputs, incidences):
        if input_offset not in retained_map:
            continue
        kind = retained_map[input_offset]
        count = 1 if kind == "binary" else 2
        weights = retained_weights(kind, incidence, coordinates[axis:axis + count])
        axis += count
        r, s = add(base, input_offset)
        rows = side_rows(r, s)
        result.append(tuple(
            sum(weights[branch] * rows[branch][component] for branch in weights)
            for component in range(3)
        ))
    if axis != retained_coordinate_count(config):
        raise AssertionError((config.name, axis))
    return tuple(result)


def side_denominator(config, union):
    _, input_offsets = shifted_offsets(config, union)
    retained_offsets = dict(config.retained)
    factors = set()
    original_inputs = union[1]
    shifted_by_original = dict(zip(original_inputs, input_offsets))
    for offset in retained_offsets:
        r, s = shifted_by_original[offset]
        factors.add((1, 0, r + 2))
        factors.add((0, 1, s + 2))
        factors.add((1, 1, r + s + 3))
    result = constant(F(1))
    for p_coefficient, q_coefficient, constant_value in sorted(factors):
        factor = constant(F(constant_value))
        if p_coefficient:
            factor = poly_add(factor, linear(0, F(0)))
        if q_coefficient:
            factor = poly_add(factor, linear(1, F(0)))
        result = poly_mul(result, factor)
    return result


def reconstruct_side_numerators(config, union, denominator, degrees):
    retained_count = len(config.retained)
    tables = [[{} for _ in range(3)] for _ in range(retained_count)]
    for index in product(*(range(degree + 1) for degree in degrees)):
        P, Q, x, y, z = map(F, index)
        distributions = retained_side_distributions(config, union, P, Q, (x, y, z))
        denominator_value = poly_evaluate(denominator, (P, Q, x, y, z))
        for side_index, distribution in enumerate(distributions):
            for component, probability in enumerate(distribution):
                tables[side_index][component][index] = probability * denominator_value
    numerators = tuple(
        tuple(tensor_interpolate(table, degrees) for table in side_tables)
        for side_tables in tables
    )
    test = (F(4, 3), F(5, 2), F(2, 7), F(3, 8), F(5, 9))
    direct = retained_side_distributions(config, union, test[0], test[1], test[2:])
    denominator_value = poly_evaluate(denominator, test)
    reconstructed = tuple(
        tuple(poly_evaluate(numerator, test) / denominator_value for numerator in group)
        for group in numerators
    )
    if direct != reconstructed:
        raise AssertionError(("side interpolation mismatch", config.name))
    return numerators


def side_entropy_upper(side_groups, denominator, bounds):
    raise AssertionError("side metadata required")


def binary_interval_entropy_upper(low, high):
    if low <= F(1, 2) <= high:
        return log_bounds(F(2))[1]
    probability = high if high < F(1, 2) else low
    return entropy_bounds((probability, 1 - probability))[1]


def compact_q_tail_parameter_upper(compact_low, q_constant):
    # Q=b/(1-b), input second label is Q+q_constant, and the c-row conditional
    # split is (1/(s+2),(s+1)/(s+2)).  The first probability decreases in b.
    b = compact_low
    return (1 - b) / (F(q_constant + 2) - F(q_constant + 1) * b)


def compact_linear_reciprocal_upper(compact_low, constant_value):
    value = compact_low
    return (1 - value) / (
        F(constant_value) - F(constant_value - 1) * value
    )


def compact_sum_reciprocal_upper(p_low, q_low, constant_value):
    P = p_low / (1 - p_low)
    Q = q_low / (1 - q_low)
    return 1 / (P + Q + constant_value)


def add_dense_controls(first, second, denominator):
    if isinstance(first, CommonDenControls):
        return add_common_controls(first, second)
    return {
        index: first.get(index, F(0)) + second.get(index, F(0))
        for index in denominator
    }


def correlated_side_entropy_upper(
    side_groups, denominator, bounds, branch_sets, q_constants
):
    result = []
    for group, branches, q_constant in zip(side_groups, branch_sets, q_constants):
        if len(branches) == 2 and set(branches) == {"h", "m"}:
            first_low, first_high = rational_range(group[0], denominator, bounds)
            result.append(binary_interval_entropy_upper(first_low, first_high))
            continue
        if len(branches) == 2 and set(branches) == {"h", "c"}:
            first_low, first_high = rational_range(group[0], denominator, bounds)
            binary_part = binary_interval_entropy_upper(first_low, first_high)
            tail_controls = add_dense_controls(group[1], group[2], denominator)
            _, tail_high = rational_range(tail_controls, denominator, bounds)
            conditional = compact_q_tail_parameter_upper(bounds[1][0], q_constant)
            conditional_entropy = entropy_bounds((conditional, 1 - conditional))[1]
            result.append(binary_part + tail_high * conditional_entropy)
            continue
        intervals = [rational_range(numerator, denominator, bounds) for numerator in group]
        result.append(min(
            sum(component_entropy_upper(low, high) for low, high in intervals),
            log_bounds(F(3))[1],
        ))
    return min(result)


def endpoint_side_entropy_upper(
    config, union, eliminated, pattern, bounds
):
    shifted_input_offsets = dict(zip(union[1], shifted_offsets(config, union)[1]))
    candidates = []
    for input_index, chosen in zip(eliminated, pattern):
        branch = union[2][input_index][chosen][1]
        r_constant, s_constant = shifted_input_offsets[union[1][input_index]]
        if branch == "h":
            return F(0)
        if branch == "m":
            probability = compact_linear_reciprocal_upper(
                bounds[0][0], r_constant + 2
            )
            candidates.append(entropy_bounds((probability, 1 - probability))[1])
            continue
        if branch == "c":
            first = compact_sum_reciprocal_upper(
                bounds[0][0], bounds[1][0], r_constant + s_constant + 3
            )
            conditional = compact_q_tail_parameter_upper(
                bounds[1][0], s_constant
            )
            candidates.append(
                entropy_bounds((first, 1 - first))[1]
                + entropy_bounds((conditional, 1 - conditional))[1]
            )
            continue
        raise AssertionError(branch)
    return min(candidates)


@dataclass(frozen=True)
class Box:
    gram_numerators: tuple[CommonDenControls, ...]
    gram_denominator: CommonDenControls
    side_groups: tuple[tuple[CommonDenControls, CommonDenControls, CommonDenControls], ...]
    side_denominator: CommonDenControls
    bounds: tuple[tuple[F, F], ...]
    depths: tuple[int, ...]


def certify(config):
    union = build_union(config.cluster)
    eliminated, patterns = endpoint_patterns(union[1], union[2], dict(config.retained))
    if len(patterns) != config.expected_patterns:
        raise AssertionError((config.name, len(patterns)))

    gram_den = gram_denominator(config, union)
    base_degrees = polynomial_degrees(gram_den)
    gram_degrees = (base_degrees[0], base_degrees[1], 2, 2, 2)
    gram_nums = tuple(
        reconstruct_gram_numerator(config, union, pattern, gram_den, gram_degrees)
        for pattern in patterns
    )
    print(
        f"{config.name}: endpoint Gram branches reconstructed: {len(gram_nums)}; "
        f"degrees={gram_degrees}", flush=True
    )

    side_den = side_denominator(config, union)
    side_base_degrees = polynomial_degrees(side_den)
    side_degrees = (side_base_degrees[0], side_base_degrees[1], 1, 1, 1)
    side_nums = reconstruct_side_numerators(config, union, side_den, side_degrees)
    retained_map = dict(config.retained)
    shifted_input_offsets = dict(zip(union[1], shifted_offsets(config, union)[1]))
    side_branch_sets = tuple(
        tuple(branch for _, branch in incidence)
        for offset, incidence in zip(union[1], union[2])
        if offset in retained_map
    )
    side_q_constants = tuple(
        shifted_input_offsets[offset][1]
        for offset in union[1]
        if offset in retained_map
    )
    print(
        f"{config.name}: retained side distributions reconstructed: {len(side_nums)}; "
        f"degrees={side_degrees}", flush=True
    )

    compact_gram_nums = tuple(
        common_den_controls(bernstein_coefficients(
            compactify(numerator, gram_degrees[0], gram_degrees[1]), gram_degrees
        ))
        for numerator in gram_nums
    )
    compact_gram_den = common_den_controls(bernstein_coefficients(
        compactify(gram_den, gram_degrees[0], gram_degrees[1]), gram_degrees
    ))
    compact_side_groups = tuple(
        tuple(
            common_den_controls(bernstein_coefficients(
                compactify(numerator, side_degrees[0], side_degrees[1]), side_degrees
            ))
            for numerator in group
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
                f"{config.name}: processed={processed}, certified={certified}, "
                f"pending={len(stack)}",
                flush=True,
            )
        side_upper = correlated_side_entropy_upper(
            box.side_groups, box.side_denominator, box.bounds,
            side_branch_sets, side_q_constants,
        )
        t_upper = max(
            rational_range(numerator, box.gram_denominator, box.bounds)[1]
            for numerator in box.gram_numerators
        )
        margin = None
        if F(0) <= t_upper < F(1):
            bell_lower = entropy_bounds(isotropic_probabilities(t_upper))[0]
            margin = bell_lower - 2 * side_upper
        if margin is not None and margin > 0:
            certified += 1
            if smallest_margin is None or margin < smallest_margin:
                smallest_margin = margin
                smallest_box = box.bounds
            continue
        available = [
            axis for axis in range(NVAR) if box.depths[axis] < MAX_DEPTH_PER_AXIS
        ]
        if not available:
            raise AssertionError((
                "uncertified box", config.name, box.bounds,
                float(t_upper), None if margin is None else float(margin),
            ))
        axis = min(available, key=lambda candidate: (box.depths[candidate], candidate))
        gram_num_splits = [
            split_controls(value, gram_degrees, axis) for value in box.gram_numerators
        ]
        gram_den_left, gram_den_right = split_controls(
            box.gram_denominator, gram_degrees, axis
        )
        side_group_splits = [
            [split_controls(value, side_degrees, axis) for value in group]
            for group in box.side_groups
        ]
        side_den_left, side_den_right = split_controls(
            box.side_denominator, side_degrees, axis
        )
        low, high = box.bounds[axis]
        midpoint = (low + high) / 2
        left_bounds, right_bounds = list(box.bounds), list(box.bounds)
        left_bounds[axis], right_bounds[axis] = (low, midpoint), (midpoint, high)
        depths = list(box.depths)
        depths[axis] += 1
        for side, bounds, gram_den_child, side_den_child in (
            (0, tuple(left_bounds), gram_den_left, side_den_left),
            (1, tuple(right_bounds), gram_den_right, side_den_right),
        ):
            stack.append(Box(
                tuple(pair[side] for pair in gram_num_splits), gram_den_child,
                tuple(tuple(pair[side] for pair in group) for group in side_group_splits),
                side_den_child, bounds, tuple(depths),
            ))

    print(f"{config.name}: adaptive compact boxes certified: {certified}")
    print(
        f"{config.name}: smallest certified natural-log margin > "
        f"{float(smallest_margin):.12e} at {smallest_box}"
    )
    print(f"{config.name}: triangular SU(3) face cluster is Bell-no-go")


def main():
    for config in CONFIGURATIONS:
        certify(config)


if __name__ == "__main__":
    main()
