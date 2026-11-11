#!/usr/bin/env python3
"""Read-only verifier for the sealed round-63 package."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
import model as M
from pattern import build_global_single_summary


def sha_bytes(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha_obj(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def fail(message):
    raise AssertionError(message)


def verify_manifest():
    lines = (ROOT / 'SHA256SUMS.txt').read_text().splitlines()
    entries = {}
    for line in lines:
        digest, rel = line.split('  ', 1)
        path = ROOT / rel
        if rel in entries or not path.is_file() or sha_bytes(path) != digest:
            fail('manifest mismatch: ' + rel)
        entries[rel] = digest
    actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
              if p.is_file() and p.name != 'SHA256SUMS.txt'}
    if set(entries) != actual:
        fail('manifest coverage mismatch')
    return len(entries)


def verify_bindings(repo_root):
    bindings = json.loads((ROOT / 'bindings.json').read_text())
    checked = 0
    if repo_root is not None:
        for rel, record in bindings['files'].items():
            path = repo_root / rel
            if not path.is_file() or sha_bytes(path) != record['sha256'] or path.stat().st_size != record['bytes']:
                fail('live binding mismatch: ' + rel)
            checked += 1
    conflicts = bindings['round62_binding_conflicts']
    if len(conflicts) != 2 or any(x['round62_sha256'] == x['round63_disk_sha256'] for x in conflicts):
        fail('round62/current binding conflict ledger mismatch')
    return checked


def pools():
    px = M.expand_pool(ROOT / 'inputs/w12X.txt', M.HX, M.HZ)
    pz = M.expand_pool(ROOT / 'inputs/w12Z.txt', M.HZ, M.HX)
    lx = M.logical_basis(px, M.HX)
    lz = M.logical_basis(pz, M.HZ)
    if (len(px), len(pz), len(lx), len(lz)) != (1884, 1884, 12, 12):
        fail('frozen pool/basis reconstruction mismatch')
    return px, pz, lx, lz


def verify_round62(lx, lz):
    ledger = json.loads((ROOT / 'outputs/round62_cegar20.json').read_text())['ledger']
    if len(ledger) != 20:
        fail('round62 ledger length mismatch')
    prior = []
    schedules = set()
    traces = set()
    for i, step in enumerate(ledger):
        if step['iteration'] != i or step['outer']['status'] != 'SAT':
            fail(f'round62 iteration/status mismatch at {i}')
        times = step['schedule']
        if sha_obj(times) != step['schedule_sha256']:
            fail(f'round62 schedule hash mismatch at {i}')
        audit = M.audit_schedule(times, True)
        if not audit['ok'] or not audit['global_interleaved']:
            fail(f'round62 schedule audit failed at {i}')
        if any(M.block_holds(times, atoms) for atoms in prior):
            fail(f'round62 prior block exclusion failed at {i}')
        block = step['block']
        sec = M.Sector(block['sector'], times, lz if block['sector'] == 'Xerr' else lx)
        witness = step['effective'][block['sector']]['witness']
        replay = sec.verify_effective_selection(witness['selected'], 10)
        if not replay['ok'] or replay['net_support'] != witness['net_support']:
            fail(f'round62 raw witness failed at {i}')
        if not M.block_holds(times, block['atoms']):
            fail(f'round62 source block failed at {i}')
        prior.append(block['atoms'])
        schedules.add(step['schedule_sha256'])
        traces.add(block['trace_sha256'])
    if len(schedules) != 20 or len(traces) != 20:
        fail('round62 uniqueness mismatch')
    return {'iterations': 20, 'exclusions': 190, 'witnesses': 20}


def verify_controls(lx, lz):
    # These are regenerated from raw schedules, not accepted from JSON flags.
    import run as R
    c1 = M.Sector('Zerr', R.control_schedule('C1'), lx)
    if not M.c1_named_certificate(c1)['ok']:
        fail('C1 direct-360 control failed')
    for label, dual in (('Xerr', lz), ('Zerr', lx)):
        c2 = M.Sector(label, R.control_schedule('C2'), dual)
        if not M.c2_repair_certificate(c2)['ok']:
            fail('C2 repair control failed: ' + label)
    neg = json.loads((ROOT / 'outputs/round62_negative_controls.json').read_text())
    if not neg['all_negative_controls_pass']:
        fail('round62 negative controls failed')
    return 3


def verify_pattern_frontier():
    obj = json.loads((ROOT / 'outputs/pattern_cegar10_frontier.json').read_text())
    rows = obj['new_distinct_support_clauses_by_iteration']
    if len(rows) != 10:
        fail('pattern CEGAR iteration count mismatch')
    sx = sum(x['Xerr'] for x in rows)
    sz = sum(x['Zerr'] for x in rows)
    if (sx, sz, sx + sz) != (8159, 7715, 15874):
        fail('pattern CEGAR aggregate mismatch')
    if obj['totals']['raw_positive_witnesses_replayed_before_insertion'] != 15874:
        fail('pattern raw-replay count mismatch')
    if obj['backend']['proof_producing'] or obj['status'] != 'BOUNDED_POSITIVE_FRONTIER_ONLY':
        fail('pattern evidence level mismatch')
    return {'iterations': 10, 'Xerr': sx, 'Zerr': sz, 'clauses': sx + sz}


def verify_static_summary(px, pz, full):
    expected = json.loads((ROOT / 'outputs/global_single_clauses.json').read_text())
    totals = expected['totals']
    if totals != {'atom_deletion_controls': 7200, 'generalized_clauses': 1440,
                  'order_cases_checked': 103680, 'raw_exact_suffix_patterns': 1440}:
        fail('static summary totals mismatch')
    expected_hashes = [(x['clauses_sha256'], x['deletion_controls_sha256'])
                       for x in expected['sectors']]
    if expected_hashes != [
        ('b5c8562739038ab16273cece9f5048430bd106419f96cdcbaf116ca01fb483f8',
         'e7f0a6769516c43d2bfa9ccc11347a4762ba7e0c105e8ad7ffa1868107d63b1b'),
        ('9290efb7781f3f044723f9b41b99088e1bd5892a01006ce97486e0f482c63d65',
         '687a760c7c9c776d3be0ec96e9017bdff3ab143112ae8a33b821341fb714a361')]:
        fail('static certificate hashes mismatch')
    if full:
        actual = build_global_single_summary(px, pz)
        for sector, exp in zip(actual['sectors'], expected['sectors']):
            if sector != exp:
                fail('full static replay mismatch: ' + sector['sector'])
        if actual['totals'] != totals:
            fail('full static replay totals mismatch')
    return {'clauses': 1440, 'order_cases': 103680,
            'atom_deletion_controls': 7200, 'full_replay': full}


def verify_proof_and_process_ledgers():
    proof = json.loads((ROOT / 'outputs/proof_backend_frontier.json').read_text())
    if proof['checked_drup_drat_lrat_proofs'] != 0 or proof['absence_unsat_claims'] != 0:
        fail('proof frontier must record zero')
    if any(x['status'] != 'ERROR' or x['verdict_use'] != 'none'
           for x in proof['direct_360_attempts']):
        fail('interrupted proof attempt was promoted')
    proc = json.loads((ROOT / 'process_accounting.json').read_text())
    if proc['background_or_detached_processes_started'] or proc['handoff_compute']:
        fail('process cleanliness mismatch')
    return {'checked_proofs': 0, 'absence_unsat_claims': 0,
            'background_processes': 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--full-static', action='store_true',
                    help='regenerate all 1,440 clauses and 7,200 deletion controls')
    ap.add_argument('--repo-root', type=Path,
                    help='also check live governing-file hashes')
    args = ap.parse_args()
    manifest = verify_manifest()
    px, pz, lx, lz = pools()
    result = {
        'status': 'PASS',
        'manifest_entries_verified': manifest,
        'live_bindings_verified': verify_bindings(args.repo_root),
        'round62': verify_round62(lx, lz),
        'named_controls_rebuilt': verify_controls(lx, lz),
        'static_single': verify_static_summary(px, pz, args.full_static),
        'pattern_cegar': verify_pattern_frontier(),
        'proof_and_process': verify_proof_and_process_ledgers(),
        'exact_residual': [11, 12],
        'verdict': 'NOT_CLOSED',
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
