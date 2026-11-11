#!/usr/bin/env python3
"""Grid-audit the exact interior SU(3) covariant-mixture entropy reduction.

This is evidence for, not a proof of, the remaining all-parameter entropy inequality.
"""

from __future__ import annotations

import math

from check_su3_pieri_channel_formulas import entropy, irrep_dimension


MAX_TOTAL_WEIGHT = 30
GRID_DENOMINATOR = 120


def bell_entropy(t: float) -> float:
    return entropy([(1 + 8 * t) / 9] + [(1 - t) / 9] * 8)


def main() -> None:
    checked_irreps = 0
    checked_weights = 0
    smallest = (math.inf, None)
    smallest_positive = (math.inf, None)

    for total in range(2, MAX_TOTAL_WEIGHT + 1):
        for r in range(1, total):
            s = total - r
            d = irrep_dimension(r, s)
            environment_dimensions = [
                irrep_dimension(r - 1, s),
                irrep_dimension(r + 1, s - 1),
                irrep_dimension(r, s + 1),
            ]
            mu = [environment_dimension / (3 * d) for environment_dimension in environment_dimensions]
            extreme_outputs = [
                [1, 0, 0],
                [1 / (r + 2), (r + 1) / (r + 2), 0],
                [
                    1 / (r + s + 3),
                    (r + s + 2) / ((s + 2) * (r + s + 3)),
                    (s + 1) * (r + s + 2) / ((s + 2) * (r + s + 3)),
                ],
            ]

            for a in range(GRID_DENOMINATOR + 1):
                for b in range(GRID_DENOMINATOR + 1 - a):
                    weights = [
                        a / GRID_DENOMINATOR,
                        b / GRID_DENOMINATOR,
                        (GRID_DENOMINATOR - a - b) / GRID_DENOMINATOR,
                    ]
                    t = (sum(weight * weight / center for weight, center in zip(weights, mu)) - 1) / 8
                    output = [
                        sum(weights[i] * extreme_outputs[i][j] for i in range(3))
                        for j in range(3)
                    ]
                    margin = bell_entropy(t) - 2 * entropy(output)
                    record = (r, s, tuple(weights), t, tuple(output))
                    if margin < smallest[0]:
                        smallest = (margin, record)
                    if 1e-12 < margin < smallest_positive[0]:
                        smallest_positive = (margin, record)
                    if margin < -1e-10:
                        raise AssertionError((margin, record))
                    checked_weights += 1
            checked_irreps += 1

    print(f"interior input irreps checked: {checked_irreps}")
    print(f"simplex grid points checked: {checked_weights}")
    print(f"smallest Bell-minus-highest-weight-side margin: {smallest[0]:.12e} at {smallest[1]}")
    print(
        "smallest strictly positive grid margin: "
        f"{smallest_positive[0]:.12e} at {smallest_positive[1]}"
    )
    print("interior SU(3) mixture entropy grid found no violation")


if __name__ == "__main__":
    main()
