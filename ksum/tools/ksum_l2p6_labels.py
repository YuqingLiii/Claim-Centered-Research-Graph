"""Attach exact stabilizer-irrep labels to archived L33 Wedderburn blocks.

The reviewed L33 solver returns one multiplicity block for each real irrep of
H=S_(N-1) x C(sigma), but records only multiplicity and irrep dimension.  This
read-only companion rebuilds the deterministic bases, evaluates factor-group
characters on them, and labels the small q=3,4,5 sectors used in L2 phase 6.
It never resolves an SDP and never modifies an archived certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
from pathlib import Path

import numpy as np

import ksum_l33_reduced_adv as l33


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def partitions(n: int, cap: int | None = None):
    if n == 0:
        yield ()
        return
    cap = n if cap is None else min(cap, n)
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def specht_dimension(shape: tuple[int, ...]) -> int:
    hooks = 1
    for i, row in enumerate(shape):
        for j in range(row):
            hooks *= row - j + sum(other > j for other in shape[i + 1 :])
    return math.factorial(sum(shape)) // hooks


def content_sum(shape: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(shape) for j in range(row))


def action_mapping(inputs: np.ndarray, q: int, alphabet=None, pos_swap=None):
    moved = inputs.copy()
    if pos_swap is not None:
        a, b = pos_swap
        moved[:, [a, b]] = moved[:, [b, a]]
    if alphabet is not None:
        moved = np.asarray(alphabet, dtype=np.int16)[moved]
    return l33.lex_indices(moved, q)


def isotypic_character_ratio(family, mapping: np.ndarray) -> float:
    """Return chi_U(g)/dim(U) from U tensor multiplicity-space projectors."""
    inverse = np.argsort(mapping)
    multiplicity = family[0].shape[1]
    trace = sum(float(np.trace(qb.T @ qb[inverse])) for qb in family)
    return trace / (multiplicity * len(family))


def involution_parts(q: int, target: int):
    sigma = [(target - a) % q for a in range(q)]
    fixed = [a for a in range(q) if sigma[a] == a]
    cycles = []
    seen = set(fixed)
    for a in range(q):
        if a not in seen:
            b = sigma[a]
            cycles.append(tuple(sorted((a, b))))
            seen.update((a, b))
    return sigma, sorted(fixed), sorted(cycles)


def endpoint_flip(q: int, cycle):
    p = list(range(q))
    a, b = cycle
    p[a], p[b] = b, a
    return p


def pair_swap(q: int, first, second):
    p = list(range(q))
    a, b = first
    c, d = second
    p[a], p[b], p[c], p[d] = c, d, a, b
    return p


def fixed_swap(q: int, fixed):
    p = list(range(q))
    a, b = fixed[:2]
    p[a], p[b] = b, a
    return p


def sign_symbol(value: float, tol=2e-6):
    if abs(value - 1.0) < tol:
        return "+"
    if abs(value + 1.0) < tol:
        return "-"
    if abs(value) < tol:
        return "0"
    return f"{value:+.6f}"


def alphabet_label(inputs, q, target, family, position_dim):
    _, fixed, cycles = involution_parts(q, target)
    tau, r = len(fixed), len(cycles)
    ratios = {}
    if r:
        p = endpoint_flip(q, cycles[0])
        ratios["single_pair_flip"] = isotypic_character_ratio(
            family, action_mapping(inputs, q, alphabet=p)
        )
    if r >= 2:
        p = pair_swap(q, cycles[0], cycles[1])
        ratios["pair_swap"] = isotypic_character_ratio(
            family, action_mapping(inputs, q, alphabet=p)
        )
    if tau >= 2:
        p = fixed_swap(q, fixed)
        ratios["fixed_swap"] = isotypic_character_ratio(
            family, action_mapping(inputs, q, alphabet=p)
        )

    irrep_dim = len(family) // position_dim
    if tau == 1 and r == 1:
        label = "C2:" + ("triv" if ratios["single_pair_flip"] > 0 else "sign")
    elif tau == 2 and r == 1:
        label = (
            "C2_pair:" + sign_symbol(ratios["single_pair_flip"])
            + " x S2_fixed:" + sign_symbol(ratios["fixed_swap"])
        )
    elif tau in (0, 1) and r == 2:
        if irrep_dim == 2:
            label = "B2:bipartition((1),(1))"
        else:
            flip = sign_symbol(ratios["single_pair_flip"])
            perm = sign_symbol(ratios["pair_swap"])
            table = {
                ("+", "+"): "B2:bipartition((2),empty)",
                ("+", "-"): "B2:bipartition((1,1),empty)",
                ("-", "+"): "B2:bipartition(empty,(2))",
                ("-", "-"): "B2:bipartition(empty,(1,1))",
            }
            label = table.get((flip, perm), f"B2:unresolved({flip},{perm})")
        if tau == 1:
            label += " x S1:triv"
    else:
        label = f"C(sigma):unimplemented(tau={tau},r={r},dim={irrep_dim})"
    return label, irrep_dim, ratios


def label_case(root: Path, n: int, q: int, target: int):
    stem = f"n{n}_q{q}_t{target}"
    json_path = root / f"{stem}.json"
    npz_path = root / f"{stem}.npz"
    if not json_path.exists():
        json_path = root / f"heldout_{stem}.json"
        npz_path = root / f"heldout_{stem}.npz"
    archived = json.loads(json_path.read_text(encoding="utf-8"))
    cert = np.load(npz_path, allow_pickle=False)

    inputs = np.asarray(list(itertools.product(range(q), repeat=n)), dtype=np.int16)
    centralizer = l33.centralizer_of_sigma(q, target)
    blocks, _ = l33.group_algebra_blocks(inputs, q, centralizer)
    generator_maps, _ = l33.stabilizer_generator_mappings(inputs, q, centralizer)
    families, info = l33.align_isotypic_copies(blocks, generator_maps)
    if info["isotypic_block_dims"] != archived["block_dims"]:
        raise RuntimeError(f"deterministic block order drift at {stem}")

    tail = n - 1
    pos_map = action_mapping(inputs, q, pos_swap=(1, 2))
    shapes = list(partitions(tail))
    candidates = [
        (shape, specht_dimension(shape), content_sum(shape) / math.comb(tail, 2))
        for shape in shapes
    ]
    profile_by_block = {row["block"]: row for row in archived["block_profiles_by_trace"]}
    rows = []
    for block_id, family in enumerate(families):
        pos_ratio = isotypic_character_ratio(family, pos_map)
        compatible = [candidate for candidate in candidates if len(family) % candidate[1] == 0]
        shape, pos_dim, expected_ratio = min(
            compatible, key=lambda x: abs(x[2] - pos_ratio)
        )
        if abs(pos_ratio - expected_ratio) > 2e-6:
            raise RuntimeError(f"unresolved S_{tail} label for block {block_id}: {pos_ratio}")
        if len(family) % pos_dim:
            raise RuntimeError(f"irrep dimension mismatch for block {block_id}")
        c_label, c_dim, c_ratios = alphabet_label(inputs, q, target, family, pos_dim)
        profile = profile_by_block[block_id]
        value = np.asarray(cert[f"block_{block_id:03d}"])
        eigvals, eigvecs = np.linalg.eigh(0.5 * (value + value.T))
        top = eigvecs[:, -1]
        # Sign-free internal-direction diagnostic: participation and overlap with
        # the constant coordinate in the deterministic multiplicity basis.
        participation = 1.0 / float(np.sum(top**4))
        row = {
            "block": block_id,
            "label": {"S_tail": list(shape), "C_sigma": c_label},
            "multiplicity_dim": int(value.shape[0]),
            "irrep_dimension": len(family),
            "position_irrep_dimension": pos_dim,
            "alphabet_irrep_dimension": c_dim,
            "position_transposition_character_ratio": pos_ratio,
            "alphabet_character_ratios": c_ratios,
            "trace_share": profile["natural_trace_share"],
            "frobenius_share": profile["natural_frob_share"],
            "effective_rank": profile["effective_rank"],
            "top_eigenvalue_trace_fraction": profile["top_trace_fractions"][0],
            "top_direction_participation": participation,
            "top_direction_abs_first_coordinate": abs(float(top[0])),
        }
        rows.append(row)
    rows.sort(key=lambda row: -row["trace_share"])
    return {
        "case": [n, q, target],
        "tau": archived["tau"],
        "note": "Sector labels are irreps of the L33 stabilizer S_(N-1) x C(sigma), not vector labels for the full S_N action.",
        "archived_json_sha256": sha256_file(json_path),
        "archived_npz_sha256": sha256_file(npz_path),
        "sectors_by_trace": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="ksum/artifacts/logs_ksum_expL_20260719")
    parser.add_argument("--cases", nargs="*", default=["5,4,0", "5,4,1", "6,3,0", "7,3,0"])
    parser.add_argument("--json")
    args = parser.parse_args()
    root = Path(args.root)
    cases = [tuple(map(int, item.split(","))) for item in args.cases]
    result = {
        "script_sha256": sha256_file(Path(__file__)),
        "reviewed_l33_sha256": sha256_file(Path(l33.__file__)),
        "cases": [label_case(root, *case) for case in cases],
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.json:
        out = Path(args.json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
