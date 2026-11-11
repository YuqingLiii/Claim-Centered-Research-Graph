#!/usr/bin/env python3
"""Build fresh iteration-193 from authorized free CSS-dual and mandatory orbits."""
from __future__ import annotations
import argparse,collections,gzip,hashlib,io,json
from pathlib import Path
L,M,G=12,6,72
DELTAS=tuple((i,j) for i in range(L) for j in range(M))

def csha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def fsha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
def write_gz(p,o):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('wb') as raw:
  with gzip.GzipFile(filename='',mode='wb',fileobj=raw,compresslevel=9,mtime=0) as enc:
   with io.TextIOWrapper(enc,encoding='utf-8',newline='\n') as txt:
    json.dump(o,txt,sort_keys=True,separators=(',',':'));txt.write('\n')
def add(x,d):
 i,j=divmod(int(x),M);return ((i+d[0])%L)*M+(j+d[1])%M
def neg(x):
 i,j=divmod(int(x),M);return ((-i)%L)*M+((-j)%M)
def tq(q,d):
 q=int(q);return add(q,d) if q<G else G+add(q-G,d)
def dq(q):
 q=int(q);return G+neg(q) if q<G else neg(q-G)
def te(n,d):
 k,c,q=n.split(':');return f'{k}:{add(c,d)}:{tq(q,d)}'
def de(n):
 k,c,q=n.split(':');assert k in ('X','Z');return f'{"Z" if k=="X" else "X"}:{neg(c)}:{dq(q)}'
def bkey(b):return tuple(sorted((str(x),str(y)) for x,y in b['atoms']))
def tb(k,d):return tuple(sorted((te(x,d),te(y,d)) for x,y in k))
def db(k):return tuple(sorted((de(x),de(y)) for x,y in k))
def skey(s):return (str(s['sector']),tuple(sorted(map(int,s['data_support']))),tuple(sorted((int(c),tuple(sorted(map(int,ks)))) for c,ks in s['group_kinds'].items())))
def ts(k,d):
 s,data,groups=k;return (s,tuple(sorted(tq(q,d) for q in data)),tuple(sorted((add(c,d),ks) for c,ks in groups)))
def ds(k):
 s,data,groups=k;return ('Zerr' if s=='Xerr' else 'Xerr',tuple(sorted(dq(q) for q in data)),tuple(sorted((neg(c),ks) for c,ks in groups)))
def kjson(k):return [k[0],list(k[1]),[[c,list(ks)] for c,ks in k[2]]]
def bjson(k):return [[x,y] for x,y in k]
def sem(k):
 s,data,groups=k;names=[f'D:{q}' for q in data];gd={str(c):list(ks) for c,ks in groups}
 for c,ks in groups:names += [f'R:{c}:{x}' for x in ks]
 o={'sector':s,'selected_names':names,'data_support':list(data),'group_kinds':gd}
 return o,csha(o)
def kt(x):return (str(x[0]),tuple(map(int,x[1])),tuple((int(c),tuple(map(int,ks))) for c,ks in x[2]))
def partition(keys,action):
 keyset=set(keys);rem=set(keyset);out=[]
 while rem:
  seed=next(iter(rem));orb={action(seed,d) for d in DELTAS};assert orb<=keyset
  rep=min(orb);out.append((rep,orb));rem-=orb
 return sorted(out,key=lambda x:x[0])
