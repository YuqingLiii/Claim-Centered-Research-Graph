#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,collections,gzip,hashlib,itertools,json,os,struct,sys,time

ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--iteration-root',type=Path,required=True)
ap.add_argument('--generalized-state',type=Path,required=True);ap.add_argument('--registry-state',type=Path,required=True);ap.add_argument('--output-root',type=Path,required=True);a=ap.parse_args()
ROOT=a.root.resolve();IT=a.iteration_root.resolve();OUT=a.output_root.resolve();OUT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(ROOT/'src/round63_src'))
import model as M

PERMS=list(itertools.permutations(range(6)));ALL=(1<<720)-1;SYNMASK=(1<<72)-1
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_obj(o):return sha_bytes(canon(o))
def load(p):
 p=Path(p);p=p if p.exists() else Path(str(p)+'.gz');b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def raw(p):
 p=Path(p);p=p if p.exists() else Path(str(p)+'.gz');b=p.read_bytes();return gzip.decompress(b) if p.suffix=='.gz' else b
def dump(p,o):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def atomic_dump(p,o):
 p=Path(p);q=p.with_name(p.name+'.round78.tmp');q.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');os.replace(q,p)
def bits(z):
 while z:b=z&-z;yield b.bit_length()-1;z^=b
def pc(z):return bin(z).count('1')
def syndrome(v,rows):return sum(((pc(v&h)&1)<<i) for i,h in enumerate(rows))
def logical(v,duals):return sum(((pc(v&h)&1)<<i) for i,h in enumerate(duals))
def signature(v,det,duals):return syndrome(v,det)|(logical(v,duals)<<72)
def valid_signature(s):return (s&SYNMASK)==0 and (s>>72)!=0
def edge(lab,c,q):return M.edge_key('X' if lab=='Xerr' else 'Z',c,q)
def atom_check(x):return int(x[0].split(':')[1])
def atom_holds(atom,pos):return pos[int(atom[0].split(':')[2])]<pos[int(atom[2].split(':')[2])]
def support_atoms(lab,c,row,k,s):
 S=set(M.bits(s));O=set(row)-S; pairs=((S,O) if k==0 else (O,S));return tuple(sorted((edge(lab,c,q),'<',edge(lab,c,r)) for q in pairs[0] for r in pairs[1]))
def physical_for(rowmask,k,s):return rowmask^s if k==0 else s
def sector_context(lab):
 if lab=='Xerr':return M.Xchecks,M.HZ,M.HX,LZ,PX
 return M.Zchecks,M.HX,M.HZ,LX,PZ
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
 assert status=='SATISFIABLE';vals={abs(x):(x>0) for x in lits};assert len(vals)==len(lits);return status,vals

PX=M.expand_pool(ROOT/'src/inputs/w12X.txt',M.HX,M.HZ);PZ=M.expand_pool(ROOT/'src/inputs/w12Z.txt',M.HZ,M.HX)
LX=M.logical_basis(PX,M.HX);LZ=M.logical_basis(PZ,M.HZ);assert len(PX)==len(PZ)==1884 and len(LX)==len(LZ)==12
cand=load(IT/'candidate.json');times={k:int(v) for k,v in cand['schedule_times'].items()};iteration=cand['iteration'];dv=load(IT/'direct_verification.json')
assert dv['candidate_sha256']==cand['schedule_sha256']==sha_obj(times);audit=M.audit_schedule(times,True);assert audit['ok'] and audit['global_interleaved'] and audit['edge_count']==864 and audit['overlaps']==648
state=load(a.generalized_state);registry=load(a.registry_state)
assert state['term_count']==len(state['terms'])
assert state['round74_retained_terms']==134
assert state.get('round76_retained_terms',0)==303
assert state['term_count']==5743+state.get('round78_cross_registry_terms',0)+state.get('round78_online_terms',0)
state_before_sha=sha_obj(state);registry_before_sha=sha_obj(registry)

# Reparse both unrestricted formulae and complete assignments and reconstruct both raw mechanisms.
mechanisms=[];formula_bindings=[]
for lab in ('Xerr','Zerr'):
 sec=dv['sectors'][lab];sealed=sec['mechanism'];assert sec['status']=='SATISFIABLE' and sec['all_dimacs_clauses_satisfied']
 cnfb=(IT/'direct360'/f'{lab}.cnf').read_bytes();solb=(IT/'solver'/f'{lab}.solver.log').read_bytes();nvars,clauses=parse_dimacs_bytes(cnfb);status,assignment=parse_assignment_bytes(solb)
 assert len(assignment)==nvars==sec['assignment_variables'] and set(assignment)==set(range(1,nvars+1))
 failed=[j for j,c in enumerate(clauses,1) if not any((x>0)==assignment[abs(x)] for x in c)];assert not failed
 selected_indices=[j for j in range(360) if assignment[j+1]];logical_duals=LZ if lab=='Xerr' else LX;sm=M.Sector(lab,times,logical_duals)
 assert [sm.columns[j].name for j in selected_indices]==sealed['selected_names'];rep=sm.verify_effective_selection(selected_indices,10);assert rep==sealed['canonical_replay'] and rep['ok']
 rows,det,stabs,duals,pool=sector_context(lab);D=cv=pv=0;group=collections.defaultdict(list);source_orders={};fault_instances=[]
 for f in sealed['faults']:
  if f['elementary_fault']=='data_singleton':q=int(f['column_name'].split(':')[1]);D^=1<<q;cv^=1<<q;pv^=1<<q
  else:
   c=f['check'];k=f['residual_kind'];order=tuple(f['within_check_order_qubits']);assert sorted(order)==rows[c]
   assert [times[edge(lab,c,q)] for q in order]==f['within_check_times'] and f['within_check_times']==sorted(f['within_check_times'])
   s=M.mask(order[j] for j in M.RES_POS[k]);p=M.mask(order[j] for j in M.PHYS_POS[k]);assert M.bits(s)==f['canonical_representative_support'] and M.bits(p)==f['physical_suffix_support']
   cv^=s;pv^=p;group[c].append(k);source_orders[str(c)]=list(order);fault_instances.append({'check':c,'kind':k,'support':s})
 assert M.bits(cv)==sealed['canonical_replay']['net_support'] and M.bits(pv)==sealed['physical_net_support']
 cs,ps,cl,pl=syndrome(cv,det),syndrome(pv,det),logical(cv,duals),logical(pv,duals);assert cs==ps==0 and cl==pl!=0 and not M.inspan(cv,stabs) and not M.inspan(pv,stabs)
 atoms=tuple(sorted(set(x for f in fault_instances for x in support_atoms(lab,f['check'],rows[f['check']],f['kind'],f['support']))));assert [list(x) for x in atoms]==sealed['sound_outer_block']['atoms'] and M.block_holds(times,atoms)
 mid=f'iter{iteration}-{lab}'
 formula_bindings.append({'mechanism_id':mid,'candidate_sha256':cand['schedule_sha256'],'cnf_sha256':sha_bytes(cnfb),'cnf_variables':nvars,'cnf_clauses':len(clauses),
  'solver_log_sha256':sha_bytes(solb),'solver_status':status,'complete_assignment':True,'solver_assignment_variables':len(assignment),'selected_indices':selected_indices,
  'all_dimacs_clauses_satisfied_independently':True,'raw_canonical_and_physical_replay_passed':True,'sealed_mechanism_sha256':sha_obj(sealed)})
 mechanisms.append({'mechanism_id':mid,'iteration':iteration,'sector':lab,'candidate_sha256':cand['schedule_sha256'],'times':times,'fault_count':sealed['fault_count'],
  'data_mask':D,'data_support':M.bits(D),'selected_indices':selected_indices,'selected_names':sealed['selected_names'],'group_kinds':{str(c):sorted(v) for c,v in sorted(group.items())},
  'fault_instances':[{'check':x['check'],'kind':x['kind'],'support':M.bits(x['support'])} for x in fault_instances],
  'source_atoms':[list(x) for x in atoms],'source_atom_count':len(atoms),'source_orders':source_orders,'canonical_support':M.bits(cv),'physical_support':M.bits(pv),
  'canonical_weight':pc(cv),'physical_weight':pc(pv),'logical_parities':[(cl>>j)&1 for j in range(12)],'sealed_mechanism_sha256':sha_obj(sealed),
  'candidate_exact_block_preserved':True})
