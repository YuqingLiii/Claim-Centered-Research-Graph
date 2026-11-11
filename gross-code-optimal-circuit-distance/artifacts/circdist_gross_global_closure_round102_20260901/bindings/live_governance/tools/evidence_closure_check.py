#!/usr/bin/env python3
"""Check project-local evidence for projects using the current root layout.

Adapted from the SE/k-Sum release f9249e93. Legacy projects are intentionally
outside this check; their existing validators remain available.
"""
from pathlib import Path
import argparse
import yaml

from proof_dag_schema import load_problem

ROOT = Path(__file__).resolve().parents[1]


def collect_paths(value, result):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {'path', 'file', 'build'} and isinstance(child, str):
                result.add(Path(child.rstrip('/')))
            collect_paths(child, result)
    elif isinstance(value, list):
        for child in value:
            collect_paths(child, result)


def check_project(root, project):
    errors = []
    references = set()
    try:
        loaded = load_problem(root / project)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f'{project}: cannot load nodes: {exc}'], 0
    if not loaded.nodes:
        return [f'{project}: no canonical nodes'], 0
    for node in loaded.nodes.values():
        collect_paths(node, references)
    for relative in sorted(references):
        if relative.is_absolute() or '..' in relative.parts or not relative.parts or relative.parts[0] != project:
            errors.append(f'{project}: nonlocal structured path: {relative}')
        elif not (root / relative).exists():
            errors.append(f'{project}: missing node-linked path: {relative}')
    for store in ('artifacts', 'reviews', 'tools'):
        for path in sorted((root / project / store).rglob('*')):
            if not path.is_file() or path.name == 'README.md' or '__pycache__' in path.parts or path.suffix in {'.pyc', '.pyo'}:
                continue
            relative = path.relative_to(root)
            if relative not in references and not any(parent in references for parent in relative.parents):
                errors.append(f'{project}: unlinked evidence: {relative}')
    return errors, len(references)


def main():
    projects = {p.parent.parent.name for p in ROOT.glob('*/proof-dag/PROJECT.yaml')}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--problem', choices=sorted(projects)+['all'], default='all')
    args = parser.parse_args()
    names = sorted(projects) if args.problem == 'all' else [args.problem]
    if not names:
        print('ERROR: no current-layout projects found')
        return 1
    failures = []
    for name in names:
        errors, count = check_project(ROOT, name)
        failures.extend(errors)
        if not errors:
            print(f'{name}: evidence closure OK, {count} structured paths; all evidence project-local and linked')
    for error in failures:
        print('ERROR:', error)
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
