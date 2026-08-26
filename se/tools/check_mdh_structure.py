"""Reproduce the finite MDH structure checks linked by SE.mdh.structure.

The exact checks use the standard library. --spectral additionally uses
NumPy for finite comparisons; neither mode establishes an all-n theorem.
Existing evidence files are read-only. --output always creates a new file.
"""

from __future__ import annotations

import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import platform
import re
import subprocess
import sys

from mdh_family import FamilyData, difference_operator
from mdh_phi_tower import build_certificate

PROJECT = Path(__file__).resolve().parents[1]
ARTIFACTS = PROJECT / "artifacts"


def check_exact(n: int) -> dict:
    fd = FamilyData(n, verbose=False)
    cells = fd.canonical_cells()
    gram = fd.gram_cells(cells)
    orthogonality_errors = sum(
        gram[i][j] != 0 and cells[i][:3] != cells[j][:3]
        for i in range(len(cells)) for j in range(i + 1, len(cells))
    )
    recurrence, columns = fd.recurrence("phi", cells=cells)
    recurrence_errors = []
    for cell, coefficients in recurrence.items():
        if coefficients is None:
            if any(fd.cell_fn(cell)):
                recurrence_errors.append([str(cell), "not in span"])
        elif any(co != 0 and abs(other[5] - cell[5]) > 1
                 for other, co in zip(columns, coefficients)):
            recurrence_errors.append([str(cell), "out-of-band support"])
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        difference_operator(fd)
    difference_ok = "bispectrality: ALL OK" in output.getvalue()
    reference = json.loads((ARTIFACTS / "mdh_dimensions.json").read_text())
    expected = {
        (tuple(e["lam"]), tuple(e["mu"]), tuple(e["nu"])): (e["m_Y"], e["m_N"])
        for e in reference["block_dictionary_D1"][f"n={n}"]
        if e["m_Y"] * e["m_N"] != 0
    }
    dimensions_ok = fd.dims == expected
    tower = build_certificate(n)
    result = {
        "n": n, "cells": len(fd.cells), "canonical_cells": len(cells),
        "orbits": fd.norb, "dimensions_match": dimensions_ok,
        "orthogonality_errors": orthogonality_errors,
        "recurrence_errors": recurrence_errors,
        "difference_operator_ok": difference_ok,
        "tower_labels": tower["labels"],
    }
    if n == 4:
        generated = {
            "cells": [[list(c[0]), list(c[1]), list(c[2]), c[3], c[4], c[5]] for c in cells],
            "orb_sizes": fd.osize, "xval": [str(x) for x in fd.xval],
            "phival": [str(x) for x in fd.phival],
            "gram_diag": [str(gram[i][i]) for i in range(len(cells))],
            "table": {
                f"{lam}|{mu}|{nu}": [[[str(v) for v in row] for row in block] for block in blocks]
                for (lam, mu, nu), blocks in fd.table.items()
            },
        }
        archived = json.loads((ARTIFACTS / "mdh_family_n4.json").read_text())
        result["archived_family_equal"] = generated == archived
        result["archived_tower_equal"] = tower == json.loads(
            (ARTIFACTS / "mdh_phi_tower_n4.json").read_text()
        )
    result["passed"] = bool(
        dimensions_ok and not orthogonality_errors and not recurrence_errors and difference_ok
        and result.get("archived_family_equal", True)
        and result.get("archived_tower_equal", True)
    )
    return result


def check_spectral() -> list[dict]:
    cases = [
        ("random-n3", ["mdh_sigma.py", "random", "--n", "3"], "mismatches: 0"),
        ("reference-n3", ["mdh_sigma.py", "n3opt"], "LAW-1:"),
        ("parity-n4", ["mdh_n4_d1.py"], "parity form [[a,0],[b,0],[0,c]] for ALL 51 orbit images: OK"),
    ]
    results = []
    for name, arguments, marker in cases:
        command = [sys.executable, "-B", str(PROJECT / "tools" / arguments[0]), *arguments[1:]]
        run = subprocess.run(command, capture_output=True, text=True, timeout=180, check=False)
        passed = run.returncode == 0 and marker in run.stdout
        if name == "reference-n3":
            match = re.search(r"best assignment error ([0-9.eE+-]+)", run.stdout)
            passed = passed and match is not None and float(match.group(1)) <= 1e-10
        if name == "parity-n4":
            passed = passed and "S_row^2 = I: True" in run.stdout
        results.append({
            "name": name, "command": command, "exit_code": run.returncode,
            "passed": bool(passed), "stdout": run.stdout, "stderr": run.stderr,
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, nargs="+", choices=(2, 3, 4), default=[2, 3, 4])
    parser.add_argument("--spectral", action="store_true", help="Also run the NumPy spectral comparisons.")
    parser.add_argument("--output", type=Path, help="Optional new JSON output; never overwrites a file.")
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error(f"refusing to overwrite {args.output}")
    exact = []
    for n in args.n:
        print(f"Checking the exact finite structure at n={n}", file=sys.stderr, flush=True)
        exact.append(check_exact(n))
    spectral = check_spectral() if args.spectral else []
    source_files = sorted((PROJECT / "tools").glob("mdh_*.py")) + [Path(__file__).resolve()]
    inputs = [ARTIFACTS / name for name in (
        "mdh_dimensions.json", "mdh_family_n4.json", "mdh_phi_tower_n4.json",
        "mdh_n4_521_block.json", "mdh_opt_t_n4.npy", "blocks_n3.json",
    )]
    payload = {
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "scope": "Exact structure checks at requested_n; spectral tests only on the named instances. Not an all-n proof.",
        "requested_n": args.n,
        "exact": exact, "spectral": spectral,
        "source_sha256": {str(p.relative_to(PROJECT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files},
        "input_sha256": {str(p.relative_to(PROJECT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        "passed": all(r["passed"] for r in exact + spectral),
    }
    if args.spectral:
        import numpy
        payload["numpy"] = numpy.__version__
    text = json.dumps(payload, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(text)
    print(text, end="")
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
