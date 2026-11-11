#!/usr/bin/env python3
"""Verify the 2026-08-26 migration, not the mathematical truth of its claims.

Archive retention across the format boundary is distinct from --previous-state
retention between two current-format snapshots. This check uses saved hashes,
never the historical Git checker that omitted circdist.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json

from proof_dag_schema import _load_yaml, claim_hash, load_problem, validate_preservation

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / 'maintenance/circdist_protocol_20260826'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(root=ROOT, record=RECORD, check_working_tree=False):
    errors = []
    protected = json.loads((record/'protected_files.json').read_text())
    copies = json.loads((record/'copies.json').read_text())
    path_map = json.loads((record/'path_map.json').read_text())
    original_root = record/'before/research/circdist/proof-dag'
    originals = {p.stem:_load_yaml(p) for p in sorted((original_root/'nodes').glob('*.yaml'))}
    current = load_problem(root/'circdist')
    migrated = load_problem(record/'baseline/circdist')
    baseline_hashes = json.loads((record/'baseline_files.json').read_text())
    for relative, expected in baseline_hashes.items():
        path = record/'baseline'/relative
        if not path.is_file() or digest(path) != expected:
            errors.append(f'Post-migration baseline changed or missing: {relative}')
    if set(originals) != set(migrated.nodes):
        errors.append('Migration changed the registered node set')
    if _load_yaml(original_root/'PROJECT.yaml')['roots'] != migrated.roots:
        errors.append('Migration changed the four project roots')
    if check_working_tree:
        for relative, expected in protected.items():
            path = root/relative
            if not path.is_file() or digest(path) != expected:
                errors.append(f'Protected original changed or missing: {relative}')
    for entry in copies:
        path = root/entry['path']
        if not path.is_file() or digest(path) != entry['sha256']:
            errors.append(f'Copied archival bytes changed or missing: {entry["path"]}')

    def relocate(x):
        if isinstance(x,dict):
            return {k:path_map.get(v,v) if k=='path' and isinstance(v,str) else relocate(v) for k,v in x.items()}
        if isinstance(x,list): return [relocate(v) for v in x]
        return x

    events = 0
    claims = {}
    for node_id, old in originals.items():
        if node_id not in migrated.nodes: continue
        new = migrated.nodes[node_id]
        # Entire routes are compared: statements, premises, assumptions, proof,
        # review scope, reviewed hashes, assessments and caveats are all protected.
        for key in ['id','role','aliases','claim','routes','assumptions','disposition','formalization']:
            if relocate(old.get(key)) != new.get(key):
                errors.append(f'{node_id}: invariant changed: {key}')
        for key in ['level','caveats']:
            if old['assessment'].get(key) != new['assessment'].get(key):
                errors.append(f'{node_id}: assessment {key} changed')
        for key, values in old['assessment'].get('basis',{}).items():
            expected = relocate(values)
            actual = new['assessment'].get('basis',{}).get(key,[])
            if key == 'evidence':
                if any(v not in actual for v in expected):
                    errors.append(f'{node_id}: historical evidence link lost')
            elif actual != expected:
                errors.append(f'{node_id}: assessment basis {key} changed')
        archive = root/'circdist/artifacts/history/pre_protocol_20260826/nodes'/(node_id+'.yaml')
        if archive.is_file():
            historical = _load_yaml(archive)
            if historical != old:
                errors.append(f'{node_id}: archived original differs from saved baseline')
            events += len(historical.get('events',{}))
            ref = archive.relative_to(root).as_posix()
            if not any(e.get('path')==ref for e in new['assessment']['basis']['evidence']):
                errors.append(f'{node_id}: archived history not linked from current node')
        claims[node_id] = claim_hash(new['claim'])
    old_budget = _load_yaml(record/'before/research/circdist/notes/SCHEDULER.yaml')['budget']
    if _load_yaml(record/'baseline/operations/circdist/SCHEDULER.yaml')['budget'] != old_budget:
        errors.append('Budget changed during migration')
    baseline = record/'baseline/circdist'
    if not baseline.exists():
        errors.append('Post-migration preservation baseline is missing')
    else:
        errors.extend(validate_preservation(load_problem(baseline),current))
    return {
        'ok':not errors,
        'scope':'Mechanical migration and retained evidence only; no proof, independent review, solver run, or promotion.',
        'nodes':len(current.nodes),'archived_events':events,
        'protected_original_files':len(protected),'byte_identical_copies':len(copies),
        'working_tree_protected_files_checked':check_working_tree,
        'levels':dict(Counter(n['assessment']['level'] for n in current.nodes.values())),
        'claim_hashes':claims,'errors':errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path,help='optionally write the verification result as JSON')
    parser.add_argument('--check-working-tree', action='store_true',
                        help='one-time check that every old circdist/SE/k-Sum file is still unchanged; omit after later authorized research edits')
    args = parser.parse_args()
    result = verify(check_working_tree=args.check_working_tree)
    if args.report:
        args.report.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    for error in result['errors']:
        print('ERROR:',error)
    if result['ok']:
        extra = f', {result["protected_original_files"]} untouched original files' if args.check_working_tree else ''
        print(f'Migration preservation OK: {result["nodes"]} nodes, {result["archived_events"]} original events, {result["byte_identical_copies"]} byte-identical copies{extra}')
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
