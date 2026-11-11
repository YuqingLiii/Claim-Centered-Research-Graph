#!/usr/bin/env python3
"""Validate the retained Round94 process ledger and serialization claims."""
from pathlib import Path
import argparse
import json


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
L = json.loads((R / "PROCESS_LEDGER.json").read_text())
assert L["status"] == "PASS" and L["schema"] == "circdist-gross-round94-process-ledger-v1"
assert L["science_solver_children"] == 36 and L["outer_solver_children"] == 12 and L["direct_solver_children"] == 24
assert L["strict_serial_solver_intervals_checked"] and L["proof_fixture_synchronous_children"] == 6
assert L["all_children_reaped"] and L["background_processes"] == L["detached_processes"] == 0
assert L["survivors"] == L["timeouts"] == 0
records = L["records"]
assert L["bounded_foreground_records"] == len(records)
paths = {row["path"] for row in records}
actual = {p.relative_to(R).as_posix() for p in (R / "logs/process").glob("*.json")}
assert paths == actual
names = set()
solver = []
failures = []
for row in records:
    assert row["name"] not in names
    names.add(row["name"])
    assert row["final_status"] == "exited_and_reaped" and row["reaped"] and not row["detached"]
    assert row["timed_out"] is False and row["returncode"] in (0, 1, 10)
    if row["returncode"] == 1:
        failures.append(row["name"])
    if row["returncode"] == 10 and "cadical_proof" in row["name"]:
        solver.append((row["started_unix"], row["ended_unix"], row["name"]))
assert set(failures) <= {
    "prepare_reconstruction", "direct_iter136_Xerr_assignment_check",
    "round94_make_package_metadata_preliminary",
}
assert {"prepare_reconstruction", "direct_iter136_Xerr_assignment_check"} <= set(failures)
assert sorted(row["name"] for row in L["corrected_failure_records"]) == sorted(failures)
solver.sort()
assert len(solver) == 36
assert all(left[1] <= right[0] for left, right in zip(solver, solver[1:]))
for iteration in range(136, 148):
    assert f"outer_iter{iteration}_cadical_proof" in names
    assert f"direct_iter{iteration}_Xerr_cadical_proof" in names
    assert f"direct_iter{iteration}_Zerr_cadical_proof" in names
fixture = L["proof_fixture_runs"]
assert len(fixture) == 6 and all(row["reaped"] for row in fixture)
assert [(row["name"], row["returncode"]) for row in fixture] == [
    ("valid_drat_generate_lrat", 0), ("valid_generated_lrat", 0),
    ("corrupt_drat", 1), ("truncated_drat", 1),
    ("corrupt_lrat", 1), ("truncated_lrat", 1),
]
bootstrap = (R / L["bootstrap_process_log"]).read_text()
assert "failed logged-runner creation" in bootstrap and "reaped rc=1" in bootstrap
print("ROUND94_PROCESS_LEDGER_PASS", len(records), len(solver), len(failures))
