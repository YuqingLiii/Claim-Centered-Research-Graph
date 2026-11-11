#!/usr/bin/env python3
"""Exact triangle-cover certificate for the 217-variable p-cut gate.

The frozen certificate contains only nonnegative integer multipliers indexed
by stabilizer orbits of homogeneous triangle inequalities.  This checker
reconstructs every orbit and every edge coefficient from the frozen H4
instance, applies the multipliers with Python integers, and verifies that all
edge residuals are nonnegative.  The MILP used to discover the multipliers
is not invoked and is not trusted by the proof.
"""

from __future__ import annotations

from collections import defaultdict, deque
import hashlib
import itertools
import sys
from pathlib import Path

import h5py
import numpy as np
import sympy as sp


HERE = Path(__file__).resolve()
PROJECT = HERE.parents[1]
TOOLS = PROJECT / "tools"
BOOTSTRAP = TOOLS / "bootstrap"
sys.path[:0] = [str(TOOLS), str(BOOTSTRAP)]

from h4_exact_instance_checker import (  # noqa: E402
    EXPECTED_CLASSICAL,
    exact_int_matrix,
    exact_signs,
)
import h4_nogap_irrep_cache as h4rep  # noqa: E402


MAT = PROJECT / "artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")
CERTIFICATE = PROJECT / "artifacts/certificates/d4-pcut-triangle-cover-certificate-20260830.npz"
EXPECTED_CERTIFICATE_SHA256 = "fe1444390cc921aae3e1fb40b3389fc9ae94d1ae77fee83813f9198c06f7f504"
EXPECTED_P_GATE_SHA256 = "5049871cbbb88448752b893e2157cef7377993c91215d4d99e7bc0467e9f4adf"
N = 300


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def p_gate_sha256(p_support, p_signs, edge_weight) -> str:
    """Canonical digest of the 217-variable objective map.

    The ordering is the sorted ambient support, its archived signs, then the
    lexicographic upper-triangle gauged weights M_ij.  All integers use signed
    little-endian int64, so the digest is independent of NumPy's native
    endianness.
    """
    digest = hashlib.sha256(b"D4-p-cut-gate-v1\0")
    digest.update(np.asarray(p_support, dtype="<i8").tobytes())
    digest.update(np.asarray(p_signs, dtype="<i8").tobytes())
    digest.update(
        np.asarray([edge_weight[edge] for edge in sorted(edge_weight)], dtype="<i8").tobytes()
    )
    return digest.hexdigest()


def transformed(vector: np.ndarray, permutation, signs) -> np.ndarray:
    result = np.empty(N, dtype=np.int8)
    result[np.asarray(permutation, dtype=np.int64)] = (
        np.asarray(signs, dtype=np.int8) * vector
    )
    return result


