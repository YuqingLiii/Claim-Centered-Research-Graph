#!/usr/bin/env python3
"""Check links between current proof-DAG nodes and their Lean formalizations."""

from __future__ import annotations

import argparse
import re
import tempfile
from pathlib import Path

import yaml

from proof_dag_schema import claim_hash


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {
    "se": ROOT / "se",
    "ksum": ROOT / "ksum",
}
DECLARATION = r"^\s*(?:def|abbrev|theorem|lemma)\s+{}\b"


def _load_nodes(project_root: Path) -> list[tuple[Path, dict]]:
    records = []
    for path in sorted((project_root / "proof-dag" / "nodes").glob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(record, dict):
            records.append((path, record))
    return records


def _has_declaration(text: str, name: str) -> bool:
    return bool(re.search(DECLARATION.format(re.escape(name)), text, re.MULTILINE))


def validate_project(root: Path, project_root: Path) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    for node_path, node in _load_nodes(project_root):
        formalization = node.get("formalization")
        if formalization is None:
            continue
        checked += 1
        node_id = str(node.get("id", node_path.stem))
        lean = formalization.get("lean") if isinstance(formalization, dict) else None
        if not isinstance(lean, dict):
            errors.append(f"{node_id}: formalization.lean must be a mapping")
            continue

        file_value = lean.get("file")
        if not isinstance(file_value, str) or not file_value:
            errors.append(f"{node_id}: formalization.lean.file is required")
            continue
        lean_path = Path(file_value)
        if lean_path.is_absolute() or ".." in lean_path.parts:
            errors.append(f"{node_id}: Lean file must use a repository-relative path")
            continue
        full_path = root / lean_path
        if not full_path.is_file():
            errors.append(f"{node_id}: missing Lean file {file_value}")
            continue

        text = full_path.read_text(encoding="utf-8")
        claim = node.get("claim")
        if not isinstance(claim, str):
            errors.append(f"{node_id}: claim must be a string")
            continue
        expected_hash = claim_hash(claim)
        if lean.get("claim_hash") != expected_hash:
            errors.append(f"{node_id}: claim_hash does not match the current node claim")
        if lean.get("sync_state") == "current":
            if lean.get("source_claim_hash") not in (None, expected_hash):
                errors.append(f"{node_id}: source_claim_hash does not match the current claim")
            if expected_hash.removeprefix("sha256:") not in text[:6000]:
                errors.append(f"{node_id}: Lean file does not quote the current claim hash")

        claim_name = lean.get("claim")
        if not isinstance(claim_name, str) or not _has_declaration(text, claim_name):
            errors.append(f"{node_id}: declared Lean claim {claim_name!r} is absent from {file_value}")
        for theorem in lean.get("theorems") or []:
            if not _has_declaration(text, str(theorem)):
                errors.append(f"{node_id}: declared theorem {theorem!r} is absent from {file_value}")

        state = lean.get("state")
        if state in {"composition-checked", "proved"} and not lean.get("theorems"):
            errors.append(f"{node_id}: {state} requires at least one declared theorem")
        if state == "composition-checked" and "rel" not in lean:
            errors.append(f"{node_id}: composition-checked requires an explicit rel list")

        build = lean.get("build")
        if build:
            build_path = root / str(build)
            if not build_path.exists():
                errors.append(f"{node_id}: missing linked build evidence {build}")
        elif state in {"composition-checked", "proved"}:
            warnings.append(f"{node_id}: no build-evidence path is linked")

    return errors, warnings, checked


def selftest() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        project = root / "se"
        nodes = project / "proof-dag" / "nodes"
        lean_dir = project / "lean" / "SE"
        nodes.mkdir(parents=True)
        lean_dir.mkdir(parents=True)
        claim = "One equals one."
        digest = claim_hash(claim)
        lean_file = lean_dir / "Test.lean"
        lean_file.write_text(
            f"/- claim-hash: {digest.removeprefix('sha256:')} -/\n"
            "def Claim : Prop := 1 = 1\n"
            "theorem checked : Claim := rfl\n",
            encoding="utf-8",
        )
        record = {
            "id": "SE.Test",
            "claim": claim,
            "assessment": {"level": "OPEN", "summary": "Fixture."},
            "formalization": {"lean": {
                "module": "SE.Test",
                "file": "se/lean/SE/Test.lean",
                "claim": "Claim",
                "state": "proved",
                "claim_hash": digest,
                "source_claim_hash": digest,
                "sync_state": "current",
                "theorems": ["checked"],
            }},
        }
        (nodes / "SE.Test.yaml").write_text(
            yaml.safe_dump(record, sort_keys=False), encoding="utf-8"
        )
        errors, _, count = validate_project(root, project)
        if errors or count != 1:
            print("SELFTEST FAIL:", errors)
            return 1
        record["formalization"]["lean"]["claim_hash"] = "sha256:bad"
        (nodes / "SE.Test.yaml").write_text(
            yaml.safe_dump(record, sort_keys=False), encoding="utf-8"
        )
        errors, _, _ = validate_project(root, project)
        if not any("claim_hash" in error for error in errors):
            print("SELFTEST FAIL: hash drift was not detected")
            return 1
    print("Lean-DAG selftest: 2/2 checks passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", choices=("se", "ksum", "all"), default="all")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()

    names = tuple(PROJECTS) if args.problem == "all" else (args.problem,)
    failures = 0
    for name in names:
        errors, warnings, count = validate_project(ROOT, PROJECTS[name])
        for warning in warnings:
            print(f"WARNING: {warning}")
        for error in errors:
            print(f"FAIL: {error}")
        failures += len(errors)
        if not errors:
            print(f"{name}: {count} linked Lean formalizations structurally valid")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
