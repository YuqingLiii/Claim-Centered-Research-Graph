#!/usr/bin/env python3
"""Exact rank-20 CUT7 checker from two quadrilateral equality relations."""

import collections
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
RANK21_CHECKER = ROOT / (
    "grothendieck-d4/tools/"
    "h4_rank21_quadrilateral_orbit_checker.py"
)
EXPECTED_RANK21_CHECKER_SHA = (
    "21294c5aaba2aafeafe0a795464e3543ede8fa90512289454dc96a06c005c272"
)

CLUSTER = (0, 1, 2, 248, 268, 269, 288)
EXPECTED_PATTERNS = (
    0, 1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16, 18, 20, 28, 30,
    32, 34, 40, 44, 46, 48, 49, 50, 51, 52, 53, 56, 57, 60, 61, 62,
    63,
)

# Feature coordinates are constant followed by lexicographic CUT7 edges.
# Q1=x_05-x_06-x_15+x_16, on actual core (0,1,269,288).
NULL_Q1 = (
    0,
    0, 0, 0, 0, 1, -1,
    0, 0, 0, -1, 1,
    0, 0, 0, 0,
    0, 0, 0,
    0, 0,
    0,
)
# Q2=x_03-x_04-x_23+x_24, on actual core (0,2,248,268).
NULL_Q2 = (
    0,
    0, 0, 1, -1, 0, 0,
    0, 0, 0, 0, 0,
    -1, 1, 0, 0,
    0, 0, 0,
    0, 0,
    0,
)
RANK20_ROW_CODES = (
    0, 1, 2, 3, 4, 5, 8, 9, 12, 14, 16, 18, 20, 28, 32, 34, 40,
    44, 48, 49,
)
RANK20_COLUMNS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16,
                  17, 18, 19, 20, 21)
