#!/usr/bin/env python3
"""Attribute Phase-22 residual changes to low-weight multisymmetric invariants."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

import ksum_l2p22_critical_dense_residual as p22


def project(pi, b, columns):
    X = np.column_stack(columns).astype(float)
    scales = np.max(np.abs(X), axis=0)
    scales[scales == 0] = 1.0
    X /= scales
    sw = np.sqrt(pi)
    coef, _, rank, sing = np.linalg.lstsq(X * sw[:, None], b * sw, rcond=1e-11)
    g = b - X @ coef
    l2sq = float(np.sum(pi * g * g))
    l1 = float(np.sum(pi * np.abs(g)))
    corr = 0.0 if l1 == 0 else 2 * l2sq / l1
    return corr, int(rank), float(sing[rank - 1]) if rank else None


def analyze(N):
    L = int(N ** (2 / 3))
    while (L + 1) ** 3 <= N * N:
        L += 1
    while L**3 > N * N:
        L -= 1
    D = L // 2
    dense, _ = p22.dense_component(N, L)
    bal, _, U, M, a, _ = p22.balanced_component(N, L)
    support = sorted(set(dense) | set(bal))
    pi = np.array([0.5 * dense.get(h, 0.0) + 0.5 * bal.get(h, 0.0) for h in support])
    pi /= pi.sum()
    b = np.array([1.0 if all(r == 0 for (r, u), cnt in h) else 0.0 for h in support])

    vals = {name: [] for name in ["one", "C", "S2", "S3", "M1", "S4", "M2", "X2"]}
    for h in support:
        slots = [(r, u) for (r, u), cnt in h for _ in range(cnt)]
        s = np.array([r + u for r, u in slots], dtype=float)
        x = np.array([r * u for r, u in slots], dtype=float)
        vals["one"].append(1.0)
        vals["C"].append(float(np.sum(x)))
        vals["S2"].append(float(np.sum(s**2)))
        vals["S3"].append(float(np.sum(s**3)))
        vals["M1"].append(float(np.sum(s * x)))
        vals["S4"].append(float(np.sum(s**4)))
        vals["M2"].append(float(np.sum((s**2) * x)))
        vals["X2"].append(float(np.sum(x**2)))
    vals = {k: np.array(v) for k, v in vals.items()}

    basis = ["one", "C", "S2", "S3", "M1"]
    if D >= 5:
        basis += ["S4", "M2", "X2", "S2^2", "S2*C", "C^2"]
        vals["S2^2"] = vals["S2"] ** 2
        vals["S2*C"] = vals["S2"] * vals["C"]
        vals["C^2"] = vals["C"] ** 2

    scalar_names = ["one", "C"] + (["C^2"] if D >= 5 else [])
    families = {}
    for names in [
        scalar_names,
        ["one", "C", "S2"],
        ["one", "C", "S3"],
        ["one", "C", "M1"],
        ["one", "C", "S2", "S3"],
        ["one", "C", "S2", "M1"],
        ["one", "C", "S3", "M1"],
        ["one", "C", "S2", "S3", "M1"],
        basis,
    ]:
        key = "+".join(names)
        corr, rank, smin = project(pi, b, [vals[n] for n in names])
        families[key] = {"corr": corr, "rank": rank, "smin": smin}

    if D >= 5:
        low = ["one", "C", "S2", "S3", "M1"]
        for extra in ["S4", "M2", "X2", "S2^2", "S2*C", "C^2"]:
            names = low + [extra]
            corr, rank, smin = project(pi, b, [vals[n] for n in names])
            families["low3+" + extra] = {"corr": corr, "rank": rank, "smin": smin}
        for extra in ["S2", "S3", "M1", "S4", "M2", "X2", "S2^2", "S2*C"]:
            names = scalar_names + [extra]
            corr, rank, smin = project(pi, b, [vals[n] for n in names])
            families["scalar+" + extra] = {"corr": corr, "rank": rank, "smin": smin}

    raw_feats = []
    raw_keys = set()
    patterns = None
    for h in support:
        fd, patterns = p22.feature_dict(h, D)
        raw_feats.append(fd)
        raw_keys.update(fd)
    raw_keys = sorted(raw_keys)
    Xraw = [np.array([fd.get(k, 0.0) for fd in raw_feats]) for k in raw_keys]
    raw_corr, raw_rank, raw_smin = project(pi, b, Xraw)
    basis_corr, basis_rank, basis_smin = project(pi, b, [vals[n] for n in basis])

    return {
        "N": N,
        "L": L,
        "D": D,
        "U": U,
        "M": M,
        "a": a,
        "support": len(support),
        "raw_columns": len(raw_keys),
        "raw_rank": raw_rank,
        "raw_corr": raw_corr,
        "raw_smin": raw_smin,
        "invariant_basis": basis,
        "invariant_rank": basis_rank,
        "invariant_corr": basis_corr,
        "invariant_smin": basis_smin,
        "families": families,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Ns", nargs="+", type=int, default=[27, 33])
    args = parser.parse_args()
    payload = {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "results": [analyze(N) for N in args.Ns],
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
