#!/usr/bin/env python3
"""Heavy deterministic replay of the bounded round-63 support-pattern CEGAR.

This is a positive-witness experiment, never an absence oracle.  The outer
scheduler is the exact unrestricted 864-edge/648-MC interleaved model.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import model as M
from outer import OuterScheduler


def words(value):
    return [value & ((1 << 64) - 1),
            (value >> 64) & ((1 << 64) - 1),
            (value >> 128) & ((1 << 64) - 1)]


def sha_obj(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def patterns(sec, pool):
    residuals = sec.columns[144:]
    supports = np.array([words(c.support) for c in residuals], dtype=np.uint64)
    pairs = np.array(list(itertools.combinations(range(len(residuals)), 2)), dtype=np.int16)
    pair_supports = supports[pairs[:, 0]] ^ supports[pairs[:, 1]]
    first_single = np.full(len(residuals), -1, dtype=np.int32)
    first_pair = np.full(len(pairs), -1, dtype=np.int32)
    for vi, logical in enumerate(pool):
        vw = np.array(words(logical), dtype=np.uint64)
        sw = np.bitwise_count(supports ^ vw).sum(axis=1)
        first_single[(first_single < 0) & (sw <= 9)] = vi
        pw = np.bitwise_count(pair_supports ^ vw).sum(axis=1)
        first_pair[(first_pair < 0) & (pw <= 8)] = vi
    out = {}
    for ri, vi in enumerate(first_single):
        if vi >= 0:
            c = residuals[ri]
            atoms = tuple(sorted(M.support_atoms(sec, c.index)))
            data = pool[int(vi)] ^ c.support
            selected = [c.index] + M.bits(data)
            witness = sec.verify_effective_selection(selected, 10)
            assert witness['ok']
            out.setdefault(atoms, witness)
    for pi, vi in enumerate(first_pair):
        if vi >= 0:
            c = residuals[int(pairs[pi, 0])]
            d = residuals[int(pairs[pi, 1])]
            atoms = tuple(sorted(set(M.support_atoms(sec, c.index) +
                                     M.support_atoms(sec, d.index))))
            data = pool[int(vi)] ^ c.support ^ d.support
            selected = [c.index, d.index] + M.bits(data)
            if len(selected) != len(set(selected)):
                continue
            witness = sec.verify_effective_selection(selected, 10)
            assert witness['ok']
            out.setdefault(atoms, witness)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--iterations', type=int, default=10)
    ap.add_argument('--timeout-ms', type=int, default=30000)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    px = M.expand_pool(ROOT / 'inputs/w12X.txt', M.HX, M.HZ)
    pz = M.expand_pool(ROOT / 'inputs/w12Z.txt', M.HZ, M.HX)
    lx = M.logical_basis(px, M.HX)
    lz = M.logical_basis(pz, M.HZ)
    outer = OuterScheduler(True)
    seen = set()
    ledger = []
    for iteration in range(args.iterations):
        started = time.time()
        solved = outer.solve(args.timeout_ms)
        row = {'iteration': iteration, 'outer': solved}
        if solved['status'] != 'SAT':
            ledger.append(row)
            break
        schedule = solved.pop('compressed_schedule')
        row['schedule'] = schedule
        row['schedule_sha256'] = sha_obj(schedule)
        row['sectors'] = {}
        for label, pool, dual in (('Xerr', px, lz), ('Zerr', pz, lx)):
            sec = M.Sector(label, schedule, dual)
            found = patterns(sec, pool)
            added = []
            for atoms, witness in found.items():
                if atoms in seen:
                    continue
                seen.add(atoms)
                outer.add_block(list(atoms), f'{iteration}-{label}')
                added.append({'atoms': atoms, 'witness': witness})
            row['sectors'][label] = {'patterns': len(found), 'new': len(added),
                                      'added': added}
        row['global_clause_count'] = len(seen)
        row['wall_seconds'] = time.time() - started
        ledger.append(row)
        if sum(v['new'] for v in row['sectors'].values()) == 0:
            break
    Path(args.output).write_text(json.dumps({'ledger': ledger}, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
