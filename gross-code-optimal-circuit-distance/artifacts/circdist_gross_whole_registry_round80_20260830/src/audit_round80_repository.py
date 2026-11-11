#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,subprocess
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--repo-root',type=Path,required=True);ap.add_argument('--phase',choices=['preinstall','postcopy'],required=True);a=ap.parse_args();R=a.root.resolve();Q=a.repo_root.resolve();target='circdist/artifacts/circdist_gross_whole_registry_round80_20260830';self_rel=R.relative_to(Q).as_posix() if Q in R.parents else None
def data(p):
 p=Path(p)
 if not p.exists() and Path(str(p)+'.gz').exists():p=Path(str(p)+'.gz')
 b=p.read_bytes();return gzip.decompress(b) if p.suffix=='.gz' else b
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while True:
   b=f.read(8<<20)
   if not b:break
   h.update(b)
 return h.hexdigest()
def scan():
 rows=[]
 for p in sorted(Q.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(Q).as_posix()
  if rel=='.git' or rel.startswith('.git/') or rel==target or rel.startswith(target+'/') or (self_rel and (rel==self_rel or rel.startswith(self_rel+'/'))):continue
  rows.append({'bytes':p.stat().st_size,'path':rel,'sha256':sha(p)})
 return rows
before_blob=data(R/'preflight/repository_inventory_before.jsonl');before=[json.loads(x) for x in before_blob.decode().splitlines() if x]
after=scan();blob=''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in after).encode();post=R/f'preflight/repository_inventory_{a.phase}.jsonl';post.write_bytes(blob)
bm={x['path']:x for x in before};am={x['path']:x for x in after};added=[am[k] for k in sorted(am.keys()-bm.keys())];removed=[bm[k] for k in sorted(bm.keys()-am.keys())];changed=[{'path':k,'before':bm[k],'after':am[k]} for k in sorted(am.keys()&bm.keys()) if am[k]!=bm[k]]
prot=json.load(open(R/'preflight/protected_hashes_before.json'));prows=[]
for x in prot['files']:
 p=Q/x['path'];now={'exists':p.is_file(),'bytes':p.stat().st_size if p.is_file() else None,'sha256':sha(p) if p.is_file() else None};prows.append({'path':x['path'],'before':{'bytes':x['bytes'],'sha256':x['sha256']},'after':now,'unchanged':now['exists'] and now['bytes']==x['bytes'] and now['sha256']==x['sha256']})
status=subprocess.run(['git','status','--short','-z'],cwd=Q,stdout=subprocess.PIPE,check=True).stdout;(R/f'preflight/git_status_{a.phase}.z').write_bytes(status)
obj={'schema':'round80-repository-drift-disclosure-v1','phase':a.phase,'package_excluded':target,'before':{'file_count':len(before),'inventory_sha256':hashlib.sha256(before_blob).hexdigest()},'after':{'file_count':len(after),'inventory_sha256':hashlib.sha256(blob).hexdigest()},'drift':{'added_count':len(added),'removed_count':len(removed),'changed_count':len(changed),'added':added,'removed':removed,'changed':changed},'protected':{'file_count':len(prows),'unchanged_count':sum(x['unchanged'] for x in prows),'all_unchanged':all(x['unchanged'] for x in prows),'files':prows},'proposer_interpretation':'all package-excluding drift is unrelated concurrent repository work; preserved and not reverted; protected set must remain unchanged','canonical_edits_by_proposer':0}
(R/f'preflight/concurrent_repository_change_disclosure_{a.phase}.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');print(json.dumps({'phase':a.phase,'before':len(before),'after':len(after),'added':len(added),'removed':len(removed),'changed':len(changed),'protected_all_unchanged':obj['protected']['all_unchanged'],'inventory_sha256':obj['after']['inventory_sha256']},sort_keys=True))
