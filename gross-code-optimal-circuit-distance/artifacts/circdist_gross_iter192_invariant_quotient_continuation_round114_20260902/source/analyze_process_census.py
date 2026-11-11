#!/usr/bin/env python3
"""Classify a raw ps snapshot while excluding the census wrapper itself."""
from pathlib import Path
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument("--input", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()

needles = (
    "cadical", "order5_enumerator", "compile_outer_cnf.py",
    "run_round98_campaign.py", "build_direct_from_candidate.py",
    "verify_outer_sat_model.py",
)
lines = a.input.read_text().splitlines()
raw_hits = [line for line in lines if any(n in line for n in needles)]
self_hits = [
    line for line in raw_hits
    if "recovery_process_census" in line or "/bin/ps -axo" in line
]
science_hits = [line for line in raw_hits if line not in self_hits]
assert not science_hits, science_hits
out = {
    "schema": "circdist-round98-recovery-process-census-v1",
    "status": "PASS",
    "command": "/bin/ps -axo pid=,ppid=,stat=,command=",
    "science_process_patterns": list(needles),
    "raw_pattern_matches": raw_hits,
    "excluded_census_wrapper_matches": self_hits,
    "matching_live_science_processes": science_hits,
    "science_survivor_count": 0,
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "science_survivor_count": 0,
                  "wrapper_false_positives": len(self_hits)}, sort_keys=True))
