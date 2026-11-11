#!/usr/bin/env python3
"""Exact checker for the H4-invariant-seed degree-four SOS no-go draft.

This verifies only the ansatz in which every degree-at-most-two SOS summand
is individually H4 invariant.  It does not test covariant/nontrivial-isotypic
summands and therefore does not decide the full degree-four SOS problem.

Usage:
  python h4_invariant_seed_nogo_checker.py MAT SYSTEM CERTIFICATE

Dependencies: numpy, h5py, sympy.
"""

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


def exact_positive_ldl(matrix):
    """Return exact LDL pivots; fail unless the symmetric matrix is PD."""
    n = len(matrix)
    L = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    diagonal = []
    for j in range(n):
        pivot = Fraction(matrix[j][j]) - sum(
            L[j][k] * L[j][k] * diagonal[k] for k in range(j)
        )
        if pivot <= 0:
            die(f"nonpositive exact LDL pivot {j}: {pivot}")
        diagonal.append(pivot)
        for i in range(j + 1, n):
            L[i][j] = (
                Fraction(matrix[i][j])
                - sum(L[i][k] * L[j][k] * diagonal[k] for k in range(j))
            ) / pivot
    return diagonal


def main():
    if len(sys.argv) != 4:
        die("usage: checker.py MAT SYSTEM CERTIFICATE")
    mat_path, system_path, certificate_path = map(Path, sys.argv[1:])
    probe = load_probe()
    cert = json.load(open(certificate_path))

    if cert.get("schema") != "d4-invariant-seed-weighted-evaluation-certificate-v1":
        die("wrong certificate schema")
    if int(cert.get("weight_denominator", 0)) <= 0:
        die("weight denominator is not positive")
    if probe.file_md5(mat_path) != probe.EXPECTED_MD5:
        die("MAT MD5 mismatch")

    with h5py.File(mat_path, "r") as handle:
        A = probe.exact_int_matrix(handle["A"][()], "A")
        ax = probe.exact_sign_vector(handle["ax"][()], "ax")
        by = probe.exact_sign_vector(handle["by"][()], "by")
    if probe.canonical_A_sha(A) != cert["A_sha256"]:
        die("canonical A SHA mismatch")

    system = json.load(open(system_path))
    generators = []
    for record in system["group"]["coxeter_generators"]:
        permutation = np.asarray(record["perm"], dtype=np.uint16)
        signs = np.asarray(record["sign"], dtype=np.int8)
        if not probe.preserves_A(A, (permutation, signs)):
            die("a Coxeter generator does not preserve A")
        generators.append((permutation, signs))
    GP, GS, _, _ = probe.generate_group(generators)
    if len(GP) != 14400 or probe.group_sha(GP, GS) != cert["action_sha256"]:
        die("signed H4 action mismatch")

    probe.init_pairs()
    basis_id, orient, _, invariant_orbits = probe.invariant_monomial_basis(
        generators, GP, GS
    )
    if len(invariant_orbits) != 55:
        die("unexpected invariant degree-at-most-two dimension")

    hleft = [
        sum(int(A[i, j]) * int(by[j]) for j in range(probe.N))
        for i in range(probe.N)
    ]
    hright = [
        sum(int(ax[i]) * int(A[i, j]) for i in range(probe.N))
        for j in range(probe.N)
    ]
    C = sum(
        int(ax[i]) * int(A[i, j]) * int(by[j])
        for i in range(probe.N) for j in range(probe.N)
    )
    if C != int(cert["target_C"]):
        die("target C mismatch")
    zero_fields = [j for j, value in enumerate(hright) if value == 0]
    if zero_fields != [46, 56, 85, 99, 131, 148]:
        die("right zero-field set mismatch")

    zR = np.concatenate([ax, by]).astype(np.int8)
    zL = np.concatenate([by, ax]).astype(np.int8)
    corners_R = probe.face_corners(zR, [probe.N + j for j in zero_fields])
    corners_L = probe.face_corners(zL, zero_fields)
    values_R = np.stack([
        probe.eval_invariant_basis(z, basis_id, orient, 55) for z in corners_R
    ])
    values_L = np.stack([
        probe.eval_invariant_basis(z, basis_id, orient, 55) for z in corners_L
    ])
    restriction_rows = (
        probe.face_restriction_matrix(values_R)
        + probe.face_restriction_matrix(values_L)
    )
    restriction = sp.Matrix(restriction_rows)
    if int(restriction.rank()) != 12:
        die("equality restriction rank is not 12")
    Kcols = [probe.primitive_integer_vector(v) for v in restriction.nullspace()]
    if len(Kcols) != int(cert["basis_dimension"]):
        die("invariant equality-vanishing basis dimension mismatch")
    fvec = probe.target_invariant_coordinates(A, basis_id, orient, 55)
    kernel_payload = json.dumps(
        {
            "restriction_rows": restriction_rows,
            "primitive_nullspace_basis": Kcols,
            "target_coordinates": fvec,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    if hashlib.sha256(kernel_payload).hexdigest() != cert["basis_hash"]:
        die("canonical invariant-kernel hash mismatch")

    base_invariant, incident = probe.build_incident_updates(
        zR, basis_id, orient, 55
    )
    q_values = []
    target_values = []
    for variable in range(probe.NV):
        invariant_value = base_invariant - 2 * incident[variable]
        q_values.append(probe.q_values(invariant_value, Kcols))
        target_values.append(
            probe.f_single_flip(A, ax, by, hleft, hright, variable)
        )
    seen_pairs = set()
    for a in range(probe.NV):
        b = (137 * a + 53) % probe.NV
        if b == a:
            b = (b + 1) % probe.NV
        u, v = sorted((a, b))
        if (u, v) in seen_pairs:
            continue
        seen_pairs.add((u, v))
        pair_correction = probe.pair_basis_contribution(
            zR, u, v, basis_id, orient, 55
        )
        invariant_value = (
            base_invariant - 2 * incident[u] - 2 * incident[v]
            + 4 * pair_correction
        )
        q_values.append(probe.q_values(invariant_value, Kcols))
        target_values.append(
            probe.f_double_flip(A, ax, by, hleft, hright, u, v)
        )

    weights = [int(x) for x in cert["weight_numerators"]]
    if len(weights) != len(q_values) or len(weights) != int(cert["test_point_count"]):
        die("weight/test-point count mismatch")
    dimension = len(Kcols)
    gram = [[0 for _ in range(dimension)] for _ in range(dimension)]
    for weight, vector in zip(weights, q_values):
        for i in range(dimension):
            for j in range(i, dimension):
                gram[i][j] += weight * int(vector[i]) * int(vector[j])
    for i in range(dimension):
        for j in range(i):
            gram[i][j] = gram[j][i]
    gram_hash = hashlib.sha256(
        json.dumps(gram, separators=(",", ":")).encode()
    ).hexdigest()
    if gram_hash != cert["gram_numerator_sha256"]:
        die("weighted Gram numerator hash mismatch")

    weighted_target = sum(
        weight * value for weight, value in zip(weights, target_values)
    )
    if str(weighted_target) != cert["weighted_target_numerator"]:
        die("weighted target numerator mismatch")
    if weighted_target >= 0:
        die("weighted target is not strictly negative")

    pivots = exact_positive_ldl(gram)
    last = pivots[-1]
    if (
        str(last.numerator) != cert["last_ldl_pivot_numerator"]
        or str(last.denominator) != cert["last_ldl_pivot_denominator"]
    ):
        die("last exact LDL pivot mismatch")

    result = {
        "status": "EXACT_INVARIANT_SEED_SOS_NO_GO_VERIFIED",
        "scope": cert["scope"],
        "certificate_sha256": sha256_file(certificate_path),
        "basis_dimension": dimension,
        "test_point_count": len(weights),
        "weighted_target_numerator": str(weighted_target),
        "exact_positive_ldl_pivots": len(pivots),
        "gram_numerator_sha256": gram_hash,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
