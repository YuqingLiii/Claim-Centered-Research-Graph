#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,collections,gzip,hashlib,itertools,json,sys,time

ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path,required=True);ap.add_argument('--output-root',type=Path,required=True);a=ap.parse_args()
REPO=a.repo_root.resolve();OUT=a.output_root.resolve();OUT.mkdir(parents=True,exist_ok=True)
R69=REPO/'circdist/artifacts/circdist_gross_block_minimization_round69_20260829'
R71=REPO/'circdist/artifacts/circdist_gross_cegar_continuation_round71_20260829'
sys.path.insert(0,str(R71/'src/round63_src'))
import model as M

PERMS=list(itertools.permutations(range(6)));ALL=(1<<720)-1;SYNMASK=(1<<72)-1

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha_obj(o):return sha_bytes(canon(o))
def load(p):
 p=Path(p);b=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes();return json.loads(b)
def raw(p):
 p=Path(p);return gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes()
def parse_dimacs_bytes(b):
 nvars=nclauses=None;clauses=[]
 for line in b.decode().splitlines():
  s=line.strip()
  if not s or s.startswith('c'):continue
  if s.startswith('p '):
   _,fmt,nv,nc=s.split();assert fmt=='cnf';nvars=int(nv);nclauses=int(nc);continue
  vals=[int(x) for x in s.split()];assert vals[-1]==0 and 0 not in vals[:-1];clauses.append(vals[:-1])
 assert nvars is not None and len(clauses)==nclauses and max(abs(x) for c in clauses for x in c)<=nvars
 return nvars,clauses
def parse_assignment_bytes(b):
 status=None;lits=[]
 for line in b.decode(errors='replace').splitlines():
  if line.startswith('s '):status=line[2:].strip()
  if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
 assert status=='SATISFIABLE';a={abs(x):(x>0) for x in lits};assert len(a)==len(lits)
 return status,a
def failed_clauses(clauses,a):
 return [i for i,c in enumerate(clauses,1) if not any((lit>0)==a.get(abs(lit),False) for lit in c)]
def dump(p,o):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def bits(z):
 while z:
  b=z&-z;yield b.bit_length()-1;z^=b
def pc(z):return bin(z).count('1')
def syndrome(v,rows):return sum(((pc(v&h)&1)<<i) for i,h in enumerate(rows))
def logical(v,duals):return sum(((pc(v&h)&1)<<i) for i,h in enumerate(duals))
def signature(v,det,duals):return syndrome(v,det)|(logical(v,duals)<<72)
def valid_signature(s):return (s&SYNMASK)==0 and (s>>72)!=0
def edge(lab,c,q):return M.edge_key('X' if lab=='Xerr' else 'Z',c,q)
def atom_check(x):return int(x[0].split(':')[1])
def atom_holds(atom,pos):return pos[int(atom[0].split(':')[2])]<pos[int(atom[2].split(':')[2])]
def support_atoms(lab,c,row,k,s):
 S=set(M.bits(s));O=set(row)-S;out=[]
 if k==0:
  for q in sorted(S):
   for r in sorted(O):out.append((edge(lab,c,q),'<',edge(lab,c,r)))
 else:
  for q in sorted(O):
   for r in sorted(S):out.append((edge(lab,c,q),'<',edge(lab,c,r)))
 return tuple(sorted(out))
def physical_for(rowmask,k,s):return rowmask^s if k==0 else s

def sector_context(lab):
 if lab=='Xerr':return M.Xchecks,M.HZ,M.HX,LZ,PX
 return M.Zchecks,M.HX,M.HZ,LX,PZ

# Frozen weight-12 pools and independently derived quotient duals.
PX=M.expand_pool(R71/'src/inputs/w12X.txt',M.HX,M.HZ);PZ=M.expand_pool(R71/'src/inputs/w12Z.txt',M.HZ,M.HX)
LX=M.logical_basis(PX,M.HX);LZ=M.logical_basis(PZ,M.HZ)
assert len(PX)==len(PZ)==1884 and len(LX)==len(LZ)==12

