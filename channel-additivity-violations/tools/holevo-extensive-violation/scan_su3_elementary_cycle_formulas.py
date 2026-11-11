#!/usr/bin/env python3
"""Formula-only scan of translated elementary SU(3) Pieri cycles."""

from __future__ import annotations

import numpy as np


MAX_BASE_WEIGHT = 50
GRID_DENOMINATOR = 30


def dimension(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) / 2


def environment_barycenter(r, s):
    d = dimension(r, s)
    result = {}
    if r:
        result["h"] = dimension(r - 1, s) / (3 * d)
    if s:
        result["m"] = dimension(r + 1, s - 1) / (3 * d)
    result["c"] = dimension(r, s + 1) / (3 * d)
    return result


def branch_data(p, q):
    environment_dimension = dimension(p, q)
    dimensions = {"h": dimension(p + 1, q)}
    if p:
        dimensions["m"] = dimension(p - 1, q + 1)
    if q:
        dimensions["c"] = dimension(p, q - 1)
    contractions = {
        branch: 3 * input_dimension / (8 * environment_dimension) - 1 / 8
        for branch, input_dimension in dimensions.items()
    }
    return environment_dimension, dimensions, contractions


def cross_numerator(p, q, first, second):
    environment_dimension, dimensions, contractions = branch_data(p, q)
    remaining = set(dimensions) - {first, second}
    if remaining:
        omitted = next(iter(remaining))
        pair_numerator = (
            3 * environment_dimension
            - 2 * dimensions[omitted]
            + dimensions[omitted] * contractions[omitted]
        )
    else:
        pair_numerator = 3 * environment_dimension
    return (
        pair_numerator
        - dimensions[first] * contractions[first]
        - dimensions[second] * contractions[second]
    )


def mixture_t(r, s, weights):
    center = environment_barycenter(r, s)
    return (sum(weights[key] * weights[key] / center[key] for key in center) - 1) / 8


def extreme_rows(r, s):
    rows = {}
    if r:
        rows["h"] = np.array([1.0, 0.0, 0.0])
    if s:
        rows["m"] = np.array([1 / (r + 2), (r + 1) / (r + 2), 0.0])
    rows["c"] = np.array(
        [
            1 / (r + s + 3),
            (r + s + 2) / ((s + 2) * (r + s + 3)),
            (s + 1) * (r + s + 2) / ((s + 2) * (r + s + 3)),
        ]
    )
    return rows


def entropy_rows(probabilities):
    safe = np.where(probabilities > 0, probabilities, 1)
    return -(np.where(probabilities > 0, probabilities * np.log2(safe), 0)).sum(axis=-1)


def main() -> None:
    axis = np.linspace(0, 1, GRID_DENOMINATOR + 1)
    x, y, z = np.meshgrid(axis, axis, axis, indexing="ij")
    global_best = (-np.inf, None)
    checked = 0

    for total in range(2, MAX_BASE_WEIGHT + 1):
        for p in range(total - 1):
            q = total - p
            if q < 2:
                continue
            r1, r2, r3 = (p + 1, q), (p + 2, q - 2), (p, q - 1)
            dimensions = [dimension(*r1), dimension(*r2), dimension(*r3)]
            total_dimension = sum(dimensions)

            t1 = mixture_t(*r1, {"h": x, "m": 1 - x, "c": 0 * x})
            weights2 = {"h": 1 - y, "c": y}
            if r2[1]:
                weights2["m"] = 0 * y
            t2 = mixture_t(*r2, weights2)
            weights3 = {"m": z, "c": 1 - z}
            if r3[0]:
                weights3["h"] = 0 * z
            t3 = mixture_t(*r3, weights3)

            numerator = dimensions[0] * t1 + dimensions[1] * t2 + dimensions[2] * t3
            numerator += x * (1 - z) * cross_numerator(p, q, "h", "c")
            numerator += (1 - x) * y * cross_numerator(p + 2, q - 1, "m", "c")
            numerator += (1 - y) * z * cross_numerator(p + 1, q - 2, "h", "m")
            t = numerator / total_dimension

            rows1 = extreme_rows(*r1)
            rows2 = extreme_rows(*r2)
            rows3 = extreme_rows(*r3)
            q1 = x[..., None] * rows1["h"] + (1 - x[..., None]) * rows1["m"]
            q2 = (1 - y[..., None]) * rows2["h"] + y[..., None] * rows2["c"]
            q3 = z[..., None] * rows3["m"] + (1 - z[..., None]) * rows3["c"]
            side = np.minimum.reduce([entropy_rows(q1), entropy_rows(q2), entropy_rows(q3)])
            bell = entropy_rows(
                np.concatenate(
                    [((1 + 8 * t) / 9)[..., None], np.repeat(((1 - t) / 9)[..., None], 8, axis=-1)],
                    axis=-1,
                )
            )
            margin = 2 * side - bell
            index = np.unravel_index(np.argmax(margin), margin.shape)
            value = float(margin[index])
            if value > global_best[0]:
                global_best = (
                    value,
                    ((p, q), tuple(float(v[index]) for v in (x, y, z)), float(t[index]), float(side[index]), float(bell[index])),
                )
            checked += 1

    print(f"elementary cycle base weights checked: {checked}")
    print(f"largest total base weight: {MAX_BASE_WEIGHT}")
    print(f"grid points per cycle: {(GRID_DENOMINATOR + 1) ** 3}")
    print(f"global best block upper margin: {global_best[0]:.12f} at {global_best[1]}")
    if global_best[0] <= 0:
        print("formula scan found no elementary SU(3) cycle candidate")
    else:
        print("formula scan found a positive elementary-cycle block upper margin")


if __name__ == "__main__":
    main()
