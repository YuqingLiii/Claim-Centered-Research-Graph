"""Independent structural audit of the L33 cyclic 2-Sum reduction.

Recomputes group/orbit counts without L33's orbit helpers, checks tau and
centralizer bookkeeping plus predicate preservation, and checks that L33's
numerical Wedderburn families have the full symmetric-commutant dimension and
reconstruct PSD H-invariant natural matrices.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import platform
import sys
from collections import Counter
from pathlib import Path

import numpy as np


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def centralizer(q: int, target: int) -> list[tuple[int, ...]]:
    sigma = tuple((target - a) % q for a in range(q))
    return [
        perm
        for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    ]


def label(x: tuple[int, ...], q: int, target: int) -> bool:
    return any(
        (x[i] + x[j]) % q == target
        for i in range(len(x))
        for j in range(i + 1, len(x))
    )


def full_pair_signature(
    x: tuple[int, ...], y: tuple[int, ...], perms: list[tuple[int, ...]]
) -> tuple[int, ...]:
    q = len(perms[0])
    candidates = []
    for perm in perms:
        counts = Counter((perm[a], perm[b]) for a, b in zip(x, y))
        candidates.append(tuple(counts.get((a, b), 0) for a in range(q) for b in range(q)))
    return min(candidates)


def full_input_signature(
    x: tuple[int, ...], perms: list[tuple[int, ...]]
) -> tuple[int, ...]:
    q = len(perms[0])
    candidates = []
    for perm in perms:
        counts = Counter(perm[a] for a in x)
        candidates.append(tuple(counts.get(a, 0) for a in range(q)))
    return min(candidates)


def stabilizer_unordered_signature(
    x: tuple[int, ...], y: tuple[int, ...], perms: list[tuple[int, ...]]
) -> tuple[int, ...]:
    q = len(perms[0])
    candidates = []
    for transpose in (False, True):
        left, right = (y, x) if transpose else (x, y)
        for perm in perms:
            tail = Counter((perm[a], perm[b]) for a, b in zip(left[1:], right[1:]))
            candidates.append(
                (perm[left[0]], perm[right[0]])
                + tuple(tail.get((a, b), 0) for a in range(q) for b in range(q))
            )
    return min(candidates)


def load_l33(path: Path):
    spec = importlib.util.spec_from_file_location("ksum_l33_review_target", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load L33 target")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit_group(q: int, target: int) -> dict[str, int]:
    target %= q
    perms = centralizer(q, target)
    sigma = tuple((target - a) % q for a in range(q))
    tau = sum(sigma[a] == a for a in range(q))
    expected = math.factorial(tau) * 2 ** ((q - tau) // 2) * math.factorial((q - tau) // 2)
    if len(perms) != expected:
        raise AssertionError((len(perms), expected))
    for perm in perms:
        for a in range(q):
            for b in range(q):
                if (((a + b) % q == target) != ((perm[a] + perm[b]) % q == target)):
                    raise AssertionError("centralizer failed to preserve the pair relation")
    return {"q": q, "target": target, "tau": tau, "centralizer_order": len(perms)}


def audit_instance(n: int, q: int, target: int, module) -> dict[str, object]:
    target %= q
    inputs_t = list(itertools.product(range(q), repeat=n))
    inputs = np.asarray(inputs_t, dtype=np.int16)
    perms = centralizer(q, target)
    group = audit_group(q, target)
    yes = [x for x in inputs_t if label(x, q, target)]
    no = [x for x in inputs_t if not label(x, q, target)]
    equality_signatures = {full_pair_signature(x, y, perms) for x in yes for y in no}
    diagonal_signatures = {full_input_signature(x, perms) for x in inputs_t}

    np_perms = [np.asarray(perm, dtype=np.int16) for perm in perms]
    spectral, spectral_info = module.group_algebra_blocks(inputs, q, np_perms)
    maps, _ = module.stabilizer_generator_mappings(inputs, q, np_perms)
    families, family_info = module.align_isotypic_copies(spectral, maps)
    model_dimension = sum(
        dim * (dim + 1) // 2 for dim in family_info["isotypic_block_dims"]
    )
    commutant_signatures = {
        stabilizer_unordered_signature(x, y, perms)
        for i, x in enumerate(inputs_t)
        for y in inputs_t[i:]
    }
    if model_dimension != len(commutant_signatures):
        raise AssertionError(
            f"symmetric commutant dimension mismatch: {model_dimension} != {len(commutant_signatures)}"
        )

    basis = np.column_stack([block for family in families for block in family])
    orthogonality_residual = float(
        np.max(np.abs(basis.T @ basis - np.eye(len(inputs_t))))
    )
    rng = np.random.default_rng(20260718 + 100 * n + q + target)
    natural = np.zeros((len(inputs_t), len(inputs_t)))
    for family in families:
        raw = rng.normal(size=(family[0].shape[1], family[0].shape[1]))
        psd = raw @ raw.T
        for aligned in family:
            natural += aligned @ psd @ aligned.T
    min_eigenvalue = float(np.linalg.eigvalsh((natural + natural.T) / 2)[0])
    invariance_residual = 0.0
    for mapping in maps:
        invariance_residual = max(
            invariance_residual,
            float(np.max(np.abs(natural[np.ix_(mapping, mapping)] - natural))),
        )

    label_mask = np.asarray([label(x, q, target) for x in inputs_t])
    reduced_eq = len(
        module.pair_orbit_representatives(
            inputs,
            np.flatnonzero(label_mask),
            np.flatnonzero(~label_mask),
            q,
            np_perms,
        )
    )
    reduced_diag = len(module.input_orbit_representatives(inputs, q, np_perms))
    if reduced_eq != len(equality_signatures) or reduced_diag != len(diagonal_signatures):
        raise AssertionError("L33 orbit-code counts disagree with independent signatures")
    return {
        "n": n,
        **group,
        "sn_input_orbits": math.comb(n + q - 1, n),
        "equality_orbits": len(equality_signatures),
        "diagonal_orbits": len(diagonal_signatures),
        "symmetric_commutant_dimension": len(commutant_signatures),
        "model_dimension": model_dimension,
        "isotypic_block_dims": family_info["isotypic_block_dims"],
        "irrep_dimensions": family_info["irrep_dimensions_repetitions"],
        "basis_orthogonality_residual": orthogonality_residual,
        "random_psd_min_eigenvalue": min_eigenvalue,
        "random_psd_invariance_residual": invariance_residual,
        "max_schur_polar_residual": family_info["max_schur_polar_residual"],
        "max_within_cluster_spread": spectral_info["max_within_cluster_spread"],
        "min_between_cluster_gap": spectral_info["min_between_cluster_gap"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--instances",
        default="3,3,0;4,3,0;5,4,0;5,4,1;6,3,0;6,3,1",
        help="semicolon-separated n,q,t triples",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    target_path = root / "tools" / "ksum_l33_reduced_adv.py"
    module = load_l33(target_path)
    print(
        "PROVENANCE "
        + json.dumps(
            {
                "command": " ".join([sys.executable, *sys.argv]),
                "python": sys.executable,
                "python_version": platform.python_version(),
                "numpy_version": np.__version__,
                "review_script_sha256": sha256(Path(__file__).resolve()),
                "target_sha256": sha256(target_path),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    for q, target in ((3, 0), (3, 1), (4, 0), (4, 1), (5, 0)):
        print("GROUP_JSON " + json.dumps(audit_group(q, target), sort_keys=True), flush=True)
    count = 0
    for raw in args.instances.split(";"):
        n, q, target = map(int, raw.split(","))
        result = audit_instance(n, q, target, module)
        count += 1
        print("INSTANCE_JSON " + json.dumps(result, sort_keys=True), flush=True)
    print(f"AUDIT_RESULT PASS instances={count}", flush=True)


if __name__ == "__main__":
    main()
