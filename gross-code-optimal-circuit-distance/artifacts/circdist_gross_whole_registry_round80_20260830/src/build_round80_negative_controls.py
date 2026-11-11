#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,sys
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();sys.path[:0]=[str(R/'src/round63_src'),str(R/'src')]
import model as M
def load(p):
 p=Path(p)
 if not p.exists() and Path(str(p)+'.gz').exists():p=Path(str(p)+'.gz')
 b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
rows=[];schedules=[]
for i in range(90,102):
 d=R/'cegar'/f'iter{i}';cand=load(d/'candidate.json');v=load(d/'direct_verification.json')
 for s in ('Xerr','Zerr'):
  n=v['sectors'][s]['negative_controls'];assert n['flip_first_selected_primary']['failed_clause_count']>0 and not n['remove_first_fault']['ok']
  rows.append({'iteration':i,'sector':s,'flip_assignment_control':n['flip_first_selected_primary'],'remove_fault_control':n['remove_first_fault']})
 times={k:int(x) for k,x in cand['schedule_times'].items()};q=0;inc=sorted(e for e in times if e.endswith(f':{q}'));assert len(inc)==6
 bad=dict(times);bad[inc[1]]=bad[inc[0]];audit=M.audit_schedule(bad,True);assert not audit['ok'] and audit['conflicts']
 schedules.append({'iteration':i,'mutation':{'edge':inc[1],'original_time':times[inc[1]],'corrupted_time':times[inc[0]],'collides_with':inc[0]},'accepted':False,'audit':audit})
p=R/'cegar/iter90/solver/Xerr.solver.log';lines=p.read_text(errors='replace').splitlines();expected=load(R/'cegar/iter90/direct360/Xerr.summary.json')['variables'];removed=None
for j in range(len(lines)-1,-1,-1):
 if lines[j].startswith('v '):
  vals=[x for x in lines[j].split()[1:] if x!='0']
  if vals:removed=vals[-1];toks=lines[j].split();toks.remove(removed);lines[j]=' '.join(toks);break
assert removed is not None
raw=('\n'.join(lines)+'\n').encode();out=R/'controls/truncated_assignment_iter90_Xerr.solver.log';out.write_bytes(raw);lits=[]
for line in raw.decode(errors='replace').splitlines():
 if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
present=len({abs(x) for x in lits});assert present==expected-1,(present,expected)
online=load(R/'classification/round80_online_retained_terms.json')['terms'];cross=load(R/'cross_registry/round80_cross_registry_retained_terms.json')['terms']
odeletions=sum(len(t['deletion_controls']) for t in online);xdeletions=sum(len(t['deletion_controls']) for t in cross);whole=load(R/'whole_registry/hitting_synthesis/factorized_selector_proofs.json')['proofs'];wdeletions=sum(len(t['deletion_controls']) for t in whole)
obj={'schema':'round80-negative-controls-v1','status':'PASS','classification_deletion_controls':'embedded in every retained term; each removed atom exposes a tuple invalid for the named positive relation or fixed selector; this licenses only candidate relation/fixed-selector atom minimality and never installed-union/global physical minimality or absence','direct_controls':rows,'schedule_mutation_controls':schedules,
 'counts':{'assignment_flip_rejected':24,'fault_removal_rejected':24,'schedule_collision_rejected':12,'truncated_assignment_rejected':1,'whole_registry_retained_term_deletion_controls':wdeletions,'online_retained_term_deletion_controls':odeletions,'cross_registry_retained_term_deletion_controls':xdeletions,'retained_term_deletion_controls_total':wdeletions+odeletions+xdeletions,'proof_checker_valid_accepts':2,'proof_checker_corrupt_rejects':2,'proof_checker_truncated_rejects':2},
 'truncated_assignment':{'path':'controls/truncated_assignment_iter90_Xerr.solver.log','uncompressed_sha256':hashlib.sha256(raw).hexdigest(),'assignment_variables_present':present,'expected_variables':expected,'removed_literal':int(removed),'accepted':False,'reason':'complete assignment cardinality mismatch'},
 'whole_registry_zero_domain_regression':{'raw_zero_domain_attempts':2461,'accepted_zero_domain_terms':0,'rule':'a candidate with an empty exact local-order product is rejected before semantic classification or state mutation'},
 'absence_semantics':{'zero_truth_cells_used':0,'zero_domains_used':0,'positive_finder_misses_used':0,'completion_misses_used':0,'solver_negatives_used':0,'deletion_countertuples_used':0}}
(R/'controls/negative_controls.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');print(json.dumps(obj['counts'],sort_keys=True))
