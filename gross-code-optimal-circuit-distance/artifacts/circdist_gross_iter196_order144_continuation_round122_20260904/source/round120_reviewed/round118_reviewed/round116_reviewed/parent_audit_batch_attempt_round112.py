#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json
import independent_iter191_direct_audit_round112 as g
L,M,G=12,6,72

def canonical_sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def file_sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
def add(i,d):
 x,y=divmod(int(i),M);return ((x+d[0])%L)*M+(y+d[1])%M
def tq(q,d):
 q=int(q);return add(q,d) if q<G else G+add(q-G,d)
def te(n,d):
 k,c,q=n.split(':');return f'{k}:{add(c,d)}:{tq(q,d)}'
def key_from_names(sector,names):
 data=[];groups={}
 for n in names:
  p=n.split(':')
  if p[0]=='D':data.append(int(p[1]))
  else: groups.setdefault(int(p[1]),[]).append(int(p[2]))
 return (sector,tuple(sorted(data)),tuple(sorted((c,tuple(sorted(v))) for c,v in groups.items())))
def trans_key(k,d):
 s,data,groups=k
 return (s,tuple(sorted(tq(q,d) for q in data)),tuple(sorted((add(c,d),kinds) for c,kinds in groups)))
def key_json(k):return [k[0],list(k[1]),[[c,list(ks)] for c,ks in k[2]]]
def key_tuple(x):return (str(x[0]),tuple(map(int,x[1])),tuple((int(c),tuple(map(int,ks))) for c,ks in x[2]))
def semantic(k):
 s,data,groups=k;names=[f'D:{q}' for q in data];gd={str(c):list(ks) for c,ks in groups}
 for c,ks in groups:names += [f'R:{c}:{x}' for x in ks]
 o={'sector':s,'selected_names':names,'data_support':list(data),'group_kinds':gd}
 return canonical_sha(o),names,gd
def replay(k,sector,duals):
 inds=list(k[1])+[144+3*c+x for c,ks in k[2] for x in ks]
 assert len(inds)==len(set(inds))<=10
 can=phy=0
 for i in inds:
  col=sector['columns'][i];can^=g.mask(col['support']);phy^=g.mask(col['physical_support'])
 cs=sector['syndrome'](can);ps=sector['syndrome'](phy)
 lp=[g.parity(can,d) for d in duals];plp=[g.parity(phy,d) for d in duals]
 assert cs==ps==0 and lp==plp and any(lp)
 assert not g.inspan(can,sector['stabilizers']) and not g.inspan(phy,sector['stabilizers'])
 return {'selected_indices':inds,'fault_count':len(inds),'canonical_support':g.bits(can),'physical_support':g.bits(phy),'syndrome':[],'logical_parities':lp,'canonical_nonstabilizer':True,'physical_nonstabilizer':True}
ap=argparse.ArgumentParser();ap.add_argument('--sector',choices=['Xerr','Zerr'],required=True);ap.add_argument('--attempt',type=int,required=True);ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--direct-root',type=Path,required=True);ap.add_argument('--cnf',type=Path,required=True);ap.add_argument('--assignment',type=Path,required=True);ap.add_argument('--prior-audit',type=Path,action='append',default=[]);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
base=a.direct_root/'direct360'/a.sector
nvars,clauses=g.parse_cnf(a.cnf);values=g.parse_assignment(a.assignment,nvars);failed=g.failed_clauses(clauses,values);assert not failed
selected=[i for i in range(360) if values[i+1]];assert len(selected)<=10
cols=json.loads(base.with_suffix('.columns.json').read_text());names=[cols['columns'][i]['name'] for i in selected]
k=key_from_names(a.sector,names);digest,norm_names,gd=semantic(k);assert norm_names==names
cand=json.loads(a.candidate.read_text());times={str(x):int(y) for x,y in cand['compressed_times'].items()};assert canonical_sha(times)==cand['compressed_schedule_sha256'];g.audit_schedule(times)
reb=g.reconstruct_sector(a.sector,times);duals=[g.mask(x['support']) for x in cols['logical_duals']];parent_replay=replay(k,reb,duals)
with gzip.open(a.source,'rt') as f:src=json.load(f)
installed={}
for s in src['selectors']:
 sk=key_from_names(s['sector'],s['selected_names']);sd,_,_=semantic(sk);assert sd==s['selector_semantic_sha256'];assert sk not in installed;installed[sk]=s['mechanism_id']
prior={}
for p in a.prior_audit:
 o=json.loads(p.read_text());assert o['accepted_collision_free']
 for row in o['orbit_rows']:
  pk=key_tuple(row['selector_key']);assert pk not in prior;prior[pk]=str(p)
orbit_rows=[];orbit_keys=set();collisions=[]
for d in ((i,j) for i in range(L) for j in range(M)):
 tt={te(n,d):v for n,v in times.items()};sa=g.audit_schedule(tt);sec=g.reconstruct_sector(a.sector,tt);tk=trans_key(k,d);td,tn,tg=semantic(tk);rr=replay(tk,sec,duals);assert len(tn)==rr['fault_count']
 assert tk not in orbit_keys;orbit_keys.add(tk)
 if tk in installed:collisions.append({'kind':'installed','delta':list(d),'mechanism_id':installed[tk],'selector_semantic_sha256':td})
 if tk in prior:collisions.append({'kind':'prior_batch','delta':list(d),'prior_audit':prior[tk],'selector_semantic_sha256':td})
 orbit_rows.append({'delta':list(d),'selector_key':key_json(tk),'selector_semantic_sha256':td,'selected_names':tn,'group_kinds':tg,'translated_schedule_sha256':canonical_sha(tt),'used_layers':sa['used_layers'],**rr})
assert len(orbit_keys)==72
out={'schema':'circdist-gross-round112-direct-selector-batch-attempt-audit-v1','status':'PASS','sector':a.sector,'attempt':a.attempt,'cnf_sha256':file_sha(a.cnf),'variables':nvars,'clauses':len(clauses),'assignment_sha256':file_sha(a.assignment),'all_variables_assigned_exactly_once':True,'all_clauses_checked':len(clauses),'all_clauses_satisfied':True,'selected_indices':selected,'selected_names':names,'parent_selector_key':key_json(k),'parent_selector_semantic_sha256':digest,'parent_replay':parent_replay,'orbit_size':len(orbit_keys),'orbit_rows':orbit_rows,'installed_selector_count':len(installed),'prior_accepted_orbit_count':len(prior)//72,'collisions':collisions,'collision_count':len(collisions),'accepted_collision_free':not collisions,'all_translated_schedules_legal':True,'all_translated_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer':True}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ['status','sector','attempt','variables','clauses','assignment_sha256','selected_names','orbit_size','collision_count','accepted_collision_free']},sort_keys=True))
