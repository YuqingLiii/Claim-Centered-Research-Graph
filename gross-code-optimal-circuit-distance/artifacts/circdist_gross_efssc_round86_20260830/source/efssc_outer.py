#!/usr/bin/env python3
"""Exact fixed-selector semantic cuts over the reviewed iteration-102 frontier.

For each reviewed raw direct-360 witness, this compiler symbolically recomputes the
complete 84-bit detector/logical signature for every possible within-check order.
It blocks the full validity domain of that fixed selector, not merely an atom cube.
"""
from pathlib import Path
import argparse, gzip, hashlib, json, sys, time

ap=argparse.ArgumentParser()
ap.add_argument('--package',type=Path,required=True)
ap.add_argument('--output',type=Path,required=True)
ap.add_argument('--timeout-ms',type=int,default=600000)
ap.add_argument('--cut-limit',type=int,default=0,help='0 means all')
a=ap.parse_args(); P=a.package.resolve(); a.output.mkdir(parents=True,exist_ok=True)
sys.path[:0]=[str(P/'src/round63_src'),str(P/'src')]
import z3
import model as M, round68_build as B
from outer import OuterScheduler

def load(rel):
 p=P/rel
 if not p.exists(): p=Path(str(p)+'.gz')
 b=p.read_bytes()
 return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha(o): return hashlib.sha256(canon(o)).hexdigest()
def dump(name,o): (a.output/name).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def parity(args,const=False):
 args=list(args)
 if not args: return z3.BoolVal(bool(const))
 v=args[0]
 for x in args[1:]: v=z3.Xor(v,x)
 return z3.Not(v) if const else v

t0=time.monotonic()
# Bind exact reviewed restart.
dyn=load('restart/dynamic_blocks_iteration102.json')
gen=load('restart/installed_generalized_terms_iteration102.json')
reg=load('restart/online_mechanism_registry_iteration102.json')
raw=load('restart/full_raw_mechanisms_iteration102.json')
expected={'dynamic':'62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2','generalized':'4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3','registry':'b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604','raw':'fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600'}
actual={'dynamic':sha(dyn),'generalized':sha(gen),'registry':sha(reg),'raw':sha(raw)}
assert actual==expected,(actual,expected)
assert len(dyn)==204 and gen['term_count']==len(gen['terms'])==12820
assert reg['mechanism_count']==raw['mechanism_count']==120
assert {m['mechanism_id'] for m in reg['mechanisms']}=={m['mechanism_id'] for m in raw['mechanisms']}
assert not (P/'cegar/iter102').exists()

px,pz,lx,lz=B.load_context()
rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X'); rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z')
r62=load('src/round62_cegar20.json'); B.replay_round62_blocks(r62,lx,lz)
outer=OuterScheduler(True)
for i,r in enumerate(rx+rz): outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
for b in r62['outer_blocks']: outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
for t in gen['terms']: outer.add_block([tuple(x) for x in t['atoms']],t['term_id'],t.get('source_term_sha256'))
for i,b in enumerate(dyn): outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{i}-{b['sector']}",b.get('mechanism_sha256'))
assert len(outer.blocks)==14484

# Per-qubit 84-bit signature coefficients for each CSS sector.
sector_data={
 'Xerr':{'checks':M.Xchecks,'edge_kind':'X','det':M.HZ,'duals':lz},
 'Zerr':{'checks':M.Zchecks,'edge_kind':'Z','det':M.HX,'duals':lx},
}
def sig(v,det,duals):
 return sum(((M.popcount(v&h)&1)<<i) for i,h in enumerate(det)) | sum(((M.popcount(v&h)&1)<<(72+i)) for i,h in enumerate(duals))
for lab,d in sector_data.items(): d['q_sig']=[sig(1<<q,d['det'],d['duals']) for q in range(144)]

# Cache rank predicates because many selectors reuse a local check/kind subset.
rank_cache={}; membership_cache={}
def rank_expr(lab,c,q):
 key=(lab,c,q)
 if key not in rank_cache:
  d=sector_data[lab]; kind=d['edge_kind']; row=d['checks'][c]
  tq=outer.t[M.edge_key(kind,c,q)]
  rank_cache[key]=z3.Sum([z3.If(outer.t[M.edge_key(kind,c,r)]<tq,1,0) for r in row if r!=q])
 return rank_cache[key]
def selected_positions(kinds):
 # XOR of distinct direct residual columns, using canonical RES_POS.
 parity_set=set()
 for k in kinds:
  for p in M.RES_POS[int(k)]:
   if p in parity_set: parity_set.remove(p)
   else: parity_set.add(p)
 return tuple(sorted(parity_set))
def member_expr(lab,c,kinds,q):
 poss=selected_positions(kinds); key=(lab,c,poss,q)
 if key not in membership_cache:
  r=rank_expr(lab,c,q)
  membership_cache[key]=z3.Or([r==p for p in poss]) if poss else z3.BoolVal(False)
 return membership_cache[key]

