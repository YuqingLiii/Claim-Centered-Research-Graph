#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'round63_src'));sys.path.insert(0,str(HERE))
import model as M
from outer import OuterScheduler
import round68_build as B
import round68_verify as V

def dump(path,obj):Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',required=True);ap.add_argument('--iterations',type=int,default=5);ap.add_argument('--output',required=True);a=ap.parse_args()
 root=Path(a.root);px,pz,lx,lz=B.load_context()
 rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz
 r62=json.loads((HERE/'round62_cegar20.json').read_text());B.replay_round62_blocks(r62,lx,lz)
 primary=json.loads((root/'verification.json').read_text())
 outer=OuterScheduler(True)
 for i,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 primary_atoms=[]
 for lab in ('Xerr','Zerr'):
  atoms=[tuple(x) for x in primary['sectors'][lab]['mechanism']['sound_outer_block']['atoms']]
  outer.add_block(atoms,'r68-primary-'+lab)
  primary_atoms.append(atoms)
 rows=[];new_blocks=[]
 for it in range(a.iterations):
  solved=outer.solve(120000);row={'iteration':it,'outer':{k:v for k,v in solved.items() if k!='compressed_schedule'}}
  if solved['status']!='SAT':rows.append(row);break
  times=solved['compressed_schedule'];row['schedule']=times;row['schedule_sha256']=B.sha_obj(times);row['audit']=M.audit_schedule(times,True)
  assert row['audit']['ok'] and row['audit']['global_interleaved']
  assert all(not M.block_holds(times,z) for z in primary_atoms+new_blocks)
  ss=B.sectors(times,lx,lz);row['sectors']={};added=0
  for lab,pool in (('Xerr',px),('Zerr',pz)):
   pre=M.fast_w12_adversary(ss[lab],pool)
   entry={'finder_status':pre['status'],'method':pre['method'],'complete_for_absence':False,
          'checked_single':pre.get('checked_single'),'checked_pairs':pre.get('checked_pairs')}
   if pre['status']=='SAT':
    mech=V.mechanism(ss[lab],pre['witness']['selected'])
    atoms=[tuple(x) for x in mech['sound_outer_block']['atoms']]
    outer.add_block(atoms,f'r68-cont-{it}-{lab}')
    new_blocks.append(atoms);added+=1
    entry['mechanism']=mech
   row['sectors'][lab]=entry
  row['sound_blocks_added']=added;row['total_asserted_blocks_after_step']=len(outer.blocks)
  rows.append(row)
  if not added:break
 out={'schema':'circdist-gross-round68-positive-cegar-continuation-v1',
      'scope':'positive witness continuation only; no finder absence is a verdict',
      'starting_blocks':{'round63_global_single':1440,'round62_retained':20,'round68_primary':2},
      'iterations_requested':a.iterations,'iterations_completed':len(rows),'ledger':rows,
      'new_sound_blocks':len(new_blocks),'all_source_mechanisms_raw_replayed':True,
      'no_exploratory_round63_pair_clauses_used':True,'outer_exhausted':False}
 dump(a.output,out)
 print(json.dumps({'iterations':len(rows),'new_blocks':len(new_blocks),'statuses':[[r.get('sectors',{}).get(l,{}).get('finder_status') for l in ('Xerr','Zerr')] for r in rows]}))
if __name__=='__main__':main()
