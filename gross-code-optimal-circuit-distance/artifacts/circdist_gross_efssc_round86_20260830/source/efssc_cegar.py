#!/usr/bin/env python3
"""Strict-serial exact semantic-cut CEGAR from reviewed Gross iteration 102."""
from pathlib import Path
import argparse,gzip,hashlib,json,os,sys,time
ap=argparse.ArgumentParser()
ap.add_argument('--package',type=Path,required=True);ap.add_argument('--seed-candidate',type=Path,required=True);ap.add_argument('--seed-domains',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
ap.add_argument('--start-iteration',type=int,default=103);ap.add_argument('--max-candidates',type=int,default=6);ap.add_argument('--outer-timeout-ms',type=int,default=600000)
a=ap.parse_args();P=a.package.resolve();O=a.output.resolve();O.mkdir(parents=True,exist_ok=False);sys.path[:0]=[str(P/'src/round63_src'),str(P/'src')]
import z3
import model as M,round68_build as B,round68_verify as V
from outer import OuterScheduler

def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha(o):return hashlib.sha256(canon(o)).hexdigest()
def load_path(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def load_rel(rel):
 p=P/rel
 if not p.exists():p=Path(str(p)+'.gz')
 return load_path(p)
def dump(p,o):p=O/p;p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+'.tmp');tmp.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');os.replace(tmp,p)
def parity(args,const=False):
 args=list(args)
 if not args:return z3.BoolVal(bool(const))
 v=args[0]
 for x in args[1:]:v=z3.Xor(v,x)
 return z3.Not(v) if const else v

t0=time.monotonic();dyn=load_rel('restart/dynamic_blocks_iteration102.json');gen=load_rel('restart/installed_generalized_terms_iteration102.json');reg=load_rel('restart/online_mechanism_registry_iteration102.json');raw=load_rel('restart/full_raw_mechanisms_iteration102.json')
expected={'dynamic':'62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2','generalized':'4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3','registry':'b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604','raw':'fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600'}
actual={'dynamic':sha(dyn),'generalized':sha(gen),'registry':sha(reg),'raw':sha(raw)};assert actual==expected
assert len(dyn)==204 and gen['term_count']==12820 and reg['mechanism_count']==raw['mechanism_count']==120 and not (P/'cegar/iter102').exists()
px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');r62=load_rel('src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz)
outer=OuterScheduler(True)
for i,r in enumerate(rx+rz):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
for t in gen['terms']:outer.add_block([tuple(x) for x in t['atoms']],t['term_id'],t.get('source_term_sha256'))
for i,b in enumerate(dyn):outer.add_block([tuple(x) for x in b['atoms']],f'dynamic-{i}-{b["sector"]}',b.get('mechanism_sha256'))
assert len(outer.blocks)==14484
sector_data={'Xerr':{'checks':M.Xchecks,'edge_kind':'X','det':M.HZ,'duals':lz},'Zerr':{'checks':M.Zchecks,'edge_kind':'Z','det':M.HX,'duals':lx}}
def sig(v,det,duals):return sum(((M.popcount(v&h)&1)<<i) for i,h in enumerate(det))|sum(((M.popcount(v&h)&1)<<(72+i)) for i,h in enumerate(duals))
for lab,d in sector_data.items():d['q_sig']=[sig(1<<q,d['det'],d['duals']) for q in range(144)]
rank_cache={};member_cache={}
def pos_parity(kinds):
 s=set()
 for k in kinds:
  for p in M.RES_POS[int(k)]:
   if p in s:s.remove(p)
   else:s.add(p)
 return tuple(sorted(s))
def rank_expr(lab,c,q):
 key=(lab,c,q)
 if key not in rank_cache:
  d=sector_data[lab];tq=outer.t[M.edge_key(d['edge_kind'],c,q)];rank_cache[key]=z3.Sum([z3.If(outer.t[M.edge_key(d['edge_kind'],c,r)]<tq,1,0) for r in d['checks'][c] if r!=q])
 return rank_cache[key]
def member(lab,c,kinds,q):
 poss=pos_parity(kinds);key=(lab,c,poss,q)
 if key not in member_cache:
  r=rank_expr(lab,c,q);member_cache[key]=z3.Or([r==p for p in poss]) if poss else z3.BoolVal(False)
 return member_cache[key]
