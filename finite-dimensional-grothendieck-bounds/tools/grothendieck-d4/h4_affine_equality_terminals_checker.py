#!/usr/bin/env python3
"""Exact checker for affine H4 symmetry and equality terminals of the d=4 cut.

The checker uses only exact integer/discrete operations after verifying that
the HDF5 inputs are exactly integral.  It proves the finite statements quoted
in d4-affine-h4-equality-terminals-20260830.md.

Run from the repository root in an environment containing numpy and h5py:

  python grothendieck-d4/tools/h4_affine_equality_terminals_checker.py
"""

import collections
import hashlib
import json
import math
from pathlib import Path

import h5py
import numpy as np


N = 300
EXPECTED_C = 2081044153087351400
EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_A_SHA = "5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5"
EXPECTED_ACTION_SHA = "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"

ROOT = Path(__file__).resolve().parents[2]
MAT = ROOT / "grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")


def fail(message):
    raise AssertionError(message)


def file_md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical_A_sha(A):
    h = hashlib.sha256()
    for x in A.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def exact_int_matrix(raw, name):
    a = np.asarray(raw)
    if a.shape != (N, N):
        fail(f"{name}: shape {a.shape}")
    out = np.empty((N, N), dtype=np.int64)
    it = np.nditer(a, flags=["multi_index"])
    for z in it:
        x = float(z)
        q = int(x)
        if not math.isfinite(x) or float(q) != x:
            fail(f"{name}{it.multi_index}: not exactly integral")
        out[it.multi_index] = q
    return out


def exact_sign_vector(raw, name):
    a = np.asarray(raw).reshape(-1)
    if len(a) != N:
        fail(f"{name}: length {len(a)}")
    out = np.empty(N, dtype=np.int8)
    for i, z in enumerate(a):
        x = float(z)
        if x not in (-1.0, 1.0):
            fail(f"{name}[{i}]: not a sign")
        out[i] = int(x)
    return out


def compose(g, h):
    """Composition in the signed-permutation convention used by the archive."""
    p, s = g
    q, t = h
    return q[p].astype(np.uint16, copy=False), (s * t[p]).astype(np.int8, copy=False)


def group_key(g):
    p, s = g
    return p.tobytes() + np.packbits(s > 0).tobytes()


def generate_group(generators):
    identity = (np.arange(N, dtype=np.uint16), np.ones(N, dtype=np.int8))
    group = [identity]
    seen = {group_key(identity)}
    queue = collections.deque([identity])
    while queue:
        h = queue.popleft()
        for generator in generators:
            z = compose(h, generator)
            key = group_key(z)
            if key not in seen:
                seen.add(key)
                group.append((z[0].copy(), z[1].copy()))
                queue.append(group[-1])
                if len(group) > 14400:
                    fail("generated group exceeded 14400")
    return group


def group_sha(group):
    h = hashlib.sha256()
    for key in sorted(group_key(g) for g in group):
        h.update(key)
    return h.hexdigest()


def preserves_A(A, g):
    p, s = g
    return np.array_equal(A, s[:, None] * A[p][:, p] * s[None, :])


def packed(bits):
    return np.packbits(np.asarray(bits, dtype=np.uint8)).tobytes()


def unpacked(blob):
    return np.unpackbits(np.frombuffer(blob, dtype=np.uint8))[:N].astype(np.uint8)


def xor_subset(center_blob, variable_coordinates, mask):
    bits = unpacked(center_blob)
    for k, i in enumerate(variable_coordinates):
        bits[i] ^= (mask >> k) & 1
    return packed(bits)


def act_partial_assignment(node, inverse_permutation, alpha):
    """Apply s' = s[p] xor alpha to a sparse ternary assignment.

    ``node`` lists only fixed coordinates; all omitted coordinates are free.
    """
    image = []
    for coordinate, value in node:
        output_coordinate = int(inverse_permutation[coordinate])
        image.append((output_coordinate, int(value) ^ int(alpha[output_coordinate])))
    return tuple(sorted(image))


def partial_assignment_orbits(action_generators, fixed_count):
    if fixed_count == 1:
        unseen = {((i, value),) for i in range(N) for value in (0, 1)}
    elif fixed_count == 2:
        unseen = {
            ((i, vi), (j, vj))
            for i in range(N)
            for j in range(i + 1, N)
            for vi in (0, 1)
            for vj in (0, 1)
        }
    else:
        fail("only the first two nontrivial coverage layers are checked")

    orbit_sizes = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        queue = collections.deque([seed])
        while queue:
            node = queue.popleft()
            for inverse_permutation, alpha in action_generators:
                image = act_partial_assignment(node, inverse_permutation, alpha)
                if image not in orbit:
                    orbit.add(image)
                    queue.append(image)
        unseen.difference_update(orbit)
        orbit_sizes.append(len(orbit))
    return collections.Counter(orbit_sizes)


