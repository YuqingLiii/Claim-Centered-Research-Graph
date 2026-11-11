#!/usr/bin/env python3
"""Promote the read-only second recovery inventory and classify its ps census."""
from pathlib import Path
import argparse
import json
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("--scratch", type=Path, required=True)
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
S, R = a.scratch.resolve(), a.root.resolve()
(R / "logs/recovery").mkdir(parents=True, exist_ok=True)

inv = json.loads((S / "second_recovery_inventory.json").read_text())
inv["interruption"] = {
    "ordinal": 2,
    "kind": "model-capacity",
    "classification": "orchestration-only",
    "science_process_was_interrupted": False,
    "science_artifact_recomputation_authorized_or_performed": False,
    "basis": (
        "the fresh ps census has zero live science children; the package inventory "
        "revalidates all twelve iterations, the exact order-5 result, the unstarted "
        "i172 frontier, all child records, and the commissioned canonical hashes"
    ),
}
(R / "verification/model_capacity_recovery2_inventory.json").write_text(
    json.dumps(inv, indent=2, sort_keys=True) + "\n")

for src, dst in (
    ("second_recovery_inventory.stdout", "logs/recovery/second_recovery_inventory.stdout"),
    ("second_recovery_inventory.stderr", "logs/recovery/second_recovery_inventory.stderr"),
    ("second_recovery_inventory.process.json", "logs/process/second_recovery_inventory.json"),
    ("second_recovery_process_census.stdout", "logs/recovery/second_recovery_process_census.stdout"),
    ("second_recovery_process_census.stderr", "logs/recovery/second_recovery_process_census.stderr"),
    ("second_recovery_process_census.process.json", "logs/process/second_recovery_process_census.json"),
):
    shutil.copy2(S / src, R / dst)

needles = (
    "cadical", "order5_enumerator", "compile_outer_cnf.py",
    "run_round98_campaign.py", "build_direct_from_candidate.py",
    "verify_outer_sat_model.py",
)
lines = (S / "second_recovery_process_census.stdout").read_text().splitlines()
raw = [line for line in lines if any(n in line for n in needles)]
self_hits = [line for line in raw if "second_recovery_process_census" in line or "/bin/ps -axo" in line]
science = [line for line in raw if line not in self_hits]
assert not science, science
census = {
    "schema": "circdist-round98-recovery-process-census-v1",
    "status": "PASS", "recovery_ordinal": 2,
    "command": "/bin/ps -axo pid=,ppid=,stat=,command=",
    "science_process_patterns": list(needles),
    "raw_pattern_matches": raw,
    "excluded_census_wrapper_matches": self_hits,
    "matching_live_science_processes": science,
    "science_survivor_count": 0,
}
(R / "verification/recovery2_process_census.json").write_text(
    json.dumps(census, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "recovery": 2,
                  "science_survivor_count": 0}, sort_keys=True))
