#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();o=json.loads((R/'verification/compression.json').read_text())
for x in o['rows']:
 p=R/x['stored_path'];b=p.read_bytes();raw=gzip.decompress(b)
 assert hashlib.sha256(b).hexdigest()==x['stored_sha256'] and len(b)==x['stored_bytes']
 assert hashlib.sha256(raw).hexdigest()==x['content_sha256'] and len(raw)==x['content_bytes'] and raw.count(b'\n')==x['content_lf']
 assert not (R/x['source_path']).exists()
assert len(o['rows'])==o['files_compressed'] and sum(x['content_bytes'] for x in o['rows'])==o['content_bytes'] and sum(x['stored_bytes'] for x in o['rows'])==o['stored_bytes']
print(json.dumps({'status':'PASS','files_checked':len(o['rows']),'content_bytes':o['content_bytes'],'stored_bytes':o['stored_bytes']},sort_keys=True))
