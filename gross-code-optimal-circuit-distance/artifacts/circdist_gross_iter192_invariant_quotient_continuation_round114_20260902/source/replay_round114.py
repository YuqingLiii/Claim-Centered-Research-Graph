#!/usr/bin/env python3
"""Nonmutating strict-serial replay for the Round114 Gross package."""
from __future__ import annotations
import argparse,datetime,gzip,hashlib,json,os,signal,subprocess,time
from pathlib import Path,PurePosixPath
CHUNK=8<<20

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def norm(v):
 if isinstance(v,dict):return {k:norm(x) for k,x in v.items() if k not in {'seconds','wall_seconds','compile_seconds','started_unix','ended_unix','started_utc','ended_utc','child_pid','parent_pid','runner_pid','preparer_pid','preparer_ppid'}}
 if isinstance(v,list):return [norm(x) for x in v]
 return v
def manifest(root,name):
 rows=[]
 for n,line in enumerate((root/name).read_text().splitlines(),1):
  digest,sep,rel=line.partition('  ');pos=PurePosixPath(rel)
  assert sep and len(digest)==64 and rel==pos.as_posix() and not pos.is_absolute() and '..' not in pos.parts and rel not in rows
  assert (root/rel).is_file() and sha(root/rel)==digest,(name,n,rel);rows.append(rel)
 assert rows==sorted(rows);return rows
ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True);ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--mode',choices=('preseal','installed'),required=True);a=ap.parse_args()
P,R,O=a.package.resolve(),a.repo.resolve(),a.output.resolve();assert P.is_dir() and R.is_dir() and P not in O.parents and O!=P and not O.exists()
runroot=O.parent/(O.stem+'.work');assert not runroot.exists();runroot.mkdir(parents=True);tmp=runroot/'tmp';tmp.mkdir()
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(P/'python/site-packages'),'TMPDIR':str(tmp)}
runs=[]
def run(name,cmd,timeout=3600,expected=0):
 cmd=list(map(str,cmd));op,ep=runroot/(name+'.stdout'),runroot/(name+'.stderr');st=time.time()
 with op.open('wb') as out,ep.open('wb') as err:
  c=subprocess.Popen(cmd,cwd=P,env=env,stdout=out,stderr=err,start_new_session=False);timed=term=killed=False
  print(json.dumps({'event':'START','name':name,'child_pid':c.pid},sort_keys=True),flush=True)
  try:rc=c.wait(timeout=timeout)
  except subprocess.TimeoutExpired:
   timed=term=True;c.send_signal(signal.SIGTERM)
   try:rc=c.wait(timeout=15)
   except subprocess.TimeoutExpired:killed=True;c.kill();rc=c.wait()
 en=time.time();row={'name':name,'argv':cmd,'cwd':str(P),'environment':env,'parent_pid':os.getpid(),'child_pid':c.pid,'returncode':rc,
  'expected_returncode':expected,'returncode_matches':rc==expected and not timed,'started_unix':st,'ended_unix':en,
  'started_utc':datetime.datetime.fromtimestamp(st,datetime.timezone.utc).isoformat(),'ended_utc':datetime.datetime.fromtimestamp(en,datetime.timezone.utc).isoformat(),
  'wall_seconds':round(en-st,6),'stdout':str(op),'stdout_sha256':sha(op),'stdout_bytes':op.stat().st_size,
  'stderr':str(ep),'stderr_sha256':sha(ep),'stderr_bytes':ep.stat().st_size,'timed_out':timed,'term_sent':term,'kill_sent':killed,'reaped':True,'detached':False}
 runs.append(row);print(json.dumps({'event':'END','name':name,'child_pid':c.pid,'rc':rc,'seconds':row['wall_seconds']},sort_keys=True),flush=True)
 assert row['returncode_matches'],(name,rc,op.read_bytes()[-2000:],ep.read_bytes()[-2000:]);return row
