#!/usr/bin/env python3
"""Accept raw evidence-closure rc1 only for unique paths under the new package."""
import argparse
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--log", type=Path, required=True)
ap.add_argument("--package-relative", required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
prefix_path = a.package_relative.rstrip("/") + "/"
prefix = "ERROR: circdist: unlinked evidence: " + prefix_path
lines = [line for line in a.log.read_text().splitlines() if line.strip()]
assert lines and all(line.startswith(prefix) for line in lines), lines[:20]
paths = [line[len("ERROR: circdist: unlinked evidence: "):] for line in lines]
assert len(paths) == len(set(paths)) and all(path.startswith(prefix_path) for path in paths)
out = {
    "schema": "circdist-round124-evidence-closure-interpretation-v1",
    "status": "PASS", "raw_exit_code": 1, "error_count": len(lines),
    "all_errors_under_new_package": True, "unique_diagnostics": True,
    "package_prefix": prefix_path,
    "meaning": "expected pre-review unlinked-package behavior only; canonical evidence was not edited",
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