# Read and independently replay all 48 sealed mechanisms.
mechanisms=[];needed=set();formula_bindings=[]
for it in range(6,30):
 cand=load(R71/f'cegar/iter{it}/candidate.json.gz');times={k:int(v) for k,v in cand['schedule_times'].items()}
 audit=M.audit_schedule(times,True);assert audit['ok'] and audit['global_interleaved'] and audit['edge_count']==864 and audit['overlaps']==648
 dv=load(R71/f'cegar/iter{it}/direct_verification.json.gz')
 assert dv['candidate_sha256']==cand['schedule_sha256']==sha_obj(times)
 for lab in ('Xerr','Zerr'):
  sec=dv['sectors'][lab];m=sec['mechanism'];assert sec['status']=='SATISFIABLE' and sec['all_dimacs_clauses_satisfied']
  # Independently parse the sealed unrestricted direct formula and the complete
  # solver assignment.  This does not trust the saved verifier result.
  cnf_bytes=raw(R71/f'cegar/iter{it}/direct360/{lab}.cnf.gz');solver_bytes=raw(R71/f'cegar/iter{it}/solver/{lab}.solver.log.gz')
  nvars,clauses=parse_dimacs_bytes(cnf_bytes);status,assignment=parse_assignment_bytes(solver_bytes)
  assert len(assignment)==nvars==sec['assignment_variables'] and not failed_clauses(clauses,assignment)
  selected_indices=[j for j in range(360) if assignment[j+1]]
  assert selected_indices==m['selected_indices'] and len(selected_indices)==m['fault_count']<=10
  # Rebuild every selected elementary column from the schedule/model, then
  # compare it to the sealed raw witness before the independent XOR replay.
  logical_duals=LZ if lab=='Xerr' else LX;sector_model=M.Sector(lab,times,logical_duals)
  assert [sector_model.columns[j].name for j in selected_indices]==m['selected_names']
  independent_effective=sector_model.verify_effective_selection(selected_indices,10);assert independent_effective['ok']
  assert independent_effective==m['canonical_replay']
  rows,det,stabs,duals,pool=sector_context(lab);D=0;cv=0;pv=0;selected=[];group=collections.defaultdict(list)
  for f in m['faults']:
   selected.append(f['column_name'])
   if f['elementary_fault']=='data_singleton':
    q=int(f['column_name'].split(':')[1]);assert f['data_support']==[q];D^=1<<q;cv^=1<<q;pv^=1<<q
   else:
    c=f['check'];k=f['residual_kind'];order=tuple(f['within_check_order_qubits']);assert sorted(order)==rows[c]
    ot=tuple(times[edge(lab,c,q)] for q in order);assert tuple(sorted(ot))==ot and list(ot)==f['within_check_times']
    s=M.mask(order[j] for j in M.RES_POS[k]);p=M.mask(order[j] for j in M.PHYS_POS[k])
    assert M.bits(s)==f['canonical_representative_support'] and M.bits(p)==f['physical_suffix_support']
    cv^=s;pv^=p;group[c].append(k);needed.add((lab,c))
  assert len(selected)==m['fault_count']<=10 and selected==m['selected_names']
  assert M.bits(cv)==m['canonical_replay']['net_support'] and M.bits(pv)==m['physical_net_support']
  cs=syndrome(cv,det);ps=syndrome(pv,det);cl=logical(cv,duals);pl=logical(pv,duals)
  assert cs==ps==0 and cl==pl!=0 and not M.inspan(cv,stabs) and not M.inspan(pv,stabs)
  calc_atoms=[]
  for f in m['faults']:
   if f['elementary_fault']=='ancilla_hook_suffix':calc_atoms.extend(support_atoms(lab,f['check'],rows[f['check']],f['residual_kind'],M.mask(f['canonical_representative_support'])))
  calc_atoms=tuple(sorted(set(calc_atoms)));stored=tuple(tuple(x) for x in m['sound_outer_block']['atoms'])
  assert calc_atoms==stored and M.block_holds(times,stored)
  mid=f'iter{it}-{lab}'
  formula_bindings.append({'mechanism_id':mid,'candidate_sha256':cand['schedule_sha256'],'cnf_sha256':sha_bytes(cnf_bytes),'cnf_variables':nvars,'cnf_clauses':len(clauses),'solver_log_sha256':sha_bytes(solver_bytes),'solver_status':status,'solver_assignment_variables':len(assignment),'assignment_sha256':sha_obj(sorted((v,b) for v,b in assignment.items())),'selected_indices':selected_indices,'selected_names':selected,'all_dimacs_clauses_satisfied_independently':True,'sealed_mechanism_sha256':sha_obj(m)})
  mechanisms.append({'mechanism_id':mid,'iteration':it,'sector':lab,'candidate_sha256':cand['schedule_sha256'],'times':times,'fault_count':m['fault_count'],'data_mask':D,'data_support':M.bits(D),'selected_names':selected,'group_kinds':{str(c):sorted(v) for c,v in sorted(group.items())},'source_atoms':[list(x) for x in stored],'source_atom_count':len(stored),'source_orders':{str(c):next(f['within_check_order_qubits'] for f in m['faults'] if f.get('check')==c) for c in sorted(group)},'canonical_support':M.bits(cv),'physical_support':M.bits(pv),'canonical_weight':pc(cv),'physical_weight':pc(pv),'logical_parities':[(cl>>j)&1 for j in range(12)],'sealed_mechanism_sha256':sha_obj(m)})
assert len(mechanisms)==48 and len(needed)==113
structural_pair_keys={(m['sector'],aa,bb) for m in mechanisms for aa,bb in itertools.combinations(sorted(int(x) for x in m['group_kinds']),2)}
assert len(structural_pair_keys)==607

