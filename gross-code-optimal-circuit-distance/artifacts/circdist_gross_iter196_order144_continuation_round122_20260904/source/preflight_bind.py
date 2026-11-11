#!/usr/bin/env python3
from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path

ROOT = Path('<repo>')
PKG = ROOT / 'circdist/artifacts/circdist_gross_iter195_order144_continuation_round120_20260904'
FRONTIER = PKG / 'frontier/iter196'
SCRATCH = Path('/private/tmp/circdist-round122-proposer')
LEDGER = SCRATCH / 'logs/process/session_process.jsonl'
OUTPUT = SCRATCH / 'verification/preflight_binding.json'

EXPECTED = {
    'scheduler': '4b91623164ec9c5a9ece1b81a35561945146befbe2c3edd05b669fac1a177eb1',
    'proofpilot': '58cff681f9a5eb7d1db149f9ab2d6d6a111bdb4624058373199cd551faff5e44',
    'gross': '5e94918dbbe3ecc730d1eaa80e70c3b5713e2d87c4b9c44ca33b979b5ef10095',
    'review': 'fc4b1c7e33c1a5f8e6dbad1715baa24b2a6d1a88c8368bc3a3632d768ce05d6d',
    'root_manifest': 'e004f8b28e1bd88916f81b1de55e43efcedb4f4924f0f39a2b52830ba143150d',
    'source': '31256761866d464eba48c278e2247d6f396a1372ad0508886e06e3f24ea6f51a',
    'semantic_source': 'f93cd8e600e1b02db801d84a5b6b2eb0def408f3bca65528c8b0a6b5b0e0b73d',
    'state': 'ab064886695d712b62fddadb8639a75e9d230faa9e8e2d870605ebaf72946da9',
    'selector_state': 'a960134b6315978cd800261ab5dd6ce287a3fd96c7dda5c33abd19c8671527c9',
    'base': 'cf1907663bca93d838d85ba7a4eb8f682f3939b601d4a0295905699f1118e639',
    'quotient': '12d86dfec0d588760a42edc7a8d43ac6f0172415956384bce461da592e08a593',
    'unstarted_audit': '8dabbbd044bd1a85541cf724f0d2ea4b49ba7d048c56f89a4b26e4430f077150',
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
        'proofpilot': Path('/private/tmp/circdist-round122-proofpilot-rank.json'),
        'gross': ROOT / 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml',
        'review': ROOT / 'circdist/reviews/circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md',
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
    assert '0.00040460332515293107' in serialized

    state = json.loads(paths['state'].read_text())
    assert state['started'] is False and state['stop'] is None and state['next_iteration'] == 196
    assert state['source_file_sha256'] == EXPECTED['source']
    assert state['source_semantic_payload_sha256'] == EXPECTED['semantic_source']
    assert state['selector_state_sha256'] == EXPECTED['selector_state']
    assert state['block_count'] == 814392 and state['selector_count'] == 51336

    with gzip.open(paths['source'], 'rt') as handle:
        source = json.load(handle)
    claimed_semantic = source.pop('semantic_payload_sha256')
    semantic = canonical_sha(source)
    source['semantic_payload_sha256'] = claimed_semantic
    assert semantic == claimed_semantic == EXPECTED['semantic_source']
    assert len(source['blocks']) == 814392 and len(source['selectors']) == 51336
    assert source['expected']['assertions'] == 870126
    selector_projection = [
        {key: selector.get(key) for key in ('mechanism_id', 'sector', 'selected_names', 'data_support', 'group_kinds', 'selector_semantic_sha256')}
        for selector in source['selectors']
    ]
    selector_state = canonical_sha(selector_projection)
    assert selector_state == EXPECTED['selector_state']
    del selector_projection

    base_header = cnf_header(paths['base'])
    quotient_header = cnf_header(paths['quotient'])
    assert base_header == {'variables': 3130306, 'clauses': 11477997, 'raw': 'p cnf 3130306 11477997'}
    assert quotient_header == {'variables': 4365826, 'clauses': 21362300, 'raw': 'p cnf 4365826 21362300'}
    quotient_check = json.loads((FRONTIER / 'order144_quotient/check.json').read_text())
    assert quotient_check['status'] == 'PASS'
    assert quotient_check['encoding']['final_variables'] == 4365826
    assert quotient_check['encoding']['final_clauses'] == 21362300
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
    assert len(manifest) == 594
    for path in (paths['source'], paths['state'], paths['base'], paths['quotient'], paths['unstarted_audit'], paths['solver']):
        rel = path.relative_to(PKG).as_posix()
        assert manifest[rel] == sha256(path)

    output = {
        'schema': 'circdist-gross-round122-iter196-preflight-binding-v1',
        'status': 'PASS',
        'dispatch': {
            'winner': 'CIRCDIST.gross@dstar-residual',
            'score': '0.00040460332515293107',
            'observed': observed,
        },
        'frontier': {
            'iteration': 196,
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
            'prior_round122_solver_starts': 0,
            'equisatisfiable_with_exact_base': True,
        },
        'root_manifest_rows': len(manifest),
        'limitations': [
            'This preflight does not solve either formula.',
            'The quotient theorem is scoped only to the exact invariant iteration-196 base.',
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status':'PASS','iteration':196,'blocks':len(source['blocks']),'selectors':len(source['selectors']),'assertions':source['expected']['assertions'],'base':base_header,'quotient':quotient_header,'prior_solver_starts':0}, sort_keys=True))


if __name__ == '__main__':
    main()
