#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,collections,functools,gc,gzip,hashlib,itertools,json,struct,subprocess,sys,tempfile,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import z3
import model as M
import round68_build as B
import round68_verify as V
from outer import OuterScheduler

ALL=(1<<720)-1;SYNMASK=(1<<72)-1
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_obj(o):return sha_bytes(json.dumps(o,sort_keys=True,separators=(',',':')).encode())
def jround(o):return json.loads(json.dumps(o))
def path_for(p):
 p=Path(p)
 if p.exists():return p
 q=Path(str(p)+'.gz')
 if q.exists():return q
 raise FileNotFoundError(p)
def data(p):
 q=path_for(p);b=q.read_bytes();return gzip.decompress(b) if q.suffix=='.gz' else b
def load(p):return json.loads(data(p))
def materialize(src,dst):dst=Path(dst);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data(src));return dst
def bits(z):
 while z:b=z&-z;yield b.bit_length()-1;z^=b
def pc(z):return bin(z).count('1')
def mask(xs):return sum(1<<int(x) for x in xs)

def verify_manifest(allow_unsealed=False):
 seal=ROOT/'SHA256SUMS.txt';pay=ROOT/'PAYLOAD_SHA256SUMS.txt'
 if not seal.exists():
  assert allow_unsealed and not pay.exists(),'incomplete seal';return {'present':False,'entries':0}
 assert pay.exists();rows=[]
 for line in seal.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=ROOT/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,('seal',rel);rows.append(rel)
 expected=sorted(q.relative_to(ROOT).as_posix() for q in ROOT.rglob('*') if q.is_file() and q.relative_to(ROOT).as_posix()!='SHA256SUMS.txt');assert sorted(rows)==expected,(len(rows),len(expected))
 prows=[]
 for line in pay.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=ROOT/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,('payload',rel);prows.append(rel)
 pexpected=sorted(q.relative_to(ROOT).as_posix() for q in ROOT.rglob('*') if q.is_file() and q.relative_to(ROOT).as_posix() not in {'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'});assert sorted(prows)==pexpected
 return {'present':True,'entries':len(rows),'payload_entries':len(prows),'external_root_seal_sha256':sha_bytes(seal.read_bytes())}

def verify_compression(allow_unsealed=False):
 p=ROOT/'COMPRESSED_INVENTORY.json'
 if not p.exists():assert allow_unsealed;return {'present':False,'files':0}
 inv=load(p);assert inv['file_count']==len(inv['files']);actual=sorted(x.relative_to(ROOT).as_posix() for x in ROOT.rglob('*.gz'));assert actual==sorted(x['path'] for x in inv['files']);ut=ct=0
 for r in inv['files']:
  q=ROOT/r['path'];b=q.read_bytes();assert b[:2]==b'\x1f\x8b' and int.from_bytes(b[4:8],'little')==0 and len(b)==r['compressed_bytes'] and sha_bytes(b)==r['compressed_sha256'];z=gzip.decompress(b);assert len(z)==r['uncompressed_bytes'] and sha_bytes(z)==r['uncompressed_sha256'] and not (ROOT/r['original_path']).exists();ut+=len(z);ct+=len(b)
 assert (ut,ct)==(inv['uncompressed_bytes'],inv['compressed_bytes']);return {'present':True,'files':len(actual),'uncompressed_bytes':ut,'compressed_bytes':ct}

def verify_nested_manifest(pkg,want):
 p=pkg/'SHA256SUMS.txt';assert sha_bytes(p.read_bytes())==want;rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=pkg/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,(pkg.name,rel);rows.append(rel)
 expected=sorted(q.relative_to(pkg).as_posix() for q in pkg.rglob('*') if q.is_file() and q.relative_to(pkg).as_posix()!='SHA256SUMS.txt');assert sorted(rows)==expected;return len(rows)

def verify_bindings(repo_root=None):
 s=load(ROOT/'SOURCE_BINDINGS.json');assert s['status']=='PASS'
 assert s['commissioned_dispatcher']['sha256']=='7e49c500c7102c7df933bb406aa88dae75c47594b9f7b956e8786c9b6278b48a'
 assert s['accepted_round78']['seal_file_sha256']=='db82c387493285e56eeddcef6e7bafc3e48954c4034e6ec2fc699cea1699c987'
 assert s['accepted_round78']['payload_manifest_sha256']=='1c9b1bf35b0adba900cf188c3bf6098ff8a19b2cf1729396e2ce7ef7f60f24fb'
 assert s['fresh_round79_review']['sha256']=='e90dc1a23c5c1740267c0ed21920ef4b4af05dab1aecd5eeef934c2a25d2a17a'
 assert s['R77_F1_final_compressor']['bytes']==2760 and s['R77_F1_final_compressor']['sha256']=='d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde'
 for r in s['embedded_source_copies']:
  b=data(ROOT/r['path']);assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256'],r['path']
 for r in s['engine_files']:
  b=data(ROOT/r['path']);assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256'],r['path']
 start=s['reviewed_unstarted_iteration90'];assert start['iteration']==90 and start['installed_blocks']==12235 and start['counts']=={'base':1460,'dynamic':180,'generalized':10595,'raw_mechanisms':96,'registry':96}
 objs={}
 for k,r in start['states'].items():
  b=data(ROOT/r['path']);assert len(b)==r['uncompressed_bytes'] and sha_bytes(b)==r['uncompressed_sha256'];o=json.loads(b);assert sha_obj(o)==r['semantic_sha256']==start['semantic_sha256'][k];objs[k]=o
 assert len(objs['dynamic'])==180 and objs['generalized']['term_count']==10595 and objs['registry']['mechanism_count']==objs['raw_mechanisms']['mechanism_count']==96
 e=s['environment_freeze'];b=data(ROOT/e['path']);assert len(b)==e['bytes'] and sha_bytes(b)==e['sha256']
 cp=ROOT/s['R77_F1_final_compressor']['path'];assert len(cp.read_bytes())==2760 and sha_bytes(cp.read_bytes())==s['R77_F1_final_compressor']['sha256']
 live=0
 if repo_root:
  for r in s['live_exact_bindings']:
   b=data(ROOT/r['snapshot']);q=repo_root/r['live_path'];assert q.is_file() and q.read_bytes()==b,r['live_path'];live+=1
  ap=repo_root/s['accepted_round78']['live_repo_path'];assert sha_bytes((ap/'SHA256SUMS.txt').read_bytes())==s['accepted_round78']['seal_file_sha256'];assert sha_bytes((ap/'PAYLOAD_SHA256SUMS.txt').read_bytes())==s['accepted_round78']['payload_manifest_sha256'];live+=2
  rp=repo_root/s['fresh_round79_review']['live_repo_path'];assert sha_bytes(rp.read_bytes())==s['fresh_round79_review']['sha256'];live+=1
 return {'embedded_files':len(s['embedded_source_copies']),'engine_files':len(s['engine_files']),'reviewed_start_blocks':12235,'live_bindings_checked':live,'commissioned_dispatcher':'PASS','accepted_round78':'PASS','fresh_round79_review':'PASS','R77_F1_final_compressor':'PASS'}