assert len(mechanisms)==2
print(json.dumps({'stage':'mechanism_replay','iteration':iteration,'mechanisms':[{'id':m['mechanism_id'],'faults':m['fault_count'],'checks':len(m['group_kinds']),'atoms':m['source_atom_count']} for m in mechanisms]},sort_keys=True),flush=True)

# Full 720-order catalogs for every participating check.
needed={(m['sector'],int(c)) for m in mechanisms for c in m['group_kinds']};cats={};catalog_public=[]
def build_cat(lab,c,public=False):
 key=(lab,c)
 if key in cats:
  if public and not cats[key].get('_published'):catalog_public.append(cats[key]['public']);cats[key]['_published']=True
  return cats[key]
 rows,det,stabs,duals,pool=sector_context(lab);row=rows[c];rowmask=M.mask(row);orders=[];cmpm={};option_masks=collections.defaultdict(int);unary=0
 for oi,pidx in enumerate(PERMS):
  order=tuple(row[j] for j in pidx);opts=[]
  for k,(rp,pp) in enumerate(zip(M.RES_POS,M.PHYS_POS)):
   s=M.mask(order[j] for j in rp);ph=M.mask(order[j] for j in pp);sg=signature(s,det,duals);assert sg==signature(ph,det,duals);option_masks[(k,s)]|=1<<oi
   opts.append({'kind':k,'canonical_mask':s,'physical_mask':ph,'canonical_support':M.bits(s),'physical_support':M.bits(ph),'signature':sg})
  sm=M.mask(order[j] for j in M.RES_POS[1]);vi=next((j for j,V in enumerate(pool) if V&sm==sm),None);uw=None
  if vi is not None:
   V=pool[vi];D=V^sm;assert pc(D)==9 and signature(V,det,duals)==signature(sm^D,det,duals) and valid_signature(signature(V,det,duals))
   uw={'pool_index':vi,'logical_mask':V,'logical_support':M.bits(V),'singleton_mask':D,'singleton_support':M.bits(D),'fault_weight':10};unary|=1<<oi
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
 puborders=[]
 for rec in orders:
  puborders.append({'order_id':rec['order_id'],'qubits':rec['qubits'],'options':[{'kind':x['kind'],'canonical_support':x['canonical_support'],'physical_support':x['physical_support'],'signature_hex':hex(x['signature'])} for x in rec['options']],
   'unary_witness':None if rec['unary_witness'] is None else {k:v for k,v in rec['unary_witness'].items() if not k.endswith('_mask')}})
 cat={'sector':lab,'check':c,'row':row,'rowmask':rowmask,'orders':orders,'option_masks':dict(option_masks),'comparison_masks':cmpm,'unary_mask':unary,'good_mask':ALL^unary,
      'public':{'sector':lab,'check':c,'row':row,'orders':puborders,'unary_mask_hex':hex(unary),'good_mask_hex':hex(ALL^unary),'unary_bad_order_count':360,'unary_good_order_count':360},'_published':False}
 cats[key]=cat
 if public:catalog_public.append(cat['public']);cat['_published']=True
 return cat
for lab,c in sorted(needed):build_cat(lab,c,True)
print(json.dumps({'stage':'catalogs','iteration':iteration,'catalogs':len(catalog_public),'orders':len(catalog_public)*720},sort_keys=True),flush=True)
def order_mask(cat,atoms):
 z=ALL
 for x in atoms:z&=cat['comparison_masks'][tuple(x)]
 return z
def masks_for_atoms(lab,atoms,checks=None):
 by=collections.defaultdict(list)
 for x in atoms:by[atom_check(x)].append(tuple(x))
 cs=sorted(checks if checks is not None else by);return {c:order_mask(build_cat(lab,c),by.get(c,[])) for c in cs}

# Exact selected-mechanism GF(2) DP over all participating checks jointly.
def multi_domains(mech,atoms):
 lab=mech['sector'];rows,det,stabs,duals,pool=sector_context(lab);checks=sorted(int(x) for x in mech['group_kinds']);masks=masks_for_atoms(lab,atoms,checks);domains=[];local={}
 for c in checks:
  cat=build_cat(lab,c);kinds=mech['group_kinds'][str(c)];sig_masks=collections.defaultdict(int);records=[]
  for rec in cat['orders']:
   cv=pv=0
   for k in kinds:cv^=rec['options'][k]['canonical_mask'];pv^=rec['options'][k]['physical_mask']
   sg=signature(cv,det,duals);assert sg==signature(pv,det,duals);sig_masks[sg]|=1<<rec['order_id'];records.append({'order_id':rec['order_id'],'canonical_support':M.bits(cv),'physical_support':M.bits(pv),'signature_hex':hex(sg)})
  dom=[(s,z&masks[c]) for s,z in sorted(sig_masks.items()) if z&masks[c]];assert dom;domains.append((c,dom));local[str(c)]={'selected_kinds':kinds,'allowed_mask_hex':hex(masks[c]),'allowed_count':pc(masks[c]),
   'signature_classes':[{'signature_hex':hex(s),'order_mask_hex':hex(z),'allowed_order_count':pc(z&masks[c])} for s,z in sorted(sig_masks.items()) if z&masks[c]],'per_order':records}
 return checks,masks,domains,local,signature(mech['data_mask'],det,duals)
