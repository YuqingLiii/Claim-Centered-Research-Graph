#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,collections,gzip,hashlib,itertools,json,os,shutil,struct,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import model as M
import round68_build as B
import round68_verify as V
from outer import OuterScheduler
ALL720=(1<<720)-1
PERMS=list(itertools.permutations(range(6)))

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_obj(o): return sha_bytes(json.dumps(o,sort_keys=True,separators=(',',':')).encode())
def read_gz(rel):
 with gzip.open(ROOT/rel,'rb') as f:return f.read()
def load_gz(rel):return json.loads(read_gz(rel))
def load_json(rel):return json.loads((ROOT/rel).read_text())
def mask(qs):return M.mask(qs)
def bits(z):
 while z:
  b=z&-z;yield b.bit_length()-1;z^=b
def parity(v,duals):return [M.popcount(v&z)&1 for z in duals]
def syndrome(v,rows):return sum(((M.popcount(v&h)&1)<<i) for i,h in enumerate(rows))
def atom_holds(atom,pos):
 a,op,b=atom;assert op=='<';return pos[int(a.split(':')[2])]<pos[int(b.split(':')[2])]
def fail(msg):raise AssertionError(msg)

def verify_manifest():
 p=ROOT/'SHA256SUMS.txt'
 if not p.exists():return {'present':False}
 rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=ROOT/rel
  assert q.is_file() and sha_bytes(q.read_bytes())==h,(rel,'hash mismatch');rows.append(rel)
 expected=sorted(q.relative_to(ROOT).as_posix() for q in ROOT.rglob('*') if q.is_file() and q.relative_to(ROOT).as_posix()!='SHA256SUMS.txt')
 assert sorted(rows)==expected,(len(rows),len(expected),'manifest coverage mismatch')
 return {'present':True,'entries':len(rows)}

def verify_compression():
 inv=load_json('COMPRESSED_INVENTORY.json');total=0
 for r in inv['files']:
  p=ROOT/r['path'];raw=p.read_bytes();assert len(raw)==r['compressed_bytes'] and sha_bytes(raw)==r['compressed_sha256']
  data=read_gz(r['path']);assert len(data)==r['uncompressed_bytes'] and sha_bytes(data)==r['uncompressed_sha256'];total+=len(data)
 return {'files':len(inv['files']),'uncompressed_bytes':total}

def verify_source_bindings(repo):
 d=load_json('SOURCE_BINDINGS.json');checked=0
 if repo is not None:
  for b in d['bindings']:
   p=repo/b['path'];assert p.exists(),b['path']
   if b['kind']=='file':
    z=p.read_bytes();assert len(z)==b['bytes'] and sha_bytes(z)==b['sha256'],b['path'];checked+=1
   else:
    rows=[]
    for q in sorted(x for x in p.rglob('*') if x.is_file()):
     z=q.read_bytes();rows.append({'path':q.relative_to(p).as_posix(),'bytes':len(z),'sha256':sha_bytes(z)})
    assert rows==b['files'],b['path'];assert len(rows)==b['file_count'] and sum(x['bytes'] for x in rows)==b['bytes']
    assert sha_obj(rows)==b['tree_sha256'],b['path'];checked+=len(rows)
 for src,dst in d['offline_snapshots'].items():
  want=next(x['sha256'] for x in d['bindings'] if x['path']==src and x['kind']=='file')
  assert sha_bytes((ROOT/dst).read_bytes())==want
 return {'binding_records':len(d['bindings']),'live_files_checked':checked,'offline_snapshots':len(d['offline_snapshots']),'repo_checked':repo is not None}

def verify_preflight():
 expected={'preflight_round62.run.json':0,'preflight_round63_full_static.run.json':0,'preflight_round68_sealed.run.json':0,'preflight_round68_full.run.json':1}
 out={}
 for n,code in expected.items():
  d=load_json('preflight/'+n);assert d['exit_code']==code and not d['timed_out'];out[n]=code
 assert 'live source binding mismatch' in (ROOT/'preflight/preflight_round68_full.log').read_text()
 assert "CIRCDIST.gross.yaml" in (ROOT/'preflight/preflight_round68_full.log').read_text()
 assert "SCHEDULER.yaml" in (ROOT/'preflight/preflight_round68_full.log').read_text()
 for n in ('preflight_round62.log','preflight_round63_full_static.log','preflight_round68_sealed.log'):
  txt=(ROOT/'preflight'/n).read_text();assert 'PASS' in txt
 a=load_json('preflight/inherited_all_file_read_audit.json');assert len(a['packages'])==3
 assert [(x['file_count'],x['bytes']) for x in a['packages']]==[(27,733974),(25,678695),(102,34305998)]
 return {'run_exit_codes':out,'all_inherited_files_read':sum(x['file_count'] for x in a['packages'])}

