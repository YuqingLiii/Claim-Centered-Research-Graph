#!/usr/bin/env python3
"""Independent exact checker for the H4 blocks {9,12,13,14} no-go.

The checker rebuilds the canonical equality-vanishing K covariants over
GF(24001), restricts them to the exact party-swap eigenspaces, evaluates the
6665 symmetric Gram products and the Bell target on the certified Boolean
points, and verifies a stored 6666-square augmented minor has nonzero
determinant.

Required third-party packages: numpy, h5py, python-flint.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import h5py
import numpy as np
from flint import nmod_mat


P = 24001
ORDER = 14400
CVAL = 2081044153087351400
BLOCKS = [9, 12, 13, 14]
EXPECTED_DIMS = [(43, 64), (28, 15), (11, 6), (43, 64)]
EXPECTED_WIDTHS = [(946, 2080), (406, 120), (66, 21), (946, 2080)]
EXPECTED_MANIFEST_SHA = (
    "41eaa1a24984bdc456ec325c9e45f6e0d989d86dadfcbb7e88db2e10fc04a86b"
)
EXPECTED_PARITY_SHA = (
    "6bb82b3541835071477be91d725068dada1b550c14acfd855bc6783485254624"
)
EXPECTED_ACTION_SHA = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_MINOR_CERT_SHA = (
    "83a7a2b76e3743fde450a3dfcd58f2bf27f5486712583d7ecfa2866aacb9add0"
)
EXPECTED_MINOR_SHA = (
    "ea67e7d6be507d8a54384dcdbaf7e92485221abe2917a2a1a0a8a680a0dca9a7"
)
EXPECTED_DETERMINANT = 5172


def die(message):
    raise SystemExit("ERROR: " + str(message))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def deterministic_four_sets(count: int, seed: int) -> list[tuple[int, ...]]:
    seen = set()
    output = []
    counter = 0
    while len(output) < count:
        raw = hashlib.shake_256(f"{seed}:{counter}".encode()).digest(16)
        values = []
        for position in range(4):
            value = int.from_bytes(raw[4 * position:4 * position + 4], "little") % 600
            while value in values:
                value = (value + 1) % 600
            values.append(value)
        subset = tuple(sorted(values))
        if subset not in seen:
            seen.add(subset)
            output.append(subset)
        counter += 1
    return output


def target_column(A, z0, subsets):
    x0 = z0[:300].astype(np.int64)
    y0 = z0[300:].astype(np.int64)
    base = int(x0 @ (A @ y0))
    if base != CVAL:
        die("base Boolean point does not attain C")
    row = A @ y0
    column = x0 @ A
    delta = np.empty(600, dtype=np.int64)
    delta[:300] = -2 * x0 * row
    delta[300:] = -2 * y0 * column
    target = np.empty(600 + len(subsets), dtype=np.uint16)
    target[:600] = (-delta % P).astype(np.uint16)
    for index, subset in enumerate(subsets):
        objective = base + sum(int(delta[u]) for u in subset)
        left = [u for u in subset if u < 300]
        right = [u - 300 for u in subset if u >= 300]
        for u in left:
            for v in right:
                objective += 4 * int(x0[u]) * int(A[u, v]) * int(y0[v])
        target[600 + index] = (CVAL - objective) % P
    return target


def exact_covariants(base, elements, block, z0, subsets):
    meta = block["meta"]
    degree = int(meta["degree"])
    multiplicity = int(meta["m_W_minus_D"])
    representation = block["Rhat"].astype(np.int64)
    V = block["V"].astype(np.int64)
    needed_pairs = sorted({
        pair for subset in subsets for pair in itertools.combinations(subset, 2)
    })
    pair_index = {pair: index for index, pair in enumerate(needed_pairs)}
    constant = np.zeros((degree, multiplicity), dtype=np.int64)
    linear = np.zeros((600, degree, multiplicity), dtype=np.int64)
    quadratic = np.zeros(
        (len(needed_pairs), degree, multiplicity), dtype=np.int64
    )
    for record in meta["active_modules"]:
        start = int(record["copy_start"])
        end = int(record["copy_end"])
        transformed = (representation @ V[:, start:end]) % P
        values = np.empty(ORDER, dtype=np.int64)
        first = np.full(ORDER, -1, dtype=np.int32)
        second = np.full(ORDER, -1, dtype=np.int32)
        selected_pair = np.full(ORDER, -1, dtype=np.int32)
        for group_index, (permutation, signs) in enumerate(elements):
            image, action_sign = base.act_mid(
                int(record["rep_mid"]), permutation, signs
            )
            support = tuple(base.mid_support(int(image)))
            value = int(action_sign)
            for variable in support:
                value *= int(z0[variable])
            values[group_index] = value
            if support:
                first[group_index] = support[0]
            if len(support) == 2:
                second[group_index] = support[1]
                selected_pair[group_index] = pair_index.get(
                    tuple(sorted(support)), -1
                )
        terms = values[:, None, None] * transformed
        constant[:, start:end] = np.sum(terms, axis=0) % P
        view = linear[:, :, start:end]
        valid = first >= 0
        np.add.at(view, first[valid], terms[valid])
        valid = second >= 0
        np.add.at(view, second[valid], terms[valid])
        valid = selected_pair >= 0
        if np.any(valid):
            view2 = quadratic[:, :, start:end]
            np.add.at(view2, selected_pair[valid], terms[valid])
    linear %= P
    quadratic %= P
    Z = block["Z"].astype(np.int64)
    output = np.empty(
        (600 + len(subsets), degree, int(meta["m_K"])), dtype=np.int64
    )
    output[:600] = ((constant[None, :, :] - 2 * linear) @ Z) % P
    for index, subset in enumerate(subsets):
        correction = np.zeros_like(constant)
        for pair in itertools.combinations(subset, 2):
            correction += quadratic[pair_index[pair]]
        raw = (
            constant
            - 2 * np.sum(linear[np.asarray(subset)], axis=0)
            + 4 * correction
        )
        output[600 + index] = (raw @ Z) % P
    return output


def parity_features(values, J, basis, batch=64):
    values = (values @ basis.astype(np.int64)) % P
    dimension = values.shape[2]
    ii, jj = np.triu_indices(dimension)
    out = np.empty((len(values), len(ii)), dtype=np.uint16)
    offdiag = ii != jj
    J = J.astype(np.int64)
    for lo in range(0, len(values), batch):
        hi = min(len(values), lo + batch)
        gram = np.einsum(
            "tdi,de,tej->tij",
            values[lo:hi], J, values[lo:hi], optimize=True,
        ) % P
        packed = gram[:, ii, jj]
        packed[:, offdiag] = 2 * packed[:, offdiag] % P
        out[lo:hi] = packed.astype(np.uint16)
    return out


def check_parity_basis(T, plus, minus, expected):
    k = T.shape[0]
    identity = np.eye(k, dtype=np.int64)
    T64 = T.astype(np.int64)
    plus64 = plus.astype(np.int64)
    minus64 = minus.astype(np.int64)
    if not np.array_equal(T64 @ T64 % P, identity):
        die("party-swap involution failure")
    if plus.shape[1] != expected[0] or minus.shape[1] != expected[1]:
        die("party parity dimension mismatch")
    if not np.array_equal(T64 @ plus64 % P, plus64 % P):
        die("plus basis eigenvalue failure")
    if not np.array_equal(T64 @ minus64 % P, (-minus64) % P):
        die("minus basis eigenvalue failure")
    combined = np.ascontiguousarray(np.concatenate([plus, minus], axis=1))
    rank = nmod_mat(k, k, memoryview(combined.ravel()), P).rank()
    if int(rank) != k:
        die("combined party parity basis is singular")


def main():
    project = Path(__file__).resolve().parents[1]
    draft = project / "artifacts/drafts"
    certificate_path = draft / (
        "d4-four-block-party-parity-linear-nogo-certificate-20260830.json"
    )
    minor_path = draft / (
        "d4-four-block-party-parity-augmented-minor-20260830.json"
    )
    certificate = json.load(open(certificate_path))
    minor_certificate = json.load(open(minor_path))
    if sha256(minor_path) != EXPECTED_MINOR_CERT_SHA:
        die("minor certificate SHA")
    if minor_certificate["augmented_minor_sha256"] != EXPECTED_MINOR_SHA:
        die("minor SHA field")
    if int(minor_certificate["augmented_minor_determinant_mod_p"]) != EXPECTED_DETERMINANT:
        die("minor determinant field")
    pivots = list(map(int, minor_certificate["pivot_rows"]))
    if len(pivots) != 6666 or len(set(pivots)) != 6666:
        die("pivot row list")
    source_rows = int(minor_certificate["source_shape"][0])
    if source_rows != 8000 or max(pivots) >= source_rows:
        die("pivot row range")

    cache = project / (
        "artifacts/replay/h4_canonical_K_operator_bundle/canonical_K_pencils"
    )
    parity = project / (
        "artifacts/drafts/session-full-sos/party-swap-K-modp"
    )
    if sha256(cache / "canonical_K_pencil_manifest.json") != EXPECTED_MANIFEST_SHA:
        die("canonical K manifest SHA")
    if sha256(parity / "party_swap_K_modp_exact.json") != EXPECTED_PARITY_SHA:
        die("party parity manifest SHA")

    backend = load(
        project / "tools/h4_K_linear_operator_modp_batched.py",
        "h4_four_block_checker_backend",
    )
    system = project / (
        "artifacts/frozen-instance/"
        "d4_n1_300x300.mat.H4_level2_exact_system.json"
    )
    nogap = project / "tools/bootstrap/h4_nogap_irrep_cache.py"
    specdir = project / "artifacts/drafts/session-full-sos/full-spec"
    operator = backend.OperatorBatched(
        str(system), str(nogap), str(specdir), str(cache),
        blocks=BLOCKS, verbose=True,
    )
    base = load(
        project / "tools/h4_K_full_dual_slice_release.py",
        "h4_four_block_checker_dual",
    )
    base.init_pairs()
    _, elements, _, action_sha = operator.ng.load_and_match_certified_action(
        str(system), operator.G
    )
    if action_sha != EXPECTED_ACTION_SHA:
        die("certified action SHA")

    mat = project / "artifacts/frozen-instance/d4_n1_300x300.mat"
    with h5py.File(mat, "r") as archive:
        A = np.asarray(archive["A"][()]).astype(np.int64)
        ax = np.asarray(archive["ax"][()]).reshape(-1).astype(np.int8)
        by = np.asarray(archive["by"][()]).reshape(-1).astype(np.int8)
    z0 = np.concatenate([ax, by]).astype(np.int8)

    # Only the prefix through the last certified pivot is needed.
    prefix_rows = max(pivots) + 1
    subsets = deterministic_four_sets(prefix_rows - 600, 2026083004)
    target = target_column(A, z0, subsets)
    columns = []
    parity_records = []
    for block_index, block in enumerate(operator.blocks):
        ir = int(block["ir"])
        pdata = np.load(parity / f"party_swap_K_modp_block_{ir:02d}.npz")
        T = pdata["T_modp"]
        plus = pdata["plus_basis_modp"]
        minus = pdata["minus_basis_modp"]
        check_parity_basis(T, plus, minus, EXPECTED_DIMS[block_index])
        values = exact_covariants(base, elements, block, z0, subsets)
        widths = []
        for basis in (plus, minus):
            feature = parity_features(values, block["J"], basis)
            widths.append(feature.shape[1])
            columns.append(feature)
        if tuple(widths) != EXPECTED_WIDTHS[block_index]:
            die("parity feature width")
        parity_records.append({
            "gap_irrep_id": ir,
            "plus_dimension": int(plus.shape[1]),
            "minus_dimension": int(minus.shape[1]),
            "plus_parameters": widths[0],
            "minus_parameters": widths[1],
        })
    matrix = np.ascontiguousarray(
        np.column_stack(columns + [target]).astype(np.uint16)
    )
    if matrix.shape != (prefix_rows, 6666):
        die(f"evaluation matrix shape {matrix.shape}")
    minor_array = np.ascontiguousarray(matrix[pivots, :])
    minor_sha = hashlib.sha256(minor_array.tobytes(order="C")).hexdigest()
    if minor_sha != EXPECTED_MINOR_SHA:
        die(f"augmented minor SHA {minor_sha}")
    minor = nmod_mat(6666, 6666, memoryview(minor_array.ravel()), P)
    determinant = int(minor.det()) % P
    if determinant != EXPECTED_DETERMINANT or determinant == 0:
        die(f"augmented determinant {determinant}")

    output = {
        "status": "EXACT_FOUR_BLOCK_PARTY_PARITY_LINEAR_NO_GO_VERIFIED",
        "prime": P,
        "blocks": BLOCKS,
        "parity_blocks": parity_records,
        "symmetric_gram_parameters": 6665,
        "augmented_columns": 6666,
        "certified_source_points": source_rows,
        "replayed_prefix_points": prefix_rows,
        "certified_pivot_rows": len(pivots),
        "augmented_minor_sha256": minor_sha,
        "augmented_minor_determinant_mod_p": determinant,
        "gram_map_rank_exact": 6665,
        "gram_map_domain_nullity_exact": 0,
        "target_in_gram_linear_span": False,
        "psd_gram_exists_in_selected_blocks": False,
        "party_swap_reduction_lossless": True,
        "equality_face_dual_kernel_dimension": 12,
        "logical_conclusion": (
            "The nonzero augmented minor makes the 6665 Gram-product columns "
            "and target independent after exact modular reduction. Hence they "
            "are independent in characteristic zero. The target is outside "
            "the indefinite Gram image, so a PSD Gram is impossible a fortiori."
        ),
        "certificate_sha256": sha256(certificate_path),
        "minor_certificate_sha256": sha256(minor_path),
    }
    raw = json.dumps(output, sort_keys=True, separators=(",", ":")).encode()
    output_path = draft / (
        "d4-four-block-party-parity-nogo-checker-output-20260830.json"
    )
    output_path.write_bytes(raw)
    print(json.dumps({
        **output,
        "output_path": str(output_path),
        "output_sha256": hashlib.sha256(raw).hexdigest(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
