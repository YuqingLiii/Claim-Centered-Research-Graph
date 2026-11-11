#!/usr/bin/env python3
"""Exact five-dimensional certificate for a bent h/m, h/m, h/c three-face cover."""

from certify_su3_triangular_three_face_clusters import Configuration, certify


CONFIG = Configuration(
    "bent-hm-hm-hc-fixed-three",
    ((-3, 0), (-1, -1), (0, 0)),
    (
        ((-2, 0), "binary"),
        ((1, 0), "binary"),
        ((2, -2), "binary"),
    ),
    36,
)


if __name__ == "__main__":
    certify(CONFIG)