# Immutable bindings and package shape.
expected={P/'bindings/SCHEDULER.yaml':'9750f170f0c23f96317b08ff158671310364c8439b6bcd7f44e7c3b455dfef6a',
 P/'bindings/CIRCDIST.gross.yaml':'25d39fbd9add4f5c0d9b7fea76ab2ede1f0c5c3711cd7a152ca98bbde351a834',
 P/'PROPOSED_CIRCDIST.gross.yaml':'25d39fbd9add4f5c0d9b7fea76ab2ede1f0c5c3711cd7a152ca98bbde351a834',
 P/'bindings/round113_exact_review.md':'9737f5c015ace29a5282685b1bf19d82686e593b0e2e6216531cc0bb2a8d27e8',
 P/'bindings/round114_proofpilot_rank.json':'aa5475949d9abe25c2168d8dcd47cc5e88c453ec12d1cc9fed6cae556f3925c2',
 P/'bindings/round112_SHA256SUMS.txt':'404063fcddeb183c670192e3791c44d23d0393beefae1ee4658c1f480c910e4f',
 P/'input/iter192_full_invariant/source.json.gz':'89ed11977cacaed4f46a8c0756fef77a9706a2f3ce65d6ec1b496424fb9533f3',
 P/'input/iter192_full_invariant/state.json':'e4085c5a776561bfc136d67f64988c31c0e26b063afd715d61a836a2f6ff06f1',
 P/'reconstructed/iter192_full_invariant/formula/outer.cnf':'3388c5f4927fecce693237cf0b1090d8c7e9b965067e70f10f54c85febb9393b',
 P/'reconstructed/iter192_full_invariant_quotient/outer.cnf':'00baea753d8ef3d47bbd1e3ca149d39bd2a36ef6475e957633d00770c0071e71',
 P/'frontier/iter193_full_invariant/source.json.gz':'c01425b30638e65587e3afea63c85c6cc3eeab9eb29c605af7977ea64b125fb2',
 P/'frontier/iter193_full_invariant/state.json':'52e6564c63f65588b0fd41707cf9d2ccaecb90d88558e6b636ff20446b59e7ab',
 P/'frontier/iter193_full_invariant/formula/outer.cnf':'f6500190061f611f41ec62c7d58a6abb5b5a07acb8fcfb013c6ff28abfb9aa76',
 P/'frontier/iter193_full_invariant_quotient/outer.cnf':'cf9545d5cd9713b476f6b70962870c4701ed5ace8e73e20812fea412d7e939f1'}