def verify_classification():
 px,pz,lx,lz=B.load_context()
 catobj=load_gz('classification/local_order_catalog.json.gz');pobj=load_gz('classification/pair_classification.json.gz')
 wx=load_json('classification/Xerr_w14_individual.json');wz=load_json('classification/Zerr_w14_individual.json');w14={'Xerr':wx,'Zerr':wz}
 assert (wx['candidate_R_count'],wx['positive_R_count'],wx['negative_R_count'],wx['all_queries_decided'])==(1800,15,1785,True)
 assert (wz['candidate_R_count'],wz['positive_R_count'],wz['negative_R_count'],wz['all_queries_decided'])==(925,6,919,True)
 cats={};catalog_cases=unary_replays=0
 for e in catobj['entries']:
  lab,a=e['sector'],e['check'];rows=M.Xchecks if lab=='Xerr' else M.Zchecks;pool=px if lab=='Xerr' else pz;duals=lz if lab=='Xerr' else lx;det=M.HZ if lab=='Xerr' else M.HX;stabs=M.HX if lab=='Xerr' else M.HZ;row=rows[a]
  assert e['row']==row and len(e['orders'])==720
  seen=set();records=[];uc=gc=0
  for rec,pidx in zip(e['orders'],PERMS):
   order=tuple(rec['qubits']);assert order==tuple(row[i] for i in pidx) and order not in seen;seen.add(order);pos={q:i for i,q in enumerate(order)};opts=[]
   for k,(rp,pp) in enumerate(zip(M.RES_POS,M.PHYS_POS)):
    s=mask(order[i] for i in rp);phys=mask(order[i] for i in pp);z=rec['options'][k]
    assert z['kind']==k and z['canonical_support']==M.bits(s) and z['physical_support']==M.bits(phys)
    assert z['opposite_syndrome']==M.bits(syndrome(s,det)) and z['logical_quotient']==parity(s,duals)
    assert syndrome(s,det)==syndrome(phys,det) and parity(s,duals)==parity(phys,duals);opts.append((k,s,phys))
   sm=opts[1][1];logical=next((q for q in pool if q&sm==sm),None);isbad=logical is not None;assert rec['unary_bad']==isbad
   if isbad:
    w=rec['unary_witness'];assert mask(w['logical_support'])==logical and w['selected_residual']==f'R:{a}:1';D=mask(int(x.split(':')[1]) for x in w['singleton_columns']);assert sm^D==logical and w['fault_weight']==10
    assert syndrome(logical,det)==0 and not M.inspan(logical,stabs) and any(parity(logical,duals));uc+=1;unary_replays+=1
   else:gc+=1
   records.append({'order':order,'pos':pos,'opts':opts,'bad':isbad})
  assert (uc,gc)==(360,360)==(e['unary_bad_order_count'],e['unary_good_order_count']);cats[(lab,a)]=records;catalog_cases+=720
 pair_cases=configs_n=physical_n=terms_n=controls_n=cells_n=tuple_witnesses=0;source_hist=collections.Counter();atom_hist=collections.Counter();selector=hashlib.sha256()
 for pe in pobj['pairs']:
  lab,a,b=pe['sector'],pe['a'],pe['b'];A=cats[(lab,a)];BB=cats[(lab,b)];duals=lz if lab=='Xerr' else lx;det=M.HZ if lab=='Xerr' else M.HX;stabs=M.HX if lab=='Xerr' else M.HZ;rows=M.Xchecks if lab=='Xerr' else M.Zchecks;pool=px if lab=='Xerr' else pz
  cmap={}
  for ci,c in enumerate(pe['positive_residual_configurations']):
   s1=mask(c['a_support']);s2=mask(c['b_support']);logical=mask(c['logical_support']);D=mask(int(x.split(':')[1]) for x in c['singleton_columns']);key=(c['a_kind'],s1,c['b_kind'],s2);assert key not in cmap;cmap[key]=(ci,c)
   assert s1^s2^D==logical and c['fault_weight']==2+M.popcount(D)<=10 and M.popcount(logical)==c['logical_weight'] in (12,14)
   assert syndrome(logical,det)==0 and not M.inspan(logical,stabs) and c['logical_parities']==parity(logical,duals) and any(c['logical_parities'])
   p1=(mask(rows[a])^s1) if c['a_kind']==0 else s1;p2=(mask(rows[b])^s2) if c['b_kind']==0 else s2;physical=p1^p2^D
   assert syndrome(physical,det)==0 and not M.inspan(physical,stabs) and parity(physical,duals)==parity(logical,duals)
   if c['source']=='weight12_pool':assert logical in pool
   else:
    assert c['source']=='weight14_direct';wr=w14[lab]['weight14_completions'][str(s1^s2)];assert mask(wr['support'])==logical
   source_hist[c['source']]+=1;configs_n+=1;physical_n+=1
  assert len(cmap)==pe['positive_config_count']
  truth=[];new=[]
  for ia,ra in enumerate(A):
   rowmask=newmask=0
   for ib,rb in enumerate(BB):
    ok=ra['bad'] or rb['bad'];wi=None
    if not ok:
     for k1,s1,_ in ra['opts']:
      for k2,s2,_ in rb['opts']:
       got=cmap.get((k1,s1,k2,s2))
       if got is not None:wi=got[0];ok=True;break
      if ok:break
    if ok:rowmask|=1<<ib
    if wi is not None:
     newmask|=1<<ib;tuple_witnesses+=1;selector.update(struct.pack('<HHH',ia,ib,wi))
   truth.append(rowmask);new.append(newmask)
  assert [hex(z) for z in truth]==pe['truth_rows_hex'] and [hex(z) for z in new]==pe['new_good_good_rows_hex']
  assert sum(M.popcount(z) for z in truth)==pe['full_bad_order_pairs'];witnessed=sum(M.popcount(z) for z in new);assert witnessed==pe['new_good_good_bad_order_pairs'];cells_n+=witnessed;pair_cases+=720*720
  union=[0]*720
  for t in pe['deletion_minimal_terms']:
   atoms=[tuple(x) for x in t['atoms']];am=bm=ALL720
   for i,r in enumerate(A):
    if not all(atom_holds(x,r['pos']) for x in atoms if x[0].startswith((f'X:{a}:',f'Z:{a}:'))):am&=~(1<<i)
   for i,r in enumerate(BB):
    if not all(atom_holds(x,r['pos']) for x in atoms if x[0].startswith((f'X:{b}:',f'Z:{b}:'))):bm&=~(1<<i)
   for i in bits(am):assert bm & (ALL720^truth[i])==0
   for i in bits(am):
    if not A[i]['bad']:union[i]|=bm & sum((1<<j) for j,r in enumerate(BB) if not r['bad'])
   assert t['atom_count']==len(atoms) and len(t['deletion_controls'])==len(atoms);terms_n+=1;atom_hist[len(atoms)]+=1
   for ctrl in t['deletion_controls']:
    rem=tuple(ctrl['removed_atom']);trial=list(atoms);trial.remove(rem);ia=ctrl['exposed_a_order_id'];ib=ctrl['exposed_b_order_id'];assert ctrl['exposed_a_order']==list(A[ia]['order']) and ctrl['exposed_b_order']==list(BB[ib]['order'])
    for x in trial:assert atom_holds(x,A[ia]['pos'] if x[0].startswith((f'X:{a}:',f'Z:{a}:')) else BB[ib]['pos'])
    assert ((truth[ia]>>ib)&1)==0;controls_n+=1
  assert union==new and len(pe['deletion_minimal_terms'])==pe['term_count']
 assert (len(cats),catalog_cases,unary_replays,len(pobj['pairs']),pair_cases,configs_n,physical_n,cells_n,tuple_witnesses,terms_n,controls_n)==(23,16560,8280,30,15552000,3368,3368,1197120,1197120,4740,40180)
 assert source_hist=={'weight12_pool':3347,'weight14_direct':21};assert atom_hist=={4:8,6:52,7:1088,8:1416,9:1092,10:920,11:104,12:60}
 return {'catalog_entries':23,'local_orders':16560,'pair_relations':30,'pair_order_cases':pair_cases,'positive_configurations':configs_n,'physical_replays':physical_n,'explicit_tuple_witnesses':tuple_witnesses,'tuple_selector_sha256':selector.hexdigest(),'sound_terms':terms_n,'term_atom_histogram':dict(atom_hist),'library_relative_deletion_controls':controls_n,'negative_w14_solver_observations_non_load_bearing':2704,'negative_absence_proofs':0}