def main() -> None:
    assert file_sha256(CERTIFICATE) == EXPECTED_CERTIFICATE_SHA256
    with h5py.File(MAT, "r") as archive:
        matrix = exact_int_matrix(archive["A"][()])
        x = np.asarray(exact_signs(archive["ax"][()], "ax"), dtype=np.int64)
        y = np.asarray(exact_signs(archive["by"][()], "by"), dtype=np.int64)
    matrix_object = matrix.astype(object)
    p = (x + y) // 2
    q = (x - y) // 2
    p_support = list(map(int, np.flatnonzero(p)))
    q_support = list(map(int, np.flatnonzero(q)))
    assert len(p_support) == 217 and len(q_support) == 83
    p_value = int(p.astype(object) @ (matrix_object @ p.astype(object)))
    q_value = int(q.astype(object) @ (matrix_object @ q.astype(object)))
    assert p_value - q_value == EXPECTED_CLASSICAL

    # Recheck the q-cell SOS, so the final fixed-cell theorem is standalone.
    q_signs = q[q_support]
    q_principal = matrix[np.ix_(q_support, q_support)].astype(object)
    q_gauged = q_principal * np.outer(q_signs, q_signs)
    q_laplacian = np.diag(np.asarray(q_gauged.sum(axis=1), dtype=object)) - q_gauged
    assert all(sum(map(int, row)) == 0 for row in q_laplacian)
    q_grounded = sp.Matrix((-q_laplacian)[:-1, :-1].tolist())
    q_lower, q_diagonal = q_grounded.LDLdecomposition(hermitian=True)
    assert q_lower * q_diagonal * q_lower.T == q_grounded
    assert all(q_diagonal[i, i] > 0 for i in range(82))

    # Exact archived-pair stabilizer on the p support.
    _quotient, _quotient_data, group, _hdata, _audit = h4rep.structural_construction()
    _system, elements, _generators, _sha = h4rep.load_and_match_certified_action(
        SYSTEM, group
    )
    p_position = {coordinate: index for index, coordinate in enumerate(p_support)}
    stabilizer = []
    p8 = p.astype(np.int8)
    q8 = q.astype(np.int8)
    for permutation, signs in elements:
        if np.array_equal(transformed(p8, permutation, signs), p8) and np.array_equal(
            transformed(q8, permutation, signs), q8
        ):
            stabilizer.append(
                tuple(p_position[int(permutation[i])] for i in p_support)
            )
    assert len(stabilizer) == 6

    def triangle_canonical(triangle):
        i, j, k = triangle
        return min(
            (min(g[i], g[j]), max(g[i], g[j]), g[k]) for g in stabilizer
        )

    # Gauge p to all ones.  Its cut deficit is four times the weighted cut
    # of these off-diagonal edge coefficients.
    p_signs = p[p_support]
    p_principal = matrix[np.ix_(p_support, p_support)].astype(object)
    p_gauged = p_principal * np.outer(p_signs, p_signs)
    edge_weight = {
        (i, j): int(p_gauged[i, j])
        for i in range(217) for j in range(i + 1, 217)
    }
    assert sum(weight < 0 for weight in edge_weight.values()) == 6294
    assert sum(weight > 0 for weight in edge_weight.values()) == 15066
    objective_sha256 = p_gate_sha256(p_support, p_signs, edge_weight)
    assert objective_sha256 == EXPECTED_P_GATE_SHA256
    positive_edges = {edge for edge, weight in edge_weight.items() if weight > 0}

    # Reconstruct the 80,819 stabilizer orbits of admissible triangle covers.
    triangle_orbits = defaultdict(list)
    for (i, j), weight in edge_weight.items():
        if weight >= 0:
            continue
        for k in range(217):
            if k in (i, j):
                continue
            if (
                tuple(sorted((i, k))) in positive_edges
                and tuple(sorted((j, k))) in positive_edges
            ):
                triangle_orbits[triangle_canonical((i, j, k))].append((i, j, k))
    triangle_items = sorted(triangle_orbits.items())
    assert len(triangle_items) == 80_819

    with np.load(CERTIFICATE, allow_pickle=False) as frozen:
        column_index = np.asarray(frozen["column_index"], dtype=np.int64)
        multiplier = np.asarray(frozen["multiplier"], dtype=np.int64)
        assert str(frozen["lp_sha256"]) == (
            "744bf4b9324ef03807bd4872b315673810588bc3f5ac59cd26e112b03d189a0b"
        )
    assert len(column_index) == len(multiplier) == 26_627
    assert np.all(column_index[1:] > column_index[:-1])
    assert int(column_index[0]) >= 0 and int(column_index[-1]) < len(triangle_items)
    assert np.all(multiplier > 0)
    assert int(multiplier.max()) == 184_955_919_316_291

    # Apply the orbit multipliers directly to every one of the 23,436 edge
    # coefficients.  If T_ijk=y_ik+y_jk-y_ij, the residual is w-sum lambda*T.
    residual = dict(edge_weight)
    expanded_triangles = 0
    for column, value in zip(column_index, multiplier):
        _representative, members = triangle_items[int(column)]
        amount = int(value)
        for i, j, k in members:
            base = (i, j)
            first = tuple(sorted((i, k)))
            second = tuple(sorted((j, k)))
            residual[base] += amount
            residual[first] -= amount
            residual[second] -= amount
            expanded_triangles += 1
    assert expanded_triangles == 158_829
    assert min(residual.values()) == 0
    assert all(value >= 0 for value in residual.values())

    # Boolean truth table for every homogeneous triangle generator.
    for zi, zj, zk in itertools.product((0, 1), repeat=3):
        yij = zi ^ zj
        yik = zi ^ zk
        yjk = zj ^ zk
        assert yik + yjk - yij in (0, 2)

    # Equality is rigid already from the positive residual-edge graph.
    residual_graph = {i: [] for i in range(217)}
    positive_residual_edges = 0
    for (i, j), value in residual.items():
        if value > 0:
            residual_graph[i].append(j)
            residual_graph[j].append(i)
            positive_residual_edges += 1
    seen = {0}
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        for neighbor in residual_graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    assert len(seen) == 217

    print("certificate sha256 =", EXPECTED_CERTIFICATE_SHA256)
    print("217-variable objective sha256 =", objective_sha256)
    print("nonzero integer orbit multipliers =", len(multiplier))
    print("expanded triangle inequalities =", expanded_triangles)
    print("minimum edge residual =", min(residual.values()))
    print("positive residual edges / connected vertices =", positive_residual_edges, len(seen))
    print("EXACT_FIXED_217_PLUS_83_CELL_UPPER_BOUND_PASSED")


if __name__ == "__main__":
    main()