def delta_map(rep,action):
 out={}
 for d in DELTAS:
  key=action(rep,d);assert key not in out;out[key]=d
 return out

ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--state',type=Path,required=True)
ap.add_argument('--global-plan',type=Path,required=True);ap.add_argument('--fallback-plan',type=Path,required=True);ap.add_argument('--css-audit',type=Path,required=True)
ap.add_argument('--x-audit',type=Path,required=True);ap.add_argument('--z-audit',type=Path,required=True);ap.add_argument('--dual-audit',type=Path,required=True)
ap.add_argument('--output-source',type=Path,required=True);ap.add_argument('--output-state',type=Path,required=True);ap.add_argument('--output-audit',type=Path,required=True);a=ap.parse_args()
with gzip.open(a.source,'rt') as f:src=json.load(f)
state=json.loads(a.state.read_text());css=json.loads(a.css_audit.read_text());dual=json.loads(a.dual_audit.read_text())
xa=json.loads(a.x_audit.read_text());za=json.loads(a.z_audit.read_text())
assert css['status']==dual['status']==xa['status']==za['status']=='PASS'
assert css['bindings']['source_sha256']==fsha(a.source)==state['source_file_sha256']
assert dual['bindings']['source_sha256']==fsha(a.source)
assert dual['all_four_orbits_free_under_Z12xZ6'] and dual['all_four_orbits_pairwise_disjoint']
assert dual['all_four_orbits_collision_free_against_future_base']
# Existing exact semantic registries.
old_blocks=list(src['blocks']);old_bkeys=[bkey(b) for b in old_blocks];old_bset=set(old_bkeys);assert len(old_bkeys)==len(old_bset)==517140
old_selectors=list(src['selectors']);old_skeys=[skey(s) for s in old_selectors];old_sset=set(old_skeys);assert len(old_skeys)==len(old_sset)==25164
bparent={k:(i,b) for i,(k,b) in enumerate(zip(old_bkeys,old_blocks))}
sparent={k:(i,s) for i,(k,s) in enumerate(zip(old_skeys,old_selectors))}
# Exact missing D images split into translation orbits.  Authorization retains only
# size-72 (free) orbits; every nonfree orbit remains explicitly enumerated below.
bmissing={db(k) for k in old_bset}-old_bset
bparts=partition(bmissing,tb);bfree=[x for x in bparts if len(x[1])==72];bskip=[x for x in bparts if len(x[1])!=72]
assert len(bfree)==4124 and len(bskip)==9 and sum(len(o) for _,o in bfree)==296928 and sum(len(o) for _,o in bskip)==324
smissing={ds(k) for k in old_sset}-old_sset
sparts=partition(smissing,ts);sfree=[x for x in sparts if len(x[1])==72];sskip=[x for x in sparts if len(x[1])!=72]
assert len(sfree)==349 and len(sskip)==1 and sum(len(o) for _,o in sfree)==25128 and sum(len(o) for _,o in sskip)==36
# Preserve inherited bytes semantically/order-wise, then append complete free orbits.
blocks=list(old_blocks);family_next=collections.Counter(b['family'] for b in blocks);new_block_family=collections.Counter()
for oi,(rep,orb) in enumerate(bfree):
 dm=delta_map(rep,tb);families={bparent[db(k)][1]['family'] for k in orb};assert len(families)==1
 for d in DELTAS:
  key=tb(rep,d);pi,parent=bparent[db(key)];family=parent['family'];assert family in families
  blocks.append({'atoms':bjson(key),'family':family,'family_index':family_next[family],
    'source_id':f'r114-cssdual-o{oi}-d{d[0]}_{d[1]}','source_iteration':192,
    'round114_translation_orbit_id':f'r114-cssdual-block-o{oi}',
    'round114_translation_orbit_representative_sha256':csha(bjson(rep)),
    'round114_translation_delta_from_representative':list(d),
    'css_duality_parent_index':pi,'css_duality_parent_source_id':parent['source_id'],
    'css_duality_parent_semantic_sha256':csha(bjson(db(key))),
    'css_duality_action':'X:c:q <-> Z:-c:D(q)',
    'soundness_provenance':'CSS-duality transport of inherited reviewed sound order exclusion; exact free Z12xZ6 orbit installed atomically'})
  family_next[family]+=1;new_block_family[family]+=1
assert len(blocks)==814068
selectors=list(old_selectors);new_selector_sector=collections.Counter()
for oi,(rep,orb) in enumerate(sfree):
 dm=delta_map(rep,ts)
 for d in DELTAS:
  key=ts(rep,d);pi,parent=sparent[ds(key)];semantic,digest=sem(key)
  selectors.append({'mechanism_id':f'r114-cssdual-o{oi}-d{d[0]}_{d[1]}','source_iteration':192,
    'sector':key[0],'fault_count':len(semantic['selected_names']),'selected_names':semantic['selected_names'],
    'data_support':semantic['data_support'],'group_kinds':semantic['group_kinds'],'selector_semantic_sha256':digest,
    'origin':'round114_css_duality_free_orbit_transport',
    'round114_translation_orbit_id':f'r114-cssdual-selector-o{oi}',
    'round114_translation_orbit_representative_semantic_sha256':sem(rep)[1],
    'round114_translation_delta_from_representative':list(d),
    'css_duality_parent_index':pi,'css_duality_parent_mechanism_id':parent['mechanism_id'],
    'css_duality_parent_selector_semantic_sha256':parent['selector_semantic_sha256'],
    'css_duality_action':'Xerr <-> Zerr, q -> D(q), check -> -check, residual kind fixed',
    'soundness_provenance':'CSS-duality transport of inherited reviewed exact selector; exact free Z12xZ6 orbit installed atomically'})
  assert len(semantic['selected_names'])==len(set(semantic['selected_names']))<=10
  new_selector_sector[key[0]]+=1
