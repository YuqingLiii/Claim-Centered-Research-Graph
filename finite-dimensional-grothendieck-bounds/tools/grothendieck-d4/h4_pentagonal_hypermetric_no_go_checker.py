#!/usr/bin/env python3
"""Exact H4-reduced no-go checker for five-term hypermetrics.

The checker proves that no vector with five nonzero coefficients in {+1,-1}
is tight on all 307200 currently known C-level cuts.  In particular, it
excludes every pentagonal vector e_i+e_j+e_k-e_l-e_m.

The finite search uses the exact six-face decomposition, not floating point.
After H4 symmetry fixes one signed literal to +e_0, the 48 faces in which
coordinate 0 is free give a meet-in-the-middle signature for the other four
literals.  Every surviving complementary pair of pairs is then checked on
all 4800 equality faces.
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


def signed_literal_orbit(base, generators, a):
    """Orbit of the partial sign assignment ((0,+1),) in bit convention."""
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


def build_faces(base, group, a, b, zero_columns):
    """Return a deterministic list (variable coordinates, fixed signs)."""
    records = set()
    for p, s in group:
        variable = tuple(
            sorted(int(i) for i in np.flatnonzero(np.isin(p, zero_columns)))
        )
        right = (
            base.packed((a * s * a[p]) < 0),
            base.packed((b * s * b[p]) < 0),
            variable,
        )
        left = (
            base.packed((a * s * b[p]) < 0),
            variable,
            base.packed((b * s * a[p]) < 0),
        )
        records.add(("right", right))
        records.add(("left", left))

    faces = []
    for family, face in sorted(records):
        if family == "right":
            left_blob, right_blob, variable = face
            variable_indices = tuple(300 + i for i in variable)
        else:
            left_blob, variable, right_blob = face
            variable_indices = tuple(variable)
        bits = np.concatenate((base.unpacked(left_blob), base.unpacked(right_blob)))
        signs = (1 - 2 * bits.astype(np.int8)).astype(np.int8)
        signs[list(variable_indices)] = 0
        faces.append((variable_indices, signs))
    return faces


def exact_correlation(faces):
    fixed = np.stack([signs for _, signs in faces]).astype(np.int64)
    correction = np.zeros(600, dtype=np.int64)
    for variable, _ in faces:
        correction[list(variable)] += 64
    C = 64 * (fixed.T @ fixed)
    C[np.diag_indices(600)] += correction
    return C


def seven_cluster_orbit_census(faces, generators):
    """Census clusters V union {j}, where V is a terminal free six-set."""
    six_sets = sorted(set(tuple(variable) for variable, _ in faces))
    if len(six_sets) != 1200:
        raise AssertionError(f"terminal free-six-set count {len(six_sets)}")
    clusters = set()
    for variable in six_sets:
        variable_set = set(variable)
        for j in range(600):
            if j not in variable_set:
                clusters.add(tuple(sorted(variable + (j,))))
    # There are no duplicate extensions, a useful independent incidence check.
    if len(clusters) != 1200 * 594:
        raise AssertionError(f"seven-cluster count {len(clusters)}")

    coordinate_generators = [
        np.concatenate((p, 300 + p)).astype(np.uint16) for p, _ in generators
    ]
    coordinate_generators.append(
        np.concatenate((np.arange(300, 600), np.arange(300))).astype(np.uint16)
    )
    unseen = set(clusters)
    orbit_sizes = collections.Counter()
    while unseen:
        seed = unseen.pop()
        orbit = {seed}
        queue = collections.deque([seed])
        while queue:
            cluster = queue.popleft()
            for permutation in coordinate_generators:
                image = tuple(sorted(int(permutation[i]) for i in cluster))
                if image not in clusters:
                    raise AssertionError("seven-cluster family is not invariant")
                if image not in orbit:
                    orbit.add(image)
                    unseen.discard(image)
                    queue.append(image)
        orbit_sizes[len(orbit)] += 1
    expected = collections.Counter({14400: 32, 7200: 31, 2400: 6, 3600: 4})
    if orbit_sizes != expected:
        raise AssertionError(f"seven-cluster orbit census {orbit_sizes}")
    return len(six_sets), len(clusters), orbit_sizes


def main():
    base = load_base_checker()
    with h5py.File(base.MAT, "r") as f:
        A = base.exact_int_matrix(f["A"][()], "A")
        a = base.exact_sign_vector(f["ax"][()], "ax")
        b = base.exact_sign_vector(f["by"][()], "by")
    if not np.array_equal(A, A.T):
        raise AssertionError("party-swap reduction requires exact symmetry of A")

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
    literal_orbit = signed_literal_orbit(base, generators, a)
    if len(literal_orbit) != 600:
        raise AssertionError("signed left literals are not one H4 orbit")

    B, _, columns = base.exact_switched_data(A, a, b)
    zero_columns = tuple(j for j, value in enumerate(columns) if value == 0)
    if zero_columns != (46, 56, 85, 99, 131, 148):
        raise AssertionError("zero-column set mismatch")
    faces = build_faces(base, group, a, b, zero_columns)
    if len(faces) != 4800:
        raise AssertionError(f"equality face count {len(faces)}")

    # Reconstruct the exact 600-by-600 correlation matrix M of the known cuts.
    C = exact_correlation(faces)
    Csha = correlation_sha(C)
    if Csha != EXPECTED_CORRELATION_SHA:
        raise AssertionError("exact correlation matrix SHA mismatch")
    if set(int(x) for x in np.diag(C)) != {KNOWN_CUT_COUNT}:
        raise AssertionError("exact correlation diagonal mismatch")

    signs = np.stack([row for _, row in faces]).astype(np.int8)
    incidence = (signs == 0).astype(np.int8)
    containing_zero = np.flatnonzero(incidence[:, 0])
    not_containing_zero = np.flatnonzero(~incidence[:, 0].astype(bool))
    if len(containing_zero) != 48:
        raise AssertionError("coordinate 0 should be free in exactly 48 faces")
    order = np.concatenate((containing_zero, not_containing_zero))
    signs = signs[order]
    incidence = incidence[order]

    # Two selected coordinates cannot be simultaneously free in a terminal
    # face.  Otherwise varying the two independent signs makes |b.u|=1 on all
    # vertices impossible.  Record this exact co-freeness conflict relation.
    conflict = np.zeros((600, 600), dtype=bool)
    for variable, _ in faces:
        for i in variable:
            conflict[i, list(variable)] = True
    np.fill_diagonal(conflict, True)

    # H4 transitivity plus party swap permits fixing one signed literal to
    # +e_0.  Remove coordinates conflicting with 0, then include both signs.
    coordinates = np.asarray(
        [j for j in range(1, 600) if not conflict[0, j]], dtype=np.int16
    )
    if len(coordinates) != 555:
        raise AssertionError(f"allowed coordinate count {len(coordinates)}")
    literal_coordinate = np.repeat(coordinates, 2)
    literal_sign = np.tile(np.asarray([-1, 1], dtype=np.int8), len(coordinates))
    literal_value = (signs[:, literal_coordinate] * literal_sign).T
    literal_incidence = incidence[:, literal_coordinate].T
    if len(literal_coordinate) != 1110:
        raise AssertionError("signed literal count mismatch")

    # Enumerate every locally legal unordered pair of the remaining literals
    # and bucket it by its exact contribution on the 48 zero-containing faces.
    buckets = collections.defaultdict(list)
    pairs = []
    for u in range(len(literal_coordinate)):
        i = int(literal_coordinate[u])
        for v in range(u + 1, len(literal_coordinate)):
            j = int(literal_coordinate[v])
            if conflict[i, j]:
                continue
            pair_index = len(pairs)
            pairs.append((u, v))
            signature = (literal_value[u, :48] + literal_value[v, :48]).tobytes()
            buckets[signature].append(pair_index)
    pair_array = np.asarray(pairs, dtype=np.int32)
    pair_coordinates = literal_coordinate[pair_array]
    if len(pair_array) != 568692 or len(buckets) != 134755:
        raise AssertionError(
            f"unexpected pair census {(len(pair_array), len(buckets))}"
        )

    # Four literals sum to zero on the 48 faces iff their two pair signatures
    # are negatives.  Test every unordered complementary pair of pair-buckets.
    # Cross-conflicts enforce r<=1 on every face.  The exact face condition is
    # |fixed sum| = 1-r, where r is the number of selected free coordinates.
    raw_complementary_pairings = 0
    globally_conflict_free_pairings = 0
    fully_compatible = 0
    keys = set(buckets)
    for key in sorted(keys):
        signature = np.frombuffer(key, dtype=np.int8)
        negative_key = (-signature).astype(np.int8).tobytes()
        if negative_key not in buckets or key > negative_key:
            continue
        first_bucket = np.asarray(buckets[key], dtype=np.int32)
        second_bucket = np.asarray(buckets[negative_key], dtype=np.int32)
        for first_pair in first_bucket:
            candidates = second_bucket
            if key == negative_key:
                candidates = candidates[candidates > first_pair]
            raw_complementary_pairings += len(candidates)
            if not len(candidates):
                continue

            left_coordinates = pair_coordinates[first_pair]
            right_coordinates = pair_coordinates[candidates]
            good = (
                (right_coordinates[:, 0] != left_coordinates[0])
                & (right_coordinates[:, 1] != left_coordinates[0])
                & (right_coordinates[:, 0] != left_coordinates[1])
                & (right_coordinates[:, 1] != left_coordinates[1])
            )
            good &= ~conflict[left_coordinates[0], right_coordinates[:, 0]]
            good &= ~conflict[left_coordinates[0], right_coordinates[:, 1]]
            good &= ~conflict[left_coordinates[1], right_coordinates[:, 0]]
            good &= ~conflict[left_coordinates[1], right_coordinates[:, 1]]
            candidates = candidates[good]
            globally_conflict_free_pairings += len(candidates)
            if not len(candidates):
                continue

            # Progressive exact filtering is only a speed optimization.  The
            # final stage includes all 4800 faces and is the certificate.
            for stop in (56, 80, 176, 4800):
                rows = slice(48, stop)
                p = pair_array[first_pair]
                q = pair_array[candidates]
                fixed_sum = (
                    signs[rows, 0].astype(np.int16)
                    + literal_value[p[0], rows]
                    + literal_value[p[1], rows]
                    + literal_value[q[:, 0], rows]
                    + literal_value[q[:, 1], rows]
                )
                free_count = (
                    incidence[rows, 0].astype(np.int16)
                    + literal_incidence[p[0], rows]
                    + literal_incidence[p[1], rows]
                    + literal_incidence[q[:, 0], rows]
                    + literal_incidence[q[:, 1], rows]
                )
                keep = np.all(np.abs(fixed_sum) == 1 - free_count, axis=1)
                candidates = candidates[keep]
                if not len(candidates):
                    break
            fully_compatible += len(candidates)

    if raw_complementary_pairings != 3164360:
        raise AssertionError(
            f"raw complementary pairing census {raw_complementary_pairings}"
        )
    if globally_conflict_free_pairings != 652266:
        raise AssertionError(
            "globally conflict-free pairing census "
            f"{globally_conflict_free_pairings}"
        )
    if fully_compatible != 0:
        raise AssertionError(f"found {fully_compatible} compatible five-terms")

    six_set_count, seven_cluster_count, seven_orbits = seven_cluster_orbit_census(
        faces, generators
    )

    result = {
        "status": "EXACT_PENTAGONAL_NO_GO_PASSED",
        "known_C_level_cuts": KNOWN_CUT_COUNT,
        "correlation_matrix_sha256": Csha,
        "symmetry_reduction": {
            "signed_left_literal_orbit_size": len(literal_orbit),
            "fixed_literal": "+e_0",
            "faces_containing_fixed_coordinate": len(containing_zero),
            "remaining_allowed_coordinates": len(coordinates),
            "remaining_signed_literals": len(literal_coordinate),
        },
        "meet_in_the_middle_census": {
            "locally_legal_literal_pairs": len(pair_array),
            "pair_signature_buckets": len(buckets),
            "raw_complementary_pairings": raw_complementary_pairings,
            "globally_conflict_free_pairings": globally_conflict_free_pairings,
            "fully_compatible_five_term_vectors": fully_compatible,
        },
        "seven_coordinate_local_facet_no_go": {
            "terminal_free_six_sets": six_set_count,
            "clusters_equal_to_free_six_set_plus_one_coordinate": (
                seven_cluster_count
            ),
            "H4_plus_party_swap_orbit_count": sum(seven_orbits.values()),
            "orbit_size_census": {
                str(size): count for size, count in sorted(seven_orbits.items())
            },
            "conclusion": (
                "Each such cluster projects one known terminal face onto all "
                "64 vertices of CUT_7.  Therefore no proper local CUT_7 "
                "facet, hypermetric or non-hypermetric, can be tight on all "
                "known equality cuts when supported on one of these clusters."
            ),
        },
        "conclusion": (
            "No vector with exactly five nonzero coefficients in {+1,-1} "
            "has b^T M b=307200.  Hence no pentagonal hypermetric is tight "
            "on all currently known C-level cuts."
        ),
        "scope": (
            "This is a complete five-term hypermetric no-go relative to the "
            "307200 certified equality cuts.  It also excludes every proper "
            "seven-node local facet on 712800 specified clusters, but not on "
            "arbitrary seven-node clusters.  It does not prove that the known "
            "cuts exhaust every C-level cut."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
