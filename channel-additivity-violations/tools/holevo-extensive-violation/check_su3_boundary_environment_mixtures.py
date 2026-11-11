#!/usr/bin/env python3
"""Audit the entropy inequality for all two-extreme SU(3) boundary-input mixtures."""

from __future__ import annotations

import math

from check_su3_pieri_channel_formulas import entropy


def h3(z: float) -> float:
    return entropy([(1 + 2 * z) / 3, (1 - z) / 3, (1 - z) / 3])


def bell_entropy(t: float) -> float:
    return entropy([(1 + 8 * t) / 9] + [(1 - t) / 9] * 8)


def main() -> None:
    checked = 0
    closest_margin = (math.inf, None)
    for weight in range(1, 101):
        c = (weight + 3) / (4 * weight)
        for step in range(1001):
            alpha = step / 1000
            mu_high = weight / (3 * (weight + 2))
            z_symmetric = 3 * (alpha - mu_high) * (weight + 2) / (
                2 * (weight + 3)
            )
            t_symmetric = c * z_symmetric * z_symmetric
            margin = bell_entropy(t_symmetric) - 2 * h3(z_symmetric)
            if margin < -1e-11:
                raise AssertionError(("symmetric", weight, alpha, margin))
            if margin < closest_margin[0]:
                closest_margin = (margin, ("symmetric", weight, alpha))
            checked += 1

            mu_middle = 2 * weight / (3 * (weight + 1))
            z_conjugate = -3 * (alpha - mu_middle) * (weight + 1) / (
                2 * (weight + 3)
            )
            t_conjugate = c * z_conjugate * z_conjugate
            margin = bell_entropy(t_conjugate) - 2 * h3(z_conjugate)
            if margin < -1e-11:
                raise AssertionError(("conjugate", weight, alpha, margin))
            if margin < closest_margin[0]:
                closest_margin = (margin, ("conjugate", weight, alpha))
            checked += 1

    print(f"boundary mixture parameter points checked: {checked}")
    print(f"smallest Bell-minus-explicit-side margin: {closest_margin[0]:.12e}")
    print("SU(3) boundary inequivalent-environment mixture inequality passed")


if __name__ == "__main__":
    main()
