#!/usr/bin/env python3
"""Deterministic small-weight scan of inequivalent-environment SU(3)-covariant qutrit channels.

For a fixed input irrep R_(r,s), the possible irreducible Stinespring environments are the up to
three summands of bar(3) tensor R.  The script aligns their input representation bases, forms
convex mixtures of the corresponding extreme channels, and searches for a positive one-shot
conjugate-Bell defect.  A sampled minimum is only an upper bound on the true S_min, so this is a
candidate search / obstruction audit rather than a proof of global optimality.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

from check_su3_pieri_channel_formulas import (
    FUNDAMENTAL,
    LAM,
    MAX_TOTAL_WEIGHT,
    build_mixed_irreps,
    decompose,
    entropy,
    irrep_dimension,
)


RNG = np.random.default_rng(20260830)
GRID_DENOMINATOR = 20
RANDOM_STATES = 2500
MAX_INPUT_WEIGHT = 4


def occupations(n: int) -> list[tuple[int, int, int]]:
    return [(a, b, n - a - b) for a in range(n + 1) for b in range(n - a + 1)]


def symmetric_power_generators(n: int, conjugate: bool = False) -> list[np.ndarray]:
    basis = occupations(n)
    positions = {state: index for index, state in enumerate(basis)}
    one_particle = [-matrix.T for matrix in FUNDAMENTAL] if conjugate else FUNDAMENTAL
    result = []
    for generator in one_particle:
        matrix = np.zeros((len(basis), len(basis)), complex)
        for column, state_tuple in enumerate(basis):
            state = list(state_tuple)
            for i in range(3):
                for j in range(3):
                    if state[j] == 0:
                        continue
                    if i == j:
                        matrix[column, column] += generator[i, i] * state[i]
                        continue
                    target = state.copy()
                    target[j] -= 1
                    target[i] += 1
                    amplitude = math.sqrt(state[j] * (state[i] + 1))
                    matrix[positions[tuple(target)], column] += generator[i, j] * amplitude
        result.append(matrix)
    return result


def all_representations() -> dict[tuple[int, int], list[np.ndarray]]:
    result = build_mixed_irreps()
    result[(0, 0)] = [np.zeros((1, 1), complex) for _ in range(8)]
    for n in range(1, MAX_TOTAL_WEIGHT + 2):
        result[(n, 0)] = symmetric_power_generators(n)
        result[(0, n)] = symmetric_power_generators(n, conjugate=True)
    return result


def align_representation(
    branch_generators: list[np.ndarray], reference_generators: list[np.ndarray]
) -> np.ndarray:
    dimension = branch_generators[0].shape[0]
    equations = []
    identity = np.eye(dimension)
    for branch, reference in zip(branch_generators, reference_generators):
        equations.append(np.kron(identity, branch) - np.kron(reference.T, identity))
    stacked = np.concatenate(equations, axis=0)
    _, _, right = np.linalg.svd(stacked, full_matrices=False)
    intertwiner = right[-1].conj().reshape((dimension, dimension), order="F")
    left, _, right_polar = np.linalg.svd(intertwiner)
    unitary = left @ right_polar
    error = max(
        np.linalg.norm(branch @ unitary - unitary @ reference)
        for branch, reference in zip(branch_generators, reference_generators)
    )
    if error > 2e-6:
        raise AssertionError(f"intertwiner error {error}")
    return unitary


def environment_labels(r: int, s: int) -> list[tuple[int, int]]:
    labels = []
    if r:
        labels.append((r - 1, s))
    if s:
        labels.append((r + 1, s - 1))
    labels.append((r, s + 1))
    return labels


def aligned_isometries(
    r: int, s: int, representations: dict[tuple[int, int], list[np.ndarray]]
) -> tuple[list[tuple[int, int]], list[np.ndarray], list[np.ndarray]]:
    labels = environment_labels(r, s)
    raw = []
    generators = []
    for p, q in labels:
        sectors = decompose(representations[(p, q)], p, q)
        branch_generators, isometry, _ = sectors[(r, s)]
        raw.append(isometry)
        generators.append(branch_generators)
    reference = generators[0]
    aligned = [raw[0]]
    for isometry, branch_generators in zip(raw[1:], generators[1:]):
        aligned.append(isometry @ align_representation(branch_generators, reference))
    return labels, aligned, reference


def output_from_isometry(isometry: np.ndarray, environment_dimension: int, state: np.ndarray) -> np.ndarray:
    matrix = (isometry @ state).reshape(3, environment_dimension)
    return matrix @ matrix.conj().T


def adjoint_on_x(isometry: np.ndarray, environment_dimension: int, x: np.ndarray) -> np.ndarray:
    return isometry.conj().T @ np.kron(x, np.eye(environment_dimension)) @ isometry


def weight_grid(branches: int) -> list[np.ndarray]:
    if branches == 2:
        return [np.array([a, GRID_DENOMINATOR - a], float) / GRID_DENOMINATOR for a in range(GRID_DENOMINATOR + 1)]
    return [
        np.array([a, b, GRID_DENOMINATOR - a - b], float) / GRID_DENOMINATOR
        for a in range(GRID_DENOMINATOR + 1)
        for b in range(GRID_DENOMINATOR + 1 - a)
    ]


def candidate_states(generators: list[np.ndarray], dimension: int) -> np.ndarray:
    states = []
    for coefficients in (
        [1, 0, math.sqrt(2), 0, 0, 0, 0, 0],
        [0.3, -0.7, 1.1, 0.2, -0.5, 0.9, -0.4, 0.6],
    ):
        observable = sum(c * g for c, g in zip(coefficients, generators))
        _, vectors = np.linalg.eigh(observable)
        states.extend(vectors.T)
    random = RNG.normal(size=(RANDOM_STATES, dimension)) + 1j * RNG.normal(
        size=(RANDOM_STATES, dimension)
    )
    random /= np.linalg.norm(random, axis=1)[:, None]
    states.extend(random)
    return np.asarray(states)


def main() -> None:
    representations = all_representations()
    normalized_traceless = LAM[2] / math.sqrt(2)
    global_best = (-math.inf, None)
    smallest_purity_surplus = (math.inf, None)
    scanned_inputs = 0
    scanned_mixtures = 0

    for total_weight in range(1, MAX_INPUT_WEIGHT + 1):
        for r in range(total_weight + 1):
            s = total_weight - r
            if (r, s) not in representations:
                continue
            labels, isometries, generators = aligned_isometries(r, s, representations)
            dimension = irrep_dimension(r, s)
            states = candidate_states(generators, dimension)
            branch_outputs = []
            branch_adjoints = []
            for label, isometry in zip(labels, isometries):
                environment_dimension = irrep_dimension(*label)
                branch_outputs.append(
                    np.asarray(
                        [
                            output_from_isometry(isometry, environment_dimension, state)
                            for state in states
                        ]
                    )
                )
                branch_adjoints.append(
                    adjoint_on_x(isometry, environment_dimension, normalized_traceless)
                )

            local_best = (-math.inf, None)
            for weights in weight_grid(len(labels)):
                mixed_outputs = sum(
                    weight * outputs for weight, outputs in zip(weights, branch_outputs)
                )
                side_upper = min(entropy(np.linalg.eigvalsh(output)) for output in mixed_outputs)
                mixed_adjoint = sum(
                    weight * adjoint for weight, adjoint in zip(weights, branch_adjoints)
                )
                gram_t = 3 * np.trace(mixed_adjoint.conj().T @ mixed_adjoint).real / dimension
                exceptional = (1 + 8 * gram_t) / 9
                repeated = (1 - gram_t) / 9
                bell = entropy([exceptional] + [repeated] * 8)
                maximum_sampled_purity = max(
                    float(np.trace(output @ output).real) for output in mixed_outputs
                )
                purity_surplus = maximum_sampled_purity - (1 / 3 + 2 * gram_t / 3)
                if purity_surplus < smallest_purity_surplus[0]:
                    smallest_purity_surplus = (
                        purity_surplus,
                        ((r, s), tuple(float(x) for x in weights), gram_t),
                    )
                margin_upper = 2 * side_upper - bell
                record = (margin_upper, tuple(float(x) for x in weights), side_upper, bell, gram_t)
                if margin_upper > local_best[0]:
                    local_best = (margin_upper, record)
                if margin_upper > global_best[0]:
                    global_best = (margin_upper, ((r, s), labels, record))
                scanned_mixtures += 1
            scanned_inputs += 1
            margin, record = local_best
            print(
                f"input {(r, s)} dim {dimension} envs {labels}: "
                f"best sampled upper margin {margin:.12f} at weights {record[1]}"
            )

    print(f"input irreps scanned: {scanned_inputs}")
    print(f"mixture grid points scanned: {scanned_mixtures}")
    print(f"global best sampled upper margin: {global_best[0]:.12f} at {global_best[1]}")
    print(
        "smallest sampled square-root purity surplus: "
        f"{smallest_purity_surplus[0]:.12e} at {smallest_purity_surplus[1]}"
    )
    if global_best[0] <= 0:
        print("no positive sampled one-shot conjugate-Bell candidate found")
    else:
        print("positive sampled upper margin found; global S_min certification is still required")


if __name__ == "__main__":
    main()
