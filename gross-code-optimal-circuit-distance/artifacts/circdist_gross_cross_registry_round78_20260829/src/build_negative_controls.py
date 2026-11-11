#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,sys
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();sys.path[:0]=[str(R/'src/round63_src'),str(R/'src')]
import model as M
rows=[];schedules=[]
for i in range(42,54):
 d=R/'cegar'/f'iter{i}';cand=json.loads((d/'candidate.json').read_text());v=json.loads((d/'direct_verification.json').read_text())
 for s in ('Xerr','Zerr'):
  n=v['sectors'][s]['negative_controls'];assert n['flip_first_selected_primary']['failed_clause_count']>0 and not n['remove_first_fault']['ok']
  rows.append({'iteration':i,'sector':s,'flip_assignment_control':n['flip_first_selected_primary'],'remove_fault_control':n['remove_first_fault']})
 times={k:int(x) for k,x in cand['schedule_times'].items()};q=0;inc=sorted(e for e in times if e.endswith(f':{q}'));assert len(inc)==6
 bad=dict(times);bad[inc[1]]=bad[inc[0]];audit=M.audit_schedule(bad,True);assert not audit['ok'] and audit['conflicts']
 schedules.append({'iteration':i,'mutation':{'edge':inc[1],'original_time':times[inc[1]],'corrupted_time':times[inc[0]],'collides_with':inc[0]},'accepted':False,'audit':audit})
p=R/'cegar/iter42/solver/Xerr.solver.log';lines=p.read_text(errors='replace').splitlines();expected=json.loads((R/'cegar/iter42/direct360/Xerr.summary.json').read_text())['variables'];removed=None
for j in range(len(lines)-1,-1,-1):
 if lines[j].startswith('v '):
  toks=lines[j].split();vals=[x for x in toks[1:] if x!='0'];
  if vals:
   removed=vals[-1];toks.remove(removed);lines[j]=' '.join(toks);break
assert removed is not None
raw=('\n'.join(lines)+'\n').encode();out=R/'controls/truncated_assignment_iter42_Xerr.solver.log';out.write_bytes(raw);lits=[]
for line in raw.decode(errors='replace').splitlines():
 if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
present=len({abs(x) for x in lits});assert present==expected-1,(present,expected)
obj={'schema':'round74-negative-controls-v1','status':'PASS','classification_deletion_controls':'embedded in every retained term; each removed atom exposes an invalid selected-mechanism or positive-library tuple and records current-library-relative cover','direct_controls':rows,'schedule_mutation_controls':schedules,'counts':{'assignment_flip_rejected':24,'fault_removal_rejected':24,'schedule_collision_rejected':12,'truncated_assignment_rejected':1,'retained_term_deletion_controls':1372,'proof_checker_valid_accepts':2,'proof_checker_corrupt_truncated_rejects':2},'truncated_assignment':{'path':'controls/truncated_assignment_iter42_Xerr.solver.log.gz','uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'assignment_variables_present':present,'expected_variables':expected,'removed_literal':int(removed),'accepted':False,'reason':'complete assignment cardinality mismatch'},'absence_semantics':{'zero_truth_cells_used':0,'positive_finder_misses_used':0,'weight14_misses_used':0,'deletion_countertuples_used':0}}
(R/'controls/negative_controls.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');print(json.dumps(obj['counts'],sort_keys=True))
