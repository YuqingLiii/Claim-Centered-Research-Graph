#!/usr/bin/env python3
"""Exact checker for the recovered 300 x 300 H4 Bell instance.

This checker verifies four claims without invoking an optimizer:

1. the archived matrix and sign vectors are the frozen instance;
2. the archived signs attain the stated integer classical lower bound;
3. an exact rank-four Gram matrix over Q(sqrt(5)) attains the stated
   dimension-four vector value.
4. the Gram projector is exactly the top singular/eigenspace of ``A``.

The floating ``P`` dataset is not used to prove the Gram-matrix identities.
Instead, the exact Q(sqrt(5)) matrix is reconstructed from the integer levels
of ``A`` using the frozen level table below.  All decisive identities are then
checked with integer arithmetic after writing

    P = (X + Y sqrt(5)) / 8.

Dependencies: numpy and h5py.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from fractions import Fraction
from pathlib import Path

import h5py
import numpy as np


N = 300
D = 8
EXPECTED_MAT_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_A_SHA256 = (
    "5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5"
)
EXPECTED_CLASSICAL = 2081044153087351400
EXPECTED_VECTOR_A = 1539823299061914600
EXPECTED_VECTOR_B = 706968072319078800
EXPECTED_LAMBDA_A = 5132744330206382
EXPECTED_LAMBDA_B = 2356560241063596


# For a nonzero entry a=A_ij, first multiply this normalized value by sign(a).
# The listed pair (x,y) denotes (x+y sqrt(5))/8.  The diagonal level is included
# in the same convention: A_ii<0 and normalized P_ii=-1, hence P_ii=+1.
NORMALIZED_LEVELS = {
    0: (0, 0),
    10293655277252: (6, 0),
    21631568804130: (-1, 1),
    27105449085782: (1, 3),
    37229688645756: (2, 2),
    39431279593850: (-5, -1),
    51957372508648: (-1, 3),
    58783195593460: (2, 0),
    68008930961612: (-8, 0),
    72718584681592: (3, 1),
    77136371015016: (3, -1),
    101154567432113: (0, 2),
    124502011454782: (4, 0),
    129160051828973: (1, 1),
    159311771904990: (2, 0),
    165039882863956: (4, 0),
    176026360267662: (5, -1),
    215287571516328: (-2, 2),
}


def file_hash(path: Path, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_int64_sha256(a: np.ndarray) -> str:
    h = hashlib.sha256()
    for value in a.ravel(order="C"):
        h.update(int(value).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def exact_int_matrix(raw: np.ndarray) -> np.ndarray:
    a = np.asarray(raw)
    if a.shape != (N, N):
        raise AssertionError(f"A has shape {a.shape}, expected {(N, N)}")
    out = np.empty((N, N), dtype=np.int64)
    for index, value in np.ndenumerate(a):
        z = float(value)
        q = int(z)
        if not math.isfinite(z) or float(q) != z:
            raise AssertionError(f"A{index} is not an exact binary64 integer: {z!r}")
        out[index] = q
    return out


def exact_signs(raw: np.ndarray, name: str) -> list[int]:
    a = np.asarray(raw).reshape(-1)
    if a.size != N:
        raise AssertionError(f"{name} has length {a.size}, expected {N}")
    out = [int(x) for x in a]
    if any(x not in (-1, 1) for x in out):
        raise AssertionError(f"{name} contains an entry outside {{-1,+1}}")
    return out


def reconstruct_exact_gram(a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    levels = {abs(int(z)) for z in a.ravel()}
    if levels != set(NORMALIZED_LEVELS):
        missing = sorted(set(NORMALIZED_LEVELS) - levels)
        extra = sorted(levels - set(NORMALIZED_LEVELS))
        raise AssertionError(f"unexpected A levels; missing={missing}, extra={extra}")

    x = np.empty((N, N), dtype=np.int64)
    y = np.empty((N, N), dtype=np.int64)
    for index, value in np.ndenumerate(a):
        z = int(value)
        nx, ny = NORMALIZED_LEVELS[abs(z)]
        carrier = 1 if z >= 0 else -1
        if z == 0:
            carrier = 1
        x[index] = carrier * nx
        y[index] = carrier * ny
    return x, y


def q5_sign(real: int, radical: int) -> int:
    """Return the exact sign of ``real + radical*sqrt(5)``."""

    real = int(real)
    radical = int(radical)
    if real == 0:
        return (radical > 0) - (radical < 0)
    if radical == 0:
        return (real > 0) - (real < 0)
    if (real > 0) == (radical > 0):
        return 1 if real > 0 else -1

    # The two summands have opposite signs.  Compare their magnitudes after
    # squaring.  Equality cannot occur because sqrt(5) is irrational.
    comparison = real * real - 5 * radical * radical
    if comparison == 0:
        raise AssertionError("unexpected rational representation of zero in Q(sqrt(5))")
    if comparison > 0:
        return 1 if real > 0 else -1
    return 1 if radical > 0 else -1


def q5_determinant_4(matrix: list[list[tuple[Fraction, Fraction]]]) -> tuple[Fraction, Fraction]:
    """Leibniz determinant in Q(sqrt(5)); used only for the 4 x 4 pivot."""

    from itertools import permutations

    def add(u, v):
        return u[0] + v[0], u[1] + v[1]

    def multiply(u, v):
        return u[0] * v[0] + 5 * u[1] * v[1], u[0] * v[1] + u[1] * v[0]

    total = (Fraction(0), Fraction(0))
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        term = (Fraction(-1 if inversions % 2 else 1), Fraction(0))
        for i in range(4):
            term = multiply(term, matrix[i][perm[i]])
        total = add(total, term)
    return total


def verify_two_qubit_clifford() -> None:
    """Exact Gaussian-integer check of the four displayed Pauli strings."""

    identity_2 = np.array([[1, 0], [0, 1]], dtype=np.complex128)
    pauli_x = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
    pauli_z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
    identity_4 = np.eye(4, dtype=np.complex128)
    zero_4 = np.zeros((4, 4), dtype=np.complex128)
    gamma = [
        np.kron(pauli_x, identity_2),
        np.kron(pauli_z, identity_2),
        np.kron(pauli_y, pauli_x),
        np.kron(pauli_y, pauli_z),
    ]
    for i, gi in enumerate(gamma):
        if not np.array_equal(gi, gi.conj().T):
            raise AssertionError(f"Gamma_{i + 1} is not Hermitian")
        if not np.array_equal(gi @ gi, identity_4):
            raise AssertionError(f"Gamma_{i + 1} is not an involution")
        for j, gj in enumerate(gamma):
            target = 2 * identity_4 if i == j else zero_4
            if not np.array_equal(gi @ gj + gj @ gi, target):
                raise AssertionError(f"Clifford relation failed for {i + 1},{j + 1}")
            trace_target = 4 if i == j else 0
            if np.trace(gi @ gj) != trace_target:
                raise AssertionError(f"trace identity failed for {i + 1},{j + 1}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mat", type=Path)
    args = parser.parse_args()
    path = args.mat.resolve()

    if file_hash(path, "md5") != EXPECTED_MAT_MD5:
        raise AssertionError("MAT-file MD5 mismatch")

    with h5py.File(path, "r") as archive:
        required = {"A", "P", "ax", "by"}
        if not required.issubset(archive):
            raise AssertionError(f"missing datasets: {sorted(required - set(archive))}")
        a = exact_int_matrix(archive["A"][()])
        p_float = np.asarray(archive["P"][()], dtype=np.float64)
        ax = exact_signs(archive["ax"][()], "ax")
        by = exact_signs(archive["by"][()], "by")

    if canonical_int64_sha256(a) != EXPECTED_A_SHA256:
        raise AssertionError("canonical A SHA-256 mismatch")
    if not np.array_equal(a, a.T):
        raise AssertionError("A is not symmetric")

    classical = sum(
        int(a[i, j]) * ax[i] * by[j]
        for i in range(N)
        for j in range(N)
    )
    if classical != EXPECTED_CLASSICAL:
        raise AssertionError(f"classical witness gives {classical}")

    x, y = reconstruct_exact_gram(a)
    if not np.array_equal(x, x.T) or not np.array_equal(y, y.T):
        raise AssertionError("reconstructed P is not symmetric")
    if any(int(x[i, i]) != D or int(y[i, i]) != 0 for i in range(N)):
        raise AssertionError("reconstructed P does not have unit diagonal")

    # Exact multiplication in Q(sqrt(5)).  All intermediate values fit int64:
    # 300 * (8^2 + 5*3^2) < 2^63.
    real_part = x @ x + 5 * (y @ y)
    radical_part = x @ y + y @ x
    if not np.array_equal(real_part, (75 * D) * x):
        raise AssertionError("real part of P^2=75P failed")
    if not np.array_equal(radical_part, (75 * D) * y):
        raise AssertionError("sqrt(5) part of P^2=75P failed")

    # Stored floats are only cross-checked after the exact construction succeeds.
    p_reconstructed = (x.astype(float) + math.sqrt(5.0) * y.astype(float)) / D
    max_float_error = float(np.max(np.abs(p_reconstructed - p_float)))
    if max_float_error > 5e-15:
        raise AssertionError(f"stored P disagrees with exact P: {max_float_error}")

    nr = sum(int(a[i, j]) * int(x[i, j]) for i in range(N) for j in range(N))
    ns = sum(int(a[i, j]) * int(y[i, j]) for i in range(N) for j in range(N))
    vector_a = Fraction(nr, D)
    vector_b = Fraction(ns, D)
    if vector_a != EXPECTED_VECTOR_A or vector_b != EXPECTED_VECTOR_B:
        raise AssertionError(f"unexpected vector value: {vector_a} + {vector_b} sqrt(5)")

    # Exact spectral reduction.  Put E=P/75 and
    # lambda=(<A,P>/300)=lambda_a+lambda_b*sqrt(5).  The identity AP=lambda P
    # proves that E is an A-invariant eigenspace.  To prove this is the strict
    # top singular space without a floating eigensolver, write R=A-lambda E.
    # Then R E=0.  A direct exact row-sum bound on R^2 gives
    # ||R||_op^2 <= ||R^2||_infinity = rho^2 < lambda^2.
    lambda_a = EXPECTED_LAMBDA_A
    lambda_b = EXPECTED_LAMBDA_B
    if 300 * lambda_a != EXPECTED_VECTOR_A or 300 * lambda_b != EXPECTED_VECTOR_B:
        raise AssertionError("lambda does not equal <A,P>/300")
    if q5_sign(lambda_a, lambda_b) != 1:
        raise AssertionError("lambda is not positive")

    a_object = a.astype(object)
    x_object = x.astype(object)
    y_object = y.astype(object)
    ax_exact = a_object @ x_object
    ay_exact = a_object @ y_object
    if not np.array_equal(ax_exact, lambda_a * x_object + 5 * lambda_b * y_object):
        raise AssertionError("real part of AP=lambda P failed")
    if not np.array_equal(ay_exact, lambda_b * x_object + lambda_a * y_object):
        raise AssertionError("sqrt(5) part of AP=lambda P failed")

    lambda_sq_a = lambda_a * lambda_a + 5 * lambda_b * lambda_b
    lambda_sq_b = 2 * lambda_a * lambda_b
    a_squared = a_object @ a_object

    # Since P=(X+Y sqrt(5))/8,
    #   R^2=A^2-(lambda^2/75)P=(U+V sqrt(5))/600.
    u = 600 * a_squared - lambda_sq_a * x_object - 5 * lambda_sq_b * y_object
    v = -lambda_sq_a * y_object - lambda_sq_b * x_object
    row_sums = []
    for i in range(N):
        row_real = 0
        row_radical = 0
        for j in range(N):
            entry_sign = q5_sign(u[i, j], v[i, j])
            row_real += entry_sign * int(u[i, j])
            row_radical += entry_sign * int(v[i, j])
        row_sums.append((row_real, row_radical))
    if len(set(row_sums)) != 1:
        raise AssertionError("exact row sums of |R^2| are not constant")
    rho_sq_num_a, rho_sq_num_b = row_sums[0]
    if q5_sign(
        600 * lambda_sq_a - rho_sq_num_a,
        600 * lambda_sq_b - rho_sq_num_b,
    ) != 1:
        raise AssertionError("exact row-sum bound does not prove rho^2 < lambda^2")

    # An unambiguous coordinate realization can use the positive Cholesky factor
    # of this pivot Gram matrix.  Nonzero determinant verifies it is a basis.
    pivot = [0, 1, 2, 3]
    pivot_matrix = [
        [
            (Fraction(int(x[i, j]), D), Fraction(int(y[i, j]), D))
            for j in pivot
        ]
        for i in pivot
    ]
    pivot_det = q5_determinant_4(pivot_matrix)
    if pivot_det == (0, 0):
        raise AssertionError("declared 4 x 4 Gram pivot is singular")
    verify_two_qubit_clifford()

    print(f"MAT md5 = {EXPECTED_MAT_MD5}")
    print(f"A sha256 = {EXPECTED_A_SHA256}")
    print(f"shape = {a.shape[0]} x {a.shape[1]}; exact A levels = {len(NORMALIZED_LEVELS)}")
    print(f"classical witness value = {classical}")
    print("exact Gram identity = P^2 = 75 P; diag(P)=1; trace(P)=300; rank(P)=4")
    print(f"pivot = {pivot}; det(P_pivot) = {pivot_det[0]} + ({pivot_det[1]}) sqrt(5)")
    print(f"vector value = {vector_a} + ({vector_b}) sqrt(5)")
    print(f"top eigenvalue = {lambda_a} + ({lambda_b}) sqrt(5)")
    print("exact spectral identities = E=P/75, AP=lambda P, R=A-lambda E, RE=0")
    print(
        "exact residual bound numerator = "
        f"{rho_sq_num_a} + ({rho_sq_num_b}) sqrt(5), denominator 600; "
        "rho^2 < lambda^2"
    )
    print("conclusion = ||A||_op=lambda and range(P) is the strict top singular space")
    print("two-qubit Clifford generators = exact Hermiticity, involution, anticommutator, and trace checks pass")
    print(f"stored-float cross-check max error = {max_float_error:.3e} (non-load-bearing)")


if __name__ == "__main__":
    main()