def exact_switched_data(A, a, b):
    B = [[int(a[i]) * int(A[i, j]) * int(b[j]) for j in range(N)] for i in range(N)]
    rows = [sum(B[i]) for i in range(N)]
    cols = [sum(B[i][j] for i in range(N)) for j in range(N)]
    return B, rows, cols


def exact_F_and_fields(s_bits, B, rows, cols):
    selected = [i for i, bit in enumerate(s_bits) if bit]
    q = [sum(B[i][j] for i in selected) for j in range(N)]
    fields = [cols[j] - 2 * q[j] for j in range(N)]
    value = sum(rows[i] for i in selected) + sum(min(0, x) for x in fields)
    return value, fields


def main():
    if file_md5(MAT) != EXPECTED_MD5:
        fail("MAT MD5 mismatch")

    with h5py.File(MAT, "r") as f:
        A = exact_int_matrix(f["A"][()], "A")
        a = exact_sign_vector(f["ax"][()], "ax")
        b = exact_sign_vector(f["by"][()], "by")

    if canonical_A_sha(A) != EXPECTED_A_SHA:
        fail("canonical A SHA mismatch")
    if not np.array_equal(A, A.T):
        fail("A is not exactly symmetric")

    with open(SYSTEM) as f:
        system = json.load(f)
    generators = []
    for g in system["group"]["coxeter_generators"]:
        p = np.asarray(g["perm"], dtype=np.uint16)
        s = np.asarray(g["sign"], dtype=np.int8)
        if p.shape != (N,) or sorted(int(x) for x in p) != list(range(N)):
            fail("invalid generator permutation")
        if s.shape != (N,) or not np.all((s == 1) | (s == -1)):
            fail("invalid generator signs")
        if not preserves_A(A, (p, s)):
            fail("generator does not preserve A")
        generators.append((p, s))

    group = generate_group(generators)
    if len(group) != 14400:
        fail(f"signed group order {len(group)}")
    action_sha = group_sha(group)
    if action_sha != EXPECTED_ACTION_SHA:
        fail("full signed action SHA mismatch")

    # Exact early-layer census for a ternary coverage DAG.  A node stores
    # fixed 0/1 coordinates; all other coordinates are free.
    partial_actions = []
    for p, s in generators:
        inverse = np.empty(N, dtype=np.uint16)
        inverse[p] = np.arange(N, dtype=np.uint16)
        alpha = ((a * s * a[p]) < 0).astype(np.uint8)
        partial_actions.append((inverse, alpha))
    layer_one = partial_assignment_orbits(partial_actions, 1)
    layer_two = partial_assignment_orbits(partial_actions, 2)
    if layer_one != collections.Counter({600: 1}):
        fail(f"unexpected one-fixed-coordinate orbit census {layer_one}")
    expected_layer_two = collections.Counter({
        1200: 6,
        1800: 1,
        2400: 2,
        3600: 6,
        7200: 18,
        14400: 1,
    })
    if layer_two != expected_layer_two:
        fail(f"unexpected two-fixed-coordinate orbit census {layer_two}")

    B, rows, cols = exact_switched_data(A, a, b)
    C = sum(rows)
    if C != EXPECTED_C:
        fail(f"candidate value {C}")
    zero_columns = tuple(j for j, x in enumerate(cols) if x == 0)
    if zero_columns != (46, 56, 85, 99, 131, 148):
        fail(f"unexpected zero columns {zero_columns}")
    if min(cols) < 0:
        fail("base right face is not minimizing")
    base_zero, base_fields = exact_F_and_fields(np.zeros(N, dtype=np.uint8), B, rows, cols)
    if base_zero != 0 or tuple(j for j, x in enumerate(base_fields) if x == 0) != zero_columns:
        fail("base right six-face check failed")

    # Party swap turns the right six-face into a left six-face centered at
    # delta=(a!=b), with the right assignment fixed at delta.
    delta = (a != b).astype(np.uint8)
    if int(delta.sum()) != 83:
        fail("unexpected party-swap support")
    base_left_values = []
    for mask in range(1 << len(zero_columns)):
        s_bits = delta.copy()
        for k, i in enumerate(zero_columns):
            s_bits[i] ^= (mask >> k) & 1
        value, fields = exact_F_and_fields(s_bits, B, rows, cols)
        if value != 0:
            fail(f"base swapped face mask {mask}: F={value}")
        if any(x == 0 for x in fields):
            fail(f"base swapped face mask {mask}: nonunique right minimizer")
        minimizing_t = np.asarray([x < 0 for x in fields], dtype=np.uint8)
        if not np.array_equal(minimizing_t, delta):
            fail(f"base swapped face mask {mask}: wrong right minimizer")
        base_left_values.append(value)

    alpha_counts = collections.Counter()
    right_terminals = set()
    left_terminals = set()
    for p, s in group:
        # For x=a*(-1)^u and y=b*(-1)^v, the transformed flip variables are
        # u'=u[p] xor alpha and v'=v[p] xor beta.
        alpha = packed((a * s * a[p]) < 0)
        beta = packed((b * s * b[p]) < 0)
        alpha_counts[alpha] += 1
        variable = tuple(sorted(int(i) for i in np.flatnonzero(np.isin(p, zero_columns))))
        if len(variable) != 6:
            fail("image face lost a variable coordinate")

        # Image of the base right face: left alpha fixed, right beta+<V>.
        right_terminals.add((alpha, beta, variable))

        # Image of the party-swapped base face: left center+<V>, right fixed.
        left_center = packed((a * s * b[p]) < 0)
        fixed_right = packed((b * s * a[p]) < 0)
        left_terminals.add((left_center, variable, fixed_right))

    if len(alpha_counts) != 2400 or set(alpha_counts.values()) != {6}:
        fail("unexpected affine translation orbit/stabilizer")
    if len(right_terminals) != 2400 or len(left_terminals) != 2400:
        fail("unexpected equality-face orbit size")

    # Exhaustive discrete incidence check for all 2400*64 terminal points.
    left_face_incidence = collections.Counter()
    right_family_pairs = set()
    left_family_pairs = set()

    for alpha, beta, variable in right_terminals:
        for mask in range(64):
            t = xor_subset(beta, variable, mask)
            right_family_pairs.add(alpha + t)

    for center, variable, fixed_right in left_terminals:
        for mask in range(64):
            left = xor_subset(center, variable, mask)
            left_face_incidence[left] += 1
            left_family_pairs.add(left + fixed_right)

    left_face_points = set(left_face_incidence)
    alpha_points = set(alpha_counts)
    if len(left_face_points) != 153600 or set(left_face_incidence.values()) != {1}:
        fail("the 2400 left six-faces are not pairwise disjoint")
    if alpha_points & left_face_points:
        fail("fixed-left and left-face terminal sets overlap")
    if len(right_family_pairs) != 153600 or len(left_family_pairs) != 153600:
        fail("unexpected number of C-level pairs")
    if right_family_pairs & left_family_pairs:
        fail("right-face and swapped-left-face pair families overlap")

    result = {
        "status": "EXACT_CHECK_PASSED",
        "input": {
            "mat_md5": EXPECTED_MD5,
            "A_sha256": EXPECTED_A_SHA,
            "signed_action_sha256": action_sha,
        },
        "candidate_value_C": C,
        "affine_H4": {
            "signed_group_order": len(group),
            "left_translation_points": len(alpha_points),
            "translation_stabilizer_order": next(iter(alpha_counts.values())),
        },
        "canonical_coverage_layers": {
            "one_fixed_coordinate": {
                "raw_nodes": 600,
                "canonical_orbits": sum(layer_one.values()),
                "orbit_size_distribution": {str(k): v for k, v in sorted(layer_one.items())},
            },
            "two_fixed_coordinates": {
                "raw_nodes": 179400,
                "canonical_orbits": sum(layer_two.values()),
                "orbit_size_distribution": {str(k): v for k, v in sorted(layer_two.items())},
            },
        },
        "base_faces": {
            "right_zero_coordinates": list(zero_columns),
            "right_face_size": 64,
            "party_swapped_left_center_support": int(delta.sum()),
            "party_swapped_F_values": {"0": len(base_left_values)},
            "party_swapped_right_minimizer_unique_for_all_64": True,
        },
        "terminal_orbits": {
            "right_six_faces": len(right_terminals),
            "swapped_left_six_faces": len(left_terminals),
            "swapped_left_faces_pairwise_disjoint": True,
            "swapped_left_face_points": len(left_face_points),
            "fixed_left_terminal_points": len(alpha_points),
            "disjoint_left_assignments_with_exact_F_zero": len(alpha_points | left_face_points),
        },
        "C_level_sign_pairs": {
            "right_face_family": len(right_family_pairs),
            "swapped_left_face_family": len(left_family_pairs),
            "families_disjoint": True,
            "union": len(right_family_pairs | left_family_pairs),
        },
        "scope": (
            "Proves affine symmetry, early canonical-layer censuses, and exact equality-terminal counts; "
            "does not prove W(S,T)>=0 for every cut or completeness of the equality set."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