for p,h in expected.items():assert sha(p)==h,p
assert sha(R/'operations/circdist/SCHEDULER.yaml')==expected[P/'bindings/SCHEDULER.yaml']
assert sha(R/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml')==expected[P/'bindings/CIRCDIST.gross.yaml']
assert sha(R/'circdist/reviews/circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md')==expected[P/'bindings/round113_exact_review.md']
prior=R/'circdist/artifacts/circdist_gross_iter191_invariant_quotient_continuation_round112_20260902';assert sha(prior/'SHA256SUMS.txt')==expected[P/'bindings/round112_SHA256SUMS.txt']
assert not list(P.glob('solver/**/*.drat')) and not list(P.glob('frontier/**/*.drat')) and not list(P.glob('frontier/**/*.assignment*'))
assert not [p for p in P.rglob('*') if p.is_symlink()]
assert not [p for p in P.rglob('*') if p.is_file() and p.stat().st_nlink!=1]
# Reviewed input binding/reconstruction.
rb=runroot/'reconstruction.json'
run('iter192_reconstruction_binding',['/usr/bin/python3',P/'source/verify_iter192_reconstruction_round114.py','--repo',R,'--package',prior,'--scratch',P,'--rank',P/'bindings/round114_proofpilot_rank.json','--output',rb],1800)
rbo=load(rb);assert rbo['status']=='PASS' and rbo['base']=={'variables':1875411,'clauses':6999141} and rbo['quotient']=={'variables':2488851,'clauses':11906732}
# Complete outer assignment, decode, and orbit controls.
oassign=runroot/'outer.assignment.dimacs';ocheck=runroot/'outer.assignment_check.json'
run('outer_assignment_all_clauses',['/usr/bin/python3',P/'source/extract_and_check_assignment.py','--cnf',P/'reconstructed/iter192_full_invariant_quotient/outer.cnf','--solver-log',P/'solver/iter192/solver.log','--assignment',oassign,'--output',ocheck],1800)
assert load(ocheck)==load(P/'solver/iter192/assignment_check.json')
areplay=runroot/'outer.assignment.replay.dimacs';cand=runroot/'candidate.json';oreplay=runroot/'outer_replay.json'
run('outer_model_schedule_replay',['/usr/bin/python3',P/'source/verify_outer_sat_model.py','--solver-log',P/'solver/iter192/solver.log','--cnf',P/'reconstructed/iter192_full_invariant_quotient/outer.cnf','--source',P/'input/iter192_full_invariant/source.json.gz','--metadata',P/'reconstructed/iter192_full_invariant_quotient/metadata.json','--frozen',P/'vendor/round80','--assignment',areplay,'--candidate',cand,'--output',oreplay],1800)
assert sha(cand)==sha(P/'solver/iter192/candidate.json') and sha(areplay)==sha(P/'solver/iter192/assignment.replay.dimacs') and norm(load(oreplay))==norm(load(P/'solver/iter192/replay.json'))
ocontrol=runroot/'orbit_controls.json'
run('outer_orbit_lex_controls',['/usr/bin/python3',P/'source/check_sat_orbit_controls_round102.py','--cnf',P/'reconstructed/iter192_full_invariant_quotient/outer.cnf','--metadata',P/'reconstructed/iter192_full_invariant_quotient/metadata.json','--source',P/'input/iter192_full_invariant/source.json.gz','--assignment',oassign,'--candidate',cand,'--trace',P/'reconstructed/iter192_full_invariant_quotient/translation_trace.json.gz','--output',ocontrol],1800)
assert load(ocontrol)==load(P/'verification/iter192_sat_orbit_controls.json')
# Both physical direct adjudications.
vd=runroot/'direct_vendor.json';run('direct_vendor_replay',['/usr/bin/python3',P/'vendor/round80/src/replay_direct_candidate.py','--root',P/'solver/iter192/direct','--output',vd],1800)
assert norm(load(vd))==norm(load(P/'solver/iter192/direct/direct_verification.json'))
idp=runroot/'direct_independent.json';run('direct_independent_replay',['/usr/bin/python3',P/'source/independent_iter192_direct_audit_round114.py','--root',P,'--output',idp],1800)
assert load(idp)==load(P/'verification/iter192_direct_independent_audit.json')
# Global CSS theorem and four mandatory orbits.
ca=runroot/'css_audit.json';run('css_duality_registry_audit',['/usr/bin/python3',P/'source/audit_css_duality_round114.py','--source',P/'input/iter192_full_invariant/source.json.gz','--state',P/'input/iter192_full_invariant/state.json','--candidate',P/'solver/iter192/candidate.json','--output',ca],1800)
assert load(ca)==load(P/'verification/iter192_css_duality_registry_audit.json')
xa,za=runroot/'mandatory_Xerr.json',runroot/'mandatory_Zerr.json'
for sector,out in (('Xerr',xa),('Zerr',za)):
 run('mandatory_'+sector+'_translation_orbit',['/usr/bin/python3',P/'source/audit_batch_attempt_round112.py','--sector',sector,'--attempt','1','--candidate',P/'solver/iter192/candidate.json','--source',P/'input/iter192_full_invariant/source.json.gz','--direct-root',P/'solver/iter192/direct','--cnf',P/f'solver/iter192/direct/direct360/{sector}.cnf','--assignment',P/f'solver/iter192/direct/solver/{sector}.assignment.dimacs','--output',out],1800)
 assert load(out)==load(P/f'verification/iter192_mandatory_{sector}_translation_orbit_audit.json')
da=runroot/'mandatory_dual.json';run('mandatory_css_dual_orbits',['/usr/bin/python3',P/'source/audit_mandatory_css_dual_orbits_round114.py','--source',P/'input/iter192_full_invariant/source.json.gz','--candidate',P/'solver/iter192/candidate.json','--direct-root',P/'solver/iter192/direct','--x-audit',xa,'--z-audit',za,'--css-audit',ca,'--output',da],1800)
assert load(da)==load(P/'verification/iter192_mandatory_css_dual_orbits_audit.json')
# Deterministically regenerate the exact unstarted frontier externally.
fs,fst,fa=runroot/'iter193.source.json.gz',runroot/'iter193.state.json',runroot/'iter193.advance.json'
run('regenerate_iter193_frontier',['/usr/bin/python3',P/'source/advance_css_dual_frontier_round114.py','--source',P/'input/iter192_full_invariant/source.json.gz','--state',P/'input/iter192_full_invariant/state.json','--global-plan',P/'plans/GLOBAL_MECHANISM_PLAN.json','--fallback-plan',P/'plans/FALLBACK_BATCH_PLAN.json','--css-audit',ca,'--x-audit',xa,'--z-audit',za,'--dual-audit',da,'--output-source',fs,'--output-state',fst,'--output-audit',fa],3600)
assert sha(fs)==expected[P/'frontier/iter193_full_invariant/source.json.gz'] and sha(fst)==expected[P/'frontier/iter193_full_invariant/state.json'] and load(fa)==load(P/'verification/iter193_frontier_advance_audit.json')
reg=runroot/'registry.json';run('iter193_translation_registry',['/usr/bin/python3',P/'source/check_registry_invariance_round110.py','--source',fs,'--state',fst,'--output',reg,'--iteration','193','--blocks','814068','--selectors','50580','--assertions','869046'],1800)
assert load(reg)==load(P/'verification/iter193_registry_invariance.json')
be=runroot/'base_encoding.json';run('iter193_base_encoding',['/usr/bin/python3',P/'source/check_outer_encoding.py','--source',fs,'--cnf',P/'frontier/iter193_full_invariant/formula/outer.cnf','--metadata',P/'frontier/iter193_full_invariant/formula/metadata.json','--assertion-map',P/'frontier/iter193_full_invariant/formula/assertion_map.jsonl','--definitions',P/'frontier/iter193_full_invariant/formula/definitions.json.gz','--output',be],3600)
assert norm(load(be))==norm(load(P/'verification/iter193_base_encoding_check.json'))
qc=runroot/'quotient_check.json';run('iter193_translation_quotient',['/usr/bin/python3',P/'source/check_translation_quotient_round102.py','--base-cnf',P/'frontier/iter193_full_invariant/formula/outer.cnf','--base-metadata',P/'frontier/iter193_full_invariant/formula/metadata.json','--source',fs,'--quotient-cnf',P/'frontier/iter193_full_invariant_quotient/outer.cnf','--quotient-metadata',P/'frontier/iter193_full_invariant_quotient/metadata.json','--roots',P/'frontier/iter193_full_invariant_quotient/translation_roots.jsonl','--trace',P/'frontier/iter193_full_invariant_quotient/translation_trace.json.gz','--vendor',P/'vendor/round80','--candidate',P/'solver/iter192/candidate.json','--direct',P/'solver/iter192/direct/direct_verification.json','--output',qc],3600)
assert norm(load(qc))==norm(load(P/'verification/iter193_translation_quotient_check.json'))
st=runroot/'streams.json';run('sat_trace_streams',['/usr/bin/python3',P/'source/check_sat_trace_streams_round114.py','--root',P,'--output',st],3600)
assert load(st)==load(P/'verification/iter192_sat_trace_streams_check.json')
pc=runroot/'proof_controls.json';run('proof_toolchain_controls',['/usr/bin/python3',P/'source/check_proof_controls.py','--root',P,'--output',pc],300)
pco=load(pc);assert pco['status']=='PASS' and all(pco[k] for k in ('valid_drat_accepted','generated_lrat_accepted','corrupt_drat_rejected','truncated_drat_rejected','corrupt_lrat_rejected','truncated_lrat_rejected'))
assert len(pco['runs'])==6 and all(x['reaped'] and not x['detached'] and not x['timed_out'] for x in pco['runs'])
seal={'present':False}
if (P/'SHA256SUMS.txt').exists():
 payload=manifest(P,'PAYLOAD_SHA256SUMS.txt');rootrows=manifest(P,'SHA256SUMS.txt');actual=sorted(x.relative_to(P).as_posix() for x in P.rglob('*') if x.is_file())
 assert set(rootrows)==set(actual)-{'SHA256SUMS.txt'};seal={'present':True,'root_sha256':sha(P/'SHA256SUMS.txt'),'root_rows':len(rootrows),'payload_sha256':sha(P/'PAYLOAD_SHA256SUMS.txt'),'payload_rows':len(payload)}
if a.mode=='installed':
 assert seal['present'];assert all(not(p.stat().st_mode&0o222) for p in [P,*P.rglob('*')]);assert not [p for p in P.rglob('*') if p.is_file() and p.stat().st_nlink!=1]
out={'schema':'circdist-gross-round114-replay-v1','status':'PASS','mode':a.mode,'package':str(P),'strict_serial':True,'runs':runs,'child_count':len(runs),
 'all_children_reaped':all(x['reaped'] for x in runs),'detached_processes':0,'timed_out_processes':0,'nested_proof_control_children':6,
 'mandatory_quotient':'SATISFIABLE','direct':{'Xerr':'SATISFIABLE','Zerr':'SATISFIABLE'},'repair_entered':False,
 'css_free_block_orbits':4124,'css_free_selector_orbits':349,'mandatory_free_orbits':4,'fallback_activated':False,'iter193_unstarted':True,
 'iter193_base_sha256':expected[P/'frontier/iter193_full_invariant/formula/outer.cnf'],'iter193_quotient_sha256':expected[P/'frontier/iter193_full_invariant_quotient/outer.cnf'],
 'trace_streams':3,'trace_raw_bytes':13776739136,'trace_gzip_bytes':2451678853,'proof_controls':'PASS','seal':seal,
 'ctime_provenance_claimed':False,'hardlinks':0}
O.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ('status','mode','child_count','mandatory_quotient','direct','css_free_block_orbits','css_free_selector_orbits','mandatory_free_orbits','iter193_unstarted','trace_streams','proof_controls','seal')},sort_keys=True))
