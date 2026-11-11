#!/usr/bin/env python3
"""Exact simplex-aware certificate for highest-edge adjacent SU(3) faces."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb

from certify_su3_adjacent_elementary_faces import component_entropy_upper
from certify_su3_all_elementary_cycles import (
    LN2_UPPER,
    cross_numerator,
    dimension,
    entropy_bounds,
    environment_barycenter,
    isotropic_probabilities,
    log_bounds,
)


F = Fraction
NVAR = 5
MAX_DEPTH_PER_AXIS = 6
Poly = dict[tuple[int, ...], F]
PATTERNS = tuple(product((0, 1), repeat=3))
ENVIRONMENT_OFFSETS = ((0, 0), (1, -2), (2, -4), (2, -1), (3, -3))
INPUT_OFFSETS = ((0, -1), (1, -3), (1, 0), (2, -2), (3, -4))
INCIDENCES = (
    ((0, "c"), (1, "m")),
    ((1, "c"), (2, "m")),
    ((0, "h"), (3, "m")),
    ((1, "h"), (3, "c"), (4, "m")),
    ((2, "h"), (4, "c")),
)


def product_value(values) -> F:
    result = F(1)
    for value in values:
        result *= value
    return result


def constant(value: F) -> Poly:
    return {(0,) * NVAR: value} if value else {}


def linear(axis: int, constant_value: F, slope: F = F(1)) -> Poly:
    result = constant(constant_value)
    if slope:
        exponent = [0] * NVAR
        exponent[axis] = 1
        result[tuple(exponent)] = slope
    return result


def poly_add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, F(0)) + coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def poly_mul(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for first, a in left.items():
        for second, b in right.items():
            monomial = tuple(first[index] + second[index] for index in range(NVAR))
            result[monomial] = result.get(monomial, F(0)) + a * b
    return {monomial: value for monomial, value in result.items() if value}


def scaled(poly: Poly, scalar: F) -> Poly:
    return {monomial: scalar * coefficient for monomial, coefficient in poly.items()}


def poly_power(poly: Poly, exponent: int) -> Poly:
    result = constant(F(1))
    for _ in range(exponent):
        result = poly_mul(result, poly)
    return result


def poly_evaluate(poly: Poly, variables: tuple[F, ...]) -> F:
    return sum(
        coefficient
        * product_value(
            variables[index] ** monomial[index] for index in range(NVAR)
        )
        for monomial, coefficient in poly.items()
    )


def polynomial_degrees(poly: Poly) -> tuple[int, ...]:
    return tuple(max(monomial[axis] for monomial in poly) for axis in range(NVAR))


def lagrange_basis(degree: int, index: int) -> list[F]:
    result = [F(1)]
    denominator = F(1)
    for node in range(degree + 1):
        if node == index:
            continue
        updated = [F(0)] * (len(result) + 1)
        for power, coefficient in enumerate(result):
            updated[power] -= node * coefficient
            updated[power + 1] += coefficient
        result = updated
        denominator *= index - node
    return [coefficient / denominator for coefficient in result]


def tensor_interpolate(values: Poly, degrees: tuple[int, ...]) -> Poly:
    data = dict(values)
    for axis in range(NVAR):
        bases = [lagrange_basis(degrees[axis], node) for node in range(degrees[axis] + 1)]
        other_axes = [candidate for candidate in range(NVAR) if candidate != axis]
        updated: Poly = {}
        for fixed in product(*(range(degrees[candidate] + 1) for candidate in other_axes)):
            line = []
            for node in range(degrees[axis] + 1):
                index = [0] * NVAR
                index[axis] = node
                for candidate, value in zip(other_axes, fixed):
                    index[candidate] = value
                line.append(data[tuple(index)])
            for power in range(degrees[axis] + 1):
                index = [0] * NVAR
                index[axis] = power
                for candidate, value in zip(other_axes, fixed):
                    index[candidate] = value
                updated[tuple(index)] = sum(
                    line[node] * bases[node][power]
                    for node in range(degrees[axis] + 1)
                )
        data = updated
    return {monomial: value for monomial, value in data.items() if value}


def compactify(poly: Poly, p_degree: int, q_degree: int) -> Poly:
    result: Poly = {}
    for monomial, coefficient in poly.items():
        p_power, q_power = monomial[:2]
        for p_tail in range(p_degree - p_power + 1):
            p_coefficient = F(comb(p_degree - p_power, p_tail)) * (-1) ** p_tail
            for q_tail in range(q_degree - q_power + 1):
                q_coefficient = F(comb(q_degree - q_power, q_tail)) * (-1) ** q_tail
                target = (
                    p_power + p_tail,
                    q_power + q_tail,
                    monomial[2], monomial[3], monomial[4],
                )
                result[target] = result.get(target, F(0)) + (
                    coefficient * p_coefficient * q_coefficient
                )
    return {monomial: value for monomial, value in result.items() if value}


def bernstein_coefficients(poly: Poly, degrees: tuple[int, ...]) -> Poly:
    result: Poly = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        value = F(0)
        for monomial, coefficient in poly.items():
            if all(monomial[axis] <= index[axis] for axis in range(NVAR)):
                value += coefficient * product_value(
                    F(comb(index[axis], monomial[axis]), comb(degrees[axis], monomial[axis]))
                    for axis in range(NVAR)
                )
        result[index] = value
    return result


def split_controls(controls: Poly, degrees: tuple[int, ...], axis: int) -> tuple[Poly, Poly]:
    left: Poly = {}
    right: Poly = {}
    other_axes = [candidate for candidate in range(NVAR) if candidate != axis]
    for fixed in product(*(range(degrees[candidate] + 1) for candidate in other_axes)):
        line = []
        for moving in range(degrees[axis] + 1):
            index = [0] * NVAR
            index[axis] = moving
            for candidate, value in zip(other_axes, fixed):
                index[candidate] = value
            line.append(controls[tuple(index)])
        levels = [line]
        while len(levels[-1]) > 1:
            previous = levels[-1]
            levels.append([(previous[i] + previous[i + 1]) / 2 for i in range(len(previous) - 1)])
        for moving in range(degrees[axis] + 1):
            left_index = [0] * NVAR
            right_index = [0] * NVAR
            left_index[axis] = moving
            right_index[axis] = moving
            for candidate, value in zip(other_axes, fixed):
                left_index[candidate] = value
                right_index[candidate] = value
            left[tuple(left_index)] = levels[moving][0]
            right[tuple(right_index)] = levels[degrees[axis] - moving][moving]
    return left, right


def label(p: F, q: F, offset: tuple[int, int]) -> tuple[F, F]:
    return p + offset[0], q + offset[1]


def mixture_t(input_label, weights) -> F:
    center = environment_barycenter(*input_label)
    return (sum(weights.get(key, 0) ** 2 / center[key] for key in center) - 1) / 8


def shared_weights(s: F, t: F) -> dict[str, F]:
    return {"h": s, "c": (1 - s) * t, "m": (1 - s) * (1 - t)}


def adjacent_t(p: F, q: F, pattern, s: F, t: F, w: F) -> F:
    environments = [label(p, q, offset) for offset in ENVIRONMENT_OFFSETS]
    inputs = [label(p, q, offset) for offset in INPUT_OFFSETS]
    weights = [None] * 5
    weights[3] = shared_weights(s, t)
    target = INCIDENCES[2]
    weights[2] = {target[0][1]: w, target[1][1]: 1 - w}
    for bit, input_index in zip(pattern, (0, 1, 4)):
        incidences = INCIDENCES[input_index]
        weights[input_index] = {
            incidences[0][1]: int(bit == 0),
            incidences[1][1]: int(bit == 1),
        }
    numerator = sum(
        dimension(*input_label) * mixture_t(input_label, block_weights)
        for input_label, block_weights in zip(inputs, weights)
    )
    for environment_index, environment_label in enumerate(environments):
        attached = [
            (branch, weights[input_index][branch])
            for input_index, incidences in enumerate(INCIDENCES)
            for candidate_index, branch in incidences
            if candidate_index == environment_index
        ]
        for first in range(len(attached)):
            for second in range(first + 1, len(attached)):
                numerator += (
                    attached[first][1] * attached[second][1]
                    * cross_numerator(
                        *environment_label, attached[first][0], attached[second][0]
                    )
                )
    return numerator / sum(dimension(*input_label) for input_label in inputs)


def gram_denominator() -> Poly:
    p = linear(0, F(0))
    q = linear(1, F(4))
    p_plus_q = poly_add(p, q)
    quadratic = poly_add(
        scaled(poly_power(p, 2), F(5)),
        poly_add(
            scaled(poly_mul(p, q), F(5)),
            poly_add(scaled(p, F(19)), poly_add(scaled(q, F(12)), constant(F(12)))),
        ),
    )
    factors = [
        constant(F(8)), q,
        poly_add(p, constant(F(1))), poly_add(p, constant(F(2))),
        poly_add(p, constant(F(3))), poly_add(p, constant(F(4))),
        p_plus_q,
        poly_add(q, constant(F(-3))), poly_add(q, constant(F(-2))),
        poly_power(poly_add(q, constant(F(-1))), 2), poly_add(q, constant(F(1))),
        poly_add(p_plus_q, constant(F(1))),
        poly_add(p_plus_q, constant(F(2))),
        poly_add(p_plus_q, constant(F(3))), quadratic,
    ]
    result = constant(F(1))
    for factor in factors:
        result = poly_mul(result, factor)
    return result


def reconstruct_gram_numerator(pattern, denominator, degrees) -> Poly:
    values: Poly = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        p_value, q_offset, s_value, t_value, w_value = map(F, index)
        value = adjacent_t(p_value, q_offset + 4, pattern, s_value, t_value, w_value)
        value *= poly_evaluate(denominator, (p_value, q_offset, s_value, t_value, w_value))
        values[index] = value
    numerator = tensor_interpolate(values, degrees)
    for test in (
        (F(0), F(0), F(1, 3), F(2, 5), F(3, 7)),
        (F(3, 2), F(7, 3), F(4, 5), F(1, 4), F(2, 3)),
        (F(5), F(2), F(7, 5), F(5, 3), F(6, 5)),
    ):
        direct = adjacent_t(test[0], test[1] + 4, pattern, test[2], test[3], test[4])
        reconstructed = poly_evaluate(numerator, test) / poly_evaluate(denominator, test)
        if direct != reconstructed:
            raise AssertionError(("Gram interpolation mismatch", pattern, direct, reconstructed))
    return numerator


def side_denominator() -> Poly:
    p = linear(0, F(0))
    q = linear(1, F(4))
    return poly_mul(
        poly_mul(poly_add(p, constant(F(4))), q),
        poly_add(poly_add(p, q), constant(F(3))),
    )


def shared_distribution(p: F, q: F, s: F, t: F) -> tuple[F, F, F]:
    r, representation_s = p + 2, q - 2
    rows = {
        "h": (F(1), F(0), F(0)),
        "m": (F(1, 1) / (r + 2), (r + 1) / (r + 2), F(0)),
        "c": (
            F(1, 1) / (r + representation_s + 3),
            (r + representation_s + 2)
            / ((representation_s + 2) * (r + representation_s + 3)),
            (representation_s + 1) * (r + representation_s + 2)
            / ((representation_s + 2) * (r + representation_s + 3)),
        ),
    }
    weights = shared_weights(s, t)
    return tuple(
        sum(weights[key] * rows[key][component] for key in weights)
        for component in range(3)
    )


def reconstruct_side_numerators(denominator, degrees) -> tuple[Poly, ...]:
    value_tables = [dict() for _ in range(3)]
    for index in product(*(range(degree + 1) for degree in degrees)):
        p_value, q_offset, s_value, t_value, w_value = map(F, index)
        probabilities = shared_distribution(p_value, q_offset + 4, s_value, t_value)
        denominator_value = poly_evaluate(
            denominator, (p_value, q_offset, s_value, t_value, w_value)
        )
        for component in range(3):
            value_tables[component][index] = probabilities[component] * denominator_value
    numerators = tuple(tensor_interpolate(values, degrees) for values in value_tables)
    test = (F(3, 2), F(7, 3), F(4, 5), F(1, 4), F(0))
    direct = shared_distribution(test[0], test[1] + 4, test[2], test[3])
    denominator_value = poly_evaluate(denominator, test)
    reconstructed = tuple(poly_evaluate(numerator, test) / denominator_value for numerator in numerators)
    if direct != reconstructed:
        raise AssertionError(("side interpolation mismatch", direct, reconstructed))
    return numerators


def binary_probability(a: F, w: F) -> F:
    return w + (1 - w) * (1 - a) / (3 - 2 * a)


def binary_entropy_upper(a_low, a_high, w_low, w_high) -> F:
    probability_low = binary_probability(a_high, w_low)
    probability_high = binary_probability(a_low, w_high)
    if probability_low <= F(1, 2) <= probability_high:
        return LN2_UPPER
    probability = probability_high if probability_high < F(1, 2) else probability_low
    return entropy_bounds([probability, 1 - probability])[1]


def rational_range(numerator: Poly, denominator: Poly, bounds) -> tuple[F, F]:
    ratios = []
    for index, denominator_control in denominator.items():
        numerator_control = numerator[index]
        if denominator_control < 0:
            raise AssertionError(("negative denominator control", bounds, index))
        if denominator_control:
            ratios.append(numerator_control / denominator_control)
        elif numerator_control:
            raise AssertionError(("unmatched projective zero", bounds, index))
    if not ratios:
        raise AssertionError(("identically zero denominator box", bounds))
    return max(F(0), min(ratios)), min(F(1), max(ratios))


def shared_entropy_upper(side_numerators, side_denominator, bounds) -> F:
    probability_bounds = [
        rational_range(numerator, side_denominator, bounds)
        for numerator in side_numerators
    ]
    upper = sum(component_entropy_upper(low, high) for low, high in probability_bounds)
    return min(upper, log_bounds(F(3))[1])


@dataclass(frozen=True)
class Box:
    gram_numerators: tuple[Poly, ...]
    gram_denominator: Poly
    side_numerators: tuple[Poly, ...]
    side_denominator: Poly
    bounds: tuple[tuple[F, F], ...]
    depths: tuple[int, ...]


def main() -> None:
    gram_den = gram_denominator()
    gram_base_degrees = polynomial_degrees(gram_den)
    gram_degrees = (gram_base_degrees[0], gram_base_degrees[1], 2, 2, 2)
    gram_nums = tuple(
        reconstruct_gram_numerator(pattern, gram_den, gram_degrees)
        for pattern in PATTERNS
    )
    print(f"endpoint Gram branches reconstructed: {len(gram_nums)}", flush=True)

    side_den = side_denominator()
    side_degrees = (2, 2, 1, 1, 0)
    side_nums = reconstruct_side_numerators(side_den, side_degrees)
    print("shared-side probability functions reconstructed: 3", flush=True)

    stack = [
        Box(
            tuple(
                bernstein_coefficients(
                    compactify(numerator, gram_degrees[0], gram_degrees[1]), gram_degrees
                )
                for numerator in gram_nums
            ),
            bernstein_coefficients(
                compactify(gram_den, gram_degrees[0], gram_degrees[1]), gram_degrees
            ),
            tuple(
                bernstein_coefficients(
                    compactify(numerator, side_degrees[0], side_degrees[1]), side_degrees
                )
                for numerator in side_nums
            ),
            bernstein_coefficients(
                compactify(side_den, side_degrees[0], side_degrees[1]), side_degrees
            ),
            tuple((F(0), F(1)) for _ in range(NVAR)),
            (0,) * NVAR,
        )
    ]
    certified = 0
    smallest_margin = None
    smallest_box = None
    while stack:
        box = stack.pop()
        t_upper = max(
            rational_range(numerator, box.gram_denominator, box.bounds)[1]
            for numerator in box.gram_numerators
        )
        margin = None
        if F(0) <= t_upper < F(1):
            bell_lower = entropy_bounds(isotropic_probabilities(t_upper))[0]
            side_upper = min(
                shared_entropy_upper(
                    box.side_numerators, box.side_denominator, box.bounds
                ),
                binary_entropy_upper(
                    box.bounds[0][0], box.bounds[0][1],
                    box.bounds[4][0], box.bounds[4][1],
                ),
            )
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
            raise AssertionError(("uncertified box", box.bounds, t_upper, margin))
        axis = min(available, key=lambda candidate: (box.depths[candidate], candidate))
        gram_num_splits = [
            split_controls(value, gram_degrees, axis) for value in box.gram_numerators
        ]
        gram_den_left, gram_den_right = split_controls(
            box.gram_denominator, gram_degrees, axis
        )
        side_num_splits = [
            split_controls(value, side_degrees, axis) for value in box.side_numerators
        ]
        side_den_left, side_den_right = split_controls(
            box.side_denominator, side_degrees, axis
        )
        low, high = box.bounds[axis]
        midpoint = (low + high) / 2
        left_bounds = list(box.bounds)
        right_bounds = list(box.bounds)
        left_bounds[axis] = (low, midpoint)
        right_bounds[axis] = (midpoint, high)
        depths = list(box.depths)
        depths[axis] += 1
        stack.append(
            Box(
                tuple(pair[1] for pair in gram_num_splits), gram_den_right,
                tuple(pair[1] for pair in side_num_splits), side_den_right,
                tuple(right_bounds), tuple(depths),
            )
        )
        stack.append(
            Box(
                tuple(pair[0] for pair in gram_num_splits), gram_den_left,
                tuple(pair[0] for pair in side_num_splits), side_den_left,
                tuple(left_bounds), tuple(depths),
            )
        )

    print(f"adaptive compact boxes certified: {certified}")
    print(
        "smallest certified natural-log margin > "
        f"{float(smallest_margin):.12e} at {smallest_box}"
    )
    print("highest-edge adjacent SU(3) face pair is Bell-no-go")


if __name__ == "__main__":
    main()
