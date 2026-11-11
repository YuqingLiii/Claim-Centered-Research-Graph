#!/usr/bin/env python3
"""Large-label stress test for the selected fixed-three side covers of all chain clusters.

This is numerical falsification pressure, not a compact-boundary proof.
"""

from __future__ import annotations

import numpy as np

from classify_su3_three_face_clusters import shape
from scan_su3_triangular_three_face_clusters import (
    build_union,
    evaluate,
    minimum_base,
    random_weights,
)


SELECTED_COVERS = {
    ((-4, 2), (-2, 1), (0, 0)): ((-3, 2), (-1, 1), (1, 0)),
    ((-3, 0), (-2, 1), (0, 0)): ((-1, -2), (-1, 1), (1, 0)),
    ((-3, 0), (-1, -1), (0, 0)): ((-2, 0), (1, 0), (2, -2)),
    ((-3, 3), (-2, 1), (0, 0)): ((-2, 3), (-1, 1), (1, 0)),
    ((-3, 3), (-1, 2), (0, 0)): ((-2, 3), (0, 2), (1, 0)),
    ((-2, -2), (-1, -1), (0, 0)): ((0, -1), (1, 0), (2, -2)),
    ((-2, 4), (-1, 2), (0, 0)): ((-1, 4), (0, 2), (1, 0)),
    ((-1, -1), (-1, 2), (0, 0)): ((0, 2), (1, 0), (2, -2)),
    ((-1, -1), (0, -3), (0, 0)): ((-1, -2), (1, 0), (2, -2)),
}
LABEL_OFFSETS = (0, 1, 2, 4, 16, 64, 1024, 1_000_000)
SAMPLES = 80_000
SEED = 20260830


def main():
    rng = np.random.default_rng(SEED)
    global_best = None
    for cluster, cover in SELECTED_COVERS.items():
        environments, inputs, incidences, attached = build_union(cluster)
        p_min, q_min = minimum_base(environments, inputs)
        cover_indices = tuple(inputs.index(offset) for offset in cover)
        weights = random_weights(rng, incidences, SAMPLES)
        cluster_best = None
        for p_offset in LABEL_OFFSETS:
            for q_offset in LABEL_OFFSETS:
                base_p, base_q = p_min + p_offset, q_min + q_offset
                _, gram_t, _, bell, side_matrix = evaluate(
                    base_p, base_q, environments, inputs, incidences, attached, weights
                )
                margins = bell - 2 * np.min(side_matrix[list(cover_indices)], axis=0)
                index = int(np.argmin(margins))
                record = (
                    float(margins[index]), base_p, base_q, float(gram_t[index]),
                    tuple(tuple(float(value) for value in block[index]) for block in weights),
                )
                if cluster_best is None or record[0] < cluster_best[0]:
                    cluster_best = record
        print(
            f"{shape(cluster)} {cluster}: cover={cover}; minimum={cluster_best}",
            flush=True,
        )
        global_record = (cluster_best[0], shape(cluster), cluster) + cluster_best[1:]
        if global_best is None or global_record[0] < global_best[0]:
            global_best = global_record
    print(f"global minimum: {global_best}", flush=True)
    if global_best[0] <= 0:
        raise SystemExit("at least one selected fixed-three cover failed the stress test")
    print("all nine selected fixed-three covers survived the large-label stress test", flush=True)


if __name__ == "__main__":
    main()
