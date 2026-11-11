#!/usr/bin/env python3
"""Audit CSS-dual translation orbits of the two mandatory iteration-192 witnesses."""
from __future__ import annotations
import argparse,gzip,hashlib,json
from pathlib import Path
import independent_iter192_direct_audit_round114 as g
L,M,G=12,6,72
DELTAS=tuple((i,j) for i in range(L) for j in range(M))

def csha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def fsha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
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
 k,c,q=n.split(':');return f'{"Z" if k=="X" else "X"}:{neg(c)}:{dq(q)}'
def dmask(v):
 out=0
 for q in g.bits(v):out|=1<<dq(q)
 return out
def key_tuple(x):return (str(x[0]),tuple(map(int,x[1])),tuple((int(c),tuple(map(int,ks))) for c,ks in x[2]))
def skey(s):
 return (str(s['sector']),tuple(sorted(map(int,s['data_support']))),tuple(sorted((int(c),tuple(sorted(map(int,ks)))) for c,ks in s['group_kinds'].items())))
def tkey(k,d):
 s,data,groups=k;return (s,tuple(sorted(tq(q,d) for q in data)),tuple(sorted((add(c,d),ks) for c,ks in groups)))
def dkey(k):
 s,data,groups=k;return ('Zerr' if s=='Xerr' else 'Xerr',tuple(sorted(dq(q) for q in data)),tuple(sorted((neg(c),ks) for c,ks in groups)))
def key_json(k):return [k[0],list(k[1]),[[c,list(ks)] for c,ks in k[2]]]
def semantic(k):
 s,data,groups=k;names=[f'D:{q}' for q in data];gd={str(c):list(ks) for c,ks in groups}
 for c,ks in groups:names += [f'R:{c}:{x}' for x in ks]
 o={'sector':s,'selected_names':names,'data_support':list(data),'group_kinds':gd}
 return csha(o),names,gd