# All 720 local orders, supports, physical suffixes, unary completions, and comparison masks.
cats={};catalog_public=[]
def build_cat(lab,c,public=True):
 key=(lab,c)
 if key in cats:return cats[key]
 rows,det,stabs,duals,pool=sector_context(lab);row=rows[c];rowmask=M.mask(row);orders=[];cmpm={};option_masks=collections.defaultdict(int);unary=0
 for oi,pidx in enumerate(PERMS):
  order=tuple(row[j] for j in pidx);opts=[]
  for k,(rp,pp) in enumerate(zip(M.RES_POS,M.PHYS_POS)):
   s=M.mask(order[j] for j in rp);ph=M.mask(order[j] for j in pp);cs=signature(s,det,duals);ps=signature(ph,det,duals);assert cs==ps
   option_masks[(k,s)]|=1<<oi;opts.append({'kind':k,'canonical_support':M.bits(s),'physical_support':M.bits(ph),'signature_hex':hex(cs)})
  sm=M.mask(order[j] for j in M.RES_POS[1]);vi=next((j for j,V in enumerate(pool) if V&sm==sm),None)
  uw=None
  if vi is not None:
   V=pool[vi];D=V^sm;assert pc(D)==9 and syndrome(V,det)==0 and logical(V,duals)!=0 and not M.inspan(V,stabs)
   uw={'pool_index':vi,'logical_support':M.bits(V),'singleton_support':M.bits(D),'fault_weight':10};unary|=1<<oi
  orders.append({'order_id':oi,'qubits':list(order),'options':opts,'unary_witness':uw})
 for q in row:
  for r in row:
   if q==r:continue
   z=0
   for oi,pidx in enumerate(PERMS):
    order=tuple(row[j] for j in pidx)
    if order.index(q)<order.index(r):z|=1<<oi
   cmpm[(edge(lab,c,q),'<',edge(lab,c,r))]=z
 assert pc(unary)==360
 cat={'sector':lab,'check':c,'row':row,'rowmask':rowmask,'orders':orders,'option_masks':dict(option_masks),'comparison_masks':cmpm,'unary_mask':unary,'good_mask':ALL^unary}
 cats[key]=cat
 if public:catalog_public.append({'sector':lab,'check':c,'row':row,'orders':orders,'unary_mask_hex':hex(unary),'good_mask_hex':hex(ALL^unary),'unary_bad_order_count':360,'unary_good_order_count':360})
 return cat
for lab,c in sorted(needed):build_cat(lab,c)
assert len(catalog_public)==113 and sum(len(x['orders']) for x in catalog_public)==81360

def order_mask(cat,atoms):
 z=ALL
 for x in atoms:z&=cat['comparison_masks'][tuple(x)]
 return z

def masks_for_atoms(lab,atoms,checks=None):
 by=collections.defaultdict(list)
 for x in atoms:by[atom_check(x)].append(tuple(x))
 cs=sorted(checks if checks is not None else by)
 return {c:order_mask(build_cat(lab,c,public=False),by.get(c,[])) for c in cs}

# Exact multi-check factorization. Each local order maps to one explicit canonical/physical contribution.
def multi_domains(mech,atoms):
 lab=mech['sector'];rows,det,stabs,duals,pool=sector_context(lab);checks=sorted(int(x) for x in mech['group_kinds']);masks=masks_for_atoms(lab,atoms,checks);domains=[];local={}
 for c in checks:
  cat=build_cat(lab,c,public=False);kinds=mech['group_kinds'][str(c)];sig_masks=collections.defaultdict(int);records=[]
  for rec in cat['orders']:
   cv=pv=0
   for k in kinds:
    z=rec['options'][k];cv^=M.mask(z['canonical_support']);pv^=M.mask(z['physical_support'])
   cs=signature(cv,det,duals);ps=signature(pv,det,duals);assert cs==ps
   sig_masks[cs]|=1<<rec['order_id'];records.append({'order_id':rec['order_id'],'canonical_support':M.bits(cv),'physical_support':M.bits(pv),'signature_hex':hex(cs)})
  dom=[(s,z&masks[c]) for s,z in sorted(sig_masks.items()) if z&masks[c]];assert dom;domains.append((c,dom));local[str(c)]={'selected_kinds':kinds,'allowed_mask_hex':hex(masks[c]),'allowed_count':pc(masks[c]),'signature_classes':[{'signature_hex':hex(s),'order_mask_hex':hex(z),'allowed_order_count':pc(z&masks[c])} for s,z in sorted(sig_masks.items()) if z&masks[c]],'per_order':records}
 const=signature(mech['data_mask'],det,duals);return checks,masks,domains,local,const

