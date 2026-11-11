#!/usr/bin/env python3
"""Bind the external post-payload replay into excluded final metadata before root sealing."""
from pathlib import Path
import argparse, hashlib, json, shutil

def scan(p):
 h=hashlib.sha256(); size=lf=0
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b); size+=len(b); lf+=b.count(b'\n')
 return h.hexdigest(),size,lf
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--replay',type=Path,required=True); a=ap.parse_args(); r=a.root.resolve(); p=a.replay.resolve(); x=json.loads(p.read_text())
assert x['status']=='PASS' and x['direct_child_count']==18 and x['strict_serial'] and x['strict_child_nonoverlap'] and x['all_children_reaped'] and x['detached_processes']==0
assert all(c['returncode']==0 and c['reaped'] and not c['timed_out'] and not c['detached'] for c in x['children'])
shutil.copyfile(p,r/'verification/postseal_replay.json'); digest,size,lf=scan(p)
res=json.loads((r/'RESULT.json').read_text()); res['verification']['postpayload_package_replay']='PASS'; res['verification']['postpayload_replay_children']=18; res['postpayload_replay_binding']={'external_record':str(p),'sha256':digest,'bytes':size,'lf':lf,'strict_child_nonoverlap':True,'all_children_reaped':True}; (r/'RESULT.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','replay_sha256':digest,'bytes':size,'lf':lf,'children':18},sort_keys=True))
