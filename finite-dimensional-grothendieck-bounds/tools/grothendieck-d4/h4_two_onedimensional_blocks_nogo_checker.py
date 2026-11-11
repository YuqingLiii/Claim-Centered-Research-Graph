#!/usr/bin/env python3
"""Exact checker for the two one-dimensional H4-block SOS no-go.

The checked ansatz allows all degree-at-most-two equality-vanishing
summands in the trivial and Coxeter-sign isotypic components.  It does not
allow any of the other eighteen real H4 irreducibles, and therefore does not
decide the full degree-four SOS problem.

Usage:
  python h4_two_onedimensional_blocks_nogo_checker.py MAT SYSTEM CERTIFICATE

Dependencies: numpy, h5py, sympy.
"""

import collections
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

import h5py
import numpy as np
import sympy as sp


def die(message):
    raise SystemExit("ERROR: " + str(message))


def load_probe():
    path = Path(__file__).with_name("h4_invariant_vanishing_probe.py")
    spec = importlib.util.spec_from_file_location("h4_invariant_probe", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_hash(payload):
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def exact_positive_ldl(matrix):
    """Return exact LDL pivots; fail unless the symmetric matrix is PD."""
    n = len(matrix)
    lower = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    diagonal = []
    for j in range(n):
        pivot = Fraction(matrix[j][j]) - sum(
            lower[j][k] * lower[j][k] * diagonal[k] for k in range(j)
        )
        if pivot <= 0:
            die(f"nonpositive exact LDL pivot {j}: {pivot}")
        diagonal.append(pivot)
        for i in range(j + 1, n):
            lower[i][j] = (
                Fraction(matrix[i][j])
                - sum(
                    lower[i][k] * lower[j][k] * diagonal[k]
                    for k in range(j)
                )
            ) / pivot
    return diagonal


def coxeter_sign_character(probe, generators, group_p, group_s, parent):
    """Construct and exhaustively check the character sending each s_i to -1."""
    character = np.ones(len(group_p), dtype=np.int8)
    for index in range(1, len(group_p)):
        character[index] = -character[parent[index]]

    lookup = {
        probe.gkey((permutation, signs)): index
        for index, (permutation, signs) in enumerate(zip(group_p, group_s))
    }
    for index, element in enumerate(zip(group_p, group_s)):
        for generator in generators:
            image = probe.compose(element, generator)
            target = lookup.get(probe.gkey(image))
            if target is None:
                die("Coxeter generator edge left the generated group")
            if int(character[target]) != -int(character[index]):
                die("word parity does not define the Coxeter-sign character")
    return character


def twisted_monomial_basis(probe, generators, group_p, group_s, character):
    """Degree <=2 orbit sums transforming by the Coxeter-sign character."""
    relation = np.full(probe.MON_DIM, -1, dtype=np.int32)
    orientation = np.zeros(probe.MON_DIM, dtype=np.int8)
    records = []

    for start in range(probe.MON_DIM):
        if relation[start] >= 0:
            continue
        orbit_id = len(records)
        relation[start] = orbit_id
        orientation[start] = 1
        queue = collections.deque([start])
        members = []
        conflict = False
        while queue:
            monomial = queue.popleft()
            members.append(monomial)
            old_orientation = int(orientation[monomial])
            for permutation, signs in generators:
                image, action_sign = probe.act_mid(
                    monomial, permutation, signs
                )
                # Every Coxeter generator has character -1.
                new_orientation = -old_orientation * int(action_sign)
                if relation[image] < 0:
                    relation[image] = orbit_id
                    orientation[image] = new_orientation
                    queue.append(image)
                else:
                    if relation[image] != orbit_id:
                        die("twisted monomial orbit crossed relation ids")
                    if int(orientation[image]) != new_orientation:
                        conflict = True

        plus = 0
        minus = 0
        for index, (permutation, signs) in enumerate(zip(group_p, group_s)):
            image, action_sign = probe.act_mid(start, permutation, signs)
            if image == start:
                twisted_sign = int(character[index]) * int(action_sign)
                if twisted_sign == 1:
                    plus += 1
                else:
                    minus += 1
        if (plus + minus) * len(members) != len(group_p):
            die("twisted orbit-stabilizer identity failed")
        if conflict != (minus > 0):
            die("twisted orientation conflict failed the full-group check")
        records.append(
            {
                "rep": start,
                "members": members,
                "conflict": conflict,
                "stabilizer_plus": plus,
                "stabilizer_minus": minus,
            }
        )

    basis_id = np.full(probe.MON_DIM, -1, dtype=np.int16)
    active = []
    for record in records:
        if record["conflict"]:
            continue
        basis_index = len(active)
        for monomial in record["members"]:
            basis_id[monomial] = basis_index
        active.append(record)
    return basis_id, orientation, active


def equality_kernel(
    probe,
    z_right,
    z_left,
    zero_fields,
    basis_id,
    orientation,
    basis_dimension,
):
    right_values = np.stack(
        [
            probe.eval_invariant_basis(
                point, basis_id, orientation, basis_dimension
            )
            for point in probe.face_corners(
                z_right, [probe.N + j for j in zero_fields]
            )
        ]
    )
    left_values = np.stack(
        [
            probe.eval_invariant_basis(
                point, basis_id, orientation, basis_dimension
            )
            for point in probe.face_corners(z_left, zero_fields)
        ]
    )
    rows = (
        probe.face_restriction_matrix(right_values)
        + probe.face_restriction_matrix(left_values)
    )
    matrix = sp.Matrix(rows)
    kernel = [
        probe.primitive_integer_vector(vector)
        for vector in matrix.nullspace()
    ]
    return rows, int(matrix.rank()), kernel


def evaluation_vectors(
    probe, z_right, basis_id, orientation, basis_dimension, kernel
):
    base, incident = probe.build_incident_updates(
        z_right, basis_id, orientation, basis_dimension
    )
    values = []
    for variable in range(probe.NV):
        basis_value = base - 2 * incident[variable]
        values.append(probe.q_values(basis_value, kernel))

    seen_pairs = set()
    pairs = []
    for a in range(probe.NV):
        b = (137 * a + 53) % probe.NV
        if b == a:
            b = (b + 1) % probe.NV
        u, v = sorted((a, b))
        if (u, v) in seen_pairs:
            continue
        seen_pairs.add((u, v))
        pairs.append((u, v))
        correction = probe.pair_basis_contribution(
            z_right, u, v, basis_id, orientation, basis_dimension
        )
        basis_value = (
            base - 2 * incident[u] - 2 * incident[v] + 4 * correction
        )
        values.append(probe.q_values(basis_value, kernel))
    return values, pairs


def weighted_gram(weights, values):
    dimension = len(values[0])
    matrix = [[0 for _ in range(dimension)] for _ in range(dimension)]
    for weight, vector in zip(weights, values):
        for i in range(dimension):
            left = int(weight) * int(vector[i])
            for j in range(i, dimension):
                matrix[i][j] += left * int(vector[j])
    for i in range(dimension):
        for j in range(i):
            matrix[i][j] = matrix[j][i]
    return matrix


def matrix_hash(matrix):
    return hashlib.sha256(
        json.dumps(matrix, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    if len(sys.argv) != 4:
        die("usage: checker.py MAT SYSTEM CERTIFICATE")
    mat_path, system_path, certificate_path = map(Path, sys.argv[1:])
    probe = load_probe()
    probe.init_pairs()
    certificate = json.load(open(certificate_path))

    if certificate.get("schema") != "d4-two-1d-blocks-weighted-evaluation-v1":
        die("wrong certificate schema")
    if int(certificate.get("weight_denominator", 0)) <= 0:
        die("weight denominator is not positive")
    if probe.file_md5(mat_path) != probe.EXPECTED_MD5:
        die("MAT MD5 mismatch")

    with h5py.File(mat_path, "r") as handle:
        objective = probe.exact_int_matrix(handle["A"][()], "A")
        ax = probe.exact_sign_vector(handle["ax"][()], "ax")
        by = probe.exact_sign_vector(handle["by"][()], "by")
    if probe.canonical_A_sha(objective) != certificate["A_sha256"]:
        die("canonical A SHA mismatch")
    if not np.array_equal(objective, objective.T):
        die("the frozen objective is not symmetric")

    system = json.load(open(system_path))
    generators = []
    for record in system["group"]["coxeter_generators"]:
        permutation = np.asarray(record["perm"], dtype=np.uint16)
        signs = np.asarray(record["sign"], dtype=np.int8)
        if not probe.preserves_A(objective, (permutation, signs)):
            die("a Coxeter generator does not preserve A")
        generators.append((permutation, signs))
    group_p, group_s, parent, _ = probe.generate_group(generators)
    if len(group_p) != 14400:
        die("wrong signed H4 group order")
    if probe.group_sha(group_p, group_s) != certificate["action_sha256"]:
        die("signed H4 action mismatch")
    character = coxeter_sign_character(
        probe, generators, group_p, group_s, parent
    )

    trivial_id, trivial_orientation, _, trivial_orbits = (
        probe.invariant_monomial_basis(generators, group_p, group_s)
    )
    sign_id, sign_orientation, sign_orbits = twisted_monomial_basis(
        probe, generators, group_p, group_s, character
    )
    sign_representatives = [record["rep"] for record in sign_orbits]
    if len(trivial_orbits) != 55:
        die("wrong trivial degree-at-most-two multiplicity")
    if sign_representatives != certificate["sign_orbit_representatives"]:
        die("wrong Coxeter-sign orbit representatives")

    left_fields = [
        sum(int(objective[i, j]) * int(by[j]) for j in range(probe.N))
        for i in range(probe.N)
    ]
    right_fields = [
        sum(int(ax[i]) * int(objective[i, j]) for i in range(probe.N))
        for j in range(probe.N)
    ]
    target_constant = sum(
        int(ax[i]) * int(objective[i, j]) * int(by[j])
        for i in range(probe.N)
        for j in range(probe.N)
    )
    if target_constant != int(certificate["target_C"]):
        die("target C mismatch")
    swapped_target_constant = sum(
        int(by[i]) * int(objective[i, j]) * int(ax[j])
        for i in range(probe.N)
        for j in range(probe.N)
    )
    if swapped_target_constant != target_constant:
        die("the swapped-left base point is not an equality point")
    zero_fields = [j for j, value in enumerate(right_fields) if value == 0]
    if zero_fields != [46, 56, 85, 99, 131, 148]:
        die("right zero-field set mismatch")
    z_right = np.concatenate([ax, by]).astype(np.int8)
    z_left = np.concatenate([by, ax]).astype(np.int8)

    trivial_rows, trivial_rank, trivial_kernel = equality_kernel(
        probe,
        z_right,
        z_left,
        zero_fields,
        trivial_id,
        trivial_orientation,
        len(trivial_orbits),
    )
    target_coordinates = probe.target_invariant_coordinates(
        objective, trivial_id, trivial_orientation, len(trivial_orbits)
    )
    trivial_payload = {
        "restriction_rows": trivial_rows,
        "primitive_nullspace_basis": trivial_kernel,
        "target_coordinates": target_coordinates,
    }
    if trivial_rank != 12 or len(trivial_kernel) != 43:
        die("wrong trivial equality-kernel dimensions")
    if canonical_hash(trivial_payload) != certificate["trivial_basis_hash"]:
        die("trivial equality-kernel hash mismatch")

    sign_rows, sign_rank, sign_kernel = equality_kernel(
        probe,
        z_right,
        z_left,
        zero_fields,
        sign_id,
        sign_orientation,
        len(sign_orbits),
    )
    sign_payload = {
        "active_representatives": sign_representatives,
        "restriction_rows": sign_rows,
        "primitive_nullspace_basis": sign_kernel,
    }
    if sign_rank != 2 or len(sign_kernel) != 17:
        die("wrong Coxeter-sign equality-kernel dimensions")
    if canonical_hash(sign_payload) != certificate["sign_basis_hash"]:
        die("Coxeter-sign equality-kernel hash mismatch")

    trivial_values, trivial_pairs = evaluation_vectors(
        probe,
        z_right,
        trivial_id,
        trivial_orientation,
        len(trivial_orbits),
        trivial_kernel,
    )
    sign_values, sign_pairs = evaluation_vectors(
        probe,
        z_right,
        sign_id,
        sign_orientation,
        len(sign_orbits),
        sign_kernel,
    )
    if trivial_pairs != sign_pairs or len(trivial_pairs) != 600:
        die("test-point pair recipe mismatch")

    target_values = [
        probe.f_single_flip(
            objective, ax, by, left_fields, right_fields, variable
        )
        for variable in range(probe.NV)
    ]
    target_values.extend(
        probe.f_double_flip(
            objective, ax, by, left_fields, right_fields, u, v
        )
        for u, v in trivial_pairs
    )
    # Independently evaluate the target on all 1200 Boolean points.  The
    # absolute-entry sum proves that every int64 dot product below is exact.
    absolute_bound = sum(abs(int(value)) for value in objective.flat)
    if absolute_bound >= 2**63:
        die("direct target self-test would risk int64 overflow")
    direct_target_values = []
    for flipped in [(variable,) for variable in range(probe.NV)] + [
        (u, v) for u, v in trivial_pairs
    ]:
        point = z_right.copy()
        for variable in flipped:
            point[variable] *= -1
        x = point[: probe.N].astype(np.int64)
        y = point[probe.N :].astype(np.int64)
        direct_target_values.append(
            target_constant - int(x @ objective @ y)
        )
    if direct_target_values != target_values:
        die("single/double-flip target formulas failed direct evaluation")

    weights = [int(value) for value in certificate["weight_numerators"]]
    if not (
        len(weights)
        == len(target_values)
        == len(trivial_values)
        == len(sign_values)
        == int(certificate["test_point_count"])
    ):
        die("weight/test-point count mismatch")

    trivial_gram = weighted_gram(weights, trivial_values)
    sign_gram = weighted_gram(weights, sign_values)
    trivial_hash = matrix_hash(trivial_gram)
    sign_hash = matrix_hash(sign_gram)
    if trivial_hash != certificate["trivial_gram_numerator_sha256"]:
        die("trivial weighted Gram hash mismatch")
    if sign_hash != certificate["sign_gram_numerator_sha256"]:
        die("Coxeter-sign weighted Gram hash mismatch")

    weighted_target = sum(
        weight * value for weight, value in zip(weights, target_values)
    )
    if str(weighted_target) != certificate["weighted_target_numerator"]:
        die("weighted target numerator mismatch")
    if weighted_target >= 0:
        die("weighted target is not strictly negative")

    trivial_pivots = exact_positive_ldl(trivial_gram)
    sign_pivots = exact_positive_ldl(sign_gram)
    for label, pivots in (
        ("trivial", trivial_pivots),
        ("sign", sign_pivots),
    ):
        last = pivots[-1]
        if str(last.numerator) != certificate[f"{label}_last_pivot_numerator"]:
            die(f"{label} last LDL pivot numerator mismatch")
        if str(last.denominator) != certificate[f"{label}_last_pivot_denominator"]:
            die(f"{label} last LDL pivot denominator mismatch")

    result = {
        "status": "EXACT_TWO_ONE_DIMENSIONAL_BLOCKS_SOS_NO_GO_VERIFIED",
        "scope": certificate["scope"],
        "certificate_sha256": sha256_file(certificate_path),
        "test_point_count": len(weights),
        "trivial_block_dimension": len(trivial_kernel),
        "sign_block_dimension": len(sign_kernel),
        "trivial_positive_ldl_pivots": len(trivial_pivots),
        "sign_positive_ldl_pivots": len(sign_pivots),
        "weighted_target_numerator": str(weighted_target),
        "trivial_gram_numerator_sha256": trivial_hash,
        "sign_gram_numerator_sha256": sign_hash,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
