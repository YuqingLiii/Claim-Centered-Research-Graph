#!/usr/bin/env python3
"""Create a self-contained replay view using the final SAT attempt per sector."""
from pathlib import Path
import argparse
import json
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.direct.resolve()
    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    shutil.copy2(source / "candidate.json", output / "candidate.json")
    shutil.copy2(source / "build_summary.json", output / "build_summary.json")
    shutil.copytree(source / "direct360", output / "direct360")
    (output / "solver").mkdir()
    for sector in ("Xerr", "Zerr"):
        final = source / "retry_unsat_profile" / f"{sector}.solver.log"
        assignment = source / "retry_unsat_profile" / f"{sector}.assignment.dimacs"
        check = source / "retry_unsat_profile" / f"{sector}.assignment_check.json"
        assert final.is_file() and assignment.is_file() and check.is_file()
        solver_text = final.read_text(errors="replace")
        assert "s SATISFIABLE" in solver_text
        assert json.loads(check.read_text())["status"] == "PASS"
        shutil.copy2(final, output / "solver" / f"{sector}.solver.log")
        shutil.copy2(assignment, output / "solver" / f"{sector}.assignment.dimacs")
        shutil.copy2(check, output / "solver" / f"{sector}.assignment_check.json")
    record = {
        "schema": "circdist-gross-round102-adjudicated-direct-view-v1",
        "status": "PASS",
        "source": str(source),
        "sectors": {
            sector: {
                "solver_log": f"solver/{sector}.solver.log",
                "assignment": f"solver/{sector}.assignment.dimacs",
                "assignment_check": f"solver/{sector}.assignment_check.json",
                "attempt": "retry_unsat_profile",
                "solver_status": "SATISFIABLE",
            } for sector in ("Xerr", "Zerr")
        },
    }
    (output / "ASSEMBLY.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "sectors": ["Xerr", "Zerr"]}, sort_keys=True))


if __name__ == "__main__":
    main()
