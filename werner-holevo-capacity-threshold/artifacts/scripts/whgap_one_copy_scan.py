#!/usr/bin/env python3
"""Reproducible one-copy coherent-information scan for the qutrit WH family.

This is numerical evidence only.  It combines rank-stratified random starts, structured
isotropic near-pure starts, and local L-BFGS-B polishing.  Pure inputs are included as an exact
zero baseline because the channel and complement outputs have the same nonzero spectrum there.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize


def levi_civita(i: int, j: int, k: int) -> int:
    if len({i, j, k}) < 3:
        return 0
    return 1 if (i, j, k) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)} else -1


def kraus(x: float) -> list[np.ndarray]:
    result = [np.sqrt(1.0 - x) * np.eye(3, dtype=complex)]
    for i in range(3):
        a = np.array(
            [[levi_civita(i, j, k) for k in range(3)] for j in range(3)],
            dtype=complex,
        )
        result.append(np.sqrt(x / 2.0) * a)
    return result


def channel(rho: np.ndarray, x: float) -> np.ndarray:
    return (1.0 - x) * rho + (x / 2.0) * (np.trace(rho) * np.eye(3) - rho.T)


def complement(rho: np.ndarray, ks: list[np.ndarray]) -> np.ndarray:
    return np.array(
        [[np.trace(ka @ rho @ kb.conj().T) for kb in ks] for ka in ks], dtype=complex
    )


def entropy_bits(state: np.ndarray) -> float:
    state = (state + state.conj().T) / 2.0
    vals = np.linalg.eigvalsh(state)
    vals[np.abs(vals) < 2e-15] = 0.0
    if vals.min(initial=0.0) < -2e-10:
        raise ValueError(f"non-PSD output, min eigenvalue {vals.min()}")
    vals = np.clip(vals, 0.0, None)
    vals /= vals.sum()
    nz = vals[vals > 0.0]
    return float(-np.dot(nz, np.log2(nz)))


def coherent_information(rho: np.ndarray, x: float, ks: list[np.ndarray]) -> float:
    return entropy_bits(channel(rho, x)) - entropy_bits(complement(rho, ks))


def vector_to_state(z: np.ndarray, rank: int) -> np.ndarray:
    n = 3 * rank
    t = z[:n].reshape(3, rank) + 1j * z[n:].reshape(3, rank)
    rho = t @ t.conj().T
    tr = float(np.trace(rho).real)
    if tr < 1e-30:
        return np.eye(3) / 3.0
    return rho / tr


def state_to_vector(rho: np.ndarray, rank: int) -> np.ndarray:
    vals, vecs = np.linalg.eigh((rho + rho.conj().T) / 2.0)
    order = np.argsort(vals)[::-1][:rank]
    t = vecs[:, order] * np.sqrt(np.clip(vals[order], 0.0, None))[None, :]
    return np.concatenate([t.real.ravel(), t.imag.ravel()])


def random_state(rng: np.random.Generator, rank: int) -> np.ndarray:
    t = rng.normal(size=(3, rank)) + 1j * rng.normal(size=(3, rank))
    rho = t @ t.conj().T
    return rho / np.trace(rho)


def isotropic_family() -> list[np.ndarray]:
    psi = np.array([1.0, 1.0j, 0.0], dtype=complex) / np.sqrt(2.0)
    psibar = psi.conj()
    p = np.outer(psi, psi.conj())
    q = np.outer(psibar, psibar.conj())
    states = []
    for eps in np.concatenate([np.logspace(-12, -2, 21), np.linspace(0.02, 0.5, 13)]):
        states.append((1.0 - eps) * p + eps * q)
    return states


@dataclass
class Candidate:
    ic: float
    rank_parameter: int
    source: str
    rho: np.ndarray


def scan_one_x(x: float, seed: int, random_per_rank: int, polish: int) -> dict:
    rng = np.random.default_rng(seed)
    ks = kraus(x)

    # Independent implementation check of the declared channel formula.
    check_rho = random_state(rng, 3)
    kraus_out = sum(k @ check_rho @ k.conj().T for k in ks)
    formula_error = float(np.linalg.norm(kraus_out - channel(check_rho, x)))

    candidates: list[Candidate] = [
        Candidate(0.0, 1, "exact-pure-baseline", np.diag([1.0, 0.0, 0.0])),
        Candidate(
            coherent_information(np.eye(3) / 3.0, x, ks),
            3,
            "maximally-mixed",
            np.eye(3) / 3.0,
        ),
    ]
    for rho in isotropic_family():
        candidates.append(Candidate(coherent_information(rho, x, ks), 2, "isotropic-grid", rho))

    for rank in (2, 3):
        for _ in range(random_per_rank):
            rho = random_state(rng, rank)
            candidates.append(Candidate(coherent_information(rho, x, ks), rank, "random", rho))

        seeds = sorted(
            (c for c in candidates if c.rank_parameter == rank),
            key=lambda c: c.ic,
            reverse=True,
        )[:polish]
        for index, candidate in enumerate(seeds):
            z0 = state_to_vector(candidate.rho, rank)

            def objective(z: np.ndarray) -> float:
                return -coherent_information(vector_to_state(z, rank), x, ks)

            result = minimize(
                objective,
                z0,
                method="L-BFGS-B",
                options={"maxiter": 1200, "ftol": 1e-14, "gtol": 1e-9, "maxls": 50},
            )
            rho = vector_to_state(result.x, rank)
            candidates.append(
                Candidate(
                    coherent_information(rho, x, ks),
                    rank,
                    f"polished-{rank}-{index}-success-{bool(result.success)}",
                    rho,
                )
            )

    winner = max(candidates, key=lambda c: c.ic)
    eigs = np.linalg.eigvalsh((winner.rho + winner.rho.conj().T) / 2.0)
    positive = [c.ic for c in candidates if c.ic > 1e-9]
    return {
        "x": x,
        "seed": seed,
        "formula_error_fro": formula_error,
        "candidate_count": len(candidates),
        "best_ic_bits": winner.ic,
        "best_source": winner.source,
        "best_rank_parameter": winner.rank_parameter,
        "best_state_eigenvalues": eigs.tolist(),
        "count_above_1e-9_bits": len(positive),
        "maximally_mixed_ic_bits": coherent_information(np.eye(3) / 3.0, x, ks),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--x",
        nargs="+",
        type=float,
        default=[0.39, 0.4, 0.41, 0.45, 0.49],
    )
    parser.add_argument("--seed", type=int, default=20260829)
    parser.add_argument("--random-per-rank", type=int, default=400)
    parser.add_argument("--polish", type=int, default=10)
    args = parser.parse_args()

    report = {
        "scope": "numerical one-copy lower-bound search; not a global upper-bound certificate",
        "xs": [
            scan_one_x(x, args.seed + index, args.random_per_rank, args.polish)
            for index, x in enumerate(args.x)
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
