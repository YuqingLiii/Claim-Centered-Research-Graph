#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from collections import Counter,defaultdict
import argparse,hashlib,json,math,sys,time
p=argparse.ArgumentParser();p.add_argument('--state',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--vendor',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();t0=time.time()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def objsha(o):return hashlib.sha256(canon(o)).hexdigest()
state=json.loads(a.state.read_text());cand=json.loads(a.candidate.read_text());selectors=state['selectors'];assert len(selectors)==state['selector_count']==234
sys.path[:0]=[str(a.vendor/'src/round63_src'),str(a.vendor/'src')]
import model
import round68_build as builder
_,_,lx,lz=builder.load_context();times=cand['compressed_times'];sectors=builder.sectors(times,lx,lz)
bysec={k:[] for k in ('Xerr','Zerr')}
for idx,x in enumerate(selectors):
 assert x['sector'] in bysec and len(x['selected_names'])==len(set(x['selected_names']))
 # Independently bind each inherited selector's semantic hash.
 sem={k:x.get(k) for k in ('sector','selected_names','data_support','group_kinds')}
 assert objsha(sem)==x['selector_semantic_sha256']
 bysec[x['sector']].append((idx,x,frozenset(x['selected_names'])))
existing={(x['sector'],tuple(sorted(x['selected_names']))) for x in selectors}
domain_expected=sum(math.comb(len(bysec[k]),3) for k in bysec);domain_seen=0;weight_hist=Counter();eligible_triples=0;novel_triples=0
novel={} # exact result -> canonical first triple + multiplicity
first_overweight=None
for sector in ('Xerr','Zerr'):
 rows=bysec[sector]
 for (ia,sa,A),(ib,sb,B),(ic,sc,C) in combinations(rows,3):
  domain_seen+=1;R=A^B^C;w=len(R);weight_hist[w]+=1
  ids=(sa['mechanism_id'],sb['mechanism_id'],sc['mechanism_id'])
  if w>10 and first_overweight is None:first_overweight={'sector':sector,'input_ids':ids,'exact_symmetric_difference_weight':w,'selected_names':sorted(R)}
  if not (1<=w<=10):continue
  eligible_triples+=1;key=(sector,tuple(sorted(R)))
  if key in existing:continue
  novel_triples+=1
  if key not in novel:novel[key]={'sector':sector,'selected_names':list(key[1]),'weight':w,'first_input_ids':ids,'triple_multiplicity':0}
  novel[key]['triple_multiplicity']+=1
assert domain_seen==domain_expected
hits=[];miss_reason=Counter()
for key,row in sorted(novel.items()):
 v=model.verify_named_selection(sectors[row['sector']],row['selected_names'],10)
 assert v['weight']==row['weight'] and v['selected_names']==row['selected_names']
 row['candidate_exact_verification']=v
 row['selector_semantic_sha256']=objsha({'sector':row['sector'],'selected_names':row['selected_names'],'data_support':sorted(int(n.split(':')[1]) for n in row['selected_names'] if n.startswith('D:')),'group_kinds':{str(c):sorted(int(n.split(':')[2]) for n in row['selected_names'] if n.startswith('R:'+str(c)+':')) for c in sorted({int(n.split(':')[1]) for n in row['selected_names'] if n.startswith('R:')})}})
 if v['ok']:hits.append(row)
 else:
  miss_reason['nonzero_syndrome' if v['syndrome'] else 'logical_trivial' if not v['nontrivial'] else 'other']+=1
# Cross-sector exact ambiguity witness: same names have sector-dependent physical effect.
cross=None
for _,sx,A in bysec['Xerr']:
 for _,sz,B in bysec['Zerr']:
  names=sorted(A^B)
  if not names:continue
  vx=model.verify_named_selection(sectors['Xerr'],names,360);vz=model.verify_named_selection(sectors['Zerr'],names,360)
  if vx['net_support']!=vz['net_support'] or vx['syndrome']!=vz['syndrome'] or vx['logical_parities']!=vz['logical_parities']:
   cross={'x_input_id':sx['mechanism_id'],'z_input_id':sz['mechanism_id'],'symmetric_difference_names':names,'weight':len(names),'Xerr_effect':vx,'Zerr_effect':vz,'reason':'no sector-independent XOR semantics'};break
 if cross:break
assert cross is not None and first_overweight is not None
# Schedule-local validity counterexample for any retained term, if available.
schedule_counterexample=None
for hit in hits:
 for sel in selectors:
  alt=sel.get('source_times')
  if not alt or alt==times:continue
  altsec=builder.sectors(alt,lx,lz);v=model.verify_named_selection(altsec[hit['sector']],hit['selected_names'],10)
  if not v['ok']:
   schedule_counterexample={'retained_names':hit['selected_names'],'sector':hit['sector'],'valid_on_iteration136':hit['candidate_exact_verification'],'invalid_on_source_schedule_of':sel['mechanism_id'],'alternate_verification':v,'reason':'must encode a dynamic exact EFSSC predicate, not an unconditional global contradiction'};break
 if schedule_counterexample:break
# All hits are retained by the exact domain policy; no sampling/cap.
for j,h in enumerate(hits):h['proposed_mechanism_id']=f'r94-triple-{j:04d}-{h["sector"]}'
out={'schema':'circdist-round94-exact-triple-gf2-closure-v1','status':'PASS','strategy':'exact higher-order same-sector GF(2) closure of three distinct reviewed selectors','finite_domain':{'selector_count':234,'sector_counts':{k:len(v) for k,v in bysec.items()},'unordered_distinct_triples_expected':domain_expected,'unordered_distinct_triples_enumerated':domain_seen,'coverage_rule':'itertools.combinations over every three-element subset independently in each sector; equality of seen and binomial count proves finite-domain coverage','exact_location_symmetric_difference':True,'weight_cap':10},'counts':{'eligible_weight_1_to_10_triples':eligible_triples,'novel_eligible_triples_with_multiplicity':novel_triples,'unique_novel_eligible_results':len(novel),'exact_candidate_valid_results_retained':len(hits),'miss_reasons':dict(miss_reason),'result_weight_histogram_all_triples':dict(sorted(weight_hist.items()))},'soundness_theorem':{'statement':'For one CSS sector, XOR of the parity effects of three exact named fault sets equals the parity effect of their exact location symmetric difference. If that result contains at most ten distinct valid locations, its schedule-dependent detector-zero/logical-nonzero predicate is an ordinary exact EFSSC and is a conservative exclusion. Every three-selector result in the declared domain is enumerated.','proof_steps':['Each named location contributes one GF(2) support column in the frozen direct model.','Associativity and x xor x = 0 identify the three-set sum with exact symmetric difference of location names.','Same-sector restriction keeps all columns in one fixed physical/signature map.','Exact named-selection replay checks distinct valid columns, weight <= 10, detector syndrome zero, and nontrivial logical action.','The outer EFSSC encodes this validity as a schedule-dependent predicate; it does not assert universal validity or absence.']},'rejected_relaxation_counterexamples':{'cross_sector_xor':cross,'overweight_result':first_overweight,'schedule_globalization':schedule_counterexample},'retention_policy':'retain every unique novel result of weight <=10 that exact replay proves valid on iteration136; no heuristic, sample, or cap','retained_terms':hits,'limitations':['Covers exactly order-3 GF(2) closure of the 234-selector frontier, not arbitrary mechanisms or closure orders >=4.','A positive retained term only excludes schedules on which that exact EFSSC is valid; it proves no direct absence.','No claim of global exhaustion or D* narrowing follows.'],'seconds':round(time.time()-t0,6)}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','domain':domain_seen,'eligible_triples':eligible_triples,'unique_novel':len(novel),'retained':len(hits),'seconds':out['seconds']},sort_keys=True))
