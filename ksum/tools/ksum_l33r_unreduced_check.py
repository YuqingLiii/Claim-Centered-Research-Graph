"""Independent-review runner for the unreduced HLS dual Adv+/- SDP.

This deliberately mirrors tools/ksum_stage0_d_direct_adv.py: one PSD variable
indexed by (input, query position), with no symmetry reduction. The additions
are argparse, provenance output, an optional size guard, and JSON output.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
import time
from pathlib import Path

import cvxpy as cp
import numpy as np
import scipy
import scipy.sparse as sp


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("q", type=int)
    parser.add_argument("target", type=int, nargs="?", default=0)
    parser.add_argument("--solver", default="MOSEK")
    parser.add_argument("--eps", type=float, default=1e-7)
    parser.add_argument("--max-iters", type=int, default=500000)
    parser.add_argument("--max-psd-dim", type=int, default=1400)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    started = time.perf_counter()
    n, q, target = args.n, args.q, args.target % args.q
    inputs = np.asarray(list(itertools.product(range(q), repeat=n)), dtype=np.int16)
    labels = np.zeros(len(inputs), dtype=np.int8)
    for i in range(n):
        for j in range(i + 1, n):
            labels |= ((inputs[:, i] + inputs[:, j]) % q == target)

    input_count = len(inputs)
    dim = input_count * n
    here = Path(__file__).resolve()
    baseline = here.with_name("ksum_stage0_d_direct_adv.py")
    print(
        "PROVENANCE "
        + json.dumps(
            {
                "command": " ".join([sys.executable, *sys.argv]),
                "python": sys.executable,
                "python_version": platform.python_version(),
                "numpy_version": np.__version__,
                "scipy_version": scipy.__version__,
                "cvxpy_version": cp.__version__,
                "installed_solvers": cp.installed_solvers(),
                "review_script_sha256": sha256(here),
                "baseline_sha256": sha256(baseline),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    print(
        f"INSTANCE n={n} q={q} t={target} inputs={input_count} psd_dim={dim} "
        f"yes={int(labels.sum())} no={int((1-labels).sum())}",
        flush=True,
    )
    if dim > args.max_psd_dim and not args.force:
        print(
            f"SIZE_GUARD psd_dim={dim} max_psd_dim={args.max_psd_dim}; "
            "use --force to attempt the unreduced cone",
            flush=True,
        )
        raise SystemExit(2)

    yes = np.flatnonzero(labels)
    no = np.flatnonzero(1 - labels)
    eq_rows: list[int] = []
    eq_cols: list[int] = []
    row = 0
    for a in yes:
        diff = inputs[no] != inputs[a]
        for no_offset, b in enumerate(no):
            for i in np.flatnonzero(diff[no_offset]):
                eq_rows.append(row)
                eq_cols.append((a * n + int(i)) * dim + (b * n + int(i)))
            row += 1
    aeq = sp.csr_matrix(
        (np.ones(len(eq_rows)), (eq_rows, eq_cols)),
        shape=(row, dim * dim),
    )
    diag_rows = np.repeat(np.arange(input_count), n)
    diagonal_indices = np.arange(dim)
    diag_cols = diagonal_indices * dim + diagonal_indices
    adiag = sp.csr_matrix(
        (np.ones(dim), (diag_rows, diag_cols)),
        shape=(input_count, dim * dim),
    )
    print(
        f"AFFINE equality={row} diagonal={input_count} eq_nnz={aeq.nnz}",
        flush=True,
    )

    matrix = cp.Variable((dim, dim), PSD=True, name="unreduced_hls_matrix")
    bound = cp.Variable(nonneg=True, name="adv_pm")
    vector = cp.reshape(matrix, (dim * dim, 1), order="C")
    problem = cp.Problem(cp.Minimize(bound), [aeq @ vector == 1, adiag @ vector <= bound])
    solve_options: dict[str, object] = {"verbose": args.verbose}
    if args.solver.upper() == "SCS":
        solve_options.update(eps=args.eps, max_iters=args.max_iters)
    solve_started = time.perf_counter()
    problem.solve(solver=args.solver.upper(), **solve_options)
    solve_seconds = time.perf_counter() - solve_started
    value = None if bound.value is None else float(bound.value)
    result = {
        "n": n,
        "q": q,
        "target": target,
        "inputs": input_count,
        "psd_dim": dim,
        "yes": int(labels.sum()),
        "no": int((1 - labels).sum()),
        "equalities": row,
        "solver": args.solver.upper(),
        "eps_argument": args.eps,
        "status": problem.status,
        "value": value,
        "solve_seconds": solve_seconds,
        "wall_seconds": time.perf_counter() - started,
    }
    print("RESULT_JSON " + json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
