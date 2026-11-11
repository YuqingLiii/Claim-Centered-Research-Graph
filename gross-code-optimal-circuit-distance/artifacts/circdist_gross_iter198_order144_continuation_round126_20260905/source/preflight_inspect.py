#!/usr/bin/env python3
import datetime as dt
import hashlib
import json
import os
import pathlib
import sys
import traceback

SCRATCH = pathlib.Path('/private/tmp/circdist-round122-proposer')
LEDGER = SCRATCH / 'process-ledger-preflight.jsonl'


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
        fh.flush()
        os.fsync(fh.fileno())


def main():
    root = pathlib.Path('<repo>')
    requested = [
        root / 'DAG_PROTOCOL.md',
        root / 'FILE_PROTOCOL.md',
        root / 'circdist/README.md',
        root / 'operations/circdist/SCHEDULER.yaml',
        root / 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml',
        root / 'circdist/reviews/circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md',
    ]
    package = root / 'circdist/artifacts/circdist_gross_iter195_order144_continuation_round120_20260904'
    for path in requested:
        print(f'===== FILE {path.relative_to(root)} size={path.stat().st_size} sha256={sha256(path)} =====')
        print(path.read_text(encoding='utf-8', errors='replace'))
    print(f'===== PACKAGE {package.relative_to(root)} =====')
    for path in sorted(p for p in package.rglob('*') if p.is_file()):
        rel = path.relative_to(package)
        print(f'{rel}\t{path.stat().st_size}\t{sha256(path)}')


if __name__ == '__main__':
    start = now()
    base = {
        'kind': 'exec-self',
        'pid': os.getpid(),
        'ppid': os.getppid(),
        'argv': sys.argv,
        'cwd': os.getcwd(),
        'start_utc': start,
    }
    append({**base, 'event': 'start'})
    code = 0
    try:
        main()
    except BaseException:
        code = 1
        traceback.print_exc()
    append({**base, 'event': 'end', 'end_utc': now(), 'returncode': code, 'reaped': True})
    raise SystemExit(code)
