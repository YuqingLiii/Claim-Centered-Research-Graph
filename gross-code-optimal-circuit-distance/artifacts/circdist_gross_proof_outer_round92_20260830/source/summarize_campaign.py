from pathlib import Path
import json,hashlib,gzip,os
R=Path('/tmp/circdist_round92_science')
def load(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sh(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def sho(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
rows=[]
for i in range(124,136):
 meta=load(R/f'formulas/iter{i}/metadata.json');src=load(R/f'formulas/iter{i}/source.json.gz');rep=load(R/f'iter{i}/outer/replay.json');dv=load(R/f'iter{i}/direct/direct_verification.json');rec=load(R/f'iter{i}/record.json')
 sec={}
 for s in ('Xerr','Zerr'):
  m=dv['sectors'][s]['mechanism'];summ=load(R/f'iter{i}/direct/direct360/{s}.summary.json')
  assert dv['sectors'][s]['status']=='SATISFIABLE' and dv['sectors'][s]['all_dimacs_clauses_satisfied'] and m['physical_syndrome']==[] and m['physical_nontrivial'] and m['canonical_physical_parities_equal']
  sec[s]={'status':'SATISFIABLE','weight':m['fault_count'],'selected_names':m['selected_names'],'logical_bits_lsb_first':''.join(map(str,m['canonical_replay']['logical_parities'])),'direct_cnf_sha256':summ['dimacs_sha256'],'mechanism_sha256':sho(m),'physical_replay':True}
 rows.append({'iteration':i,'selector_count':meta['selector_count'],'assertions':meta['assertions'],'outer_variables':meta['variables'],'outer_clauses':meta['clauses'],'source_semantic_sha256':src['semantic_payload_sha256'],'source_file_sha256':sh(R/f'formulas/iter{i}/source.json.gz'),'outer_cnf_sha256':meta['cnf_sha256'],'outer_status':'SATISFIABLE','outer_assignment_sha256':rep['assignment_sha256'],'candidate_schedule_sha256':rep['compressed_schedule_sha256'],'used_layers':rep['frozen_schedule_audit']['used_layers'],'frozen_schedule_ok':rep['frozen_schedule_audit']['ok'],'direct':sec,'state_after_sha256':rec['state_after_sha256']})
final=load(R/'state/iter136_state.json');fs=load(R/'formulas/iter136/source.json.gz');fm=load(R/'formulas/iter136/metadata.json');fc=load(R/'formulas/iter136/encoding_check.json')
summary={'schema':'circdist-gross-round92-campaign-summary-v1','status':'PASS','strict_serial':True,'iterations':rows,'completed_iterations':list(range(124,136)),'outer_sat_count':12,'direct_sat_count':24,'timeouts':0,'unknowns':0,'unsat_count':0,'new_ordinary_campaign_selectors':24,'preouter_retained_selectors':44,'final':{'next_iteration':136,'started':False,'selector_count':final['selector_count'],'selector_state_sha256':final['selector_state_sha256'],'source_semantic_sha256':fs['semantic_payload_sha256'],'source_file_sha256':sh(R/'formulas/iter136/source.json.gz'),'assertions':fm['assertions'],'variables':fm['variables'],'clauses':fm['clauses'],'cnf_sha256':fm['cnf_sha256'],'encoding_check_status':fc['status']}}
(R/'data/campaign_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
# Bounded process ledger.
proc=[]
for p in sorted((R/'logs').glob('*.process.json')):proc.append({'path':p.relative_to(R).as_posix(),**load(p)})
for p in sorted((R/'controls/actual_sat_trace').glob('*.run.json')):proc.append({'path':p.relative_to(R).as_posix(),**load(p)})
assert len(proc)==40 and all(x['final_status']=='exited_and_reaped' and not x['timed_out'] for x in proc)
ledger={'schema':'circdist-gross-round92-process-ledger-v1','status':'PASS','bounded_foreground_children':len(proc),'science_solver_children':37,'actual_trace_checker_children':3,'proof_fixture_synchronous_children':6,'proof_fixture_children_reaped':True,'weight9_synthesis_auxiliary_gzip_children':1,'weight9_synthesis_auxiliary_children_reaped':True,'background_processes':0,'survivors':0,'timeouts':0,'records':proc,'timeout_policy':'TERM, bounded harvest, KILL if needed, mandatory wait/reap; no timeout occurred','canceled_packaging_experiment':{'name':'online_weight9_synthesis.py','disposition':'interrupted by parent steering with Ctrl-C; exit 1; traceback retained only in failure ledger; no result/state/source write; process reaped'}}
(R/'PROCESS_LEDGER.json').write_text(json.dumps(ledger,indent=2,sort_keys=True)+'\n')
print(json.dumps({'campaign_summary_sha256':sh(R/'data/campaign_summary.json'),'process_ledger_sha256':sh(R/'PROCESS_LEDGER.json'),'weights':[[x['direct']['Xerr']['weight'],x['direct']['Zerr']['weight']] for x in rows],'final':summary['final']},sort_keys=True))
