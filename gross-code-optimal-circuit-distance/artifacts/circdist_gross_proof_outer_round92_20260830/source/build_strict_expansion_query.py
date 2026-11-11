#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--cnf',type=Path,required=True);ap.add_argument('--map',type=Path,required=True);ap.add_argument('--old-count',type=int,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--summary',type=Path,required=True);a=ap.parse_args()
rows=[json.loads(x) for x in a.map.read_text().splitlines()];new=[x for x in rows if x.get('family')=='efssc_exclusion' and x['selector_index']>=a.old_count]
assert len(new)==44 and [x['selector_index'] for x in new]==list(range(164,208))
remove={x['root_clause_ids'][0] for x in new};vars=[-x['root_clauses'][0][0] for x in new];assert all(v>0 for v in vars)
with a.cnf.open() as f:
 h=f.readline().split();assert h[:2]==['p','cnf'];nv,nc=map(int,h[2:]);clauses=[]
 for i,line in enumerate(f,1):
  if i not in remove:clauses.append(line)
assert len(clauses)==nc-len(remove)
a.output.parent.mkdir(parents=True,exist_ok=True)
with a.output.open('w') as f:
 f.write(f'p cnf {nv} {len(clauses)+1}\n');f.writelines(clauses);f.write(' '.join(map(str,vars))+' 0\n')
b=a.output.read_bytes();summary={'schema':'round92-strict-old-union-expansion-query-v1','status':'BUILT','semantics':'exact frozen iter124 base constraints and old 164 EFSSC exclusions, with definitions for 44 proposed selectors and one disjunction requiring at least one proposed selector valid','variables':nv,'clauses':len(clauses)+1,'removed_new_negative_root_clause_ids':sorted(remove),'new_validity_variables':vars,'new_union_clause':vars,'cnf_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'lines':b.count(b'\n')}
a.summary.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
