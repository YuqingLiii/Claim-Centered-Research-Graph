#!/usr/bin/env python3
"""Exact certificate for the conjugate-edge orientation of two SU(3) faces."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product

from certify_su3_adjacent_elementary_faces import (
    Poly,
    bernstein_coefficients,
    compactify,
    constant,
    lagrange_basis,
    linear,
    poly_add,
    poly_evaluate,
    poly_mul,
    poly_power,
    polynomial_degrees,
    product_value,
    scaled,
    split_controls,
)
from certify_su3_all_elementary_cycles import (
    LN2_UPPER,
    cross_numerator,
    dimension,
    entropy_bounds,
    environment_barycenter,
    isotropic_probabilities,
)


F = Fraction
NVAR = 4
MAX_DEPTH_PER_AXIS = 6
PATTERNS = tuple(product(range(3), (0, 1), (0, 1)))
ENVIRONMENT_OFFSETS = ((0, 0), (1, -2), (2, -1), (3, -3), (4, -2))
INPUT_OFFSETS = ((0, -1), (1, 0), (2, -2), (3, -1), (4, -3))
INCIDENCES = (
    ((0, "c"), (1, "m")),
    ((0, "h"), (2, "m")),
    ((1, "h"), (2, "c"), (3, "m")),
    ((2, "h"), (4, "m")),
    ((3, "h"), (4, "c")),
)


def label(p: F, q: F, offset: tuple[int, int]) -> tuple[F, F]:
    return p + offset[0], q + offset[1]


def mixture_t(input_label, weights) -> F:
    center = environment_barycenter(*input_label)
    return (sum(weights.get(key, 0) ** 2 / center[key] for key in center) - 1) / 8


def adjacent_t(p: F, q: F, pattern: tuple[int, int, int], u: F, v: F) -> F:
    environments = [label(p, q, offset) for offset in ENVIRONMENT_OFFSETS]
    inputs = [label(p, q, offset) for offset in INPUT_OFFSETS]
    central = INCIDENCES[2]
    weights = [None] * 5
    weights[2] = {
        branch: int(index == pattern[0])
        for index, (_, branch) in enumerate(central)
    }
    for bit, input_index in zip(pattern[1:], (0, 4)):
        incidences = INCIDENCES[input_index]
        weights[input_index] = {
            incidences[0][1]: int(bit == 0),
            incidences[1][1]: int(bit == 1),
        }
    for input_index, value in ((1, u), (3, v)):
        incidences = INCIDENCES[input_index]
        weights[input_index] = {
            incidences[0][1]: value,
            incidences[1][1]: 1 - value,
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
                    attached[first][1]
                    * attached[second][1]
                    * cross_numerator(
                        *environment_label, attached[first][0], attached[second][0]
                    )
                )
    return numerator / sum(dimension(*input_label) for input_label in inputs)


def common_denominator() -> Poly:
    p = linear(0, F(0))
    q = linear(1, F(3))
    p_plus_q = poly_add(p, q)
    quadratic = poly_add(
        poly_add(scaled(poly_mul(p, q), F(5)), scaled(p, F(-2))),
        poly_add(
            scaled(poly_power(q, 2), F(5)),
            poly_add(scaled(q, F(11)), constant(F(-10))),
        ),
    )
    factors = [
        constant(F(8)),
        q,
        poly_add(p, constant(F(1))),
        poly_add(p, constant(F(2))),
        poly_power(poly_add(p, constant(F(3))), 2),
        poly_add(p, constant(F(4))),
        poly_add(p, constant(F(5))),
        poly_add(q, constant(F(-2))),
        poly_add(q, constant(F(-1))),
        poly_add(q, constant(F(1))),
        poly_add(p_plus_q, constant(F(1))),
        poly_add(p_plus_q, constant(F(2))),
        poly_add(p_plus_q, constant(F(3))),
        poly_add(p_plus_q, constant(F(4))),
        quadratic,
    ]
    result = constant(F(1))
    for factor in factors:
        result = poly_mul(result, factor)
    return result


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


def reconstruct_numerator(pattern, denominator: Poly, degrees) -> Poly:
    values: Poly = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        p_value, q_offset, u_value, v_value = map(F, index)
        value = adjacent_t(p_value, q_offset + 3, pattern, u_value, v_value)
        value *= poly_evaluate(denominator, (p_value, q_offset, u_value, v_value))
        values[index] = value
    numerator = tensor_interpolate(values, degrees)
    for test in (
        (F(0), F(0), F(1, 3), F(2, 5)),
        (F(3, 2), F(7, 3), F(4, 5), F(1, 4)),
        (F(5), F(2), F(7, 5), F(5, 3)),
    ):
        direct = adjacent_t(test[0], test[1] + 3, pattern, test[2], test[3])
        reconstructed = poly_evaluate(numerator, test) / poly_evaluate(denominator, test)
        if direct != reconstructed:
            raise AssertionError(("interpolation mismatch", pattern, direct, reconstructed))
    return numerator


def binary_probability(a: F, weight: F, shift: int) -> F:
    return weight + (1 - weight) * (1 - a) / (shift - (shift - 1) * a)


def binary_entropy_upper(a_low, a_high, weight_low, weight_high, shift) -> F:
    probability_low = binary_probability(a_high, weight_low, shift)
    probability_high = binary_probability(a_low, weight_high, shift)
    if probability_low <= F(1, 2) <= probability_high:
        return LN2_UPPER
    probability = probability_high if probability_high < F(1, 2) else probability_low
    return entropy_bounds([probability, 1 - probability])[1]


@dataclass(frozen=True)
class Box:
    numerators: tuple[Poly, ...]
    denominator: Poly
    bounds: tuple[tuple[F, F], ...]
    depths: tuple[int, ...]


def rational_upper(numerator: Poly, denominator: Poly, bounds) -> F:
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
    return max(ratios)


def main() -> None:
    denominator = common_denominator()
    base_degrees = polynomial_degrees(denominator)
    degrees = (base_degrees[0], base_degrees[1], 2, 2)
    numerators = tuple(
        reconstruct_numerator(pattern, denominator, degrees) for pattern in PATTERNS
    )
    print(f"endpoint Gram branches reconstructed: {len(numerators)}", flush=True)
    compact_denominator = bernstein_coefficients(
        compactify(denominator, degrees[0], degrees[1]), degrees
    )
    compact_numerators = tuple(
        bernstein_coefficients(compactify(numerator, degrees[0], degrees[1]), degrees)
        for numerator in numerators
    )
    stack = [
        Box(
            compact_numerators,
            compact_denominator,
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
            rational_upper(numerator, box.denominator, box.bounds)
            for numerator in box.numerators
        )
        margin = None
        if F(0) <= t_upper < F(1):
            bell_lower = entropy_bounds(isotropic_probabilities(t_upper))[0]
            side_upper = min(
                binary_entropy_upper(
                    box.bounds[0][0], box.bounds[0][1],
                    box.bounds[2][0], box.bounds[2][1], 3,
                ),
                binary_entropy_upper(
                    box.bounds[0][0], box.bounds[0][1],
                    box.bounds[3][0], box.bounds[3][1], 5,
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
        numerator_splits = [split_controls(value, degrees, axis) for value in box.numerators]
        denominator_left, denominator_right = split_controls(box.denominator, degrees, axis)
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
                tuple(pair[1] for pair in numerator_splits), denominator_right,
                tuple(right_bounds), tuple(depths),
            )
        )
        stack.append(
            Box(
                tuple(pair[0] for pair in numerator_splits), denominator_left,
                tuple(left_bounds), tuple(depths),
            )
        )

    print(f"adaptive compact boxes certified: {certified}")
    print(
        "smallest certified natural-log margin > "
        f"{float(smallest_margin):.12e} at {smallest_box}"
    )
    print("conjugate-edge adjacent SU(3) face pair is Bell-no-go")


if __name__ == "__main__":
    main()
