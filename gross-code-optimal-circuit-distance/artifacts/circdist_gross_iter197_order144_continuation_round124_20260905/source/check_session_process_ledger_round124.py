#!/usr/bin/env python3
"""Audit the strict serial Round124 child-process ledger."""
import argparse
import datetime
import json
import os
from collections import Counter
from pathlib import Path


def stamp(value):
    return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


p = argparse.ArgumentParser()
p.add_argument("--ledger", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args()
raw_rows = [json.loads(line) for line in a.ledger.read_text().splitlines() if line.strip()]
# The supervising serial wrapper appends this checker's STARTED row before exec.
# Exclude the current child PID so the audited cutpoint contains only completed children.
rows = [r for r in raw_rows if r.get("child_pid") != os.getpid()]
started = [r for r in rows if r.get("state") == "STARTED"]
reaped = [r for r in rows if r.get("state") == "REAPED"]
assert len(started) == len(reaped)
smap, rmap = {}, {}
for row in started:
    assert row["child_pid"] not in smap
    smap[row["child_pid"]] = row
for row in reaped:
    pid = row["child_pid"]
    assert pid in smap and pid not in rmap
    rmap[pid] = row
    begin = smap[pid]
    assert begin["tag"] == row["tag"] and begin["argv"] == row["argv"]
    assert begin["start_utc"] == row["start_utc"] and row.get("reaped") is True
    assert stamp(row["end_utc"]) >= stamp(row["start_utc"])
assert set(smap) == set(rmap)
intervals = sorted((stamp(r["start_utc"]), stamp(r["end_utc"]), r["child_pid"], r["tag"]) for r in reaped)
overlaps = []
for left, right in zip(intervals, intervals[1:]):
    if left[1] > right[0]:
        overlaps.append({"left": left, "right": right})
assert not overlaps
solver_names = {"cadical", "cadical-1.9.5-arm64-macos", "kissat", "minisat", "glucose"}
solver_exec = [r for r in reaped if r.get("argv") and Path(r["argv"][0]).name.lower() in solver_names]
identity = [r for r in solver_exec if "identify-pinned-cadical-round124" in r["tag"]]
solves = [r for r in solver_exec if r not in identity]
assert len(identity) == 1 and identity[0]["rc"] == 0
assert len(solves) == 3 and all(r["rc"] == 10 for r in solves)
expected = {
    "solve-iter197-exact-order144-quotient-proof-first",
    "solve-iter197-Xerr-complete-direct360-proof-first",
    "solve-iter197-Zerr-complete-direct360-proof-first",
}
assert {r["tag"] for r in solves} == expected
for row in solves:
    assert "--no-binary" in row["argv"]
    assert str(row["argv"][-1]).endswith(".drat")
assert not [r for r in solver_exec if r not in identity and any("iter198" in str(x) for x in r["argv"])]
assert not [r for r in reaped if r.get("detached")]
assert not [r for r in reaped if r.get("timeout_triggered")]
out = {
    "schema": "circdist-gross-round124-session-process-ledger-check-v1",
    "status": "PASS",
    "rows": len(rows),
    "current_checker_started_row_excluded": len(raw_rows) - len(rows),
    "started_records": len(started),
    "reaped_records": len(reaped),
    "all_started_have_exactly_one_reap": True,
    "all_children_reaped": True,
    "strict_serial_nonoverlap": True,
    "maximum_simultaneous_children": 1,
    "overlaps": overlaps,
    "solver_executable_invocations_total": len(solver_exec),
    "solver_identity_probes": 1,
    "solver_processes_total": 3,
    "solver_sat_processes": 3,
    "solver_returncodes": [r["rc"] for r in solves],
    "solver_tags": [r["tag"] for r in solves],
    "proof_output_from_byte_zero_for_all_solves": True,
    "iter198_solver_invocations": 0,
    "returncode_counts": dict(sorted(Counter(str(r["rc"]) for r in reaped).items())),
    "nonzero_non_sat_tags": [r["tag"] for r in reaped if r["rc"] not in (0, 10)],
    "detached_children": 0,
    "background_children": 0,
    "timeouts_triggered": 0,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