def verify_state_and_ledgers():
 whole=load(ROOT/'whole_registry/hitting_synthesis/summary.json');wi=load(ROOT/'whole_registry/hitting_synthesis/install_result.json');assert whole['status']=='PASS' and whole['retained']==whole['strict_installed_union_expansions']==24 and whole['literal_pair_cells_replayed']==304704 and whole['complete_factorized_product_tuples']==35294400
 assert wi['state_before_semantic_sha256']=='ba4e37e48c856f8966fd86540daab423468c551289856517aacc35cc1403c8f3' and wi['state_after_semantic_sha256']=='b71eb0509a99016a1718aa2f03ba19193c9b88ef359b47898c3d3517127e9a5f'
 cs=load(ROOT/'cegar/summary.json');assert cs['status']=='PASS' and cs['iteration_range']==[90,101] and cs['completed_dual_sector_candidates']==12 and cs['outer_verdicts']=={'SAT':12,'TIMEOUT':0,'UNKNOWN':0,'UNSAT':0} and cs['direct_sector_verdicts']=={'SATISFIABLE':24,'UNKNOWN_OR_TIMEOUT':0,'UNSAT_PROOFS_ACCEPTED':0} and cs['candidate_exact_blocks_added']==24 and not cs['branch_closed'] and cs['accepted_absence_proofs']==0
 chain=load(ROOT/'cegar/iteration_state_chain.json');assert chain['status']=='PASS' and len(chain['iterations'])==12 and chain['next_iteration']==102
 previous={'dynamic':'30227f09a28c318ea392ae0473cc7644c294ea02aac6007d30eaddd1884ee348','generalized':'b71eb0509a99016a1718aa2f03ba19193c9b88ef359b47898c3d3517127e9a5f','registry':'6663a3a3036199de684255c622690ebf00e02b7e5fd0249af6bbafcfece42cdd','raw_mechanisms':'6746258d7e045c211596ec264a1bcf9a748357e6b7a8f76008e532e189179f1f'}
 prev_counts={'dynamic':180,'generalized':10619,'registry':96,'raw_mechanisms':96,'total':12259};totals={'online':0,'cross':0}
 for i,row in zip(range(90,102),chain['iterations']):
  d=ROOT/'cegar'/f'iter{i}';o=load(d/'iteration_outcome.json');c=load(d/'state_commit_complete.json');cand=load(d/'candidate.json');outer=load(d/'outer_result.json');orep=load(d/'outer_independent_replay.json');dv=load(d/'direct_verification.json');g=load(d/'generalization/summary.json');x=load(d/'cross_registry/summary.json');aa=load(d/'direct_absence_attempt.json')
  assert row['iteration']==o['iteration']==c['iteration']==i and o['fresh_outer_process'] and o['outer_status']==outer['status']=='SAT' and orep['status']=='PASS' and orep['parsed_ordered_assertions_equal'] and orep['serialized_formula_fixed_model_status']=='SAT'
  assert c['status']=='PASS' and c['all_live_bindings_match'] and c['before_semantic_sha256']==previous and row['before_semantic_sha256']==previous and sha_bytes(data(d/'state_commit_complete.json'))==row['commit_complete_file_sha256']==o['state_commit_complete_sha256']
  assert {'dynamic':o['dynamic_blocks_before'],'generalized':o['generalized_terms_before'],'registry':o['mechanism_registry_before'],'raw_mechanisms':o['raw_mechanisms_before'],'total':o['installed_blocks_before']}==prev_counts
  assert g['status']==x['status']=='PASS' and g['retained_increment']==o['online_generalized_retained_increment'] and x['retained_increment']==o['cross_registry_retained_increment'] and o['dynamic_blocks_after']==o['dynamic_blocks_before']+2 and o['generalized_terms_after']==o['generalized_terms_before']+g['retained_increment']+x['retained_increment'] and o['mechanism_registry_after']==o['raw_mechanisms_after']==o['mechanism_registry_before']+2
  assert cand['asserted_blocks']['total']==o['installed_blocks_before'] and cand['audit']['ok'] and cand['audit']['global_interleaved'] and cand['audit']['edge_count']==864 and cand['audit']['overlaps']==648
  assert all(o['all_dimacs_clauses_satisfied'].values()) and o['raw_replay_passed'] and not o['repair_entered'] and not o['branch_closed'] and aa['solver_status']=='SAT' and not aa['absence_accepted'] and aa['selected_sector']==max(aa['sector_formula_counts'],key=lambda lab:(aa['sector_formula_counts'][lab]['clauses'],aa['sector_formula_counts'][lab]['variables'],lab))
  if i==90:
   trace=data(d/aa['proof_output_path']);assert aa['proof_producing_solver_requested'] and len(trace)==aa['proof_output_bytes']==248948763 and sha_bytes(trace)==aa['proof_output_sha256']=='420634d8d7bcbe9184e3a16a04915a5cbb6f2f5ea248360f9d407af7d18e48c9'
  else:assert not aa['proof_producing_solver_requested'] and not aa['proof_output_exists'] and aa['proof_output_bytes']==0
  for lab in ('Xerr','Zerr'):
   sec=dv['sectors'][lab];fs=sec['formula_summary'];assert sec['status']=='SATISFIABLE' and sec['all_dimacs_clauses_satisfied'] and fs['complete_query'] and fs['primary_selection_variables']==360 and fs['W']==10 and sec['mechanism']['canonical_replay']['ok'] and sec['mechanism']['physical_syndrome']==[] and sec['mechanism']['physical_nontrivial'] and sec['mechanism']['fault_count']<=10
  previous=dict(c['after_semantic_sha256']);assert row['after_semantic_sha256']==previous;totals['online']+=g['retained_increment'];totals['cross']+=x['retained_increment'];prev_counts={'dynamic':o['dynamic_blocks_after'],'generalized':o['generalized_terms_after'],'registry':o['mechanism_registry_after'],'raw_mechanisms':o['raw_mechanisms_after'],'total':o['installed_blocks_after']}
 assert previous==chain['final_semantic_sha256'];rs=load(ROOT/'restart/restart_state.json');assert rs['status']=='PASS' and rs['next_iteration']==102 and not rs['started'] and rs['counts']=={'dynamic':prev_counts['dynamic'],'generalized':prev_counts['generalized'],'raw_mechanisms':120,'registry':120,'total_blocks':prev_counts['total']} and rs['semantic_sha256']==previous and not rs['branch_closed']
 live={'dynamic':load(ROOT/'cegar/dynamic_blocks.json'),'generalized':load(ROOT/'classification/installed_generalized_terms.json'),'registry':load(ROOT/'classification/online_mechanism_registry.json'),'raw_mechanisms':load(ROOT/'classification/full_raw_mechanisms.json')}
 for k,r in rs['states'].items():b=data(ROOT/r['path']);o=json.loads(b);assert len(b)==r['bytes'] and sha_bytes(b)==r['file_sha256'] and sha_obj(o)==r['semantic_sha256']==previous[k] and o==live[k]
 wterms=load(ROOT/'whole_registry/hitting_synthesis/retained_terms.json')['terms'];online=load(ROOT/'classification/round80_online_retained_terms.json')['terms'];cross=load(ROOT/'cross_registry/round80_cross_registry_retained_terms.json')['terms'];allnew=wterms+online+cross;ids=[t['term_id'] for t in allnew];assert len(ids)==len(set(ids)) and set(ids)<={t['term_id'] for t in live['generalized']['terms']}
 assert load(ROOT/'RESULT.json')['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED' and not load(ROOT/'RESULT.json')['D_star_Gross_changed'] and (ROOT/'VERDICT.txt').read_text().strip()=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED'
 return {'completed_candidates':12,'direct_sat_raw_replayed':24,'new_exact_blocks':24,'whole_registry_terms':24,'online_terms':totals['online'],'cross_registry_terms':totals['cross'],'final_dynamic':prev_counts['dynamic'],'final_generalized':prev_counts['generalized'],'final_registry':120,'next_iteration':102,'next_total_blocks':prev_counts['total'],'absence_proofs':0,'branch_closed':False}
def verify_processes():
 p=load(ROOT/'PROCESS_LEDGER.json');rows=p['accepted_cegar_process_records'];assert p['status']=='PASS' and p['strict_serial_execution'] and len(rows)==p['accepted_cegar_process_count'] and p['accepted_iterations']==12 and p['post_control_state_semantic_sha256']==load(ROOT/'restart/restart_state.json')['semantic_sha256']
 assert all(not r['timed_out'] and not r['sigterm_sent'] and not r['sigkill_sent'] for r in rows)
 for a,b in zip(rows,rows[1:]):assert a['ended_utc']<=b['started_utc']
 assert sorted(set(r['iteration'] for r in rows))==list(range(90,102))
 return {'accepted_records':len(rows),'exit_codes':dict(collections.Counter(str(r['exit_code']) for r in rows)),'timeouts':0,'signals':0,'development_attempts':len(p['development_attempts']),'proof_control_attempts':len(p['proof_control_records'])}
def verify_negative_controls():
 n=load(ROOT/'controls/negative_controls.json');assert n['status']=='PASS' and len(n['direct_controls'])==24 and len(n['schedule_mutation_controls'])==12
 for r in n['direct_controls']:assert r['flip_assignment_control']['failed_clause_count']>0 and not r['remove_fault_control']['ok']
 for r in n['schedule_mutation_controls']:
  times={k:int(v) for k,v in load(ROOT/'cegar'/f"iter{r['iteration']}"/'candidate.json')['schedule_times'].items()};m=r['mutation'];times[m['edge']]=m['corrupted_time'];assert jround(M.audit_schedule(times,True))==r['audit'] and not r['accepted']
 raw=data(ROOT/n['truncated_assignment']['path']);lits=[]
 for line in raw.decode(errors='replace').splitlines():
  if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
 assert len({abs(x) for x in lits})==n['truncated_assignment']['expected_variables']-1 and sha_bytes(raw)==n['truncated_assignment']['uncompressed_sha256'] and not n['truncated_assignment']['accepted']
 assert all(v==0 for v in n['absence_semantics'].values());return n['counts']
def run_control(cmd,want,markers):
 p=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=30);assert p.returncode==want and any(x.encode() in p.stdout for x in markers),(p.returncode,p.stdout[-1000:]);return {'exit_code':p.returncode,'marker':next(x for x in markers if x.encode() in p.stdout)}
