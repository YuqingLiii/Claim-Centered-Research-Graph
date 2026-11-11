#!/usr/bin/env python3
"""Exact Round92 weight-9 slack synthesis for the frozen Gross direct-360 semantics.

This is a public proof-object generator.  It enumerates the stated finite candidate
families, computes exact selector domains by a meet-in-the-middle GF(2) factorization,
and checks one-atom cube relaxations over every local permutation.
"""
from pathlib import Path
from collections import Counter, defaultdict
from functools import reduce
from itertools import combinations, permutations, product
import argparse, gzip, hashlib, json, math, sys

MASK72=(1<<72)-1
BASE_IDS=("r90-i115-Zerr","r90-i119-Xerr")
BASE_LOC=((115,"Zerr"),(119,"Xerr"))
EXPECTED={
 "scheduler":"3a2b9380b0a9b0c248704f05ef45eaabd30cec98e8ddeed3c954785c9163a56f",
 "node":"4a19230bce6822d3afab50db16b2657ec0924b826b409b0c65d3c9fd57c10992",
 "review91":"72e36d7fdf33a4a4b868b01a5bcb9dadf22a45482bfbc2225aeead4bf9496f0d",
 "round90_root":"41ac5ad7f28895f09aae29a256d91aec241298ec7bfe0d1dec2e14709fa00ca7",
 "round90_payload":"545efe756a51190aaa8877e1d0d9fa1100da48aa213811b75a62a1f6a9b6c4d4",
 "iter124_source_file":"1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544",
 "iter124_source_semantic":"d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e",
 "iter124_cnf":"2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a",
}

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_file(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha_obj(o):return sha_bytes(canon(o))
def xor_all(xs):return reduce(int.__xor__,xs,0)
def load_json(p):
 b=Path(p).read_bytes()
 return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)

def parse_names(names):
 data=[]; groups=defaultdict(set)
 for name in names:
  p=name.split(':')
  if p[0]=='D':data.append(int(p[1]))
  else:
   assert p[0]=='R' and len(p)==3
   groups[int(p[1])].add(int(p[2]))
 assert len(names)==len(set(names))
 return sorted(data),dict(sorted(groups.items()))

def positions(respos,kinds):
 out=set()
 for k in kinds:out.symmetric_difference_update(respos[k])
 return tuple(sorted(out))

def factor_spec(source,sector,names):
 sd=source['sector_definitions'][sector]; qs=[int(x) for x in sd['qubit_signatures']]
 respos=[set(x) for x in source['residual_positions']]
 data,groups=parse_names(names)
 fixed=xor_all(qs[q] for q in data)
 factors=[]
 for c,kinds in groups.items():
  pos=positions(respos,kinds);row=tuple(sd['checks'][c]);k=len(pos)
  opts=[]
  for supp in combinations(row,k):
   opts.append({'support':tuple(sorted(supp)),'signature':xor_all(qs[q] for q in supp)})
  # All support choices are distinct as sets; retain duplicates in signature if any.
  factors.append({'check':c,'kinds':tuple(sorted(kinds)),'positions':pos,'row':row,
                  'options':opts,'permutations_per_support':math.factorial(k)*math.factorial(6-k)})
 return fixed,factors

def side_states(factors,fixed=0):
 # Counter preserves multiplicity if two support tuples share a signature.
 counter=Counter();witness={}
 if not factors:
  return Counter({fixed:1}),{fixed:[]}
 for chosen in product(*(f['options'] for f in factors)):
  sig=fixed^xor_all(x['signature'] for x in chosen)
  counter[sig]+=1
  witness.setdefault(sig,[{'check':f['check'],'support':list(x['support'])} for f,x in zip(factors,chosen)])
 return counter,witness

def construct_perm(factor,support):
 P=set(factor['positions']);S=set(support);row=set(factor['row'])
 a=iter(sorted(S));b=iter(sorted(row-S));out=[]
 for i in range(6):out.append(next(a) if i in P else next(b))
 assert set(out)==row
 return out

