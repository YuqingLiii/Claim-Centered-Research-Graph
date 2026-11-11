#!/usr/bin/env python3
"""Deterministic negative controls for schedule, witness, and CEGAR replay.

Every corruption is made after constructing a known-good object.  The output is
machine-readable and the program exits nonzero unless every corruption is
rejected by the corresponding raw verifier.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import model as M
import run as R


def load(args):
    px = M.expand_pool(args.w12x, M.HX, M.HZ)
    pz = M.expand_pool(args.w12z, M.HZ, M.HX)
    lx = M.logical_basis(px, M.HX)
    lz = M.logical_basis(pz, M.HZ)
    return px, pz, lx, lz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--w12x', required=True)
    ap.add_argument('--w12z', required=True)
    ap.add_argument('--cegar', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    px, pz, lx, lz = load(args)
    results = {}

    # Schedule corruption 1: force two gates sharing data q to the same time.
    good = R.control_schedule('C1')
    q_edges = [e for e in M.ALL_EDGES if M.edge_tuple(e)[2] == 0]
    bad = dict(good)
    bad[q_edges[1]] = bad[q_edges[0]]
    a = M.audit_schedule(bad)
    results['shared_qubit_collision'] = {
        'detected': not a['ok'] and len(a['conflicts']) > 0,
        'changed_edge': q_edges[1], 'source_edge': q_edges[0],
        'conflict_count': len(a['conflicts']), 'audit_ok': a['ok']}

    # Schedule corruption 2: on the globally serial candidate, swap the first
    # overlap's Z edge with its same-data X edge. Global timestamp uniqueness is
    # preserved, so conflicts remain impossible, while exactly one side of that
    # overlap's MC comparison changes truth value.
    serial = R.control_schedule('published')
    a0, b0, shared = M.OVERLAPS[0]
    q0 = shared[0]
    e, f = M.edge_key('Z', b0, q0), M.edge_key('X', a0, q0)
    trial = dict(serial)
    trial[e], trial[f] = trial[f], trial[e]
    aa = M.audit_schedule(trial)
    results['mc_only_timestamp_swap'] = {
        'detected': not aa['ok'] and not aa['conflicts'] and len(aa['mc_violations']) > 0,
        'swapped_edges': [e, f], 'conflict_count': len(aa['conflicts']),
        'mc_violation_count': len(aa['mc_violations']),
        'first_mc_violation': aa['mc_violations'][0] if aa['mc_violations'] else None,
        'audit_ok': aa['ok']}

    # Effective witness corruption: introduce a duplicate direct column.
    c1 = M.Sector('Zerr', good, lx)
    cert = M.c1_named_certificate(c1)
    dup = list(cert['selected'])
    dup[-1] = dup[0]
    rejected = c1.verify_effective_selection(dup, 10)
    results['duplicate_direct_column'] = {
        'detected': not rejected['ok'] and 'distinct' in rejected.get('error', ''),
        'original_ok': cert['ok'], 'corrupted_result': rejected}

    # Repair corruption: change the rigid hook voltage to a value outside U.
    c2t = R.control_schedule('C2')
    c2 = M.Sector('Xerr', c2t, lz)
    cert2 = M.c2_repair_certificate(c2)
    choices = [dict(x) for x in cert2['choices']]
    hook = c2.columns[choices[0]['column']]
    invalid_u = choices[0]['u'] ^ 1
    while invalid_u in hook.u_options:
        invalid_u ^= 2
    choices[0]['u'] = invalid_u
    rejected2 = c2.verify_repair_trace(choices, 10)
    results['invalid_repair_voltage'] = {
        'detected': not rejected2['ok'] and 'voltage not in U' in rejected2.get('error', ''),
        'original_ok': cert2['ok'], 'corrupted_result': rejected2}

    # CEGAR soundness/rejection control: every persisted witness and block is
    # replayed from raw schedule times. The witness must verify, its preserving
    # conjunction must hold on the originating schedule, and reversing one atom
    # by swapping its two timestamps must falsify that conjunction.
    ledger = json.loads(Path(args.cegar).read_text())['ledger']
    replay = []
    for step in ledger:
        times = step['schedule']
        label = step['block']['sector']
        sec = M.Sector(label, times, lz if label == 'Xerr' else lx)
        witness = step['effective'][label]['witness']
        raw = sec.verify_effective_selection(witness['selected'], 10)
        atoms = step['block']['atoms']
        holds = M.block_holds(times, atoms)
        mutated = dict(times)
        ea, _, eb = atoms[0]
        mutated[ea], mutated[eb] = mutated[eb], mutated[ea]
        fails_after_swap = not M.block_holds(mutated, atoms)
        replay.append({'iteration': step['iteration'], 'raw_witness_ok': raw['ok'],
                       'block_holds_on_source': holds,
                       'block_fails_after_endpoint_swap': fails_after_swap})
    results['cegar_trace_replay'] = {
        'detected': bool(replay) and all(x['raw_witness_ok'] and
                                        x['block_holds_on_source'] and
                                        x['block_fails_after_endpoint_swap'] for x in replay),
        'iterations': replay}

    ok = all(v.get('detected') is True for v in results.values())
    out = {'all_negative_controls_pass': ok, 'controls': results}
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
