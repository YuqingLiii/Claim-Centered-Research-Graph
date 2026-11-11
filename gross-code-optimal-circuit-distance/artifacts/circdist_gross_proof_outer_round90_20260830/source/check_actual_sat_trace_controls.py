#!/usr/bin/env python3
"""Verify the sealed actual-Gross SAT-trace negative-control records."""
from pathlib import Path
import argparse
import hashlib
import json


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
args = parser.parse_args()
control = args.root.resolve() / "controls/actual_gross_sat_trace"
summary = json.loads((control / "summary.json").read_text())
assert summary["status"] == "PASS"
assert summary["formula_sha256"] == "a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594"
assert summary["source_trace_sha256"] == "31e91eb241b2f14041c6642fd7b138045a8c629daa9193b4c347ec17009723ce"
assert summary["source_trace_empty_clause_lines"] == 0
for name in ("full", "truncated", "corrupt"):
    run = json.loads((control / f"{name}.run.json").read_text())
    row = summary["drat_checker_runs"][name]
    assert run["returncode"] == row["returncode"] == 1
    assert run["timed_out"] is row["timed_out"] is False
    assert row["accepted"] is False
    assert sha256(control / f"{name}.log") == row["log_sha256"]
    text = (control / f"{name}.log").read_text(errors="replace")
    assert "NOT VERIFIED" in text
assert summary["full_sat_trace_rejected"] is True
assert summary["truncated_sat_trace_rejected"] is True
assert summary["corrupt_sat_trace_rejected"] is True
assert "not applicable" in summary["lrat_control"]
print("ACTUAL_GROSS_SAT_TRACE_CONTROLS_PASS")
