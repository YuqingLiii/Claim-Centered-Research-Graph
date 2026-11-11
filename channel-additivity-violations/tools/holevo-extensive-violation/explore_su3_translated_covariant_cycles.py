#!/usr/bin/env python3
"""Scan translated elementary hexagons in the SU(3) Pieri branching graph."""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np

from check_su3_pieri_channel_formulas import LAM, entropy, irrep_dimension
from explore_su3_inequivalent_environment_mixtures import aligned_isometries, all_representations
from explore_su3_minimal_covariant_cycle import embed_environment_rows


MAX_ENVIRONMENT_WEIGHT = 6
GRID_DENOMINATOR = 30


def cycle_labels(p: int, q: int):
    environments = [(p, q), (p + 2, q - 1), (p + 1, q - 2)]
    inputs = [
        ((p + 1, q), (environments[0], environments[1])),
        ((p + 2, q - 2), (environments[1], environments[2])),
        ((p, q - 1), (environments[2], environments[0])),
    ]
    return environments, inputs


def build_data(p: int, q: int, representations):
    environments, inputs = cycle_labels(p, q)
    offsets = {}
    environment_dimension = 0
    for label in environments:
        offsets[label] = environment_dimension
        environment_dimension += irrep_dimension(*label)
    data = []
    input_dimension = 0
    for input_label, incident in inputs:
        labels, isometries, generators = aligned_isometries(*input_label, representations)
        by_environment = dict(zip(labels, isometries))
        embedded = []
        for environment_label in incident:
            local_dimension = irrep_dimension(*environment_label)
            embedded.append(
                embed_environment_rows(
                    by_environment[environment_label],
                    offsets[environment_label],
                    local_dimension,
                    environment_dimension,
                )
            )
        dimension = irrep_dimension(*input_label)
        observable = generators[2] + math.sqrt(2) * generators[7]
        _, vectors = np.linalg.eigh(observable)
        highest = vectors[:, -1]
        extreme_outputs = []
        for isometry in embedded:
            matrix = (isometry @ highest).reshape(3, environment_dimension)
            extreme_outputs.append(matrix @ matrix.conj().T)
        data.append((input_dimension, dimension, embedded, extreme_outputs))
        input_dimension += dimension
    return data, input_dimension, environment_dimension


def isometry_at(data, input_dimension, environment_dimension, weights):
    result = np.zeros((3 * environment_dimension, input_dimension), complex)
    for (offset, dimension, embedded, _), weight in zip(data, weights):
        result[:, offset : offset + dimension] = (
            math.sqrt(weight) * embedded[0] + math.sqrt(1 - weight) * embedded[1]
        )
    return result


def gram_t(isometry, input_dimension, environment_dimension):
    x = LAM[2] / math.sqrt(2)
    adjoint = isometry.conj().T @ np.kron(x, np.eye(environment_dimension)) @ isometry
    return 3 * np.trace(adjoint.conj().T @ adjoint).real / input_dimension


def polynomial_coefficients(data, input_dimension, environment_dimension):
    points = [
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (0.5, 0, 0),
        (0, 0.5, 0),
        (0, 0, 0.5),
    ]
    design = []
    values = []
    for x, y, z in points:
        design.append([1, x, y, z, x * x, y * y, z * z, x * y, y * z, z * x])
        values.append(
            gram_t(
                isometry_at(data, input_dimension, environment_dimension, (x, y, z)),
                input_dimension,
                environment_dimension,
            )
        )
    numeric = np.linalg.solve(np.asarray(design), np.asarray(values))
    return [Fraction(float(value)).limit_denominator(10**7) for value in numeric]


def evaluate_polynomial(coefficients, x, y, z):
    monomials = [1, x, y, z, x * x, y * y, z * z, x * y, y * z, z * x]
    return sum(float(coefficient) * monomial for coefficient, monomial in zip(coefficients, monomials))


def main() -> None:
    representations = all_representations()
    global_best = (-math.inf, None)
    checked_cycles = 0
    skipped_cycles = 0
    for total in range(2, MAX_ENVIRONMENT_WEIGHT):
        for p in range(total - 1):
            q = total - p
            if q < 2:
                continue
            environments, inputs = cycle_labels(p, q)
            if any(label not in representations for label in environments):
                continue
            if max(irrep_dimension(*input_label) for input_label, _ in inputs) > 30:
                print(f"base {(p, q)} skipped: an input irrep exceeds dimension 30")
                skipped_cycles += 1
                continue
            data, input_dimension, environment_dimension = build_data(p, q, representations)
            coefficients = polynomial_coefficients(data, input_dimension, environment_dimension)
            local_best = (-math.inf, None)
            for i in range(GRID_DENOMINATOR + 1):
                x = i / GRID_DENOMINATOR
                for j in range(GRID_DENOMINATOR + 1):
                    y = j / GRID_DENOMINATOR
                    for k in range(GRID_DENOMINATOR + 1):
                        z = k / GRID_DENOMINATOR
                        t = evaluate_polynomial(coefficients, x, y, z)
                        bell = entropy([(1 + 8 * t) / 9] + [(1 - t) / 9] * 8)
                        side = math.inf
                        for weight, (_, _, _, extreme_outputs) in zip((x, y, z), data):
                            output = weight * extreme_outputs[0] + (1 - weight) * extreme_outputs[1]
                            side = min(side, entropy(np.linalg.eigvalsh(output)))
                        margin = 2 * side - bell
                        if margin > local_best[0]:
                            local_best = (margin, ((x, y, z), t, side, bell))
                        if margin > global_best[0]:
                            global_best = (
                                margin,
                                ((p, q), (input_dimension, environment_dimension), local_best[1]),
                            )
            print(
                f"base {(p, q)} dims {(input_dimension, environment_dimension)}: "
                f"best block upper margin {local_best[0]:.12f}; coefficients "
                f"{[str(value) for value in coefficients]}"
            )
            checked_cycles += 1
    print(f"translated elementary cycles checked: {checked_cycles}")
    print(f"larger cycles skipped before dense-SVD alignment: {skipped_cycles}")
    print(f"global best block upper margin: {global_best[0]:.12f} at {global_best[1]}")
    if global_best[0] <= 0:
        print("no translated elementary SU(3) cycle candidate found")
    else:
        print("positive translated-cycle block upper margin found")


if __name__ == "__main__":
    main()
