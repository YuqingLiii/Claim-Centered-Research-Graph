#!/usr/bin/env python3
"""Verify protected current inputs and their package snapshots."""
from pathlib import Path
import argparse
import hashlib
import json


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--package", type=Path, required=True)
parser.add_argument("--repository", type=Path)
args = parser.parse_args()
package = args.package.resolve()
bindings = json.loads((package / "INPUT_BINDINGS.json").read_text())

for relative, expected in bindings["package_snapshot_sha256"].items():
    observed = sha256(package / relative)
    assert observed == expected, (relative, observed, expected)

if args.repository:
    repository = args.repository.resolve()
    for relative, expected in bindings["expected_protected_sha256"].items():
        observed = sha256(repository / relative)
        assert observed == expected, (relative, observed, expected)

print(
    "PROTECTED_INPUTS_PASS",
    len(bindings["package_snapshot_sha256"]),
    len(bindings["expected_protected_sha256"]) if args.repository else 0,
)
