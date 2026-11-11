#!/usr/bin/env python3
"""Explore the smallest six-edge SU(3) input/environment branching cycle.

The environment vertices are (0,2), (2,1), (1,0), and the input vertices are (1,2), (2,0),
(0,1).  Each input irrep is embedded into the two incident environment products.  This is the
first reducible-input covariant family not covered by a one-center Pieri-star theorem.
"""

from __future__ import annotations

import math

import numpy as np

from check_su3_pieri_channel_formulas import LAM, entropy, irrep_dimension
from explore_su3_inequivalent_environment_mixtures import (
    RNG,
    aligned_isometries,
    all_representations,
    output_from_isometry,
)


GRID_DENOMINATOR = 30
RANDOM_STATES = 12000


ENVIRONMENTS = [(0, 2), (2, 1), (1, 0)]
INPUTS = [
    ((1, 2), ((0, 2), (2, 1))),
    ((2, 0), ((2, 1), (1, 0))),
    ((0, 1), ((1, 0), (0, 2))),
]


def embed_environment_rows(
    local: np.ndarray, environment_offset: int, local_environment_dimension: int, total_environment_dimension: int
) -> np.ndarray:
    result = np.zeros((3 * total_environment_dimension, local.shape[1]), complex)
    for output in range(3):
        result[
            output * total_environment_dimension
            + environment_offset : output * total_environment_dimension
            + environment_offset
            + local_environment_dimension,
            :,
        ] = local[
            output * local_environment_dimension : (output + 1) * local_environment_dimension,
            :,
        ]
    return result


def build_cycle_data():
    representations = all_representations()
    environment_offsets = {}
    total_environment_dimension = 0
    for label in ENVIRONMENTS:
        environment_offsets[label] = total_environment_dimension
        total_environment_dimension += irrep_dimension(*label)

    input_data = []
    total_input_dimension = 0
    for input_label, incident in INPUTS:
        labels, isometries, generators = aligned_isometries(*input_label, representations)
        by_environment = dict(zip(labels, isometries))
        embedded = []
        for environment_label in incident:
            local = by_environment[environment_label]
            local_environment_dimension = irrep_dimension(*environment_label)
            embedded.append(
                embed_environment_rows(
                    local,
                    environment_offsets[environment_label],
                    local_environment_dimension,
                    total_environment_dimension,
                )
            )
        dimension = irrep_dimension(*input_label)
        input_data.append(
            {
                "label": input_label,
                "incident": incident,
                "isometries": embedded,
                "generators": generators,
                "offset": total_input_dimension,
                "dimension": dimension,
            }
        )
        total_input_dimension += dimension
    return input_data, total_input_dimension, total_environment_dimension


def build_isometry(input_data, total_input_dimension, total_environment_dimension, weights):
    isometry = np.zeros((3 * total_environment_dimension, total_input_dimension), complex)
    for data, weight in zip(input_data, weights):
        start = data["offset"]
        stop = start + data["dimension"]
        isometry[:, start:stop] = (
            math.sqrt(weight) * data["isometries"][0]
            + math.sqrt(1 - weight) * data["isometries"][1]
        )
    error = np.linalg.norm(isometry.conj().T @ isometry - np.eye(total_input_dimension))
    if error > 2e-7:
        raise AssertionError(f"cycle isometry error {error}")
    return isometry


def channel_output(isometry, total_environment_dimension, state):
    matrix = (isometry @ state).reshape(3, total_environment_dimension)
    return matrix @ matrix.conj().T


def bell_entropy_from_isometry(isometry, total_input_dimension, total_environment_dimension):
    x = LAM[2] / math.sqrt(2)
    adjoint = isometry.conj().T @ np.kron(x, np.eye(total_environment_dimension)) @ isometry
    t = 3 * np.trace(adjoint.conj().T @ adjoint).real / total_input_dimension
    bell = entropy([(1 + 8 * t) / 9] + [(1 - t) / 9] * 8)
    return t, bell


def exact_gram_polynomial(x, y, z):
    return (
        41 / 128
        - 15 * x / 64
        - 3 * y / 16
        + 9 * z / 64
        + 105 * x * x / 128
        + 9 * y * y / 40
        + 9 * z * z / 128
        - 3 * x * y / 16
        - 3 * y * z / 16
        - 15 * z * x / 64
    )


def highest_weight_states(input_data, total_input_dimension):
    result = []
    for data in input_data:
        observable = data["generators"][2] + math.sqrt(2) * data["generators"][7]
        _, vectors = np.linalg.eigh(observable)
        state = np.zeros(total_input_dimension, complex)
        state[data["offset"] : data["offset"] + data["dimension"]] = vectors[:, -1]
        result.append(state)
    return result


def main() -> None:
    input_data, total_input_dimension, total_environment_dimension = build_cycle_data()
    highest = highest_weight_states(input_data, total_input_dimension)
    best = (-math.inf, None)

    for i in range(GRID_DENOMINATOR + 1):
        for j in range(GRID_DENOMINATOR + 1):
            for k in range(GRID_DENOMINATOR + 1):
                weights = (i / GRID_DENOMINATOR, j / GRID_DENOMINATOR, k / GRID_DENOMINATOR)
                isometry = build_isometry(
                    input_data, total_input_dimension, total_environment_dimension, weights
                )
                t, bell = bell_entropy_from_isometry(
                    isometry, total_input_dimension, total_environment_dimension
                )
                if not np.isclose(t, exact_gram_polynomial(*weights), atol=3e-8, rtol=0):
                    raise AssertionError(("cycle Gram polynomial", weights, t))
                side_upper = min(
                    entropy(
                        np.linalg.eigvalsh(
                            channel_output(isometry, total_environment_dimension, state)
                        )
                    )
                    for state in highest
                )
                margin_upper = 2 * side_upper - bell
                if margin_upper > best[0]:
                    best = (margin_upper, (weights, t, bell, side_upper))

    weights, _, _, _ = best[1]
    isometry = build_isometry(
        input_data, total_input_dimension, total_environment_dimension, weights
    )
    random = RNG.normal(size=(RANDOM_STATES, total_input_dimension)) + 1j * RNG.normal(
        size=(RANDOM_STATES, total_input_dimension)
    )
    random /= np.linalg.norm(random, axis=1)[:, None]
    sampled_side = min(
        entropy(
            np.linalg.eigvalsh(channel_output(isometry, total_environment_dimension, state))
        )
        for state in random
    )
    _, bell = bell_entropy_from_isometry(
        isometry, total_input_dimension, total_environment_dimension
    )

    print(f"cycle input dimension: {total_input_dimension}")
    print(f"cycle environment dimension: {total_environment_dimension}")
    print(f"weight grid points checked: {(GRID_DENOMINATOR + 1) ** 3}")
    print(f"best block-highest upper margin: {best[0]:.12f} at {best[1]}")
    print(f"random states checked at best point: {RANDOM_STATES}")
    print(f"best-point sampled random side entropy: {sampled_side:.12f}")
    print(f"best-point sampled random margin: {2 * sampled_side - bell:.12f}")
    if best[0] <= 0:
        print("minimal SU(3) covariant cycle has no block-certified positive Bell candidate")
    else:
        print("positive block upper margin found; global side minimum still requires certification")


if __name__ == "__main__":
    main()