def verify_proof_controls():
 c=ROOT/'controls/round80_proof_checker';t=ROOT/'tooling';s=load(c/'summary.json');assert s['status']=='PASS' and s['fresh_generation'] and s['counts']=={'candidate_specific_gross_proofs':0,'corrupt_rejects':2,'proof_generation_unsat':1,'truncated_rejects':2,'valid_accepts':2}
 for n,r in s['fixtures'].items():b=data(c/n);assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256']
 with tempfile.TemporaryDirectory(prefix='circdist_r80_proof_') as td:
  lrat=Path(td)/'generated.lrat';out={};out['drat_valid']=run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.fresh.drat','-t','170','-L',lrat],0,['VERIFIED']);assert sha_bytes(lrat.read_bytes())==s['fixtures']['php6_5.fresh.lrat']['sha256'];out['lrat_valid']=run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',lrat],0,['VERIFIED']);out['drat_corrupt']=run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.corrupt.drat','-t','170'],1,['NOT VERIFIED','ERROR']);out['drat_truncated']=run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.truncated.drat','-t','170'],1,['NOT VERIFIED','ERROR']);out['lrat_corrupt']=run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',c/'php6_5.corrupt.lrat'],1,['NOT VERIFIED','ERROR']);out['lrat_truncated']=run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',c/'php6_5.truncated.lrat'],1,['NOT VERIFIED','ERROR']);return out