def multi_check(mech,atoms,want_witness=False):
 checks,masks,domains,local,const=multi_domains(mech,atoms);dp={const:()};maxstates=1
 for c,dom in domains:
  nd={}
  for s,w in dp.items():
   for x,z in dom:
    ns=s^x
    if ns not in nd:nd[ns]=w+(next(bits(z)),)
  dp=nd;maxstates=max(maxstates,len(dp))
 bad=sorted(s for s in dp if not valid_signature(s));wit=None
 if bad:
  s=bad[0];wit={'final_signature_hex':hex(s),'syndrome_support':M.bits(s&SYNMASK),'logical_parities':[((s>>72)>>j)&1 for j in range(12)],'order_ids':{str(c):o for c,o in zip(checks,dp[s])},'orders':{str(c):build_cat(mech['sector'],c,False)['orders'][o]['qubits'] for c,o in zip(checks,dp[s])},'interpretation':'selected mechanism invalid on this tuple only; not global physical absence'}
 return {'sound':not bad,'checks':checks,'masks':masks,'domains':domains,'local':local,'constant_signature_hex':hex(const),'reachable_signature_count':len(dp),'max_layer_state_count':maxstates,'invalid_signature_count':len(bad),'invalid_witness':wit}

def minimize_multi(mech,reverse):
 cur=[tuple(x) for x in mech['source_atoms']];seq=list(reversed(cur)) if reverse else list(cur)
 base=multi_check(mech,cur);assert base['sound']
 for x in seq:
  if x not in cur:continue
  trial=cur.copy();trial.remove(x)
  if multi_check(mech,trial)['sound']:cur=trial
 final=multi_check(mech,cur);assert final['sound'];controls=[]
 for x in cur:
  trial=cur.copy();trial.remove(x);q=multi_check(mech,trial);assert not q['sound'] and q['invalid_witness']
  controls.append({'removed_atom':list(x),'exposed_tuple':q['invalid_witness'],'control_scope':'selected-mechanism relation only; no global absence'})
 counts={str(c):pc(final['masks'][c]) for c in final['checks']};total=1
 for n in counts.values():total*=n
 return {'relation_kind':'multi_check_exact_selected_mechanism','mechanism_id':mech['mechanism_id'],'sector':mech['sector'],'checks':final['checks'],'atoms':[list(x) for x in sorted(cur)],'atom_count':len(cur),'allowed_order_counts':counts,'covered_tuple_count':total,'reachable_signature_count':final['reachable_signature_count'],'max_layer_state_count':final['max_layer_state_count'],'constant_signature_hex':final['constant_signature_hex'],'allowed_order_masks_hex':{str(c):hex(final['masks'][c]) for c in final['checks']},'mechanism_selector':{'selected_names':mech['selected_names'],'data_support':mech['data_support'],'per_check_selected_kinds':mech['group_kinds'],'physical_rule':'for each tuple/order and kind k, use PHYS_POS[k]; XOR with fixed data support','per_check_order_table_embedded':True},'deletion_controls':controls,'direction':'reverse' if reverse else 'forward','soundness':'all reachable GF(2) syndrome/logical signatures have syndrome zero and logical quotient nonzero'}

multi_relations=[];multi_candidates=[]
for idx,mech in enumerate(mechanisms):
 # Local table is saved once with the forward relation; reverse refers by mechanism id.
 terms=[]
 for rev in (False,True):
  t=minimize_multi(mech,rev);terms.append(t);multi_candidates.append(t)
 checks,masks,domains,local,const=multi_domains(mech,[tuple(x) for x in mech['source_atoms']])
 multi_relations.append({'mechanism_id':mech['mechanism_id'],'sector':mech['sector'],'fault_count':mech['fault_count'],'participating_checks':checks,'source_atom_count':mech['source_atom_count'],'source_selected_names':mech['selected_names'],'source_data_support':mech['data_support'],'source_canonical_support':mech['canonical_support'],'source_physical_support':mech['physical_support'],'source_logical_parities':mech['logical_parities'],'source_raw_replay_passed':True,'local_order_contributions':local,'minimized_terms':terms})
 print('MULTI',idx+1,'/48',mech['mechanism_id'],'checks',len(checks),'atoms',[(x['atom_count'],x['covered_tuple_count']) for x in terms],flush=True)

# Explicit positive weight-14 completion pool: one-stabilizer transforms, sealed round69 positives, and new raw source weight-14 supports.
w14={};w14_sources={}
for lab in ('Xerr','Zerr'):
 rows,det,stabs,duals,pool=sector_context(lab);z={}
 for vi,V in enumerate(pool):
  for hi,h in enumerate(stabs):
   W=V^h
   if pc(W)==14:z.setdefault(W,{'source':'w12_xor_stabilizer','w12_pool_index':vi,'stabilizer_check':hi})
 old=load(R69/'classification/pair_classification.json.gz')
 for p in old['pairs']:
  if p['sector']!=lab:continue
  for c in p['positive_residual_configurations']:
   if c['source']=='weight14_direct':z.setdefault(M.mask(c['logical_support']),{'source':'round69_positive_weight14','round69_pair':[p['a'],p['b']]})
 for mech in mechanisms:
  if mech['sector']==lab and mech['canonical_weight']==14:z.setdefault(M.mask(mech['canonical_support']),{'source':'round71_raw_weight14','mechanism_id':mech['mechanism_id']})
 for W,src in z.items():assert syndrome(W,det)==0 and logical(W,duals)!=0 and not M.inspan(W,stabs)
 w14[lab]=sorted(z);w14_sources[lab]=z
 print('W14',lab,len(z),flush=True)

