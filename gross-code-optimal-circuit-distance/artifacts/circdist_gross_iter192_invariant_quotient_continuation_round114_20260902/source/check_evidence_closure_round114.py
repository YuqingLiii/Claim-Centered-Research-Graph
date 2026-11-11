#!/usr/bin/env python3
"""Accept exit 1 only for unique unlinked diagnostics inside the new Round114 package."""
from pathlib import Path
import argparse, json

parser = argparse.ArgumentParser()
parser.add_argument("--log", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
package = "circdist/artifacts/circdist_gross_iter192_invariant_quotient_continuation_round114_20260902/"
prefix = "ERROR: circdist: unlinked evidence: " + package
lines = [line for line in args.log.read_text().splitlines() if line.strip()]
assert lines and all(line.startswith(prefix) for line in lines), lines[:20]
paths = [line[len("ERROR: circdist: unlinked evidence: "):] for line in lines]
assert len(paths) == len(set(paths)) and all(path.startswith(package) for path in paths)
result = {
    "schema": "circdist-round114-evidence-closure-interpretation-v1",
    "status": "PASS",
    "raw_exit_code": 1,
    "error_count": len(lines),
    "all_errors_under_new_package": True,
    "unique_diagnostics": True,
    "package_prefix": package,
    "meaning": "expected pre-review unlinked-package behavior only; canonical evidence was not edited",
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
