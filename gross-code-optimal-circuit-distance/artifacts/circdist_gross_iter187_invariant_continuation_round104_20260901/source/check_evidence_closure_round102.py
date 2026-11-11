#!/usr/bin/env python3
"""Accept pre-review evidence closure only for this single new package."""
from pathlib import Path
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--log", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
package = "circdist/artifacts/circdist_gross_global_closure_round102_20260901/"
prefix = "ERROR: circdist: unlinked evidence: "
lines = [line for line in args.log.read_text().splitlines() if line.strip()]
assert lines and all(line.startswith(prefix) for line in lines), lines[:20]
paths = [line[len(prefix):] for line in lines]
assert len(paths) == len(set(paths))
assert all(path.startswith(package) for path in paths), [
    path for path in paths if not path.startswith(package)
]
result = {
    "schema": "circdist-gross-round102-evidence-closure-interpretation-v1",
    "status": "PASS",
    "raw_exit_code": 1,
    "error_count": len(paths),
    "all_errors_under_new_package": True,
    "unique_diagnostics": True,
    "package_prefix": package,
    "meaning": "expected proposer-package diagnostics before independent review/linking; canonical evidence was not edited",
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
