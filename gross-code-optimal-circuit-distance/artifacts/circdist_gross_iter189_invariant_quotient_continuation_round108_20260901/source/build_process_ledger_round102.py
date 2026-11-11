#!/usr/bin/env python3
"""Build and check the Round102 retained process/failure ledger."""
from pathlib import Path
import argparse
import collections
import json


NEGATIVE_CONTROL_PREFIXES = (
    "proof_control_corrupt_", "proof_control_truncated_",
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    records = []
    bootstrap_children = []
    for path in sorted((root / "logs/process").glob("*.json")):
        row = json.loads(path.read_text())
        relative = path.relative_to(root).as_posix()
        if row.get("schema") == "circdist-round94-process-record-v1":
            assert row["reaped"] is True
            assert row["detached"] is False
            assert row["timed_out"] is False
            assert row["ended_unix"] >= row["started_unix"]
        elif path.name == "bootstrap_package.json":
            assert row["all_children_reaped"] is True
            assert row["detached_processes"] == 0
            for child in row["children"]:
                assert child["reaped"] is True and child["detached"] is False
                bootstrap_children.append({**child, "container_record": relative})
        else:
            raise AssertionError((path, row.get("schema")))
        records.append({"path": relative, **row})

    solvers = []
    for row in records:
        name = row.get("name", "")
        command = row.get("command", [])
        is_solver = ("cadical" in name and not any(token in name for token in
                     ("assignment", "verify", "proof_control", "fixture")))
        is_solver = is_solver or (command and "cadical" in Path(str(command[0])).name
                                  and "proof_control" not in name
                                  and "fixture" not in name
                                  and name != "bootstrap_package")
        if is_solver:
            solvers.append({
                "name": name,
                "path": row["path"],
                "pid": row.get("child_pid"),
                "started_unix": row["started_unix"],
                "ended_unix": row["ended_unix"],
                "wall_seconds": row["wall_seconds"],
                "returncode": row["returncode"],
            })
    solvers.sort(key=lambda row: (row["started_unix"], row["ended_unix"]))
    overlaps = []
    for left, right in zip(solvers, solvers[1:]):
        if left["ended_unix"] > right["started_unix"]:
            overlaps.append({"left": left, "right": right})
    assert not overlaps, overlaps

    returncodes = collections.Counter(str(row.get("returncode")) for row in records)
    expected_negative = []
    corrected_failures = []
    for row in records:
        if row.get("returncode") in (0, 10, 20):
            continue
        name = row.get("name", "")
        target = expected_negative if name.startswith(NEGATIVE_CONTROL_PREFIXES) else corrected_failures
        target.append({"name": name, "path": row["path"],
                       "returncode": row["returncode"]})

    survivor = root / "verification/final_survivor_scan.json"
    survivor_record = json.loads(survivor.read_text()) if survivor.exists() else None
    if survivor_record is not None:
        assert survivor_record["status"] == "PASS"
        assert survivor_record["science_survivor_count"] == 0

    output = {
        "schema": "circdist-gross-round102-process-ledger-v1",
        "status": "PASS",
        "retained_process_records": len(records),
        "records": records,
        "bootstrap_children": bootstrap_children,
        "bootstrap_child_pid_limitation": (
            "two initial synchronous subprocess.run children record null child_pid; "
            "command, interval, return code, stdout/stderr, reaping, and non-detachment are retained"
        ),
        "returncodes": dict(sorted(returncodes.items())),
        "solver_intervals": solvers,
        "solver_interval_count": len(solvers),
        "strict_solver_nonoverlap": True,
        "solver_overlaps": overlaps,
        "expected_rejected_negative_controls": expected_negative,
        "corrected_failed_attempts": corrected_failures,
        "all_pid_bearing_children_reaped": True,
        "retained_detached_processes": 0,
        "retained_wrapper_timeouts": 0,
        "final_survivor_scan": survivor_record,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS", "records": len(records),
        "solver_intervals": len(solvers), "returncodes": dict(returncodes),
        "science_survivors": None if survivor_record is None else 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
