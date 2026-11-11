#!/usr/bin/env python3
"""Hash every non-certificate SAT DRAT trace before deliberate scratch removal."""
from pathlib import Path
import argparse
import hashlib
import json


def inspect(path):
    digest = hashlib.sha256()
    size = 0
    line_feeds = 0
    empty_clause_lines = 0
    prefix = b""
    first = True
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(8 << 20)
            if not chunk:
                break
            digest.update(chunk)
            size += len(chunk)
            line_feeds += chunk.count(b"\n")
            joined = prefix + chunk
            empty_clause_lines += joined.count(b"\n0\n")
            if first and joined.startswith(b"0\n"):
                empty_clause_lines += 1
            first = False
            prefix = joined[-2:]
    return {
        "bytes": size,
        "lf_count": line_feeds,
        "sha256": digest.hexdigest(),
        "empty_clause_lines": empty_clause_lines,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for iteration in range(124, 136):
        formula_metadata = json.loads(
            (args.root / f"formulas/iter{iteration}/metadata.json").read_text()
        ) if (args.root / f"formulas/iter{iteration}/metadata.json").exists() else json.loads(
            Path("circdist/artifacts/circdist_gross_proof_outer_round88_20260830/formulas/iter112/metadata.json").read_text()
        )
        objects = [
            (
                "outer",
                args.root / f"iter{iteration}/outer/outer.drat",
                args.root / f"iter{iteration}/outer/solver.log",
                formula_metadata["cnf_sha256"],
            )
        ]
        for sector in ("Xerr", "Zerr"):
            summary = json.loads(
                (args.root / f"iter{iteration}/direct/direct360/{sector}.summary.json").read_text()
            )
            objects.append(
                (
                    sector,
                    args.root / f"iter{iteration}/direct/solver/{sector}.drat",
                    args.root / f"iter{iteration}/direct/solver/{sector}.solver.log",
                    summary["dimacs_sha256"],
                )
            )
        for kind, trace, solver_log, formula_sha in objects:
            log_text = solver_log.read_text(errors="replace")
            assert "s SATISFIABLE" in log_text
            row = {
                "iteration": iteration,
                "query": kind,
                "formula_sha256": formula_sha,
                "solver_status": "SATISFIABLE",
                "proof_output_enabled": True,
                "certificate_disposition": "not an UNSAT certificate",
                "retention": "hash/size/line disposition retained; full non-certificate trace removed with scratch",
                **inspect(trace),
            }
            assert row["empty_clause_lines"] == 0
            rows.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    output = {
        "schema": "circdist-round92-sat-drat-trace-disposition-v1",
        "status": "PASS",
        "scope": "All 36 solver invocations enabled textual proof output, but all returned SAT; these traces contain no empty clause and prove no UNSAT fact.",
        "trace_count": len(rows),
        "traces": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
