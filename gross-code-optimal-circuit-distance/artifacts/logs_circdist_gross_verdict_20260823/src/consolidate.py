#!/usr/bin/env python3
"""consolidate.py -- gather every record THIS box produced into one jsonl, so the accounting
and manifest scripts (which scan *.jsonl) see them.  job7k writes its record as the last line of
stdout, but a worker that had to build the pool cache prints a preamble first, so a plain
json.load() would fail; harvest.read_rec takes the last parseable JSON line."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import harvest
recs = harvest.collect()
out = os.path.join(HERE, 'logs', 'verdictbox.jsonl')
n = 0
with open(out, 'w') as f:
    for r in sorted(recs, key=lambda r: (r['sector'], r['K'], r['Ew'], r['orbit'])):
        r = {k: v for k, v in r.items() if k != '_src'}
        f.write(json.dumps(r) + "\n")
        n += 1
print("wrote %s with %d records" % (out, n))
