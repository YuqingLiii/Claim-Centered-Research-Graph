#!/usr/bin/env python3
"""Read-only replay validator for the sealed round-62 package."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
import model as M
import run as R


def sha_bytes(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(msg):
    raise AssertionError(msg)


def main():
    # The manifest intentionally excludes itself.
    manifest = {}
    for line in (ROOT / 'SHA256SUMS.txt').read_text().splitlines():
        digest, rel = line.split('  ', 1)
        manifest[rel] = digest
        p = ROOT / rel
        if not p.is_file() or sha_bytes(p) != digest:
            fail('manifest mismatch: ' + rel)

    px = M.expand_pool(ROOT / 'inputs/w12X.txt', M.HX, M.HZ)
    pz = M.expand_pool(ROOT / 'inputs/w12Z.txt', M.HZ, M.HX)
    lx = M.logical_basis(px, M.HX)
    lz = M.logical_basis(pz, M.HZ)
    if len(px) != 1884 or len(pz) != 1884 or len(lx) != 12 or len(lz) != 12:
        fail('frozen-pool reconstruction mismatch')

    ledger = json.loads((ROOT / 'outputs/cegar20.json').read_text())['ledger']
    prior_blocks = []
    schedules = set()
    traces = set()
    for i, step in enumerate(ledger):
        if step['iteration'] != i or step['outer']['status'] != 'SAT':
            fail(f'outer status/iteration mismatch at {i}')
        times = step['schedule']
        if R.sha_obj(times) != step['schedule_sha256']:
            fail(f'schedule digest mismatch at {i}')
        audit = M.audit_schedule(times, True)
        if not audit['ok'] or not audit['global_interleaved']:
            fail(f'raw schedule rejected at {i}')
        if any(M.block_holds(times, atoms) for atoms in prior_blocks):
            fail(f'outer schedule violates a prior CEGAR block at {i}')
        block = step['block']
        label = block['sector']
        sec = M.Sector(label, times, lz if label == 'Xerr' else lx)
        witness = step['effective'][label]['witness']
        replay = sec.verify_effective_selection(witness['selected'], 10)
        if not replay['ok'] or replay['net_support'] != witness['net_support']:
            fail(f'effective witness rejected at {i}')
        if not M.block_holds(times, block['atoms']):
            fail(f'block does not preserve source witness at {i}')
        trace = {'type': 'effective', 'sector': label,
                 'schedule_sha256': step['schedule_sha256'],
                 'witness': witness, 'atoms': block['atoms']}
        if R.sha_obj(trace) != block['trace_sha256']:
            fail(f'trace digest mismatch at {i}')
        prior_blocks.append(block['atoms'])
        schedules.add(step['schedule_sha256'])
        traces.add(block['trace_sha256'])

    # Rebuild decisive named controls rather than trusting their JSON flags.
    c1 = M.Sector('Zerr', R.control_schedule('C1'), lx)
    if not M.c1_named_certificate(c1)['ok']:
        fail('C1 normalized direct-360 control failed')
    for label, dual in (('Xerr', lz), ('Zerr', lx)):
        c2 = M.Sector(label, R.control_schedule('C2'), dual)
        if not M.c2_repair_certificate(c2)['ok']:
            fail('C2 repair-zero control failed in ' + label)

    neg = json.loads((ROOT / 'outputs/negative_controls.json').read_text())
    if not neg['all_negative_controls_pass']:
        fail('persisted negative controls did not pass')

    result = {
        'status': 'PASS',
        'manifest_entries_verified': len(manifest),
        'cegar_iterations_replayed': len(ledger),
        'unique_schedules': len(schedules),
        'unique_counterexample_traces': len(traces),
        'prior_block_exclusions_checked': len(ledger) * (len(ledger) - 1) // 2,
        'frozen_pool_sizes': {'X': len(px), 'Z': len(pz)},
        'named_controls_rebuilt': ['C1/Zerr effective', 'C2/Xerr repair0', 'C2/Zerr repair0'],
        'negative_controls_pass': True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