def valid_expr(m):
 lab=m['sector'];d=sector_data[lab];ds=sig(M.mask(m['data_support']),d['det'],d['duals']);terms=[[] for _ in range(84)]
 for cs,ks0 in sorted(m['group_kinds'].items(),key=lambda x:int(x[0])):
  c=int(cs);ks=tuple(sorted(map(int,ks0)))
  for q in d['checks'][c]:
   z=member(lab,c,ks,q);qs=d['q_sig'][q]
   for b in range(84):
    if (qs>>b)&1:terms[b].append(z)
 bits=[parity(terms[b],bool((ds>>b)&1)) for b in range(84)]
 return z3.And(*[z3.Not(x) for x in bits[:72]],z3.Or(*bits[72:]))
def source_eval(expr,m):
 return z3.simplify(z3.substitute(expr,*[(v,z3.IntVal(int(m['source_times'][e]))) for e,v in outer.t.items()]))
def norm_initial(m):return {'mechanism_id':m['mechanism_id'],'source_iteration':m['iteration'],'sector':m['sector'],'fault_count':m['fault_count'],'selected_names':m['selected_names'],'data_support':m['data_support'],'group_kinds':m['group_kinds'],'source_schedule_sha256':m['candidate_sha256'],'source_times':m['times'],'origin':'reviewed_round80_raw_registry'}
def add_cut(m):
 assert m['fault_count']==len(m['data_support'])+sum(len(v) for v in m['group_kinds'].values())<=10
 ex=valid_expr(m);sv=source_eval(ex,m);assert z3.is_true(sv),(m['mechanism_id'],sv)
 outer.s.add(z3.Not(ex));m=dict(m);m['source_symbolic_validity']=str(sv);m['selector_semantic_sha256']=sha({k:m[k] for k in ('sector','selected_names','data_support','group_kinds')});catalog.append(m)

catalog=[]
for m in sorted(raw['mechanisms'],key=lambda x:(x['iteration'],x['sector'])):add_cut(norm_initial(m))
seed_c=load_path(a.seed_candidate);seed_d=load_path(a.seed_domains);seed_times=seed_c['schedule_times']
for lab in ('Xerr','Zerr'):
 m=dict(seed_d['sectors'][lab]['selector']);m['source_times']=seed_times;m['origin']='round86_seed_iter102_direct360';add_cut(m)
assert len(catalog)==122

def concrete_survivors(times):
 ss=B.sectors(times,lx,lz);out=[]
 for m in catalog:
  if M.verify_named_selection(ss[m['sector']],m['selected_names'],10)['ok']:out.append(m['mechanism_id'])
 return out

def make_selector(iteration,lab,sec,mech,times,schedsha):
 names=mech['selected_names'];data=[int(n.split(':')[1]) for n in names if n.startswith('D:')];groups={}
 for n in names:
  if n.startswith('R:'):
   _,c,k=n.split(':');groups.setdefault(c,[]).append(int(k))
 return {'mechanism_id':f'r86-i{iteration}-{lab}','source_iteration':iteration,'sector':lab,'fault_count':mech['fault_count'],'selected_names':names,'data_support':data,'group_kinds':{c:sorted(v) for c,v in sorted(groups.items(),key=lambda x:int(x[0]))},'source_schedule_sha256':schedsha,'source_times':times,'canonical_support':mech['canonical_replay']['net_support'],'physical_support':mech['physical_net_support'],'source_atoms':mech['sound_outer_block']['atoms'],'source_atom_count':mech['sound_outer_block']['atom_count'],'origin':'round86_incremental_direct360'}

