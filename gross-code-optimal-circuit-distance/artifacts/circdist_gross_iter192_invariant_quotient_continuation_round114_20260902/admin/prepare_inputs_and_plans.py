#!/usr/bin/env python3
from pathlib import Path
import datetime, hashlib, json, os, shutil
scratch=Path('/private/tmp/circdist-r114-proposer-20260902')
repo=Path('<repo>')
pkg=repo/'circdist/artifacts/circdist_gross_iter191_invariant_quotient_continuation_round112_20260902'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
inputs=scratch/'input/iter192_full_invariant'; inputs.mkdir(parents=True,exist_ok=False)
copy_rows=[]
for rel in ('frontier/iter192_full_invariant/source.json.gz','frontier/iter192_full_invariant/state.json'):
 src=pkg/rel; dst=inputs/src.name; shutil.copyfile(src,dst)
 ss,ds=src.stat(),dst.stat()
 copy_rows.append({'source':str(src),'destination':str(dst),'sha256':sha(dst),'bytes':ds.st_size,'source_inode':ss.st_ino,'destination_inode':ds.st_ino,'source_nlink':ss.st_nlink,'destination_nlink':ds.st_nlink,'distinct_inode':ss.st_ino!=ds.st_ino})
plans=scratch/'plans'; plans.mkdir()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
global_plan={
 'schema':'circdist-gross-round114-predeclared-global-information-gain-plan-v1','created_utc':now,'frozen_before_mandatory_solver':True,
 'input_iteration':192,'input_source_sha256':'89ed11977cacaed4f46a8c0756fef77a9706a2f3ce65d6ec1b496424fb9533f3','input_state_sha256':'e4085c5a776561bfc136d67f64988c31c0e26b063afd715d61a836a2f6ff06f1',
 'mandatory_first':['reconstruct exact iter192 base and 71-root quotient','solve the exact reviewed quotient with proof output enabled from byte zero','if SAT verify complete assignment, every clause, decoding, blocks, selectors, lex roots, action and frozen schedule','build and adjudicate unrestricted Xerr then Zerr direct-360 sectors serially'],
 'stronger_mechanism_attempt':{
   'name':'full CSS-duality involution and order-144 action closure','map':'D sends check coordinate g=(i,j) to -g=(-i mod 12,-j mod 6), swaps X and Z, and sends data q=g to 72+(-g) and q=72+g to -g; residual-kind indices are preserved','group':'translations Z_12 x Z_6 extended by D with D^2=1 and D T_delta D=T_-delta','checks':['all frozen check/incidence/edge maps','D involution and conjugation on all finite domains','all block and selector semantic images','complete missing-image/collision census','physical replay for retained selector images','full registry closure under translation generators and D','order-144 quotient recurrence and equisatisfiability only if the base is proved invariant'],'bounded_domain':'exactly the 517,140 input block semantics, 25,164 input selectors, and at most the bilateral mandatory-parent orbits; no adaptive family growth','acceptance':'retain only if every action, semantic, provenance, closure and physical check passes; any unchecked or nonfree image is rejected','information_gain':'a sound dual closure transports every exclusion across CSS sectors and licenses a 143-root orbit quotient, covering a symmetry coset absent from the Round112 71-root translation quotient'},
 'fallback_condition':'only if no sound usable stronger global mechanism is obtained after the exact bounded audit','root_stop':'stop immediately if a certified branch A or B theorem closes the root'
}
batch_plan={
 'schema':'circdist-gross-round114-predeclared-direct-selector-fallback-batch-v1','created_utc':now,'frozen_before_mandatory_solver':True,'activated_only_if':'the stronger CSS-duality mechanism audit yields no sound usable retained mechanism','source_iteration':192,'next_iteration':193,'enumeration_order':['Xerr','Zerr'],'mandatory_parent_counts':{'Xerr':1,'Zerr':1},'target_collision_free_parents_per_sector':8,'maximum_total_attempts_per_sector_including_mandatory':16,'maximum_additional_solver_attempts_per_sector':15,'no_adaptive_expansion':True,'strict_serial':True,'stop_rule':'per sector stop immediately at 8 accepted collision-free parents including mandatory, or at 16 total attempts, or on proof-checked UNSAT/UNKNOWN; never launch attempt target+1','blocking_rule':'append one 360-literal clause false on exactly each prior complete primary selection; auxiliary variables are excluded','collision_rule':'retain and block a collision model but do not count it toward the target','candidate_acceptance':['SAT rc10','complete assignment covers each variable exactly once','every cumulative CNF clause satisfied','named weight <=10, zero syndrome, nonzero logical action and nonstabilizer in canonical and physical replay','free collision-free 72-element translation orbit','all translated schedules and mechanisms replay','zero installed and prior accepted-orbit collision'],'unsat_rule':'usable only with retained DRAT, independently accepted and converted LRAT, independently accepted LRAT, and corrupt/truncated negative controls','unknown_rule':'timeout or UNKNOWN is no verdict and stops the sector','frontier_rule':'atomically append all accepted complete 72-element orbits only after bilateral adjudication; build/check exactly one fresh unstarted iteration-193 frontier and do not solve it','root_scope':'finite information gain only; no root conclusion absent a complete branch theorem','information_gain_relative_to_round112':'doubles the accepted collision-free parent target from 4 to 8 per sector while retaining a fixed 16-attempt ceiling, exact primary AllSAT blocking, and no adaptive expansion'
}
(plans/'GLOBAL_MECHANISM_PLAN.json').write_text(json.dumps(global_plan,indent=2,sort_keys=True)+'\n')
(plans/'FALLBACK_BATCH_PLAN.json').write_text(json.dumps(batch_plan,indent=2,sort_keys=True)+'\n')
out={'schema':'circdist-gross-round114-input-and-plan-preparation-v1','status':'PASS','created_utc':now,'copies':copy_rows,'global_plan_sha256':sha(plans/'GLOBAL_MECHANISM_PLAN.json'),'fallback_plan_sha256':sha(plans/'FALLBACK_BATCH_PLAN.json'),'plans_frozen_before_solver':True}
(scratch/'admin/input_plan_preparation.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
