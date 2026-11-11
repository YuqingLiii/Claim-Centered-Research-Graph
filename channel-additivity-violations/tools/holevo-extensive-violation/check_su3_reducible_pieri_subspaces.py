#!/usr/bin/env python3
"""Audit the two-lower-branch SU(3) Pieri direct-sum formula through p+q<=6.

For an irreducible environment V_(p,q), p,q>=1, the only invariant direct sum not containing
the product-output highest branch is R_low=V_(p-1,q+1) direct-sum V_(p,q-1).  This script checks
the closed Gram parameter and the explicit middle-branch entropy certificate used in the
all-parameter no-go proof.
"""

from __future__ import annotations

import math

import numpy as np

from check_su3_pieri_channel_formulas import (
    LAM,
    MAX_TOTAL_WEIGHT,
    build_mixed_irreps,
    decompose,
    entropy,
    irrep_dimension,
)


TOL = 3e-8


def expected_low_gram(p: int, q: int) -> float:
    return ((5 * p + 2) * q + 5 * p * p + 9 * p - 2) / (
        8 * (p + 1) * (p + q + 2)
    )


def main() -> None:
    representations = build_mixed_irreps()
    normalized_traceless = LAM[2] / math.sqrt(2)
    checked = 0
    closest_margin = (-math.inf, None)

    for (p, q), environment in sorted(
        representations.items(), key=lambda item: (sum(item[0]), item[0])
    ):
        if not p or not q or p + q > MAX_TOTAL_WEIGHT:
            continue

        environment_dimension = irrep_dimension(p, q)
        sectors = decompose(environment, p, q)
        isometry = np.concatenate(
            [sectors[(p - 1, q + 1)][1], sectors[(p, q - 1)][1]], axis=1
        )
        input_dimension = isometry.shape[1]
        compressed_x = (
            isometry.conj().T
            @ np.kron(normalized_traceless, np.eye(environment_dimension))
            @ isometry
        )
        gram_t = (
            3
            * np.trace(compressed_x.conj().T @ compressed_x).real
            / input_dimension
        )
        expected_t = expected_low_gram(p, q)
        if not np.isclose(gram_t, expected_t, atol=TOL, rtol=0):
            raise AssertionError(
                f"{(p, q)} low-sum Gram t: expected {expected_t}, got {gram_t}"
            )

        explicit_side_entropy = entropy([p / (p + 1), 1 / (p + 1)])
        exceptional = (1 + 8 * gram_t) / 9
        repeated = (1 - gram_t) / 9
        bell_entropy = entropy([exceptional] + [repeated] * 8)
        margin = 2 * explicit_side_entropy - bell_entropy
        if not margin < -1e-8:
            raise AssertionError(f"{(p, q)} nonnegative Bell margin {margin}")
        if margin > closest_margin[0]:
            closest_margin = (margin, (p, q))
        checked += 1

    print(f"two-lower-branch direct sums checked: {checked}")
    print(
        "closest checked explicit-side Bell margin: "
        f"{closest_margin[0]:.12f} at {closest_margin[1]}"
    )
    print(
        "SU(3) reducible Pieri-subspace formulas passed through total weight "
        f"{MAX_TOTAL_WEIGHT}"
    )


if __name__ == "__main__":
    main()
