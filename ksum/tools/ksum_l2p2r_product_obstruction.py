"""Exact checks of the normalized sign-separated product correlation formula.

The structural proof belongs in the review report.  This driver stress-tests its
normalization against unequal rational shapes and scales, then checks positive
mixtures of sign-aligned products.  Every local factor has zero total mass and
opposite constant signs on the axis and interior regions.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


def local_factor(scale: Fraction, variant: int):
    if variant % 3 == 0:
        axis_shape = (Fraction(1, 3), Fraction(2, 3))
        interior_shape = (Fraction(1, 4), Fraction(3, 4))
    elif variant % 3 == 1:
        axis_shape = (Fraction(4, 5), Fraction(1, 5))
        interior_shape = (Fraction(2, 7), Fraction(3, 7), Fraction(2, 7))
    else:
        axis_shape = (Fraction(1, 2), Fraction(1, 2))
        interior_shape = (Fraction(1, 9), Fraction(2, 9), Fraction(2, 3))
    factor = {}
    for index, probability in enumerate(axis_shape):
        factor[("A", index)] = -scale * probability
    for index, probability in enumerate(interior_shape):
        factor[("I", index)] = scale * probability
    assert sum(factor.values()) == 0
    assert sum(abs(weight) for weight in factor.values()) == 2 * scale
    return factor


def normalized_product(factors):
    raw = {}
    for choices in itertools.product(*(tuple(factor.items()) for factor in factors)):
        state = tuple(label for label, _ in choices)
        weight = Fraction(1)
        for _, local_weight in choices:
            weight *= local_weight
        raw[state] = weight
    norm = sum(abs(weight) for weight in raw.values())
    r = len(factors)
    orientation = (-1) ** (r + 1)
    return {state: Fraction(orientation) * weight / norm for state, weight in raw.items()}


def statistics(weights):
    norm = sum(abs(weight) for weight in weights.values())
    mass = sum(weights.values())
    no_mass = sum(
        weight for state, weight in weights.items() if all(region == "A" for region, _ in state)
    )
    correlation = sum(
        weight * (-1 if all(region == "A" for region, _ in state) else 1)
        for state, weight in weights.items()
    )
    return norm, mass, no_mass, correlation


def verify_product(r: int, offset: int):
    scales = [Fraction((index + 2) * (offset + 1), index + offset + 3) for index in range(r)]
    factors = [local_factor(scale, index + offset) for index, scale in enumerate(scales)]
    weights = normalized_product(factors)
    norm, mass, no_mass, correlation = statistics(weights)
    expected = Fraction(1, 2 ** (r - 1))
    assert norm == 1
    assert mass == 0
    assert no_mass == -Fraction(1, 2**r)
    assert correlation == expected
    return weights, {
        "r": r,
        "variant": offset,
        "local_l1_scales": [str(2 * scale) for scale in scales],
        "normalized_l1": str(norm),
        "total_mass": str(mass),
        "no_mass": str(no_mass),
        "correlation": str(correlation),
        "expected": str(expected),
        "result": "PASS",
    }


def verify_mixture(r: int):
    first, _ = verify_product(r, 0)
    second, _ = verify_product(r, 2)
    mixture_weight = Fraction(2, 5)
    keys = set(first) | set(second)
    mixture = {
        key: mixture_weight * first.get(key, 0) + (1 - mixture_weight) * second.get(key, 0)
        for key in keys
    }
    norm, mass, no_mass, correlation = statistics(mixture)
    expected = Fraction(1, 2 ** (r - 1))
    assert norm == 1
    assert mass == 0
    assert no_mass == -Fraction(1, 2**r)
    assert correlation == expected
    return {
        "r": r,
        "mixture_weights": [str(mixture_weight), str(1 - mixture_weight)],
        "normalized_l1": str(norm),
        "total_mass": str(mass),
        "no_mass": str(no_mass),
        "correlation": str(correlation),
        "expected": str(expected),
        "result": "PASS",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    products = []
    mixtures = []
    for r in range(1, 5):
        for offset in range(3):
            _, record = verify_product(r, offset)
            products.append(record)
        mixtures.append(verify_mixture(r))
    payload = {
        "class": "every local factor zero-mass and sign-separated; sign-aligned positive mixtures",
        "arithmetic": "fractions.Fraction",
        "products": products,
        "mixtures": mixtures,
        "verification": "PASS",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
