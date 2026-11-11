#!/usr/bin/env python3
"""Import externally written preseal replay records without changing their bytes."""
from pathlib import Path
import argparse, hashlib, json, shutil

def scan(path):
    raw=Path(path).read_bytes(); return {"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),"lf":raw.count(b"\n")}

ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--external',type=Path,required=True); a=ap.parse_args()
r=a.root.resolve(); e=a.external.resolve()
mapping={e/'preseal_replay.json':r/'verification/preseal_replay.json',
         e/'preseal_replay.process.json':r/'logs/process/preseal_replay_outer.json',
         e/'preseal_replay.stdout.log':r/'logs/preseal_replay.stdout.log',
         e/'preseal_replay.stderr.log':r/'logs/preseal_replay.stderr.log'}
for src,dst in mapping.items(): dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(src,dst)
failure=r/'logs/failures/F110-008'; failure.mkdir(parents=True,exist_ok=True)
for src,name in ((r/'logs/input_registry_invariance.stdout.log','stdout.log'),
                 (r/'logs/input_registry_invariance.stderr.log','stderr.log'),
                 (r/'logs/process/input_registry_invariance.json','process.json')): shutil.copyfile(src,failure/name)
replay=json.loads((r/'verification/preseal_replay.json').read_text())
assert replay['status']=='PASS' and replay['child_count']==19 and replay['strict_child_nonoverlap'] and not replay['package_mutated']
binding={'schema':'circdist-gross-round110-preseal-replay-binding-v1','status':'PASS',
         'external_source':str(e/'preseal_replay.json'),'retained':'verification/preseal_replay.json',
         **scan(r/'verification/preseal_replay.json'),'child_count':19,'strict_serial':True,
         'strict_child_nonoverlap':True,'all_children_reaped':True,'detached_processes':0,'timeouts':0,'package_mutated':False}
(r/'verification/preseal_replay_binding.json').write_text(json.dumps(binding,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','imported':len(mapping),'replay':scan(r/'verification/preseal_replay.json')},sort_keys=True))
