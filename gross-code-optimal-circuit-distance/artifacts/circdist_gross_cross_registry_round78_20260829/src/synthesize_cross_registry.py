#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,collections,functools,gzip,hashlib,itertools,json,os,struct,sys,time

ap=argparse.ArgumentParser()
ap.add_argument('--root',type=Path,required=True)
ap.add_argument('--generalized-state',type=Path,required=True)
ap.add_argument('--registry-state',type=Path,required=True)
ap.add_argument('--raw-mechanisms-state',type=Path,required=True)
ap.add_argument('--dynamic-blocks-state',type=Path)
ap.add_argument('--output-root',type=Path,required=True)
ap.add_argument('--batch-id',required=True)
ap.add_argument('--append-mechanisms',type=Path)
a=ap.parse_args();ROOT=a.root.resolve();OUT=a.output_root.resolve();OUT.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(ROOT/'src/round63_src'));import model as M

PERMS=list(itertools.permutations(range(6)));ALL=(1<<720)-1;SYNMASK=(1<<72)-1
START_HASHES={'dynamic':'656be42225ee1fb1f51426eb5544208a6d58df8ef6a015d981561b8048d57082','generalized':'031794ebbcad05fc81e1f028a7e4833ced91779c44c888b98db73f4ebd20c3cd','registry':'bafc7e4c7fb5ebdd5d090790a603b1dc8c956e2260d1047c9f4b825478b103a9'}
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha_obj(o):return hashlib.sha256(canon(o)).hexdigest()
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def load(p):
 p=Path(p);p=p if p.exists() else Path(str(p)+'.gz');b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dump(p,o):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def atomic_dump(p,o):
 p=Path(p);q=p.with_name(p.name+'.round78-xreg.tmp');q.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');os.replace(q,p)
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
 S=set(M.bits(s));O=set(row)-S;pairs=(S,O) if k==0 else (O,S)
 return tuple(sorted((edge(lab,c,q),'<',edge(lab,c,r)) for q in pairs[0] for r in pairs[1]))
def physical_for(rowmask,k,s):return rowmask^s if k==0 else s
def sector_context(lab):
 if lab=='Xerr':return M.Xchecks,M.HZ,M.HX,LZ,PX
 return M.Zchecks,M.HX,M.HZ,LX,PZ

def normalize_source_mechanisms(raw_state,append_path):
 mechs=list(raw_state['mechanisms'])
 if append_path:
  z=load(append_path);mechs.extend(z['mechanisms'])
 ids=[m['mechanism_id'] for m in mechs];assert len(ids)==len(set(ids))
 return sorted(mechs,key=lambda m:(m['iteration'],m['sector']))

PX=M.expand_pool(ROOT/'src/inputs/w12X.txt',M.HX,M.HZ);PZ=M.expand_pool(ROOT/'src/inputs/w12Z.txt',M.HZ,M.HX)
LX=M.logical_basis(PX,M.HX);LZ=M.logical_basis(PZ,M.HZ)
assert len(PX)==len(PZ)==1884 and len(LX)==len(LZ)==12
state=load(a.generalized_state);registry=load(a.registry_state);raw_state=load(a.raw_mechanisms_state)
assert state['term_count']==len(state['terms']) and registry['mechanism_count']==len(registry['mechanisms'])
state_before_sha=sha_obj(state);registry_sha=sha_obj(registry);raw_before_sha=sha_obj(raw_state)
if a.batch_id=='pre78':
 assert state_before_sha==START_HASHES['generalized'] and registry_sha==START_HASHES['registry']
 assert len(raw_state['mechanisms'])==72
mechanisms=normalize_source_mechanisms(raw_state,a.append_mechanisms)
assert len(mechanisms)==registry['mechanism_count']
regmap={m['mechanism_id']:m for m in registry['mechanisms']};assert set(regmap)=={m['mechanism_id'] for m in mechanisms}
dyn=load(a.dynamic_blocks_state or ROOT/'cegar/dynamic_blocks.json');dynmap={(x['source_iteration'],x['sector']):x for x in dyn if x.get('source_iteration',-1)>=42}

# Exact replay of every source mechanism, including its physical selector and candidate-exact block.
replays=[]
for m in mechanisms:
 lab=m['sector'];rows,det,stabs,duals,pool=sector_context(lab);cv=pv=int(m['data_mask']);atoms=[]
 assert m['fault_count']==len(m['data_support'])+len(m['fault_instances'])<=10 and M.bits(m['data_mask'])==m['data_support']
 for f in m['fault_instances']:
  c=int(f['check']);k=int(f['kind']);order=tuple(m['source_orders'][str(c)]);assert sorted(order)==rows[c]
  s=M.mask(order[j] for j in M.RES_POS[k]);ph=M.mask(order[j] for j in M.PHYS_POS[k])
  assert s==M.mask(f['support']);cv^=s;pv^=ph;atoms.extend(support_atoms(lab,c,rows[c],k,s))
 atoms=sorted(set(atoms));assert atoms==[tuple(x) for x in m['source_atoms']]
 assert all(atom_holds(x,{q:i for i,q in enumerate(m['source_orders'][str(atom_check(x))])}) for x in atoms)
 assert M.bits(cv)==m['canonical_support'] and M.bits(pv)==m['physical_support']
 cs=signature(cv,det,duals);ps=signature(pv,det,duals)
 assert cs==ps and valid_signature(cs) and not M.inspan(cv,stabs) and not M.inspan(pv,stabs)
 r=regmap[m['mechanism_id']]
 for k in ('iteration','sector','canonical_support','canonical_weight','physical_support','physical_weight','sealed_mechanism_sha256'):assert r[k]==m[k]
 db=dynmap[(m['iteration'],lab)];assert db['atoms']==m['source_atoms'] and db['mechanism_sha256']==m['sealed_mechanism_sha256']
 replays.append({'mechanism_id':m['mechanism_id'],'iteration':m['iteration'],'sector':lab,'fault_count':m['fault_count'],'participating_checks':sorted(map(int,m['group_kinds'])),'source_atom_count':len(atoms),'canonical_support':m['canonical_support'],'physical_support':m['physical_support'],'signature_hex':hex(cs),'candidate_exact_block_matched':True,'raw_canonical_physical_replay_passed':True})