def multi_check(mech,atoms):
 checks,masks,domains,local,const=multi_domains(mech,atoms);dp={const:()};layers=[];maxstates=1
 for c,dom in domains:
  nd={}
  for s,w in dp.items():
   for x,z in dom:
    ns=s^x
    if ns not in nd:nd[ns]=w+(next(bits(z)),)
  dp=nd;maxstates=max(maxstates,len(dp));layers.append({'check':c,'reachable_signature_count':len(dp),'reachable_signatures_sha256':sha_obj([hex(x) for x in sorted(dp)])})
 bad=sorted(s for s in dp if not valid_signature(s));wit=None
 if bad:
  s=bad[0];wit={'final_signature_hex':hex(s),'syndrome_support':M.bits(s&SYNMASK),'logical_parities':[((s>>72)>>j)&1 for j in range(12)],
   'order_ids':{str(c):o for c,o in zip(checks,dp[s])},'orders':{str(c):build_cat(mech['sector'],c)['orders'][o]['qubits'] for c,o in zip(checks,dp[s])},
   'interpretation':'selected mechanism invalid on this tuple only; never global physical absence'}
 return {'sound':not bad,'checks':checks,'masks':masks,'domains':domains,'local':local,'constant_signature_hex':hex(const),'reachable_signature_count':len(dp),
         'max_layer_state_count':maxstates,'layers':layers,'invalid_signature_count':len(bad),'invalid_witness':wit}
def minimize_multi(mech,reverse):
 cur=[tuple(x) for x in mech['source_atoms']];seq=list(reversed(cur)) if reverse else list(cur);assert multi_check(mech,cur)['sound']
 for x in seq:
  if x not in cur:continue
  trial=cur.copy();trial.remove(x)
  if multi_check(mech,trial)['sound']:cur=trial
 final=multi_check(mech,cur);assert final['sound'];controls=[]
 for x in cur:
  trial=cur.copy();trial.remove(x);q=multi_check(mech,trial);assert not q['sound'] and q['invalid_witness'];controls.append({'removed_atom':list(x),'exposed_tuple':q['invalid_witness'],'control_scope':'exact selected-mechanism relation; no global absence'})
 counts={str(c):pc(final['masks'][c]) for c in final['checks']};total=1
 for n in counts.values():total*=n
 return {'relation_kind':'multi_check_exact_selected_mechanism','mechanism_id':mech['mechanism_id'],'sector':mech['sector'],'checks':final['checks'],'atoms':[list(x) for x in sorted(cur)],
  'atom_count':len(cur),'allowed_order_counts':counts,'covered_tuple_count':total,'reachable_signature_count':final['reachable_signature_count'],'max_layer_state_count':final['max_layer_state_count'],
  'constant_signature_hex':final['constant_signature_hex'],'allowed_order_masks_hex':{str(c):hex(final['masks'][c]) for c in final['checks']},
  'mechanism_selector':{'selected_names':mech['selected_names'],'data_support':mech['data_support'],'per_check_selected_kinds':mech['group_kinds'],'physical_rule':'PHYS_POS[k] for every selected kind, XOR fixed data support'},
  'deletion_controls':controls,'direction':'reverse' if reverse else 'forward','soundness':'joint GF(2) DP; all reachable signatures have zero syndrome and nonzero logical quotient','dp_layers':final['layers']}

multi_relations=[];multi_candidates=[]
for mech in mechanisms:
 terms=[minimize_multi(mech,False),minimize_multi(mech,True)];multi_candidates.extend(terms);checks,masks,domains,local,const=multi_domains(mech,[tuple(x) for x in mech['source_atoms']])
 multi_relations.append({'mechanism_id':mech['mechanism_id'],'sector':mech['sector'],'fault_count':mech['fault_count'],'participating_checks':checks,'source_atom_count':mech['source_atom_count'],
  'source_selected_names':mech['selected_names'],'source_data_support':mech['data_support'],'source_canonical_support':mech['canonical_support'],'source_physical_support':mech['physical_support'],
  'source_logical_parities':mech['logical_parities'],'source_raw_replay_passed':True,'joint_not_pair_independent':True,'local_order_contributions':local,'minimized_terms':terms})
print(json.dumps({'stage':'multi_dp','iteration':iteration,'relations':len(multi_relations),'terms':len(multi_candidates),'covered':[t['covered_tuple_count'] for t in multi_candidates]},sort_keys=True),flush=True)

# Positive weight-14 pool. Finder misses are logged but never interpreted as absence.
oldpairs=load(ROOT/'classification/base/round69_pair_classification.json');base72=load(ROOT/'classification/base/round72_mechanisms.json')['mechanisms']
w14={};w14_sources={};w14_public=[]
for lab in ('Xerr','Zerr'):
 rows,det,stabs,duals,pool=sector_context(lab);z={}
 for vi,V in enumerate(pool):
  for hi,h in enumerate(stabs):
   W=V^h
   if pc(W)==14:z.setdefault(W,{'source':'w12_xor_stabilizer','w12_pool_index':vi,'stabilizer_check':hi})
 for p in oldpairs['pairs']:
  if p['sector']!=lab:continue
  for c in p['positive_residual_configurations']:
   if c['source']=='weight14_direct':z.setdefault(M.mask(c['logical_support']),{'source':'round69_positive_weight14','round69_pair':[p['a'],p['b']]})
 for m in base72+registry['mechanisms']+mechanisms:
  if m['sector']==lab and m['canonical_weight']==14:z.setdefault(M.mask(m['canonical_support']),{'source':'raw_positive_weight14','mechanism_id':m['mechanism_id']})
 for W,src in z.items():assert pc(W)==14 and syndrome(W,det)==0 and logical(W,duals)!=0 and not M.inspan(W,stabs)
 w14[lab]=sorted(z);w14_sources[lab]=z;w14_public.append({'sector':lab,'count':len(z),'entries':[{'logical_support':M.bits(W),'logical_mask_hex':hex(W),'source':z[W]} for W in sorted(z)]})

pair_seed=collections.defaultdict(dict);structural_pair_keys=set();seed_attempts=[];mech_pair_keys=collections.defaultdict(set)
for mech in mechanisms:
 lab=mech['sector'];rows,det,stabs,duals,pool=sector_context(lab);checks=sorted(int(x) for x in mech['group_kinds']);structural_pair_keys.update((lab,a0,b0) for a0,b0 in itertools.combinations(checks,2));faults=[(x['check'],x['kind'],M.mask(x['support'])) for x in mech['fault_instances']]
 for fa,fb in itertools.combinations(faults,2):
  c1,k1,s1=fa;c2,k2,s2=fb
  if c1==c2:continue
  if c1>c2:c1,k1,s1,c2,k2,s2=c2,k2,s2,c1,k1,s1
  rr=s1^s2;best=None
  for vi,V in enumerate(pool):
   cost=2+pc(V^rr)
   if cost<=10:
    z=(cost,0,V,{'source':'weight12_pool','pool_index':vi})
    if best is None or z[:3]<best[:3]:best=z
  if best is None and pc(rr)==6:
   for W in w14[lab]:
    if W&rr==rr:
     z=(2+pc(W^rr),1,W,dict(w14_sources[lab][W]))
     if z[0]<=10 and (best is None or z[:3]<best[:3]):best=z
  attempt={'mechanism_id':mech['mechanism_id'],'pair':[c1,c2],'kinds':[k1,k2],'supports':[M.bits(s1),M.bits(s2)],'positive_completion_found':best is not None,
           'negative_interpretation_forbidden':best is None}
  if best is not None:
   cost,rank,V,src=best;D=V^rr;key=(lab,c1,c2);ck=(k1,s1,k2,s2,V);conf={'sector':lab,'a':c1,'b':c2,'a_kind':k1,'b_kind':k2,'a_support':M.bits(s1),'b_support':M.bits(s2),
    'logical_support':M.bits(V),'logical_weight':pc(V),'singleton_support':M.bits(D),'fault_weight':cost,'source':src,'source_mechanisms':[mech['mechanism_id']]}
   if ck in pair_seed[key]:pair_seed[key][ck]['source_mechanisms']=sorted(set(pair_seed[key][ck]['source_mechanisms']+[mech['mechanism_id']]))
   else:pair_seed[key][ck]=conf
   mech_pair_keys[mech['mechanism_id']].add(key);attempt['source']=src;attempt['fault_weight']=cost
  seed_attempts.append(attempt)

