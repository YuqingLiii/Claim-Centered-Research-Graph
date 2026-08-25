#!/usr/bin/env python3
"""Check that public evidence is reachable from the current SE or k-Sum DAG."""

from __future__ import annotations

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ("se", "ksum")
CORE_TOOLS = {
    Path("tools/evidence_closure_check.py"),
    Path("tools/lean_dag_check.py"),
    Path("tools/proof_dag_check.py"),
    Path("tools/proof_dag_schema.py"),
    Path("tools/test_dag_contracts.py"),
}


def collect_paths(value: object, result: set[Path]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"path", "file", "build"} and isinstance(child, str):
                path = Path(child.rstrip("/"))
                if child and not child.startswith(("/", "git:")):
                    result.add(path)
            collect_paths(child, result)
    elif isinstance(value, list):
        for child in value:
            collect_paths(child, result)


def is_reachable(relative: Path, references: set[Path]) -> bool:
    return relative in references or any(parent in references for parent in relative.parents)


def main() -> int:
    references_by_project: dict[str, set[Path]] = {}
    all_references: set[Path] = set()
    errors: list[str] = []
    for project in PROJECTS:
        references: set[Path] = set()
        node_dir = ROOT / project / "proof-dag" / "nodes"
        for node in sorted(node_dir.glob("*.yaml")):
            document = yaml.safe_load(node.read_text(encoding="utf-8"))
            collect_paths(document, references)
        references_by_project[project] = references
        all_references.update(references)

    for reference in sorted(all_references):
        if not (ROOT / reference).exists():
            errors.append(f"missing node-linked path: {reference}")

    for project, references in references_by_project.items():
        project_root = ROOT / project
        prefix = Path(project)
        for store in ("artifacts", "reviews", "tools"):
            root = project_root / store
            if not root.exists():
                continue
            for path in sorted(root.rglob("*")):
                relative = path.relative_to(ROOT)
                if (
                    not path.is_file()
                    or path.name == "README.md"
                    or "__pycache__" in relative.parts
                    or path.suffix in {".pyc", ".pyo"}
                ):
                    continue
                if not is_reachable(relative, references):
                    errors.append(f"unlinked {project} evidence: {relative}")

        foreign_prefixes = [Path(other) for other in PROJECTS if other != project]
        for reference in sorted(references):
            if any(prefix_ == reference or prefix_ in reference.parents for prefix_ in foreign_prefixes):
                errors.append(f"{project} node links another project: {reference}")
            if (
                reference.parts
                and reference.parts[0] in PROJECTS
                and reference.parts[0] != project
            ):
                errors.append(f"{project} node links nonlocal project material: {reference}")

    shared_tool_files = {
        path.relative_to(ROOT)
        for path in (ROOT / "tools").rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix not in {".pyc", ".pyo"}
    }
    unexpected_tools = shared_tool_files - CORE_TOOLS
    if unexpected_tools:
        errors.extend(f"non-shared tool at repository level: {path}" for path in sorted(unexpected_tools))

    for misplaced in ("artifacts", "reviews", "paper", "papers", "research"):
        if (ROOT / misplaced).exists():
            errors.append(
                "project material belongs inside se/ or ksum/, found: "
                f"{misplaced}/"
            )

    if errors:
        print("Evidence-closure check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"Evidence closure OK: {len(all_references)} structured paths; "
        "all public evidence is project-local and linked from SE or k-Sum nodes"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