EXPECTED_CLUSTER_ORBIT_SHA = (
    "48931b756d544220564820b4701355b0c7f191a5c5092bf0872b406ea0188337"
)
EXPECTED_SIGNED_PAIR_ORBIT_SHA = (
    "a0ba7c275933803d23f08429c0ac743251611713add5d296793e371b68340c86"
)
EXPECTED_JOINT_VALUE_CENSUS = {
    (-2, -2): 1,
    (-2, 0): 6,
    (-2, 2): 1,
    (0, -2): 6,
    (0, 0): 36,
    (0, 2): 6,
    (2, -2): 1,
    (2, 0): 6,
    (2, 2): 1,
}


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_rank21_checker():
    if file_sha256(RANK21_CHECKER) != EXPECTED_RANK21_CHECKER_SHA:
        raise AssertionError("rank-21 checker SHA mismatch")
    spec = importlib.util.spec_from_file_location("rank21_checker", RANK21_CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def signed_pair_event_orbits(generators, a_switch, b_switch):
    """Exact orbits of relations s_a=epsilon*s_b under H4 plus party swap."""
    event_generators = []
    for permutation, signs in generators:
        inverse = np.empty(300, dtype=np.uint16)
        inverse[permutation] = np.arange(300, dtype=np.uint16)
        alpha_left = a_switch * signs * a_switch[permutation]
        alpha_right = b_switch * signs * b_switch[permutation]
        event_generators.append(
            (
                np.concatenate((inverse, 300 + inverse)).astype(np.uint16),
                np.concatenate((alpha_left, alpha_right)).astype(np.int8),
            )
        )
    swap_alpha = a_switch * b_switch
    event_generators.append(
        (
            np.concatenate((np.arange(300, 600), np.arange(300))).astype(
                np.uint16
            ),
            np.concatenate((swap_alpha, swap_alpha)).astype(np.int8),
        )
    )

    def act(event, generator):
        a, b, epsilon = event
        permutation, signs = generator
        aa = int(permutation[a])
        bb = int(permutation[b])
        image_epsilon = int(epsilon * signs[aa] * signs[bb])
        if aa < bb:
            return aa, bb, image_epsilon
        return bb, aa, image_epsilon

    unseen = {
        (a, b, epsilon)
        for a in range(600)
        for b in range(a + 1, 600)
        for epsilon in (-1, 1)
    }
    records = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        queue = collections.deque([seed])
        unseen.remove(seed)
        while queue:
            event = queue.popleft()
            for generator in event_generators:
                image = act(event, generator)
                if image not in orbit:
                    orbit.add(image)
                    unseen.discard(image)
                    queue.append(image)
        records.append((seed, len(orbit)))

    digest = hashlib.sha256()
    for (a, b, epsilon), size in records:
        digest.update(a.to_bytes(2, "little"))
        digest.update(b.to_bytes(2, "little"))
        digest.update(int(epsilon).to_bytes(1, "little", signed=True))
        digest.update(size.to_bytes(4, "little"))
    return records, digest.hexdigest()


def quadrilateral_relation_census(
    faces, generators, a_switch, b_switch, core_orbit
):
    """Classify every two-pair tautology up to the exact signed symmetry."""
    records, digest = signed_pair_event_orbits(generators, a_switch, b_switch)
    if len(records) != 70 or sum(size for _, size in records) != 359400:
        raise AssertionError("signed pair-event orbit census mismatch")
    if digest != EXPECTED_SIGNED_PAIR_ORBIT_SHA:
        raise AssertionError("signed pair-event orbit SHA mismatch")

    face_signs = np.stack([signs for _, signs in faces]).astype(np.int8)
    partners = {}
    for event, _ in records:
        a, b, epsilon = event
        first_good = face_signs[:, a] * face_signs[:, b] == epsilon
        restricted = face_signs[~first_good]
        groups = collections.defaultdict(list)
        for coordinate in range(600):
            if coordinate in (a, b) or np.any(restricted[:, coordinate] == 0):
                continue
            raw = restricted[:, coordinate].tobytes()
            negative = (-restricted[:, coordinate]).tobytes()
            if raw <= negative:
                groups[raw].append((coordinate, 1))
            else:
                groups[negative].append((coordinate, -1))
        event_partners = []
        for values in groups.values():
            for (c, orientation_c), (d, orientation_d) in itertools.combinations(
                values, 2
            ):
                second_epsilon = orientation_c * orientation_d
                second_good = face_signs[:, c] * face_signs[:, d] == second_epsilon
                if not np.all(first_good | second_good):
                    raise AssertionError("quadrilateral signature false positive")
                event_partners.append((c, d, second_epsilon))
        if event_partners:
            partners[event] = tuple(sorted(event_partners))

    expected = {
        (0, 1, 1): (
            (269, 288, 1),
            (286, 295, 1),
            (289, 299, 1),
        )
    }
    if partners != expected:
        raise AssertionError(f"quadrilateral relation census mismatch {partners}")
    supports = {
        tuple(sorted((event[0], event[1], partner[0], partner[1])))
        for event, event_partners in partners.items()
        for partner in event_partners
    }
    if not supports <= core_orbit or len(supports) != 3:
        raise AssertionError("quadrilateral supports escape the core orbit")
    return len(records), digest, len(supports)


def double_core_union_census(core_orbit):
    """Enumerate all pairs of distinct cores whose union fits in seven nodes."""
    cores = sorted(core_orbit)
    core_set = set(cores)
    incidence = collections.defaultdict(list)
    for index, core in enumerate(cores):
        for coordinate in core:
            incidence[coordinate].append(index)
    pairs = set()
    for indices in incidence.values():
        pairs.update(itertools.combinations(indices, 2))
    unions = collections.defaultdict(set)
    for i, j in pairs:
        union = tuple(sorted(set(cores[i]) | set(cores[j])))
        if len(union) <= 7:
            unions[len(union)].add(union)
    if set(unions) != {6, 7}:
        raise AssertionError(f"unexpected double-core union sizes {set(unions)}")
    if len(pairs) != 36000 or len(unions[6]) != 3600 or len(unions[7]) != 32400:
        raise AssertionError("double-core union census mismatch")
    if min(unions[7]) != CLUSTER:
        raise AssertionError("canonical double-core seven-union mismatch")
    for union in unions[7]:
        contained = sum(
            tuple(subset) in core_set for subset in itertools.combinations(union, 4)
        )
        if contained != 2:
            raise AssertionError("seven-union contains an unexpected core count")

    # A third core could in principle fit into a one-coordinate extension of
    # a size-six union.  An exact triple-incidence audit excludes this case.
    by_triple = collections.defaultdict(list)
    for core in cores:
        for triple in itertools.combinations(core, 3):
            by_triple[triple].append(core)
    for union in unions[6]:
        union_set = set(union)
        contained = {core for core in cores if set(core) <= union_set}
        if len(contained) != 2:
            raise AssertionError("size-six union core count mismatch")
        third_core_completions = set()
        for triple in itertools.combinations(union, 3):
            for core in by_triple[triple]:
                remainder = set(core) - union_set
                if len(remainder) == 1:
                    third_core_completions.add((core, next(iter(remainder))))
        if third_core_completions:
            raise AssertionError("a seven-set can contain three core-orbit members")
    return len(pairs), {size: len(items) for size, items in unions.items()}


def main():
    rank21 = load_rank21_checker()
    strength = rank21.load_strength_checker()
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

    # Systematic core-pair enumeration, independent of the rank computation.
    core_orbit = strength.cluster_orbit(rank21.CORE, generators)
    if len(core_orbit) != 1800:
        raise AssertionError("quadrilateral-core orbit mismatch")
    event_orbit_count, event_orbit_sha, relation_seed_count = (
        quadrilateral_relation_census(faces, generators, a, b, core_orbit)
    )
    pair_count, union_census = double_core_union_census(core_orbit)

    patterns = rank21.projected_patterns(CLUSTER, faces)
    if tuple(sorted(patterns)) != EXPECTED_PATTERNS:
        raise AssertionError("rank-20 cluster projection mismatch")
    for code in patterns:
        feature = rank21.cut_feature(code, 7)
        if sum(x * y for x, y in zip(feature, NULL_Q1)) != 0:
            raise AssertionError("first quadrilateral relation failed")
        if sum(x * y for x, y in zip(feature, NULL_Q2)) != 0:
            raise AssertionError("second quadrilateral relation failed")

    # Two independent null vectors prove rank <=20; this minor proves >=20.
    rank_minor = [
        [rank21.cut_feature(code, 7)[j] for j in RANK20_COLUMNS]
        for code in RANK20_ROW_CODES
    ]
    rank_determinant = strength.bareiss_determinant(rank_minor)
    if rank_determinant != -8192:
        raise AssertionError(f"unexpected rank-20 determinant {rank_determinant}")

    joint_values = collections.Counter()
    values = {}
    for code in range(64):
        feature = rank21.cut_feature(code, 7)
        pair = (
            sum(x * y for x, y in zip(feature, NULL_Q1)),
            sum(x * y for x, y in zip(feature, NULL_Q2)),
        )
        values[code] = pair
        joint_values[pair] += 1
    if dict(joint_values) != EXPECTED_JOINT_VALUE_CENSUS:
        raise AssertionError(f"unexpected joint null census {joint_values}")
    # Axis witnesses force both coefficients of any valid null combination
    # to vanish: +/-Q1 occur with Q2=0, and +/-Q2 occur with Q1=0.
    expected_witnesses = {17: (2, 0), 33: (-2, 0), 6: (0, 2), 10: (0, -2)}
    if any(values[code] != value for code, value in expected_witnesses.items()):
        raise AssertionError("two-dimensional no-facet witnesses changed")

    orbit = strength.cluster_orbit(CLUSTER, generators)
    if len(orbit) != 3600 or min(orbit) != CLUSTER:
        raise AssertionError("rank-20 seven-cluster orbit mismatch")
    orbit_sha = strength.orbit_sha(orbit)
    if orbit_sha != EXPECTED_CLUSTER_ORBIT_SHA:
        raise AssertionError("rank-20 orbit SHA mismatch")

    free_six_sets = set(tuple(variable) for variable, _ in faces)
    if any(
        CLUSTER[:omit] + CLUSTER[omit + 1 :] in free_six_sets
        for omit in range(7)
    ):
        raise AssertionError("rank-20 representative contains a terminal six-set")

    result = {
        "status": "EXACT_RANK20_DOUBLE_QUADRILATERAL_PASSED",
        "systematic_core_pair_census": {
            "signed_pair_event_orbits": event_orbit_count,
            "signed_pair_event_orbit_sha256": event_orbit_sha,
            "quadrilateral_relation_seed_supports": relation_seed_count,
            "all_quadrilateral_relations_form_one_core_orbit": True,
            "core_orbit_size": len(core_orbit),
            "intersecting_core_pairs": pair_count,
            "union_size_census": union_census,
            "every_size7_union_contains_exactly_two_cores": True,
            "no_seven_set_contains_three_cores": True,
        },
        "canonical_cluster": list(CLUSTER),
        "projected_CUT7_vertices": len(patterns),
        "exact_feature_rank": 20,
        "rank_minor_determinant": rank_determinant,
        "nullspace_basis": [
            "x_05-x_06-x_15+x_16",
            "x_03-x_04-x_23+x_24",
        ],
        "joint_null_value_census": {
            str(pair): count for pair, count in sorted(joint_values.items())
        },
        "no_valid_null_combination_witnesses": {
            str(code): list(value) for code, value in expected_witnesses.items()
        },
        "cluster_orbit": {"size": len(orbit), "sha256": orbit_sha},
        "refuted_route": (
            "The two-dimensional nullspace intersects the cone of valid "
            "CUT_7 inequalities only at zero, so it supplies no cut facet."
        ),
        "scope": (
            "This exactly classifies one rank-20 orbit and completely "
            "enumerates pairwise unions inside the known 1800-core orbit; "
            "it does not classify all seven-cluster orbits."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