def exact_domain(source,sector,names,need_witness=True):
 fixed,factors=factor_spec(source,sector,names)
 cut=len(factors)//2
 L,Lw=side_states(factors[:cut],fixed)
 R,Rw=side_states(factors[cut:],0)
 lt=Counter();rt=Counter()
 for x,n in L.items():lt[x&MASK72]+=n
 for x,n in R.items():rt[x&MASK72]+=n
 support_tuples=sum(lt[k]*rt[k] for k in lt.keys()&rt.keys())-sum(L[x]*R.get(x,0) for x in L)
 assert support_tuples>=0
 mult=math.prod(f['permutations_per_support'] for f in factors)
 local_orders=support_tuples*mult
 witness=None
 if support_tuples and need_witness:
  bylow=defaultdict(list)
  for x in R:bylow[x&MASK72].append(x)
  pair=None
  for x in L:
   for y in bylow.get(x&MASK72,()):
    if x!=y:pair=(x,y);break
   if pair:break
  assert pair
  x,y=pair; choices=Lw[x]+Rw[y];choice_by={z['check']:z['support'] for z in choices}
  perms={str(f['check']):construct_perm(f,choice_by[f['check']]) for f in factors}
  total=x^y
  witness={'support_choices':choices,'local_permutations':perms,
           'signature_decimal':str(total),'syndrome_hex':hex(total&MASK72),
           'logical_bits':format(total>>72,'012b')[::-1]}
  assert (total&MASK72)==0 and (total>>72)!=0
 proof_payload={
  'sector':sector,'selected_names':list(names),'fixed_signature_decimal':str(fixed),
  'factors':[{'check':f['check'],'kinds':list(f['kinds']),'positions':list(f['positions']),
              'row':list(f['row']),'option_count':len(f['options']),
              'options_sha256':sha_obj([{'support':list(o['support']),'signature_decimal':str(o['signature'])} for o in f['options']]),
              'permutations_per_support':f['permutations_per_support']} for f in factors],
  'left_distinct_signatures':len(L),'right_distinct_signatures':len(R),
  'left_support_tuples':sum(L.values()),'right_support_tuples':sum(R.values()),
  'valid_support_tuples':support_tuples,'valid_local_order_tuples':local_orders,
 }
 proof_payload['factorized_proof_sha256']=sha_obj(proof_payload)
 return proof_payload,witness

def selection_object(source,sector,names,mechanism_id,origin,domain,witness):
 data,groups=parse_names(names)
 obj={
  'mechanism_id':mechanism_id,'source_iteration':'pre-124','sector':sector,
  'fault_count':len(names),'selected_names':list(names),'data_support':data,
  'group_kinds':{str(c):sorted(v) for c,v in groups.items()},
  'origin':origin,'source_schedule_sha256':None,
 }
 semantic={k:obj[k] for k in ('sector','selected_names','data_support','group_kinds')}
 obj['selector_semantic_sha256']=sha_obj(semantic)
 obj['exact_domain']={k:domain[k] for k in ('valid_support_tuples','valid_local_order_tuples','factorized_proof_sha256')}
 obj['domain_witness']=witness
 return obj

def valid_signature(source,sector,names,orders):
 sd=source['sector_definitions'][sector];qs=[int(x) for x in sd['qubit_signatures']];res=[set(x) for x in source['residual_positions']]
 data,groups=parse_names(names);v=xor_all(qs[q] for q in data)
 for c,kinds in groups.items():
  pos=positions(res,kinds);order=orders[c]
  v^=xor_all(qs[order[i]] for i in pos)
 return v,(v&MASK72)==0 and (v>>72)!=0

