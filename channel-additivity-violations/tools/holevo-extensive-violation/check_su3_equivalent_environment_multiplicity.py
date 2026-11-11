#!/usr/bin/env python3
"""Audit the convex Gram reduction for repeated copies of one SU(3) environment irrep."""

from __future__ import annotations

import math

from check_su3_pieri_channel_formulas import entropy, irrep_dimension
from check_su3_reducible_pieri_subspaces import expected_low_gram


def middle_gram(p: int, q: int) -> float:
    return ((2 * p - 1) * q + 5 * p - 1) / (8 * (p + 1) * (q + 1))


def third_gram(p: int, q: int) -> float:
    return ((2 * q - 1) * p + 2 * (q * q - 1)) / (
        8 * (q + 1) * (p + q + 2)
    )


def bell_entropy(t: float) -> float:
    return entropy([(1 + 8 * t) / 9] + [(1 - t) / 9] * 8)


def main() -> None:
    checked = 0
    closest_margin = (-math.inf, None)
    for p in range(1, 8):
        for q in range(1, 8):
            dm = irrep_dimension(p - 1, q + 1)
            dc = irrep_dimension(p, q - 1)
            tm = middle_gram(p, q)
            tc = third_gram(p, q)
            tlow = expected_low_gram(p, q)
            if not (tlow > tm and tlow > tc):
                raise AssertionError(f"Gram ordering failed at {(p, q)}")

            side = entropy([p / (p + 1), 1 / (p + 1)])
            for rm in range(1, 5):
                for rc in range(1, 5):
                    for step in range(6):
                        h = min(rm, rc) * step / 5
                        numerator = (
                            h * (dm + dc) * tlow
                            + (rm - h) * dm * tm
                            + (rc - h) * dc * tc
                        )
                        denominator = h * (dm + dc) + (rm - h) * dm + (rc - h) * dc
                        t = numerator / denominator
                        if t > tlow + 1e-12:
                            raise AssertionError(f"convex Gram bound failed at {(p, q, rm, rc, h)}")
                        margin = 2 * side - bell_entropy(t)
                        if not margin < -1e-10:
                            raise AssertionError(f"Bell no-go failed at {(p, q, rm, rc, h)}")
                        if margin > closest_margin[0]:
                            closest_margin = (margin, (p, q, rm, rc, h))
                        checked += 1

    print(f"multiplicity parameter points checked: {checked}")
    print(
        "closest checked explicit-side Bell margin: "
        f"{closest_margin[0]:.12f} at {closest_margin[1]}"
    )
    print("equivalent-environment multiplicity convex reduction passed")


if __name__ == "__main__":
    main()
