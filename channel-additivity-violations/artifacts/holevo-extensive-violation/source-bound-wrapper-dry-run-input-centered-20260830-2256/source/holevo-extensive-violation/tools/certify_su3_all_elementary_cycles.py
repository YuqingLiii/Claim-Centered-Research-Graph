#!/usr/bin/env python3
"""Exact compactified certificate for every translated elementary SU(3) cycle.

The proof uses only the standard library.  It reconstructs the four rational
corner Gram functions from exact representation-theoretic formulas, maps the
unbounded parameters p>=0 and q>=2 to a compact square, and bounds each
rational function by rational Bernstein control points.  Adaptive dyadic
subdivision then compares the Bell-output entropy with one explicit side
output, using rigorous atanh-series logarithm intervals.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb


F = Fraction
LOG_TERMS = 24
MAX_DEPTH_PER_AXIS = 6


def dimension(p: F, q: F) -> F:
    return (p + 1) * (q + 1) * (p + q + 2) / 2


def environment_barycenter(r: F, s: F) -> dict[str, F]:
    total = dimension(r, s)
    result: dict[str, F] = {}
    if r:
        result["h"] = dimension(r - 1, s) / (3 * total)
    if s:
        result["m"] = dimension(r + 1, s - 1) / (3 * total)
    result["c"] = dimension(r, s + 1) / (3 * total)
    return result


def mixture_t(r: F, s: F, weights: dict[str, F]) -> F:
    center = environment_barycenter(r, s)
    return (sum(weights[key] ** 2 / center[key] for key in center) - 1) / 8


def branch_data(p: F, q: F) -> tuple[F, dict[str, F], dict[str, F]]:
    environment_dimension = dimension(p, q)
    dimensions = {"h": dimension(p + 1, q)}
    if p:
        dimensions["m"] = dimension(p - 1, q + 1)
    if q:
        dimensions["c"] = dimension(p, q - 1)
    contractions = {
        branch: 3 * input_dimension / (8 * environment_dimension) - F(1, 8)
        for branch, input_dimension in dimensions.items()
    }
    return environment_dimension, dimensions, contractions


def cross_numerator(p: F, q: F, first: str, second: str) -> F:
    environment_dimension, dimensions, contractions = branch_data(p, q)
    remaining = set(dimensions) - {first, second}
    if remaining:
        omitted = next(iter(remaining))
        pair_numerator = (
            3 * environment_dimension
            - 2 * dimensions[omitted]
            + dimensions[omitted] * contractions[omitted]
        )
    else:
        pair_numerator = 3 * environment_dimension
    return (
        pair_numerator
        - dimensions[first] * contractions[first]
        - dimensions[second] * contractions[second]
    )


def cycle_t(p: F, q: F, x: F, y: int, z: int) -> F:
    representations = ((p + 1, q), (p + 2, q - 2), (p, q - 1))
    dimensions = [dimension(*label) for label in representations]
    third_weights = {"m": F(z), "c": F(1 - z)}
    if p:
        third_weights["h"] = F(0)
    contractions = [
        mixture_t(*representations[0], {"h": x, "m": 1 - x, "c": F(0)}),
        mixture_t(
            *representations[1], {"h": F(1 - y), "m": F(0), "c": F(y)}
        ),
        mixture_t(*representations[2], third_weights),
    ]
    numerator = sum(d * t for d, t in zip(dimensions, contractions))
    numerator += x * (1 - z) * cross_numerator(p, q, "h", "c")
    numerator += (1 - x) * y * cross_numerator(p + 2, q - 1, "m", "c")
    numerator += (1 - y) * z * cross_numerator(p + 1, q - 2, "h", "m")
    return numerator / sum(dimensions)


# Polynomials are sparse maps in variables (p,Q,x) before compactification and
# in variables (a,b,x) afterwards.  Here Q=q-2, a=p/(p+1), b=Q/(Q+1).
Poly = dict[tuple[int, int, int], F]


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
            monomial = tuple(first[index] + second[index] for index in range(3))
            result[monomial] = result.get(monomial, F(0)) + a * b
    return {monomial: value for monomial, value in result.items() if value}


def poly_scale(poly: Poly, scalar: F) -> Poly:
    return {monomial: scalar * value for monomial, value in poly.items() if scalar * value}


def poly_evaluate(poly: Poly, variables: tuple[F, F, F]) -> F:
    return sum(
        coefficient
        * variables[0] ** monomial[0]
        * variables[1] ** monomial[1]
        * variables[2] ** monomial[2]
        for monomial, coefficient in poly.items()
    )


def linear(axis: int, constant: F, slope: F = F(1)) -> Poly:
    zero = (0, 0, 0)
    exponent = [0, 0, 0]
    exponent[axis] = 1
    result = {zero: constant}
    if slope:
        result[tuple(exponent)] = slope
    return {monomial: value for monomial, value in result.items() if value}


def poly_power(poly: Poly, exponent: int) -> Poly:
    result = {(0, 0, 0): F(1)}
    for _ in range(exponent):
        result = poly_mul(result, poly)
    return result


def denominator_polynomial(corner: tuple[int, int]) -> Poly:
    """Known positive denominator after q=Q+2, up to no omitted factor."""
    p = linear(0, F(0))
    q = linear(1, F(2))
    factors: list[Poly] = [
        {(0, 0, 0): F(8)},
        poly_power(q, 2),
        poly_add(p, {(0, 0, 0): F(1)}),
        poly_add(p, {(0, 0, 0): F(3)}),
    ]
    y, z = corner
    if y == z:
        factors.append(poly_power(poly_add(p, {(0, 0, 0): F(2)}), 2))
    factors.append(poly_add(q, {(0, 0, 0): F(-1 if z else 1)}))
    if y == 0:
        factors.append(poly_add(poly_add(p, q), {(0, 0, 0): F(1)}))
    else:
        factors.append(poly_add(poly_add(p, q), {(0, 0, 0): F(3)}))
    factors.append(poly_power(poly_add(poly_add(p, q), {(0, 0, 0): F(2)}), 2))
    result = {(0, 0, 0): F(1)}
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


def reconstruct_numerator(corner: tuple[int, int]) -> tuple[Poly, Poly]:
    degrees = (7, 6, 2) if corner[0] == corner[1] else (5, 6, 2)
    bases = [
        [lagrange_basis(degree, index) for index in range(degree + 1)]
        for degree in degrees
    ]
    denominator = denominator_polynomial(corner)
    numerator: Poly = {}
    y, z = corner
    for p_index, q_index, x_index in product(
        range(degrees[0] + 1), range(degrees[1] + 1), range(degrees[2] + 1)
    ):
        p_value, q_offset, x_value = F(p_index), F(q_index), F(x_index)
        value = cycle_t(p_value, q_offset + 2, x_value, y, z)
        value *= poly_evaluate(denominator, (p_value, q_offset, x_value))
        if not value:
            continue
        for i, first in enumerate(bases[0][p_index]):
            for j, second in enumerate(bases[1][q_index]):
                for k, third in enumerate(bases[2][x_index]):
                    coefficient = value * first * second * third
                    if coefficient:
                        monomial = (i, j, k)
                        numerator[monomial] = numerator.get(monomial, F(0)) + coefficient
    numerator = {monomial: value for monomial, value in numerator.items() if value}

    tests = (
        (F(0), F(0), F(1, 3)),
        (F(3, 2), F(7, 3), F(4, 5)),
        (F(5), F(2), F(7, 5)),
    )
    for p_value, q_offset, x_value in tests:
        direct = cycle_t(p_value, q_offset + 2, x_value, y, z)
        reconstructed = poly_evaluate(numerator, (p_value, q_offset, x_value))
        reconstructed /= poly_evaluate(denominator, (p_value, q_offset, x_value))
        if direct != reconstructed:
            raise AssertionError(("interpolation mismatch", corner, direct, reconstructed))
    return numerator, denominator


def compactify(poly: Poly, p_degree: int, q_degree: int) -> Poly:
    """Homogenize p=a/(1-a), Q=b/(1-b) into a polynomial on [0,1]^2."""
    result: Poly = {}
    for (p_power, q_power, x_power), coefficient in poly.items():
        for p_tail in range(p_degree - p_power + 1):
            p_coefficient = F(comb(p_degree - p_power, p_tail)) * (-1) ** p_tail
            for q_tail in range(q_degree - q_power + 1):
                q_coefficient = F(comb(q_degree - q_power, q_tail)) * (-1) ** q_tail
                monomial = (p_power + p_tail, q_power + q_tail, x_power)
                result[monomial] = result.get(monomial, F(0)) + (
                    coefficient * p_coefficient * q_coefficient
                )
    return {monomial: value for monomial, value in result.items() if value}


def bernstein_coefficients(poly: Poly, degrees: tuple[int, int, int]) -> Poly:
    result: Poly = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        value = F(0)
        for monomial, coefficient in poly.items():
            if all(monomial[axis] <= index[axis] for axis in range(3)):
                factor = F(1)
                for axis in range(3):
                    factor *= F(
                        comb(index[axis], monomial[axis]),
                        comb(degrees[axis], monomial[axis]),
                    )
                value += coefficient * factor
        result[index] = value
    return result


def split_controls(controls: Poly, degrees: tuple[int, int, int], axis: int) -> tuple[Poly, Poly]:
    left: Poly = {}
    right: Poly = {}
    other_axes = [candidate for candidate in range(3) if candidate != axis]
    for fixed in product(*(range(degrees[candidate] + 1) for candidate in other_axes)):
        line = []
        for moving in range(degrees[axis] + 1):
            index = [0, 0, 0]
            index[axis] = moving
            for candidate, value in zip(other_axes, fixed):
                index[candidate] = value
            line.append(controls[tuple(index)])
        levels = [line]
        while len(levels[-1]) > 1:
            previous = levels[-1]
            levels.append([(previous[i] + previous[i + 1]) / 2 for i in range(len(previous) - 1)])
        for moving in range(degrees[axis] + 1):
            left_index = [0, 0, 0]
            right_index = [0, 0, 0]
            left_index[axis] = moving
            right_index[axis] = moving
            for candidate, value in zip(other_axes, fixed):
                left_index[candidate] = value
                right_index[candidate] = value
            left[tuple(left_index)] = levels[moving][0]
            right[tuple(right_index)] = levels[degrees[axis] - moving][moving]
    return left, right


def reduced_log_bounds(value: F) -> tuple[F, F]:
    z = (value - 1) / (value + 1)
    z_squared = z * z
    power = z
    total = F(0)
    for index in range(LOG_TERMS):
        total += 2 * power / (2 * index + 1)
        power *= z_squared
    remainder = 2 * power / ((2 * LOG_TERMS + 1) * (1 - z_squared))
    return total, total + remainder


LN2_LOWER, LN2_UPPER = reduced_log_bounds(F(2))


def log_bounds(value: F) -> tuple[F, F]:
    if value <= 0:
        raise ValueError("log input must be positive")
    exponent = 0
    reduced = value
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    low, high = reduced_log_bounds(reduced)
    if exponent >= 0:
        return low + exponent * LN2_LOWER, high + exponent * LN2_UPPER
    return low + exponent * LN2_UPPER, high + exponent * LN2_LOWER


def entropy_bounds(probabilities: list[F]) -> tuple[F, F]:
    low = F(0)
    high = F(0)
    for probability in probabilities:
        if not probability:
            continue
        log_low, log_high = log_bounds(probability)
        low -= probability * log_high
        high -= probability * log_low
    return low, high


def isotropic_probabilities(t: F) -> list[F]:
    return [(1 + 8 * t) / 9] + [(1 - t) / 9] * 8


def side_probability(a: F, x: F) -> F:
    return x + (1 - x) * (1 - a) / (3 - 2 * a)


def side_entropy_upper(a_low: F, a_high: F, x_low: F, x_high: F) -> F:
    probability_low = side_probability(a_high, x_low)
    probability_high = side_probability(a_low, x_high)
    if probability_low <= F(1, 2) <= probability_high:
        return LN2_UPPER
    probability = probability_high if probability_high < F(1, 2) else probability_low
    return entropy_bounds([probability, 1 - probability])[1]


@dataclass(frozen=True)
class Box:
    numerator: Poly
    denominator: Poly
    bounds: tuple[tuple[F, F], tuple[F, F], tuple[F, F]]
    depths: tuple[int, int, int]


def certify_corner(corner: tuple[int, int]) -> tuple[int, F, tuple[tuple[F, F], ...]]:
    numerator, denominator = reconstruct_numerator(corner)
    p_degree = max(max(key[0] for key in numerator), max(key[0] for key in denominator))
    q_degree = max(max(key[1] for key in numerator), max(key[1] for key in denominator))
    degrees = (p_degree, q_degree, 2)
    compact_numerator = compactify(numerator, p_degree, q_degree)
    compact_denominator = compactify(denominator, p_degree, q_degree)
    initial = Box(
        bernstein_coefficients(compact_numerator, degrees),
        bernstein_coefficients(compact_denominator, degrees),
        ((F(0), F(1)), (F(0), F(1)), (F(0), F(1))),
        (0, 0, 0),
    )
    stack = [initial]
    certified = 0
    smallest_margin: F | None = None
    smallest_box: tuple[tuple[F, F], ...] | None = None
    while stack:
        box = stack.pop()
        if any(value < 0 for value in box.denominator.values()):
            raise AssertionError(("negative denominator control", corner, box.bounds))
        ratios = []
        for index, denominator_control in box.denominator.items():
            numerator_control = box.numerator[index]
            if denominator_control:
                ratios.append(numerator_control / denominator_control)
            elif numerator_control:
                raise AssertionError(
                    ("unmatched projective zero", corner, box.bounds, index)
                )
        if not ratios:
            raise AssertionError(("identically zero denominator box", corner, box.bounds))
        t_upper = max(ratios)
        a_low, a_high = box.bounds[0]
        x_low, x_high = box.bounds[2]
        passed = False
        margin = None
        if F(0) <= t_upper < F(1):
            bell_lower = entropy_bounds(isotropic_probabilities(t_upper))[0]
            side_upper = side_entropy_upper(a_low, a_high, x_low, x_high)
            margin = bell_lower - 2 * side_upper
            passed = margin > 0
        if passed:
            certified += 1
            if smallest_margin is None or margin < smallest_margin:
                smallest_margin = margin
                smallest_box = box.bounds
            continue
        available = [
            axis for axis in range(3) if box.depths[axis] < MAX_DEPTH_PER_AXIS
        ]
        if not available:
            raise AssertionError(
                ("uncertified compact box", corner, box.bounds, t_upper, margin)
            )
        axis = min(available, key=lambda candidate: (box.depths[candidate], candidate))
        numerator_left, numerator_right = split_controls(box.numerator, degrees, axis)
        denominator_left, denominator_right = split_controls(box.denominator, degrees, axis)
        low, high = box.bounds[axis]
        midpoint = (low + high) / 2
        left_bounds = list(box.bounds)
        right_bounds = list(box.bounds)
        left_bounds[axis] = (low, midpoint)
        right_bounds[axis] = (midpoint, high)
        depths = list(box.depths)
        depths[axis] += 1
        stack.append(Box(numerator_right, denominator_right, tuple(right_bounds), tuple(depths)))
        stack.append(Box(numerator_left, denominator_left, tuple(left_bounds), tuple(depths)))
    if smallest_margin is None or smallest_box is None:
        raise AssertionError(("no boxes certified", corner))
    return certified, smallest_margin, smallest_box


def main() -> None:
    total_boxes = 0
    global_margin: F | None = None
    global_location = None
    for corner in ((0, 0), (0, 1), (1, 0), (1, 1)):
        boxes, margin, location = certify_corner(corner)
        total_boxes += boxes
        if global_margin is None or margin < global_margin:
            global_margin = margin
            global_location = (corner, location)
        print(
            f"corner {corner}: {boxes} compact boxes certified; "
            f"smallest natural-log margin > {float(margin):.12e}"
        )
    print(f"total compact boxes certified: {total_boxes}")
    print(
        "global certified natural-log margin > "
        f"{float(global_margin):.12e} at {global_location}"
    )
    print("all translated elementary SU(3) cycles are Bell-no-go")


if __name__ == "__main__":
    main()
