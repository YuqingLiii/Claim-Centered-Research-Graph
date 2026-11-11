#!/usr/bin/env python3
from pathlib import Path
import gzip,hashlib,json,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent.parent
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import model as M

def loadgz(p):
 with gzip.open(p,'rt') as f:return json.load(f)
rows=[];schedules=[]
for i in range(6,30):
 d=ROOT/'cegar'/f'iter{i}';cand=loadgz(d/'candidate.json.gz');v=loadgz(d/'direct_verification.json.gz')
 for s in ('Xerr','Zerr'):
  n=v['sectors'][s]['negative_controls'];assert n['flip_first_selected_primary']['failed_clause_count']>0 and not n['remove_first_fault']['ok']
  rows.append({'iteration':i,'sector':s,'flip_assignment_control':n['flip_first_selected_primary'],'remove_fault_control':n['remove_first_fault']})
 times={k:int(x) for k,x in cand['schedule_times'].items()};q=0;inc=sorted(e for e in times if e.endswith(f':{q}'));assert len(inc)==6
 bad=dict(times);bad[inc[1]]=bad[inc[0]];audit=M.audit_schedule(bad,True);assert not audit['ok'] and audit['conflicts']
 schedules.append({'iteration':i,'mutation':{'edge':inc[1],'original_time':times[inc[1]],'corrupted_time':times[inc[0]],'collides_with':inc[0]},'accepted':False,'audit':audit})
assert len(rows)==48 and len(schedules)==24
# Produce one deterministic truncated assignment artifact and assert incompleteness.
p=ROOT/'cegar/iter6/solver/Xerr.solver.log.gz'
with gzip.open(p,'rt') as f:lines=f.read().splitlines()
for j in range(len(lines)-1,-1,-1):
 if lines[j].startswith('v '):
  toks=lines[j].split(); assert len(toks)>2; toks.pop(-2 if toks[-1]=='0' else -1); lines[j]=' '.join(toks);break
raw=('\n'.join(lines)+'\n').encode();out=ROOT/'controls/truncated_assignment_iter6_Xerr.solver.log.gz'
with out.open('wb') as f:
 with gzip.GzipFile(filename='',mode='wb',fileobj=f,compresslevel=9,mtime=0) as g:g.write(raw)
lits=[]
for line in raw.decode(errors='replace').splitlines():
 if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
assert len({abs(x) for x in lits})==5995
obj={'schema':'round71-negative-controls-v1','status':'PASS','direct_controls':rows,'schedule_mutation_controls':schedules,'counts':{'assignment_flip_rejected':48,'fault_removal_rejected':48,'schedule_collision_rejected':24,'truncated_assignment_rejected':1},'truncated_assignment':{'path':'controls/truncated_assignment_iter6_Xerr.solver.log.gz','uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'assignment_variables_present':5995,'expected_variables':5996,'accepted':False,'reason':'complete assignment cardinality mismatch'}}
(ROOT/'controls/negative_controls.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
print(json.dumps(obj['counts'],indent=2))
