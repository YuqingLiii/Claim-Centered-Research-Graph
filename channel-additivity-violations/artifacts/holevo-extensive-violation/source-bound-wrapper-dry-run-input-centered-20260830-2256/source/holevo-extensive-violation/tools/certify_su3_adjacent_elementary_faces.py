#!/usr/bin/env python3
"""Exact rational certificate for the canonical pair of adjacent SU(3) faces."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb

from certify_su3_all_elementary_cycles import (
    LN2_UPPER,
    entropy_bounds,
    isotropic_probabilities,
    log_bounds,
)
from scan_su3_adjacent_elementary_faces import ENDPOINT_PATTERNS, adjacent_t


F = Fraction
NVAR = 4
MAX_DEPTH_PER_AXIS = 6
Poly = dict[tuple[int, ...], F]


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


def poly_evaluate(poly: Poly, variables: tuple[F, ...]) -> F:
    return sum(
        coefficient
        * product_value(
            variables[index] ** monomial[index] for index in range(NVAR)
        )
        for monomial, coefficient in poly.items()
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


def poly_power(poly: Poly, exponent: int) -> Poly:
    result = constant(F(1))
    for _ in range(exponent):
        result = poly_mul(result, poly)
    return result


def scaled(poly: Poly, scalar: F) -> Poly:
    return {monomial: scalar * coefficient for monomial, coefficient in poly.items()}


def denominator_polynomial(pattern: tuple[str, int, int]) -> Poly:
    p = linear(0, F(0))
    q = linear(1, F(2))
    p_plus_q = poly_add(p, q)

    factors = [
        constant(F(8)),
        poly_add(p, constant(F(2))),
        poly_add(p, constant(F(3))),
        poly_add(p, constant(F(4))),
        poly_add(q, constant(F(1))),
        poly_power(poly_add(p_plus_q, constant(F(3))), 2),
        poly_add(p_plus_q, constant(F(4))),
        poly_add(p_plus_q, constant(F(5))),
        poly_add(
            poly_add(scaled(poly_mul(p, q), F(5)), scaled(p, F(2))),
            poly_add(scaled(q, F(13)), constant(F(10))),
        ),
    ]

    branch, first, second = pattern
    if branch == "h":
        factors.append(poly_add(p, constant(F(1))))
        factors.append(poly_add(p_plus_q, constant(F(1))) if first == 0 else q)
        if second == 1:
            factors.extend(
                [poly_add(q, constant(F(-1))), poly_add(p_plus_q, constant(F(2)))]
            )
    elif branch == "m":
        if first == 0:
            factors.extend([q, poly_add(p_plus_q, constant(F(1)))])
        factors.append(
            poly_add(p_plus_q, constant(F(2)))
            if second == 0
            else poly_add(q, constant(F(-1)))
        )
    elif branch == "c":
        factors.append(poly_add(q, constant(F(2))))
        factors.append(poly_add(p_plus_q, constant(F(1))) if first == 0 else q)
        factors.append(
            poly_add(p_plus_q, constant(F(2)))
            if second == 0
            else poly_add(q, constant(F(-1)))
        )
    else:
        raise ValueError(pattern)

    result = constant(F(1))
    for factor in factors:
        result = poly_mul(result, factor)
    return result


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


def polynomial_degrees(poly: Poly) -> tuple[int, ...]:
    return tuple(max(monomial[axis] for monomial in poly) for axis in range(NVAR))


def reconstruct_numerator(pattern: tuple[str, int, int]) -> tuple[Poly, Poly]:
    denominator = denominator_polynomial(pattern)
    denominator_degrees = polynomial_degrees(denominator)
    degrees = (denominator_degrees[0], denominator_degrees[1], 2, 2)
    bases = [
        [lagrange_basis(degree, index) for index in range(degree + 1)]
        for degree in degrees
    ]
    numerator: Poly = {}
    for grid_index in product(*(range(degree + 1) for degree in degrees)):
        p_value = F(grid_index[0])
        q_offset = F(grid_index[1])
        u_value = F(grid_index[2])
        v_value = F(grid_index[3])
        value = adjacent_t(p_value, q_offset + 2, pattern, u_value, v_value)
        value *= poly_evaluate(denominator, (p_value, q_offset, u_value, v_value))
        if not value:
            continue
        for monomial in product(*(range(degree + 1) for degree in degrees)):
            coefficient = value * product_value(
                bases[axis][grid_index[axis]][monomial[axis]]
                for axis in range(NVAR)
            )
            if coefficient:
                numerator[monomial] = numerator.get(monomial, F(0)) + coefficient
    numerator = {monomial: value for monomial, value in numerator.items() if value}

    tests = (
        (F(0), F(0), F(1, 3), F(2, 5)),
        (F(3, 2), F(7, 3), F(4, 5), F(1, 4)),
        (F(5), F(2), F(7, 5), F(5, 3)),
    )
    for p_value, q_offset, u_value, v_value in tests:
        direct = adjacent_t(p_value, q_offset + 2, pattern, u_value, v_value)
        reconstructed = poly_evaluate(
            numerator, (p_value, q_offset, u_value, v_value)
        ) / poly_evaluate(denominator, (p_value, q_offset, u_value, v_value))
        if direct != reconstructed:
            raise AssertionError(
                ("interpolation mismatch", pattern, direct, reconstructed)
            )
    return numerator, denominator


def compactify(poly: Poly, p_degree: int, q_degree: int) -> Poly:
    result: Poly = {}
    for monomial, coefficient in poly.items():
        p_power, q_power, u_power, v_power = monomial
        for p_tail in range(p_degree - p_power + 1):
            p_coefficient = F(comb(p_degree - p_power, p_tail)) * (-1) ** p_tail
            for q_tail in range(q_degree - q_power + 1):
                q_coefficient = F(comb(q_degree - q_power, q_tail)) * (-1) ** q_tail
                target = (p_power + p_tail, q_power + q_tail, u_power, v_power)
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


def compact_to_p(value: F):
    return None if value == 1 else value / (1 - value)


def compact_to_q(value: F):
    return None if value == 1 else 2 + value / (1 - value)


def c_row(p, q) -> tuple[F, F, F]:
    if p is None or q is None:
        c1 = F(0)
    else:
        c1 = 1 / (p + q + 5)
    if q is None:
        c2 = F(0)
        c3 = F(1)
    elif p is None:
        c2 = 1 / (q + 1)
        c3 = q / (q + 1)
    else:
        c2 = (p + q + 4) / ((q + 1) * (p + q + 5))
        c3 = q * (p + q + 4) / ((q + 1) * (p + q + 5))
    return c1, c2, c3


def side_u_probability(a: F, u: F) -> F:
    return u + (1 - u) * (1 - a) / (4 - 3 * a)


def side_u_entropy_upper(a_low: F, a_high: F, u_low: F, u_high: F) -> F:
    probability_low = side_u_probability(a_high, u_low)
    probability_high = side_u_probability(a_low, u_high)
    if probability_low <= F(1, 2) <= probability_high:
        return LN2_UPPER
    probability = probability_high if probability_high < F(1, 2) else probability_low
    return entropy_bounds([probability, 1 - probability])[1]


def component_entropy_upper(low: F, high: F) -> F:
    if not high:
        return F(0)
    if high <= F(1, 3):
        return entropy_bounds([high])[1]
    if low >= F(3, 8):
        return entropy_bounds([low])[1]
    return F(3, 8)


def side_v_entropy_upper(bounds: tuple[tuple[F, F], ...]) -> F:
    (a_low, a_high), (b_low, b_high), _, (v_low, v_high) = bounds
    p_low, p_high = compact_to_p(a_low), compact_to_p(a_high)
    q_low, q_high = compact_to_q(b_low), compact_to_q(b_high)
    c_low_low = c_row(p_low, q_low)
    c_high_high = c_row(p_high, q_high)
    c_high_low = c_row(p_high, q_low)
    c_low_high = c_row(p_low, q_high)

    probability_bounds = (
        (
            1 - v_high + v_high * c_high_high[0],
            1 - v_low + v_low * c_low_low[0],
        ),
        (v_low * c_low_high[1], v_high * c_high_low[1]),
        (v_low * c_low_low[2], v_high * c_high_high[2]),
    )
    upper = sum(component_entropy_upper(low, high) for low, high in probability_bounds)
    _, log3_upper = log_bounds(F(3))
    return min(upper, log3_upper)


@dataclass(frozen=True)
class RationalControls:
    numerator: Poly
    denominator: Poly
    degrees: tuple[int, ...]


@dataclass(frozen=True)
class Box:
    branches: tuple[RationalControls, ...]
    bounds: tuple[tuple[F, F], ...]
    depths: tuple[int, ...]


def branch_upper(branch: RationalControls, bounds) -> F:
    ratios = []
    for index, denominator_control in branch.denominator.items():
        numerator_control = branch.numerator[index]
        if denominator_control < 0:
            raise AssertionError(("negative denominator control", bounds, index))
        if denominator_control:
            ratios.append(numerator_control / denominator_control)
        elif numerator_control:
            raise AssertionError(("unmatched projective zero", bounds, index))
    if not ratios:
        raise AssertionError(("identically zero denominator box", bounds))
    return max(ratios)


def initial_branches() -> tuple[RationalControls, ...]:
    result = []
    for pattern in ENDPOINT_PATTERNS:
        numerator, denominator = reconstruct_numerator(pattern)
        p_degree = max(polynomial_degrees(numerator)[0], polynomial_degrees(denominator)[0])
        q_degree = max(polynomial_degrees(numerator)[1], polynomial_degrees(denominator)[1])
        degrees = (p_degree, q_degree, 2, 2)
        result.append(
            RationalControls(
                bernstein_coefficients(compactify(numerator, p_degree, q_degree), degrees),
                bernstein_coefficients(compactify(denominator, p_degree, q_degree), degrees),
                degrees,
            )
        )
    return tuple(result)


def split_branch(branch: RationalControls, axis: int) -> tuple[RationalControls, RationalControls]:
    numerator_left, numerator_right = split_controls(branch.numerator, branch.degrees, axis)
    denominator_left, denominator_right = split_controls(branch.denominator, branch.degrees, axis)
    return (
        RationalControls(numerator_left, denominator_left, branch.degrees),
        RationalControls(numerator_right, denominator_right, branch.degrees),
    )


def main() -> None:
    if not (log_bounds(F(3))[0] > 1 and log_bounds(F(8, 3))[1] < 1):
        raise AssertionError("component-entropy critical-point brackets failed")
    branches = initial_branches()
    print(f"endpoint Gram branches reconstructed: {len(branches)}", flush=True)
    stack = [
        Box(
            branches,
            tuple((F(0), F(1)) for _ in range(NVAR)),
            (0,) * NVAR,
        )
    ]
    certified = 0
    smallest_margin = None
    smallest_box = None
    while stack:
        box = stack.pop()
        t_upper = max(branch_upper(branch, box.bounds) for branch in box.branches)
        margin = None
        passed = False
        if F(0) <= t_upper < F(1):
            bell_lower = entropy_bounds(isotropic_probabilities(t_upper))[0]
            side_upper = min(
                side_u_entropy_upper(
                    box.bounds[0][0],
                    box.bounds[0][1],
                    box.bounds[2][0],
                    box.bounds[2][1],
                ),
                side_v_entropy_upper(box.bounds),
            )
            margin = bell_lower - 2 * side_upper
            passed = margin > 0
        if passed:
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
        split = [split_branch(branch, axis) for branch in box.branches]
        low, high = box.bounds[axis]
        midpoint = (low + high) / 2
        left_bounds = list(box.bounds)
        right_bounds = list(box.bounds)
        left_bounds[axis] = (low, midpoint)
        right_bounds[axis] = (midpoint, high)
        depths = list(box.depths)
        depths[axis] += 1
        stack.append(
            Box(tuple(pair[1] for pair in split), tuple(right_bounds), tuple(depths))
        )
        stack.append(
            Box(tuple(pair[0] for pair in split), tuple(left_bounds), tuple(depths))
        )

    print(f"adaptive compact boxes certified: {certified}")
    print(
        "smallest certified natural-log margin > "
        f"{float(smallest_margin):.12e} at {smallest_box}"
    )
    print("canonical adjacent elementary SU(3) face pair is Bell-no-go")


if __name__ == "__main__":
    main()