def selector_signature_bits(mech):
 lab=mech['sector']; d=sector_data[lab]
 data_mask=M.mask(mech['data_support']); data_sig=sig(data_mask,d['det'],d['duals'])
 terms=[[] for _ in range(84)]
 local_public=[]
 for cs,ks0 in sorted(mech['group_kinds'].items(),key=lambda kv:int(kv[0])):
  c=int(cs); ks=tuple(sorted(map(int,ks0))); poss=selected_positions(ks)
  row=d['checks'][c]
  for q in row:
   m=member_expr(lab,c,ks,q); qs=d['q_sig'][q]
   for b in range(84):
    if (qs>>b)&1: terms[b].append(m)
  local_public.append({'check':c,'kinds':list(ks),'canonical_position_parity':list(poss),'row':row})
 bits=[parity(terms[b],bool((data_sig>>b)&1)) for b in range(84)]
 return bits,data_sig,local_public

cut_records=[]
source_fail=[]
mechs=sorted(raw['mechanisms'],key=lambda m:(m['iteration'],m['sector']))
if a.cut_limit: mechs=mechs[:a.cut_limit]
for mi,m in enumerate(mechs):
 assert m['fault_count']==len(m['data_support'])+sum(len(v) for v in m['group_kinds'].values())<=10
 bits,data_sig,local=selector_signature_bits(m)
 valid=z3.And(*[z3.Not(x) for x in bits[:72]],z3.Or(*bits[72:]))
 # Source schedule must be in the full symbolic validity domain.
 subst=[]
 for e,v in outer.t.items(): subst.append((v,z3.IntVal(int(m['times'][e]))))
 sv=z3.simplify(z3.substitute(valid,*subst))
 if not z3.is_true(sv): source_fail.append((m['mechanism_id'],str(sv)))
 outer.s.add(z3.Not(valid))
 cut_records.append({'cut_index':mi,'mechanism_id':m['mechanism_id'],'iteration':m['iteration'],'sector':m['sector'],'fault_count':m['fault_count'],'data_support':m['data_support'],'groups':local,'data_signature_hex':hex(data_sig),'source_validity_evaluation':str(sv),'fixed_selector_full_domain_cut':True})
assert not source_fail,source_fail
compile_seconds=time.monotonic()-t0

# Serialize before solving; this is a deterministic proof input only for exact Z3 version.
smt=outer.s.to_smt2(); (a.output/'outer_with_efssc.smt2').write_text(smt)
formula_sha=hashlib.sha256(smt.encode()).hexdigest()
outer.s.set(timeout=a.timeout_ms)
ts=time.monotonic(); ans=outer.s.check(); solve_seconds=time.monotonic()-ts
status=str(ans).upper(); reason=outer.s.reason_unknown() if ans==z3.unknown else None
result={'schema':'round86-efssc-outer-result-v1','status':status,'reason_unknown':reason,'timeout_ms':a.timeout_ms,'solve_seconds':solve_seconds,'compile_seconds':compile_seconds,'total_seconds':time.monotonic()-t0,'existing_blocks':14484,'efssc_cuts':len(cut_records),'assertions':len(outer.s.assertions()),'edge_variables':864,'rank_expressions':len(rank_cache),'membership_expressions':len(membership_cache),'formula_sha256':formula_sha,'restart_semantic_sha256':actual,'source_validity_failures':source_fail,'new_mechanism':'complete symbolic fixed-selector validity domains over exact direct-360 residual semantics'}
if ans==z3.sat:
 model=outer.s.model(); rawtimes={e:model.eval(v,model_completion=True).as_long() for e,v in outer.t.items()}; times=M.compress_schedule(rawtimes); audit=M.audit_schedule(times,True)
 result['candidate_schedule']=times; result['candidate_schedule_sha256']=sha(times); result['candidate_audit']=audit
 # Independently evaluate all 120 selectors concretely on the survivor.
 ss=B.sectors(times,lx,lz); survivors=[]
 for m in mechs:
  ev=M.verify_named_selection(ss[m['sector']],m['selected_names'],10)
  if ev['ok']: survivors.append(m['mechanism_id'])
 result['concrete_fixed_selector_survivors']=survivors
 assert audit['ok'] and audit['global_interleaved'] and not survivors
 dump('candidate.json',{'schema':'round86-efssc-survivor-v1','schedule_times':times,'schedule_sha256':sha(times),'audit':audit,'existing_blocks_avoided':14484,'efssc_cuts_avoided':len(cut_records)})
dump('cut_catalog.json',{'schema':'round86-efssc-cut-catalog-v1','mechanism_count':len(cut_records),'cuts':cut_records})
dump('result.json',result)
print(json.dumps({k:result[k] for k in ('status','reason_unknown','solve_seconds','compile_seconds','existing_blocks','efssc_cuts','assertions','rank_expressions','membership_expressions','formula_sha256')},sort_keys=True),flush=True)
