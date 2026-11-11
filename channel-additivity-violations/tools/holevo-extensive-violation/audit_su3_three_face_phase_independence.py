#!/usr/bin/env python3
"""Verify phase independence for every connected three-face incidence union."""

from certify_su3_triangular_three_face_clusters import build_union
from classify_su3_three_face_clusters import all_clusters, shape


def main():
    for cluster in all_clusters():
        _, inputs, incidences, _ = build_union(cluster)
        environment_sets = [{index for index, _ in incidence} for incidence in incidences]
        maximum = max(
            len(environment_sets[first] & environment_sets[second])
            for first in range(len(inputs))
            for second in range(first)
        )
        if maximum > 1:
            raise AssertionError((cluster, maximum))
        print(f"{shape(cluster)} {cluster}: maximum shared environments per input pair={maximum}")
    print("all 11 connected three-face classes are phase-independent")


if __name__ == "__main__":
    main()
