#!/usr/bin/env python3
"""Formula scan for two adjacent elementary SU(3) Pieri faces.

Three input-block weights are eliminated exactly by separate convexity, leaving
12 endpoint patterns.  The scan retains the two outer weights of the added
face and compactifies the two unbounded representation labels.
"""

from __future__ import annotations

import itertools

from certify_su3_all_elementary_cycles import (
    branch_data,
    cross_numerator,
    dimension,
    environment_barycenter,
)


COMPACT_GRID = 31
WEIGHT_GRID = 101


ENVIRONMENT_OFFSETS = ((0, 0), (2, -1), (1, -2), (1, 1), (3, 0))
INPUT_OFFSETS = ((1, 0), (2, -2), (0, -1), (2, 1), (3, -1))
INCIDENCES = (
    ((0, "h"), (1, "m"), (3, "c")),
    ((1, "c"), (2, "h")),
    ((2, "m"), (0, "c")),
    ((3, "h"), (4, "m")),
    ((4, "c"), (1, "h")),
)
ENDPOINT_PATTERNS = tuple(itertools.product(("h", "m", "c"), (0, 1), (0, 1)))


def label(base_p, base_q, offset):
    return base_p + offset[0], base_q + offset[1]


def mixture_t(input_label, weights):
    center = environment_barycenter(*input_label)
    return (sum(weights.get(key, 0) ** 2 / center[key] for key in center) - 1) / 8


def adjacent_t(p, q, pattern, u, v):
    environments = [label(p, q, offset) for offset in ENVIRONMENT_OFFSETS]
    inputs = [label(p, q, offset) for offset in INPUT_OFFSETS]
    weights = [
        {key: int(key == pattern[0]) for _, key in INCIDENCES[0]},
        {INCIDENCES[1][0][1]: pattern[1], INCIDENCES[1][1][1]: 1 - pattern[1]},
        {INCIDENCES[2][0][1]: pattern[2], INCIDENCES[2][1][1]: 1 - pattern[2]},
        {INCIDENCES[3][0][1]: u, INCIDENCES[3][1][1]: 1 - u},
        {INCIDENCES[4][0][1]: v, INCIDENCES[4][1][1]: 1 - v},
    ]
    numerator = sum(
        dimension(*input_label) * mixture_t(input_label, block_weights)
        for input_label, block_weights in zip(inputs, weights)
    )
    for environment_index, environment_label in enumerate(environments):
        attached = [
            (branch, weights[input_index][branch])
            for input_index, incidences in enumerate(INCIDENCES)
            for candidate_index, branch in incidences
            if candidate_index == environment_index
        ]
        for first in range(len(attached)):
            for second in range(first + 1, len(attached)):
                numerator += (
                    attached[first][1]
                    * attached[second][1]
                    * cross_numerator(
                        *environment_label, attached[first][0], attached[second][0]
                    )
                )
    return numerator / sum(dimension(*input_label) for input_label in inputs)


def entropy(probabilities):
    import numpy as np

    probabilities = np.asarray(probabilities)
    safe = np.where(probabilities > 0, probabilities, 1)
    return -np.sum(
        np.where(probabilities > 0, probabilities * np.log2(safe), 0), axis=-1
    )


def main() -> None:
    import numpy as np

    axis = np.linspace(0, 1, WEIGHT_GRID)
    u, v = np.meshgrid(axis, axis, indexing="ij")
    best = (float("inf"), None)
    pattern_counts = np.zeros(len(ENDPOINT_PATTERNS), dtype=np.int64)
    for a_index in range(COMPACT_GRID):
        a = a_index / COMPACT_GRID
        p = a / (1 - a)
        for b_index in range(COMPACT_GRID):
            b = b_index / COMPACT_GRID
            q = 2 + b / (1 - b)
            curves = []
            for pattern in ENDPOINT_PATTERNS:
                f00 = adjacent_t(p, q, pattern, 0, 0)
                f10 = adjacent_t(p, q, pattern, 1, 0)
                f01 = adjacent_t(p, q, pattern, 0, 1)
                fh0 = adjacent_t(p, q, pattern, 0.5, 0)
                f0h = adjacent_t(p, q, pattern, 0, 0.5)
                f11 = adjacent_t(p, q, pattern, 1, 1)
                u2 = 2 * (f10 + f00 - 2 * fh0)
                u1 = f10 - f00 - u2
                v2 = 2 * (f01 + f00 - 2 * f0h)
                v1 = f01 - f00 - v2
                uv = f11 - f00 - u2 - u1 - v2 - v1
                curves.append(f00 + u1 * u + u2 * u * u + v1 * v + v2 * v * v + uv * u * v)
            curves = np.asarray(curves)
            maximizing_pattern = np.argmax(curves, axis=0)
            pattern_counts += np.bincount(
                maximizing_pattern.ravel(), minlength=len(ENDPOINT_PATTERNS)
            )
            t = np.take_along_axis(curves, maximizing_pattern[None, :, :], axis=0)[0]

            first_probability = u + (1 - u) / (p + 4)
            first_side = entropy(
                np.stack([first_probability, 1 - first_probability, np.zeros_like(u)], axis=-1)
            )
            r, s = p + 3, q - 1
            c1 = 1 / (r + s + 3)
            c2 = (r + s + 2) / ((s + 2) * (r + s + 3))
            c3 = (s + 1) * (r + s + 2) / ((s + 2) * (r + s + 3))
            second_side = entropy(
                np.stack([v * c1 + 1 - v, v * c2, v * c3], axis=-1)
            )
            side = np.minimum(first_side, second_side)
            bell = entropy(
                np.concatenate(
                    [
                        ((1 + 8 * t) / 9)[..., None],
                        np.repeat(((1 - t) / 9)[..., None], 8, axis=-1),
                    ],
                    axis=-1,
                )
            )
            margin = bell - 2 * side
            index = np.unravel_index(np.argmin(margin), margin.shape)
            if margin[index] < best[0]:
                best = (
                    float(margin[index]),
                    (
                        p,
                        q,
                        float(u[index]),
                        float(v[index]),
                        float(t[index]),
                        ENDPOINT_PATTERNS[int(maximizing_pattern[index])],
                    ),
                )

    print(f"compact p/q grid: {COMPACT_GRID} by {COMPACT_GRID}")
    print(f"retained-weight grid: {WEIGHT_GRID} by {WEIGHT_GRID}")
    print(f"convex endpoint patterns per p/q point: {len(ENDPOINT_PATTERNS)}")
    print(
        "patterns active on the formula grid: "
        + repr(
            [
                (ENDPOINT_PATTERNS[index], int(count))
                for index, count in enumerate(pattern_counts)
                if count
            ]
        )
    )
    print(f"smallest Bell-minus-twice-side margin: {best[0]:.12f} bit at {best[1]}")
    if best[0] > 0:
        print("no adjacent-elementary-face Bell candidate found on the formula grid")
    else:
        print("adjacent-elementary-face formula grid found a candidate")


if __name__ == "__main__":
    main()
