#!/usr/bin/env python3
from pathlib import Path
import argparse,json,hashlib

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--verification',type=Path,required=True);ap.add_argument('--dynamic-blocks',type=Path,required=True);ap.add_argument('--iteration',type=int,required=True);a=ap.parse_args();d=json.loads(a.verification.read_text());dyn=json.loads(a.dynamic_blocks.read_text()) if a.dynamic_blocks.exists() else [];assert len(dyn)==2*a.iteration
 for sector in ('Xerr','Zerr'):
  s=d['sectors'][sector];assert s['status']=='SATISFIABLE' and s['all_dimacs_clauses_satisfied'];m=s['mechanism'];assert m['canonical_replay']['ok'] and m['physical_syndrome']==[] and m['physical_nontrivial'];b=m['sound_outer_block'];dyn.append({'schema':'round69-raw-replayed-dynamic-block-v1','source_iteration':a.iteration,'sector':sector,'candidate_sha256':d['candidate_sha256'],'mechanism_sha256':sha(m),'selected_names':m['selected_names'],'fault_count':m['fault_count'],'atoms':b['atoms'],'atom_count':b['atom_count']})
 a.dynamic_blocks.write_text(json.dumps(dyn,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','dynamic_blocks':len(dyn),'next_iteration':len(dyn)//2},sort_keys=True))
if __name__=='__main__':main()