# Seed pair configurations use source-selected residuals only; no negative result is used.
pair_seed=collections.defaultdict(dict);mech_pair_keys=collections.defaultdict(set);seed_attempts=[]
for mech in mechanisms:
 lab=mech['sector'];rows,det,stabs,duals,pool=sector_context(lab);faults=[]
 # Rebuild selected option supports from source order and selected kinds.
 for cs,kinds in mech['group_kinds'].items():
  c=int(cs);order=mech['source_orders'][cs]
  for k in kinds:faults.append((c,k,M.mask(order[j] for j in M.RES_POS[k])))
 positives=0
 for (c1,k1,s1),(c2,k2,s2) in itertools.combinations(faults,2):
  if c1==c2:continue
  if c1>c2:c1,k1,s1,c2,k2,s2=c2,k2,s2,c1,k1,s1
  rr=s1^s2;best=None
  for vi,V in enumerate(pool):
   cost=2+pc(V^rr)
   if cost<=10:
    cand=(cost,0,V,{'source':'weight12_pool','pool_index':vi})
    if best is None or cand[:3]<best[:3]:best=cand
  if best is None and pc(rr)==6:
   for W in w14[lab]:
    if W&rr==rr:
     cand=(2+pc(W^rr),1,W,dict(w14_sources[lab][W]))
     if cand[0]<=10 and (best is None or cand[:3]<best[:3]):best=cand
  attempt={'mechanism_id':mech['mechanism_id'],'pair':[c1,c2],'kinds':[k1,k2],'supports':[M.bits(s1),M.bits(s2)],'positive_completion_found':best is not None}
  if best is not None:
   cost,rank,V,src=best;D=V^rr;key=(lab,c1,c2);ck=(k1,s1,k2,s2,V)
   conf={'sector':lab,'a':c1,'b':c2,'a_kind':k1,'b_kind':k2,'a_support':M.bits(s1),'b_support':M.bits(s2),'logical_support':M.bits(V),'logical_weight':pc(V),'singleton_support':M.bits(D),'fault_weight':cost,'source':src,'source_mechanisms':[mech['mechanism_id']]}
   if ck in pair_seed[key]:pair_seed[key][ck]['source_mechanisms']=sorted(set(pair_seed[key][ck]['source_mechanisms']+[mech['mechanism_id']]))
   else:pair_seed[key][ck]=conf
   mech_pair_keys[mech['mechanism_id']].add(key);positives+=1;attempt['source']=src;attempt['fault_weight']=cost
  seed_attempts.append(attempt)
 mech['positive_selected_pair_count']=positives

# Conservative pair relations and deletion-minimal rectangles from explicit configurations.
def rect_sound(A,B,truth):return all((B & (ALL^truth[i]))==0 for i in bits(A))
def minimize_pair(lab,ca,cb,truth,conf,reverse):
 base=list(support_atoms(lab,ca['check'],ca['row'],conf['a_kind'],M.mask(conf['a_support']))+support_atoms(lab,cb['check'],cb['row'],conf['b_kind'],M.mask(conf['b_support'])))
 cur=list(base);seq=list(reversed(base)) if reverse else list(base)
 for x in seq:
  if x not in cur:continue
  trial=cur.copy();trial.remove(x);by=collections.defaultdict(list)
  for y in trial:by[atom_check(y)].append(y)
  A=order_mask(ca,by[ca['check']]);B=order_mask(cb,by[cb['check']])
  if rect_sound(A,B,truth):cur=trial
 by=collections.defaultdict(list)
 for y in cur:by[atom_check(y)].append(y)
 A=order_mask(ca,by[ca['check']]);B=order_mask(cb,by[cb['check']]);assert rect_sound(A,B,truth)
 controls=[]
 for x in cur:
  trial=cur.copy();trial.remove(x);tb=collections.defaultdict(list)
  for y in trial:tb[atom_check(y)].append(y)
  A2=order_mask(ca,tb[ca['check']]);B2=order_mask(cb,tb[cb['check']]);wit=None
  for i in bits(A2):
   z=B2&(ALL^truth[i])
   if z:wit=(i,next(bits(z)));break
  assert wit is not None
  controls.append({'removed_atom':list(x),'exposed_a_order_id':wit[0],'exposed_b_order_id':wit[1],'exposed_a_order':ca['orders'][wit[0]]['qubits'],'exposed_b_order':cb['orders'][wit[1]]['qubits'],'control_scope':'conservative positive pair library only; no global absence'})
 ag=A&ca['unary_mask'];ggA=A&ca['good_mask'];bg=B&cb['unary_mask'];ggB=B&cb['good_mask'];paircov=sum(pc(ggB & truth[i]) for i in bits(ggA));counts={'total':pc(A)*pc(B),'a_unary':pc(ag)*pc(B),'b_unary_after_a_good':pc(ggA)*pc(bg),'explicit_pair_after_both_good':paircov}
 assert sum(counts[k] for k in ('a_unary','b_unary_after_a_good','explicit_pair_after_both_good'))==counts['total']
 return {'relation_kind':'positive_pair_rectangle','sector':lab,'a':ca['check'],'b':cb['check'],'atoms':[list(x) for x in sorted(cur)],'atom_count':len(cur),'a_order_mask_hex':hex(A),'b_order_mask_hex':hex(B),'a_order_count':pc(A),'b_order_count':pc(B),'covered_tuple_count':counts['total'],'coverage_partition':counts,'mechanism_selector':{'priority':['a_unary_witness','b_unary_witness','first_explicit_pair_configuration'],'pair_configuration_source_mechanisms':conf['source_mechanisms'],'seed_configuration_sha256':sha_obj(conf)},'seed_source_mechanisms':conf['source_mechanisms'],'seed_configuration':conf,'deletion_controls':controls,'direction':'reverse' if reverse else 'forward'}

