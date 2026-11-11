#!/usr/bin/env python3
"""Non-certificate probes for shorter remaining SU(3) three-face covers.

This program uses floating-point sampling only.  Its purpose is route selection:
it evaluates the *endpoint-reduced* Gram maximum, rather than the original
channel Gram value, for candidate fixed-side covers.  No output of this file is
an all-parameter certificate.
"""

from __future__ import annotations

import argparse
from itertools import combinations

import numpy as np

from certify_su3_triangular_three_face_clusters import (
    Configuration,
    build_union,
    endpoint_patterns,
    gram_t,
    retained_side_distributions,
)


TRIANGLE = ((-2, 1), (-1, -1), (0, 0))
BENT = ((-3, 0), (-2, 1), (0, 0))


def entropy_rows(probabilities):
    values = np.asarray(probabilities, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(values > 0, -values * np.log(values), 0.0)
    return np.sum(terms, axis=-1)


def endpoint_quadratic_coefficients(config, union, pattern, P, Q):
    """Interpolate the endpoint Gram polynomial for binary retained blocks.

    There is one local quadratic per retained coordinate and one bilinear term
    per pair of distinct retained blocks, with no higher cross interaction.
    """
    count = len(config.retained)
    zero = [0.0] * count
    constant = float(gram_t(config, union, pattern, P, Q, zero))
    linear = np.zeros(count)
    quadratic = np.zeros(count)
    at_one = []
    for axis in range(count):
        one = list(zero)
        half = list(zero)
        one[axis] = 1.0
        half[axis] = 0.5
        value_one = float(gram_t(config, union, pattern, P, Q, one))
        value_half = float(gram_t(config, union, pattern, P, Q, half))
        quadratic[axis] = 2 * (value_one + constant - 2 * value_half)
        linear[axis] = value_one - constant - quadratic[axis]
        at_one.append(value_one)
    cross = np.zeros((count, count))
    for first, second in combinations(range(count), 2):
        both = list(zero)
        both[first] = both[second] = 1.0
        cross[first, second] = (
            float(gram_t(config, union, pattern, P, Q, both))
            - at_one[first] - at_one[second] + constant
        )
    return constant, linear, quadratic, cross


def endpoint_gram_max(config, union, patterns, P, Q, coordinates):
    samples = np.asarray(coordinates, dtype=float)
    maximum = np.full(len(samples), -np.inf)
    winners = np.zeros(len(samples), dtype=int)
    for pattern_index, pattern in enumerate(patterns):
        constant, linear, quadratic, cross = endpoint_quadratic_coefficients(
            config, union, pattern, P, Q
        )
        values = constant + samples @ linear + (samples * samples) @ quadratic
        for first, second in combinations(range(samples.shape[1]), 2):
            values += cross[first, second] * samples[:, first] * samples[:, second]
        improved = values > maximum
        maximum[improved] = values[improved]
        winners[improved] = pattern_index
    return maximum, winners


def binary_side_entropies(config, union, P, Q, coordinates):
    samples = np.asarray(coordinates, dtype=float)
    retained = dict(config.retained)
    result = []
    axis = 0
    # Fetching the two endpoint distributions through the exact public helper
    # avoids duplicating branch-order or shifted-label conventions.
    for offset, incidence in zip(union[1], union[2]):
        if offset not in retained:
            continue
        if retained[offset] != "binary":
            raise ValueError("this exploratory interpolator expects binary retained blocks")
        low = retained_side_distributions(
            config, union, P, Q, [0.0] * axis + [0.0] + [0.0] * (len(retained) - axis - 1)
        )[axis]
        high = retained_side_distributions(
            config, union, P, Q, [0.0] * axis + [1.0] + [0.0] * (len(retained) - axis - 1)
        )[axis]
        x = samples[:, axis, None]
        distributions = (1 - x) * np.asarray(low) + x * np.asarray(high)
        result.append(entropy_rows(distributions))
        axis += 1
    return np.asarray(result)


def margins(config, P, Q, coordinates):
    union = build_union(config.cluster)
    _, patterns = endpoint_patterns(union[1], union[2], dict(config.retained))
    t_values, winners = endpoint_gram_max(config, union, patterns, P, Q, coordinates)
    isotropic = np.column_stack(((1 + 8 * t_values) / 9, (1 - t_values) / 9))
    bell = -isotropic[:, 0] * np.log(isotropic[:, 0])
    bell -= 8 * isotropic[:, 1] * np.log(isotropic[:, 1])
    sides = binary_side_entropies(config, union, P, Q, coordinates)
    return bell - 2 * np.min(sides, axis=0), t_values, winners, patterns


def mixed_coordinates(rng, count, dimension):
    ordinary = rng.random((count // 2, dimension))
    corner = rng.beta(0.18, 0.18, size=(count - len(ordinary), dimension))
    anchors = np.asarray(
        list(np.ndindex(*(2,) * dimension)) + [(0.5,) * dimension], dtype=float
    )
    return np.vstack((ordinary, corner, anchors))


def probe_bent(samples):
    config = Configuration(
        "weakest-bent-fixed-two-probe",
        BENT,
        (((-1, 1), "binary"), ((1, 0), "binary")),
        72,
    )
    rng = np.random.default_rng(20260830)
    coordinates = mixed_coordinates(rng, samples, 2)
    coordinates = np.vstack((coordinates, np.asarray(((0.0, 0.7),))))
    label_pairs = (
        (0, 0), (0, 1), (0, 2), (0, 16), (0, 10**6),
        (1, 0), (1, 1), (2, 0), (16, 0), (10**6, 0),
        (16, 16), (10**6, 10**6),
    )
    for P, Q in label_pairs:
        gap, t_values, winners, patterns = margins(config, P, Q, coordinates)
        index = int(np.argmin(gap))
        print(
            f"bent P={P} Q={Q}: min={gap[index]:.12g}; "
            f"weights={tuple(coordinates[index])}; t={t_values[index]:.12g}; "
            f"pattern={patterns[winners[index]]}"
        )


def probe_triangle(samples):
    union = build_union(TRIANGLE)
    binary_offsets = tuple(
        offset for offset, incidence in zip(union[1], union[2]) if len(incidence) == 2
    )
    covers = tuple(combinations(binary_offsets, 3))
    rng = np.random.default_rng(20260830)
    coordinates = mixed_coordinates(rng, samples, 3)
    label_values = (0, 1, 4, 64, 10**6)
    worst = {cover: (float("inf"), None) for cover in covers}
    for P in label_values:
        for Q in label_values:
            for cover in covers:
                config = Configuration(
                    "input-triangle-three-side-probe",
                    TRIANGLE,
                    tuple((offset, "binary") for offset in cover),
                    24,
                )
                gap, t_values, winners, patterns = margins(config, P, Q, coordinates)
                index = int(np.argmin(gap))
                if gap[index] < worst[cover][0]:
                    worst[cover] = (
                        float(gap[index]),
                        (P, Q, tuple(coordinates[index]), float(t_values[index]), patterns[winners[index]]),
                    )
    for cover, record in sorted(worst.items(), key=lambda item: item[1][0], reverse=True):
        print(f"triangle cover={cover}: sampled endpoint-reduced worst={record}")

    sector_probes = (
        (
            "low-P",
            ((-1, 1), (1, 0), (2, -2)),
            (0, 1, 4, 16, 32, 48, 63),
        ),
        (
            "high-P",
            ((-2, 0), (1, -3), (1, 0)),
            (63, 64, 128, 4096, 10**6),
        ),
    )
    q_values = (0, 1, 4, 16, 48, 64, 128, 1024, 10**6)
    for name, cover, p_values in sector_probes:
        config = Configuration(
            f"input-triangle-{name}-probe",
            TRIANGLE,
            tuple((offset, "binary") for offset in cover),
            24,
        )
        sector_worst = (float("inf"), None)
        for P in p_values:
            for Q in q_values:
                gap, t_values, winners, patterns = margins(
                    config, P, Q, coordinates
                )
                index = int(np.argmin(gap))
                if gap[index] < sector_worst[0]:
                    sector_worst = (
                        float(gap[index]),
                        (
                            P,
                            Q,
                            tuple(coordinates[index]),
                            float(t_values[index]),
                            patterns[winners[index]],
                        ),
                    )
        print(f"triangle sector={name} cover={cover}: sampled worst={sector_worst}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("bent", "triangle"))
    parser.add_argument("--samples", type=int, default=4000)
    arguments = parser.parse_args()
    if arguments.mode == "bent":
        probe_bent(arguments.samples)
    else:
        probe_triangle(arguments.samples)


if __name__ == "__main__":
    main()