# Append mandatory original X/Z and CSS-dual X/Z orbits (four disjoint free orbits).
mandatory=[]
for tag,o in (('mandatory-Xerr',xa),('mandatory-Zerr',za)):
 rows=o['orbit_rows'];parent=kt(o['parent_selector_key'])
 mandatory.append((tag,rows,parent,o['parent_selector_semantic_sha256'],fsha(a.x_audit if o['sector']=='Xerr' else a.z_audit),'translated_schedule_sha256'))
for result in dual['results']:
 tag='mandatory-cssdual-'+result['source_sector']+'-to-'+result['target_sector']
 mandatory.append((tag,result['orbit_rows'],kt(result['dual_parent_selector_key']),result['dual_parent_semantic_sha256'],fsha(a.dual_audit),'translated_dual_schedule_sha256'))
pre_mandatory=set(map(skey,selectors));mandatory_sets=[]
for oi,(tag,rows,parent,parent_digest,audit_sha,schedule_field) in enumerate(mandatory):
 assert len(rows)==72;orbit=set()
 for row in rows:
  d=tuple(map(int,row['delta']));key=kt(row['selector_key']);assert key==ts(parent,d);assert key not in orbit;orbit.add(key)
  semantic,digest=sem(key);assert digest==row['selector_semantic_sha256'];assert key not in pre_mandatory
  selectors.append({'mechanism_id':f'r114-{tag}-d{d[0]}_{d[1]}','source_iteration':192,'sector':key[0],
    'fault_count':len(semantic['selected_names']),'selected_names':semantic['selected_names'],'data_support':semantic['data_support'],
    'group_kinds':semantic['group_kinds'],'selector_semantic_sha256':digest,'origin':'round114_mandatory_adjudicated_free_orbit',
    'round114_translation_orbit_id':f'r114-{tag}','round114_translation_orbit_representative_semantic_sha256':parent_digest,
    'round114_translation_delta_from_parent':list(d),'round114_orbit_audit_sha256':audit_sha,
    'source_schedule_sha256':row[schedule_field],
    'soundness_provenance':'complete direct SAT assignment, canonical and frozen physical replay, and exact collision-free free Z12xZ6 orbit audit'})
  new_selector_sector[key[0]]+=1
 assert len(orbit)==72;mandatory_sets.append(orbit);pre_mandatory|=orbit
for i,o in enumerate(mandatory_sets):
 for j in range(i):assert not(o&mandatory_sets[j])
assert len(selectors)==50580 and len({skey(s) for s in selectors})==50580
# Exact translation closure after all additions.
final_bset={bkey(b) for b in blocks};final_sset={skey(s) for s in selectors}
for gen in ((1,0),(0,1)):
 assert all(tb(k,gen) in final_bset for k in final_bset)
 assert all(ts(k,gen) in final_sset for k in final_sset)
# Build the fresh source and exact expected expression counts.
src.pop('semantic_payload_sha256');src['schema']='circdist-gross-iteration193-full-translation-closure-finite-source-v1'
src['blocks']=blocks;src['selectors']=selectors
bindings=src['bindings'];bindings.update({
 'round114_dispatch_scheduler_sha256':'9750f170f0c23f96317b08ff158671310364c8439b6bcd7f44e7c3b455dfef6a',
 'round114_proofpilot_sha256':'aa5475949d9abe25c2168d8dcd47cc5e88c453ec12d1cc9fed6cae556f3925c2',
 'round114_css_duality_global_plan_sha256':fsha(a.global_plan),'round114_fallback_plan_sha256':fsha(a.fallback_plan),
 'round114_css_duality_audit_sha256':fsha(a.css_audit),'round114_mandatory_x_orbit_audit_sha256':fsha(a.x_audit),
 'round114_mandatory_z_orbit_audit_sha256':fsha(a.z_audit),'round114_mandatory_css_dual_audit_sha256':fsha(a.dual_audit),
 'round114_retained_css_duality_free_block_orbits':len(bfree),'round114_retained_css_duality_free_selector_orbits':len(sfree),
 'round114_skipped_nonfree_block_orbits':len(bskip),'round114_skipped_nonfree_selector_orbits':len(sskip),
 'round114_mandatory_free_selector_orbits':4,'round114_quotient_group':'Z_12 x Z_6','round114_quotient_group_order':72})
expected=src['expected'];expected['reviewed_blocks']=len(blocks);expected['selectors']=len(selectors)
expected['block_family_counts']=dict(sorted(collections.Counter(b['family'] for b in blocks).items()))
residual=[set(map(int,x)) for x in src['residual_positions']]
def pos(ks):
 o=set()
 for k in ks:o.symmetric_difference_update(residual[int(k)])
 return tuple(sorted(o))
