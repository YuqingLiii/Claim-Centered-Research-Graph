#!/usr/bin/env python3
"""Deterministic continuation-seeded width-two orbit circuit exchange.

Within a fixed-D block, the first N uses the closed Phase-20 interleaved
label-aware seed.  A final circuit at N is transported to N+1 by greedy
injective nearest-neighbor matching in normalized occupancy coordinates,
preserving the YES/NO label and prioritizing larger cofactor weights.  Exact
rank repair uses transported columns first and the same closed interleaved
order only as filler.

At each N, at most two coordinated exchanges are performed.  The entering
block is either the first or first two worst global dual-residual orbits.  The
deletion pool is the four smallest-cofactor support columns, with label match
to the entering residual first.  All singleton deletions and all pairs from
that fixed pool are tested.  The exact merit is the Phase-20 closed objective

    correlation^2 / global_max_abs_dual_residual,

subject to tail mass >=1/4.  No current-N LP optimum/support is queried.

All algebra is exact SymPy rational arithmetic.  This is finite proposer
reconnaissance, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import itertools
import json
import math
import sys
import time
from pathlib import Path

from sympy import Matrix, Rational

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ksum_l2p14_target_scale_sweep import (  # noqa: E402
    independent_rows,
    moment_row,
    orbits,
    qstr,
    row_patterns,
)
from ksum_l2p20_label_aware_exchange import (  # noqa: E402
    initial_support,
    interleaved_order,
    orbit_record,
    orbit_stats,
)


def digest_json(obj) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def evaluate_support(B, hs, labels, support, threshold):
    support = tuple(sorted(support))
    if len(support) != B.rows + 1:
        return None
    A = B[:, support]
    if A.rank() != B.rows:
        return None
    null = A.nullspace()
    if len(null) != 1 or any(x == 0 for x in null[0]):
        return None
    raw = list(null[0])
    weights = [x / sum(abs(y) for y in raw) for x in raw]
    corr = sum(labels[j] * weights[k] for k, j in enumerate(support))
    if corr < 0:
        weights = [-x for x in weights]
        corr = -corr
    tail = sum(abs(weights[k]) for k, j in enumerate(support)
               if orbit_stats(hs[j])[1] >= threshold)
    if corr == 0:
        return None
    signs = [1 if x > 0 else -1 for x in weights]
    rhs = Matrix([labels[j] - corr * signs[k] for k, j in enumerate(support)])
    dual = A.T.gauss_jordan_solve(rhs)[0]
    residuals = [
        Rational(labels[j]) - sum(B[i, j] * dual[i] for i in range(B.rows))
        for j in range(B.cols)
    ]
    residual_order = sorted(range(B.cols), key=lambda j: (-abs(residuals[j]), j))
    maxres = abs(residuals[residual_order[0]])
    score = corr * corr / maxres if tail >= Rational(1, 4) else Rational(0)
    return {
        "support": support,
        "weights": weights,
        "correlation": corr,
        "tail_mass": tail,
        "dual": dual,
        "residuals": residuals,
        "residual_order": residual_order,
        "max_residual": maxres,
        "score": score,
        "dual_pass": bool(maxres <= corr),
    }


def merit(state):
    return (
        state["score"], state["correlation"], state["tail_mass"],
        tuple(-j for j in state["support"]),
    )


def normalized_distance(old_H, old_N, new_H, new_N):
    old_flat = [z for pair in old_H for z in pair]
    new_flat = [z for pair in new_H for z in pair]
    l1 = sum(abs(Rational(x, old_N) - Rational(y, new_N))
             for x, y in zip(old_flat, new_flat))
    old_ct = orbit_stats(old_H)[1]
    new_ct = orbit_stats(new_H)[1]
    ct_gap = abs(Rational(old_ct, old_N * old_N)
                 - Rational(new_ct, new_N * new_N))
    return l1, ct_gap


def transport_support(old_hs, old_state, old_N, new_hs, new_N):
    new_labels = [1 if orbit_stats(H)[1] > 0 else -1 for H in new_hs]
    old_items = sorted(
        zip(old_state["support"], old_state["weights"]),
        key=lambda item: (-abs(item[1]), item[0]),
    )
    used = set()
    mapped = []
    details = []
    for old_j, old_w in old_items:
        old_H = old_hs[old_j]
        old_label = 1 if orbit_stats(old_H)[1] > 0 else -1
        candidates = [j for j, lab in enumerate(new_labels)
                      if lab == old_label and j not in used]
        new_j = min(
            candidates,
            key=lambda j: normalized_distance(old_H, old_N, new_hs[j], new_N)
            + (j,),
        )
        used.add(new_j)
        mapped.append(new_j)
        details.append({
            "old_orbit": orbit_record(old_H),
            "old_abs_weight": qstr(abs(old_w)),
            "new_orbit_index": new_j,
            "new_orbit": orbit_record(new_hs[new_j]),
            "normalized_distance": qstr(normalized_distance(old_H, old_N, new_hs[new_j], new_N)[0]),
        })
    return mapped, details


def repair_to_full_circuit(B, hs, transported):
    order = list(dict.fromkeys(transported + interleaved_order(hs)))
    _rref, pivots = B[:, order].rref()
    basis = [order[k] for k in pivots]
    if len(basis) != B.rows:
        raise RuntimeError("transport plus filler order did not span feature space")
    Cinv = B[:, basis].inv()
    bset = set(basis)
    extra_order = list(dict.fromkeys(transported + interleaved_order(hs)))
    for j in extra_order:
        if j in bset:
            continue
        coeff = Cinv * B[:, j]
        if all(x != 0 for x in coeff):
            support = tuple(sorted(basis + [j]))
            overlap = len(set(support) & set(transported))
            return support, overlap
    raise RuntimeError("rank repair found no full circuit")


def block_exchange(B, hs, labels, state, threshold, iterations=2, deletion_pool=4):
    history = []
    stop = None
    for step in range(iterations + 1):
        history.append({
            "step": step,
            "correlation": qstr(state["correlation"]),
            "tail_mass": qstr(state["tail_mass"]),
            "max_residual": qstr(state["max_residual"]),
            "score": qstr(state["score"]),
            "dual_pass": state["dual_pass"],
        })
        if state["dual_pass"]:
            stop = "global dual bound passed"
            break
        if step == iterations:
            stop = "fixed two-step cap reached"
            break
        outside = [j for j in state["residual_order"] if j not in state["support"]]
        entering_blocks = [(outside[0],)]
        if len(outside) >= 2:
            entering_blocks.append(tuple(sorted(outside[:2])))
        weight_map = dict(zip(state["support"], state["weights"]))
        candidates = []
        for entering in entering_blocks:
            entering_labels = sorted(labels[j] for j in entering)
            leave_order = sorted(
                state["support"],
                key=lambda j: (
                    labels[j] not in entering_labels,
                    abs(weight_map[j]),
                    j,
                ),
            )[:deletion_pool]
            for leaving in itertools.combinations(leave_order, len(entering)):
                trial_support = tuple(sorted(
                    (set(state["support"]) - set(leaving)) | set(entering)
                ))
                trial = evaluate_support(B, hs, labels, trial_support, threshold)
                if trial is not None and trial["tail_mass"] >= Rational(1, 4):
                    candidates.append(trial)
        if not candidates:
            stop = "no bounded block candidate is a tail-feasible full circuit"
            break
        best = max(candidates, key=merit)
        if merit(best) <= merit(state):
            stop = "bounded block local optimum"
            break
        state = best
    return state, history, stop


def build_case(N, D):
    hs = orbits(N)
    rps = row_patterns(D)
    rows = [[moment_row(H, rp) for H in hs] for rp in rps]
    B, basis_rows = independent_rows(Matrix(rows))
    labels = [1 if orbit_stats(H)[1] > 0 else -1 for H in hs]
    return hs, rows, B, basis_rows, labels


def run_block(D, N0, N1, resume=None):
    results = []
    if resume is None:
        previous = None
        previous_hs = None
    else:
        previous, previous_hs = resume
    for N in range(N0, N1 + 1):
        started = time.perf_counter()
        hs, rows, B, basis_rows, labels = build_case(N, D)
        threshold = math.ceil(D * D / 4)
        if previous is None:
            seed_support = initial_support(B, interleaved_order(hs))
            transport = None
            transported_overlap = None
            seed_kind = "closed Phase-20 interleaved start seed"
        else:
            mapped, transport = transport_support(previous_hs, previous, N - 1, hs, N)
            seed_support, transported_overlap = repair_to_full_circuit(B, hs, mapped)
            seed_kind = "continued nearest-label normalized-occupancy seed with exact rank repair"
        seed = evaluate_support(B, hs, labels, seed_support, threshold)
        if seed is None:
            raise RuntimeError("seed is not a full circuit")
        final, history, stop = block_exchange(B, hs, labels, seed, threshold)
        results.append({
            "N": N,
            "D_polynomial_cutoff": D,
            "orbit_count": len(hs),
            "feature_rank": B.rows,
            "seed_kind": seed_kind,
            "transport_details": transport,
            "transported_support_overlap_after_rank_repair": transported_overlap,
            "seed": {
                "correlation": qstr(seed["correlation"]),
                "tail_mass": qstr(seed["tail_mass"]),
                "dual_violation_ratio_decimal": float(seed["max_residual"] / seed["correlation"]),
                "support": [orbit_record(hs[j], seed["weights"][k])
                            for k, j in enumerate(seed["support"])],
            },
            "final": {
                "correlation": qstr(final["correlation"]),
                "above_two_thirds": bool(final["correlation"] > Rational(2, 3)),
                "tail_mass": qstr(final["tail_mass"]),
                "tail_mass_at_least_quarter": bool(final["tail_mass"] >= Rational(1, 4)),
                "max_residual": qstr(final["max_residual"]),
                "dual_violation_ratio_decimal": float(final["max_residual"] / final["correlation"]),
                "global_dual_bound_passes": final["dual_pass"],
                "score": qstr(final["score"]),
                "support_size": len(final["support"]),
                "support_feature_rank": B[:, final["support"]].rank(),
                "support": [orbit_record(hs[j], final["weights"][k])
                            for k, j in enumerate(final["support"])],
            },
            "exchange_history": history,
            "stop_reason": stop,
            "basis_row_indices": basis_rows,
            "orbit_sha256": digest_json(hs),
            "raw_matrix_sha256": digest_json(rows),
            "elapsed_seconds": round(time.perf_counter() - started, 6),
        })
        previous = {
            "support": tuple(final["support"]),
            "weights": list(final["weights"]),
        }
        previous_hs = hs
        print(
            f"completed D={D},N={N}, corr={qstr(final['correlation'])}, "
            f"ratio={float(final['max_residual']/final['correlation']):.6g}, stop={stop}",
            flush=True,
        )
        del rows, B
        gc.collect()
    return results


def parse_block(spec):
    try:
        d, n0, n1 = map(int, spec.split(":"))
        return d, n0, n1
    except Exception as exc:
        raise argparse.ArgumentTypeError("block must be D:N0:N1") from exc


def load_resume(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    block = data["blocks"][-1]
    record = block["results"][-1]
    D = record["D_polynomial_cutoff"]
    N = record["N"]
    hs = orbits(N)
    lookup = {tuple(tuple(x) for x in H): j for j, H in enumerate(hs)}
    support = []
    weights = []
    for item in record["final"]["support"]:
        key = tuple(tuple(x) for x in item["orbit"])
        support.append(lookup[key])
        weights.append(Rational(item["weight"]))
    return D, N, {"support": tuple(support), "weights": weights}, hs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--block", action="append", type=parse_block, default=[])
    ap.add_argument("--resume-from")
    args = ap.parse_args()
    blocks = args.block or [(5, 11, 16), (6, 17, 23), (7, 24, 31)]
    started = time.perf_counter()
    out_blocks = []
    resume_payload = None
    if args.resume_from:
        old_D, old_N, old_state, old_hs = load_resume(args.resume_from)
        if len(blocks) != 1 or blocks[0][0] != old_D or blocks[0][1] != old_N + 1:
            raise ValueError("resume requires one block with same D and N_start=previous N+1")
        resume_payload = (old_state, old_hs)
    for block_index, (D, N0, N1) in enumerate(blocks):
        print(f"starting block D={D},N={N0}..{N1}", flush=True)
        out_blocks.append({
            "D": D, "N_start": N0, "N_end": N1,
            "results": run_block(
                D, N0, N1,
                resume=resume_payload if block_index == 0 else None,
            ),
        })
    out = {
        "scope": "q=5,K=2 deterministic continuation-seeded width-two block exchange",
        "tier": "exact finite proposer test; no asymptotic inference",
        "exchange_width": 2,
        "deletion_pool": 4,
        "exchange_steps_per_N": 2,
        "blocks": out_blocks,
        "total_elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "blocks": len(out_blocks),
        "cases": sum(len(x["results"]) for x in out_blocks),
        "seconds": out["total_elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