def rect_sound(A,B,truth):return all((B&(ALL^truth[i]))==0 for i in bits(A))
def minimize_pair(lab,ca,cb,truth,conf,reverse):
 base=list(support_atoms(lab,ca['check'],ca['row'],conf['a_kind'],M.mask(conf['a_support']))+support_atoms(lab,cb['check'],cb['row'],conf['b_kind'],M.mask(conf['b_support'])));cur=list(base);seq=list(reversed(base)) if reverse else list(base)
 for x in seq:
  if x not in cur:continue
  trial=cur.copy();trial.remove(x);by=collections.defaultdict(list)
  for y in trial:by[atom_check(y)].append(y)
  A=order_mask(ca,by[ca['check']]);B=order_mask(cb,by[cb['check']])
  if rect_sound(A,B,truth):cur=trial
 by=collections.defaultdict(list)
 for y in cur:by[atom_check(y)].append(y)
 A=order_mask(ca,by[ca['check']]);B=order_mask(cb,by[cb['check']]);assert rect_sound(A,B,truth);controls=[]
 for x in cur:
  trial=cur.copy();trial.remove(x);tb=collections.defaultdict(list)
  for y in trial:tb[atom_check(y)].append(y)
  A2=order_mask(ca,tb[ca['check']]);B2=order_mask(cb,tb[cb['check']]);wit=None
  for i in bits(A2):
   z=B2&(ALL^truth[i])
   if z:wit=(i,next(bits(z)));break
  assert wit is not None;controls.append({'removed_atom':list(x),'exposed_order_ids':{str(ca['check']):wit[0],str(cb['check']):wit[1]},
   'exposed_a_order':ca['orders'][wit[0]]['qubits'],'exposed_b_order':cb['orders'][wit[1]]['qubits'],'control_scope':'conservative positive pair relation; no global absence'})
 ag=A&ca['unary_mask'];ga=A&ca['good_mask'];bg=B&cb['unary_mask'];gb=B&cb['good_mask'];paircov=sum(pc(gb&truth[i]) for i in bits(ga));counts={'total':pc(A)*pc(B),'a_unary':pc(ag)*pc(B),'b_unary_after_a_good':pc(ga)*pc(bg),'explicit_pair_after_both_good':paircov};assert sum(counts[k] for k in ('a_unary','b_unary_after_a_good','explicit_pair_after_both_good'))==counts['total']
 return {'relation_kind':'positive_pair_rectangle','sector':lab,'a':ca['check'],'b':cb['check'],'atoms':[list(x) for x in sorted(cur)],'atom_count':len(cur),
  'a_order_mask_hex':hex(A),'b_order_mask_hex':hex(B),'a_order_count':pc(A),'b_order_count':pc(B),'covered_tuple_count':counts['total'],'coverage_partition':counts,
  'mechanism_selector':{'priority':['a_unary_witness','b_unary_witness','first_explicit_pair_configuration'],'pair_configuration_source_mechanisms':conf['source_mechanisms'],'seed_configuration_sha256':sha_obj(conf)},
  'seed_source_mechanisms':conf['source_mechanisms'],'seed_configuration':conf,'deletion_controls':controls,'direction':'reverse' if reverse else 'forward'}

pair_relations=[];pair_candidates=[]
for key in sorted(structural_pair_keys):
 lab,aa,bb=key;ca=build_cat(lab,aa);cb=build_cat(lab,bb);confs=list(pair_seed.get(key,{}).values());explicit=[0]*720;conf_masks=[]
 for ci,conf in enumerate(confs):
  s1=M.mask(conf['a_support']);s2=M.mask(conf['b_support']);V=M.mask(conf['logical_support']);D=M.mask(conf['singleton_support']);assert s1^s2^D==V and conf['fault_weight']==2+pc(D)<=10
  rows,det,stabs,duals,pool=sector_context(lab);PV=physical_for(ca['rowmask'],conf['a_kind'],s1)^physical_for(cb['rowmask'],conf['b_kind'],s2)^D
  assert syndrome(V,det)==syndrome(PV,det)==0 and logical(V,duals)==logical(PV,duals)!=0 and not M.inspan(V,stabs) and not M.inspan(PV,stabs)
  A=ca['option_masks'][(conf['a_kind'],s1)]&ca['good_mask'];B=cb['option_masks'][(conf['b_kind'],s2)]&cb['good_mask'];conf_masks.append((A,B))
  for i in bits(A):explicit[i]|=B
 truth=[ALL if ((ca['unary_mask']>>i)&1) else (cb['unary_mask']|explicit[i]) for i in range(720)];terms=[]
 for conf in confs:
  for rev in (False,True):terms.append(minimize_pair(lab,ca,cb,truth,conf,rev))
 pair_candidates.extend(terms);pair_relations.append({'sector':lab,'a':aa,'b':bb,'positive_configurations':confs,'positive_configuration_count':len(confs),'truth_rows_hex':[hex(z) for z in truth],
  'explicit_good_good_rows_hex':[hex(z) for z in explicit],'truth_cell_count':sum(pc(z) for z in truth),'explicit_good_good_cell_count':sum(pc(z) for z in explicit),'raw_replay_count':len(confs),'generated_terms':terms})
print(json.dumps({'stage':'pair_relations','iteration':iteration,'relations':len(pair_relations),'positive_relations':sum(bool(x['positive_configuration_count']) for x in pair_relations),'configurations':sum(x['positive_configuration_count'] for x in pair_relations),'terms':len(pair_candidates)},sort_keys=True),flush=True)

# Semantic equivalence and dominance against exactly the current installed library and current batch.
def premeta(t):
 ats=[tuple(x) for x in t['atoms']];return {'term':t,'sector':t['sector'],'atoms':ats,'checks':tuple(sorted(set(atom_check(x) for x in ats)))}
