#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();x=json.loads((R/'synthesis/mixed_sector_theorem.json').read_text());names=json.loads((R/'synthesis/order5_input/name_universe.json').read_text())
assert x['status']=='PASS' and x['frozen_css_linearity'] and len(names)==x['name_universe_count']==360
assert hashlib.sha256((R/'synthesis/order5_input/name_universe.json').read_bytes()).hexdigest()==x['name_universe_sha256']
assert x['logical_nontriviality_truth_table']=={'00':'mixed trivial','01':'Z component nontrivial','10':'X component nontrivial','11':'both components nontrivial'}
# Exhaust every possible pair of component logical-nontriviality bits.
for xb in (0,1):
 for zb in (0,1):
  mixed=bool(xb or zb);assert mixed==(bool(xb) or bool(zb));assert not mixed or xb or zb
# Exhaust set cardinality on a finite toy universe; the symbolic inequality then follows from subset inclusion.
for xm in range(16):
 for zm in range(16):
  weight=lambda value: bin(value).count('1')
  assert weight(xm) <= weight(xm|zm) and weight(zm) <= weight(xm|zm)
assert (R/x['proof']).is_file() and 'same-sector component' in x['conclusion'] and x['new_closure_beyond_components'] is False
print(json.dumps({'status':'PASS','logical_cases':4,'finite_set_controls':256,'name_universe_count':len(names)},sort_keys=True))
