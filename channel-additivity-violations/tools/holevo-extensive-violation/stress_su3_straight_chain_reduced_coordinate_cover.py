#!/usr/bin/env python3
"""Stress the six-dimensional alternative cover for the formerly seven-dimensional chain."""

import numpy as np

from scan_su3_triangular_three_face_clusters import (
    build_union,
    evaluate,
    minimum_base,
    random_weights,
)


CLUSTER = ((-2, 4), (-1, 2), (0, 0))
COVER = ((-1, 4), (0, 2), (2, -2))
LABEL_OFFSETS = (0, 1, 2, 4, 16, 64, 1024, 1_000_000)
SAMPLES = 120_000
SEED = 20260831


def main():
    environments, inputs, incidences, attached = build_union(CLUSTER)
    cover_indices = tuple(inputs.index(offset) for offset in COVER)
    coordinate_count = sum(len(incidences[index]) - 1 for index in cover_indices)
    endpoint_count = 1
    for index, incidence in enumerate(incidences):
        if index not in cover_indices:
            endpoint_count *= len(incidence)
    assert coordinate_count == 4
    assert endpoint_count == 24

    rng = np.random.default_rng(SEED)
    weights = random_weights(rng, incidences, SAMPLES)
    p_min, q_min = minimum_base(environments, inputs)
    best = None
    for p_offset in LABEL_OFFSETS:
        for q_offset in LABEL_OFFSETS:
            base_p, base_q = p_min + p_offset, q_min + q_offset
            _, gram_t, _, bell, side_matrix = evaluate(
                base_p, base_q, environments, inputs, incidences, attached, weights
            )
            margins = bell - 2 * np.min(side_matrix[list(cover_indices)], axis=0)
            index = int(np.argmin(margins))
            record = float(margins[index]), base_p, base_q, float(gram_t[index]), index
            if best is None or record[0] < best[0]:
                best = record
    print(f"cluster={CLUSTER}")
    print(f"cover={COVER}; coordinates={coordinate_count}; endpoints={endpoint_count}")
    print(f"minimum={best}")
    if best[0] <= 0:
        raise SystemExit("reduced-coordinate cover failed")
    print("reduced-coordinate six-dimensional cover survived the stress test")


if __name__ == "__main__":
    main()