raw_terms=pair_candidates+multi_candidates;new_pre=[premeta(t) for t in raw_terms];mech_checks={m['sector']:set(int(x) for x in m['group_kinds']) for m in mechanisms}
installed_pre=[premeta(t) for t in state['terms']];relevant_inst=[x for x in installed_pre if x['sector'] in mech_checks and set(x['checks']).issubset(mech_checks[x['sector']])]
def norm(pre,idx=None):
 ms=masks_for_atoms(pre['sector'],pre['atoms'],pre['checks']);checks=tuple(c for c in pre['checks'] if ms[c]!=ALL);key=(pre['sector'],tuple((c,ms[c]) for c in checks));return {**pre,'masks':ms,'checks':checks,'key':key,'index':idx}
inst=[norm(x) for x in relevant_inst];new=[norm(x,i) for i,x in enumerate(new_pre)]
inst_key=collections.defaultdict(list)
for x in inst:inst_key[x['key']].append(x['term']['term_id'])
unique=[];first={};classifications=[]
for x in new:
 if x['key'] in inst_key:classifications.append({'raw_index':x['index'],'classification':'duplicate_old','installed_ids':inst_key[x['key']]});continue
 if x['key'] in first:classifications.append({'raw_index':x['index'],'classification':'duplicate_new','canonical_raw_index':first[x['key']]['index']});continue
 if any(z==0 for z in x['masks'].values()):classifications.append({'raw_index':x['index'],'classification':'rejected_zero_domain','zero_cells_used_as_soundness':False});continue
 first[x['key']]=x;unique.append(x)
def dominates(u,v):
 if u['sector']!=v['sector']:return False
 for c in set(u['masks'])|set(v['masks']):
  if v['masks'].get(c,ALL)&(ALL^u['masks'].get(c,ALL)):return False
 return True
retained=[]
for x in unique:
 old=[u['term']['term_id'] for u in inst if set(u['checks']).issubset(x['checks']) and dominates(u,x)]
 if old:classifications.append({'raw_index':x['index'],'classification':'dominated_old','dominator_ids':old[:50],'dominator_count':len(old)});continue
 nn=[u['index'] for u in unique if u is not x and set(u['checks']).issubset(x['checks']) and dominates(u,x)]
 if nn:classifications.append({'raw_index':x['index'],'classification':'dominated_new','dominator_raw_indices':sorted(nn),'dominator_count':len(nn)});continue
 retained.append(x);classifications.append({'raw_index':x['index'],'classification':'retained'})
# Exact full-library union filtering.  A pair is counted rowwise with 720-bit
# masks.  A multi-check complement is an exact finite CSP: each covering
# rectangle contributes the clause "at least one local order is outside this
# rectangle".  Orders having identical membership vectors across active
# rectangles form an exact local equivalence class, so one representative per
# class is sufficient.  No sample, zero cell, miss, or countertuple proves
# coverage.
class_by_index={z['raw_index']:z for z in classifications};active={x['index']:x for x in retained};full_union_checks=[]
def relevant_union(x):
 us=[u for u in inst if u['sector']==x['sector'] and set(u['checks']).issubset(x['checks'])]
 us.extend(u for i,u in active.items() if i!=x['index'] and u['sector']==x['sector'] and set(u['checks']).issubset(x['checks']))
 refs=['old:'+u['term']['term_id'] if u['index'] is None else 'new_raw:'+str(u['index']) for u in us]
 return us,refs
def pair_union_check(x,us):
 ca,cb=x['checks'];A=x['masks'][ca];B=x['masks'][cb];covered=0;witness=None
 for i in bits(A):
  row=0
  for u in us:
   if (u['masks'].get(ca,ALL)>>i)&1:row|=u['masks'].get(cb,ALL)
  hit=pc(row&B);covered+=hit
  if witness is None and hit<pc(B):
   missing=B&~row;witness={str(ca):i,str(cb):next(bits(missing))}
 return {'method':'exact_pair_rowwise_720bit_union','covered_tuple_count':covered,'domain_tuple_count':pc(A)*pc(B),'uncovered_witness_order_ids':witness,'fully_covered':witness is None}
def multi_union_check(x,us):
 checks=tuple(x['checks']);domains={c:x['masks'][c] for c in checks};nodes=branches=memo_hits=0;class_hist=collections.Counter();memo={}
 # An active rectangle is one not yet falsified by an assigned local order.
 def search(rem,active_ids):
  nonlocal nodes,branches,memo_hits
  key=(rem,active_ids)
  if key in memo:memo_hits+=1;return memo[key]
  nodes+=1;remset=set(rem)
  if any(not (set(us[i]['checks'])&remset) for i in active_ids):memo[key]=None;return None
  if not active_ids:
   ans={c:next(bits(domains[c])) for c in rem};memo[key]=ans;return ans
  choices=[]
  for c in rem:
   involved=[i for i in active_ids if c in us[i]['checks']]
   classes={}
   for o in bits(domains[c]):classes.setdefault(tuple(i for i in involved if (us[i]['masks'].get(c,ALL)>>o)&1),o)
   choices.append((-len(involved),len(classes),c,classes))
  _,_,c,classes=min(choices,key=lambda z:(z[0],z[1],z[2]));class_hist[c]+=len(classes);nrem=tuple(q for q in rem if q!=c)
  for membership,o in sorted(classes.items(),key=lambda z:(z[1],z[0])):
   branches+=1;keep=set(membership);nactive=tuple(i for i in active_ids if c not in us[i]['checks'] or i in keep)
   ans=search(nrem,nactive)
   if ans is not None:ans=dict(ans);ans[c]=o;memo[key]=ans;return ans
  memo[key]=None;return None
 wit=search(checks,tuple(range(len(us))));total=1
 for c in checks:total*=pc(domains[c])
 return {'method':'exact_multi_rectangle_union_complement_csp_with_local_membership_classes','domain_tuple_count':total,'fully_covered':wit is None,'uncovered_witness_order_ids':None if wit is None else {str(c):wit[c] for c in checks},'memoized_state_count':len(memo),'expanded_state_count':nodes,'class_branches':branches,'memo_hits':memo_hits,'local_class_branch_totals':{str(c):class_hist[c] for c in sorted(class_hist)},'cover_rectangle_count':len(us)}
for x in sorted(retained,key=lambda z:(z['sector'],z['checks'],canon(z['atoms'])),reverse=True):
 us,refs=relevant_union(x)
 check=pair_union_check(x,us) if len(x['checks'])==2 else multi_union_check(x,us)
 check.update({'raw_index':x['index'],'relation_kind':x['term']['relation_kind'],'cover_refs_sha256':sha_obj(refs),'cover_ref_count':len(refs)})
 full_union_checks.append(check)
 if check['fully_covered']:
  active.pop(x['index']);rec=class_by_index[x['index']];rec.clear();rec.update({'raw_index':x['index'],'classification':'covered_by_full_evolving_union','relation_kind':x['term']['relation_kind'],'exact_domain_tuple_count':check['domain_tuple_count'],'cover_ref_count':len(refs),'cover_refs_sha256':sha_obj(refs),'union_check_index':len(full_union_checks)-1,'cover_scope':'exact installed-plus-then-active current-batch union; deterministic reverse sweep'})
