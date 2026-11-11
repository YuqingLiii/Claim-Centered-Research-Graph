#!/usr/bin/env python3
"""Exact strength-7 counterexample and local-facet no-go checker."""

import collections
import hashlib
import importlib.util
import json
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
PENTAGONAL_CHECKER = ROOT / (
    "grothendieck-d4/tools/"
    "h4_pentagonal_hypermetric_no_go_checker.py"
)
EXPECTED_PENTAGONAL_CHECKER_SHA = (
    "ee6bb77e12b53515ecc9bed001f92d833aa2da74c06daf9e78cb295d9f0a88f3"
)
CLUSTER = tuple(range(7))
EXPECTED_PATTERNS = (
    0, 2, 4, 6, 8, 9, 10, 11, 14, 16, 17, 18, 20, 22, 24, 25, 26, 27,
    32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 52, 53,
    57,
)
EXPECTED_BASIS_PATTERNS = (
    0, 2, 4, 6, 8, 9, 10, 11, 14, 16, 17, 18, 20, 24, 25, 32, 33, 36,
    37, 38, 40, 48,
)
EXPECTED_ORBIT_SHA = (
    "0967fdde3d8b760d0acde0c3bd54075a7ce6b39c76caa6c5777784160bfa47d9"
)


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_pentagonal_checker():
    if file_sha256(PENTAGONAL_CHECKER) != EXPECTED_PENTAGONAL_CHECKER_SHA:
        raise AssertionError("pentagonal checker SHA mismatch")
    spec = importlib.util.spec_from_file_location(
        "pentagonal_checker", PENTAGONAL_CHECKER
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def projected_patterns(cluster, faces):
    patterns = set()
    for variable, fixed_signs in faces:
        free_positions = [r for r, i in enumerate(cluster) if i in variable]
        base_bits = [0 if fixed_signs[i] > 0 else 1 for i in cluster]
        for mask in range(1 << len(free_positions)):
            bits = base_bits[:]
            for k, position in enumerate(free_positions):
                bits[position] = (mask >> k) & 1
            anchor = bits[0]
            code = sum((bits[r] ^ anchor) << (r - 1) for r in range(1, 7))
            patterns.add(code)
    return patterns


def cut_feature(code):
    bits = [0] + [(code >> (r - 1)) & 1 for r in range(1, 7)]
    return [1] + [
        bits[i] ^ bits[j] for i in range(7) for j in range(i + 1, 7)
    ]


def bareiss_determinant(matrix):
    """Fraction-free exact determinant over the integers."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise AssertionError("determinant matrix is not square")
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k] != 0), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss division was not exact")
                a[i][j] = numerator // previous
        previous = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def cluster_orbit(cluster, generators):
    coordinate_generators = [
        np.concatenate((p, 300 + p)).astype(np.uint16) for p, _ in generators
    ]
    coordinate_generators.append(
        np.concatenate((np.arange(300, 600), np.arange(300))).astype(np.uint16)
    )
    orbit = {tuple(cluster)}
    queue = collections.deque(orbit)
    while queue:
        current = queue.popleft()
        for permutation in coordinate_generators:
            image = tuple(sorted(int(permutation[i]) for i in current))
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    return orbit


def orbit_sha(orbit):
    h = hashlib.sha256()
    for cluster in sorted(orbit):
        for coordinate in cluster:
            h.update(int(coordinate).to_bytes(2, "little", signed=False))
    return h.hexdigest()


def main():
    pentagonal = load_pentagonal_checker()
    base = pentagonal.load_base_checker()
    with h5py.File(base.MAT, "r") as f:
        A = base.exact_int_matrix(f["A"][()], "A")
        a = base.exact_sign_vector(f["ax"][()], "ax")
        b = base.exact_sign_vector(f["by"][()], "by")
    if not np.array_equal(A, A.T):
        raise AssertionError("party swap requires exact symmetry")
    with open(base.SYSTEM) as f:
        system = json.load(f)
    generators = [
        (
            np.asarray(g["perm"], dtype=np.uint16),
            np.asarray(g["sign"], dtype=np.int8),
        )
        for g in system["group"]["coxeter_generators"]
    ]
    group = base.generate_group(generators)
    if len(group) != 14400 or base.group_sha(group) != base.EXPECTED_ACTION_SHA:
        raise AssertionError("signed H4 group reconstruction failed")
    _, _, columns = base.exact_switched_data(A, a, b)
    zero_columns = tuple(j for j, value in enumerate(columns) if value == 0)
    faces = pentagonal.build_faces(base, group, a, b, zero_columns)
    if len(faces) != 4800:
        raise AssertionError("terminal face count mismatch")

    patterns = projected_patterns(CLUSTER, faces)
    if tuple(sorted(patterns)) != EXPECTED_PATTERNS:
        raise AssertionError("projected pattern set mismatch")
    if len(patterns) != 36:
        raise AssertionError("strength-7 counterexample disappeared")

    basis_matrix = [cut_feature(code) for code in EXPECTED_BASIS_PATTERNS]
    determinant = bareiss_determinant(basis_matrix)
    if determinant != -32768:
        raise AssertionError(f"unexpected feature determinant {determinant}")

    orbit = cluster_orbit(CLUSTER, generators)
    if len(orbit) != 7200 or min(orbit) != CLUSTER:
        raise AssertionError("counterexample cluster orbit mismatch")
    sha = orbit_sha(orbit)
    if sha != EXPECTED_ORBIT_SHA:
        raise AssertionError("counterexample orbit SHA mismatch")
    free_six_sets = set(tuple(variable) for variable, _ in faces)
    for cluster in orbit:
        for omit in range(7):
            subset = cluster[:omit] + cluster[omit + 1 :]
            if subset in free_six_sets:
                raise AssertionError("counterexample orbit contains a free six-set")

    missing = sorted(set(range(64)) - patterns)
    result = {
        "status": "EXACT_STRENGTH7_COUNTEREXAMPLE_PASSED",
        "claim_refuted": (
            "The 307200 known equality cuts form a strength-7 covering array "
            "on the 600 coordinates, modulo global cut-sign reversal."
        ),
        "lexicographically_first_seven_cluster": list(CLUSTER),
        "projected_CUT7_vertices": len(patterns),
        "missing_vertex_codes": missing,
        "counterexample_orbit": {
            "size_under_H4_plus_party_swap": len(orbit),
            "sha256": sha,
            "contains_terminal_free_six_set": False,
        },
        "local_facet_search": {
            "feature_coordinates": "constant plus the 21 CUT_7 edge variables",
            "exact_rank": 22,
            "basis_pattern_codes": list(EXPECTED_BASIS_PATTERNS),
            "basis_determinant": determinant,
            "conclusion": (
                "No nonzero affine-linear cut expression is constant on all "
                "36 observed vertices.  Hence no equality-compatible proper "
                "local CUT_7 facet exists on this cluster or its orbit."
            ),
        },
        "scope": (
            "This refutes strength 7 with its lexicographically first possible "
            "cluster and closes the local-facet route on the complete 7200-"
            "cluster orbit.  It does not classify every seven-cluster orbit."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
