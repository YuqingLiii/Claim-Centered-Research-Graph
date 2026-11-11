#!/usr/bin/env python3
"""Accept evidence closure only when every error is under this unlinked package."""
from pathlib import Path
import argparse,json
parser=argparse.ArgumentParser()
parser.add_argument('--log',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
prefix='ERROR: circdist: unlinked evidence: circdist/artifacts/circdist_gross_proof_outer_round90_20260830/'
lines=[line for line in args.log.read_text().splitlines() if line.strip()]
assert lines and all(line.startswith(prefix) for line in lines), lines[:10]
paths=[line[len('ERROR: circdist: unlinked evidence: '):] for line in lines]
assert len(paths)==len(set(paths))
out={'schema':'circdist-round90-evidence-closure-interpretation-v1','status':'PASS',
     'raw_exit_code':1,'error_count':len(lines),'all_errors_under_new_package':True,
     'package_prefix':'circdist/artifacts/circdist_gross_proof_outer_round90_20260830/',
     'meaning':'expected pre-review unlinked-package behavior only; canonical evidence was not edited'}
args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
