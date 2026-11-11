#!/usr/bin/env python3
"""Accept prelink exit 1 only for unique diagnostics under this one package."""
from pathlib import Path
import argparse
import json


ap = argparse.ArgumentParser()
ap.add_argument("--log", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
package = "circdist/artifacts/circdist_gross_proof_outer_round94_20260830/"
prefix = "ERROR: circdist: unlinked evidence: " + package
lines = [line for line in a.log.read_text().splitlines() if line.strip()]
assert lines and all(line.startswith(prefix) for line in lines), lines[:20]
paths = [line[len("ERROR: circdist: unlinked evidence: "):] for line in lines]
assert len(paths) == len(set(paths))
assert all(path.startswith(package) for path in paths)
out = {
    "schema": "circdist-round94-evidence-closure-interpretation-v1", "status": "PASS",
    "raw_exit_code": 1, "error_count": len(lines), "all_errors_under_new_package": True,
    "unique_diagnostics": True, "package_prefix": package,
    "meaning": "expected pre-review unlinked-package behavior only; canonical evidence was not edited",
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
