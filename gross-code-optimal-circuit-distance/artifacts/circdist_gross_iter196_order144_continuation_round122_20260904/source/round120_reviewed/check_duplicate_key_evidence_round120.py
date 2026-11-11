#!/usr/bin/env python3
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
