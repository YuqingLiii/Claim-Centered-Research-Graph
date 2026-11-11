#!/usr/bin/env python3
"""Exact cardinality-coupled lower-bound probe for the d=4 cut objective."""

import json
import math
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
MAT = ROOT / "grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat"


def exact_int_matrix(raw):
    a = np.asarray(raw)
    out = np.empty(a.shape, dtype=np.int64)
    it = np.nditer(a, flags=["multi_index"])
    for z in it:
        x = float(z)
        q = int(x)
        if not math.isfinite(x) or float(q) != x:
            raise ValueError(f"nonintegral A entry at {it.multi_index}")
        out[it.multi_index] = q
    return out


def main():
    with h5py.File(MAT, "r") as f:
        A = exact_int_matrix(f["A"][()])
        ax = np.asarray(f["ax"][()]).reshape(-1).astype(np.int64)
        by = np.asarray(f["by"][()]).reshape(-1).astype(np.int64)

    B = ax[:, None] * A * by[None, :]
    rows = [sum(int(x) for x in B[i]) for i in range(300)]
    cols = [sum(int(B[i, j]) for i in range(300)) for j in range(300)]

    row_prefix = [0]
    for x in sorted(rows):
        row_prefix.append(row_prefix[-1] + x)

    column_prefixes = []
    for j in range(300):
        prefix = [0]
        for x in sorted((int(B[i, j]) for i in range(300)), reverse=True):
            prefix.append(prefix[-1] + x)
        column_prefixes.append(prefix)

    bounds = []
    for h in range(301):
        lower = row_prefix[h]
        lower += sum(
            min(0, cols[j] - 2 * column_prefixes[j][h])
            for j in range(300)
        )
        bounds.append(lower)

    argmin = min(range(301), key=bounds.__getitem__)
    print(json.dumps({
        "formula": "L_h=sum(h smallest row margins)+sum_j min(0,c_j-2*sum(h largest B_ij))",
        "minimum": {"h": argmin, "lower_bound": bounds[argmin]},
        "nonnegative_cardinalities": [h for h, v in enumerate(bounds) if v >= 0],
        "selected_values": {str(h): bounds[h] for h in (0, 1, 2, 10, 40, 100, 165, 300)},
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