def load_outer_context():
 px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');unary=rx+rz;assert len(unary)==1440;r62=load(ROOT/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz);assert len(r62['outer_blocks'])==20;return px,pz,lx,lz,unary,r62
def verify_outer_fresh(i):
 px,pz,lx,lz,unary,r62=load_outer_context();d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');before=load(d/'dynamic_before.json');gens=load(d/'generalized_before.json');outer=OuterScheduler(True)
 for j,r in enumerate(unary):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 for t in gens['terms']:outer.add_block([tuple(x) for x in t['atoms']],t['term_id'],t.get('source_term_sha256'))
 for j,b in enumerate(before):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b.get('mechanism_sha256'))
 assert len(outer.blocks)==cand['asserted_blocks']['total']==1440+20+gens['term_count']+len(before);rebuilt=outer.s.to_smt2().encode();stored=data(d/'outer.smt2');assert rebuilt==stored,(i,sha_bytes(rebuilt),sha_bytes(stored));times={k:int(v) for k,v in cand['schedule_times'].items()};assert M.audit_schedule(times,True)==cand['audit'] and set(times)==set(M.ALL_EDGES)
 fixed=z3.Solver();fixed.add(z3.parse_smt2_string(stored.decode()))
 for e in M.ALL_EDGES:fixed.add(z3.Int('t_'+e.replace(':','_'))==times[e])
 assert fixed.check()==z3.sat and all(not M.block_holds(times,[tuple(x) for x in t['atoms']]) for t in gens['terms']) and all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in before)
 return {'schema':'round78-fresh-outer-full-replay-v1','status':'PASS','iteration':i,'blocks':len(outer.blocks),'smt2_sha256':sha_bytes(stored),'schedule_sha256':sha_obj(times),'fixed_model_status':'SAT','named_edges':864,'mc_constraints':648}

def verify_direct_full():
 px,pz,lx,lz,unary,r62=load_outer_context();rows=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r80_direct_') as td:
  tmp=Path(td)
  for i in range(90,102):
   d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');saved=load(d/'direct_verification.json');times={k:int(v) for k,v in cand['schedule_times'].items()};ss=B.sectors(times,lx,lz);vr=tmp/f'iter{i}';(vr/'direct360').mkdir(parents=True);(vr/'solver').mkdir()
   for lab in ('Xerr','Zerr'):
    gen=tmp/f'generated-{i}'/lab;gen.parent.mkdir(parents=True,exist_ok=True);B.build_direct_cnf(ss[lab],gen,cand['schedule_sha256'],10)
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):
     got=data(d/'direct360'/f'{lab}.{suffix}');want=gen.with_suffix('.'+suffix).read_bytes();assert got==want,(i,lab,suffix,sha_bytes(got),sha_bytes(want));(vr/'direct360'/f'{lab}.{suffix}').write_bytes(got)
    (vr/'solver'/f'{lab}.solver.log').write_bytes(data(d/'solver'/f'{lab}.solver.log'));got=jround(V.verify_one(vr,lab,ss[lab]));assert got==saved['sectors'][lab];rows.append({'iteration':i,'sector':lab,'cnf_sha256':sha_bytes(data(d/'direct360'/f'{lab}.cnf')),'assignment_variables':got['assignment_variables'],'fault_weight':got['mechanism']['fault_count'],'raw_replay':'PASS'})
 return {'status':'PASS','formulae_rebuilt':24,'assignments_replayed':24,'rows':rows}

def sig_context():
 px,pz,lx,lz=B.load_context();return px,pz,lx,lz
def signature(lab,v,lx,lz):
 det=M.HZ if lab=='Xerr' else M.HX;duals=lz if lab=='Xerr' else lx;return sum(((pc(v&r)&1)<<j) for j,r in enumerate(det))|(sum(((pc(v&r)&1)<<j) for j,r in enumerate(duals))<<72)
def valid_signature(s):return (s&SYNMASK)==0 and (s>>72)!=0
def sector_rows(lab):return M.Xchecks if lab=='Xerr' else M.Zchecks
def edge(lab,c,q):return M.edge_key('X' if lab=='Xerr' else 'Z',c,q)
def support_atoms(lab,c,row,k,s):
 S=set(M.bits(s));O=set(row)-S;pairs=(S,O) if k==0 else (O,S);return tuple(sorted((edge(lab,c,q),'<',edge(lab,c,r)) for q in pairs[0] for r in pairs[1]))

