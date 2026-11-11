from pathlib import Path
import gzip, hashlib, json, math, os, subprocess, sys, time
R=Path(sys.argv[1]).resolve(); O=Path(sys.argv[2]).resolve(); repo=R.parents[2]
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()
def canon(x): return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def load(p):
 p=Path(p)
 if not p.exists() and Path(str(p)+'.gz').exists(): p=Path(str(p)+'.gz')
 opener=gzip.open if p.suffix=='.gz' else open
 with opener(p,'rt',encoding='utf-8') as f:return json.load(f)
rows=[]
for p in sorted(x for x in R.rglob('*') if x.is_file()):
 rows.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
# Verify the already-produced independent scientific audit and exact frontier.
audit=load(R/'verification/independent_campaign_audit.json')
assert audit['status']=='PASS' and audit['completed_candidate_count']==12
assert audit['outer_sat_count']==12 and audit['direct_sat_count']==24
assert [x['iteration'] for x in audit['iterations']]==list(range(160,172))
order5=load(R/'synthesis/order5_gf2_closure.json')
assert order5['status']=='PASS' and order5['retained_term_count']==0
assert order5['finite_domain']['unordered_distinct_quintuples_enumerated']==math.comb(125,5)+math.comb(109,5)==351359546
assert order5['sector_results']['Xerr']['unique_eligible_replayed']==38382
assert order5['sector_results']['Zerr']['unique_eligible_replayed']==1771
state=load(R/'state/iter172_state.json'); meta=load(R/'formulas/iter172/metadata.json')
assert state['next_iteration']==172 and state['started'] is False and state['stop'] is None
assert state['selector_count']==304 and state['selector_state_sha256']=='a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1'
assert meta['assertions']==19186 and meta['variables']==413646 and meta['clauses']==1406245
assert meta['cnf_sha256']=='f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342'
proc=[]
for p in sorted((R/'logs/process').glob('*.json')):
 x=load(p); assert x['final_status']=='exited_and_reaped' and x['reaped'] and not x['timed_out']
 proc.append({'path':p.relative_to(R).as_posix(),'returncode':x['returncode'],'final_status':x['final_status'],'timed_out':x['timed_out']})
assert sum(x['returncode']==10 for x in proc)==36
assert [(Path(x['path']).name,x['returncode']) for x in proc if x['returncode'] not in (0,10)]==[
 ('independent_campaign_audit_attempt1.json',1),('order5_Xerr_exact_enum.json',-6),('order5_compile.json',1)]
canonical={
 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml':'912721a2fc92419ace54c78c092dee2d545b2a03262a4c1f22a16444c93435bd',
 'operations/circdist/SCHEDULER.yaml':'079be3ade7085377a3453951a6dc651adf73ce067252f50b9b664bb9d3a1beb9',
 'circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md':'5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64',
 'DAG_PROTOCOL.md':'d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095',
 'FILE_PROTOCOL.md':'d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595',
 'circdist/reviews/circdist_gross_proof_outer_round96_exact_review_round97_20260831.md':'f8700a2e90c849442c3917e96afc049a9417b40a28e2800d6ca37317e3b5b369',
}
for p,h in canonical.items(): assert sha(repo/p)==h,(p,sha(repo/p),h)
out={
 'schema':'circdist-round98-model-capacity-recovery-inventory-v1','status':'PASS','created_unix':time.time(),
 'recovery_boundary':'after the pre-interruption deterministic compression child resumed and exited/reaped with rc=0; before any report or seal generation',
 'package_file_count':len(rows),'package_stored_bytes':sum(x['bytes'] for x in rows),
 'package_inventory_sha256':hashlib.sha256(canon(rows)).hexdigest(),'rows':rows,
 'science_integrity':{'iterations':list(range(160,172)),'outer_sat':12,'direct_sat':24,'order5_domain':351359546,'order5_unique_eligible':40153,'order5_retained':0,'frontier_iteration':172,'frontier_selector_count':304,'audit_status':'PASS'},
 'process_integrity':{'record_count':len(proc),'solver_sat_children':36,'all_recorded_children_reaped':True,'timed_out':0,'records':proc},
 'canonical_sha256':canonical,
 'interruption':{'kind':'model-capacity','classification':'orchestration-only','science_process_was_interrupted':False,'science_artifact_recomputation_authorized_or_performed':False,'basis':'the only child spanning recovery was deterministic packaging compression; it resumed and exited/reaped rc=0; all 36 solver records and all other recorded children were already exited/reaped; the independent scientific audit was PASS'},
}
O.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:out[k] for k in ('status','package_file_count','package_stored_bytes','package_inventory_sha256')},sort_keys=True))
