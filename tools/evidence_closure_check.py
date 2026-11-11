#!/usr/bin/env python3
"""Check evidence closure for every project and the bounded publication surface.

Every node-linked path must exist or be listed in EVIDENCE_GAPS.yaml (declared, not present).
Every file under <project>/{artifacts,reviews,tools} must be reachable from that project's nodes
(README.md files are navigation and exempt). No node may link another project's material.
"""

from __future__ import annotations

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
CORE_TOOLS = {
    Path("tools/evidence_closure_check.py"),
    Path("tools/lean_dag_check.py"),
    Path("tools/proof_dag_check.py"),
    Path("tools/proof_dag_schema.py"),
    Path("tools/test_dag_contracts.py"),
}
PUBLIC_PAPER = Path("paper/claim-centered-research-record.pdf")


def projects(root: Path) -> list[str]:
    return sorted(p.parent.parent.name for p in root.glob("*/proof-dag/PROJECT.yaml"))


def declared_gaps(root: Path) -> set[Path]:
    registry = root / "EVIDENCE_GAPS.yaml"
    if not registry.is_file():
        return set()
    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    return {Path(str(item["path"]).rstrip("/")) for item in data.get("declared_missing_paths") or []}


def collect_paths(value: object, result: set[Path]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"path", "file", "build"} and isinstance(child, str):
                if child and not child.startswith(("/", "git:")):
                    result.add(Path(child.rstrip("/")))
            collect_paths(child, result)
    elif isinstance(value, list):
        for child in value:
            collect_paths(child, result)


def is_reachable(relative: Path, references: set[Path]) -> bool:
    return relative in references or any(parent in references for parent in relative.parents)


def check_project(root: Path, project: str) -> tuple[list[str], int, list[Path]]:
    errors: list[str] = []
    references: set[Path] = set()
    for node in sorted((root / project / "proof-dag" / "nodes").glob("*.yaml")):
        collect_paths(yaml.safe_load(node.read_text(encoding="utf-8")), references)
    gaps = declared_gaps(root)
    gap_hits: list[Path] = []
    for reference in sorted(references):
        if reference.is_absolute() or ".." in reference.parts or not reference.parts or reference.parts[0] != project:
            errors.append(f"{project}: nonlocal structured path: {reference}")
        elif not (root / reference).exists():
            if reference in gaps:
                gap_hits.append(reference)
            else:
                errors.append(f"{project}: missing node-linked path: {reference}")
    for store in ("artifacts", "reviews", "tools"):
        base = root / project / store
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            relative = path.relative_to(root)
            if (not path.is_file() or path.name == "README.md" or "__pycache__" in relative.parts
                    or path.suffix in {".pyc", ".pyo"}):
                continue
            if not is_reachable(relative, references):
                errors.append(f"{project}: unlinked evidence: {relative}")
    return errors, len(references), gap_hits


def main() -> int:
    errors: list[str] = []
    total, total_gaps = 0, []
    names = projects(ROOT)
    for project in names:
        e, count, gap_hits = check_project(ROOT, project)
        errors.extend(e)
        total += count
        total_gaps.extend(gap_hits)
        if not e:
            note = f"; {len(gap_hits)} declared gaps" if gap_hits else ""
            print(f"{project}: evidence closure OK, {count} structured paths{note}")

    shared_tool_files = {
        path.relative_to(ROOT)
        for path in (ROOT / "tools").rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}
    }
    errors.extend(f"non-shared tool at repository level: {path}" for path in sorted(shared_tool_files - CORE_TOOLS))

    paper_root = ROOT / "paper"
    if paper_root.exists():
        paper_files = {path.relative_to(ROOT) for path in paper_root.rglob("*") if path.is_file()}
        errors.extend(f"unexpected public paper file: {path}" for path in sorted(paper_files - {PUBLIC_PAPER}))
        if PUBLIC_PAPER not in paper_files:
            errors.append(f"missing public paper PDF: {PUBLIC_PAPER}")

    for misplaced in ("artifacts", "reviews", "papers", "research"):
        if (ROOT / misplaced).exists():
            errors.append(f"project material belongs inside a project directory, found: {misplaced}/")

    for gap in total_gaps:
        print(f"DECLARED GAP (linked, not in repository): {gap}")
    if errors:
        print("Evidence-closure check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Evidence closure OK for {len(names)} projects: {total} structured paths; "
          f"{len(total_gaps)} linked paths are declared gaps listed in EVIDENCE_GAPS.yaml and are NOT present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