def verify_all_raw_mechanisms():
 px,pz,lx,lz=sig_context();raw=load(ROOT/'classification/full_raw_mechanisms.json');reg=load(ROOT/'classification/online_mechanism_registry.json');dyn=load(ROOT/'cegar/dynamic_blocks.json');assert raw['mechanism_count']==reg['mechanism_count']==120;regmap={m['mechanism_id']:m for m in reg['mechanisms']};dynmap={(x['source_iteration'],x['sector']):x for x in dyn if x.get('source_iteration',-1)>=42};sectors=collections.Counter()
 for m in raw['mechanisms']:
  lab=m['sector'];rows=sector_rows(lab);cv=pv=int(m['data_mask']);atoms=[];assert m['fault_count']==len(m['data_support'])+len(m['fault_instances'])<=10 and M.bits(m['data_mask'])==m['data_support']
  for f in m['fault_instances']:
   c=int(f['check']);k=int(f['kind']);order=tuple(m['source_orders'][str(c)]);assert sorted(order)==rows[c];sv=M.mask(order[j] for j in M.RES_POS[k]);ph=M.mask(order[j] for j in M.PHYS_POS[k]);assert M.bits(sv)==f['support'];cv^=sv;pv^=ph;atoms.extend(support_atoms(lab,c,rows[c],k,sv))
  atoms=sorted(set(atoms));assert [list(x) for x in atoms]==m['source_atoms'] and M.bits(cv)==m['canonical_support'] and M.bits(pv)==m['physical_support'];cs=signature(lab,cv,lx,lz);ps=signature(lab,pv,lx,lz);assert cs==ps and valid_signature(cs)
  r=regmap[m['mechanism_id']];assert all(r[k]==m[k] for k in ('iteration','sector','canonical_support','canonical_weight','physical_support','physical_weight','sealed_mechanism_sha256'));db=dynmap[(m['iteration'],lab)];assert db['atoms']==m['source_atoms'] and db['mechanism_sha256']==m['sealed_mechanism_sha256'];sectors[lab]+=1
 assert sectors=={'Xerr':60,'Zerr':60};return {'status':'PASS','mechanisms':120,'sectors':dict(sectors),'canonical_physical_signature_identity':120,'candidate_exact_blocks_matched':120}
def catalog_runtime(entry,lx,lz):
 assert len(entry['orders'])==720 and [x['order_id'] for x in entry['orders']]==list(range(720));lab=entry['sector'];row=entry['row'];opts=collections.defaultdict(int);unary=[];cmp={}
 for q in row:
  for r in row:
   if q!=r:cmp[(q,r)]=0
 for o in entry['orders']:
  assert sorted(o['qubits'])==sorted(row);pos={q:j for j,q in enumerate(o['qubits'])}
  for q,r in cmp:
   if pos[q]<pos[r]:cmp[(q,r)]|=1<<o['order_id']
  for op in o['options']:
   cv=mask(op['canonical_support']);pv=mask(op['physical_support']);sg=signature(lab,cv,lx,lz);assert sg==signature(lab,pv,lx,lz)==int(op['signature_hex'],16);opts[(int(op['kind']),tuple(op['canonical_support']))]|=1<<o['order_id']
  u=o['unary_witness'];unary.append(u)
  if u is not None:sg=signature(lab,mask(u['logical_support']),lx,lz);assert valid_signature(sg) and u['fault_weight']<=10
 um=int(entry['unary_mask_hex'],16);assert um==sum((1<<i) for i,u in enumerate(unary) if u is not None) and pc(um)==entry['unary_bad_order_count']==360 and entry['good_mask_hex']==hex(ALL^um)
 return {'entry':entry,'unary':unary,'unary_mask':um,'good':ALL^um,'opts':opts,'cmp':cmp}
def term_atom_mask(t,c,cat):
 z=ALL
 for a in t['atoms']:
  if int(a[0].split(':')[1])!=c:continue
  q=int(a[0].split(':')[2]);r=int(a[2].split(':')[2]);z&=cat['cmp'][(q,r)]
 return z
