#!/usr/bin/env python3
"""Independent selector-prefix and physical-mechanism continuation audit."""
from pathlib import Path
import argparse,gzip,hashlib,json,sys
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def sho(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--dependency',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();V=a.dependency.resolve()/'vendor/round80'
sys.path[:0]=[str(V/'src/round63_src'),str(V/'src')];import model,round68_build
_,_,lx,lz=round68_build.load_context();state=load(R/'continuation/preouter_iter124_state.json');selectors=list(state['selectors'])
assert state['next_iteration']==124 and not state['started'] and len(selectors)==state['selector_count']==208
assert state['selector_state_sha256']=='e1283b9fa221ecea75b5cb233e78ecee6fc9a461e5eef84144b3c61cadd1da94'
rows=[]
for i in range(124,136):
 F=R/f'formulas/iter{i}';E=R/f'iterations/iter{i}';S=load(F/'source.json.gz');C=load(E/'outer/candidate.json');D=load(E/'direct/direct_verification.json');rec=load(E/'record.json')
 assert len(S['selectors'])==S['expected']['selectors']==len(selectors)
 semantic=dict(S);rs=semantic.pop('semantic_payload_sha256');assert sho(semantic)==rs
 times={str(k):int(v) for k,v in C['compressed_times'].items()};schedule=sho(times);assert schedule==C['compressed_schedule_sha256']==D['candidate_sha256']
 audit=model.audit_schedule(times,True);assert audit==C['frozen_audit'] and audit['ok'] and audit['global_interleaved'] and audit['edge_count']==864 and audit['overlaps']==648
 sectors=round68_build.sectors(times,lx,lz)
 assert not any(model.verify_named_selection(sectors[s['sector']],s['selected_names'],10)['ok'] for s in selectors)
 new=[]
 for sec in ('Xerr','Zerr'):
  z=D['sectors'][sec];m=z['mechanism'];assert z['status']=='SATISFIABLE' and z['all_dimacs_clauses_satisfied'] and z['formula_summary']['complete_query']
  assert 1<=m['fault_count']<=10 and m['physical_syndrome']==[] and m['physical_nontrivial'] and m['canonical_physical_parities_equal']
  exact=model.verify_named_selection(sectors[sec],m['selected_names'],10);assert exact['ok'] and exact['weight']==m['fault_count']
  data=[];groups={}
  for n in m['selected_names']:
   p=n.split(':')
   if p[0]=='D':data.append(int(p[1]))
   else:groups.setdefault(p[1],[]).append(int(p[2]))
  sel={'mechanism_id':f'r92-i{i}-{sec}','source_iteration':i,'sector':sec,'fault_count':m['fault_count'],'selected_names':m['selected_names'],'data_support':sorted(data),'group_kinds':{k:sorted(v) for k,v in sorted(groups.items(),key=lambda q:int(q[0]))},'source_schedule_sha256':schedule,'source_times':times,'canonical_support':m['canonical_replay']['net_support'],'physical_support':m['physical_net_support'],'source_atoms':m['sound_outer_block']['atoms'],'source_atom_count':m['sound_outer_block']['atom_count'],'origin':f'round92_proof_outer_iteration{i}_direct360','source_symbolic_validity':'True'}
  sel['selector_semantic_sha256']=sho({k:sel[k] for k in ('sector','selected_names','data_support','group_kinds')});new.append(sel)
 selectors+=new;keys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256');statehash=sho([{k:s.get(k) for k in keys} for s in selectors])
 assert rec['source_selector_count']==len(selectors)-2 and rec['new_selectors']==[s['mechanism_id'] for s in new] and rec['state_after_sha256']==statehash and rec['state_mutated_atomically'] and not rec['repair_entered']
 N=load(R/f'formulas/iter{i+1}/source.json.gz');assert len(N['selectors'])==len(selectors)
 rows.append({'iteration':i,'schedule_sha256':schedule,'source_selector_count':len(selectors)-2,'state_after_sha256':statehash,'weights':{s:D['sectors'][s]['mechanism']['fault_count'] for s in ('Xerr','Zerr')}})
final=load(R/'continuation/final_state.json');assert final['selectors']==selectors and final['selector_count']==232 and final['selector_state_sha256']==rows[-1]['state_after_sha256']=='1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81'
assert final['next_iteration']==136 and not final['started'] and final['stop'] is None
FM=load(R/'formulas/iter136/metadata.json');FS=load(R/'formulas/iter136/source.json.gz');assert FM['cnf_sha256']=='289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e' and FS['semantic_payload_sha256']=='a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe'
out={'schema':'circdist-round92-continuation-audit-v1','status':'PASS','initial_iteration':124,'initial_selector_count':208,'completed_candidates':12,'new_campaign_selectors':24,'final_selector_count':232,'final_selector_state_sha256':final['selector_state_sha256'],'fresh_next_iteration':136,'fresh_source_semantic_sha256':FS['semantic_payload_sha256'],'fresh_cnf_sha256':FM['cnf_sha256'],'iterations':rows}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('ROUND92_CONTINUATION_AUDIT_PASS',len(rows))

