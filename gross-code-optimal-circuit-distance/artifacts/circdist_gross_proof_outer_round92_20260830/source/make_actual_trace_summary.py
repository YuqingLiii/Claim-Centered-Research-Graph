from pathlib import Path
import hashlib,json
R=Path('/tmp/circdist_round92_science');C=R/'controls/actual_sat_trace'
def sh(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
rows={}
for n in ('full','truncated','corrupt'):
 run=json.loads((C/f'{n}.run.json').read_text());log=(C/f'{n}.log').read_text(errors='replace')
 assert run['returncode']==1 and not run['timed_out'] and 'NOT VERIFIED' in log
 rows[n]={'returncode':1,'timed_out':False,'accepted':False,'trace_sha256':sh(C/f'{n}.drat'),'trace_bytes':(C/f'{n}.drat').stat().st_size,'log_sha256':sh(C/f'{n}.log'),'stderr_sha256':sh(C/f'{n}.stderr.log')}
D=json.loads((R/'data/sat_drat_trace_disposition.json').read_text());src=next(x for x in D['traces'] if x['iteration']==127 and x['query']=='Zerr')
out={'schema':'circdist-round92-actual-sat-trace-controls-v1','status':'PASS','iteration':127,'query':'Zerr','formula_sha256':src['formula_sha256'],'source_trace_sha256':src['sha256'],'source_trace_bytes':src['bytes'],'source_trace_empty_clause_lines':src['empty_clause_lines'],'drat_checker_runs':rows,'full_sat_trace_rejected':True,'truncated_sat_trace_rejected':True,'corrupt_sat_trace_rejected':True,'lrat_control':'not applicable: no actual Gross UNSAT refutation exists; separate valid/corrupt/truncated fixture checks DRAT-to-LRAT and LRAT checker behavior','scope':'negative checker controls only; rejection of a SAT-side stream is not an absence result'}
assert rows['full']['trace_sha256']==src['sha256'];(C/'summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
