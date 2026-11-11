from pathlib import Path
import argparse,json,sys,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
P=a.package.resolve();sys.path[:0]=[str(P/'src/round63_src'),str(P/'src')]
import model as M, round68_build as B
a.output.mkdir(parents=True,exist_ok=False);(a.output/'direct360').mkdir();(a.output/'solver').mkdir()
src=json.loads(a.candidate.read_text());times={k:int(v) for k,v in src['schedule_times'].items()}
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
audit=M.audit_schedule(times,True);assert audit['ok'] and audit['global_interleaved'] and sha(times)==src['schedule_sha256']
px,pz,lx,lz=B.load_context();ss=B.sectors(times,lx,lz)
c={'schema':'round86-efssc-direct-candidate-v1','schedule_times':times,'schedule_sha256':sha(times),'audit':audit,'source_outer_formula_sha256':src.get('outer_formula_sha256'),'efssc_cuts_avoided':src['efssc_cuts_avoided'],'existing_blocks_avoided':src['existing_blocks_avoided']}
(a.output/'candidate.json').write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
for lab in ('Xerr','Zerr'):B.build_direct_cnf(ss[lab],a.output/'direct360'/lab,c['schedule_sha256'],10)
print(json.dumps({'status':'PASS','candidate':c['schedule_sha256'],'cnfs':{lab:json.loads((a.output/'direct360'/f'{lab}.summary.json').read_text()) for lab in ('Xerr','Zerr')}},sort_keys=True))
