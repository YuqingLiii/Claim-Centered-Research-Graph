#!/usr/bin/env python3
"""Verify the live governance inputs still equal the retained Round102 bindings."""
from pathlib import Path
import argparse
import hashlib
import json


parser = argparse.ArgumentParser()
parser.add_argument("--repository", type=Path, required=True)
parser.add_argument("--package", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
repository = args.repository.resolve()
package = args.package.resolve()
bindings = json.loads((package / "bindings" / "LIVE_GOVERNANCE.json").read_text())
assert bindings["status"] == "PASS"
for row in bindings["rows"]:
    live = repository / row["original_path"]
    stored = package / row["stored_path"]
    assert live.is_file() and stored.is_file()
    live_raw = live.read_bytes()
    stored_raw = stored.read_bytes()
    assert live_raw == stored_raw
    assert hashlib.sha256(live_raw).hexdigest() == row["sha256"]
    assert len(live_raw) == row["bytes"] and live_raw.count(b"\n") == row["lf"]
result = {
    "schema": "circdist-gross-round102-live-governance-check-v1",
    "status": "PASS",
    "files_checked": len(bindings["rows"]),
    "canonical_scheduler_review_protocols_tooling_unchanged": True,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
