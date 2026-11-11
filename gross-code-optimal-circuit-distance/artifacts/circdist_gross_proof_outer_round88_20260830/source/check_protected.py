#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True);ap.add_argument('--repository',type=Path);a=ap.parse_args();P=a.package.resolve();B=json.loads((P/'INPUT_BINDINGS.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
for rel,copy in B['canonical_snapshot_copies'].items():
 expected=B['expected_protected_sha256'][rel];assert sha(P/copy)==expected,(copy,sha(P/copy),expected)
assert sha(P/'bindings/round86/SHA256SUMS.txt')==B['round86_root_manifest_sha256']
assert sha(P/'bindings/round86/PAYLOAD_SHA256SUMS.txt')==B['round86_payload_manifest_sha256']
if a.repository:
 R=a.repository.resolve()
 for rel,expected in B['expected_protected_sha256'].items():assert sha(R/rel)==expected,(rel,sha(R/rel),expected)
 print('PROTECTED_REPOSITORY_PASS',len(B['expected_protected_sha256']))
else:print('PROTECTED_SNAPSHOTS_PASS')
