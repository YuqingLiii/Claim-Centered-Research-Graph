#!/usr/bin/env python3
"""Exact refutation of the naive top-space sign-lock ansatz.

For the frozen H4 instance, reconstruct

    P = (X + Y sqrt(5)) / 8

and compare the exact coordinate signs of ``P by`` and ``P ax`` with the
archived classical witness signs.  No floating-point comparison is used.

Dependencies: numpy and h5py.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import h5py
import numpy as np

from h4_exact_instance_checker import (
    EXPECTED_A_SHA256,
    canonical_int64_sha256,
    exact_int_matrix,
    exact_signs,
    q5_sign,
    reconstruct_exact_gram,
)


EXPECTED = {
    "P_by": {
        "same": 257,
        "opposite": 37,
        "zero": 6,
        "zero_indices": [168, 177, 212, 232, 267, 287],
    },
    "P_ax": {
        "same": 254,
        "opposite": 40,
        "zero": 6,
        "zero_indices": [168, 177, 212, 232, 267, 287],
    },
}


def exact_profile(
    x_part: np.ndarray,
    y_part: np.ndarray,
    source: list[int],
    target: list[int],
) -> dict[str, object]:
    source_object = np.asarray(source, dtype=object)
    real = x_part.astype(object) @ source_object
    radical = y_part.astype(object) @ source_object
    signs = np.asarray(
        [q5_sign(int(a), int(b)) for a, b in zip(real, radical)],
        dtype=np.int8,
    )
    target_array = np.asarray(target, dtype=np.int8)
    return {
        "same": int(np.count_nonzero(signs == target_array)),
        "opposite": int(np.count_nonzero(signs == -target_array)),
        "zero": int(np.count_nonzero(signs == 0)),
        "zero_indices": np.flatnonzero(signs == 0).tolist(),
        "opposite_indices": np.flatnonzero(signs == -target_array).tolist(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mat", type=Path)
    args = parser.parse_args()

    with h5py.File(args.mat.resolve(), "r") as archive:
        a = exact_int_matrix(archive["A"][()])
        ax = exact_signs(archive["ax"][()], "ax")
        by = exact_signs(archive["by"][()], "by")

    if canonical_int64_sha256(a) != EXPECTED_A_SHA256:
        raise AssertionError("canonical A SHA-256 mismatch")

    x_part, y_part = reconstruct_exact_gram(a)
    profiles = {
        "P_by": exact_profile(x_part, y_part, by, ax),
        "P_ax": exact_profile(x_part, y_part, ax, by),
    }

    for name, expected in EXPECTED.items():
        actual = profiles[name]
        for key, value in expected.items():
            if actual[key] != value:
                raise AssertionError(
                    f"{name}.{key}: observed {actual[key]!r}, expected {value!r}"
                )

    print(f"A_canonical_sha256 = {EXPECTED_A_SHA256}")
    for name in ("P_by", "P_ax"):
        profile = profiles[name]
        print(
            f"{name}: same={profile['same']}, opposite={profile['opposite']}, "
            f"zero={profile['zero']}"
        )
        print(f"{name}: zero_indices={profile['zero_indices']}")
        print(f"{name}: opposite_indices={profile['opposite_indices']}")
    print("conclusion = both naive top-space sign-lock identities are false")


if __name__ == "__main__":
    main()
