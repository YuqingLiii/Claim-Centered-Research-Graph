#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,shutil

def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha(o):return hashlib.sha256(canon(o)).hexdigest()
def load(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def writegz(p,o):Path(p).write_bytes(gzip.compress((json.dumps(o,indent=2,sort_keys=True)+'\n').encode(),compresslevel=9,mtime=0))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-in',type=Path,required=True);ap.add_argument('--state-in',type=Path,required=True);ap.add_argument('--synthesis',type=Path,required=True);ap.add_argument('--source-out',type=Path,required=True);ap.add_argument('--state-out',type=Path,required=True);ap.add_argument('--record-out',type=Path,required=True);a=ap.parse_args()
 s=load(a.source_in);st=load(a.state_in);syn=load(a.synthesis);assert len(s['selectors'])==st['selector_count']==164 and syn['retained_ordinary_selector_count']==44 and syn['retained_relaxed_cube_count']==0
 oldhash=s.pop('semantic_payload_sha256');new=[]
 compact_keys=('mechanism_id','source_iteration','sector','fault_count','selected_names','data_support','group_kinds','source_schedule_sha256','origin','selector_semantic_sha256')
 for x in syn['retained_ordinary_selectors']:
  y={k:x[k] for k in compact_keys};new.append(y)
 assert len({x['selector_semantic_sha256'] for x in s['selectors']+new})==208
 s['selectors']+=new
 syn_sha=hashlib.sha256(a.synthesis.read_bytes()).hexdigest()
 s['bindings']['round92_weight9_synthesis_file_sha256']=syn_sha
 s['bindings']['round92_preouter_parent_semantic_sha256']=oldhash
 s['expected']['selectors']=len(s['selectors']);s['expected']['assertions']=18882+len(s['selectors'])
 res=[set(x) for x in s['residual_positions']]
 def pos(ks):
  z=set()
  for k in ks:z.symmetric_difference_update(res[int(k)])
  return tuple(sorted(z))
 mem=set();ranks=set()
 for x in s['selectors']:
  sd=s['sector_definitions'][x['sector']]
  for cs,ks in x['group_kinds'].items():
   c=int(cs);p=pos(ks)
   for q in sd['checks'][c]:
    mem.add((x['sector'],c,p,q))
    if p and p!=tuple(range(6)):ranks.add((x['sector'],c,q))
 s['expected']['membership_expressions']=len(mem);s['expected']['rank_expressions']=len(ranks)
 s['semantic_payload_sha256']=sha(s)
 # Full state entries retain auditable domain proof and witness fields.
 state_new=[]
 for x in syn['retained_ordinary_selectors']:
  y=dict(x);y['preouter_installation']='round92-weight9-slack-synthesis';state_new.append(y)
 selectors=st['selectors']+state_new
 keys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
 state_hash=sha([{k:x.get(k) for k in keys} for x in selectors])
 out=dict(st);out.update({'schema':'round92-proof-outer-continuation-state-v1','parent_selector_count':164,'parent_selector_state_sha256':st['selector_state_sha256'],'preouter_selector_count':44,'selector_count':208,'selector_state_sha256':state_hash,'next_iteration':124,'started':False,'stop':None,'selectors':selectors,'preouter_synthesis_file_sha256':syn_sha,'preouter_atomic_commit':True})
 rec={'schema':'round92-preouter-atomic-install-v1','status':'PASS','iteration':124,'parent_selector_count':164,'parent_selector_state_sha256':st['selector_state_sha256'],'parent_source_semantic_sha256':oldhash,'synthesis_file_sha256':syn_sha,'retained_terms':44,'retained_relaxed_cubes':0,'new_selector_ids':[x['mechanism_id'] for x in new],'new_selector_semantic_sha256':[x['selector_semantic_sha256'] for x in new],'state_after_sha256':state_hash,'source_after_semantic_sha256':s['semantic_payload_sha256'],'atomic':True}
 for p in (a.source_out,a.state_out,a.record_out):p.parent.mkdir(parents=True,exist_ok=True)
 writegz(a.source_out,s);a.state_out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');a.record_out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
 print(json.dumps(rec,sort_keys=True))
if __name__=='__main__':main()
