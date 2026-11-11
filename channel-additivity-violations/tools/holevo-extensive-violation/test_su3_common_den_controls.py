#!/usr/bin/env python3
"""Exact equivalence tests for the common-denominator Bernstein backend."""

from fractions import Fraction
from itertools import product
from random import Random

import certify_su3_highest_edge_adjacent_faces as fraction_backend
from su3_common_den_controls import (
    add_common_controls,
    common_den_controls,
    fraction_controls,
    rational_range_common,
    split_common_controls,
)


def main():
    rng = Random(20260830)
    for degrees in ((2, 2), (3, 2, 1), (2, 1, 2, 1)):
        fraction_backend.NVAR = len(degrees)
        indices = tuple(product(*(range(degree + 1) for degree in degrees)))
        numerator = {
            index: Fraction(rng.randint(-20, 20), rng.randint(1, 17)) for index in indices
        }
        denominator = {
            index: Fraction(rng.randint(1, 20), rng.randint(1, 17)) for index in indices
        }
        common_num = common_den_controls(numerator)
        common_den = common_den_controls(denominator)
        assert fraction_controls(common_num) == numerator
        assert fraction_controls(common_den) == denominator
        bounds = tuple((Fraction(0), Fraction(1)) for _ in degrees)
        assert rational_range_common(common_num, common_den, bounds) == fraction_backend.rational_range(
            numerator, denominator, bounds
        )
        for axis in range(len(degrees)):
            fraction_splits = fraction_backend.split_controls(numerator, degrees, axis)
            common_splits = split_common_controls(common_num, degrees, axis)
            assert tuple(map(fraction_controls, common_splits)) == fraction_splits
            fraction_den_splits = fraction_backend.split_controls(denominator, degrees, axis)
            common_den_splits = split_common_controls(common_den, degrees, axis)
            for fraction_num, fraction_den, compact_num, compact_den in zip(
                fraction_splits, fraction_den_splits, common_splits, common_den_splits
            ):
                assert rational_range_common(compact_num, compact_den, bounds) == fraction_backend.rational_range(
                    fraction_num, fraction_den, bounds
                )
        doubled = add_common_controls(common_num, common_num)
        assert fraction_controls(doubled) == {
            index: 2 * value for index, value in numerator.items()
        }
    print("common-denominator Bernstein controls exactly match Fraction backend")


if __name__ == "__main__":
    main()
