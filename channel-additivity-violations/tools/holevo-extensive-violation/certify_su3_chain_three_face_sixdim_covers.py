#!/usr/bin/env python3
"""Exact six-dimensional certificates for chain covers with one retained ternary block."""

from __future__ import annotations

import argparse

import certify_su3_input_centered_triangle_sixdim as core
from certify_su3_triangular_three_face_clusters import Configuration


CONFIGURATIONS = {
    "bent-left-ternary": Configuration(
        "bent-left-ternary-fixed-three",
        ((-3, 3), (-2, 1), (0, 0)),
        (((-2, 3), "binary"), ((-1, 1), "ternary"), ((1, 0), "binary")),
        24,
    ),
    "bent-right-ternary": Configuration(
        "bent-right-ternary-fixed-three",
        ((-3, 3), (-1, 2), (0, 0)),
        (((-2, 3), "binary"), ((0, 2), "binary"), ((1, 0), "ternary")),
        24,
    ),
    "straight-ternary": Configuration(
        "straight-ternary-fixed-three",
        ((-2, -2), (-1, -1), (0, 0)),
        (((0, -1), "ternary"), ((1, 0), "binary"), ((2, -2), "binary")),
        24,
    ),
    "straight-reduced-coordinate": Configuration(
        "straight-reduced-coordinate-fixed-three",
        ((-2, 4), (-1, 2), (0, 0)),
        (((-1, 4), "binary"), ((0, 2), "ternary"), ((2, -2), "binary")),
        24,
    ),
    "bent-central-ternary": Configuration(
        "bent-central-ternary-fixed-three",
        ((-1, -1), (-1, 2), (0, 0)),
        (((0, 2), "binary"), ((1, 0), "ternary"), ((2, -2), "binary")),
        24,
    ),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("configuration", choices=tuple(CONFIGURATIONS))
    arguments = parser.parse_args()
    core.CONFIG = CONFIGURATIONS[arguments.configuration]
    core.main()


if __name__ == "__main__":
    main()
