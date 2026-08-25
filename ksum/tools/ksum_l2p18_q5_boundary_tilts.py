#!/usr/bin/env python3
"""Phase-18 q=5 formula-defined base-law repair diagnostics.

All variants remain inside the phase-16 selective weighted-projection normal
form.  No LP solution and no optimal-dual absolute value is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ksum_l2p17_q5_explicit_pi as p17


def normalise_logweights(logw: np.ndarray) -> np.ndarray:
    logw = logw - np.max(logw)
    w = np.exp(logw)
    return w / np.sum(w)


def dm_weights(hs, alpha: float) -> np.ndarray:
    return normalise_logweights(
        np.array([p17.orbit_log_weight(H, alpha) for H in hs]))


def feature_matrix(hs, D: int):
    rp = p17.row_patterns(D)
    A = np.array([[float(p17.moment_row(H, p)) for H in hs] for p in rp])
    return A, rp


def weighted_basis(A: np.ndarray, w: np.ndarray):
    norms = np.sqrt(np.sum(A * A * w[None, :], axis=1))
    keep = norms > 0
    An = A[keep] / norms[keep, None]
    X = An.T * np.sqrt(w)[:, None]
    U, s, _ = np.linalg.svd(X, full_matrices=False)
    tol = max(X.shape) * np.finfo(float).eps * s[0]
    rank = int(np.sum(s > tol))
    return An, U[:, :rank], s, rank


def project(A, w, b, ct, threshold):
    An, U, s, rank = weighted_basis(A, w)
    y = b * np.sqrt(w)
    pw = U @ (U.T @ y)
    p = pw / np.sqrt(w)
    g = b - p
    l2sq = float(np.dot(w, g * g))
    l1 = float(np.dot(w, np.abs(g)))
    tail = float(np.dot(w[ct >= threshold], np.abs(g[ct >= threshold])) / l1)
    corr = 2 * l2sq / l1
    return {
        "rank": rank,
        "smallest_retained_singular_value": float(s[rank - 1]),
        "largest_discarded_singular_value": (
            None if rank == len(s) else float(s[rank])),
        "no_probability": float(np.dot(w, b)),
        "correlation": corr,
        "passes_strict_two_thirds": bool(corr > 2 / 3 + 1e-10),
        "residual_l2_squared": l2sq,
        "residual_l1": l1,
        "tail_threshold": threshold,
        "tail_absolute_mass_fraction": tail,
        "weighted_orthogonality_residual": float(np.max(np.abs(An @ (w * g)))),
        "min_positive_weight": float(np.min(w[w > 0])),
    }


def leverage_kernel(A, w):
    """Return K_D^w(H,H), using l_H=w_H K(H,H)."""
    _, U, _, rank = weighted_basis(A, w)
    lev = np.sum(U * U, axis=1)
    K = lev / w
    return K, rank


def run_N(N: int):
    D = max(3, math.ceil(math.sqrt(N)))
    hs = p17.orbits(N)
    A, rp = feature_matrix(hs, D)
    b = np.array([float(sum(r * u for r, u in H) == 0) for H in hs])
    ct = np.array([sum(r * u for r, u in H) for H in hs])
    threshold = (N ** 1.5) / 4
    variants = []

    alpha_specs = [
        ("alpha_N_inv", 1 / N),
        ("alpha_N_inv_sqrt", 1 / math.sqrt(N)),
        ("alpha_1", 1.0),
        ("alpha_sqrt_N", math.sqrt(N)),
        ("alpha_N", float(N)),
    ]
    for name, alpha in alpha_specs:
        w = dm_weights(hs, alpha)
        rec = project(A, w, b, ct, threshold)
        rec.update({"variant": name, "formula": "DM(alpha(N))", "alpha": alpha})
        variants.append(rec)

    w0 = dm_weights(hs, 1.0)
    delta = float(np.dot(w0, b))
    for name, power in (("boundary_sqrt_balance", 0.5),
                        ("boundary_exact_balance", 1.0)):
        multiplier = ((1 - delta) / delta) ** power
        w = w0 * np.where(b > 0, multiplier, 1.0)
        w /= np.sum(w)
        rec = project(A, w, b, ct, threshold)
        rec.update({
            "variant": name,
            "formula": "pi_1(H)*lambda_N^(b(H)); lambda_N=((1-delta_N)/delta_N)^power",
            "power": power,
            "lambda": multiplier,
        })
        variants.append(rec)

    # A softer geometric boundary tilt which remains label-free once C_t is
    # known: it weights distance to the C_t=0 boundary by a fixed power.
    for beta in (0.5, 1.0):
        w = w0 * np.power(1.0 + ct, -beta)
        w /= np.sum(w)
        rec = project(A, w, b, ct, threshold)
        rec.update({
            "variant": f"Ct_boundary_beta_{beta:g}",
            "formula": "pi_1(H)*(1+C_t(H))^(-beta)",
            "beta": beta,
        })
        variants.append(rec)

    # One-shot Christoffel tilts are computed from the formula-defined alpha=1
    # Gram law, then held fixed while the new weighted projection is formed.
    K, R = leverage_kernel(A, w0)
    for name, mult in (
        ("leverage_up", 1.0 + K / R),
        ("leverage_down", 1.0 / (1.0 + K / R)),
    ):
        w = w0 * mult
        w /= np.sum(w)
        rec = project(A, w, b, ct, threshold)
        rec.update({
            "variant": name,
            "formula": "pi_1(H)*(1+K_D^{pi_1}(H,H)/R)^(+1 or -1)",
            "base_rank": R,
            "kernel_min": float(np.min(K)),
            "kernel_max": float(np.max(K)),
        })
        variants.append(rec)

    # A diagnostic grid over the same DM-times-C_t-boundary family.  The grid
    # optimum is reported only as a falsification check; it is not promoted to
    # a formula-defined witness chosen independently of the data.
    grid = []
    alpha_grid = sorted({1 / N, 1 / math.sqrt(N), 0.1, 0.25, 0.5, 1.0, 2.0})
    beta_grid = (0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5)
    for alpha in alpha_grid:
        wa = dm_weights(hs, alpha)
        for beta in beta_grid:
            w = wa * np.power(1.0 + ct, -beta)
            w /= np.sum(w)
            rec = project(A, w, b, ct, threshold)
            grid.append({
                "alpha": alpha,
                "beta": beta,
                "correlation": rec["correlation"],
                "tail_absolute_mass_fraction": rec["tail_absolute_mass_fraction"],
                "passes_correlation": rec["passes_strict_two_thirds"],
                "passes_tail_quarter": bool(
                    rec["tail_absolute_mass_fraction"] >= 0.25 - 1e-10),
            })

    feasible = [x for x in grid if x["passes_correlation"]
                and x["passes_tail_quarter"]]
    tail_feasible = [x for x in grid if x["passes_tail_quarter"]]
    best_joint = max(grid, key=lambda x: min(1.5 * x["correlation"],
                                             4 * x["tail_absolute_mass_fraction"]))
    best_corr_with_tail = (None if not tail_feasible else
                           max(tail_feasible, key=lambda x: x["correlation"]))

    return {
        "N": N,
        "D": D,
        "orbit_count": len(hs),
        "raw_feature_rows": len(rp),
        "variants": variants,
        "dm_Ct_grid": {
            "alpha_values": alpha_grid,
            "beta_values": beta_grid,
            "number_passing_both_corr_and_tail_quarter": len(feasible),
            "best_correlation_subject_to_tail_quarter": best_corr_with_tail,
            "best_balanced_score_point": best_joint,
            "all_points": grid,
        },
    }


def digest(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--max-n", type=int, default=64)
    args = ap.parse_args()
    ns = [n for n in (8, 12, 16, 20, 24, 32, 40, 50, 64) if n <= args.max_n]
    cases = [run_N(N) for N in ns]
    out = {
        "scope": "q=5, K=2, D=ceil(sqrt(N)), phase-16 weighted projection",
        "arithmetic": "float64 SVD diagnostic",
        "cases": cases,
        "input_sha256": digest([(x["N"], x["D"]) for x in cases]),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