def ungzip_to(rel,dst):dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(read_gz(rel))
def verify_outer_smt_only(i):
 px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz
 r62=load_json('src/round62_cegar20.json');pair=load_gz('classification/pair_classification.json.gz');general=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{j}",[tuple(x) for x in t['atoms']]) for p in pair['pairs'] for j,t in enumerate(p['deletion_minimal_terms'])];dyn=load_json('cegar/dynamic_blocks.json')
 outer=OuterScheduler(True)
 for j,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 for tag,atoms in general:outer.add_block(atoms,tag)
 for j,b in enumerate(dyn[:2*i]):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b['mechanism_sha256'])
 smt=outer.s.to_smt2().encode();cand=load_gz(f'cegar/iter{i}/candidate.json.gz');assert smt==read_gz(f'cegar/iter{i}/outer.smt2.gz') and sha_bytes(smt)==cand['outer_smt2_sha256']
 print(json.dumps({'status':'PASS','outer_iteration':i,'blocks':len(outer.blocks),'smt2_sha256':sha_bytes(smt)},sort_keys=True))

def verify_cegar():
 px,pz,lx,lz=B.load_context();rx,sx=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,sz=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz;assert len(records)==1440
 r62=load_json('src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz);pair=load_gz('classification/pair_classification.json.gz');general=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{j}",[tuple(x) for x in t['atoms']]) for p in pair['pairs'] for j,t in enumerate(p['deletion_minimal_terms'])];assert len(general)==4740
 dyn=load_json('cegar/dynamic_blocks.json');summary=load_json('cegar/summary.json');assert len(dyn)==12 and summary['completed_iterations']==6
 out=[]
 with tempfile.TemporaryDirectory(prefix='circdist_round69_verify_') as td:
  tmp=Path(td)
  for i in range(6):
   base=f'cegar/iter{i}';cand=load_gz(base+'/candidate.json.gz');ores=load_gz(base+'/outer_result.json.gz');saved=load_gz(base+'/direct_verification.json.gz');times={k:int(v) for k,v in cand['schedule_times'].items()};assert sha_obj(times)==cand['schedule_sha256'];assert M.audit_schedule(times,True)==cand['audit'];assert ores['status']=='SAT' and ores['compressed_schedule']==times
   outer=OuterScheduler(True)
   for j,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
   for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
   for tag,atoms in general:outer.add_block(atoms,tag)
   for j,b in enumerate(dyn[:2*i]):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b['mechanism_sha256'])
   smt_saved=read_gz(base+'/outer.smt2.gz');assert sha_bytes(smt_saved)==cand['outer_smt2_sha256'];assert len(outer.blocks)==6200+2*i
   child=subprocess.run([sys.executable,str(ROOT/'verify.py'),'--outer-only',str(i)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=120);assert child.returncode==0 and '"status": "PASS"' in child.stdout,(i,child.stdout[-2000:])
   assert cand['asserted_blocks']=={'round63_single':1440,'round62':20,'round69_generalized':4740,'round69_dynamic':2*i,'total':6200+2*i,'exploratory_round63_pair':0}
   for _,atoms in general:assert not M.block_holds(times,atoms)
   for b in dyn[:2*i]:assert not M.block_holds(times,[tuple(x) for x in b['atoms']])
   assert all(not M.block_holds(times,[tuple(x) for x in r['atoms']]) for r in records)
   assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in r62['outer_blocks'])
   assert cand['order_bindings']=={'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)}
   assert cand['model_metadata']==json.loads(json.dumps(M.model_metadata(px,pz,lx,lz)));assert cand['pool_bindings']['Xerr_pool_count']==cand['pool_bindings']['Zerr_pool_count']==1884
   ss=B.sectors(times,lx,lz);assert cand['columns']=={lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()}
   vr={'schema':'round69-complete-direct360-replay-v1','candidate_sha256':cand['schedule_sha256'],'schedule_audit':M.audit_schedule(times,True),'sectors':{}}
   vrroot=tmp/f'iter{i}';(vrroot/'direct360').mkdir(parents=True);(vrroot/'solver').mkdir()
   for lab in ('Xerr','Zerr'):
    gen=tmp/f'generated-{i}'/lab;B.build_direct_cnf(ss[lab],gen,cand['schedule_sha256'],10)
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):
     rel=base+f'/direct360/{lab}.{suffix}.gz';data=read_gz(rel);assert data==(gen.with_suffix('.'+suffix)).read_bytes(),(i,lab,suffix);(vrroot/'direct360'/f'{lab}.{suffix}').write_bytes(data)
    ungzip_to(base+f'/solver/{lab}.solver.log.gz',vrroot/'solver'/f'{lab}.solver.log');run=json.loads(read_gz(base+f'/solver/{lab}.run.json.gz'));assert run['exit_code']==10 and not run['timed_out']
    vr['sectors'][lab]=json.loads(json.dumps(V.verify_one(vrroot,lab,ss[lab])));assert vr['sectors'][lab]==saved['sectors'][lab]
    entry=dyn[2*i+(0 if lab=='Xerr' else 1)];mech=vr['sectors'][lab]['mechanism'];block=mech['sound_outer_block'];assert entry['source_iteration']==i and entry['sector']==lab and entry['candidate_sha256']==cand['schedule_sha256'] and entry['mechanism_sha256']==sha_obj(mech) and entry['atoms']==block['atoms'] and entry['atom_count']==block['atom_count']
   assert saved['repair_gate']['entered'] is False
   out.append({'iteration':i,'outer':'SAT','Xerr':'SAT/raw-replay','Zerr':'SAT/raw-replay','installed_blocks':6200+2*i,'candidate_sha256':cand['schedule_sha256']})
 return {'iterations':out,'new_raw_replayed_blocks':12,'outer_unsat':False,'direct_unsat_candidates':0,'absence_proofs':0,'repair_entered':False,'next_iteration':6}

