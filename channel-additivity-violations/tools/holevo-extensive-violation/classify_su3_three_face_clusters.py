#!/usr/bin/env python3
"""Exhaustively classify connected triples of elementary SU(3) Pieri faces.

The face bases form a triangular lattice.  We quotient only by translation, not by an
unproved channel-level Weyl/conjugation equivalence, and retain the h/m/c incidence labels.
"""

from __future__ import annotations

from itertools import combinations


NEIGHBORS = ((1, 1), (-1, -1), (1, -2), (-1, 2), (2, -1), (-2, 1))
ENVIRONMENT_OFFSETS = ((0, 0), (2, -1), (1, -2))
INPUT_OFFSETS = ((1, 0), (2, -2), (0, -1))
FACE_EDGES = (
    (0, 0, "h"), (0, 2, "c"),
    (1, 0, "m"), (1, 1, "c"),
    (2, 1, "h"), (2, 2, "m"),
)


def add(first, second):
    return first[0] + second[0], first[1] + second[1]


def subtract(first, second):
    return first[0] - second[0], first[1] - second[1]


def translate_normal_form(cluster):
    return min(
        tuple(sorted(subtract(point, origin) for point in cluster))
        for origin in cluster
    )


def adjacent(first, second):
    return subtract(first, second) in NEIGHBORS


def shape(cluster):
    degrees = {
        point: sum(adjacent(point, other) for other in cluster if other != point)
        for point in cluster
    }
    edge_count = sum(degrees.values()) // 2
    if edge_count == 3:
        return "triangle"
    if edge_count != 2:
        raise AssertionError((cluster, degrees))
    center = next(point for point, degree in degrees.items() if degree == 2)
    ends = [point for point, degree in degrees.items() if degree == 1]
    first, second = subtract(ends[0], center), subtract(ends[1], center)
    return "straight" if first == (-second[0], -second[1]) else "bent"


def union_signature(cluster):
    environments = sorted(
        {add(base, offset) for base in cluster for offset in ENVIRONMENT_OFFSETS}
    )
    inputs = sorted({add(base, offset) for base in cluster for offset in INPUT_OFFSETS})
    environment_index = {label: index for index, label in enumerate(environments)}
    input_index = {label: index for index, label in enumerate(inputs)}
    edges = {
        (
            input_index[add(base, INPUT_OFFSETS[input_slot])],
            environment_index[add(base, ENVIRONMENT_OFFSETS[environment_slot])],
            branch,
        )
        for base in cluster
        for environment_slot, input_slot, branch in FACE_EDGES
    }
    input_degrees = sorted(
        sum(edge[0] == index for edge in edges) for index in range(len(inputs))
    )
    environment_degrees = sorted(
        sum(edge[1] == index for edge in edges) for index in range(len(environments))
    )
    return len(inputs), len(environments), len(edges), input_degrees, environment_degrees


def all_clusters():
    two_step_points = (
        {(0, 0)}
        | set(NEIGHBORS)
        | {add(first, second) for first in NEIGHBORS for second in NEIGHBORS}
    )
    result = set()
    for candidate in combinations(two_step_points, 3):
        cluster = set(candidate)
        if (0, 0) not in cluster:
            continue
        if not all(
            any(adjacent(point, other) for other in cluster if other != point)
            for point in cluster
        ):
            continue
        result.add(translate_normal_form(cluster))
    return sorted(result)


def main():
    clusters = all_clusters()
    grouped = {name: [] for name in ("straight", "bent", "triangle")}
    for cluster in clusters:
        grouped[shape(cluster)].append(cluster)
    assert {name: len(values) for name, values in grouped.items()} == {
        "straight": 3,
        "bent": 6,
        "triangle": 2,
    }
    print(f"translation classes: {len(clusters)}")
    for name in ("straight", "bent", "triangle"):
        print(f"{name}: {len(grouped[name])}")
        for cluster in grouped[name]:
            signature = union_signature(cluster)
            print(
                f"  {cluster}: I/E/edges={signature[0]}/{signature[1]}/{signature[2]}, "
                f"degI={signature[3]}, degE={signature[4]}"
            )


if __name__ == "__main__":
    main()