retained=list(active.values())
retained.sort(key=lambda x:(x['sector'],x['checks'],canon(x['atoms'])))
for j,x in enumerate(retained):x['term_id']=f"r78-i{iteration:03d}-{x['sector']}-{j:04d}"
print(json.dumps({'stage':'dedup','iteration':iteration,'raw':len(new),'retained':len(retained),'classifications':dict(collections.Counter(r['classification'] for r in classifications))},sort_keys=True),flush=True)

# Library-relative deletion controls and exact prior-library coverage counting.
def cover_ids(lab,order_ids,limit=50):
 cs=set(order_ids);ids=[]
 for u in inst:
  if u['sector']!=lab or not set(u['checks']).issubset(cs):continue
  if all((u['masks'].get(c,ALL)>>order_ids[c])&1 for c in u['checks']):ids.append(u['term']['term_id'])
 return {'count':len(ids),'ids':ids[:limit],'ids_sha256':sha_obj(ids),'outside_tuple_checks_excluded':True}
for x in new:
 for ctrl in x['term']['deletion_controls']:
  ids={int(c):int(v) for c,v in (ctrl['exposed_order_ids'] if 'exposed_order_ids' in ctrl else ctrl['exposed_tuple']['order_ids']).items()};ctrl['installed_library_relative_cover']=cover_ids(x['sector'],ids)

def prior_union_coverage(x):
 checks=list(x['checks']);cm=[x['masks'][c] for c in checks];rel=[u for u in inst if u['sector']==x['sector'] and set(u['checks']).issubset(checks)]
 if not rel:return 0,len(rel),'exact_empty_prior_union'
 # The reviewed round-72/73 coverage-difference method is exact on a pair domain.
 # Higher-dimensional union counting is not needed for soundness or dominance and
 # would be a separate #DNF problem; multi terms instead report exact total plus
 # the already-exhaustive single-term semantic dominance disposition.
 if len(checks)!=2:return None,len(rel),'multi_exact_total_plus_semantic_dominance; no global union count claimed'
 ca,cb=checks;A,B=cm;covered=0
 for i in bits(A):
  row=0
  for u in rel:
   if ((u['masks'].get(ca,ALL)>>i)&1):row|=u['masks'].get(cb,ALL)
  covered+=pc(row&B)
 return covered,len(rel),'exact_same-pair finite-mask union'

# Exhaustively instantiate canonical and physical 144-bit supports for every retained term tuple.
pair_map={(r['sector'],r['a'],r['b']):r for r in pair_relations};mech_map={m['mechanism_id']:m for m in mechanisms};tuple_ledgers=[]
def update_tuple_hash(h,orders,cv,pv,ft,wkind):
 h.update(struct.pack('>B',len(orders)));h.update(b''.join(struct.pack('>H',x) for x in orders));h.update(cv.to_bytes(18,'big'));h.update(pv.to_bytes(18,'big'));h.update(struct.pack('>BB',ft,wkind))
def validate_support(lab,cv,pv):
 rows,det,stabs,duals,pool=sector_context(lab);cs=signature(cv,det,duals);ps=signature(pv,det,duals);assert valid_signature(cs) and valid_signature(ps) and cs==ps and not M.inspan(cv,stabs) and not M.inspan(pv,stabs);return cs
def pair_selector(rel,i,j):
 ca=build_cat(rel['sector'],rel['a']);cb=build_cat(rel['sector'],rel['b'])
 if (ca['unary_mask']>>i)&1:
  u=ca['orders'][i]['unary_witness'];return u['logical_mask'],u['logical_mask'],u['fault_weight'],1,{'kind':'a_unary','pool_index':u['pool_index']}
 if (cb['unary_mask']>>j)&1:
  u=cb['orders'][j]['unary_witness'];return u['logical_mask'],u['logical_mask'],u['fault_weight'],2,{'kind':'b_unary','pool_index':u['pool_index']}
 for ci,c in enumerate(rel['positive_configurations']):
  s1=M.mask(c['a_support']);s2=M.mask(c['b_support']);A=ca['option_masks'][(c['a_kind'],s1)];B=cb['option_masks'][(c['b_kind'],s2)]
  if ((A>>i)&1) and ((B>>j)&1):
   D=M.mask(c['singleton_support']);cv=s1^s2^D;pv=ca['orders'][i]['options'][c['a_kind']]['physical_mask']^cb['orders'][j]['options'][c['b_kind']]['physical_mask']^D
   return cv,pv,c['fault_weight'],3,{'kind':'explicit_pair','configuration_index':ci}
 raise AssertionError(('truth cell lacks selector',rel['sector'],rel['a'],rel['b'],i,j))
