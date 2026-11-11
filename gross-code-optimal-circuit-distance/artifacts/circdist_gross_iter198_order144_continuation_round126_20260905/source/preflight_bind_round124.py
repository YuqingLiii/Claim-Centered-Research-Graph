#!/usr/bin/env python3
from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path

ROOT = Path('<repo>')
PKG = ROOT / 'circdist/artifacts/circdist_gross_iter196_order144_continuation_round122_20260904'
FRONTIER = PKG / 'frontier/iter197'
SCRATCH = Path('/private/tmp/circdist-round124-proposer')
LEDGER = SCRATCH / 'logs/process/session_process.jsonl'
OUTPUT = SCRATCH / 'verification/preflight_binding.json'

EXPECTED = {
    'scheduler': '614e571512506e8b5e0306fbd01fa52077a98eef449939fb784bfe06d4f4e6f3',
    'proofpilot': 'c363db975d3436eccbdbc57e6d952bee52bf49f0c010484369cb5c0ad46ddbdf',
    'gross': '1ff87b5e421e72c8df4557f23efac5becbf1da35cd6077577b8c211ce5a2b140',
    'review': '436ee1dc38e0506d0048dd07084417964637de50de848ed076449fdf0311b0cb',
    'root_manifest': '8871b88af19ea26b051f9fc1cdeea12e2fcb00dc43e486710748e2493ec36a28',
    'source': '6ce8b8593fabc80ce0917f342126e351da30114802765a46773da348115aec44',
    'semantic_source': 'bee49435279caa3fb6cc02e0f1b145e3568eb54e6d3ac02c49e5bae3c5fa42f4',
    'state': 'cd005e436ff92c66badefb5a30e83531d81d9339bfbc047ebbdbb32627eb1ed0',
    'selector_state': '2b5d1178c5532d62f8e6266d627aaa4c228fa18526e7f79156cc667b1e207608',
    'base': 'f46bc3862e2c4db10570d73d5a364750fa1892d90ecd0fa3d08fe411c3755ef3',
    'quotient': 'fe73a93b7a171fd2afcffe210729f165684297d3d85f4260d883e5ed69ffd334',
    'unstarted_audit': '68e06e13c5242beb3d0170565968b911ba68e2b0715d8c3b91a33c4a8f8761b5',
    'solver': 'fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9',
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(8 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(obj) -> str:
    digest = hashlib.sha256()
    encoder = json.JSONEncoder(sort_keys=True, separators=(',', ':'))
    for text in encoder.iterencode(obj):
        digest.update(text.encode())
    return digest.hexdigest()


def cnf_header(path: Path) -> dict:
    with path.open('rb') as handle:
        while True:
            line = handle.readline()
            assert line, f'no DIMACS header in {path}'
            if line.startswith(b'p cnf '):
                parts = line.split()
                assert len(parts) == 4
                return {'variables': int(parts[2]), 'clauses': int(parts[3]), 'raw': line.decode().strip()}


def parse_manifest(path: Path) -> dict[str, str]:
    rows = {}
    for line in path.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        assert len(digest) == 64 and rel not in rows and not rel.startswith('/') and '..' not in Path(rel).parts
        rows[rel] = digest
    assert list(rows) == sorted(rows)
    return rows


def main() -> None:
    paths = {
        'scheduler': ROOT / 'operations/circdist/SCHEDULER.yaml',
        'proofpilot': Path('/private/tmp/circdist-round124-proofpilot-rank.json'),
        'gross': ROOT / 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml',
        'review': ROOT / 'circdist/reviews/circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md',
        'root_manifest': PKG / 'SHA256SUMS.txt',
        'source': FRONTIER / 'source.json.gz',
        'state': FRONTIER / 'state.json',
        'base': FRONTIER / 'formula/outer.cnf',
        'quotient': FRONTIER / 'order144_quotient/outer.cnf',
        'unstarted_audit': FRONTIER / 'CHECKED_UNSTARTED.json',
        'solver': PKG / 'tooling/cadical-1.9.5-arm64-macos',
    }
    observed = {}
    for key, path in paths.items():
        assert path.is_file(), path
        observed[key] = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': sha256(path)}
        assert observed[key]['sha256'] == EXPECTED[key], (key, observed[key]['sha256'])

    proofpilot = json.loads(paths['proofpilot'].read_text())
    serialized = json.dumps(proofpilot, sort_keys=True)
    assert 'CIRCDIST.gross@dstar-residual' in serialized
    assert '0.00014884524515336767' in serialized

    state = json.loads(paths['state'].read_text())
    assert state['started'] is False and state['stop'] is None and state['next_iteration'] == 197
    assert state['source_file_sha256'] == EXPECTED['source']
    assert state['source_semantic_payload_sha256'] == EXPECTED['semantic_source']
    assert state['selector_state_sha256'] == EXPECTED['selector_state']
    assert state['block_count'] == 814392 and state['selector_count'] == 51552

    with gzip.open(paths['source'], 'rt') as handle:
        source = json.load(handle)
    claimed_semantic = source.pop('semantic_payload_sha256')
    semantic = canonical_sha(source)
    source['semantic_payload_sha256'] = claimed_semantic
    assert semantic == claimed_semantic == EXPECTED['semantic_source']
    assert len(source['blocks']) == 814392 and len(source['selectors']) == 51552
    assert source['expected']['assertions'] == 870342
    selector_projection = [
        {key: selector.get(key) for key in ('mechanism_id', 'sector', 'selected_names', 'data_support', 'group_kinds', 'selector_semantic_sha256')}
        for selector in source['selectors']
    ]
    selector_state = canonical_sha(selector_projection)
    assert selector_state == EXPECTED['selector_state']
    del selector_projection

    base_header = cnf_header(paths['base'])
    quotient_header = cnf_header(paths['quotient'])
    assert base_header == {'variables': 3140244, 'clauses': 11511680, 'raw': 'p cnf 3140244 11511680'}
    assert quotient_header == {'variables': 4375764, 'clauses': 21395983, 'raw': 'p cnf 4375764 21395983'}
    quotient_check = json.loads((FRONTIER / 'order144_quotient/check.json').read_text())
    assert quotient_check['status'] == 'PASS'
    assert quotient_check['encoding']['final_variables'] == 4375764
    assert quotient_check['encoding']['final_clauses'] == 21395983
    assert quotient_check['group']['nonidentity'] == 143
    assert quotient_check['equisatisfiability_theorem']['stabilizers'].startswith('Non-strict <=')

    audit = json.loads(paths['unstarted_audit'].read_text())
    assert audit['status'] == 'PASS' and audit['state_started'] is False
    assert audit['ledger_solver_invocations'] == 0
    assert audit['forbidden_solver_model_assignment_proof_artifacts'] == []
    assert audit['file_count_before_audit_output'] == 15
    audit_rows = {row['path']: row for row in audit['files_before_audit_output']}
    assert len(audit_rows) == 15
    for rel, row in audit_rows.items():
        path = FRONTIER / rel
        assert path.is_file() and path.stat().st_size == row['bytes'] and sha256(path) == row['sha256']

    forbidden_suffixes = ('.drat', '.lrat', '.proof', '.model', '.assignment')
    forbidden = []
    for path in FRONTIER.rglob('*'):
        if not path.is_file():
            continue
        base = path.name.lower()
        if base.endswith(forbidden_suffixes) or any(token in base for token in ('solver.log', 'solver.stderr', 'assignment.dimacs', 'model.dimacs')):
            forbidden.append(path.relative_to(FRONTIER).as_posix())
    assert forbidden == []
    ledger_rows = [json.loads(line) for line in LEDGER.read_text().splitlines() if line.strip()]
    solver_names = {'cadical', 'cadical-1.9.5-arm64-macos', 'kissat', 'minisat', 'glucose', 'cryptominisat5'}
    prior_solver_starts = [row for row in ledger_rows if row.get('state') == 'STARTED' and row.get('argv') and Path(row['argv'][0]).name.lower() in solver_names]
    assert prior_solver_starts == []

    manifest = parse_manifest(paths['root_manifest'])
    assert len(manifest) == 667
    for path in (paths['source'], paths['state'], paths['base'], paths['quotient'], paths['unstarted_audit'], paths['solver']):
        rel = path.relative_to(PKG).as_posix()
        assert manifest[rel] == sha256(path)

    output = {
        'schema': 'circdist-gross-round124-iter197-preflight-binding-v1',
        'status': 'PASS',
        'dispatch': {
            'winner': 'CIRCDIST.gross@dstar-residual',
            'score': '0.00014884524515336767',
            'observed': observed,
        },
        'frontier': {
            'iteration': 197,
            'status_before_science': 'CHECKED_UNSTARTED',
            'source_sha256': EXPECTED['source'],
            'semantic_source_sha256': semantic,
            'state_sha256': EXPECTED['state'],
            'selector_state_sha256': selector_state,
            'blocks': len(source['blocks']),
            'selectors': len(source['selectors']),
            'assertions': source['expected']['assertions'],
            'base': {**base_header, 'sha256': EXPECTED['base'], 'bytes': paths['base'].stat().st_size},
            'quotient': {**quotient_header, 'sha256': EXPECTED['quotient'], 'bytes': paths['quotient'].stat().st_size, 'roots': 143},
            'unstarted_audit_sha256': EXPECTED['unstarted_audit'],
            'forbidden_artifacts': forbidden,
            'prior_round124_solver_starts': 0,
            'equisatisfiable_with_exact_base': True,
        },
        'root_manifest_rows': len(manifest),
        'limitations': [
            'This preflight does not solve either formula.',
            'The quotient theorem is scoped only to the exact invariant iteration-197 base.',
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status':'PASS','iteration':197,'blocks':len(source['blocks']),'selectors':len(source['selectors']),'assertions':source['expected']['assertions'],'base':base_header,'quotient':quotient_header,'prior_solver_starts':0}, sort_keys=True))


if __name__ == '__main__':
    main()
