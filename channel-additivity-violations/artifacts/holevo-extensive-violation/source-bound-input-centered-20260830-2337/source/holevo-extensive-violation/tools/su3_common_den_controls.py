#!/usr/bin/env python3
"""Exact Bernstein controls with one common denominator per control tensor."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd
from typing import Mapping


Index = tuple[int, ...]


def _lcm(first: int, second: int) -> int:
    return first // gcd(first, second) * second


@dataclass(frozen=True)
class CommonDenControls:
    values: Mapping[Index, int]
    denominator: int

    def __post_init__(self):
        if self.denominator <= 0:
            raise ValueError("control denominator must be positive")


def common_den_controls(controls) -> CommonDenControls:
    denominator = 1
    for value in controls.values():
        denominator = _lcm(denominator, value.denominator)
    return CommonDenControls(
        {
            index: value.numerator * (denominator // value.denominator)
            for index, value in controls.items()
        },
        denominator,
    )


def fraction_controls(controls: CommonDenControls):
    """Testing/debug conversion; certificate hot paths never call this."""
    return {
        index: Fraction(value, controls.denominator)
        for index, value in controls.values.items()
    }


def split_common_controls(
    controls: CommonDenControls, degrees: tuple[int, ...], axis: int
) -> tuple[CommonDenControls, CommonDenControls]:
    degree = degrees[axis]
    output_denominator = controls.denominator << degree
    left: dict[Index, int] = {}
    right: dict[Index, int] = {}
    other_axes = [candidate for candidate in range(len(degrees)) if candidate != axis]
    for fixed in product(*(range(degrees[candidate] + 1) for candidate in other_axes)):
        line = []
        for moving in range(degree + 1):
            index = [0] * len(degrees)
            index[axis] = moving
            for candidate, value in zip(other_axes, fixed):
                index[candidate] = value
            line.append(controls.values[tuple(index)])
        levels = [line]
        while len(levels[-1]) > 1:
            previous = levels[-1]
            levels.append([
                previous[position] + previous[position + 1]
                for position in range(len(previous) - 1)
            ])
        for moving in range(degree + 1):
            left_index = [0] * len(degrees)
            right_index = [0] * len(degrees)
            left_index[axis] = moving
            right_index[axis] = moving
            for candidate, value in zip(other_axes, fixed):
                left_index[candidate] = value
                right_index[candidate] = value
            left[tuple(left_index)] = levels[moving][0] << (degree - moving)
            right_level = degree - moving
            right[tuple(right_index)] = levels[right_level][moving] << moving
    return (
        CommonDenControls(left, output_denominator),
        CommonDenControls(right, output_denominator),
    )


def add_common_controls(
    first: CommonDenControls, second: CommonDenControls
) -> CommonDenControls:
    if first.values.keys() != second.values.keys():
        raise ValueError("control grids do not match")
    if first.denominator == second.denominator:
        return CommonDenControls(
            {index: first.values[index] + second.values[index] for index in first.values},
            first.denominator,
        )
    denominator = _lcm(first.denominator, second.denominator)
    first_scale = denominator // first.denominator
    second_scale = denominator // second.denominator
    return CommonDenControls(
        {
            index: first.values[index] * first_scale + second.values[index] * second_scale
            for index in first.values
        },
        denominator,
    )


def _less(first: tuple[int, int], second: tuple[int, int]) -> bool:
    return first[0] * second[1] < second[0] * first[1]


def rational_range_common(
    numerator: CommonDenControls,
    denominator: CommonDenControls,
    bounds,
) -> tuple[Fraction, Fraction]:
    if numerator.values.keys() != denominator.values.keys():
        raise ValueError("numerator and denominator control grids do not match")
    minimum = None
    maximum = None
    for index, denominator_control in denominator.values.items():
        numerator_control = numerator.values[index]
        if denominator_control < 0:
            raise AssertionError(("negative denominator control", bounds, index))
        if denominator_control:
            candidate = (
                numerator_control * denominator.denominator,
                denominator_control * numerator.denominator,
            )
            if minimum is None or _less(candidate, minimum):
                minimum = candidate
            if maximum is None or _less(maximum, candidate):
                maximum = candidate
        elif numerator_control:
            raise AssertionError(("unmatched projective zero", bounds, index))
    if minimum is None:
        raise AssertionError(("identically zero denominator box", bounds))
    return (
        max(Fraction(0), Fraction(*minimum)),
        min(Fraction(1), Fraction(*maximum)),
    )