def update_online_hash(h,orders,cv,pv,ft,wk):h.update(struct.pack('>B',len(orders))+b''.join(struct.pack('>H',x) for x in orders)+cv.to_bytes(18,'big')+pv.to_bytes(18,'big')+struct.pack('>BB',ft,wk))
def verify_pair_batch(base,kind,lx,lz):
 cats_obj=load(base/'local_order_catalog.json');cats={(e['sector'],e['check']):catalog_runtime(e,lx,lz) for e in cats_obj['entries']};rels=load(base/'pair_relations.json')['relations'];terms=load(base/'retained_terms.json')['terms'];tuple_obj=load(base/'tuple_raw_replay.json');tuplemap={x['term_id']:x for x in tuple_obj['terms']};pair_terms=[t for t in terms if 'pair_rectangle' in t['relation_kind']];groups=collections.defaultdict(list)
 for t in pair_terms:groups[(t['sector'],t['a'],t['b'])].append(t)
 total=0;relation_cells=0;explicit_cells=0
 @functools.lru_cache(maxsize=None)
 def val(lab,cv,pv):
  a=signature(lab,cv,lx,lz);b=signature(lab,pv,lx,lz);assert a==b and valid_signature(a);return a
 for rel in rels:
  key=(rel['sector'],rel['a'],rel['b']);ca=cats[(rel['sector'],rel['a'])];cb=cats[(rel['sector'],rel['b'])];explicit=[0]*720;choices=[{} for _ in range(720)];confm=[]
  for ci,c in enumerate(rel['positive_configurations']):
   ak=(int(c['a_kind']),tuple(c['a_support']));bk=(int(c['b_kind']),tuple(c['b_support']));A=ca['opts'][ak]&ca['good'];Bm=cb['opts'][bk]&cb['good'];confm.append((A,Bm))
   for i in bits(A):
    explicit[i]|=Bm
    z=Bm
    while z:
     b=z&-z;j=b.bit_length()-1;choices[i].setdefault(j,ci);z^=b
  truth=[ALL if ((ca['unary_mask']>>i)&1) else cb['unary_mask']|explicit[i] for i in range(720)];assert [hex(x) for x in explicit]==rel['explicit_good_good_rows_hex'] and [hex(x) for x in truth]==rel['truth_rows_hex'];assert sum(pc(x) for x in truth)==rel['truth_cell_count'] and sum(pc(x) for x in explicit)==rel['explicit_good_good_cell_count'] and len(confm)==rel['positive_configuration_count'];relation_cells+=rel['truth_cell_count'];explicit_cells+=rel['explicit_good_good_cell_count']
  for t in groups.get(key,[]):
   A=term_atom_mask(t,t['a'],ca);Bm=term_atom_mask(t,t['b'],cb);assert A==int(t['a_order_mask_hex'],16) and Bm==int(t['b_order_mask_hex'],16) and pc(A)==t['a_order_count'] and pc(Bm)==t['b_order_count'] and pc(A)*pc(Bm)==t['covered_tuple_count']>0 and all((Bm&~truth[i])==0 for i in bits(A))
   h=hashlib.sha256();hist=collections.Counter();shist=collections.Counter();sigs=set();samples=[];count=0
   for i in bits(A):
    for j in bits(Bm):
     if ca['unary'][i] is not None:u=ca['unary'][i];cv=pv=mask(u['logical_support']);ft=int(u['fault_weight']);wk=1;src={'kind':'a_unary','pool_index':u['pool_index']}
     elif cb['unary'][j] is not None:u=cb['unary'][j];cv=pv=mask(u['logical_support']);ft=int(u['fault_weight']);wk=2;src={'kind':'b_unary','pool_index':u['pool_index']}
     else:
      ci=choices[i][j];c=rel['positive_configurations'][ci];D=mask(c['singleton_support']);cv=mask(c['a_support'])^mask(c['b_support'])^D;oa=ca['entry']['orders'][i]['options'][int(c['a_kind'])];ob=cb['entry']['orders'][j]['options'][int(c['b_kind'])];pv=mask(oa['physical_support'])^mask(ob['physical_support'])^D;ft=int(c['fault_weight']);wk=3;src={'kind':'global_explicit','configuration_id':c['configuration_id']} if kind=='cross' else {'kind':'explicit_pair','configuration_index':ci}
     sg=val(t['sector'],cv,pv);assert ft<=10
     if kind=='cross':h.update(struct.pack('>HH',i,j)+cv.to_bytes(18,'big')+pv.to_bytes(18,'big')+struct.pack('>BB',ft,wk));shist[src['kind']]+=1
     else:update_online_hash(h,[i,j],cv,pv,ft,wk)
     count+=1;hist[ft]+=1;sigs.add(sg)
     if len(samples)<3:
      if kind=='cross':samples.append({'order_ids':{str(t['a']):i,str(t['b']):j},'canonical_support':M.bits(cv),'physical_support':M.bits(pv),'fault_count':ft,'signature_hex':hex(sg),'selector':src})
      else:samples.append({'order_ids':{str(t['a']):i,str(t['b']):j},'canonical_mask_hex':hex(cv),'canonical_support':M.bits(cv),'physical_mask_hex':hex(pv),'physical_support':M.bits(pv),'fault_weight':ft,'signature_hex':hex(sg),'selector_source':src})
   q=tuplemap[t['term_id']];assert count==q['tuples_instantiated']==t['covered_tuple_count'] and h.hexdigest()==q['selector_stream_sha256'] and {str(k):v for k,v in hist.items()}==q['fault_count_histogram' if kind=='cross' else 'fault_weight_histogram'] and sha_obj([hex(s) for s in sorted(sigs)])==q['signature_set_sha256'] and len(sigs)==q['signature_count'] and samples==q['samples']
   if kind=='cross':assert {str(k):v for k,v in shist.items()}==q['selector_kind_histogram'] and q['validation_mode']=='literal_every_tuple' and q['all_canonical_physical_replays_passed']
   else:assert q['validation_mode']=='literal_every_tuple' and q['selector_stream_scope']=='every covered tuple' and q['all_raw_replays_passed']
   total+=count
 assert sum(t['covered_tuple_count'] for t in pair_terms)==total;return {'catalogs':len(cats),'relations':len(rels),'pair_terms':len(pair_terms),'literal_tuples':total,'truth_cells':relation_cells,'explicit_cells':explicit_cells,'cats':cats,'tuplemap':tuplemap,'terms':terms}

def verify_online_multi(base,rt,lx,lz):
 terms=[t for t in rt['terms'] if t['relation_kind'].startswith('multi')];rels=load(base/'multi_check_relations.json')['relations'];relmap={(r['mechanism_id'],r['sector']):r for r in rels};mechs={m['mechanism_id']:m for m in load(base/'mechanisms.json')['mechanisms']};total=0
 for t in terms:
  rel=relmap[(t['mechanism_id'],t['sector'])];mech=mechs[t['mechanism_id']];checks=t['checks'];product=1;dp={int(t['constant_signature_hex'],16)};layers=[];fh=hashlib.sha256()
  for c in checks:
   m=int(t['allowed_order_masks_hex'][str(c)],16);assert m>0;ids=list(bits(m));assert len(ids)==t['allowed_order_counts'][str(c)];product*=len(ids);records=rel['local_order_contributions'][str(c)]['per_order'];assert len(records)==720;sigs=set();cat=rt['cats'][(t['sector'],c)]
   for j in ids:
    rec=records[j];assert rec['order_id']==j;cv=mask(rec['canonical_support']);pv=mask(rec['physical_support']);sg=signature(t['sector'],cv,lx,lz);assert sg==signature(t['sector'],pv,lx,lz)==int(rec['signature_hex'],16);sigs.add(sg);update_online_hash(fh,[j],cv,pv,mech['fault_count'],4)
   dp={a^b for a in dp for b in sigs};layers.append({'check':c,'reachable_signature_count':len(dp),'reachable_signatures_sha256':sha_obj([hex(z) for z in sorted(dp)])})
  q=rt['tuplemap'][t['term_id']];h=hashlib.sha256();h.update(fh.digest());assert product==t['covered_tuple_count']==q['tuples_instantiated'] and layers==t['dp_layers'] and len(dp)==t['reachable_signature_count'] and all(valid_signature(z) for z in dp) and h.hexdigest()==q['selector_stream_sha256'] and q['validation_mode']=='factorized_symbolic_universal' and q['all_raw_replays_passed'];total+=product
 return {'multi_terms':len(terms),'factorized_tuples':total}

