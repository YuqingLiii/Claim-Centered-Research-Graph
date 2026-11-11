#!/usr/bin/env python3
"""Exact five-dimensional certificate for the numerically weakest bent three-face chain."""

from certify_su3_triangular_three_face_clusters import Configuration, certify


CONFIG = Configuration(
    "weakest-bent-fixed-three",
    ((-3, 0), (-2, 1), (0, 0)),
    (
        ((-1, -2), "binary"),
        ((-1, 1), "binary"),
        ((1, 0), "binary"),
    ),
    36,
)


if __name__ == "__main__":
    certify(CONFIG)