pair_relations=[];pair_candidates=[]
for pi,key in enumerate(sorted(structural_pair_keys)):
 lab,aa,bb=key;ca=build_cat(lab,aa,False);cb=build_cat(lab,bb,False);confs=list(pair_seed.get(key,{}).values());new=[0]*720
 for conf in confs:
  s1=M.mask(conf['a_support']);s2=M.mask(conf['b_support']);V=M.mask(conf['logical_support']);D=M.mask(conf['singleton_support']);assert s1^s2^D==V and conf['fault_weight']==2+pc(D)<=10
  rows,det,stabs,duals,pool=sector_context(lab);PV=physical_for(ca['rowmask'],conf['a_kind'],s1)^physical_for(cb['rowmask'],conf['b_kind'],s2)^D
  assert syndrome(V,det)==syndrome(PV,det)==0 and logical(V,duals)==logical(PV,duals)!=0 and not M.inspan(V,stabs) and not M.inspan(PV,stabs)
  A=ca['option_masks'][(conf['a_kind'],s1)]&ca['good_mask'];B=cb['option_masks'][(conf['b_kind'],s2)]&cb['good_mask']
  for i in bits(A):new[i]|=B
 truth=[ALL if ((ca['unary_mask']>>i)&1) else (cb['unary_mask']|new[i]) for i in range(720)]
 terms=[]
 for conf in confs:
  for rev in (False,True):terms.append(minimize_pair(lab,ca,cb,truth,conf,rev))
 pair_candidates.extend(terms)
 pair_relations.append({'sector':lab,'a':aa,'b':bb,'positive_configurations':confs,'positive_configuration_count':len(confs),'truth_rows_hex':[hex(z) for z in truth],'explicit_good_good_rows_hex':[hex(z) for z in new],'truth_cell_count':sum(pc(z) for z in truth),'explicit_good_good_cell_count':sum(pc(z) for z in new),'raw_replay_count':len(confs),'generated_terms':terms})
 if confs or (pi+1)%50==0 or pi+1==len(structural_pair_keys):print('PAIR',pi+1,'/',len(structural_pair_keys),lab,aa,bb,'configs',len(confs),'terms',len(terms),flush=True)

# Every source mechanism either has a positive pair certificate or remains covered only by its exact multi-check relation/dynamic block.
for mech in mechanisms:mech['generalization_disposition']='pair_and_multi_positive' if mech_pair_keys[mech['mechanism_id']] else 'multi_check_exact_positive_only_pair_library_miss'

# Old semantic term catalog plus new semantic deduplication/dominance.
old_obj=load(R69/'classification/pair_classification.json.gz');old_terms=[]
for p in old_obj['pairs']:
 lab,aa,bb=p['sector'],p['a'],p['b'];ca=build_cat(lab,aa,False);cb=build_cat(lab,bb,False)
 for j,t in enumerate(p['deletion_minimal_terms']):
  ats=[tuple(x) for x in t['atoms']];ms=masks_for_atoms(lab,ats,[aa,bb]);old_terms.append({'id':f'r69-{lab}-{aa}-{bb}-{j}','sector':lab,'atoms':ats,'masks':ms,'checks':tuple(c for c in (aa,bb) if ms[c]!=ALL)})
assert len(old_terms)==4740