iterations=[];next_iter=a.start_iteration;accepted=0;stop=None
while accepted<a.max_candidates:
 formula=outer.s.to_smt2();fsha=hashlib.sha256(formula.encode()).hexdigest();outer.s.set(timeout=a.outer_timeout_ms);ts=time.monotonic();ans=outer.s.check();secs=time.monotonic()-ts;status=str(ans).upper();rec={'iteration':next_iter,'outer_status':status,'reason_unknown':outer.s.reason_unknown() if ans==z3.unknown else None,'outer_seconds':secs,'outer_formula_sha256':fsha,'existing_blocks':14484,'semantic_cuts_before':len(catalog),'assertions':len(outer.s.assertions()),'state_before_sha256':sha([{k:m.get(k) for k in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for m in catalog])}
 if ans!=z3.sat:
  rec['state_mutated']=False;rec['accepted_outer_exhaustion']=False;rec['disposition']='solver UNSAT without a separately accepted proof object' if ans==z3.unsat else 'UNKNOWN/timeout has no mathematical disposition';iterations.append(rec);stop=status;break
 mm=outer.s.model();rt={e:mm.eval(v,model_completion=True).as_long() for e,v in outer.t.items()};times=M.compress_schedule(rt);schedsha=sha(times);audit=M.audit_schedule(times,True);surv=concrete_survivors(times);assert audit['ok'] and audit['global_interleaved'] and not surv
 ss=B.sectors(times,lx,lz);direct={};new=[]
 for lab in ('Xerr','Zerr'):
  q=M.effective_adversary(ss[lab],W=10,solver_name='cadical195',conf_budget=None,with_proof=False);direct[lab]={k:v for k,v in q.items() if k not in ('witness',)}
  if q['status']=='SAT':
   selected=q['witness']['raw_selected_indices'];mech=V.mechanism(ss[lab],selected);direct[lab]['mechanism']=mech;new.append(make_selector(next_iter,lab,ss[lab],mech,times,schedsha))
 if not all(direct[x]['status']=='SAT' for x in ('Xerr','Zerr')):
  rec.update({'candidate_schedule_sha256':schedsha,'candidate_schedule':times,'candidate_audit':audit,'prior_selector_survivors':surv,'direct':direct,'new_cuts_installed':0,'state_mutated':False,'repair_entered':False,'branch_closed':False,'disposition':'non-SAT direct result is not absence without candidate-specific DRAT and LRAT acceptance'});iterations.append(rec);stop='DIRECT_'+','.join(direct[x]['status'] for x in ('Xerr','Zerr'));break
 # Atomic logical transition: validate both mechanisms and both source symbolic domains before adding either.
 exprs=[]
 for m in new:
  ex=valid_expr(m);sv=source_eval(ex,m);assert z3.is_true(sv);exprs.append((m,ex,sv))
 for m,ex,sv in exprs:
  outer.s.add(z3.Not(ex));m=dict(m);m['source_symbolic_validity']=str(sv);m['selector_semantic_sha256']=sha({k:m[k] for k in ('sector','selected_names','data_support','group_kinds')});catalog.append(m)
 rec.update({'candidate_schedule_sha256':schedsha,'candidate_schedule':times,'candidate_audit':audit,'prior_selector_survivors':surv,'direct':direct,'new_selectors':[m['mechanism_id'] for m in new],'new_cuts_installed':2,'semantic_cuts_after':len(catalog),'state_mutated':True,'repair_entered':False,'branch_closed':False,'state_after_sha256':sha([{k:m.get(k) for k in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for m in catalog])});iterations.append(rec);accepted+=1;dump(f'iterations/iter{next_iter}.json',rec);dump('checkpoint_state.json',{'schema':'round86-efssc-checkpoint-v1','next_iteration':next_iter+1,'started':False,'reviewed_base_semantic_sha256':actual,'reviewed_base_blocks':14484,'selector_count':len(catalog),'selector_state_sha256':rec['state_after_sha256'],'selectors':catalog,'completed_iterations':[r['iteration'] for r in iterations if r.get('state_mutated')]});next_iter+=1
# Persist exact final solver input and public state.
final_formula=outer.s.to_smt2();(O/'final_outer.smt2').write_text(final_formula)
state={'schema':'round86-efssc-final-state-v1','status':'PASS','reviewed_base_semantic_sha256':actual,'reviewed_base_blocks':14484,'initial_reviewed_selectors':120,'seed_round86_selectors':2,'incremental_completed_candidates':accepted,'selector_count':len(catalog),'selector_state_sha256':sha([{k:m.get(k) for k in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for m in catalog]),'next_iteration':next_iter,'started':False,'stop':stop,'rank_expressions':len(rank_cache),'membership_expressions':len(member_cache),'final_assertions':len(outer.s.assertions()),'final_formula_sha256':hashlib.sha256(final_formula.encode()).hexdigest(),'iterations':iterations,'selectors':catalog,'wall_seconds':time.monotonic()-t0}
dump('final_state.json',state);print(json.dumps({k:state[k] for k in ('status','selector_count','incremental_completed_candidates','next_iteration','started','stop','rank_expressions','membership_expressions','final_assertions','final_formula_sha256','wall_seconds')},sort_keys=True),flush=True)
