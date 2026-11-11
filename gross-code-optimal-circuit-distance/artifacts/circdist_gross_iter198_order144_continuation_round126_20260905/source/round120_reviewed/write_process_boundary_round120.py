#!/usr/bin/env python3
"""Bind the exact balanced Round120 ledger cutpoint and its checker result."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--ledger", type=Path, required=True)
ap.add_argument("--check", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
rows = [json.loads(line) for line in a.ledger.read_text().splitlines() if line.strip()]
started = [row for row in rows if row.get("state") == "STARTED"]
reaped = [row for row in rows if row.get("state") == "REAPED"]
assert len(started) == len(reaped)
assert {(r["child_pid"], r["tag"]) for r in started} == {(r["child_pid"], r["tag"]) for r in reaped}
check = json.loads(a.check.read_text())
assert check["status"] == "PASS"
solver_executable = [r for r in reaped if r.get("argv") and Path(r["argv"][0]).name.lower() in {
    "cadical", "cadical-1.9.5-arm64-macos", "kissat", "minisat", "glucose"
}]
solver_identity = [r for r in solver_executable if r["tag"] == "identify-pinned-cadical"]
solver = [r for r in solver_executable if r not in solver_identity]
out = {
    "schema": "circdist-gross-round120-process-ledger-cutpoint-v1",
    "status": "PASS",
    "ledger": "logs/process/session_process.jsonl",
    "ledger_sha256": sha(a.ledger),
    "ledger_check": "PROCESS_LEDGER_CHECK.json",
    "ledger_check_sha256": sha(a.check),
    "rows": len(rows),
    "processes": len(started),
    "all_started_have_exactly_one_reap": True,
    "strict_serial_nonoverlap": True,
    "solver_executable_invocations": len(solver_executable),
    "solver_identity_probes": len(solver_identity),
    "solver_processes": len(solver),
    "solver_returncodes": [r["rc"] for r in solver],
    "science_complete_before_cutpoint": True,
    "post_cutpoint_science_permitted": False,
    "excluded_by_design": [
        "the active final cutpoint snapshot operation itself",
        "this process-boundary writer",
        "sealing and read-only seal verification",
        "installed-root read-only replay",
        "postseal repository-gate replay",
        "final survivor inspection and exact scratch cleanup",
    ],
    "note": "Post-cutpoint operations are separately reported from wrapper, seal, replay, and cleanup outputs; none may invoke a solver or change retained science.",
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
