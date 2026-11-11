#!/usr/bin/env python3
"""Exact no-go checker for equality-compatible triangle hypermetrics.

It proves that no nontrivial three-variable hypermetric inequality is tight
on all 307200 currently known C-level cuts.  Only integer/discrete arithmetic
is used in the certified calculation.
"""

import collections
import hashlib
import importlib.util
import json
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
BASE_CHECKER = ROOT / (
    "grothendieck-d4/tools/"
    "h4_affine_equality_terminals_checker.py"
)
EXPECTED_BASE_CHECKER_SHA = (
    "d9b7687704e3ac8575e3bcd9c092b06270315b439aeadbd40a141143da2435dd"
)
EXPECTED_CORRELATION_SHA = (
    "71a507ef2e641adf4515907dec377f8552b7a07e5fae75196f8ba9ba6ff0b3f1"
)
KNOWN_CUT_COUNT = 307200


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_base_checker():
    if file_sha256(BASE_CHECKER) != EXPECTED_BASE_CHECKER_SHA:
        raise AssertionError("base checker SHA mismatch")
    spec = importlib.util.spec_from_file_location("affine_h4_checker", BASE_CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def correlation_sha(C):
    h = hashlib.sha256()
    for x in C.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def main():
    base = load_base_checker()
    with h5py.File(base.MAT, "r") as f:
        A = base.exact_int_matrix(f["A"][()], "A")
        a = base.exact_sign_vector(f["ax"][()], "ax")
        b = base.exact_sign_vector(f["by"][()], "by")

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
        raise AssertionError("signed group reconstruction failed")

    B, _, cols = base.exact_switched_data(A, a, b)
    zero_columns = tuple(j for j, x in enumerate(cols) if x == 0)
    if zero_columns != (46, 56, 85, 99, 131, 148):
        raise AssertionError("zero-column set mismatch")

    right_faces = set()
    left_faces = set()
    for p, s in group:
        variable = tuple(
            sorted(int(i) for i in np.flatnonzero(np.isin(p, zero_columns)))
        )
        right_faces.add((
            base.packed((a * s * a[p]) < 0),
            base.packed((b * s * b[p]) < 0),
            variable,
        ))
        left_faces.add((
            base.packed((a * s * b[p]) < 0),
            variable,
            base.packed((b * s * a[p]) < 0),
        ))
    if len(right_faces) != 2400 or len(left_faces) != 2400:
        raise AssertionError("face orbit size mismatch")

    # Sum u u^T over all 64 points of each six-face without expanding the
    # 307200-by-600 sign matrix.  A variable coordinate has mean zero; two
    # distinct variable coordinates have zero product mean; its square is 1.
    fixed_sign_rows = []
    diagonal_correction = np.zeros(600, dtype=np.int64)
    for family, faces in (("right", right_faces), ("left", left_faces)):
        for face in faces:
            if family == "right":
                left_blob, right_blob, variable = face
                variable_indices = 300 + np.asarray(variable, dtype=np.int64)
            else:
                left_blob, variable, right_blob = face
                variable_indices = np.asarray(variable, dtype=np.int64)
            bits = np.concatenate((base.unpacked(left_blob), base.unpacked(right_blob)))
            signs = 1 - 2 * bits.astype(np.int64)
            signs[variable_indices] = 0
            fixed_sign_rows.append(signs)
            diagonal_correction[variable_indices] += 64

    fixed_sign_rows = np.stack(fixed_sign_rows)
    if fixed_sign_rows.shape != (4800, 600):
        raise AssertionError("fixed sign table shape mismatch")
    C = 64 * (fixed_sign_rows.T @ fixed_sign_rows)
    C[np.diag_indices(600)] += diagonal_correction
    if not np.array_equal(C, C.T):
        raise AssertionError("correlation matrix is not symmetric")
    if set(int(x) for x in np.diag(C)) != {KNOWN_CUT_COUNT}:
        raise AssertionError("correlation diagonal mismatch")
    Csha = correlation_sha(C)
    if Csha != EXPECTED_CORRELATION_SHA:
        raise AssertionError("correlation SHA mismatch")

    # For b=e_i+e_j-e_k, sum(b)=1.  On a cut z, with signs u=1-2z,
    # the hypermetric slack is ((b.u)^2-1)/4.  The number of known cuts
    # having nonzero slack is
    #   (N+C_ij-C_ik-C_jk)/4,
    # and every such cut contributes slack exactly 2.
    minimum_violating_cuts = KNOWN_CUT_COUNT
    attaining_ordered_triples = 0
    representative = None
    type_counts = collections.Counter()
    for i in range(600):
        for j in range(i + 1, 600):
            numerators = KNOWN_CUT_COUNT + int(C[i, j]) - C[i] - C[j]
            if np.any(numerators % 4):
                raise AssertionError("triangle violation count is nonintegral")
            violations = numerators // 4
            violations[i] = KNOWN_CUT_COUNT
            violations[j] = KNOWN_CUT_COUNT
            local_minimum = int(violations.min())
            if local_minimum < minimum_violating_cuts:
                minimum_violating_cuts = local_minimum
                attaining_ordered_triples = 0
                representative = (i, j, int(violations.argmin()))
                type_counts.clear()
            if local_minimum == minimum_violating_cuts:
                for k in np.flatnonzero(violations == minimum_violating_cuts):
                    attaining_ordered_triples += 1
                    kind = "".join("L" if x < 300 else "R" for x in (i, j, int(k)))
                    type_counts[kind] += 1

    if minimum_violating_cuts != 896:
        raise AssertionError(f"unexpected minimum {minimum_violating_cuts}")
    if representative is None:
        raise AssertionError("missing minimizing triangle")

    result = {
        "status": "EXACT_TRIANGLE_NO_GO_PASSED",
        "known_C_level_cuts": KNOWN_CUT_COUNT,
        "correlation_matrix": {
            "shape": [600, 600],
            "sha256": Csha,
            "minimum_off_diagonal": int(C[~np.eye(600, dtype=bool)].min()),
            "maximum_off_diagonal": int(C[~np.eye(600, dtype=bool)].max()),
        },
        "triangle_hypermetric_census": {
            "coefficient_form": "b=e_i+e_j-e_k, i<j, k distinct",
            "minimum_known_cuts_with_positive_slack": minimum_violating_cuts,
            "minimum_aggregate_slack": 2 * minimum_violating_cuts,
            "representative_zero_based_combined_indices": list(representative),
            "attaining_ordered_triples": attaining_ordered_triples,
            "attainer_party_type_counts": dict(sorted(type_counts.items())),
            "globally_tight_nontrivial_triangles": 0,
        },
        "conclusion": (
            "No nonzero nonnegative combination of ordinary triangle "
            "hypermetric slacks can vanish on every currently known C-level cut."
        ),
        "scope": (
            "Refutes the equality-compatible triangle cone only.  It does not "
            "exclude pentagonal or higher hypermetrics, general cluster facets, "
            "or prove completeness of the known C-level cuts."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