members=set();ranks=set()
for s in selectors:
 definition=src['sector_definitions'][s['sector']]
 for cs,ks in s['group_kinds'].items():
  c=int(cs);p=pos(ks)
  for q in definition['checks'][c]:
   members.add((s['sector'],c,p,q))
   if p and p!=tuple(range(6)):ranks.add((s['sector'],c,q))
expected['membership_expressions']=len(members);expected['rank_expressions']=len(ranks)
expected['assertions']=4398+len(blocks)+len(selectors)
src['semantic_payload_sha256']=csha(src);write_gz(a.output_source,src)
state_fields=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
selector_state=csha([{k:s.get(k) for k in state_fields} for s in selectors])
outstate={'schema':'circdist-gross-round114-css-duality-continuation-frontier-state-v1','status':'PASS','next_iteration':193,
 'started':False,'stop':None,'block_count':len(blocks),'selector_count':len(selectors),'selector_state_sha256':selector_state,
 'source_semantic_payload_sha256':src['semantic_payload_sha256'],'source_file_sha256':fsha(a.output_source),
 'translation_group':'Z_12 x Z_6','translation_group_order':72,
 'scope':'fresh checked unstarted frontier after authorized free CSS-duality and four mandatory witness orbits; no iteration-193 solver disposition'}
a.output_state.parent.mkdir(parents=True,exist_ok=True);a.output_state.write_text(json.dumps(outstate,indent=2,sort_keys=True)+'\n')
def skipped_rows(parts,kind):
 rows=[]
 for rep,orb in parts:
  payload=kjson(rep) if kind=='selector' else bjson(rep)
  rows.append({'representative':payload,'representative_sha256':csha(payload),'orbit_size':len(orb),
               'full_orbit_semantic_sha256':csha(sorted(kjson(k) if kind=='selector' else bjson(k) for k in orb))})
 return rows
outaudit={'schema':'circdist-gross-round114-css-duality-frontier-advance-audit-v1','status':'PASS',
 'bindings':{'input_source_sha256':fsha(a.source),'input_state_sha256':fsha(a.state),'global_plan_sha256':fsha(a.global_plan),
  'fallback_plan_sha256':fsha(a.fallback_plan),'css_audit_sha256':fsha(a.css_audit),'x_audit_sha256':fsha(a.x_audit),
  'z_audit_sha256':fsha(a.z_audit),'mandatory_css_dual_audit_sha256':fsha(a.dual_audit)},
 'input':{'blocks':len(old_blocks),'selectors':len(old_selectors)},
 'retained_global_mechanism':{'free_css_dual_block_orbits':len(bfree),'free_css_dual_blocks':sum(len(o) for _,o in bfree),
  'free_css_dual_selector_orbits':len(sfree),'free_css_dual_selectors':sum(len(o) for _,o in sfree),
  'new_blocks_by_family':dict(sorted(new_block_family.items())),'new_selectors_by_sector':dict(sorted(new_selector_sector.items()))},
 'mandatory':{'free_orbits':4,'selectors':288,'original_sector_orbits':2,'css_dual_sector_orbits':2,
  'pairwise_collision_free':True,'physical_replay_all_144_dual_rows':True},
 'authorization_boundary':{'rule':'retain only new semantic mechanisms with free 72-element Z12xZ6 orbit',
  'skipped_nonfree_block_orbits':skipped_rows(bskip,'block'),'skipped_nonfree_selector_orbits':skipped_rows(sskip,'selector'),
  'extended_order144_quotient_built':False,
  'reason':'skipped nonfree D-images leave the registry outside exact D-invariance; ordinary translation quotient remains exact'},
 'output':{'blocks':len(blocks),'selectors':len(selectors),'assertions':expected['assertions'],
  'block_family_counts':expected['block_family_counts'],'membership_expressions':len(members),'rank_expressions':len(ranks),
  'source_sha256':fsha(a.output_source),'source_semantic_payload_sha256':src['semantic_payload_sha256'],
  'state_sha256':fsha(a.output_state),'selector_state_sha256':selector_state},
 'translation_invariance':{'generators':[[1,0],[0,1]],'block_generator_cases':2*len(blocks),'selector_generator_cases':2*len(selectors),
  'conclusion':'closure under generators gives closure under all 72 translations'},
 'fallback_disposition':{'activated':False,'reason':'predeclared CSS-duality transport produced a sound checkable stronger global mechanism'},
 'fresh_frontier':{'iteration':193,'started':False,'solver_invocations':0}}
a.output_audit.write_text(json.dumps(outaudit,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','blocks':len(blocks),'selectors':len(selectors),'assertions':expected['assertions'],
 'source_sha256':outaudit['output']['source_sha256'],'semantic_sha256':src['semantic_payload_sha256'],
 'state_sha256':outaudit['output']['state_sha256'],'selector_state_sha256':selector_state},sort_keys=True))