def candidate_normalize(t,idx):
 lab=t['sector'];ats=[tuple(x) for x in t['atoms']];checks=sorted(set(atom_check(x) for x in ats));ms=masks_for_atoms(lab,ats,checks);key=(lab,tuple((c,ms[c]) for c in checks if ms[c]!=ALL));z=dict(t);z['_index']=idx;z['_atoms']=ats;z['_masks']=ms;z['_checks']=tuple(c for c in checks if ms[c]!=ALL);z['_key']=key;z['_coverage']=t['covered_tuple_count'];return z
new_raw=[candidate_normalize(t,i) for i,t in enumerate(pair_candidates+multi_candidates)]
old_key_map=collections.defaultdict(list)
for t in old_terms:old_key_map[(t['sector'],tuple((c,t['masks'][c]) for c in t['checks']))].append(t['id'])
# Internal semantic duplicates first.
unique=[];keyfirst={};duplicate_records=[]
for t in new_raw:
 if t['_key'] in old_key_map:
  duplicate_records.append({'new_index':t['_index'],'classification':'duplicate_old','old_ids':old_key_map[t['_key']]});continue
 if t['_key'] in keyfirst:
  duplicate_records.append({'new_index':t['_index'],'classification':'duplicate_new','canonical_new_index':keyfirst[t['_key']]['_index']});continue
 keyfirst[t['_key']]=t;unique.append(t)

def dominates(u,v):
 # Region(v) subset Region(u); absent check means ALL.
 if u['sector']!=v['sector']:return False
 for c in set(u['masks'])|set(v['masks']):
  um=u['masks'].get(c,ALL);vm=v['masks'].get(c,ALL)
  if vm & (ALL^um):return False
 return True
old_simple=[{'id':t['id'],'sector':t['sector'],'masks':t['masks'],'checks':t['checks']} for t in old_terms]
dom_records=[];retained=[]
for t in unique:
 ds=[u['id'] for u in old_simple if set(u['checks']).issubset(set(t['_checks'])) and dominates(u,{'sector':t['sector'],'masks':t['_masks']})]
 if ds:dom_records.append({'new_index':t['_index'],'classification':'dominated_old','dominator_ids':ds[:20],'dominator_count':len(ds)});continue
 # exact proper dominance by another unique new term
 ds2=[]
 for u in unique:
  if u is t or u['_key']==t['_key']:continue
  if set(u['_checks']).issubset(set(t['_checks'])) and dominates({'sector':u['sector'],'masks':u['_masks']},{'sector':t['sector'],'masks':t['_masks']}):ds2.append(u['_index'])
 if ds2:dom_records.append({'new_index':t['_index'],'classification':'dominated_new','dominator_new_indices':sorted(ds2)[:20],'dominator_count':len(ds2)});continue
 retained.append(t)
# Stable installed term IDs and source mappings.
retained.sort(key=lambda t:(t['sector'],t['_checks'],canon(t['atoms'])))
retained_public=[]
for j,t in enumerate(retained):
 z={k:v for k,v in t.items() if not k.startswith('_')};z['term_id']=f'r72-generalized-{j:04d}';z['semantic_key_sha256']=sha_obj([t['sector'],[(c,hex(t['_masks'][c])) for c in t['_checks']]]);retained_public.append(z);t['term_id']=z['term_id']

# Every one of the 48 source tuples is covered by at least one retained generalized term.
for mech in mechanisms:
 positions={int(c):{q:i for i,q in enumerate(order)} for c,order in mech['source_orders'].items()}
 cover=[]
 for t in retained_public:
  if t['sector']!=mech['sector']:continue
  ats=[tuple(x) for x in t['atoms']]
  if all(atom_check(x) in positions and atom_holds(x,positions[atom_check(x)]) for x in ats):cover.append(t['term_id'])
 mech['covering_retained_term_ids']=cover
 assert cover,(mech['mechanism_id'],'no retained generalized cover')

# Exact library-relative coverage difference for pair terms; multi terms report exact total and domination status.
old_pair_rows={}
for p in old_obj['pairs']:
 key=(p['sector'],p['a'],p['b']);rows=[0]*720
 for t in p['deletion_minimal_terms']:
  ats=[tuple(x) for x in t['atoms']];ms=masks_for_atoms(p['sector'],ats,[p['a'],p['b']]);A=ms[p['a']];B=ms[p['b']]
  for i in bits(A):rows[i]|=B
 old_pair_rows[key]=rows
