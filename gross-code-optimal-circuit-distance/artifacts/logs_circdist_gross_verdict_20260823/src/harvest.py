#!/usr/bin/env python3
"""harvest.py -- read this box's own per-job outputs robustly.

job7k.py writes its record as the LAST line of stdout, but a worker that had to build the
weight-12 pool cache also prints a 'pools built in ...' preamble, so the file is not pure JSON.
Take the last parseable JSON line.
"""
import os, sys, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(HERE, 'logs')

OPEN8 = [('Z', 5, 18, 0), ('Z', 6, 18, 0), ('Z', 7, 18, 0), ('Z', 7, 20, 0), ('Z', 9, 22, 0),
         ('X', 5, 18, 0), ('X', 6, 18, 0), ('X', 7, 20, 0)]


def read_rec(path):
    if not os.path.exists(path):
        return None
    out = None
    for ln in open(path):
        ln = ln.strip()
        if not ln.startswith('{'):
            continue
        try:
            out = json.loads(ln)
        except Exception:
            pass
    return out


def collect():
    """every record this box produced, from single-json files and from jsonl files."""
    recs = []
    for p in sorted(glob.glob(os.path.join(LOGS, '*.json'))):
        b = os.path.basename(p)
        if not (b.startswith('h_') or b.startswith('audit_') or b.startswith('overprune')):
            continue
        r = read_rec(p)
        if r:
            r['_src'] = b
            recs.append(r)
    for p in sorted(glob.glob(os.path.join(LOGS, 'spot_*.jsonl'))):
        for ln in open(p):
            ln = ln.strip()
            if ln.startswith('{'):
                try:
                    r = json.loads(ln)
                    r['_src'] = os.path.basename(p)
                    recs.append(r)
                except Exception:
                    pass
    return recs


if __name__ == '__main__':
    recs = collect()
    done = {(r['sector'], r['K'], r['Ew'], r['orbit']): r
            for r in recs if r.get('verdict') in ('SAT', 'UNSAT')}
    print("THE 8 OPEN SUB-QUERIES")
    print("-" * 92)
    nd = 0
    for k in OPEN8:
        r = done.get(k)
        if r:
            nd += 1
            print("  %s (%d,%2d) orbit %d   **%s**  %8.1f s  %-7s  %s  [%s]"
                  % (k[0], k[1], k[2], k[3], r['verdict'], r['seconds'], r.get('solver'),
                     r['cnf_sha256'], r.get('_src')))
        else:
            print("  %s (%d,%2d) orbit %d   ... still running" % k)
    print("-" * 92)
    print("  decided %d / 8    SAT: %d" % (nd, sum(1 for k in OPEN8 if done.get(k, {}).get('verdict') == 'SAT')))
    print()
    print("OTHER RECORDS THIS BOX PRODUCED")
    print("-" * 92)
    for r in recs:
        k = (r['sector'], r['K'], r['Ew'], r['orbit'])
        if k in OPEN8 and r['_src'].startswith('h_'):
            continue
        print("  %s %-12s (%d,%2d) orbit %-3d %-6s %8.1f s  %-7s %s  [%s]"
              % (r['sector'], str(tuple(r['triple'])), r['K'], r['Ew'], r['orbit'],
                 r['verdict'], r.get('seconds', -1), r.get('solver'), r['cnf_sha256'], r['_src']))
