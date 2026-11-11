#!/usr/bin/env python3
"""Exact checker for seven-term hypermetrics and one uncovered CUT_7 orbit.

The Python layer reconstructs the H4 terminal faces and exact correlation
matrix.  It writes a deterministic compact input and invokes the pinned C++
meet-in-the-middle kernel, which exhausts 178939832 signed triples using only
integer and bit operations.  It also proves full CUT_7 projection for one
14400-cluster orbit that contains no terminal free six-set.
"""

import collections
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile

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
CPP_KERNEL = ROOT / (
    "grothendieck-d4/tools/h4_seven_hypermetric_mitm.cpp"
)
EXPECTED_CPP_SHA = (
    "c4cbbb3aa344ccff37c8a67480112346a3cad23cf0da704ad6710af07554a749"
)
EXPECTED_CORRELATION_SHA = (
    "71a507ef2e641adf4515907dec377f8552b7a07e5fae75196f8ba9ba6ff0b3f1"
)
MAGIC = 0x4434534556454E31
CLUSTER_REPRESENTATIVE = (0, 35, 137, 284, 320, 471, 594)


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_pentagonal_checker():
    if file_sha256(PENTAGONAL_CHECKER) != EXPECTED_PENTAGONAL_CHECKER_SHA:
        raise AssertionError("pentagonal checker SHA mismatch")
    if file_sha256(CPP_KERNEL) != EXPECTED_CPP_SHA:
        raise AssertionError("C++ kernel SHA mismatch")
    spec = importlib.util.spec_from_file_location(
        "pentagonal_checker", PENTAGONAL_CHECKER
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def signed_literal_orbit(base, generators, a):
    actions = []
    for p, s in generators:
        inverse = np.empty(base.N, dtype=np.uint16)
        inverse[p] = np.arange(base.N, dtype=np.uint16)
        alpha = ((a * s * a[p]) < 0).astype(np.uint8)
        actions.append((inverse, alpha))
    seed = ((0, 0),)
    orbit = {seed}
    queue = collections.deque([seed])
    while queue:
        node = queue.popleft()
        for inverse, alpha in actions:
            image = base.act_partial_assignment(node, inverse, alpha)
            if image not in orbit:
                orbit.add(image)
                queue.append(image)
    return orbit


def prepare_kernel_input(faces, path):
    signs = np.stack([row for _, row in faces]).astype(np.int8)
    incidence = signs == 0
    containing_zero = np.flatnonzero(incidence[:, 0])
    not_containing_zero = np.flatnonzero(~incidence[:, 0])
    if len(containing_zero) != 48:
        raise AssertionError("coordinate 0 terminal incidence mismatch")
    order = np.concatenate((containing_zero, not_containing_zero))
    signs = signs[order]

    conflict = np.zeros((600, 600), dtype=np.uint8)
    for variable, _ in faces:
        for i in variable:
            conflict[i, list(variable)] = 1
    np.fill_diagonal(conflict, 1)
    coordinates = np.asarray(
        [j for j in range(1, 600) if not conflict[0, j]], dtype="<u2"
    )
    literal_coordinate = np.repeat(coordinates, 2)
    literal_sign = np.tile(np.asarray([-1, 1], dtype=np.int8), len(coordinates))
    if len(coordinates) != 555 or len(literal_coordinate) != 1110:
        raise AssertionError("kernel literal census mismatch")

    with open(path, "wb") as output:
        output.write(struct.pack("<Q", MAGIC))
        output.write(signs.tobytes(order="C"))
        output.write(conflict.tobytes(order="C"))
        output.write(literal_coordinate.astype("<u2").tobytes(order="C"))
        output.write(literal_sign.tobytes(order="C"))


def run_kernel(faces):
    if sys.byteorder != "little":
        raise AssertionError("C++ binary replay currently requires little endian")
    compiler = shutil.which("clang++") or shutil.which("c++")
    if compiler is None:
        raise AssertionError("no C++17 compiler found")
    with tempfile.TemporaryDirectory(prefix="d4-seven-mitm-") as directory:
        directory = Path(directory)
        input_path = directory / "input.bin"
        executable = directory / "checker"
        prepare_kernel_input(faces, input_path)
        subprocess.run(
            [compiler, "-O3", "-std=c++17", str(CPP_KERNEL), "-o", str(executable)],
            check=True,
        )
        completed = subprocess.run(
            [str(executable), str(input_path)],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    result = json.loads(completed.stdout)
    expected = {
        "status": "EXACT_SEVEN_MITM_COMPLETE",
        "valid_signed_triples": 178939832,
        "hash_groups_with_repetition": 18022838,
        "exact_signature_groups_with_repetition": 18022838,
        "exact_representation_pairings": 3457621250,
        "cross_compatible_pairings": 356229760,
        "fully_compatible_seven_term_vectors": 0,
    }
    if result != expected:
        raise AssertionError(f"unexpected C++ census {result}")
    return result


def projected_cut_patterns(cluster, faces):
    """Exact CUT_7 patterns, normalized by the first sign."""
    patterns = set()
    cluster = tuple(cluster)
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
    if len(signed_literal_orbit(base, generators, a)) != 600:
        raise AssertionError("signed literal transitivity failed")

    B, _, columns = base.exact_switched_data(A, a, b)
    zero_columns = tuple(j for j, value in enumerate(columns) if value == 0)
    faces = pentagonal.build_faces(base, group, a, b, zero_columns)
    if len(faces) != 4800:
        raise AssertionError("terminal face count mismatch")
    correlation = pentagonal.exact_correlation(faces)
    if pentagonal.correlation_sha(correlation) != EXPECTED_CORRELATION_SHA:
        raise AssertionError("exact correlation SHA mismatch")

    kernel_result = run_kernel(faces)

    free_six_sets = set(tuple(variable) for variable, _ in faces)
    for omit in range(7):
        subset = CLUSTER_REPRESENTATIVE[:omit] + CLUSTER_REPRESENTATIVE[omit + 1 :]
        if subset in free_six_sets:
            raise AssertionError("representative contains a terminal free six-set")
    patterns = projected_cut_patterns(CLUSTER_REPRESENTATIVE, faces)
    if patterns != set(range(64)):
        raise AssertionError(f"CUT_7 projection size {len(patterns)}")
    orbit = cluster_orbit(CLUSTER_REPRESENTATIVE, generators)
    if len(orbit) != 14400 or min(orbit) != CLUSTER_REPRESENTATIVE:
        raise AssertionError("uncovered CUT_7 orbit mismatch")
    for cluster in orbit:
        for omit in range(7):
            subset = cluster[:omit] + cluster[omit + 1 :]
            if subset in free_six_sets:
                raise AssertionError("orbit unexpectedly meets the free-six family")

    result = {
        "status": "EXACT_SEVEN_TERM_NO_GO_PASSED",
        "known_C_level_cuts": 307200,
        "correlation_matrix_sha256": EXPECTED_CORRELATION_SHA,
        "seven_term_hypermetric_census": kernel_result,
        "conclusion": (
            "No vector with exactly seven nonzero coefficients in {+1,-1} "
            "has b^T M b=307200.  In particular, no seven-term vector with "
            "four +1, three -1, and coefficient sum 1 is tight on all known "
            "C-level cuts."
        ),
        "uncovered_CUT7_cluster_orbit": {
            "canonical_representative": list(CLUSTER_REPRESENTATIVE),
            "orbit_size_under_H4_plus_party_swap": len(orbit),
            "contains_terminal_free_six_set": False,
            "projected_known_cut_patterns": len(patterns),
            "conclusion": (
                "The known equality cuts project onto all 64 vertices of "
                "CUT_7.  Hence no proper local CUT_7 facet, hypermetric or "
                "non-hypermetric, supported on any cluster in this complete "
                "14400-element orbit can vanish on all known equality cuts."
            ),
        },
        "scope": (
            "Complete seven-term {+1,-1} no-go relative to the 307200 known "
            "equality cuts, plus one complete uncovered CUT_7 cluster orbit. "
            "This does not prove equality-set completeness or the global "
            "classical upper bound."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
