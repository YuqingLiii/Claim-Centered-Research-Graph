#!/usr/bin/env python3
"""Exact checker for the equality-face rank after 746825-coordinate pruning.

The earlier degree-four checker proves that the full 752621-coordinate
restriction map has rank 28.  This checker answers the separate question
whether those 28 dual directions remain independent after restricting the
primal coordinate set to the 746825 moment orbits that occur in (W-D)^2.

Usage:
  python h4_effective_equality_rank_checker.py \
    MAT SYSTEM NOGAP SPECDIR CERTIFICATE

The exhaustive upper-bound check is integer-only.  It verifies that the
sixteen degree-3/4 Walsh rows in the old 28-row basis vanish on every retained
moment orbit.  A 12x12 exact integer minor gives the matching lower bound.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import h5py
import numpy as np


P = 24001
N = 300
NV = 600
ORDER = 14400
EXPECTED_MAT_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_ACTION_SHA256 = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_SPEC_SHA256 = (
    "1b3f6fb54a17a3a55adc74ac277677ae2354f9e224174c639252763b6768b88c"
)
EXPECTED_PRODUCT_ID_SHA256 = (
    "c2c5a664bdc9e6885f32384b7fec0841bc8c6d929c7a432b700f4eab8a446a1d"
)
EXPECTED_PERM_SHA256 = (
    "eb6f70c53861e78a2059f8b776d413f136aa5d1823626e12f812a098d9d5bbdb"
)
EXPECTED_SIGN_SHA256 = (
    "33a922b15f0ad3d756e7583146472d984354b08441227c223fa288c838418a35"
)
EXPECTED_REP_SHA256 = {
    (2, 0): "34bdfc5986881e52a2ed7274e14b333d6038cd479a63cced592a13ea27533123",
    (1, 1): "a898c5d0cdcfb067b75ee349ad9755c13deb7eb36c6ebf0e1a0429734c06314b",
    (0, 2): "e38e12574a6d0a170db23b4e8ec5eaa1fbd684a9e1f2d37ae020e7dc6061d0c5",
    (4, 0): "3c6034ab103148bf6056330d3d483b8c5393eb9b4bceebf76caab549eb2134fa",
    (3, 1): "1c1dd9a62703f20b5d979ff66c2102a0d4a25c63f95c0ff15e7b735e0f96d6d7",
    (2, 2): "4185cf439964d5505db8c036b76c2aeda6e2d1ccf881faf371ed44495a4c266c",
    (1, 3): "c0ce7dd0611b84d4bf0d1658da165eae781cf24db115ec240b5616f9989669c2",
    (0, 4): "654c21fbb26fb1e5d9d185e5509390a0109d18083639a6fd286118ad10e1d92e",
}
OFFSETS = {
    (2, 0): 1,
    (1, 1): 17,
    (0, 2): 39,
    (4, 0): 55,
    (3, 1): 47212,
    (2, 2): 234908,
    (1, 3): 517768,
    (0, 4): 705464,
}
EXPECTED_ORIENTABLE = {
    (2, 0): 16,
    (1, 1): 22,
    (0, 2): 16,
    (4, 0): 47157,
    (3, 1): 187696,
    (2, 2): 282860,
    (1, 3): 187696,
    (0, 4): 47157,
}
EXPECTED_RETAINED = {
    (2, 0): 16,
    (1, 1): 22,
    (0, 2): 16,
    (4, 0): 45664,
    (3, 1): 186291,
    (2, 2): 282860,
    (1, 3): 186291,
    (0, 4): 45664,
}


def die(message):
    raise SystemExit("ERROR: " + str(message))


def digest(path, algorithm="sha256"):
    h = getattr(hashlib, algorithm)()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exact_sign_vector(raw, name):
    values = np.asarray(raw).reshape(-1)
    if len(values) != N:
        die(f"{name} has wrong length")
    out = np.empty(N, dtype=np.int8)
    for index, value in enumerate(values):
        number = float(value)
        if number == 1.0:
            out[index] = 1
        elif number == -1.0:
            out[index] = -1
        else:
            die(f"{name}[{index}] is not exactly +/-1")
    return out


def det_integer(matrix):
    """Fraction-free Bareiss determinant."""
    a = [[int(value) for value in row] for row in matrix]
    n = len(a)
    sign = 1
    previous = 1
    for column in range(n - 1):
        pivot = next((row for row in range(column, n) if a[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            sign = -sign
        value = a[column][column]
        for row in range(column + 1, n):
            for j in range(column + 1, n):
                numerator = a[row][j] * value - a[row][column] * a[column][j]
                if numerator % previous:
                    die("Bareiss exact division failed")
                a[row][j] = numerator // previous
        previous = value
    return sign * a[-1][-1]


def det_mod(matrix, prime=P):
    a = np.asarray(matrix, dtype=np.int64).copy() % prime
    d = 1
    for column in range(a.shape[0]):
        nonzero = np.flatnonzero(a[column:, column])
        if not len(nonzero):
            return 0
        pivot = column + int(nonzero[0])
        if pivot != column:
            a[[column, pivot]] = a[[pivot, column]]
            d = -d % prime
        value = int(a[column, column])
        d = d * value % prime
        a[column] = a[column] * pow(value, prime - 2, prime) % prime
        for row in range(column + 1, a.shape[0]):
            if a[row, column]:
                a[row] = (a[row] - int(a[row, column]) * a[column]) % prime
    return int(d)


def parse_reps(specdir, a, b):
    path = specdir / f"moment_reps_{a}_{b}.txt"
    if digest(path) != EXPECTED_REP_SHA256[(a, b)]:
        die(f"representative file hash mismatch for {(a, b)}")
    count = 0
    with open(path) as stream:
        for line in stream:
            idpart, rest = line.strip().split(" X:", 1)
            xpart, ypart = rest.split(" Y:", 1)
            local_id = int(idpart)
            if local_id != count:
                die(f"nonconsecutive local id in {(a, b)}")
            xs = [int(x) for x in xpart.rstrip(",").split(",") if x]
            ys = [N + int(y) for y in ypart.rstrip(",").split(",") if y]
            if len(xs) != a or len(ys) != b:
                die(f"wrong representative bidegree in {(a, b)}")
            yield OFFSETS[(a, b)] + local_id, tuple(xs + ys)
            count += 1
    if count != EXPECTED_ORIENTABLE[(a, b)]:
        die(f"wrong orientable representative count for {(a, b)}")


def main():
    if len(sys.argv) != 6:
        die("usage: checker.py MAT SYSTEM NOGAP SPECDIR CERTIFICATE")
    mat_path, system_path, nogap_path, specdir_path, certificate_path = map(
        Path, sys.argv[1:]
    )
    specdir = specdir_path
    certificate = json.load(open(certificate_path))
    if certificate.get("schema") != "d4-effective-equality-rank-v1":
        die("wrong certificate schema")

    if digest(mat_path, "md5") != EXPECTED_MAT_MD5:
        die("MAT MD5 mismatch")
    if digest(specdir / "full_invariant_dual_spec.json") != EXPECTED_SPEC_SHA256:
        die("full spec hash mismatch")
    if digest(specdir / "product_map.id.i32") != EXPECTED_PRODUCT_ID_SHA256:
        die("product id hash mismatch")
    if digest(specdir / "h4_perm_u16.bin") != EXPECTED_PERM_SHA256:
        die("permutation binary hash mismatch")
    if digest(specdir / "h4_sign_i8.bin") != EXPECTED_SIGN_SHA256:
        die("sign binary hash mismatch")

    nogap = load(nogap_path, "h4_nogap_effective_equality")
    _, _, group, _, _ = nogap.structural_construction()
    _, elements, _, action_sha = nogap.load_and_match_certified_action(
        system_path, group
    )
    if action_sha != EXPECTED_ACTION_SHA256:
        die("certified action hash mismatch")

    perm = np.array(
        np.memmap(
            specdir / "h4_perm_u16.bin",
            dtype="<u2",
            mode="r",
            shape=(ORDER, N),
        )
    )
    sign = np.array(
        np.memmap(
            specdir / "h4_sign_i8.bin",
            dtype="i1",
            mode="r",
            shape=(ORDER, N),
        )
    )
    if not np.array_equal(perm, np.stack([item[0] for item in elements])):
        die("serialized permutations differ from certified action")
    if not np.array_equal(sign, np.stack([item[1] for item in elements])):
        die("serialized signs differ from certified action")

    with h5py.File(mat_path, "r") as archive:
        ax = exact_sign_vector(archive["ax"][()], "ax")
        by = exact_sign_vector(archive["by"][()], "by")
    zero_lines = [46, 56, 85, 99, 131, 148]
    z_right = np.concatenate([ax, by])
    z_left = np.concatenate([by, ax])
    free_right = {N + line: bit for bit, line in enumerate(zero_lines)}
    free_left = {line: bit for bit, line in enumerate(zero_lines)}
    bit_right = np.zeros(NV, dtype=np.uint8)
    bit_left = np.zeros(NV, dtype=np.uint8)
    is_right = np.zeros(NV, dtype=bool)
    is_left = np.zeros(NV, dtype=bool)
    for variable, bit in free_right.items():
        bit_right[variable] = 1 << bit
        is_right[variable] = True
    for variable, bit in free_left.items():
        bit_left[variable] = 1 << bit
        is_left[variable] = True

    # Pull every variable back through every group element to both faces.
    # All entries remain int8/uint8, so subsequent arithmetic is exact.
    face_factors = []
    face_masks = []
    for bits, is_free, fixed in (
        (bit_right, is_right, z_right),
        (bit_left, is_left, z_left),
    ):
        factors = np.empty((NV, ORDER), dtype=np.int8)
        masks = np.empty((NV, ORDER), dtype=np.uint8)
        for variable in range(NV):
            party = variable >= N
            line = variable % N
            transform = perm[:, line].astype(np.int64) + (N if party else 0)
            factors[variable] = sign[:, line] * np.where(
                is_free[transform], 1, fixed[transform]
            )
            masks[variable] = bits[transform]
        face_factors.append(factors)
        face_masks.append(masks)

    walsh_masks = [mask for mask in range(64) if bin(mask).count("1") <= 4]

    def restriction(support):
        out = []
        for factors, masks in zip(face_factors, face_masks):
            pulled_mask = np.zeros(ORDER, dtype=np.uint8)
            values = np.ones(ORDER, dtype=np.int8)
            for variable in support:
                pulled_mask |= masks[variable]
                values *= factors[variable]
            bucket = (
                np.bincount(pulled_mask[values > 0], minlength=64)
                - np.bincount(pulled_mask[values < 0], minlength=64)
            ).astype(np.int64)
            out.extend(int(bucket[mask]) for mask in walsh_masks)
        return np.asarray(out, dtype=np.int64)

    # Replay the old full-coordinate 28-rank witness.  Its 28 selected rows
    # are therefore a row basis for the whole 114-row restriction matrix,
    # using the Burnside upper bound 14+14=28.
    old_supports = [tuple(row) for row in certificate["old_full_supports"]]
    old_rows = [int(value) for value in certificate["old_basis_rows"]]
    if len(old_supports) != 28 or len(old_rows) != 28:
        die("old full witness does not have size 28")
    old_matrix = np.column_stack([restriction(support) for support in old_supports])
    old_hash = hashlib.sha256(
        np.asarray(old_matrix, dtype="<i8").tobytes()
    ).hexdigest()
    if old_hash != certificate["old_restriction_matrix_sha256"]:
        die("old restriction matrix hash mismatch")
    old_det = det_mod(old_matrix[old_rows, :])
    if old_det != int(certificate["old_minor_det_mod_24001"]):
        die("old 28x28 modular minor mismatch")
    face_dimension = (57 + 3 * 7 + 2 * 3) // 6
    if face_dimension != 14:
        die("Burnside face dimension mismatch")

    product_ids = np.memmap(
        specdir / "product_map.id.i32",
        dtype="<i4",
        mode="r",
        shape=(1485, ORDER),
    )
    retained = np.unique(product_ids)
    retained = retained[retained >= 0]
    if len(retained) != 746825 or not np.array_equal(retained[:55], np.arange(55)):
        die("effective coordinate set mismatch")
    retained_set = set(map(int, retained))

    # The exact lower bound uses twelve retained low-degree orbit sums.
    lower_ids = [int(value) for value in certificate["lower_global_ids"]]
    lower_supports = [tuple(row) for row in certificate["lower_supports"]]
    lower_rows = [int(value) for value in certificate["lower_rows"]]
    if any(global_id not in retained_set for global_id in lower_ids):
        die("a lower-bound witness coordinate was pruned")
    lower_matrix = np.column_stack(
        [restriction(support) for support in lower_supports]
    )
    lower_det = det_integer(lower_matrix[lower_rows, :].tolist())
    if lower_det != int(certificate["lower_det_integer"]):
        die("exact 12x12 determinant mismatch")
    if not lower_det:
        die("lower determinant vanished")

    # The sixteen rows below are exactly the degree-3/4 rows among the old
    # 28-row basis.  Exhaustively prove that every retained orbit coordinate
    # is zero there.  This is an integer equality, not a finite-field test.
    vanishing_rows = [int(value) for value in certificate["vanishing_rows"]]
    if sorted(set(old_rows) - set(vanishing_rows)) != sorted(lower_rows):
        die("the proposed 12+16 split is not the old 28-row basis")
    if any(np.any(restriction(support)[vanishing_rows]) for support in lower_supports):
        die("a lower support violates a claimed vanishing row")

    checked = {}
    total_retained_reps = 1  # the constant orbit
    for a, b in ((2, 0), (1, 1), (0, 2), (4, 0), (3, 1), (2, 2), (1, 3), (0, 4)):
        retained_count = 0
        for global_id, support in parse_reps(specdir, a, b):
            if global_id not in retained_set:
                continue
            retained_count += 1
            vector = restriction(support)
            if np.any(vector[vanishing_rows]):
                bad = [
                    (row, int(vector[row]))
                    for row in vanishing_rows
                    if vector[row]
                ]
                die(f"effective coordinate {global_id} violates vanishing rows: {bad}")
            if retained_count % 25000 == 0:
                print(
                    f"checked bidegree {(a, b)}: {retained_count}",
                    file=sys.stderr,
                    flush=True,
                )
        if retained_count != EXPECTED_RETAINED[(a, b)]:
            die(f"wrong retained count for {(a, b)}")
        checked[f"{a},{b}"] = retained_count
        total_retained_reps += retained_count
    if total_retained_reps != 746825:
        die("retained representative census mismatch")

    # The projected old basis has sixteen support-one dependencies: each of
    # these directions is itself zero.  The other twelve have a nonsingular
    # exact minor, so this dependency list is complete and minimal.
    unit_dependencies = []
    for row in vanishing_rows:
        relation = [0] * 28
        relation[old_rows.index(row)] = 1
        unit_dependencies.append(relation)
    relation_hash = hashlib.sha256(
        json.dumps(unit_dependencies, separators=(",", ":")).encode()
    ).hexdigest()
    if relation_hash != certificate["unit_dependency_basis_sha256"]:
        die("unit dependency basis hash mismatch")

    output = {
        "status": "PROVED_EFFECTIVE_EQUALITY_RESTRICTION_RANK_12",
        "full_coordinate_count": 752621,
        "full_restriction_rank": 28,
        "effective_coordinate_count": 746825,
        "effective_restriction_rank": 12,
        "old_28_direction_dependency_dimension": 16,
        "minimal_dependencies": "sixteen support-one zero directions",
        "vanishing_rows": vanishing_rows,
        "lower_rows": lower_rows,
        "lower_det_integer": lower_det,
        "retained_representatives_checked": total_retained_reps,
        "retained_by_bidegree": checked,
        "corrected_effective_operator_kernel_lower_bound": 12,
        "corrected_effective_operator_rank_upper_bound": 746813,
        "refuted_claim": "projection preserves all 28 full restriction directions",
        "action_sha256": action_sha,
        "product_id_sha256": EXPECTED_PRODUCT_ID_SHA256,
        "unit_dependency_basis_sha256": relation_hash,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
