#!/usr/bin/env python3
"""Deterministic audit of the SU(3) decomposition 3 x 8 = 15 + 6bar + 3.

Run with the repository workspace Python runtime, which provides NumPy.
The calculation constructs the fundamental and adjoint generators, diagonalizes the total
quadratic Casimir, and checks the rational Gram/product-overlap data used in the proof artifact.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 2e-10


def entropy(values: np.ndarray | list[float]) -> float:
    return -sum(float(x) * math.log2(float(x)) for x in values if x > 1e-14)


def close(actual: np.ndarray | float, expected: np.ndarray | float, label: str) -> None:
    if not np.allclose(actual, expected, atol=TOL, rtol=0):
        raise AssertionError(f"{label}: expected {expected}, got {actual}")


def gell_mann() -> list[np.ndarray]:
    matrices = [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex),
        np.diag([1, -1, 0]).astype(complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex),
        np.diag([1, 1, -2]).astype(complex) / math.sqrt(3),
    ]
    return matrices


def main() -> None:
    lam = gell_mann()
    fundamental = [matrix / 2 for matrix in lam]

    structure = np.zeros((8, 8, 8), float)
    for a in range(8):
        for b in range(8):
            commutator = fundamental[a] @ fundamental[b] - fundamental[b] @ fundamental[a]
            for c in range(8):
                structure[a, b, c] = (-2j * np.trace(commutator @ fundamental[c])).real

    adjoint: list[np.ndarray] = []
    for a in range(8):
        matrix = np.zeros((8, 8), complex)
        for b in range(8):
            for c in range(8):
                matrix[c, b] = 1j * structure[a, b, c]
        adjoint.append(matrix)

    total = [
        np.kron(fundamental[a], np.eye(8)) + np.kron(np.eye(3), adjoint[a])
        for a in range(8)
    ]
    casimir = sum(generator @ generator for generator in total)
    eigenvalues, eigenvectors = np.linalg.eigh(casimir)

    sectors = {
        "3": (4 / 3, 3),
        "6bar": (10 / 3, 6),
        "15": (16 / 3, 15),
    }

    print("Casimir sectors")
    data: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    normalized_x = lam[2] / math.sqrt(2)
    for name, (casimir_value, dimension) in sectors.items():
        isometry = eigenvectors[:, np.abs(eigenvalues - casimir_value) < 1e-8]
        if isometry.shape[1] != dimension:
            raise AssertionError(f"{name}: wrong multiplicity {isometry.shape[1]}")
        projector = isometry @ isometry.conj().T
        compressed = isometry.conj().T @ np.kron(normalized_x, np.eye(8)) @ isometry
        norm_squared = np.trace(compressed.conj().T @ compressed).real
        gram_t = 3 * norm_squared / dimension
        fixed_u_block = projector.reshape(3, 8, 3, 8)[0, :, 0, :]
        product_spectrum = np.linalg.eigvalsh(fixed_u_block)
        data[name] = (isometry, projector)
        print(
            f"  {name}: dimension={dimension}, gram_t={gram_t:.12f}, "
            f"product_block={np.round(product_spectrum, 12).tolist()}"
        )

        if name == "3":
            close(gram_t, 1 / 64, "3 Gram contraction")
            close(
                product_spectrum,
                np.array([0, 0, 0, 0, 0, 1 / 4, 3 / 8, 3 / 8]),
                "3 product block",
            )
        elif name == "6bar":
            close(gram_t, 5 / 32, "6bar Gram contraction")
            close(
                product_spectrum,
                np.array([0, 0, 0, 1 / 4, 1 / 4, 1 / 2, 1 / 2, 1 / 2]),
                "6bar product block",
            )
        else:
            close(product_spectrum[-1], 1, "15 product vector")

    # Diagonalize a generic Cartan element in each multiplicity-free sector.  Its weight vectors
    # expose the exact output spectra used for the entropy equalities.
    generic_cartan = total[2] + math.sqrt(2) * total[7]
    print("Weight-vector output spectra")
    output_spectra: dict[str, list[np.ndarray]] = {}
    for name, (isometry, _) in data.items():
        restricted = isometry.conj().T @ generic_cartan @ isometry
        _, weights = np.linalg.eigh(restricted)
        spectra = []
        for column in range(weights.shape[1]):
            state = (isometry @ weights[:, column]).reshape(3, 8)
            spectrum = np.linalg.eigvalsh(state @ state.conj().T)[::-1]
            spectra.append(spectrum)
        output_spectra[name] = spectra
        unique = []
        for spectrum in spectra:
            rounded = tuple(np.round(spectrum, 12))
            if rounded not in unique:
                unique.append(rounded)
        print(f"  {name}: {unique}")

    close(output_spectra["3"][0], np.array([3 / 8, 3 / 8, 1 / 4]), "3 output")
    if not any(np.allclose(s, [1 / 2, 1 / 2, 0], atol=TOL, rtol=0) for s in output_spectra["6bar"]):
        raise AssertionError("6bar rank-two extremizer missing")
    if not any(np.allclose(s, [1, 0, 0], atol=TOL, rtol=0) for s in output_spectra["15"]):
        raise AssertionError("15 product output missing")

    side_three = entropy([3 / 8, 3 / 8, 1 / 4])
    bell_three = entropy([1 / 8] + [7 / 64] * 8)
    side_six = 1.0
    bell_six = entropy([1 / 4] + [3 / 32] * 8)
    print("Bell margins 2*S_min-S_Bell")
    print(f"  3: {2 * side_three - bell_three:.12f}")
    print(f"  6bar: {2 * side_six - bell_six:.12f}")
    if not 2 * side_three < bell_three or not 2 * side_six < bell_six:
        raise AssertionError("strict Bell no-go margin failed")

    print("SU(3) 3 x 8 coupling checks passed")


if __name__ == "__main__":
    main()
