#!/usr/bin/env python3
"""Exact checker for a rank-21 seven-cluster orbit and its facet no-go.

The known 307200 equality cuts satisfy a four-coordinate quadrilateral
relation on the canonical core (0,1,269,288).  A canonical seven-coordinate
extension has cut-feature rank exactly 21 rather than 22.  Its one-dimensional
nullspace, however, changes sign on genuine CUT_7 vertices, so it cannot be a
valid cut inequality in either orientation.
"""

import collections
import hashlib
import importlib.util
import json
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
STRENGTH_CHECKER = ROOT / (
    "grothendieck-d4/tools/"
    "h4_strength7_counterexample_checker.py"
)
EXPECTED_STRENGTH_CHECKER_SHA = (
    "80d2f305828745dd1a07a396ac87216e00c91ca4902b74bb2d6613949f08ae20"
)

CORE = (0, 1, 269, 288)
CLUSTER = (0, 1, 45, 108, 269, 288, 520)
EXPECTED_CORE_PATTERNS = (0, 1, 2, 4, 6, 7)
EXPECTED_CLUSTER_PATTERNS = (
    0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 18, 20, 22, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 46,
    56, 58, 59, 60, 61, 62, 63,
)

# Coordinates are: constant, then x_ij in lexicographic pair order.
# Thus Q=x_04-x_05-x_14+x_15 on CLUSTER.
NULL_VECTOR = (
    0,
    0, 0, 0, 1, -1, 0,
    0, 0, -1, 1, 0,
    0, 0, 0, 0,
    0, 0, 0,
    0, 0,
    0,
)
RANK21_ROW_CODES = (
    0, 1, 2, 3, 4, 5, 6, 8, 12, 16, 18, 20, 24, 25, 26, 32, 33,
    34, 36, 40, 56,
)
RANK21_COLUMNS = tuple(range(10)) + tuple(range(11, 22))
EXPECTED_CORE_ORBIT_SHA = (
    "9a8c35e80d9df4f39546823ebfc7cb3e419cc69c2f3103dda6e7e0e7057a0516"
)
EXPECTED_CLUSTER_ORBIT_SHA = (
    "136e5f8d3d4be0136d0b54e8fae78801d7f59905d11d0d53e1385e0d53da00cd"
)


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_strength_checker():
    if file_sha256(STRENGTH_CHECKER) != EXPECTED_STRENGTH_CHECKER_SHA:
        raise AssertionError("strength-7 checker SHA mismatch")
    spec = importlib.util.spec_from_file_location(
        "strength7_checker", STRENGTH_CHECKER
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def projected_patterns(cluster, faces):
    """Project the exact face union, modulo global cut-sign reversal."""
    patterns = set()
    for variable, fixed_signs in faces:
        free_positions = [r for r, i in enumerate(cluster) if i in variable]
        base_bits = [0 if fixed_signs[i] > 0 else 1 for i in cluster]
        for mask in range(1 << len(free_positions)):
            bits = base_bits[:]
            for k, position in enumerate(free_positions):
                bits[position] = (mask >> k) & 1
            anchor = bits[0]
            code = sum(
                (bits[r] ^ anchor) << (r - 1)
                for r in range(1, len(cluster))
            )
            patterns.add(code)
    return patterns


def cut_feature(code, n):
    bits = [0] + [(code >> (r - 1)) & 1 for r in range(1, n)]
    return [1] + [
        bits[i] ^ bits[j] for i in range(n) for j in range(i + 1, n)
    ]


def main():
    strength = load_strength_checker()
    pentagonal = strength.load_pentagonal_checker()
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

    # Minimal four-coordinate support of the rank defect.
    core_patterns = projected_patterns(CORE, faces)
    if tuple(sorted(core_patterns)) != EXPECTED_CORE_PATTERNS:
        raise AssertionError("quadrilateral-core projection mismatch")
    core_null = (0, 0, 1, -1, -1, 1, 0)
    for code in core_patterns:
        if sum(x * y for x, y in zip(cut_feature(code, 4), core_null)) != 0:
            raise AssertionError("quadrilateral relation failed")
    # Omitting feature column 5 leaves a nonzero 6-by-6 minor.
    core_minor = [
        [value for j, value in enumerate(cut_feature(code, 4)) if j != 5]
        for code in EXPECTED_CORE_PATTERNS
    ]
    core_determinant = strength.bareiss_determinant(core_minor)
    if core_determinant != -4:
        raise AssertionError(f"unexpected core determinant {core_determinant}")

    # Exact seven-coordinate rank: the displayed null vector proves rank <=21;
    # the nonzero integer minor proves rank >=21.
    patterns = projected_patterns(CLUSTER, faces)
    if tuple(sorted(patterns)) != EXPECTED_CLUSTER_PATTERNS:
        raise AssertionError("seven-cluster projection mismatch")
    for code in patterns:
        feature = cut_feature(code, 7)
        if sum(x * y for x, y in zip(feature, NULL_VECTOR)) != 0:
            raise AssertionError("rank-21 null relation failed")
    rank_minor = [
        [cut_feature(code, 7)[j] for j in RANK21_COLUMNS]
        for code in RANK21_ROW_CODES
    ]
    rank_determinant = strength.bareiss_determinant(rank_minor)
    if rank_determinant != -16384:
        raise AssertionError(f"unexpected rank-21 determinant {rank_determinant}")

    # The unique null direction is not a valid CUT_7 inequality: it takes both
    # signs on genuine cut vertices.  Therefore no proper CUT_7 face contains
    # all projected equality vertices on this cluster.
    values = {
        code: sum(
            x * y for x, y in zip(cut_feature(code, 7), NULL_VECTOR)
        )
        for code in range(64)
    }
    value_counts = collections.Counter(values.values())
    if value_counts != collections.Counter({0: 48, 2: 8, -2: 8}):
        raise AssertionError(f"unexpected CUT_7 null values {value_counts}")
    if values[9] != 2 or values[17] != -2:
        raise AssertionError("two-sided cut witnesses changed")

    core_orbit = strength.cluster_orbit(CORE, generators)
    if len(core_orbit) != 1800 or min(core_orbit) != CORE:
        raise AssertionError("quadrilateral-core orbit mismatch")
    core_sha = strength.orbit_sha(core_orbit)
    if core_sha != EXPECTED_CORE_ORBIT_SHA:
        raise AssertionError("quadrilateral-core orbit SHA mismatch")
    cluster_orbit = strength.cluster_orbit(CLUSTER, generators)
    if len(cluster_orbit) != 14400 or min(cluster_orbit) != CLUSTER:
        raise AssertionError("rank-21 cluster orbit mismatch")
    cluster_sha = strength.orbit_sha(cluster_orbit)
    if cluster_sha != EXPECTED_CLUSTER_ORBIT_SHA:
        raise AssertionError("rank-21 cluster orbit SHA mismatch")

    free_six_sets = set(tuple(variable) for variable, _ in faces)
    if any(
        CLUSTER[:omit] + CLUSTER[omit + 1 :] in free_six_sets
        for omit in range(7)
    ):
        raise AssertionError("rank-21 representative contains a terminal six-set")

    result = {
        "status": "EXACT_RANK21_QUADRILATERAL_ORBIT_PASSED",
        "proved_in_draft": {
            "quadrilateral_core": list(CORE),
            "core_projected_vertices": len(core_patterns),
            "core_feature_rank": 6,
            "core_rank_minor_determinant": core_determinant,
            "core_orbit_size": len(core_orbit),
            "core_orbit_sha256": core_sha,
            "canonical_seven_cluster": list(CLUSTER),
            "seven_projected_vertices": len(patterns),
            "seven_feature_rank": 21,
            "rank_minor_determinant": rank_determinant,
            "seven_cluster_orbit_size": len(cluster_orbit),
            "seven_cluster_orbit_sha256": cluster_sha,
        },
        "unique_null_expression": "x_04-x_05-x_14+x_15",
        "cut7_value_census": dict(sorted(value_counts.items())),
        "two_sided_witness_codes": {"positive": 9, "negative": 17},
        "refuted_route": (
            "The rank defect does not expose an equality-compatible CUT_7 "
            "facet: its unique null expression has both signs on valid cuts."
        ),
        "scope": (
            "This exactly classifies one 14400-cluster rank-21 orbit and a "
            "1800-core quadrilateral orbit.  It does not classify every "
            "seven-coordinate cluster orbit."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
