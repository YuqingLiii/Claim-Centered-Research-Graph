#!/usr/bin/env python3
"""Validate the current Set Equality and k-Sum proof DAGs."""

from __future__ import annotations

import argparse
from pathlib import Path
import yaml

from proof_dag_schema import load_problem, validate_preservation, validate_problem, write_generated


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS = {
    "se": ROOT / "se",
    "ksum": ROOT / "ksum",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", choices=("se", "ksum", "all"), default="all")
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
        if args.write_generated:
            write_generated(PROBLEMS[name], name)
        errors, warnings, count = validate_problem(ROOT, PROBLEMS[name], name)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        if args.previous_state is not None:
            previous_project = args.previous_state / name
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

    for warning in all_warnings:
        print(f"WARNING: {warning}")
    for error in all_errors:
        print(f"ERROR: {error}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