def verify_original(repo,r90,source):
 vendor=r90/'vendor/round80'
 sys.path[:0]=[str(vendor/'src/round63_src'),str(vendor/'src')]
 import model,round68_build as builder
 _,_,lx,lz=builder.load_context()
 rows=[]
 for (it,sec),mid in zip(BASE_LOC,BASE_IDS):
  direct_path=r90/f'iterations/iter{it}/direct/direct_verification.json'
  cand_path=r90/f'iterations/iter{it}/outer/candidate.json'
  direct=load_json(direct_path);cand=load_json(cand_path);m=direct['sectors'][sec]['mechanism']
  assert m['fault_count']==9 and m['selected_names']==next(x for x in source['selectors'] if x['mechanism_id']==mid)['selected_names']
  times=cand['compressed_times'];sectors=builder.sectors(times,lx,lz)
  check=model.verify_named_selection(sectors[sec],m['selected_names'],10);assert check['ok'] and check['weight']==9
  # Independent signature/order reconstruction.
  sd=source['sector_definitions'][sec];kind=sd['edge_kind'];orders={c:sorted(row,key=lambda q:times[f'{kind}:{c}:{q}']) for c,row in enumerate(sd['checks'])}
  sig,ok=valid_signature(source,sec,m['selected_names'],orders);assert ok
  logical=[(sig>>(72+i))&1 for i in range(12)]
  assert logical==m['canonical_replay']['logical_parities'] and (sig&MASK72)==0
  # Independent canonical and physical support replay.
  data,groups=parse_names(m['selected_names']);can=set(data);phys=set(data)
  for c,kinds in groups.items():
   order=orders[c]
   for k in kinds:
    for q in (order[i] for i in source['residual_positions'][k]):
     can.symmetric_difference_update([q])
    P={0:{2,3,4,5},1:{3,4,5},2:{4,5}}[k]
    for q in (order[i] for i in P):phys.symmetric_difference_update([q])
  assert sorted(can)==m['canonical_replay']['net_support'] and sorted(phys)==m['physical_net_support']
  assert m['physical_syndrome']==[] and m['physical_nontrivial'] and m['canonical_physical_parities_equal']
  rows.append({'mechanism_id':mid,'iteration':it,'sector':sec,'nine_columns':m['selected_names'],
   'check_selectors':sorted(groups),'qubit_selectors':data,
   'source_schedule_sha256':cand['compressed_schedule_sha256'],
   'direct_verification_file_sha256':sha_file(direct_path),'candidate_file_sha256':sha_file(cand_path),
   'mechanism_sha256':sha_obj(m),'terminal_residual':True,'syndrome_bits':'0'*72,
   'logical_bits_lsb_first':''.join(map(str,logical)),'canonical_support':sorted(can),'physical_support':sorted(phys),
   'physical_replay':True,'frozen_model_replay':True})
 return rows

