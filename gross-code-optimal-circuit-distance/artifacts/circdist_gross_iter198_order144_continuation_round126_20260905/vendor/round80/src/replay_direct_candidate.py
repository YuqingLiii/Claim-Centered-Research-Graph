#!/usr/bin/env python3
from pathlib import Path
import sys,json,hashlib,time,argparse
PKG=Path(__file__).resolve().parent.parent
sys.path[:0]=[str(PKG/'src/round63_src'),str(PKG/'src')]
import model as M,round68_verify as V

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--output',type=Path);a=ap.parse_args();outpath=a.output or a.root/'direct_verification.json';t=time.monotonic();c=json.loads((a.root/'candidate.json').read_text());times={k:int(v) for k,v in c['schedule_times'].items()};px,pz,lx,lz=V.load_context();ss=V.sectors(times,lx,lz);assert sha(times)==c['schedule_sha256'];assert M.audit_schedule(times,True)==c['audit']
 out={'schema':'round69-complete-direct360-replay-v1','candidate_sha256':c['schedule_sha256'],'schedule_audit':M.audit_schedule(times,True),'sectors':{}}
 for s in ('Xerr','Zerr'):out['sectors'][s]=V.verify_one(a.root,s,ss[s])
 out['repair_gate']={'entered':False,'reason':'both complete direct-360 formulas are SAT; repair requires independently checked direct UNSAT in both sectors'};outpath.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','wall_seconds':time.monotonic()-t,'candidate':c['schedule_sha256'],'sectors':{s:{'status':out['sectors'][s]['status'],'weight':out['sectors'][s]['mechanism']['fault_count'],'atoms':out['sectors'][s]['mechanism']['sound_outer_block']['atom_count']} for s in ('Xerr','Zerr')}},sort_keys=True))
if __name__=='__main__':main()