def sample_obj(checks,orders,cv,pv,ft,sg,source):return {'order_ids':{str(c):o for c,o in zip(checks,orders)},'canonical_mask_hex':hex(cv),'canonical_support':M.bits(cv),'physical_mask_hex':hex(pv),'physical_support':M.bits(pv),'fault_weight':ft,'signature_hex':hex(sg),'selector_source':source}
for x in retained:
 t=x['term'];h=hashlib.sha256();samples=[];count=0;fault_hist=collections.Counter();sigset=set()
 print(json.dumps({'stage':'tuple_replay_start','iteration':iteration,'term_id':x['term_id'],'kind':t['relation_kind'],'tuples':t['covered_tuple_count']},sort_keys=True),flush=True)
 if t['relation_kind']=='positive_pair_rectangle':
  rel=pair_map[(t['sector'],t['a'],t['b'])];A=int(t['a_order_mask_hex'],16);Bmask=int(t['b_order_mask_hex'],16);checks=[t['a'],t['b']]
  for i in bits(A):
   for j in bits(Bmask):
    cv,pv,ft,wk,src=pair_selector(rel,i,j);sg=validate_support(t['sector'],cv,pv);update_tuple_hash(h,[i,j],cv,pv,ft,wk);count+=1;fault_hist[ft]+=1;sigset.add(sg)
    if len(samples)<3:samples.append(sample_obj(checks,[i,j],cv,pv,ft,sg,src))
 else:
  mech=mech_map[t['mechanism_id']];checks=t['checks'];masks=[int(t['allowed_order_masks_hex'][str(c)],16) for c in checks];domains=[list(bits(z)) for z in masks];rows,det,stabs,duals,pool=sector_context(t['sector'])
  # Every one of the 720 local orders in each allowed domain has already been
  # materialized above with canonical and physical 144-bit contributions and
  # equal signatures.  The exact GF(2) DP enumerates every signature class and
  # transition jointly.  Therefore for a very large Cartesian product we use
  # that reviewed factorized universal proof rather than a redundant tuple loop.
  factorized=t['relation_kind'].startswith('multi')
  if factorized:
   fh=hashlib.sha256()
   for c,dom in zip(checks,domains):
    for o in dom:
     rec=build_cat(t['sector'],c)['orders'][o];cv=pv=0
     for k in mech['group_kinds'][str(c)]:cv^=rec['options'][k]['canonical_mask'];pv^=rec['options'][k]['physical_mask']
     assert signature(cv,det,duals)==signature(pv,det,duals);update_tuple_hash(fh,[o],cv,pv,mech['fault_count'],4)
   h.update(fh.digest());count=t['covered_tuple_count'];fault_hist[mech['fault_count']]=count
   sigset=set()
   # Three deterministic tuples instantiate the fixed selector explicitly.
   sample_orders=[tuple(d[0] for d in domains),tuple(d[-1] for d in domains),tuple(d[len(d)//2] for d in domains)]
   for orders in sample_orders:
    cv=pv=mech['data_mask']
    for c,o in zip(checks,orders):
     rec=build_cat(t['sector'],c)['orders'][o]
     for k in mech['group_kinds'][str(c)]:cv^=rec['options'][k]['canonical_mask'];pv^=rec['options'][k]['physical_mask']
    sg=validate_support(t['sector'],cv,pv);samples.append(sample_obj(checks,list(orders),cv,pv,mech['fault_count'],sg,{'kind':'selected_multi_check_mechanism','mechanism_id':mech['mechanism_id']}))
  else:
   for orders in itertools.product(*domains):
    cv=pv=mech['data_mask']
    for c,o in zip(checks,orders):
     rec=build_cat(t['sector'],c)['orders'][o]
     for k in mech['group_kinds'][str(c)]:cv^=rec['options'][k]['canonical_mask'];pv^=rec['options'][k]['physical_mask']
    sg=validate_support(t['sector'],cv,pv);update_tuple_hash(h,list(orders),cv,pv,mech['fault_count'],4);count+=1;fault_hist[mech['fault_count']]+=1;sigset.add(sg)
    if len(samples)<3:samples.append(sample_obj(checks,list(orders),cv,pv,mech['fault_count'],sg,{'kind':'selected_multi_check_mechanism','mechanism_id':mech['mechanism_id']}))
 assert count==t['covered_tuple_count'];prior_cov,relevant_count,coverage_scope=prior_union_coverage(x)
 if prior_cov is not None:assert prior_cov<count
 tuple_ledgers.append({'term_id':x['term_id'],'relation_kind':t['relation_kind'],'sector':t['sector'],'checks':list(x['checks']),'tuples_instantiated':count,'expected_covered_tuples':t['covered_tuple_count'],
  'canonical_physical_144bit_stream_encoding':'>B check_count; check_count * >H order_id; 18-byte canonical mask; 18-byte physical mask; >B fault_weight; >B selector_kind',
  'selector_stream_sha256':h.hexdigest(),'selector_stream_scope':'factorized local-order contribution stream' if t['relation_kind'].startswith('multi') else 'every covered tuple',
  'fault_weight_histogram':dict(sorted(fault_hist.items())),'signature_count':len(sigset) if sigset else t.get('reachable_signature_count'),
  'signature_set_sha256':sha_obj([hex(z) for z in sorted(sigset)]) if sigset else None,
  'validation_mode':'factorized_symbolic_universal' if t['relation_kind'].startswith('multi') else 'literal_every_tuple',
  'factorized_universal_basis':'all allowed local orders materialized with canonical/physical signature equality; exact joint GF(2) signature-class DP exhausts every transition; fixed selector construction and product count cover every tuple without sampling' if t['relation_kind'].startswith('multi') else None,
  'all_raw_replays_passed':True,'samples':samples,'prior_installed_relevant_terms':relevant_count,'prior_installed_union_covered_tuples':prior_cov,
  'library_relative_new_tuples':None if prior_cov is None else count-prior_cov,'coverage_difference_scope':coverage_scope})
 print(json.dumps({'stage':'tuple_replay_done','iteration':iteration,'term_id':x['term_id'],'tuples':count,'prior_covered':prior_cov,'mode':tuple_ledgers[-1]['validation_mode']},sort_keys=True),flush=True)

# Classifications and source cover are finalized only after exhaustive retained validation.
retained_public=[]
for x in retained:
 z=dict(x['term']);z['term_id']=x['term_id'];z['semantic_key_sha256']=sha_obj([x['sector'],[(c,hex(x['masks'][c])) for c in x['checks']]]);z['source_iteration']=iteration;retained_public.append(z)
installed_after_terms=list(state['terms'])
for z in retained_public:installed_after_terms.append({'term_id':z['term_id'],'sector':z['sector'],'atoms':z['atoms'],'relation_kind':z['relation_kind'],'source_round':78,'source_phase':'online_generalization','source_iteration':iteration,'source_term_sha256':sha_obj(z),'mechanism_id':z.get('mechanism_id'),'source_pair':[z['a'],z['b']] if 'a' in z else None})
after={k:v for k,v in state.items() if k!='terms'}
after.update({'schema':'round78-installed-generalized-state-v1','round78_cross_registry_terms':state.get('round78_cross_registry_terms',0),'round78_online_terms':state.get('round78_online_terms',0)+len(retained_public),'term_count':len(installed_after_terms),'terms':installed_after_terms})
after_pre=[premeta(t) for t in installed_after_terms]
for mech in mechanisms:
 pos={int(c):{q:i for i,q in enumerate(order)} for c,order in mech['source_orders'].items()};covers=[];newcovers=[]
 for t in installed_after_terms:
  if t['sector']!=mech['sector']:continue
  ats=[tuple(x) for x in t['atoms']]
  if all(atom_check(x) in pos and atom_holds(x,pos[atom_check(x)]) for x in ats):covers.append(t['term_id']);newcovers.extend([t['term_id']] if t.get('source_iteration')==iteration else [])
 mech['installed_generalized_cover_ids']=covers;mech['new_retained_cover_ids']=newcovers;mech['installed_generalized_cover_count']=len(covers);mech['new_retained_cover_count']=len(newcovers)
 mech['generalization_disposition']='new_retained_cover' if newcovers else ('dominated_or_duplicate_existing_cover' if covers else 'exact_only_no_safe_generalized_term')
 assert covers or mech['generalization_disposition']=='exact_only_no_safe_generalized_term'

counts=collections.Counter(r['classification'] for r in classifications);candidate_dominates=[]
for x in unique:
 ids=[u['term']['term_id'] for u in inst if set(x['checks']).issubset(u['checks']) and dominates(x,u) and x['key']!=u['key']]
 if ids:candidate_dominates.append({'raw_index':x['index'],'installed_terms_dominated_but_preserved':ids[:50],'count':len(ids)})
dedup={'schema':'round78-online-semantic-dedup-ledger-v1','iteration':iteration,'installed_generalized_before':state['term_count'],'reviewed_iteration78_terms':5743,
 'inherited_round74_retained_terms':state['round74_retained_terms'],'inherited_round76_retained_terms':state.get('round76_retained_terms',0),'previous_round78_cross_registry_terms':state.get('round78_cross_registry_terms',0),'previous_round78_online_terms':state.get('round78_online_terms',0),'raw_term_candidates':len(new),'pair_candidates':len(pair_candidates),'multi_check_candidates':len(multi_candidates),
 'duplicate_old':counts['duplicate_old'],'duplicate_new':counts['duplicate_new'],'dominated_old':counts['dominated_old'],'dominated_new':counts['dominated_new'],'retained_increment':len(retained_public),
 'installed_generalized_after':after['term_count'],'classifications':sorted(classifications,key=lambda x:x['raw_index']),'candidate_dominates_installed_preserved':candidate_dominates,
 'full_evolving_library_union_checks':full_union_checks,'covered_by_full_evolving_union':counts['covered_by_full_evolving_union'],'rejected_zero_domain':counts['rejected_zero_domain'],
 'coverage_difference':[{k:v for k,v in q.items() if k in ('term_id','tuples_instantiated','prior_installed_union_covered_tuples','library_relative_new_tuples','coverage_difference_scope')} for q in tuple_ledgers],
 'semantic_definition':'finite products of exact 720-order masks; single-term dominance plus exact installed-and-current-batch union coverage; pair unions use complete 720-bit rows and multi unions exhaust local membership classes; installed predecessors are never removed'}
for mech in mechanisms:mech['positive_selected_pair_relation_count']=len(mech_pair_keys[mech['mechanism_id']]);mech['positive_finder_miss_is_absence']=False
summary={'schema':'round78-online-generalization-summary-v1','status':'PASS','iteration':iteration,'source_mechanisms':2,'formula_assignment_raw_replays':2,
 'participating_catalogs':len(catalog_public),'local_orders_per_catalog':720,'local_order_records':len(catalog_public)*720,'structural_pair_relations':len(pair_relations),
 'structural_pair_cells_represented':len(pair_relations)*720*720,'positive_pair_relations':sum(bool(x['positive_configuration_count']) for x in pair_relations),
 'unary_only_pair_relations':sum(not x['positive_configuration_count'] for x in pair_relations),'positive_pair_configurations':sum(x['positive_configuration_count'] for x in pair_relations),
 'positive_pair_cells':sum(x['explicit_good_good_cell_count'] for x in pair_relations),'positive_finder_misses':sum(not x['positive_completion_found'] for x in seed_attempts),
 'positive_finder_misses_used_as_absence':0,'multi_check_exact_relations':2,'joint_multi_check_dp':True,'pair_terms_generated':len(pair_candidates),'multi_check_terms_generated':len(multi_candidates),
 'raw_term_candidates':len(new),'retained_increment':len(retained_public),'installed_generalized_before':state['term_count'],'installed_generalized_after':after['term_count'],
 'covered_by_full_evolving_union':counts['covered_by_full_evolving_union'],'multi_union_membership_class_checks':sum(x['method'].startswith('exact_multi') for x in full_union_checks),'zero_domain_candidates_rejected':counts['rejected_zero_domain'],
 'retained_tuples_covered_by_exact_validation':sum(x['tuples_instantiated'] for x in tuple_ledgers),
 'literal_retained_tuple_replays':sum(x['tuples_instantiated'] for x in tuple_ledgers if x['validation_mode']=='literal_every_tuple'),
 'factorized_symbolically_proved_tuples':sum(x['tuples_instantiated'] for x in tuple_ledgers if x['validation_mode']=='factorized_symbolic_universal'),
 'pair_domain_library_relative_new_tuples':sum(x['library_relative_new_tuples'] for x in tuple_ledgers if x['library_relative_new_tuples'] is not None),
 'candidate_exact_blocks_preserved':2,'mechanisms_with_installed_generalized_cover':sum(bool(m['installed_generalized_cover_count']) for m in mechanisms),
 'mechanisms_exact_only':sum(m['generalization_disposition']=='exact_only_no_safe_generalized_term' for m in mechanisms),'weight14_positive_pool_counts':{lab:len(w14[lab]) for lab in ('Xerr','Zerr')},
 'weight14_negative_results_used':0,'zero_truth_cells_used_as_absence':0,'deletion_countertuples_used_as_absence':0,'claim_scope':'positive sound generalization only; no absence or completeness claim'}

dump(OUT/'formula_raw_replay_bindings.json',{'schema':'round78-formula-raw-replay-bindings-v1','records':formula_bindings})
dump(OUT/'mechanisms.json',{'schema':'round78-source-mechanisms-v1','mechanisms':mechanisms})
dump(OUT/'local_order_catalog.json',{'schema':'round78-local-order-catalog-v1','entries':catalog_public})
dump(OUT/'w14_positive_pool.json',{'schema':'round78-positive-weight14-pool-v1','sectors':w14_public,'negative_scope':'only positive validated words are retained; a miss is not absence'})
dump(OUT/'multi_check_relations.json',{'schema':'round78-multi-check-exact-relations-v1','relations':multi_relations})
dump(OUT/'pair_relations.json',{'schema':'round78-positive-pair-relations-v1','relations':pair_relations,'seed_attempts':seed_attempts})
dump(OUT/'raw_term_candidates.json',{'schema':'round78-raw-generalized-candidates-v1','terms':raw_terms})
dump(OUT/'retained_terms.json',{'schema':'round78-retained-generalized-terms-v1','terms':retained_public})
dump(OUT/'tuple_raw_replay.json',{'schema':'round78-retained-tuple-raw-replay-v1','terms':tuple_ledgers,'all_passed':True})
dump(OUT/'dedup_ledger.json',dedup);dump(OUT/'summary.json',summary)
new_registry={'schema':'round78-online-mechanism-registry-v1','mechanism_count':len(registry['mechanisms'])+2,'mechanisms':registry['mechanisms']+[{k:m[k] for k in ('mechanism_id','iteration','sector','canonical_support','canonical_weight','physical_support','physical_weight','sealed_mechanism_sha256')} for m in mechanisms]}
dump(OUT/'generalized_after.json',after);dump(OUT/'mechanism_registry_after.json',new_registry)
# The two state mutations happen only after every formula, term, deletion control and retained tuple has passed.
atomic_dump(a.generalized_state,after);atomic_dump(a.registry_state,new_registry)
result={'schema':'round78-online-generalization-install-v1','status':'PASS','iteration':iteration,'state_before_semantic_sha256':state_before_sha,'state_after_semantic_sha256':sha_obj(after),
 'registry_before_semantic_sha256':registry_before_sha,'registry_after_semantic_sha256':sha_obj(new_registry),'retained_increment':len(retained_public),'generalized_count_after':after['term_count'],
 'mechanism_registry_count_after':new_registry['mechanism_count'],'summary_semantic_sha256':sha_obj(summary),'summary_file_sha256':sha_bytes((OUT/'summary.json').read_bytes()),'strict_order':'outer -> direct X/Z -> raw replay -> candidate-exact pending state -> exact catalogs/relations/raw candidates -> in-memory full evolving-library classification -> exhaustive retained validation -> finalized dedup ledger and pending generalized/registry install'}
dump(OUT/'install_result.json',result);print(json.dumps(result,sort_keys=True))