def order_atom_tests(source,r90,original_rows):
 results=[];retained=[]
 for row in original_rows:
  mid=row['mechanism_id'];it=row['iteration'];sec=row['sector'];names=row['nine_columns']
  mech=load_json(r90/f'iterations/iter{it}/direct/direct_verification.json')['sectors'][sec]['mechanism']
  cand=load_json(r90/f'iterations/iter{it}/outer/candidate.json');times=cand['compressed_times']
  sd=source['sector_definitions'][sec];kind=sd['edge_kind'];data,groups=parse_names(names)
  source_orders={c:tuple(sorted(sd['checks'][c],key=lambda q:times[f'{kind}:{c}:{q}'])) for c in groups}
  atoms=mech['sound_outer_block']['atoms'];group_atoms=defaultdict(list)
  for idx,(a,op,b) in enumerate(atoms):
   assert op=='<' and a.split(':')[:2]==b.split(':')[:2]
   group_atoms[int(a.split(':')[1])].append((idx,int(a.split(':')[2]),int(b.split(':')[2])))
  # Full cube must fix the aggregate base signature at every participating check.
  full_counts={}
  for c,aa in group_atoms.items():
   perms=[p for p in permutations(sd['checks'][c]) if all(p.index(a)<p.index(b) for _,a,b in aa)]
   full_counts[str(c)]=len(perms)
   base_contrib={valid_signature(source,sec,names,{**source_orders,c:p})[0] for p in perms}
   # Since other source orders are fixed, full cube retains exact mechanism.
   assert len(base_contrib)==1 and next(iter(base_contrib))&MASK72==0 and next(iter(base_contrib))>>72
  for atom_index,(aa,op,bb) in enumerate(atoms):
   c=int(aa.split(':')[1]);a=int(aa.split(':')[2]);b=int(bb.split(':')[2]);remaining=[x for x in group_atoms[c] if x[0]!=atom_index]
   perms=[p for p in permutations(sd['checks'][c]) if all(p.index(x)<p.index(y) for _,x,y in remaining)]
   full=[p for p in permutations(sd['checks'][c]) if all(p.index(x)<p.index(y) for _,x,y in group_atoms[c])]
   allowed=[];uncovered=[];completion_count=0;base_count=0
   existing={f'R:{c}:{k}' for k in groups[c]}
   same=[f'R:{c}:{k}' for k in range(3) if f'R:{c}:{k}' not in existing]
   # Tested variable-selector family: base or base plus one residual on changed check.
   for p in perms:
    orders=dict(source_orders);orders[c]=p
    _,ok=valid_signature(source,sec,names,orders)
    chosen=list(names) if ok else None
    if ok:base_count+=1
    if chosen is None:
     for extra in same:
      trial=sorted(set(names)|{extra},key=lambda z:(z.split(':')[0],tuple(map(int,z.split(':')[1:]))))
      _,good=valid_signature(source,sec,trial,orders)
      if good:chosen=trial;completion_count+=1;break
    if chosen is None:uncovered.append(list(p))
    else:allowed.append({'permutation':list(p),'selected_names':chosen})
   broad=len(perms)>len(full);covered=not uncovered
   rec={'mechanism_id':mid,'deleted_atom_index':atom_index,'deleted_atom':[aa,op,bb],
        'check':c,'full_permutations':len(full),'relaxed_permutations':len(perms),
        'strictly_broader_local_cube':broad,'base_covered':base_count,'completion_covered':completion_count,
        'all_relaxed_permutations_covered':covered,'uncovered_count':len(uncovered),
        'first_uncovered_permutation':uncovered[0] if uncovered else None,
        'coverage_sha256':sha_obj(allowed),'retained':bool(broad and covered and completion_count)}
   results.append(rec)
   if rec['retained']:
    retained.append({'id':f'r92-{mid}-drop-atom-{atom_index}','sector':sec,
      'base_selected_names':names,'deleted_atom_index':atom_index,'remaining_atoms':[x for j,x in enumerate(atoms) if j!=atom_index],
      'coverage':allowed,'coverage_sha256':rec['coverage_sha256']})
 return results,retained

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 repo=a.repo.resolve();r90=repo/'circdist/artifacts/circdist_gross_proof_outer_round90_20260830'
 binds={
  'scheduler':sha_file(repo/'operations/circdist/SCHEDULER.yaml'),
  'node':sha_file(repo/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml'),
  'review91':sha_file(repo/'circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md'),
  'round90_root':sha_file(r90/'SHA256SUMS.txt'),'round90_payload':sha_file(r90/'PAYLOAD_SHA256SUMS.txt'),
  'iter124_source_file':sha_file(r90/'formulas/iter124/source.json.gz')}
 source=load_json(r90/'formulas/iter124/source.json.gz');binds['iter124_source_semantic']=source['semantic_payload_sha256']
 import subprocess,tempfile
 with tempfile.TemporaryDirectory(prefix='r92-cnfhash-') as td:
  out=Path(td)/'outer.cnf';subprocess.run(['gzip','-dc',str(r90/'formulas/iter124/outer.cnf.gz')],stdout=out.open('wb'),check=True)
  binds['iter124_cnf']=sha_file(out)
 assert binds==EXPECTED,(binds,EXPECTED)
 originals=verify_original(repo,r90,source)
 old_semantics={(x['sector'],tuple(x['selected_names'])) for x in source['selectors']}
 bases={x['mechanism_id']:x for x in source['selectors'] if x['mechanism_id'] in BASE_IDS};assert len(bases)==2
 tested=[];positive={}
 # Complete one-coordinate (one added direct-360 column) family: 351 per base.
 all_columns=[f'D:{q}' for q in range(144)]+[f'R:{c}:{k}' for c in range(72) for k in range(3)]
 completion_census={}
 for mid in BASE_IDS:
  base=bases[mid];B=set(base['selected_names']);sector=base['sector'];rows=[]
  for col in all_columns:
   if col in B:continue
   names=sorted(B|{col},key=lambda z:(z.split(':')[0],tuple(map(int,z.split(':')[1:]))))
   dom,wit=exact_domain(source,sector,names)
   rec={'family':'one_fault_completion','base':mid,'added_column':col,'sector':sector,'fault_count':10,
        'selected_names':names,**{k:dom[k] for k in ('valid_support_tuples','valid_local_order_tuples','factorized_proof_sha256')}}
   tested.append(rec);rows.append(rec)
   if dom['valid_local_order_tuples']:
    key=(sector,tuple(names));positive.setdefault(key,selection_object(source,sector,names,
      f'r92-{mid}-plus-{col.replace(":","_")}',f'round92_weight9_completion_of_{mid}',dom,wit))
  completion_census[mid]={'tested':len(rows),'nonempty':sum(x['valid_local_order_tuples']>0 for x in rows),
    'zero_domain':sum(x['valid_local_order_tuples']==0 for x in rows),
    'nonempty_columns':[x['added_column'] for x in rows if x['valid_local_order_tuples']>0],
    'support_domain_total':sum(x['valid_support_tuples'] for x in rows),
    'local_order_domain_total':sum(x['valid_local_order_tuples'] for x in rows)}
 # All nonempty proper deletion minors of each 9-column base (510 candidates each).
 minor_census={}
 for mid in BASE_IDS:
  base=bases[mid];cols=base['selected_names'];sector=base['sector'];n=0;pos=0
  for mask in range(1,(1<<9)-1):
   names=[cols[i] for i in range(9) if mask>>i&1];dom,wit=exact_domain(source,sector,names)
   n+=1
   rec={'family':'proper_deletion_minor','base':mid,'mask':mask,'sector':sector,'fault_count':len(names),
        'selected_names':names,**{k:dom[k] for k in ('valid_support_tuples','valid_local_order_tuples','factorized_proof_sha256')}}
   tested.append(rec)
   if dom['valid_local_order_tuples']:
    pos+=1;key=(sector,tuple(names));positive.setdefault(key,selection_object(source,sector,names,
      f'r92-{mid}-minor-{mask:03x}',f'round92_weight9_deletion_minor_of_{mid}',dom,wit))
  minor_census[mid]={'tested':n,'nonempty':pos,'zero_domain':n-pos}
 # Compatible ordinary unions across all prior selectors, complete filtered family <=10.
 union_filtered=[]
 for x,y in combinations(source['selectors'],2):
  if x['sector']!=y['sector']:continue
  names=sorted(set(x['selected_names'])|set(y['selected_names']),key=lambda z:(z.split(':')[0],tuple(map(int,z.split(':')[1:]))))
  if len(names)<=10:union_filtered.append((x,y,names))
 union_pos=0
 for x,y,names in union_filtered:
  dom,wit=exact_domain(source,x['sector'],names);rec={'family':'compatible_union','parents':[x['mechanism_id'],y['mechanism_id']],
   'sector':x['sector'],'fault_count':len(names),'selected_names':names,**{k:dom[k] for k in ('valid_support_tuples','valid_local_order_tuples','factorized_proof_sha256')}};tested.append(rec)
  if dom['valid_local_order_tuples']:
   union_pos+=1;positive.setdefault((x['sector'],tuple(names)),selection_object(source,x['sector'],names,
    f'r92-union-{x["mechanism_id"]}-{y["mechanism_id"]}','round92_compatible_union',dom,wit))
 # Pairwise GF(2) symmetric differences across all same-sector prior selectors, filtered 1..10.
 xor_filtered=[]
 for x,y in combinations(source['selectors'],2):
  if x['sector']!=y['sector']:continue
  names=sorted(set(x['selected_names'])^set(y['selected_names']),key=lambda z:(z.split(':')[0],tuple(map(int,z.split(':')[1:]))))
  if 1<=len(names)<=10:xor_filtered.append((x,y,names))
 xor_pos=0
 for x,y,names in xor_filtered:
  dom,wit=exact_domain(source,x['sector'],names);rec={'family':'pairwise_gf2','parents':[x['mechanism_id'],y['mechanism_id']],
   'sector':x['sector'],'fault_count':len(names),'selected_names':names,**{k:dom[k] for k in ('valid_support_tuples','valid_local_order_tuples','factorized_proof_sha256')}};tested.append(rec)
  if dom['valid_local_order_tuples']:
   xor_pos+=1;positive.setdefault((x['sector'],tuple(names)),selection_object(source,x['sector'],names,
    f'r92-gf2-{x["mechanism_id"]}-{y["mechanism_id"]}','round92_pairwise_gf2',dom,wit))
 # One source-cube order atom deletion, complete within the stated same-coordinate completion family.
 atom_tests,relaxed=order_atom_tests(source,r90,originals)
 # Ordinary retained selectors exclude semantic duplicates with the old registry.
 novel=[v for k,v in sorted(positive.items()) if k not in old_semantics]
 duplicates=[v for k,v in sorted(positive.items()) if k in old_semantics]
 # Semantic duplicate among new generated families is collapsed by dictionary key.
 result={
  'schema':'circdist-gross-round92-weight9-synthesis-v1','status':'PASS','bindings':binds,
  'theorem':'Every retained ordinary selector fixes at most ten distinct direct-360 columns. Its exact predicate is true exactly on the factorized local-order domain recorded here; on every such tuple the named canonical mechanism has zero 72-bit syndrome and a nonzero 12-bit logical vector. Replacing R:check:0 canonical positions {0,1} by physical suffix {2,3,4,5} changes support by the full same-sector stabilizer row, while kinds 1 and 2 agree, so the explicit named physical mechanism is valid throughout the same domain.',
  'factorized_domain_proof':{
   'recurrence':'For each participating check c, XOR residual position sets to P_c. Every |P_c|-subset of its six qubits occurs, each in |P_c|!(6-|P_c|)! local permutations. Split check factors L,R; count pairs with equal 72-bit syndrome and unequal full 84-bit signature. Exact support-domain count is sum_s L_low[s]R_low[s] - sum_v L_full[v]R_full[v]. Multiply by the per-support permutation factors.',
   'zero_domain_rule':'A zero exact count means only that this fixed candidate selector has empty local-order validity domain and is discarded; it is not absence evidence for schedules or other mechanisms.'},
  'original_weight9_reconstruction':originals,
  'completion_census':completion_census,'minor_census':minor_census,
  'compatible_union_census':{'prior_selectors':len(source['selectors']),'filtered_fault_count_le_10':len(union_filtered),'nonempty':union_pos},
  'pairwise_gf2_census':{'same_sector_pairs':sum(1 for x,y in combinations(source['selectors'],2) if x['sector']==y['sector']),
    'filtered_fault_count_1_to_10':len(xor_filtered),'nonempty':xor_pos},
  'order_atom_removal_census':{'tested':len(atom_tests),'strictly_broader':sum(x['strictly_broader_local_cube'] for x in atom_tests),
    'fully_covered_and_retained':len(relaxed),'failed_with_countertuple':sum(bool(x['uncovered_count']) for x in atom_tests)},
  'old_selector_count':len(source['selectors']),'generated_nonempty_semantic_terms':len(positive),
  'old_semantic_duplicates':len(duplicates),'retained_ordinary_selectors':novel,
  'retained_ordinary_selector_count':len(novel),'retained_relaxed_cube_count':len(relaxed),
  'retained_relaxed_cubes':relaxed,'atom_deletion_tests':atom_tests,
  'tested_candidate_count':len(tested),'tested_candidates_sha256':sha_obj(tested),
  'tested_family_rows':tested,
  'limitations':['Local-order domain nonemptiness alone does not assert extendability to a legal global frozen schedule. A separate exact frozen-CNF strict-expansion query is required before pre-outer installation.','No zero-domain result is interpreted as a global absence statement.','Pairwise GF(2) synthesis is tested only for the complete pair family among the 164 prior selectors; higher-arity GF(2) combinations are outside this finite test.'],
 }
 result['semantic_result_sha256']=sha_obj(result)
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:result[k] for k in ('status','completion_census','minor_census','compatible_union_census','pairwise_gf2_census','order_atom_removal_census','retained_ordinary_selector_count','retained_relaxed_cube_count','tested_candidate_count','semantic_result_sha256')},sort_keys=True))
if __name__=='__main__':main()
