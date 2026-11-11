#!/usr/bin/env python3
"""Exact five-dimensional certificate for the bent c/m, h/m, h/c cover."""

from certify_su3_triangular_three_face_clusters import Configuration, certify


CONFIG = Configuration(
    "bent-cm-hm-hc-fixed-three",
    ((-1, -1), (0, -3), (0, 0)),
    (
        ((-1, -2), "binary"),
        ((1, 0), "binary"),
        ((2, -2), "binary"),
    ),
    36,
)


if __name__ == "__main__":
    certify(CONFIG)
