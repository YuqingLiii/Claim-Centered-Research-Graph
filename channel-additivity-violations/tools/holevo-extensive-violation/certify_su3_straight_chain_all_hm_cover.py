#!/usr/bin/env python3
"""Exact five-dimensional certificate for the all-h/m straight three-face chain cover."""

from certify_su3_triangular_three_face_clusters import Configuration, certify


CONFIG = Configuration(
    "straight-all-hm-fixed-three",
    ((-4, 2), (-2, 1), (0, 0)),
    (
        ((-3, 2), "binary"),
        ((-1, 1), "binary"),
        ((1, 0), "binary"),
    ),
    36,
)


if __name__ == "__main__":
    certify(CONFIG)
