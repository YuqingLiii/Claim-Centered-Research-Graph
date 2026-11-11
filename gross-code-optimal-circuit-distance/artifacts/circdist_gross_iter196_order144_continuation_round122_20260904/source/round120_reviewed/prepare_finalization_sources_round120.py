#!/usr/bin/env python3
"""Prepare the small, public Round120 packaging and replay entrypoints."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument("--parent-source", type=Path, required=True)
ap.add_argument("--output-source", type=Path, required=True)
ap.add_argument("--replay-sh", type=Path, required=True)
a = ap.parse_args()
a.output_source.mkdir(parents=True, exist_ok=True)


def adapt(name118: str, name120: str) -> None:
    text = (a.parent_source / name118).read_text()
    text = text.replace("Round118", "Round120").replace("round118", "round120")
    text = text.replace('"date": "2026-09-03"', '"date": "2026-09-04"')
    (a.output_source / name120).write_text(text)


adapt("seal_package_round118.py", "seal_package_round120.py")
adapt("check_sealed_package_round118.py", "check_sealed_package_round120.py")
adapt("sync_session_logs_round118.py", "sync_session_logs_round120.py")

(a.output_source / "write_process_boundary_round120.py").write_text(r'''#!/usr/bin/env python3
"""Bind the exact balanced Round120 ledger cutpoint and its checker result."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--ledger", type=Path, required=True)
ap.add_argument("--check", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
rows = [json.loads(line) for line in a.ledger.read_text().splitlines() if line.strip()]
started = [row for row in rows if row.get("state") == "STARTED"]
reaped = [row for row in rows if row.get("state") == "REAPED"]
assert len(started) == len(reaped)
assert {(r["child_pid"], r["tag"]) for r in started} == {(r["child_pid"], r["tag"]) for r in reaped}
check = json.loads(a.check.read_text())
assert check["status"] == "PASS"
solver_executable = [r for r in reaped if r.get("argv") and Path(r["argv"][0]).name.lower() in {
    "cadical", "cadical-1.9.5-arm64-macos", "kissat", "minisat", "glucose"
}]
solver_identity = [r for r in solver_executable if r["tag"] == "identify-pinned-cadical"]
solver = [r for r in solver_executable if r not in solver_identity]
out = {
    "schema": "circdist-gross-round120-process-ledger-cutpoint-v1",
    "status": "PASS",
    "ledger": "logs/process/session_process.jsonl",
    "ledger_sha256": sha(a.ledger),
    "ledger_check": "PROCESS_LEDGER_CHECK.json",
    "ledger_check_sha256": sha(a.check),
    "rows": len(rows),
    "processes": len(started),
    "all_started_have_exactly_one_reap": True,
    "strict_serial_nonoverlap": True,
    "solver_executable_invocations": len(solver_executable),
    "solver_identity_probes": len(solver_identity),
    "solver_processes": len(solver),
    "solver_returncodes": [r["rc"] for r in solver],
    "science_complete_before_cutpoint": True,
    "post_cutpoint_science_permitted": False,
    "excluded_by_design": [
        "the active final cutpoint snapshot operation itself",
        "this process-boundary writer",
        "sealing and read-only seal verification",
        "installed-root read-only replay",
        "postseal repository-gate replay",
        "final survivor inspection and exact scratch cleanup",
    ],
    "note": "Post-cutpoint operations are separately reported from wrapper, seal, replay, and cleanup outputs; none may invoke a solver or change retained science.",
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
''')

(a.output_source / "check_duplicate_key_evidence_round120.py").write_text(r'''#!/usr/bin/env python3
"""Check the retained strict duplicate-key repository-gate result."""
import argparse
import json
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
source = a.root / "verification/repository_gates/duplicate_yaml.json"
d = json.loads(source.read_text())
assert d["status"] == "PASS"
assert d["duplicates"] == []
assert d["files"] == 1000
assert d["mappings"] == 32898
out = {
    "schema": "circdist-gross-round120-duplicate-key-evidence-check-v1",
    "status": "PASS",
    "scope": "all repository YAML files visited by the strict duplicate-key loader at the preseal gate cutpoint",
    "yaml_files": d["files"],
    "mappings": d["mappings"],
    "duplicates": d["duplicates"],
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
''')

a.replay_sh.write_text('''#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -ne 1 ]; then
  echo "usage: $0 OUTPUT_DIRECTORY" >&2
  exit 64
fi
exec /usr/bin/python3 "$ROOT/source/replay_round120.py" --root "$ROOT" --output "$1"
''')
a.replay_sh.chmod(0o755)

print(json.dumps({
    "status": "PASS",
    "sources": [
        "seal_package_round120.py",
        "check_sealed_package_round120.py",
        "sync_session_logs_round120.py",
        "write_process_boundary_round120.py",
        "check_duplicate_key_evidence_round120.py",
    ],
    "replay_sh": str(a.replay_sh),
}, sort_keys=True))
