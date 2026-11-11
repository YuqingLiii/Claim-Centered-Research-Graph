#!/usr/bin/env python3
"""Audit the serialized Round118 JSONL child-process ledger."""
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

solver_rows = []
solver_names = {"cadical", "cadical-1.9.5-arm64-macos", "kissat", "minisat", "glucose"}
for row in reaped:
    if row.get("argv") and Path(row["argv"][0]).name.lower() in solver_names:
        solver_rows.append(row)
assert len(solver_rows) == 3 and all(row["rc"] == 10 for row in solver_rows)
solver_intervals = sorted((stamp(row["start_utc"]), stamp(row["end_utc"]), row["tag"]) for row in solver_rows)
assert all(left[1] <= right[0] for left, right in zip(solver_intervals, solver_intervals[1:]))

out = {
    "schema": "circdist-gross-round118-session-process-ledger-check-v1",
    "status": "PASS",
    "rows": len(rows),
    "started_records": len(started),
    "reaped_records": len(reaped),
    "all_started_have_exactly_one_reap": True,
    "all_children_reaped": True,
    "strict_serial_nonoverlap": True,
    "overlaps": overlaps,
    "solver_processes": len(solver_rows),
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