def run_checked(cmd,want,marker,timeout=70):
 try:r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout)
 except subprocess.TimeoutExpired:fail('checker control timed out')
 assert r.returncode==want and marker in r.stdout,(cmd,r.returncode,r.stdout[-1000:]);return {'exit_code':r.returncode,'marker':marker}
def verify_checker_controls():
 c=ROOT/'controls/proof_checker';tool=ROOT/'tooling'
 with tempfile.TemporaryDirectory(prefix='circdist_round69_checker_') as td:
  lrat=Path(td)/'valid.lrat'
  rows={}
  rows['drat_valid']=run_checked([str(tool/'drat-trim-arm64-macos'),str(c/'php6_5.cnf'),str(c/'php6_5.drat'),'-t','60','-L',str(lrat)],0,'VERIFIED')
  rows['drat_corrupt']=run_checked([str(tool/'drat-trim-arm64-macos'),str(c/'php6_5.cnf'),str(c/'php6_5_corrupted_truncated_10_lines.drat'),'-t','60'],1,'NOT VERIFIED')
  rows['lrat_valid']=run_checked([str(tool/'lrat-check-arm64-macos'),str(c/'php6_5.cnf'),str(lrat)],0,'VERIFIED')
  rows['lrat_corrupt']=run_checked([str(tool/'lrat-check-arm64-macos'),str(c/'php6_5.cnf'),str(c/'php6_5_corrupted_truncated_10_lines.lrat')],1,'NOT VERIFIED')
 return rows

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--outer-only',type=int);ap.add_argument('--quick',action='store_true',help='skip 15.5M-cell classification and six complete CEGAR reconstructions');a=ap.parse_args();t=time.monotonic()
 if a.outer_only is not None:verify_outer_smt_only(a.outer_only);return
 result={'schema':'round69-independent-package-verification-v1','manifest':verify_manifest(),'compression':verify_compression(),'bindings':verify_source_bindings(a.repo_root.resolve() if a.repo_root else None),'preflight':verify_preflight(),'checker_controls':verify_checker_controls()}
 if not a.quick:
  result['classification']=verify_classification();result['cegar']=verify_cegar()
 result['verdict']=(ROOT/'VERDICT.txt').read_text().strip() if (ROOT/'VERDICT.txt').exists() else 'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';assert result['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['status']='PASS';result['wall_seconds']=time.monotonic()-t
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
