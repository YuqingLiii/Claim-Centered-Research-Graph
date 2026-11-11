#!/usr/bin/env python3
from pathlib import Path
import sys,json,gzip,hashlib,argparse
PKG=Path(__file__).resolve().parent.parent
sys.path[:0]=[str(PKG/'src/round63_src'),str(PKG/'src')]
import model as M,round68_build as B
from outer import OuterScheduler

def load(path):
 p=Path(path)
 if p.suffix=='.gz':
  with gzip.open(p,'rt') as f:return json.load(f)
 return json.loads(p.read_text())
def dump(p,o):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--dynamic-blocks',type=Path,default=PKG/'cegar/dynamic_blocks.json');ap.add_argument('--z3-timeout-ms',type=int,default=120000);a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
 px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz;r62=load(PKG/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz)
 old=load(PKG/'classification/round69_pair_classification.json.gz')['pairs'];oldgen=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{i}",[tuple(x) for x in t['atoms']]) for p in old for i,t in enumerate(p['deletion_minimal_terms'])];assert len(oldgen)==4740
 newobj=load(PKG/'classification/retained_terms.json.gz' if (PKG/'classification/retained_terms.json.gz').exists() else PKG/'classification/retained_terms.json');newgen=[(t['term_id'],[tuple(x) for x in t['atoms']]) for t in newobj['terms']];assert len(newgen)==566
 dyn=load(a.dynamic_blocks);expected=60+2*(a.iteration-30);assert len(dyn)==expected,(a.iteration,len(dyn),expected)
 outer=OuterScheduler(True)
 for i,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 for tag,atoms in oldgen+newgen:outer.add_block(atoms,tag)
 for i,b in enumerate(dyn):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{i}-{b['sector']}",b.get('mechanism_sha256'))
 assert len(outer.blocks)==1440+20+4740+566+len(dyn)
 smt=outer.s.to_smt2();(a.output/'outer.smt2').write_text(smt);solved=outer.solve(a.z3_timeout_ms);dump(a.output/'outer_result.json',solved)
 if solved['status']!='SAT':print(json.dumps({'iteration':a.iteration,'status':solved['status'],'blocks':len(outer.blocks),'seconds':solved['seconds'],'reason_unknown':solved.get('reason_unknown')}));return
 times=solved.pop('compressed_schedule');audit=M.audit_schedule(times,True);assert audit['ok'] and audit['global_interleaved']
 assert all(not M.block_holds(times,atoms) for _,atoms in oldgen+newgen)
 ss=B.sectors(times,lx,lz);candidate={'schema':'round72-generalized-cegar-candidate-v1','iteration':a.iteration,'schedule_sha256':sha(times),'schedule_times':times,'schedule_times_sorted':[{'edge':e,'time':times[e]} for e in sorted(times)],'audit':audit,'order_bindings':{'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)},'outer':solved,'outer_smt2_sha256':hashlib.sha256(smt.encode()).hexdigest(),'asserted_blocks':{'round63_single':1440,'round62':20,'round69_generalized':4740,'round72_generalized':566,'dynamic_exact':len(dyn),'total':len(outer.blocks),'exploratory_round63_pair':0},'model_metadata':M.model_metadata(px,pz,lx,lz),'pool_bindings':{'Xerr_pool_count':len(px),'Zerr_pool_count':len(pz),'Xerr_pool_sha256':sha(px),'Zerr_pool_sha256':sha(pz),'X_logical_basis':[M.bits(x) for x in lx],'Z_logical_basis':[M.bits(x) for x in lz]},'columns':{lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()}}
 dump(a.output/'candidate.json',candidate)
 for lab in ('Xerr','Zerr'):B.build_direct_cnf(ss[lab],a.output/'direct360'/lab,candidate['schedule_sha256'],10)
 print(json.dumps({'iteration':a.iteration,'status':'SAT','schedule_sha256':candidate['schedule_sha256'],'blocks':len(outer.blocks),'outer_seconds':solved['seconds'],'audit':audit},sort_keys=True))
if __name__=='__main__':main()