def replay(k,times,duals):
 sector=g.reconstruct_sector(k[0],times)
 inds=list(k[1])+[144+3*c+x for c,ks in k[2] for x in ks]
 assert len(inds)==len(set(inds))<=10
 can=phy=0
 for i in inds:
  col=sector['columns'][i];can^=g.mask(col['support']);phy^=g.mask(col['physical_support'])
 cs=sector['syndrome'](can);ps=sector['syndrome'](phy)
 lp=[g.parity(can,x) for x in duals];plp=[g.parity(phy,x) for x in duals]
 assert cs==ps==0 and lp==plp and any(lp)
 assert not g.inspan(can,sector['stabilizers']) and not g.inspan(phy,sector['stabilizers'])
 return {'selected_indices':inds,'fault_count':len(inds),'canonical_support':g.bits(can),
         'physical_support':g.bits(phy),'syndrome':[],'logical_parities':lp,
         'canonical_nonstabilizer':True,'physical_nonstabilizer':True}

ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
ap.add_argument('--direct-root',type=Path,required=True);ap.add_argument('--x-audit',type=Path,required=True);ap.add_argument('--z-audit',type=Path,required=True)
ap.add_argument('--css-audit',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
with gzip.open(a.source,'rt') as f:src=json.load(f)
cand=json.loads(a.candidate.read_text());times={str(n):int(t) for n,t in cand['compressed_times'].items()};g.audit_schedule(times)
css=json.loads(a.css_audit.read_text());assert css['status']=='PASS' and css['bindings']['source_sha256']==fsha(a.source)
installed={skey(s) for s in src['selectors']};assert len(installed)==len(src['selectors'])
# Authorized global additions retain only missing free translation orbits.
dual_missing={dkey(k) for k in installed}-installed
free_dual_existing={k for k in dual_missing if len({tkey(k,d) for d in DELTAS})==72}
nonfree_dual_existing=dual_missing-free_dual_existing
assert len(free_dual_existing)==25128 and len(nonfree_dual_existing)==36
future_base=installed|free_dual_existing
loaded=[]
for path,sector in ((a.x_audit,'Xerr'),(a.z_audit,'Zerr')):
 o=json.loads(path.read_text());assert o['status']=='PASS' and o['sector']==sector and o['accepted_collision_free'] and o['orbit_size']==72
 orbit={key_tuple(row['selector_key']) for row in o['orbit_rows']};assert len(orbit)==72 and not (orbit & installed)
 parent=key_tuple(o['parent_selector_key']);assert parent in orbit
 loaded.append((o,parent,orbit))
# The two original mandatory orbits and their D-images must be pairwise disjoint,
# collision-free against the post-global registry, and individually free.
labels=[];sets=[]
for o,parent,orbit in loaded:
 labels.append(o['sector']+'_mandatory');sets.append(orbit)
 labels.append(('Zerr' if o['sector']=='Xerr' else 'Xerr')+'_dual_of_'+o['sector']);sets.append({dkey(k) for k in orbit})
for label,orbit in zip(labels,sets):
 assert len(orbit)==72 and not (orbit&future_base)
 for key in orbit:assert len({tkey(key,d) for d in DELTAS})==72
for i in range(len(sets)):
 for j in range(i):assert not (sets[i]&sets[j])
# Replay each dual parent under all 72 translated dual schedules.
dual_times={de(n):t for n,t in times.items()};g.audit_schedule(dual_times)
results=[]
for o,parent,original_orbit in loaded:
 dual_parent=dkey(parent);target=dual_parent[0]
 cols=json.loads((a.direct_root/'direct360'/target).with_suffix('.columns.json').read_text())
 logical=[g.mask(row['support']) for row in cols['logical_duals']]
 rows=[];orbit=set()
 original_parent_replay=o['parent_replay']
 parent_result=None
 for d in DELTAS:
  schedule={te(n,d):t for n,t in dual_times.items()};audit=g.audit_schedule(schedule)
  key=tkey(dual_parent,d);assert key not in orbit;orbit.add(key)
  digest,names,groups=semantic(key);rr=replay(key,schedule,logical)
  row={'delta':list(d),'selector_key':key_json(key),'selector_semantic_sha256':digest,
       'selected_names':names,'group_kinds':groups,'translated_dual_schedule_sha256':csha(schedule),
       'used_layers':audit['used_layers'],**rr}
  rows.append(row)
  if d==(0,0):parent_result=rr
 assert len(orbit)==72 and orbit=={dkey(k) for k in original_orbit}
 # D maps canonical and physical support exactly for the unshifted parent.
 assert parent_result['canonical_support']==g.bits(dmask(g.mask(original_parent_replay['canonical_support'])))
 assert parent_result['physical_support']==g.bits(dmask(g.mask(original_parent_replay['physical_support'])))
 results.append({'source_sector':o['sector'],'target_sector':target,'source_parent_selector_key':key_json(parent),
                 'source_parent_semantic_sha256':o['parent_selector_semantic_sha256'],
                 'dual_parent_selector_key':key_json(dual_parent),'dual_parent_semantic_sha256':semantic(dual_parent)[0],
                 'source_audit_sha256':fsha(a.x_audit if o['sector']=='Xerr' else a.z_audit),
                 'orbit_size':72,'collision_count':0,'accepted_collision_free':True,
                 'parent_support_is_exact_D_image':True,'orbit_rows':rows})
out={'schema':'circdist-gross-round114-mandatory-css-dual-orbit-audit-v1','status':'PASS',
     'bindings':{'source_sha256':fsha(a.source),'candidate_sha256':fsha(a.candidate),'candidate_schedule_sha256':cand['compressed_schedule_sha256'],
                 'css_audit_sha256':fsha(a.css_audit),'x_audit_sha256':fsha(a.x_audit),'z_audit_sha256':fsha(a.z_audit)},
     'installed_selectors':len(installed),'authorized_free_css_images':len(free_dual_existing),
     'skipped_nonfree_css_images':len(nonfree_dual_existing),'future_base_selectors':len(future_base),
     'mandatory_orbit_count':4,'mandatory_selector_count':sum(map(len,sets)),
     'all_four_orbits_pairwise_disjoint':True,'all_four_orbits_collision_free_against_future_base':True,
     'all_four_orbits_free_under_Z12xZ6':True,'all_dual_schedules_legal':True,
     'all_dual_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer':True,
     'results':results}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','mandatory_orbits':4,'mandatory_selectors':288,'free_css_images':len(free_dual_existing),
                  'skipped_nonfree_css_images':len(nonfree_dual_existing)},sort_keys=True))
