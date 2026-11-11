#!/usr/bin/env python3
"""Vectorized candidate/cover scan for all straight and bent three-face clusters.

This script is deliberately only a numerical route selector.  It uses the complete labelled
union incidence, tests every block-highest original side output, and searches fixed side-output
covers of size at most four.  A positive sampled margin is not promoted to a theorem.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np

from classify_su3_three_face_clusters import all_clusters, shape
from scan_su3_triangular_three_face_clusters import (
    build_union,
    evaluate,
    minimum_base,
    random_weights,
)


SAMPLES = 24_000
SEED = 20260830
OFFSETS = (0, 1, 2, 4, 8, 16, 32, 64)


def main():
    rng = np.random.default_rng(SEED)
    chains = [cluster for cluster in all_clusters() if shape(cluster) != "triangle"]
    global_best = None
    for cluster in chains:
        cluster_shape = shape(cluster)
        environments, inputs, incidences, attached = build_union(cluster)
        p_min, q_min = minimum_base(environments, inputs)
        weights = random_weights(rng, incidences, SAMPLES)
        subsets = tuple(
            subset
            for size in range(1, min(4, len(inputs)) + 1)
            for subset in combinations(range(len(inputs)), size)
        )
        subset_worst = {subset: float("inf") for subset in subsets}
        cluster_best = None
        for p_offset in OFFSETS:
            for q_offset in OFFSETS:
                base_p, base_q = p_min + p_offset, q_min + q_offset
                margin, gram_t, side, bell, side_matrix = evaluate(
                    base_p, base_q, environments, inputs, incidences, attached, weights
                )
                for subset in subsets:
                    sampled = float(
                        np.min(bell - 2 * np.min(side_matrix[list(subset)], axis=0))
                    )
                    subset_worst[subset] = min(subset_worst[subset], sampled)
                index = int(np.argmin(margin))
                record = (
                    float(margin[index]), base_p, base_q, float(gram_t[index]),
                    float(side[index]),
                    tuple(tuple(float(value) for value in block[index]) for block in weights),
                )
                if cluster_best is None or record[0] < cluster_best[0]:
                    cluster_best = record
                global_record = (record[0], cluster_shape, cluster) + record[1:]
                if global_best is None or global_record[0] < global_best[0]:
                    global_best = global_record

        print(
            f"{cluster_shape} {cluster}: I={len(inputs)}, E={len(environments)}, "
            f"samples/base={SAMPLES}",
            flush=True,
        )
        print(
            f"  input offsets/degrees: "
            f"{[(offset, len(incidence)) for offset, incidence in zip(inputs, incidences)]}",
            flush=True,
        )
        print(f"  smallest global side-filter margin: {cluster_best}", flush=True)
        for size in range(1, min(4, len(inputs)) + 1):
            candidates = [subset for subset in subsets if len(subset) == size]
            best_subset = max(candidates, key=subset_worst.get)
            selected = tuple(inputs[index] for index in best_subset)
            print(
                f"  best fixed original-side {size}-cover: {selected} "
                f"with sampled worst margin {subset_worst[best_subset]:.12f} bit",
                flush=True,
            )
    print(f"global smallest sampled margin: {global_best}", flush=True)
    if global_best[0] < 0:
        print(
            "candidate survives explicit block-highest side filter; global S_min still required",
            flush=True,
        )
    else:
        print("no straight/bent chain Bell candidate found by this scan", flush=True)


if __name__ == "__main__":
    main()
