#!/usr/bin/env python3
"""Exact polynomial audit of the three elementary shared-environment coefficients."""

from fractions import Fraction as F


def add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, F(0)) + coefficient
    return {monomial: value for monomial, value in result.items() if value}


def scale(poly, coefficient):
    return {monomial: value * coefficient for monomial, value in poly.items() if value}


def multiply(left, right):
    result = {}
    for (p_first, q_first), first in left.items():
        for (p_second, q_second), second in right.items():
            monomial = p_first + p_second, q_first + q_second
            result[monomial] = result.get(monomial, F(0)) + first * second
    return {monomial: value for monomial, value in result.items() if value}


def linear(p_coefficient, q_coefficient, constant):
    return {(1, 0): F(p_coefficient), (0, 1): F(q_coefficient), (0, 0): F(constant)}


def dimension(p_offset, q_offset):
    return scale(
        multiply(
            multiply(linear(1, 0, p_offset + 1), linear(0, 1, q_offset + 1)),
            linear(1, 1, p_offset + q_offset + 2),
        ),
        F(1, 2),
    )


def positive_numerator(first, second, omitted):
    # This is (8 dim(E)) times cross_numerator in the exact branch formula.
    environment = dimension(0, 0)
    branches = {"h": dimension(1, 0), "m": dimension(-1, 1), "c": dimension(0, -1)}
    result = scale(multiply(environment, environment), 24)
    result = add(result, scale(multiply(environment, branches[omitted]), -17))
    result = add(result, scale(multiply(branches[omitted], branches[omitted]), 3))
    for branch in (first, second):
        result = add(result, scale(multiply(branches[branch], branches[branch]), -3))
        result = add(result, multiply(environment, branches[branch]))
    return result


def main():
    for first, second, omitted in (("h", "m", "c"), ("h", "c", "m"), ("m", "c", "h")):
        numerator = positive_numerator(first, second, omitted)
        if not numerator or min(numerator.values()) <= 0:
            raise AssertionError((first, second, numerator))
        print(
            f"{first}{second}: positive monomials={len(numerator)}; "
            f"smallest coefficient={min(numerator.values())}; "
            f"degrees={max(i for i, _ in numerator)},{max(j for _, j in numerator)}"
        )
    print("all elementary shared-environment cross coefficients are nonnegative")


if __name__ == "__main__":
    main()
