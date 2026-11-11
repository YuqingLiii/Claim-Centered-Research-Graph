#!/usr/bin/env python3
"""Check the general SU(3) Pieri-channel formulas on all mixed weights p+q<=6.

The script recursively constructs exact representation sectors numerically from Gell--Mann
generators, decomposes 3 tensor V_(p,q) with the quadratic Casimir, and checks the closed formulas
for both lower branches.  It is an audit of the symbolic proof, not a replacement for it.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 3e-8
MAX_TOTAL_WEIGHT = 6


def entropy(values: np.ndarray | list[float]) -> float:
    return -sum(float(x) * math.log2(float(x)) for x in values if x > 1e-13)


def irrep_dimension(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir(p: int, q: int) -> float:
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3


def gell_mann() -> list[np.ndarray]:
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex),
        np.diag([1, -1, 0]).astype(complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex),
        np.diag([1, 1, -2]).astype(complex) / math.sqrt(3),
    ]


LAM = gell_mann()
FUNDAMENTAL = [matrix / 2 for matrix in LAM]


def adjoint_generators() -> list[np.ndarray]:
    structure = np.zeros((8, 8, 8), float)
    for a in range(8):
        for b in range(8):
            commutator = FUNDAMENTAL[a] @ FUNDAMENTAL[b] - FUNDAMENTAL[b] @ FUNDAMENTAL[a]
            for c in range(8):
                structure[a, b, c] = (-2j * np.trace(commutator @ FUNDAMENTAL[c])).real
    result = []
    for a in range(8):
        matrix = np.zeros((8, 8), complex)
        for b in range(8):
            for c in range(8):
                matrix[c, b] = 1j * structure[a, b, c]
        result.append(matrix)
    return result


def decompose(
    environment: list[np.ndarray], p: int, q: int
) -> dict[tuple[int, int], tuple[list[np.ndarray], np.ndarray, list[np.ndarray]]]:
    environment_dimension = environment[0].shape[0]
    total = [
        np.kron(FUNDAMENTAL[a], np.eye(environment_dimension))
        + np.kron(np.eye(3), environment[a])
        for a in range(8)
    ]
    total_casimir = sum(generator @ generator for generator in total)
    eigenvalues, eigenvectors = np.linalg.eigh(total_casimir)
    labels = [(p + 1, q)]
    if p:
        labels.append((p - 1, q + 1))
    if q:
        labels.append((p, q - 1))
    result = {}
    for label in labels:
        isometry = eigenvectors[:, np.abs(eigenvalues - casimir(*label)) < 1e-6]
        expected_dimension = irrep_dimension(*label)
        if isometry.shape[1] != expected_dimension:
            raise AssertionError(
                f"{(p, q)}->{label}: expected {expected_dimension}, got {isometry.shape[1]}"
            )
        generators = [isometry.conj().T @ total[a] @ isometry for a in range(8)]
        result[label] = (generators, isometry, total)
    return result


def build_mixed_irreps() -> dict[tuple[int, int], list[np.ndarray]]:
    representations: dict[tuple[int, int], list[np.ndarray]] = {(1, 1): adjoint_generators()}
    for total_weight in range(3, MAX_TOTAL_WEIGHT + 1):
        parent = (total_weight - 2, 1)
        child = (total_weight - 1, 1)
        representations[child] = decompose(representations[parent], *parent)[child][0]
        for q in range(2, total_weight + 1):
            p = total_weight - q
            parent = (p + 1, q - 1)
            child = (p, q)
            representations[child] = decompose(representations[parent], *parent)[child][0]
    return representations


def main() -> None:
    representations = build_mixed_irreps()
    normalized_traceless = LAM[2] / math.sqrt(2)
    checked_middle = 0
    checked_third = 0
    closest_margin = (-math.inf, None)

    for (p, q), environment in sorted(
        representations.items(), key=lambda item: (sum(item[0]), item[0])
    ):
        if not p or not q or p + q > MAX_TOTAL_WEIGHT:
            continue
        environment_dimension = irrep_dimension(p, q)
        sectors = decompose(environment, p, q)

        for branch, label in (
            ("middle", (p - 1, q + 1)),
            ("third", (p, q - 1)),
        ):
            _, isometry, total = sectors[label]
            target_dimension = isometry.shape[1]
            projector = isometry @ isometry.conj().T
            compressed_x = (
                isometry.conj().T
                @ np.kron(normalized_traceless, np.eye(environment_dimension))
                @ isometry
            )
            gram_t = (
                3
                * np.trace(compressed_x.conj().T @ compressed_x).real
                / target_dimension
            )

            fixed_u_block = projector.reshape(
                3, environment_dimension, 3, environment_dimension
            )[0, :, 0, :]
            block_spectrum = np.linalg.eigvalsh(fixed_u_block)
            nonzero = block_spectrum[block_spectrum > 1e-7]

            generic_cartan = total[2] + math.sqrt(2) * total[7]
            restricted_cartan = isometry.conj().T @ generic_cartan @ isometry
            _, weight_vectors = np.linalg.eigh(restricted_cartan)
            weight_spectra = []
            for column in range(target_dimension):
                state = (isometry @ weight_vectors[:, column]).reshape(
                    3, environment_dimension
                )
                weight_spectra.append(
                    np.linalg.eigvalsh(state @ state.conj().T)[::-1]
                )

            if branch == "middle":
                expected_t = ((2 * p - 1) * q + 5 * p - 1) / (
                    8 * (p + 1) * (q + 1)
                )
                expected_spectrum = np.array([p / (p + 1), 1 / (p + 1), 0])
                expected_maximum = p / (p + 1)
                if not np.isclose(block_spectrum[-1], expected_maximum, atol=TOL, rtol=0):
                    raise AssertionError(f"middle {(p, q)} product maximum")
                checked_middle += 1
            else:
                expected_t = ((2 * q - 1) * p + 2 * (q * q - 1)) / (
                    8 * (q + 1) * (p + q + 2)
                )
                expected_spectrum = np.array(
                    [
                        q * (p + q + 1) / ((q + 1) * (p + q + 2)),
                        (p + q + 1) / ((q + 1) * (p + q + 2)),
                        1 / (p + q + 2),
                    ]
                )
                if len(nonzero) != target_dimension:
                    raise AssertionError(f"third {(p, q)} has wrong product-block rank")
                if not np.isclose(nonzero[0], expected_spectrum[-1], atol=TOL, rtol=0):
                    raise AssertionError(f"third {(p, q)} product minimum")
                if not np.isclose(nonzero[-1], expected_spectrum[0], atol=TOL, rtol=0):
                    raise AssertionError(f"third {(p, q)} product maximum")
                checked_third += 1

            if not np.isclose(gram_t, expected_t, atol=TOL, rtol=0):
                raise AssertionError(
                    f"{branch} {(p, q)} Gram t: expected {expected_t}, got {gram_t}"
                )
            if not any(
                np.allclose(spectrum, expected_spectrum, atol=TOL, rtol=0)
                for spectrum in weight_spectra
            ):
                raise AssertionError(f"{branch} {(p, q)} extremal weight spectrum missing")

            side_entropy = entropy(expected_spectrum)
            exceptional = (1 + 8 * gram_t) / 9
            repeated = (1 - gram_t) / 9
            bell_entropy = entropy([exceptional] + [repeated] * 8)
            margin = 2 * side_entropy - bell_entropy
            if not margin < -1e-8:
                raise AssertionError(f"{branch} {(p, q)} nonnegative Bell margin {margin}")
            if margin > closest_margin[0]:
                closest_margin = (margin, (p, q, branch))

    print(f"mixed middle branches checked: {checked_middle}")
    print(f"mixed third branches checked: {checked_third}")
    print(
        "closest checked margin 2*S_min-S_Bell: "
        f"{closest_margin[0]:.12f} at {closest_margin[1]}"
    )
    print("SU(3) Pieri-channel formulas passed through total weight 6")


if __name__ == "__main__":
    main()
