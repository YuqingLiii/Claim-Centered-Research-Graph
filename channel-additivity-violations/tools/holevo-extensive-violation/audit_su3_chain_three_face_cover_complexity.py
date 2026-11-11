#!/usr/bin/env python3
"""Audit coordinate and endpoint counts for selected chain-cluster side covers."""

from math import prod

from classify_su3_three_face_clusters import shape
from scan_su3_triangular_three_face_clusters import build_union
from stress_su3_chain_three_face_fixed_three_covers import SELECTED_COVERS


def main():
    for cluster, cover in SELECTED_COVERS.items():
        _, inputs, incidences, _ = build_union(cluster)
        degrees = {offset: len(incidence) for offset, incidence in zip(inputs, incidences)}
        coordinate_count = sum(degrees[offset] - 1 for offset in cover)
        endpoint_count = prod(degrees[offset] for offset in inputs if offset not in cover)
        retained = {
            offset: tuple(branch for _, branch in incidences[inputs.index(offset)])
            for offset in cover
        }
        print(
            f"{shape(cluster)} {cluster}: coordinates={coordinate_count}; "
            f"NVAR={coordinate_count + 2}; endpoints={endpoint_count}; retained={retained}"
        )


if __name__ == "__main__":
    main()
