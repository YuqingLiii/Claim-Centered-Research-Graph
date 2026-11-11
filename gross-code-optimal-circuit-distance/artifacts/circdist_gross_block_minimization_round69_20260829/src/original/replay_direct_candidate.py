from pathlib import Path
import sys,json,hashlib,time,traceback,argparse
ap=argparse.ArgumentParser();ap.add_argument('--root',required=True);a=ap.parse_args()
R68=Path('<repo>/circdist/artifacts/circdist_gross_direct360_proof_round68_20260829')
root=Path(a.root)
sys.path[:0]=[str(R68/'src/round63_src'),str(R68/'src')]
import model as M,round68_verify as V
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
t0=time.monotonic(); status='FAIL'
try:
 c=json.loads((root/'candidate.json').read_text()); times={k:int(v) for k,v in c['schedule_times'].items()}
 px,pz,lx,lz=V.load_context(); ss=V.sectors(times,lx,lz)
 assert sha(times)==c['schedule_sha256']; assert M.audit_schedule(times,True)==c['audit']
 out={'schema':'round69-complete-direct360-replay-v1','candidate_sha256':c['schedule_sha256'],'schedule_audit':M.audit_schedule(times,True),'sectors':{}}
 for s in ('Xerr','Zerr'):out['sectors'][s]=V.verify_one(root,s,ss[s])
 out['repair_gate']={'entered':False,'reason':'both complete direct-360 formulas are SAT; repair requires independently checked direct UNSAT in both sectors'}
 (root/'direct_verification.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 status='PASS'; print(json.dumps({'status':status,'candidate':c['schedule_sha256'],'sectors':{s:{'status':out['sectors'][s]['status'],'weight':out['sectors'][s]['mechanism']['fault_count'],'atoms':out['sectors'][s]['mechanism']['sound_outer_block']['atom_count']} for s in ('Xerr','Zerr')}},sort_keys=True))
except Exception:
 traceback.print_exc(); raise
finally:
 (root/'direct_verification.run.json').write_text(json.dumps({'status':status,'wall_seconds':time.monotonic()-t0,'command':'fresh Python import of pinned round68_verify.verify_one over both complete formulas'},indent=2)+'\n')
