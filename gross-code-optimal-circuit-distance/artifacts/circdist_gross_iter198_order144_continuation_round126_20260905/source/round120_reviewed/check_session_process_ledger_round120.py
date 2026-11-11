#!/usr/bin/env python3
"""Audit the serialized Round120 JSONL child-process ledger."""
import argparse
import datetime
import json
from collections import Counter
from pathlib import Path


def stamp(value):
    return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


ap = argparse.ArgumentParser()
ap.add_argument("--ledger", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
rows = [json.loads(line) for line in a.ledger.read_text().splitlines() if line.strip()]
started = [row for row in rows if row.get("state") == "STARTED"]
reaped = [row for row in rows if row.get("state") == "REAPED"]
assert len(started) == len(reaped)
start_by_pid = {}
for row in started:
    pid = row["child_pid"]
    assert pid not in start_by_pid
    start_by_pid[pid] = row
reap_by_pid = {}
for row in reaped:
    pid = row["child_pid"]
    assert pid not in reap_by_pid and pid in start_by_pid
    reap_by_pid[pid] = row
    begin = start_by_pid[pid]
    assert begin["tag"] == row["tag"] and begin["argv"] == row["argv"]
    assert begin["start_utc"] == row["start_utc"]
    assert stamp(row["end_utc"]) >= stamp(row["start_utc"])
assert set(start_by_pid) == set(reap_by_pid)

intervals = sorted((stamp(row["start_utc"]), stamp(row["end_utc"]), row["child_pid"], row["tag"]) for row in reaped)
overlaps = []
for left, right in zip(intervals, intervals[1:]):
    if left[1] > right[0]:
        overlaps.append({"left": left, "right": right})
assert not overlaps

solver_executable_rows = []
solver_names = {"cadical", "cadical-1.9.5-arm64-macos", "kissat", "minisat", "glucose"}
for row in reaped:
    if row.get("argv") and Path(row["argv"][0]).name.lower() in solver_names:
        solver_executable_rows.append(row)
solver_identity_rows = [row for row in solver_executable_rows if row["tag"] == "identify-pinned-cadical"]
solver_rows = [row for row in solver_executable_rows if row not in solver_identity_rows]
solver_sat_rows = [row for row in solver_rows if row["rc"] == 10]
solver_start_failures = [row for row in solver_rows if row["rc"] != 10]
assert len(solver_executable_rows) == 5 and len(solver_identity_rows) == 1
assert solver_identity_rows[0]["rc"] == 0
assert len(solver_rows) == 4 and len(solver_sat_rows) == 3
assert len(solver_start_failures) == 1
assert solver_start_failures[0]["tag"] == "solve-iter195-Xerr-complete-direct360-proof-first"
assert solver_start_failures[0]["rc"] == 1
solver_intervals = sorted((stamp(row["start_utc"]), stamp(row["end_utc"]), row["tag"]) for row in solver_rows)
assert all(left[1] <= right[0] for left, right in zip(solver_intervals, solver_intervals[1:]))
assert not [row for row in reaped if row.get("detached")]
assert not [row for row in reaped if row.get("timeout_triggered")]

out = {
    "schema": "circdist-gross-round120-session-process-ledger-check-v1",
    "status": "PASS",
    "rows": len(rows),
    "started_records": len(started),
    "reaped_records": len(reaped),
    "all_started_have_exactly_one_reap": True,
    "all_children_reaped": True,
    "strict_serial_nonoverlap": True,
    "overlaps": overlaps,
    "solver_executable_invocations_total": len(solver_executable_rows),
    "solver_identity_probes": len(solver_identity_rows),
    "solver_identity_probe_tags": [row["tag"] for row in solver_identity_rows],
    "solver_processes_total": len(solver_rows),
    "solver_sat_processes": len(solver_sat_rows),
    "solver_start_failures": len(solver_start_failures),
    "solver_returncodes": [row["rc"] for row in solver_rows],
    "solver_tags": [row["tag"] for row in solver_rows],
    "solver_strict_serial_nonoverlap": True,
    "returncode_counts": dict(sorted(Counter(str(row["rc"]) for row in reaped).items())),
    "nonzero_non_sat_tags": [row["tag"] for row in reaped if row["rc"] not in (0, 10)],
    "detached_children": 0,
    "background_children": 0,
    "wrapper_start_new_session": False,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
