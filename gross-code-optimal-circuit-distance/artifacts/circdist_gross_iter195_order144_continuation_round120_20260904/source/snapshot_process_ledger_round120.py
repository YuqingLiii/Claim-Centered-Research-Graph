#!/usr/bin/env python3
"""Write a complete ledger cutpoint, excluding this active snapshot process itself."""
import argparse
import json
import os
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument("--source", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
rows = [json.loads(line) for line in a.source.read_text().splitlines() if line.strip()]
rows = [row for row in rows if row.get("child_pid") != os.getpid()]
started = {(row["child_pid"], row["tag"]) for row in rows if row.get("state") == "STARTED"}
reaped = {(row["child_pid"], row["tag"]) for row in rows if row.get("state") == "REAPED"}
assert started == reaped
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text("".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in rows))
print(json.dumps({"status": "PASS", "rows": len(rows), "processes": len(started),
                  "excluded_active_snapshot_pid": os.getpid()}, sort_keys=True))