pair_diff=[]
for key in sorted(set((t['sector'],t.get('a'),t.get('b')) for t in retained_public if t['relation_kind']=='positive_pair_rectangle')):
 lab,aa,bb=key;newrows=[0]*720
 for t in retained_public:
  if t['relation_kind']=='positive_pair_rectangle' and (t['sector'],t['a'],t['b'])==key:
   A=int(t['a_order_mask_hex'],16);B=int(t['b_order_mask_hex'],16)
   for i in bits(A):newrows[i]|=B
 oldrows=old_pair_rows.get(key,[0]*720);newcount=sum(pc(z) for z in newrows);diff=sum(pc(newrows[i]&(ALL^oldrows[i])) for i in range(720));overlap=newcount-diff
 pair_diff.append({'sector':lab,'a':aa,'b':bb,'retained_new_union_cells':newcount,'covered_by_same_pair_old_union':overlap,'library_relative_new_cells':diff,'scope':'720x720 local pair domain; old terms involving outside checks are not unconditional on this domain'})

counts=collections.Counter(r['classification'] for r in duplicate_records+dom_records)
dedup={'schema':'round72-semantic-dedup-ledger-v1','old_reviewed_terms':4740,'new_raw_term_candidates':len(new_raw),'new_pair_candidates':len(pair_candidates),'new_multi_check_candidates':len(multi_candidates),'duplicate_old':counts['duplicate_old'],'duplicate_new':counts['duplicate_new'],'dominated_old':counts['dominated_old'],'dominated_new':counts['dominated_new'],'retained_new_terms':len(retained_public),'merged_installed_generalized_terms':4740+len(retained_public),'duplicate_records':duplicate_records,'dominance_records':dom_records,'pair_domain_coverage_difference':pair_diff,'old_library_preserved_verbatim':True,'semantic_definition':'finite local-order masks; U dominates V iff every local tuple satisfying V also satisfies U; deletion controls remain library-relative'}

# Verify source disposition: pair-backed mechanisms have at least one seed; all 48 have two exact multi terms.
assert len(multi_candidates)==96
assert sum(bool(mech_pair_keys[m['mechanism_id']]) for m in mechanisms)+sum(not mech_pair_keys[m['mechanism_id']] for m in mechanisms)==48
summary={'schema':'round72-round71-generalization-summary-v1','status':'PASS','round71_mechanisms':48,'formula_assignment_raw_replays':48,'participating_catalogs':113,'local_orders_per_catalog':720,'local_order_records':113*720,'structural_pair_projections':len(structural_pair_keys),'factorized_pair_relations':len(pair_relations),'factorized_pair_order_cells':len(pair_relations)*720*720,'positive_pair_relations':sum(bool(x['positive_configuration_count']) for x in pair_relations),'unary_only_pair_relations':sum(not x['positive_configuration_count'] for x in pair_relations),'positive_pair_configurations':sum(x['positive_configuration_count'] for x in pair_relations),'positive_pair_cells':sum(x['explicit_good_good_cell_count'] for x in pair_relations),'multi_check_exact_relations':48,'multi_check_terms_generated':96,'pair_terms_generated':len(pair_candidates),'mechanisms_with_positive_pair_generalization':sum(bool(mech_pair_keys[m['mechanism_id']]) for m in mechanisms),'mechanisms_without_positive_pair_generalization':sum(not mech_pair_keys[m['mechanism_id']] for m in mechanisms),'positive_pair_library_miss_ids':[m['mechanism_id'] for m in mechanisms if not mech_pair_keys[m['mechanism_id']]],'mechanisms_with_retained_generalized_cover':sum(bool(m['covering_retained_term_ids']) for m in mechanisms),'candidate_exact_blocks_preserved':48,'mechanisms_term_failure':0,'weight14_positive_pool_counts':{k:len(v) for k,v in w14.items()},'weight14_pair_configuration_count':sum(1 for x in pair_relations for c in x['positive_configurations'] if c['source']['source']!='weight12_pool'),'weight14_negative_results_used':0,'dedup_counts':{k:dedup[k] for k in ('old_reviewed_terms','new_raw_term_candidates','new_pair_candidates','new_multi_check_candidates','duplicate_old','duplicate_new','dominated_old','dominated_new','retained_new_terms','merged_installed_generalized_terms')},'claim_scope':'conservative positive library only; no negative-side completeness or physical absence claim'}

dump(OUT/'formula_raw_replay_bindings.json',{'schema':'round72-formula-raw-replay-bindings-v1','records':formula_bindings})
dump(OUT/'mechanisms.json',{'schema':'round72-source-mechanisms-v1','mechanisms':mechanisms})
dump(OUT/'local_order_catalog.json',{'schema':'round72-local-order-catalog-v1','entries':catalog_public})
dump(OUT/'multi_check_relations.json',{'schema':'round72-multi-check-exact-relations-v1','relations':multi_relations})
dump(OUT/'pair_relations.json',{'schema':'round72-positive-pair-relations-v1','relations':pair_relations,'seed_attempts':seed_attempts})
dump(OUT/'retained_terms.json',{'schema':'round72-retained-generalized-terms-v1','terms':retained_public})
dump(OUT/'dedup_ledger.json',dedup);dump(OUT/'summary.json',summary)
print(json.dumps(summary,indent=2,sort_keys=True))
