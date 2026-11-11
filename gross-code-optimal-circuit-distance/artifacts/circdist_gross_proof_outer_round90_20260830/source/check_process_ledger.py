#!/usr/bin/env python3
"""Check that every proof-producing solver child completed and was reaped."""
from pathlib import Path
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
ledger = json.loads((root / "PROCESS_LEDGER.json").read_text())
assert ledger["status"] == "PASS"
assert ledger["foreground_bounded_solver_processes"] == 36
assert ledger["all_children_reaped"] is True
assert ledger["os_background_processes_started"] == 0
assert ledger["survivors_at_serialization"] == 0
assert len(ledger["processes"]) == 36
names = set()
for process in ledger["processes"]:
    assert process["returncode"] == 10
    assert process["timed_out"] is False
    assert process["final_status"] == "exited_and_reaped"
    assert process["child_pid"] > 0 and process["runner_pid"] > 0
    assert process["name"] not in names
    names.add(process["name"])
for iteration in range(112, 124):
    assert f"outer_iter{iteration}_cadical" in names
    assert f"direct_iter{iteration}_Xerr_cadical" in names
    assert f"direct_iter{iteration}_Zerr_cadical" in names
print("PROCESS_LEDGER_PASS", len(names))