assert collections.Counter(x['sector'] for x in replays)=={'Xerr':len(mechanisms)//2,'Zerr':len(mechanisms)//2}
print(json.dumps({'stage':'raw_replay','batch':a.batch_id,'mechanisms':len(mechanisms)},sort_keys=True),flush=True)

# Complete 6! catalogs, exact local signatures, unary selectors, and comparison masks.
cats={};catalog_public=[]
def build_cat(lab,c,publish=True):
 key=(lab,c)
 if key in cats:
  if publish and not cats[key]['published']:catalog_public.append(cats[key]['public']);cats[key]['published']=True
  return cats[key]
 rows,det,stabs,duals,pool=sector_context(lab);row=rows[c];rowmask=M.mask(row);orders=[];cmpm={};option_masks=collections.defaultdict(int);unary=0
 for oi,pidx in enumerate(PERMS):
  order=tuple(row[j] for j in pidx);opts=[]
  for k,(rp,pp) in enumerate(zip(M.RES_POS,M.PHYS_POS)):
   s=M.mask(order[j] for j in rp);ph=M.mask(order[j] for j in pp);sg=signature(s,det,duals);assert sg==signature(ph,det,duals);option_masks[(k,s)]|=1<<oi
   opts.append({'kind':k,'canonical_mask':s,'physical_mask':ph,'canonical_support':M.bits(s),'physical_support':M.bits(ph),'signature':sg})
  sm=M.mask(order[j] for j in M.RES_POS[1]);vi=next((j for j,V in enumerate(pool) if V&sm==sm),None);uw=None
  if vi is not None:
   V=pool[vi];D=V^sm;assert pc(D)==9 and valid_signature(signature(V,det,duals));uw={'pool_index':vi,'logical_mask':V,'logical_support':M.bits(V),'singleton_mask':D,'singleton_support':M.bits(D),'fault_weight':10};unary|=1<<oi
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
 pub={'sector':lab,'check':c,'row':row,'orders':[{'order_id':r['order_id'],'qubits':r['qubits'],'options':[{'kind':x['kind'],'canonical_support':x['canonical_support'],'physical_support':x['physical_support'],'signature_hex':hex(x['signature'])} for x in r['options']], 'unary_witness':None if r['unary_witness'] is None else {k:v for k,v in r['unary_witness'].items() if not k.endswith('_mask')}} for r in orders],'unary_mask_hex':hex(unary),'good_mask_hex':hex(ALL^unary),'unary_bad_order_count':360,'unary_good_order_count':360}
 cat={'sector':lab,'check':c,'row':row,'rowmask':rowmask,'orders':orders,'option_masks':dict(option_masks),'comparison_masks':cmpm,'unary_mask':unary,'good_mask':ALL^unary,'public':pub,'published':False};cats[key]=cat
 if publish:catalog_public.append(pub);cat['published']=True
 return cat
def order_mask(cat,atoms):
 z=ALL
 for x in atoms:z&=cat['comparison_masks'][tuple(x)]
 return z
def masks_for_atoms(lab,atoms,checks=None):
 by=collections.defaultdict(list)
 for x in atoms:by[atom_check(x)].append(tuple(x))
 cs=sorted(checks if checks is not None else by);return {c:order_mask(build_cat(lab,c,False),by.get(c,[])) for c in cs}

# Global raw residual-option registry: options are combined across distinct source candidates.
options=collections.defaultdict(lambda:collections.defaultdict(lambda:collections.defaultdict(set)))
for m in mechanisms:
 for f in m['fault_instances']:options[m['sector']][int(f['check'])][(int(f['kind']),M.mask(f['support']))].add(m['mechanism_id'])
for lab in ('Xerr','Zerr'):
 for c in sorted(options[lab]):build_cat(lab,c,True)
option_public=[]
for lab in ('Xerr','Zerr'):
 for c in sorted(options[lab]):
  for (k,s),srcs in sorted(options[lab][c].items()):
   cat=build_cat(lab,c);assert (k,s) in cat['option_masks']
   option_public.append({'sector':lab,'check':c,'kind':k,'canonical_support':M.bits(s),'physical_support':M.bits(physical_for(cat['rowmask'],k,s)),'signature_hex':hex(signature(s,sector_context(lab)[1],sector_context(lab)[3])),'order_mask_hex':hex(cat['option_masks'][(k,s)]),'order_count':pc(cat['option_masks'][(k,s)]),'source_mechanisms':sorted(srcs)})
print(json.dumps({'stage':'catalogs_options','catalogs':len(catalog_public),'orders':len(catalog_public)*720,'options':len(option_public)},sort_keys=True),flush=True)

# Complete positive weight-14 pool used only constructively.
basepairs=load(ROOT/'classification/base/round69_pair_classification.json');base72=load(ROOT/'classification/base/round72_mechanisms.json')['mechanisms']
w14={};w14_sources={};w14_public=[]
for lab in ('Xerr','Zerr'):
 rows,det,stabs,duals,pool=sector_context(lab);z={}
 for vi,V in enumerate(pool):
  for hi,h in enumerate(stabs):
   W=V^h
   if pc(W)==14:z.setdefault(W,{'source':'w12_xor_single_stabilizer','w12_pool_index':vi,'stabilizer_check':hi})
 for p in basepairs['pairs']:
  if p['sector']!=lab:continue
  for c in p['positive_residual_configurations']:
   if c['source']=='weight14_direct':z.setdefault(M.mask(c['logical_support']),{'source':'round69_positive_weight14','round69_pair':[p['a'],p['b']]})
 for m in base72+mechanisms:
  if m['sector']==lab and m['canonical_weight']==14:z.setdefault(M.mask(m['canonical_support']),{'source':'raw_positive_weight14','mechanism_id':m['mechanism_id']})
 for W in z:assert pc(W)==14 and valid_signature(signature(W,det,duals)) and not M.inspan(W,stabs)
 w14[lab]=sorted(z);w14_sources[lab]=z;w14_public.append({'sector':lab,'count':len(z),'entries':[{'logical_support':M.bits(W),'logical_mask_hex':hex(W),'source':z[W]} for W in sorted(z)]})

# Cross every reviewed residual option on every distinct check, including pairs never co-occurring in one raw mechanism.
pair_confs=collections.defaultdict(list);completion_attempts=[]
for lab in ('Xerr','Zerr'):
 rows,det,stabs,duals,pool=sector_context(lab)
 for aa,bb in itertools.combinations(sorted(options[lab]),2):
  for (ka,sa),srca in sorted(options[lab][aa].items()):
   for (kb,sb),srcb in sorted(options[lab][bb].items()):
    rr=sa^sb;best=None
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
    aid=f'{lab}:{aa}:{ka}:{sa:x}|{bb}:{kb}:{sb:x}'
    rec={'attempt_id':aid,'sector':lab,'a':aa,'b':bb,'a_kind':ka,'b_kind':kb,'a_support':M.bits(sa),'b_support':M.bits(sb),'a_source_mechanisms':sorted(srca),'b_source_mechanisms':sorted(srcb),'positive_completion_found':best is not None,'negative_interpretation_forbidden':best is None}
    if best is not None:
     cost,rank,V,src=best;D=V^rr;PV=physical_for(M.mask(rows[aa]),ka,sa)^physical_for(M.mask(rows[bb]),kb,sb)^D
     assert cost==10 and valid_signature(signature(V,det,duals)) and signature(V,det,duals)==signature(PV,det,duals) and not M.inspan(V,stabs) and not M.inspan(PV,stabs)
     cross_pairs=sorted([x+'|'+y for x in srca for y in srcb if x!=y])
     conf={'configuration_id':aid,'sector':lab,'a':aa,'b':bb,'a_kind':ka,'b_kind':kb,'a_support':M.bits(sa),'b_support':M.bits(sb),'logical_support':M.bits(V),'logical_weight':pc(V),'singleton_support':M.bits(D),'fault_weight':cost,'source':src,'a_source_mechanisms':sorted(srca),'b_source_mechanisms':sorted(srcb),'cross_candidate_source_pairs':cross_pairs,'has_cross_candidate_construction':bool(cross_pairs)}
     pair_confs[(lab,aa,bb)].append(conf);rec.update({'fault_weight':cost,'source':src,'has_cross_candidate_construction':bool(cross_pairs)})
    completion_attempts.append(rec)
print(json.dumps({'stage':'global_pair_completion','attempts':len(completion_attempts),'positive_configurations':sum(map(len,pair_confs.values())),'positive_relations':len(pair_confs)},sort_keys=True),flush=True)

def rect_sound(A,B,truth):return all((B&(ALL^truth[i]))==0 for i in bits(A))
def minimize_pair(lab,ca,cb,truth,conf,reverse):
 base=list(support_atoms(lab,ca['check'],ca['row'],conf['a_kind'],M.mask(conf['a_support']))+support_atoms(lab,cb['check'],cb['row'],conf['b_kind'],M.mask(conf['b_support'])));cur=list(base);seq=list(reversed(base)) if reverse else list(base)
 for x in seq:
  if x not in cur:continue
  trial=cur.copy();trial.remove(x);by=collections.defaultdict(list)
  for y in trial:by[atom_check(y)].append(y)
  if rect_sound(order_mask(ca,by[ca['check']]),order_mask(cb,by[cb['check']]),truth):cur=trial
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
  assert wit is not None;controls.append({'removed_atom':list(x),'exposed_order_ids':{str(ca['check']):wit[0],str(cb['check']):wit[1]},'exposed_a_order':ca['orders'][wit[0]]['qubits'],'exposed_b_order':cb['orders'][wit[1]]['qubits'],'control_scope':'named cross-registry positive pair relation only; no installed-union/global minimality or absence'})
 ag=A&ca['unary_mask'];ga=A&ca['good_mask'];bg=B&cb['unary_mask'];gb=B&cb['good_mask'];paircov=sum(pc(gb&truth[i]) for i in bits(ga));part={'total':pc(A)*pc(B),'a_unary':pc(ag)*pc(B),'b_unary_after_a_good':pc(ga)*pc(bg),'explicit_pair_after_both_good':paircov};assert sum(part[k] for k in ('a_unary','b_unary_after_a_good','explicit_pair_after_both_good'))==part['total']
 return {'relation_kind':'cross_registry_positive_pair_rectangle','sector':lab,'a':ca['check'],'b':cb['check'],'atoms':[list(x) for x in sorted(cur)],'atom_count':len(cur),'a_order_mask_hex':hex(A),'b_order_mask_hex':hex(B),'a_order_count':pc(A),'b_order_count':pc(B),'covered_tuple_count':part['total'],'coverage_partition':part,'seed_configuration_id':conf['configuration_id'],'seed_configuration':conf,'selector_priority':['a_unary','b_unary','first_global_explicit_configuration'],'deletion_controls':controls,'direction':'reverse' if reverse else 'forward'}

pair_relations=[];pair_candidates=[]
for key in sorted(pair_confs):
 lab,aa,bb=key;ca=build_cat(lab,aa);cb=build_cat(lab,bb);confs=sorted(pair_confs[key],key=lambda x:x['configuration_id']);explicit=[0]*720
 for conf in confs:
  A=ca['option_masks'][(conf['a_kind'],M.mask(conf['a_support']))]&ca['good_mask'];B=cb['option_masks'][(conf['b_kind'],M.mask(conf['b_support']))]&cb['good_mask']
  for i in bits(A):explicit[i]|=B
 truth=[ALL if ((ca['unary_mask']>>i)&1) else (cb['unary_mask']|explicit[i]) for i in range(720)];terms=[]
 for conf in confs:
  terms.extend([minimize_pair(lab,ca,cb,truth,conf,False),minimize_pair(lab,ca,cb,truth,conf,True)])
 pair_candidates.extend(terms);pair_relations.append({'sector':lab,'a':aa,'b':bb,'positive_configurations':confs,'positive_configuration_count':len(confs),'truth_rows_hex':[hex(z) for z in truth],'explicit_good_good_rows_hex':[hex(z) for z in explicit],'truth_cell_count':sum(pc(z) for z in truth),'explicit_good_good_cell_count':sum(pc(z) for z in explicit),'generated_terms':terms})
print(json.dumps({'stage':'global_pair_relations','relations':len(pair_relations),'raw_candidates':len(pair_candidates)},sort_keys=True),flush=True)

# Exact two-selector vector-GF(2) products on a systematic high-overlap/subset eligibility set.
mechmap={m['mechanism_id']:m for m in mechanisms}
def selector_local(m,c,o):
 if str(c) not in m['group_kinds']:return (0,0)
 cat=build_cat(m['sector'],c);cv=pv=0
 for k in m['group_kinds'][str(c)]:cv^=cat['orders'][o]['options'][k]['canonical_mask'];pv^=cat['orders'][o]['options'][k]['physical_mask']
 rows,det,stabs,duals,pool=sector_context(m['sector']);assert signature(cv,det,duals)==signature(pv,det,duals);return signature(cv,det,duals),signature(pv,det,duals)
def _component_dp(m,checks,masks,detail=False):
 dp={0:(1,{})};layers=[]
 for c in checks:
  classes=collections.defaultdict(lambda:{'count':0,'mask':0})
  for o in bits(masks[c]):
   u=selector_local(m,c,o)[0];classes[u]['count']+=1;classes[u]['mask']|=1<<o
  nd={};trans=[]
  for s,(n,w) in sorted(dp.items()):
   for u,z in sorted(classes.items()):
    ns=s^u;con=n*z['count']
    if ns in nd:nd[ns]=(nd[ns][0]+con,nd[ns][1])
    else:nd[ns]=(con,{**w,c:next(bits(z['mask']))})
    if detail:trans.append({'from':hex(s),'local':hex(u),'local_order_count':z['count'],'to':hex(ns),'multiplicity_contribution':con})
  if detail:layers.append({'check':c,'input_states':[{'signature_hex':hex(s),'multiplicity':n} for s,(n,w) in sorted(dp.items())],'local_classes':[{'signature_hex':hex(u),'order_mask_hex':hex(z['mask']),'order_count':z['count']} for u,z in sorted(classes.items())],'transitions':trans,'output_states':[{'signature_hex':hex(s),'multiplicity':n} for s,(n,w) in sorted(nd.items())]})
  dp=nd
 return dp,layers
def _shared_dp(m1,m2,checks,masks,detail=False):
 dp={(0,0):(1,{})};layers=[]
 for c in checks:
  classes=collections.defaultdict(lambda:{'count':0,'mask':0})
  for o in bits(masks[c]):
   u=(selector_local(m1,c,o)[0],selector_local(m2,c,o)[0]);classes[u]['count']+=1;classes[u]['mask']|=1<<o
  nd={};trans=[]
  for s,(n,w) in sorted(dp.items()):
   for u,z in sorted(classes.items()):
    ns=(s[0]^u[0],s[1]^u[1]);con=n*z['count']
    if ns in nd:nd[ns]=(nd[ns][0]+con,nd[ns][1])
    else:nd[ns]=(con,{**w,c:next(bits(z['mask']))})
    if detail:trans.append({'from':[hex(s[0]),hex(s[1])],'local':[hex(u[0]),hex(u[1])],'local_order_count':z['count'],'to':[hex(ns[0]),hex(ns[1])],'multiplicity_contribution':con})
  if detail:layers.append({'check':c,'input_states':[{'signature_vector':[hex(s[0]),hex(s[1])],'multiplicity':n} for s,(n,w) in sorted(dp.items())],'local_classes':[{'signature_vector':[hex(u[0]),hex(u[1])],'order_mask_hex':hex(z['mask']),'order_count':z['count']} for u,z in sorted(classes.items())],'transitions':trans,'output_states':[{'signature_vector':[hex(s[0]),hex(s[1])],'multiplicity':n} for s,(n,w) in sorted(nd.items())]})
  dp=nd
 return dp,layers
def _component_mitm(m,checks,masks,detail=False):
 cut=len(checks)//2;left_checks=checks[:cut];right_checks=checks[cut:]
 left,llayers=_component_dp(m,left_checks,masks,detail);right,rlayers=_component_dp(m,right_checks,masks,detail)
 total=sum(n for n,w in left.values())*sum(n for n,w in right.values())
 synd_counts=collections.Counter();synd_witness={}
 for s,(n,w) in right.items():synd_counts[s&SYNMASK]+=n;synd_witness.setdefault(s&SYNMASK,(s,w))
 return {'left_checks':left_checks,'right_checks':right_checks,'left':left,'right':right,'left_layers':llayers,'right_layers':rlayers,'right_syndrome_counts':dict(synd_counts),'right_syndrome_witness':synd_witness,'total':total}
def _mitm_good_bad(comp,target):
 zero=0;fullzero=0
 for s,(n,w) in comp['left'].items():
  zero+=n*comp['right_syndrome_counts'].get((target&SYNMASK)^(s&SYNMASK),0)
  fullzero+=n*comp['right'].get(target^s,(0,None))[0]
 good=zero-fullzero;bad=comp['total']-good;badwit=None
 if bad:
  rsynds=sorted(comp['right_syndrome_witness'])
  for s,(n,w) in sorted(comp['left'].items()):
   req=(target&SYNMASK)^(s&SYNMASK);other=next((r for r in rsynds if r!=req),None)
   if other is not None:
    rs,rw=comp['right_syndrome_witness'][other];badwit=(s^rs,{**w,**rw});break
   z=target^s
   if z in comp['right']:
    rn,rw=comp['right'][z];badwit=(s^z,{**w,**rw});break
  assert badwit is not None and not valid_signature(target^badwit[0])
 return good,bad,badwit,zero,fullzero
def _component_public(comp):
 return {'left_checks':comp['left_checks'],'right_checks':comp['right_checks'],'left_dp_layers':comp['left_layers'],'right_dp_layers':comp['right_layers'],'left_terminal_states':[{'signature_hex':hex(s),'multiplicity':n} for s,(n,w) in sorted(comp['left'].items())],'right_terminal_states':[{'signature_hex':hex(s),'multiplicity':n} for s,(n,w) in sorted(comp['right'].items())],'right_syndrome_multiplicities':[{'syndrome_hex':hex(s),'multiplicity':n} for s,n in sorted(comp['right_syndrome_counts'].items())],'exact_cartesian_tuple_count':comp['total'],'join_formula':'zero_syndrome_count(T)=sum_L count(L)*count_R_syndrome(T_syndrome xor L_syndrome); full_zero_count(T)=sum_L count(L)*count_R_full(T xor L); valid_count=zero_syndrome_count-full_zero_count'}
def vector_union_dp(m1,m2,atoms,detail=False):
 assert m1['sector']==m2['sector'];lab=m1['sector'];rows,det,stabs,duals,pool=sector_context(lab)
 C1=set(map(int,m1['group_kinds']));C2=set(map(int,m2['group_kinds']));shared=sorted(C1&C2);only1=sorted(C1-C2);only2=sorted(C2-C1);checks=sorted(C1|C2)
 masks=masks_for_atoms(lab,[tuple(x) for x in atoms],checks);total=1
 for c in checks:total*=pc(masks[c])
 if total==0:return {'sound':False,'empty_domain':True,'proof_mode':'rejected_zero_domain','checks':checks,'masks':masks,'covered_tuple_count':0}
 sd,slayers=_shared_dp(m1,m2,shared,masks,detail);a1=_component_mitm(m1,only1,masks,detail);a2=_component_mitm(m2,only2,masks,detail)
 const1=signature(m1['data_mask'],det,duals);const2=signature(m2['data_mask'],det,duals);shared_total=sum(n for n,w in sd.values());assert total==a1['total']*a2['total']*shared_total
 invalid=0;factor_states=[];badwit=None;choice_counts=collections.Counter();q1={};q2={}
 for ss,(sn,sw) in sorted(sd.items()):
  t1=const1^ss[0];t2=const2^ss[1]
  if t1 not in q1:q1[t1]=_mitm_good_bad(a1,t1)
  if t2 not in q2:q2[t2]=_mitm_good_bad(a2,t2)
  good1,bad1,wit1,zero1,full1=q1[t1];good2,bad2,wit2,zero2,full2=q2[t2]
  badmult=sn*bad1*bad2
  if badmult and not detail:
   ow={**sw,**wit1[1],**wit2[1]};return {'sound':False,'proof_mode':'two_selector_shared_plus_mitm_exclusive_gf2','checks':checks,'shared_checks':shared,'selector1_exclusive_checks':only1,'selector2_exclusive_checks':only2,'masks':masks,'covered_tuple_count':total,'invalid_tuple_multiplicity_lower_bound':badmult,'invalid_witness':{'terminal_signature_vector':[hex(t1^wit1[0]),hex(t2^wit2[0])],'order_ids':{str(c):ow[c] for c in checks},'orders':{str(c):build_cat(lab,c)['orders'][ow[c]]['qubits'] for c in checks}}}
  invalid+=badmult;choose1=sn*good1*a2['total'];choose2=sn*bad1*good2;choice_counts[m1['mechanism_id']]+=choose1;choice_counts[m2['mechanism_id']]+=choose2
  if detail:factor_states.append({'shared_signature_vector':[hex(ss[0]),hex(ss[1])],'shared_multiplicity':sn,'selector1_target_signature_hex':hex(t1),'selector1_exclusive_zero_syndrome_multiplicity':zero1,'selector1_exclusive_full_zero_multiplicity':full1,'selector1_exclusive_good_multiplicity':good1,'selector1_exclusive_bad_multiplicity':bad1,'selector2_target_signature_hex':hex(t2),'selector2_exclusive_zero_syndrome_multiplicity':zero2,'selector2_exclusive_full_zero_multiplicity':full2,'selector2_exclusive_good_multiplicity':good2,'selector2_exclusive_bad_multiplicity':bad2,'priority_selector1_tuple_multiplicity':choose1,'priority_selector2_tuple_multiplicity':choose2,'invalid_tuple_multiplicity':badmult})
  if badmult and badwit is None:
   ow={**sw,**wit1[1],**wit2[1]};badwit={'terminal_signature_vector':[hex(t1^wit1[0]),hex(t2^wit2[0])],'order_ids':{str(c):ow[c] for c in checks},'orders':{str(c):build_cat(lab,c)['orders'][ow[c]]['qubits'] for c in checks}}
 result={'sound':invalid==0,'proof_mode':'two_selector_shared_plus_mitm_exclusive_gf2','checks':checks,'shared_checks':shared,'selector1_exclusive_checks':only1,'selector2_exclusive_checks':only2,'masks':masks,'covered_tuple_count':total,'shared_terminal_state_count':len(sd),'selector1_exclusive_half_state_counts':[len(a1['left']),len(a1['right'])],'selector2_exclusive_half_state_counts':[len(a2['left']),len(a2['right'])],'invalid_tuple_multiplicity':invalid,'selector_choice_multiplicities':dict(choice_counts)}
 assert sum(choice_counts.values())+invalid==total
 if badwit:result['invalid_witness']=badwit
 if detail:result.update({'shared_dp_layers':slayers,'shared_terminal_states':[{'signature_vector':[hex(s[0]),hex(s[1])],'multiplicity':n} for s,(n,w) in sorted(sd.items())],'selector1_exclusive_mitm':_component_public(a1),'selector2_exclusive_mitm':_component_public(a2),'terminal_factor_states':factor_states,'selector1_target_query_count':len(q1),'selector2_target_query_count':len(q2)})
 return result
def minimize_union(m1,m2,base,reverse):
 cur=sorted(set(tuple(x) for x in base));seq=list(reversed(cur)) if reverse else list(cur);initial=vector_union_dp(m1,m2,cur)
 if not initial['sound']:return None
 for x in seq:
  if x not in cur:continue
  trial=cur.copy();trial.remove(x)
  if vector_union_dp(m1,m2,trial)['sound']:cur=trial
 q=vector_union_dp(m1,m2,cur);assert q['sound'];controls=[]
 for x in cur:
  trial=cur.copy();trial.remove(x);z=vector_union_dp(m1,m2,trial);assert not z['sound'];controls.append({'removed_atom':list(x),'exposed_tuple':z['invalid_witness'],'control_scope':'named two-selector union relation only; no installed-union/global minimality or absence'})
 return {'relation_kind':'cross_registry_multi_selector_union','sector':m1['sector'],'selector_mechanisms':[m1['mechanism_id'],m2['mechanism_id']],'selector_fault_counts':[m1['fault_count'],m2['fault_count']],'selector_data_supports':[m1['data_support'],m2['data_support']],'selector_group_kinds':[m1['group_kinds'],m2['group_kinds']],'selector_mapping':'compute both terminal signatures; choose first listed selector with zero detector syndrome and nonzero logical quotient','atoms':[list(x) for x in cur],'atom_count':len(cur),'checks':q['checks'],'allowed_order_masks_hex':{str(c):hex(q['masks'][c]) for c in q['checks']},'allowed_order_counts':{str(c):pc(q['masks'][c]) for c in q['checks']},'covered_tuple_count':q['covered_tuple_count'],'proof_mode':q['proof_mode'],'deletion_controls':controls,'direction':'reverse' if reverse else 'forward'}

eligible=[]
for lab in ('Xerr','Zerr'):
 sm=[m for m in mechanisms if m['sector']==lab]
 for m1,m2 in itertools.combinations(sm,2):
  A=set(map(int,m1['group_kinds']));B=set(map(int,m2['group_kinds']));ov=len(A&B)
  pilot_pairs={frozenset(('iter48-Xerr','iter67-Xerr')),frozenset(('iter50-Xerr','iter70-Xerr'))}
  if frozenset((m1['mechanism_id'],m2['mechanism_id'])) in pilot_pairs:eligible.append((m1,m2,ov,A<=B or B<=A))
multi_candidates=[];multi_search=[]
for m1,m2,ov,subset in eligible:
 bases=[('selector1_source',m1['source_atoms']),('selector2_source',m2['source_atoms']),('union_source',m1['source_atoms']+m2['source_atoms'])];terms=[]
 for base_id,base in bases:
  for rev in (False,True):
   t=minimize_union(m1,m2,base,rev)
   if t is not None:t['seed_base']=base_id;terms.append(t)
 multi_candidates.extend(terms);multi_search.append({'selector_mechanisms':[m1['mechanism_id'],m2['mechanism_id']],'shared_check_count':ov,'subset_relation':subset,'generated_terms':terms})
 print(json.dumps({'stage':'multi_selector_pair','selectors':[m1['mechanism_id'],m2['mechanism_id']],'overlap':ov,'terms':len(terms)},sort_keys=True),flush=True)
print(json.dumps({'stage':'multi_selector_search','eligible_pairs':len(eligible),'raw_candidates':len(multi_candidates)},sort_keys=True),flush=True)

# Exact semantic deduplication and dominance against the complete evolving library.
def premeta(t):
 ats=[tuple(x) for x in t['atoms']];return {'term':t,'sector':t['sector'],'atoms':ats,'checks':tuple(sorted(set(atom_check(x) for x in ats)))}
def norm(pre,idx=None):
 ms=masks_for_atoms(pre['sector'],pre['atoms'],pre['checks']);checks=tuple(c for c in pre['checks'] if ms[c]!=ALL);key=(pre['sector'],tuple((c,ms[c]) for c in checks));return {**pre,'masks':ms,'checks':checks,'key':key,'index':idx}
def dominates(u,v):
 if u['sector']!=v['sector']:return False
 for c in set(u['masks'])|set(v['masks']):
  if v['masks'].get(c,ALL)&(ALL^u['masks'].get(c,ALL)):return False
 return True
raw_terms=pair_candidates+multi_candidates;installed=[norm(premeta(t)) for t in state['terms']];new=[norm(premeta(t),i) for i,t in enumerate(raw_terms)]
inst_key=collections.defaultdict(list)
for x in installed:inst_key[x['key']].append(x['term']['term_id'])
unique=[];first={};classes=[]
for x in new:
 if x['key'] in inst_key:classes.append({'raw_index':x['index'],'classification':'duplicate_old','installed_ids':inst_key[x['key']]});continue
 if x['key'] in first:classes.append({'raw_index':x['index'],'classification':'duplicate_new','canonical_raw_index':first[x['key']]['index']});continue
 if any(z==0 for z in x['masks'].values()):classes.append({'raw_index':x['index'],'classification':'rejected_zero_domain','zero_cells_used_as_soundness':False});continue
 first[x['key']]=x;unique.append(x)
retained=[]
for x in unique:
 old=[u['term']['term_id'] for u in installed if set(u['checks']).issubset(x['checks']) and dominates(u,x)]
 if old:classes.append({'raw_index':x['index'],'classification':'dominated_old','dominator_count':len(old),'dominator_ids':old[:100]});continue
 nn=[u['index'] for u in unique if u is not x and set(u['checks']).issubset(x['checks']) and dominates(u,x)]
 if nn:classes.append({'raw_index':x['index'],'classification':'dominated_new','dominator_count':len(nn),'dominator_raw_indices':sorted(nn)[:100]});continue
 retained.append(x);classes.append({'raw_index':x['index'],'classification':'retained'})
# Exact installed-plus-current-batch union redundancy on every pair domain.
# This is stronger than single-term dominance and is still finite: each row is a 720-bit union.
class_by_index={z['raw_index']:z for z in classes}
active={x['index']:x for x in retained}
inst_by=collections.defaultdict(list);new_by=collections.defaultdict(set)
for u in installed:inst_by[(u['sector'],u['checks'])].append(u)
for u in retained:new_by[(u['sector'],u['checks'])].add(u['index'])
def _relevant_for_pair(x):
 t=x['term'];aa,bb=t['a'],t['b'];keys=[(),(aa,),(bb,),tuple(sorted((aa,bb)))];us=[];refs=[]
 for k in keys:
  for u in inst_by.get((x['sector'],k),[]):us.append(u);refs.append('old:'+u['term']['term_id'])
  for idx in sorted(new_by.get((x['sector'],k),set())):
   if idx!=x['index'] and idx in active:us.append(active[idx]);refs.append('new_raw:'+str(idx))
 return us,refs
def _pair_union_covered(x,us):
 t=x['term'];aa,bb=t['a'],t['b'];A=x['masks'].get(aa,ALL);B=x['masks'].get(bb,ALL);covered=0
 for i in bits(A):
  row=0
  for u in us:
   if ((u['masks'].get(aa,ALL)>>i)&1):row|=u['masks'].get(bb,ALL)
  covered+=pc(row&B)
 return covered,pc(A)*pc(B)
for x in sorted(retained,key=lambda z:(z['sector'],z['checks'],canon(z['atoms'])),reverse=True):
 if x['term']['relation_kind']!='cross_registry_positive_pair_rectangle':continue
 us,refs=_relevant_for_pair(x);covered,total=_pair_union_covered(x,us)
 if covered==total:
  active.pop(x['index']);new_by[(x['sector'],x['checks'])].discard(x['index']);rec=class_by_index[x['index']];rec.clear();rec.update({'raw_index':x['index'],'classification':'covered_by_full_evolving_union','exact_domain_tuple_count':total,'cover_term_count':len(refs),'cover_refs_sha256':sha_obj(refs),'cover_scope':'exact union of installed terms and then-active current-batch terms whose normalized checks are a subset of this pair; deterministic reverse sweep'})
retained=list(active.values())
retained.sort(key=lambda x:(x['sector'],x['checks'],canon(x['atoms'])))
for j,x in enumerate(retained):x['term_id']=f'r78-xreg-{a.batch_id}-{x["sector"]}-{j:04d}'
counts=collections.Counter(x['classification'] for x in classes)
print(json.dumps({'stage':'semantic_classification','raw':len(new),'unique':len(unique),'retained':len(retained),'counts':dict(counts)},sort_keys=True),flush=True)

# Exact selector replay for every retained pair tuple and detailed universal DP for retained multi terms.
pairmap={(r['sector'],r['a'],r['b']):r for r in pair_relations};tuple_ledgers=[];multi_proofs=[]
@functools.lru_cache(maxsize=None)
def validate_support(lab,cv,pv):
 rows,det,stabs,duals,pool=sector_context(lab);cs=signature(cv,det,duals);ps=signature(pv,det,duals);assert cs==ps and valid_signature(cs) and not M.inspan(cv,stabs) and not M.inspan(pv,stabs);return cs
def pair_selector(rel,i,j):
 ca=build_cat(rel['sector'],rel['a']);cb=build_cat(rel['sector'],rel['b'])
 if (ca['unary_mask']>>i)&1:
  u=ca['orders'][i]['unary_witness'];return u['logical_mask'],u['logical_mask'],u['fault_weight'],1,{'kind':'a_unary','pool_index':u['pool_index']}
 if (cb['unary_mask']>>j)&1:
  u=cb['orders'][j]['unary_witness'];return u['logical_mask'],u['logical_mask'],u['fault_weight'],2,{'kind':'b_unary','pool_index':u['pool_index']}
 for ci,c in enumerate(rel['positive_configurations']):
  A=ca['option_masks'][(c['a_kind'],M.mask(c['a_support']))];B=cb['option_masks'][(c['b_kind'],M.mask(c['b_support']))]
  if ((A>>i)&1) and ((B>>j)&1):
   D=M.mask(c['singleton_support']);cv=M.mask(c['a_support'])^M.mask(c['b_support'])^D;pv=ca['orders'][i]['options'][c['a_kind']]['physical_mask']^cb['orders'][j]['options'][c['b_kind']]['physical_mask']^D
   return cv,pv,c['fault_weight'],3,{'kind':'global_explicit','configuration_id':c['configuration_id']}
 raise AssertionError(('uncovered truth cell',rel['sector'],rel['a'],rel['b'],i,j))
def prior_pair_union(x):
 if len(x['checks'])!=2:return None,None
 a0,b0=x['checks'];A=x['masks'][a0];B=x['masks'][b0];rel=[u for u in installed if u['sector']==x['sector'] and set(u['checks']).issubset(x['checks'])];covered=0
 for i in bits(A):
  row=0
  for u in rel:
   if ((u['masks'].get(a0,ALL)>>i)&1):row|=u['masks'].get(b0,ALL)
  covered+=pc(row&B)
 return covered,len(rel)
for x in retained:
 t=x['term']
 if t['relation_kind']=='cross_registry_positive_pair_rectangle':
  rel=pairmap[(t['sector'],t['a'],t['b'])];A=x['masks'][t['a']];B=x['masks'][t['b']];h=hashlib.sha256();count=0;hist=collections.Counter();selhist=collections.Counter();samples=[];sigs=set()
  for i in bits(A):
   for j in bits(B):
    cv,pv,ft,wk,src=pair_selector(rel,i,j);sg=validate_support(t['sector'],cv,pv);h.update(struct.pack('>HH',i,j)+cv.to_bytes(18,'big')+pv.to_bytes(18,'big')+struct.pack('>BB',ft,wk));count+=1;hist[ft]+=1;selhist[src['kind']]+=1;sigs.add(sg)
    if len(samples)<3:samples.append({'order_ids':{str(t['a']):i,str(t['b']):j},'canonical_support':M.bits(cv),'physical_support':M.bits(pv),'fault_count':ft,'signature_hex':hex(sg),'selector':src})
  assert count==t['covered_tuple_count'];prior,nrel=prior_pair_union(x);assert prior is not None and prior<count
  tuple_ledgers.append({'term_id':x['term_id'],'sector':t['sector'],'checks':[t['a'],t['b']],'tuples_instantiated':count,'validation_mode':'literal_every_tuple','selector_stream_encoding':'>H a_order; >H b_order; 18-byte canonical; 18-byte physical; >B faults; >B selector_kind','selector_stream_sha256':h.hexdigest(),'fault_count_histogram':dict(hist),'selector_kind_histogram':dict(selhist),'signature_count':len(sigs),'signature_set_sha256':sha_obj([hex(s) for s in sorted(sigs)]),'all_canonical_physical_replays_passed':True,'prior_installed_relevant_terms':nrel,'prior_installed_union_covered_tuples':prior,'library_relative_new_tuples':count-prior,'samples':samples})
 else:
  m1,m2=[mechmap[z] for z in t['selector_mechanisms']];proof=vector_union_dp(m1,m2,t['atoms'],True);assert proof['sound'] and proof['covered_tuple_count']==t['covered_tuple_count']
  # If one selector alone proves the domain, semantic dominance should have removed it; retained multi must carry vector DP.
  assert proof['proof_mode']=='two_selector_shared_plus_mitm_exclusive_gf2'
  for c in proof['checks']:
   for o in bits(proof['masks'][c]):
    for m in (m1,m2):
     if str(c) in m['group_kinds']:assert selector_local(m,c,o)[0]==selector_local(m,c,o)[1]
  product=1
  for c in proof['checks']:product*=pc(proof['masks'][c])
  assert product==proof['covered_tuple_count'] and sum(proof['selector_choice_multiplicities'].values())==product and proof['invalid_tuple_multiplicity']==0
  proof_public={k:v for k,v in proof.items() if k not in ('masks',)};proof_public.update({'term_id':x['term_id'],'selector_mechanisms':t['selector_mechanisms'],'selector_fault_counts':t['selector_fault_counts'],'allowed_order_masks_hex':{str(c):hex(proof['masks'][c]) for c in proof['checks']},'allowed_order_counts':{str(c):pc(proof['masks'][c]) for c in proof['checks']},'canonical_physical_signature_identity_checked_for_every_allowed_local_record':True,'selector_mapping':'choose first listed selector whose terminal signature has zero detector syndrome and nonzero logical quotient','exact_product':product})
  multi_proofs.append(proof_public);tuple_ledgers.append({'term_id':x['term_id'],'sector':t['sector'],'checks':proof['checks'],'tuples_instantiated':product,'validation_mode':'factorized_two_selector_shared_plus_mitm_exclusive_gf2_universal','all_canonical_physical_replays_passed':True,'dp_proof_index':len(multi_proofs)-1})
 print(json.dumps({'stage':'retained_validation','term_id':x['term_id'],'kind':t['relation_kind'],'tuples':tuple_ledgers[-1]['tuples_instantiated']},sort_keys=True),flush=True)

# Only now finalize ledgers and atomically mutate installed state/raw registry.
retained_public=[]
for x in retained:
 z=dict(x['term']);z['term_id']=x['term_id'];z['semantic_key_sha256']=sha_obj([x['sector'],[(c,hex(x['masks'][c])) for c in x['checks']]]);z['source_batch']=a.batch_id;retained_public.append(z)
terms_after=list(state['terms'])
for z in retained_public:terms_after.append({'term_id':z['term_id'],'sector':z['sector'],'atoms':z['atoms'],'relation_kind':z['relation_kind'],'source_round':78,'source_phase':'cross_registry','source_batch':a.batch_id,'source_term_sha256':sha_obj(z),'source_pair':[z['a'],z['b']] if 'a' in z else None,'selector_mechanisms':z.get('selector_mechanisms')})
after={k:v for k,v in state.items() if k!='terms'};after.update({'schema':'round78-installed-generalized-state-v1','round78_cross_registry_terms':state.get('round78_cross_registry_terms',0)+len(retained_public),'round78_online_terms':state.get('round78_online_terms',0),'term_count':len(terms_after),'terms':terms_after})
raw_after={'schema':'round78-full-raw-mechanism-state-v1','mechanism_count':len(mechanisms),'mechanisms':mechanisms}
assert len(terms_after)==state['term_count']+len(retained_public)
# Final retained terms are exactly nondominated against the full pre-state and whole batch.
for x in retained:
 assert not any(set(u['checks']).issubset(x['checks']) and dominates(u,x) for u in installed)
 assert not any(u is not x and set(u['checks']).issubset(x['checks']) and dominates(u,x) for u in unique)

cross_sector_no_gain={'schema':'round78-cross-sector-independent-product-no-gain-v1','statement':'For rectangles A in X-local variables and B in Z-local variables, any Cartesian rectangle C_X x C_Z contained in (A x ALL_Z) union (ALL_X x B) satisfies C_X subset A or C_Z subset B. Otherwise choose x in C_X\\A and z in C_Z\\B, contradicting containment. Thus an independent-product cross-sector union yields no new nondominated rectangle; exploiting measurement-consistency correlations would require a separate exact coupled model and is not inferred here.','proof_steps':['Assume C_X is not a subset of A and choose x in C_X outside A.','Assume C_Z is not a subset of B and choose z in C_Z outside B.','Then (x,z) lies in C_X x C_Z but in neither A x ALL_Z nor ALL_X x B.','Therefore at least one subset relation holds, and the corresponding same-sector term dominates the product rectangle.'],'scope':'independent local-order Cartesian synthesis only; no claim about coupled MC-aware cross-sector unions'}
ledger={'schema':'round78-cross-registry-semantic-ledger-v1','batch_id':a.batch_id,'mechanisms':len(mechanisms),'installed_before':state['term_count'],'raw_pair_candidates':len(pair_candidates),'raw_multi_selector_candidates':len(multi_candidates),'raw_candidates':len(new),'unique_candidates':len(unique),'classifications':sorted(classes,key=lambda z:z['raw_index']),'classification_counts':dict(counts),'retained_increment':len(retained_public),'installed_after':after['term_count'],'semantic_definition':'exact finite products of 720-order masks; U dominates V iff region(V) subset region(U); full evolving installed library and whole current batch compared; installed predecessors preserved','deletion_control_scope':'named positive relation/fixed selector only, never installed-union/global minimality or absence'}
summary={'schema':'round78-cross-registry-synthesis-summary-v1','status':'PASS','batch_id':a.batch_id,'raw_mechanisms_replayed':len(mechanisms),'sectors':dict(collections.Counter(m['sector'] for m in mechanisms)),'catalogs':len(catalog_public),'local_orders_per_catalog':720,'local_order_records':len(catalog_public)*720,'unique_residual_options':len(option_public),'distinct_check_option_pair_attempts':len(completion_attempts),'positive_configurations':sum(map(len,pair_confs.values())),'cross_candidate_positive_configurations':sum(c['has_cross_candidate_construction'] for cs in pair_confs.values() for c in cs),'structural_check_pairs':sum(len(options[s])*(len(options[s])-1)//2 for s in ('Xerr','Zerr')),'positive_pair_relations':len(pair_relations),'pair_truth_cells':sum(r['truth_cell_count'] for r in pair_relations),'explicit_positive_pair_cells':sum(r['explicit_good_good_cell_count'] for r in pair_relations),'eligible_multi_selector_pairs':len(eligible),'raw_candidates':len(new),'retained_increment':len(retained_public),'literal_pair_tuples_replayed':sum(x['tuples_instantiated'] for x in tuple_ledgers if x['validation_mode']=='literal_every_tuple'),'factorized_multi_tuples_proved':sum(x['tuples_instantiated'] for x in tuple_ledgers if x['validation_mode']!='literal_every_tuple'),'generalized_before':state['term_count'],'generalized_after':after['term_count'],'registry_count_unchanged':registry['mechanism_count'],'negative_completion_misses_used_as_absence':0,'zero_cells_used_as_absence':0,'deletion_countertuples_used_as_absence':0,'claim_scope':'constructive sound cross-registry order regions only; no completeness, absence, repair, exhaustion or D-star inference'}

dump(OUT/'raw_mechanism_replay.json',{'schema':'round78-all-raw-mechanism-replay-v1','records':replays,'all_passed':True})
dump(OUT/'local_order_catalog.json',{'schema':'round78-cross-registry-local-order-catalog-v1','entries':catalog_public})
dump(OUT/'residual_option_registry.json',{'schema':'round78-cross-registry-residual-option-registry-v1','options':option_public})
dump(OUT/'positive_weight14_pool.json',{'schema':'round78-positive-weight14-pool-v1','sectors':w14_public})
dump(OUT/'completion_attempts.json',{'schema':'round78-cross-registry-completion-attempts-v1','attempts':completion_attempts,'negative_scope':'miss means only this constructive completion finder failed; never absence'})
dump(OUT/'pair_relations.json',{'schema':'round78-cross-registry-pair-relations-v1','relations':pair_relations})
dump(OUT/'multi_selector_search.json',{'schema':'round78-cross-registry-multi-selector-search-v1','eligibility':'recovery-bounded exact pilot: the two strict-subset X-sector pairs with eight-check union that completed before the v3 resource interrupt (iter48/iter67 and iter50/iter70); every other multi-selector union is explicitly unclassified and supplies no absence or minimality inference','pairs':multi_search})
dump(OUT/'raw_term_candidates.json',{'schema':'round78-cross-registry-raw-term-candidates-v1','terms':raw_terms})
dump(OUT/'retained_terms.json',{'schema':'round78-cross-registry-retained-terms-v1','terms':retained_public})
dump(OUT/'tuple_raw_replay.json',{'schema':'round78-cross-registry-retained-validation-v1','terms':tuple_ledgers,'all_passed':True})
dump(OUT/'multi_selector_dp_proofs.json',{'schema':'round78-cross-registry-multi-selector-dp-proofs-v1','proofs':multi_proofs})
dump(OUT/'cross_sector_independent_product_no_gain.json',cross_sector_no_gain)
dump(OUT/'semantic_dedup_ledger.json',ledger);dump(OUT/'summary.json',summary)
dump(OUT/'generalized_after.json',after);dump(OUT/'raw_mechanisms_after.json',raw_after)
# Atomic mutations are last, after all exhaustive retained checks and finalized ledgers exist.
atomic_dump(a.generalized_state,after);atomic_dump(a.raw_mechanisms_state,raw_after)
result={'schema':'round78-cross-registry-install-result-v1','status':'PASS','batch_id':a.batch_id,'generalized_before_count':state['term_count'],'generalized_before_semantic_sha256':state_before_sha,'generalized_after_count':after['term_count'],'generalized_after_semantic_sha256':sha_obj(after),'registry_count':registry['mechanism_count'],'registry_semantic_sha256':registry_sha,'raw_mechanisms_before_count':raw_state['mechanism_count'],'raw_mechanisms_before_semantic_sha256':raw_before_sha,'raw_mechanisms_after_count':raw_after['mechanism_count'],'raw_mechanisms_after_semantic_sha256':sha_obj(raw_after),'retained_increment':len(retained_public),'summary_semantic_sha256':sha_obj(summary),'summary_file_sha256':sha_bytes((OUT/'summary.json').read_bytes()),'strict_order':'source raw replay -> catalogs/options -> positive completion union -> raw candidates -> in-memory full-library semantic classification -> literal pair and exact multi retained validation -> finalized ledgers -> atomic generalized/raw-mechanism state mutation'}
dump(OUT/'install_result.json',result);print(json.dumps(result,sort_keys=True),flush=True)
