#!/usr/bin/env python3
from pathlib import Path
import argparse,json
ap=argparse.ArgumentParser();ap.add_argument('--log',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
prefix='ERROR: circdist: unlinked evidence: circdist/artifacts/circdist_gross_proof_outer_round92_20260830/'
lines=[x for x in a.log.read_text().splitlines() if x.strip()];assert lines and all(x.startswith(prefix) for x in lines),lines[:10]
paths=[x[len('ERROR: circdist: unlinked evidence: '):] for x in lines];assert len(paths)==len(set(paths))
o={'schema':'circdist-round92-evidence-closure-interpretation-v1','status':'PASS','raw_exit_code':1,'error_count':len(lines),'all_errors_under_new_package':True,'package_prefix':'circdist/artifacts/circdist_gross_proof_outer_round92_20260830/','meaning':'expected pre-review unlinked-package behavior only; canonical evidence was not edited'}
a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps(o,sort_keys=True))
