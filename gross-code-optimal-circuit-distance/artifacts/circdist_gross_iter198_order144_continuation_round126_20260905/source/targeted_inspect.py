#!/usr/bin/env python3
import datetime as dt
import hashlib
import json
import os
import pathlib
import sys
import traceback

ROOT = pathlib.Path('<repo>')
PKG = ROOT / 'circdist/artifacts/circdist_gross_iter195_order144_continuation_round120_20260904'
SCRATCH = pathlib.Path('/private/tmp/circdist-round122-proposer')
LEDGER = SCRATCH / 'process-ledger-preflight.jsonl'
OUT = SCRATCH / 'targeted-inspection.txt'


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def append(obj):
    with LEDGER.open('a', encoding='utf-8') as fh:
        fh.write(json.dumps(obj, sort_keys=True) + '\n')
        fh.flush(); os.fsync(fh.fileno())


def emit(fh, path, max_bytes=2_000_000):
    if not path.exists():
        fh.write(f'===== MISSING {path}\n')
        return
    fh.write(f'===== {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path} size={path.stat().st_size} sha256={sha256(path)} =====\n')
    if path.stat().st_size <= max_bytes:
        fh.write(path.read_text(encoding='utf-8', errors='replace'))
        if not path.read_bytes().endswith(b'\n'):
            fh.write('\n')
    else:
        fh.write('[content omitted: larger than inspection threshold]\n')


def main():
    chosen_rel = [
        'README.md', 'REPORT.md', 'VERDICT.md', 'manifest.json', 'MANIFEST.json',
        'MANIFEST.sha256', 'ROOT_MANIFEST.sha256', 'PAYLOAD_MANIFEST.sha256',
        'INVENTORY_MANIFEST.sha256', 'root-manifest.json', 'payload-manifest.json',
        'inventory-manifest.json', 'metadata.json',
        'verification/initial_unstarted.json',
        'verification/order144_quotient_check.json',
        'verification/preseal_replay/iter196.unstarted.json',
        'verification/preseal_replay/iter196.order144.json',
        'verification/preseal_replay/generated/state.json',
        'verification/preseal_replay/summary.json',
        'evidence/iteration196_unstarted_audit.json',
        'evidence/order144_quotient_cnf_audit_iter196.json',
        'process/process-ledger.jsonl', 'process/process_ledger.jsonl',
        'source/serial_exec_round120.py', 'source/run_outer_solver_round120.py',
        'source/replay_package_round120.py', 'replay.py', 'replay.sh',
    ]
    with OUT.open('w', encoding='utf-8') as fh:
        for path in [
            ROOT/'DAG_PROTOCOL.md', ROOT/'FILE_PROTOCOL.md', ROOT/'circdist/README.md',
            ROOT/'operations/circdist/SCHEDULER.yaml',
            ROOT/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml',
            ROOT/'circdist/reviews/circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md',
        ]:
            emit(fh, path)
        fh.write('===== PACKAGE TOP LEVEL =====\n')
        for p in sorted(PKG.iterdir()):
            fh.write(f'{p.name}\t{"dir" if p.is_dir() else p.stat().st_size}\t{sha256(p) if p.is_file() else "-"}\n')
        fh.write('===== MATCHED PACKAGE PATHS =====\n')
        needles = ('iter196', 'iteration196', 'order144', 'manifest', 'replay', 'solver', 'ledger', 'unstarted', 'quotient')
        for p in sorted(q for q in PKG.rglob('*') if q.is_file()):
            rel = str(p.relative_to(PKG))
            if any(n in rel.lower() for n in needles):
                fh.write(f'{rel}\t{p.stat().st_size}\t{sha256(p)}\n')
        for rel in chosen_rel:
            emit(fh, PKG/rel)
    print(f'wrote {OUT} size={OUT.stat().st_size} sha256={sha256(OUT)}')


if __name__ == '__main__':
    base = {'kind':'exec-self','pid':os.getpid(),'ppid':os.getppid(),'argv':sys.argv,'cwd':os.getcwd(),'start_utc':now()}
    append({**base,'event':'start'})
    code = 0
    try: main()
    except BaseException:
        code = 1; traceback.print_exc()
    append({**base,'event':'end','end_utc':now(),'returncode':code,'reaped':True})
    raise SystemExit(code)