def verify_whole_registry():
 px,pz,lx,lz=sig_context();base=ROOT/'whole_registry/pair_leaf_reconstruction';leaf=verify_pair_batch(base,'cross',lx,lz);assert leaf['pair_terms']==0 and leaf['relations']==1557
 cats_obj=load(base/'local_order_catalog.json');catobj={(e['sector'],int(e['check'])):e for e in cats_obj['entries']};cats=leaf['cats'];rels={(r['sector'],int(r['a']),int(r['b'])):r for r in load(base/'pair_relations.json')['relations']};proofs=load(ROOT/'whole_registry/hitting_synthesis/factorized_selector_proofs.json')['proofs'];terms=load(ROOT/'whole_registry/hitting_synthesis/retained_terms.json')['terms'];before=load(ROOT/'whole_registry/hitting_synthesis/generalized_before.json');after=load(ROOT/'whole_registry/hitting_synthesis/generalized_after.json');assert before['term_count']==10595 and len(proofs)==len(terms)==24 and after['terms']==before['terms']+terms and after['term_count']==10619
 def relfor(lab,x,y):return rels[(lab,*sorted((x,y)))]
 def good(rel,center,lm):
  truth=[int(x,16) for x in rel['truth_rows_hex']]
  if center==int(rel['a']):return sum((1<<oc) for oc,row in enumerate(truth) if not (lm & (ALL^row)))
  z=ALL
  for ol in bits(lm):z&=truth[ol]
  return z
 def getmask(t,c):return term_atom_mask(t,c,cats[(t['sector'],c)])
 def selector(rel,oa,ob):
  ca=catobj[(rel['sector'],int(rel['a']))];cb=catobj[(rel['sector'],int(rel['b']))];wa=ca['orders'][oa]['unary_witness'];wb=cb['orders'][ob]['unary_witness']
  if wa is not None:
   v=mask(wa['logical_support']);return v,v,int(wa['fault_weight']),{'kind':'a_unary','check':rel['a'],'order_id':oa,'residual_kind':1,'data_support':wa['singleton_support'],'canonical_support':wa['logical_support'],'physical_support':wa['logical_support']}
  if wb is not None:
   v=mask(wb['logical_support']);return v,v,int(wb['fault_weight']),{'kind':'b_unary','check':rel['b'],'order_id':ob,'residual_kind':1,'data_support':wb['singleton_support'],'canonical_support':wb['logical_support'],'physical_support':wb['logical_support']}
  for conf in rel['positive_configurations']:
   ao=ca['orders'][oa]['options'][int(conf['a_kind'])];bo=cb['orders'][ob]['options'][int(conf['b_kind'])]
   if mask(ao['canonical_support'])==mask(conf['a_support']) and mask(bo['canonical_support'])==mask(conf['b_support']):
    d=mask(conf['singleton_support']);cv=mask(ao['canonical_support'])^mask(bo['canonical_support'])^d;pv=mask(ao['physical_support'])^mask(bo['physical_support'])^d;return cv,pv,int(conf['fault_weight']),{'kind':'explicit_pair','configuration_id':conf['configuration_id'],'checks':[rel['a'],rel['b']],'order_ids':[oa,ob],'residual_kinds':[conf['a_kind'],conf['b_kind']],'data_support':conf['singleton_support'],'a_source_mechanisms':conf['a_source_mechanisms'],'b_source_mechanisms':conf['b_source_mechanisms'],'canonical_support':M.bits(cv),'physical_support':M.bits(pv)}
  raise AssertionError('no selector')
 literal=factor=0;prior=[]
 for j,(t,q) in enumerate(zip(terms,proofs)):
  assert t['term_id']==q['term_id'];lab=t['sector'];center=int(t['center']);leaves=list(map(int,t['leaves']));checks=sorted({int(a[0].split(':')[1]) for a in t['atoms']});masks={c:getmask(t,c) for c in checks};assert all(masks[c]>0 for c in checks) and {str(c):hex(masks[c]) for c in checks}==q['allowed_order_masks_hex'] and {str(c):pc(masks[c]) for c in checks}==q['allowed_order_counts']
  goods=[good(relfor(lab,center,l),center,masks[l]) for l in leaves];covered=0;parts=[]
  for g in goods:parts.append(masks[center]&g&(ALL^covered));covered|=g
  assert not (masks[center]&(ALL^covered)) and sum(pc(x) for x in parts)==pc(masks[center]) and sum(bool(x) for x in parts)>=2 and {str(l):hex(x) for l,x in zip(leaves,parts)}==q['center_partition_masks_hex']
  h=hashlib.sha256();hist=collections.Counter();kh=collections.Counter();sigs=set();samples=[];pairn=mult=0
  for li,(l,part) in enumerate(zip(leaves,parts)):
   rel=relfor(lab,center,l);truth=[int(x,16) for x in rel['truth_rows_hex']];other=1
   for z in leaves:
    if z!=l:other*=pc(masks[z])
   for oc in bits(part):
    for ol in bits(masks[l]):
     oa,ob=(oc,ol) if center==int(rel['a']) else (ol,oc);assert (truth[oa]>>ob)&1;cv,pv,ft,sel=selector(rel,oa,ob);sg=signature(lab,cv,lx,lz);assert sg==signature(lab,pv,lx,lz) and valid_signature(sg) and ft<=10;pairn+=1;mult+=other;hist[ft]+=1;kh[sel['kind']]+=1;sigs.add(sg);h.update(struct.pack('>BBHH',li,len(leaves),oc,ol)+cv.to_bytes(18,'big')+pv.to_bytes(18,'big')+struct.pack('>B',ft))
     if len(samples)<6:samples.append({'center_order_id':oc,'leaf':l,'leaf_order_id':ol,'canonical_support':M.bits(cv),'physical_support':M.bits(pv),'fault_count':ft,'signature_hex':hex(sg),'explicit_raw_physical_selector':sel})
  prod=1
  for c in checks:prod*=pc(masks[c])
  assert pairn==q['literal_pair_cells_replayed'] and mult==prod==q['complete_factorized_product_tuples']==q['selector_induced_full_tuple_multiplicity'] and h.hexdigest()==q['selector_stream_sha256'] and {str(k):v for k,v in hist.items()}==q['fault_count_histogram_on_literal_pair_cells'] and dict(kh)==q['selector_kind_histogram_on_literal_pair_cells'] and len(sigs)==q['signature_count'] and sha_obj([hex(x) for x in sorted(sigs)])==q['signature_set_sha256'] and samples==q['explicit_raw_physical_selector_samples']
  w=q['strict_installed_union_expansion_witness'];orders=w['complete_local_orders'];assert sha_obj(orders)==w['complete_local_orders_sha256'] and w['status']=='SAT' and w['strictly_outside_union'] and w['avoided_installed_terms']==10595+j
  tm={}
  for ck,order in orders.items():
   la,c=ck.split(':');assert sorted(order)==(M.Xchecks if la=='X' else M.Zchecks)[int(c)]
   for posv,qubit in enumerate(order):tm[M.edge_key(la,int(c),int(qubit))]=posv
  assert M.block_holds(tm,[tuple(a) for a in t['atoms']]) and all(not M.block_holds(tm,[tuple(a) for a in u['atoms']]) for u in before['terms']+prior);prior.append(t);literal+=pairn;factor+=prod
 assert literal==304704 and factor==35294400
 with tempfile.TemporaryDirectory(prefix='circdist_r80_whole_rebuild_') as td:
  td=Path(td);st=td/'start.json';st.write_bytes(data(ROOT/'restart/installed_generalized_terms_iteration90.json'));out=td/'out';cp=subprocess.run([sys.executable,str(ROOT/'src/synthesize_whole_registry.py'),'--root',str(ROOT),'--leaf-root',str(base),'--generalized-state',str(st),'--output-root',str(out),'--batch-id','pre090','--max-retained','24'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=1200);assert cp.returncode==0,cp.stdout[-4000:]
  names=['raw_candidates.json','classification_ledger.json','retained_terms.json','factorized_selector_proofs.json','generalized_before.json','generalized_after.json','summary.json','install_result.json']
  for name in names:assert load(out/name)==load(ROOT/'whole_registry/hitting_synthesis'/name),name
 return {'status':'PASS','leaf_catalogs':leaf['catalogs'],'leaf_relations':leaf['relations'],'leaf_truth_cells':leaf['truth_cells'],'retained_terms':24,'literal_pair_cells_replayed':literal,'complete_factorized_product_tuples':factor,'strict_outside_witnesses':24,'full_synthesis_rebuild_and_classification_match':True}

def verify_all_term_domains():
 px,pz,lx,lz=sig_context();rows=[];literal=0;factor=0
 for i in range(90,102):
  for base,kind,name in [(ROOT/'cegar'/f'iter{i}'/'generalization','online',f'online{i}'),(ROOT/'cegar'/f'iter{i}'/'cross_registry','cross',f'post{i}')]:
   rt=verify_pair_batch(base,kind,lx,lz);literal+=rt['literal_tuples'];multi={'multi_terms':0,'factorized_tuples':0}
   if kind=='online':multi=verify_online_multi(base,rt,lx,lz);factor+=multi['factorized_tuples']
   else:assert load(base/'multi_selector_dp_proofs.json')['proofs']==[]
   rows.append({'batch':name,'kind':kind,'catalogs':rt['catalogs'],'relations':rt['relations'],'pair_terms':rt['pair_terms'],'literal_tuples':rt['literal_tuples'],**multi});del rt;gc.collect()
 want=load(ROOT/'RESULT.json')['validation_domains'];assert literal==want['cross_registry_literal_pair_tuples']+want['online_literal_tuples'] and factor==want['online_factorized_multi_tuples'];return {'status':'PASS','batches':24,'literal_every_tuple_replays':literal,'factorized_multi_tuples':factor,'rows':rows}
def verify_full():
 outer=[]
 for i in range(90,102):
  p=subprocess.run([sys.executable,str(ROOT/'verify.py'),'--outer-only',str(i)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=300);assert p.returncode==0 and '"status": "PASS"' in p.stdout,(i,p.returncode,p.stdout[-2000:]);outer.append(json.loads(p.stdout))
 return {'fresh_process_outer_replays':outer,'direct':verify_direct_full(),'raw_mechanisms':verify_all_raw_mechanisms(),'whole_registry':verify_whole_registry(),'term_domains':verify_all_term_domains()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--quick',action='store_true');ap.add_argument('--full',action='store_true');ap.add_argument('--allow-unsealed',action='store_true');ap.add_argument('--outer-only',type=int);ap.add_argument('--domains-only',action='store_true');ap.add_argument('--whole-only',action='store_true');a=ap.parse_args();t=time.monotonic()
 if a.outer_only is not None:print(json.dumps(verify_outer_fresh(a.outer_only),indent=2,sort_keys=True));return
 if a.domains_only:print(json.dumps(verify_all_term_domains(),indent=2,sort_keys=True));return
 if a.whole_only:print(json.dumps(verify_whole_registry(),indent=2,sort_keys=True));return
 result={'schema':'round80-whole-registry-self-contained-verification-v1','manifest':verify_manifest(a.allow_unsealed),'compression':verify_compression(a.allow_unsealed),'bindings':verify_bindings(a.repo_root.resolve() if a.repo_root else None),'state_and_ledgers':verify_state_and_ledgers(),'processes':verify_processes(),'negative_controls':verify_negative_controls(),'proof_checker_controls':verify_proof_controls()}
 if a.full or not a.quick:result['full']=verify_full()
 result['verdict']='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['branch_closed']=False;result['D_star_Gross_changed']=False;result['fresh_independent_review_required']=True;result['status']='PASS';result['wall_seconds']=time.monotonic()-t;print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
