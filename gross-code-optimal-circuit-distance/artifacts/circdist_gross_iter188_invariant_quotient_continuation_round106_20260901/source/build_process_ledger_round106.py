#!/usr/bin/env python3
"""Build the retained Round106 PID/FIX-2 ledger."""
from pathlib import Path
import argparse
import collections
import json


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
args = ap.parse_args()
root = args.root.resolve()
records = []
for path in sorted((root / "logs/process").glob("*.json")):
    row = json.loads(path.read_text())
    assert row["schema"] == "circdist-gross-round106-process-record-v1", (path, row.get("schema"))
    assert row["reaped"] is True and row["detached"] is False
    assert row["timed_out"] is False and row["ended_unix"] >= row["started_unix"]
    records.append({"path": path.relative_to(root).as_posix(), **row})

solvers = []
for row in records:
    command = row.get("command", [])
    if command and "cadical" in Path(str(command[0])).name:
        solvers.append({"name": row["name"], "path": row["path"],
                        "pid": row["child_pid"], "started_unix": row["started_unix"],
                        "ended_unix": row["ended_unix"], "wall_seconds": row["wall_seconds"],
                        "returncode": row["returncode"]})
solvers.sort(key=lambda row: row["started_unix"])
overlaps = [{"left": left, "right": right} for left, right in zip(solvers, solvers[1:])
            if left["ended_unix"] > right["started_unix"]]
assert not overlaps and len(solvers) == 3
assert [row["returncode"] for row in solvers] == [10, 10, 10]

failures = [{"name": row["name"], "path": row["path"],
             "returncode": row["returncode"]}
            for row in records if row["returncode"] not in (0, 10, 20)]
replay = json.loads((root / "verification/preseal_replay.json").read_text())
validators = json.loads((root / "verification/repository_validators/summary.json").read_text())

postseal = json.loads((root / "verification/postseal_replay.json").read_text())
assert postseal["status"] == "PASS" and postseal["all_children_reaped"]
census = json.loads((root / "verification/final_process_census.json").read_text())
assert replay["status"] == validators["status"] == census["status"] == "PASS"
assert replay["all_children_reaped"] and replay["detached_processes"] == 0
assert validators["all_children_reaped"] and validators["detached_processes"] == 0
assert census["science_survivor_count"] == 0 and census["ps_child_reaped"]
returncodes = collections.Counter(str(row["returncode"]) for row in records)
result = {"schema": "circdist-gross-round106-process-fix2-ledger-v1",
          "status": "PASS", "retained_pid_record_count": len(records),
          "records": records, "returncodes": dict(sorted(returncodes.items())),
          "solver_intervals": solvers, "solver_interval_count": len(solvers),
          "strict_solver_nonoverlap": True, "solver_overlaps": overlaps,
          "recorded_failed_attempts": failures,
          "package_replay_children": replay["children"],
          "package_replay_child_count": replay["direct_child_count"],
          "postseal_replay_children": postseal["children"],
          "postseal_replay_child_count": postseal["direct_child_count"],
          "repository_validator_children": validators["checks"],
          "repository_validator_child_count": validators["check_count"],
          "proof_control_nested_children": json.loads(
              (root / "controls/proof_toolchain_controls.json").read_text())["runs"],
          "final_process_census": census,
          "all_pid_bearing_children_reaped": True,
          "retained_wrapper_timeouts": 0, "retained_detached_processes": 0,
          "science_survivor_count": 0,
          "scope_note": "inspection/orchestration shell calls outside the retained science wrappers are disclosed in FAILURE_LEDGER.md; all solver, verifier, replay, gate, and census children are PID-recorded."}
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "pid_records": len(records),
                  "solver_intervals": len(solvers), "failed_attempts": len(failures),
                  "replay_children": replay["direct_child_count"],
                  "postseal_replay_children": postseal["direct_child_count"],
                  "validator_children": validators["check_count"],
                  "science_survivors": 0}, sort_keys=True))
