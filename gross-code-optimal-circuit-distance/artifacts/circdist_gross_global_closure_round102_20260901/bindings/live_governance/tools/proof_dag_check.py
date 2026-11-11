#!/usr/bin/env python3
"""Validate current claim-centered projects and the unchanged legacy SE/k-Sum records."""

from __future__ import annotations

import argparse
from pathlib import Path
import yaml

from proof_dag_schema import load_problem, validate_preservation, validate_problem, write_generated
# Preserve the import interface used by the existing Lean checker.
from proof_dag_legacy import normalize_grouped, parse_front_matter, parse_node
import proof_dag_legacy


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = {
    "se": ROOT / "research/se",
    "ksum": ROOT / "research/ksum",
    "circdist": ROOT / "circdist",
    "holevo-additivity-equality": ROOT / "holevo-additivity-equality",
    "holevo-counterexample-prevalence": ROOT / "holevo-counterexample-prevalence",
    "holevo-extensive-violation": ROOT / "holevo-extensive-violation",
    "werner-holevo-capacity-threshold": ROOT / "werner-holevo-capacity-threshold",
    "grothendieck-d4": ROOT / "grothendieck-d4",
    "grothendieck-e8": ROOT / "grothendieck-e8",
    "grothendieck-group-orbit": ROOT / "grothendieck-group-orbit",
}
LEGACY_PROBLEMS = {"se", "ksum"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", choices=tuple(PROBLEMS) + ("all",), default="all")
    parser.add_argument("--verify-git", action="store_true",
                        help="resolve historical git sources for legacy SE/k-Sum records")
    parser.add_argument("--diagnose", choices=("chain-strength",), default=None,
                        help="legacy SE/k-Sum diagnostic; does not modify assessments")
    parser.add_argument(
        "--previous-state",
        type=Path,
        help="earlier repository snapshot for node, route, and append-only event retention checks",
    )
    parser.add_argument(
        "--write-generated",
        action="store_true",
        help="regenerate NODE_INDEX.md and GRAPH.mmd before validation",
    )
    args = parser.parse_args()

    names = tuple(PROBLEMS) if args.problem == "all" else (args.problem,)
    all_errors: list[str] = []
    all_warnings: list[str] = []

    for name in names:
        legacy = name in LEGACY_PROBLEMS
        if args.write_generated:
            if legacy:
                proof_dag_legacy.write_generated_v6(PROBLEMS[name], name)
            else:
                write_generated(PROBLEMS[name], name)
        if legacy:
            errors, warnings, count = proof_dag_legacy.check_problem(name, verify_git=args.verify_git)
        else:
            errors, warnings, count = validate_problem(ROOT, PROBLEMS[name], name)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        if args.previous_state is not None:
            previous_project = args.previous_state / PROBLEMS[name].relative_to(ROOT)
            try:
                previous = load_problem(previous_project)
                if not previous.nodes:
                    raise ValueError("previous snapshot contains no canonical node files")
                retention_errors = validate_preservation(previous, load_problem(PROBLEMS[name]))
            except (OSError, ValueError, yaml.YAMLError) as exc:
                retention_errors = [f"{name}: cannot compare previous state: {exc}"]
            all_errors.extend(retention_errors)
            if not retention_errors:
                print(f"{name}: prior nodes, routes, and events retained")
        if not errors:
            print(f"{name}: {count} node files structurally valid")
        if args.diagnose and legacy:
            proof_dag_legacy.chain_strength_report(name)

    for warning in all_warnings:
        print(f"WARNING: {warning}")
    for error in all_errors:
        print(f"ERROR: {error}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
