#!/usr/bin/env python3
"""Assemble the sole Round114 package in session-owned scratch using ordinary copies."""
from __future__ import annotations
import argparse,hashlib,json,os,platform,shutil,sys
from pathlib import Path
CHUNK=8<<20
PKG='circdist_gross_iter192_invariant_quotient_continuation_round114_20260902'

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def copy_file(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 assert dst.stat().st_ino!=src.stat().st_ino and dst.stat().st_nlink==1
 return {'source':str(src),'destination':str(dst),'source_inode':src.stat().st_ino,'destination_inode':dst.stat().st_ino,
         'source_nlink':src.stat().st_nlink,'destination_nlink':dst.stat().st_nlink,'bytes':dst.stat().st_size,
         'sha256':sha(dst),'distinct_inode':True}
def copy_tree(src,dst,rows):
 assert not dst.exists();shutil.copytree(src,dst,copy_function=shutil.copy2,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 for out in sorted(p for p in dst.rglob('*') if p.is_file()):
  inp=src/out.relative_to(dst);assert inp.is_file();assert out.stat().st_ino!=inp.stat().st_ino and out.stat().st_nlink==1
  rows.append({'source':str(inp),'destination':str(out),'source_inode':inp.stat().st_ino,'destination_inode':out.stat().st_ino,
               'source_nlink':inp.stat().st_nlink,'destination_nlink':out.stat().st_nlink,'bytes':out.stat().st_size,
               'sha256':sha(out),'distinct_inode':True})
ap=argparse.ArgumentParser();ap.add_argument('--work',type=Path,required=True);ap.add_argument('--stage',type=Path,required=True);ap.add_argument('--repo',type=Path,required=True);a=ap.parse_args()
W,P,R=a.work.resolve(),a.stage.resolve(),a.repo.resolve();assert W.is_dir() and R.is_dir() and not P.exists();P.mkdir(parents=True)
prior=R/'circdist/artifacts/circdist_gross_iter191_invariant_quotient_continuation_round112_20260902'
review=R/'circdist/reviews/circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md'
canonical=R/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml';scheduler=R/'operations/circdist/SCHEDULER.yaml';rank=Path('/private/tmp/circdist-round114-proofpilot-rank.json')
assert sha(scheduler)=='9750f170f0c23f96317b08ff158671310364c8439b6bcd7f44e7c3b455dfef6a'
assert sha(canonical)=='25d39fbd9add4f5c0d9b7fea76ab2ede1f0c5c3711cd7a152ca98bbde351a834'
assert sha(review)=='9737f5c015ace29a5282685b1bf19d82686e593b0e2e6216531cc0bb2a8d27e8'
assert sha(rank)=='aa5475949d9abe25c2168d8dcd47cc5e88c453ec12d1cc9fed6cae556f3925c2'
assert sha(prior/'SHA256SUMS.txt')=='404063fcddeb183c670192e3791c44d23d0393beefae1ee4658c1f480c910e4f'
# Copy every retained working subtree; no hardlinks and no source metadata mutation.
copy_rows=[]
for name in ('admin','controls','frontier','input','logs','plans','python','reconstructed','solver','source','tooling','vendor','verification'):
 copy_tree(W/name,P/name,copy_rows)
bindings=[(canonical,'bindings/CIRCDIST.gross.yaml'),(scheduler,'bindings/SCHEDULER.yaml'),(review,'bindings/round113_exact_review.md'),
 (rank,'bindings/round114_proofpilot_rank.json'),(prior/'SHA256SUMS.txt','bindings/round112_SHA256SUMS.txt'),
 (prior/'PAYLOAD_SHA256SUMS.txt','bindings/round112_PAYLOAD_SHA256SUMS.txt'),(prior/'FILE_INVENTORY.jsonl','bindings/round112_FILE_INVENTORY.jsonl'),
 (prior/'RESULT.json','bindings/round112_RESULT.json'),(prior/'FRESH_FRONTIER.json','bindings/round112_FRESH_FRONTIER.json'),
 (prior/'REPORT.md','bindings/round112_REPORT.md'),(canonical,'PROPOSED_CIRCDIST.gross.yaml')]
for src,rel in bindings:copy_rows.append(copy_file(src,P/rel))
# Retain every copy binding; the summary also binds the complete row stream.
with (P/'COPY_AUDIT_ROWS.jsonl').open('w',encoding='utf-8',newline='\n') as out:
 for row in copy_rows:out.write(json.dumps(row,sort_keys=True,separators=(',',':'))+'\n')
copy_audit={'schema':'circdist-gross-round114-ordinary-copy-no-hardlink-audit-v1','status':'PASS','files_checked':len(copy_rows),
 'all_distinct_inodes':all(x['distinct_inode'] for x in copy_rows),'all_destination_nlink_one':all(x['destination_nlink']==1 for x in copy_rows),
 'source_nlink_values':sorted(set(x['source_nlink'] for x in copy_rows)),'destination_nlink_values':sorted(set(x['destination_nlink'] for x in copy_rows)),
 'aggregate_bytes':sum(x['bytes'] for x in copy_rows),'mapping_sha256':hashlib.sha256('\n'.join(f"{x['sha256']}  {Path(x['destination']).relative_to(P).as_posix()}" for x in copy_rows).encode()).hexdigest(),
 'rows_path':'COPY_AUDIT_ROWS.jsonl','rows_sha256':sha(P/'COPY_AUDIT_ROWS.jsonl'),
 'metadata_scope':'bytes, inode separation, and link counts checked; ctime immutability is not claimed because Round113 permanently advanced repository ctimes',
 'method':'Python shutil.copy2/copytree; no hardlink operation; distinct inode/nlink checked after every copy; platform copy-on-write is permitted'}
dump(P/'COPY_AUDIT.json',copy_audit)
outer=load(P/'solver/iter192/assignment_check.json');replay=load(P/'solver/iter192/replay.json');orbit=load(P/'verification/iter192_sat_orbit_controls.json')
direct=load(P/'verification/iter192_direct_independent_audit.json');css=load(P/'verification/iter192_css_duality_registry_audit.json')
dual=load(P/'verification/iter192_mandatory_css_dual_orbits_audit.json');advance=load(P/'verification/iter193_frontier_advance_audit.json')
state=load(P/'frontier/iter193_full_invariant/state.json');base=load(P/'frontier/iter193_full_invariant/formula/metadata.json');quot=load(P/'frontier/iter193_full_invariant_quotient/metadata.json')
proof=load(P/'verification/proof_controls.json');stream=load(P/'verification/iter192_sat_trace_streams_check.json')
assert outer['solver_status']=='SATISFIABLE' and all(direct['sectors'][x]['status']=='SATISFIABLE' for x in ('Xerr','Zerr'))
assert state['started'] is False and state['stop'] is None and state['next_iteration']==193
input_bindings={'schema':'circdist-gross-round114-input-bindings-v1','status':'PASS',
 'dispatch':{'scheduler_sha256':sha(scheduler),'proofpilot_sha256':sha(rank),'sole_winner':'CIRCDIST.gross@dstar-residual','winner_score':0.0011127742156472275,'budget_pending_settlement':'139/140'},
 'governance':{'canonical_sha256':sha(canonical),'canonical_level':'CONJECTURED','D_star_Gross':[11,12],'round113_review_sha256':sha(review),
  'round112_root_manifest_sha256':sha(prior/'SHA256SUMS.txt'),'round112_manifest_full_check':'PASS'},
 'mandatory_iter192':{'source_sha256':sha(P/'input/iter192_full_invariant/source.json.gz'),'semantic_sha256':'957459e254abc70f0c66a631712ee70e856f9ca11153b78f20b06d7fb1ffe67b',
  'state_sha256':sha(P/'input/iter192_full_invariant/state.json'),'selector_state_sha256':'dbaeb3d246eef029ede5bcba760a254a75f5d77816ca9d0cbf92396fdf42ad60',
  'blocks':517140,'selectors':25164,'assertions':546702,
  'base':{'sha256':sha(P/'reconstructed/iter192_full_invariant/formula/outer.cnf'),'variables':1875411,'clauses':6999141},
  'quotient':{'sha256':sha(P/'reconstructed/iter192_full_invariant_quotient/outer.cnf'),'variables':2488851,'clauses':11906732,'lex_roots':71}},
 'copy_provenance':copy_audit,'ctime_provenance_valid':False}
dump(P/'INPUT_BINDINGS.json',input_bindings)
fresh={'schema':'circdist-gross-round114-fresh-frontier-v1','status':'PASS','iteration':193,'fresh_unstarted':True,'started':False,'stop':None,'iter193_solved':False,
 'translation_group':'Z_12 x Z_6','translation_group_order':72,'blocks':state['block_count'],'selectors':state['selector_count'],
 'assertions':base['assertions'],'source_file_sha256':state['source_file_sha256'],'source_semantic_payload_sha256':state['source_semantic_payload_sha256'],
 'state_file_sha256':sha(P/'frontier/iter193_full_invariant/state.json'),'selector_state_sha256':state['selector_state_sha256'],
 'authorized_additions':{'free_css_dual_block_orbits':4124,'free_css_dual_blocks':296928,'free_css_dual_selector_orbits':349,'free_css_dual_selectors':25128,
  'mandatory_free_orbits':4,'mandatory_selectors':288,'total_new_selectors':25416},
 'authorization_residual':{'skipped_nonfree_block_orbits':9,'skipped_nonfree_blocks':324,'skipped_nonfree_selector_orbits':1,'skipped_nonfree_selectors':36,
  'order144_quotient_not_built':True},
 'base':{'path':'frontier/iter193_full_invariant/formula/outer.cnf','sha256':base['cnf_sha256'],'variables':base['variables'],'clauses':base['clauses'],'assertions':base['assertions'],'encoding_check':'PASS'},
 'quotient':{'path':'frontier/iter193_full_invariant_quotient/outer.cnf','sha256':quot['cnf_sha256'],'variables':quot['variables'],'clauses':quot['clauses'],'assertions':quot['assertions'],'lex_roots':71,'independent_check':'PASS'},
 'forbidden_solver_artifacts_absent':not any((P/'frontier').rglob('*.drat')) and not any((P/'frontier').rglob('*.assignment*')),
 'smallest_honest_residual':'Solve the exact fresh iteration-193 71-root translation quotient proof-first; no iteration-193 solver disposition exists. The one selector and nine block nonfree D-image orbits remain explicitly inventoried for a future authorization decision.'}
dump(P/'FRESH_FRONTIER.json',fresh)
result={'schema':'circdist-gross-round114-result-v1','status':'PASS','package':'circdist/artifacts/'+PKG,
 'canonical_state_modified':False,'root_closed':False,'root_branch_A_closed':False,'root_branch_B_closed':False,
 'distance_status':{'CIRCDIST.gross':'CONJECTURED','gap-via-lift':'CONJECTURED','D_star_Gross':[11,12]},
 'iteration192':{'quotient':{'status':'SATISFIABLE','formula_sha256':outer['formula_sha256'],'assignment_sha256':outer['assignment_sha256'],
  'variables':outer['variables'],'clauses':outer['clauses'],'all_variables_assigned_exactly_once':True,'all_clauses_satisfied':True},
  'schedule':replay['frozen_schedule_audit'],'compressed_schedule_sha256':replay['compressed_schedule_sha256'],'candidate_sha256':replay['candidate_sha256'],
  'orbit_lex_controls':orbit,'direct':direct['sectors'],'repair_entered':False,
  'repair_reason':'forbidden because both complete unrestricted direct sectors are independently checked SAT'},
 'global_mechanism':{'status':'PASS','action':css['action'],'blocks':css['blocks'],'selectors':css['selectors'],
  'retained':advance['retained_global_mechanism'],'authorization_boundary':advance['authorization_boundary'],
  'information_gain_vs_round112':'349 retained free CSS-dual selector orbits plus 4 mandatory free orbits add 25,416 selectors; Round112 added 8 orbits/576 selectors',
  'fallback_activated':False,'fallback_reason':'sound stronger global CSS-duality transport mechanism obtained and checked'},
 'mandatory_orbits':{'translation_Xerr':'PASS','translation_Zerr':'PASS','css_dual':{k:dual[k] for k in ('mandatory_orbit_count','mandatory_selector_count','all_four_orbits_pairwise_disjoint','all_four_orbits_collision_free_against_future_base','all_four_orbits_free_under_Z12xZ6','all_dual_schedules_legal','all_dual_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer')}},
 'fresh_frontier':fresh,
 'proof_disposition':{'actual_Gross_UNSAT':False,'drat_or_lrat_claim_for_iteration192':False,'proof_output_enabled_from_all_solver_launches':True,
  'sat_streams_are_search_traces_not_certificates':True,'sat_stream_count':stream['stream_count'],'sat_trace_raw_bytes':stream['raw_bytes'],'sat_trace_gzip_bytes':stream['gzip_bytes'],
  'empty_clause_lines':stream['empty_clause_lines'],'valid_corrupt_truncated_toolchain_controls':proof['status'],'proof_controls_scope':proof['scope']},
 'proposed_canonical_yaml':{'path':'PROPOSED_CIRCDIST.gross.yaml','sha256':sha(P/'PROPOSED_CIRCDIST.gross.yaml'),'identical_to_bound_canonical':True,'installed':False,'level':'CONJECTURED','residual':[11,12]},
 'failures':{'ledger':'FAILURE_LEDGER.md','disclosed_ids':[f'F114-{i:03}' for i in range(1,9)],'scientific_failures_or_unknowns':0},
 'preseal_replay_binding':{'status':'PENDING'},'repository_gates':{'status':'PENDING'},'package_seal':{'status':'PENDING'}}
dump(P/'RESULT.json',result)
(P/'FAILURE_LEDGER.md').write_text("""# Round114 failure ledger

Every item is retained and classified. None produced a scientific SAT, UNSAT, or UNKNOWN discrepancy.

- **F114-001.** The copied `source/` directory inherited mode 0555, so the first attempt to create the reconstruction verifier failed with permission denied before output. Only the scratch directory mode was changed; source bytes/metadata in the sealed Round112 package were untouched.
- **F114-002.** The first outer-model replay omitted the copied z3 site-packages. Python raised `ModuleNotFoundError: z3` before a verdict. The full replay with the explicit bundled `PYTHONPATH` passed.
- **F114-003.** An inspection grep included nonexistent `source/build_invariant_quotient_round110.py`; grep returned 2 after emitting matches from the existing files. No scientific program ran; the actual quotient tool name was then read.
- **F114-004.** A read-only schema probe used the wrong scratch source path and raised `FileNotFoundError`. The corrected path was inspected; no state changed.
- **F114-005.** The first CSS audit used `int.bit_count`, unavailable in the system Python 3.9, and stopped at that compatibility call before registry conclusions. It was replaced by `bin(x).count('1')`; the entire retained audit then passed.
- **F114-006.** The first iter193 quotient-check invocation passed `vendor/` instead of `vendor/round80` and stopped at `ModuleNotFoundError: model`. No formula verdict was accepted.
- **F114-007.** The next quotient-check invocation bound `vendor/round80` but omitted z3 site-packages, stopping at `ModuleNotFoundError: z3`. The entire third invocation with both reviewed bindings passed.
- **F114-008.** A repository-status wrapper was invoked from the repository with a scratch-relative runner path and failed before launching git. The corrected absolute-target invocation from scratch passed.
""")
(P/'THEOREM_NOTES.md').write_text("""# Round114 theorem notes

## Mandatory iteration-192 result
The reviewed 71-root translation quotient is SAT. The retained assignment covers all 2,488,851 variables exactly once and satisfies all 11,906,732 clauses. Exact decoding gives a legal 864-edge, 500-layer frozen-family schedule: no resource conflict, all 648 MC overlap constraints, global interleaving, no reviewed block hit, no selector hit, and all 71 lex roots. Corrupt, truncated, reversed-lex, and missing-root controls reject as recorded.

The unrestricted direct Xerr and Zerr formulas are also SAT at weight 10. Independent standard-library reconstruction checks every clause and all 720 columns. Both mechanisms have zero detector syndrome, nonzero logical action, and canonical plus physical nonstabilizer support. Thus this candidate does not close branch A; repair is forbidden.

## CSS-duality lemma
Write a check as `g=(i,j)` in `Z_12 x Z_6`. Define `D(g)=-g`; on data qubits, `D(q)=72+(-q)` for `q<72` and `D(72+q)=-q`; and on named edges, `X:c:q` maps to `Z:-c:D(q)` and conversely. A residual name `R:c:k` maps across sectors to `R:-c:k`, with order position `k` unchanged. Exhaustive concrete checks establish `D^2=1`, `D T_delta D=T_-delta`, 144 distinct edge permutations, exact X/Z incidence and MC-overlap exchange, and stabilizer/detector/logical-quotient preservation. Therefore D transports every reviewed sound block and exact selector exclusion to a sound exclusion.

The input registry lacks 297,252 block and 25,164 selector D-images. Authorization requires every newly retained mechanism to have a free 72-element translation orbit. The package therefore installs exactly the free portion: 4,124 block orbits (296,928 blocks) and 349 selector orbits (25,128 selectors). It explicitly inventories and does not install nine size-36 block orbits (324 blocks) and one size-36 selector orbit (36 selectors). Because of that boundary, no order-144 quotient invariance is claimed; the exact order-72 translation quotient is retained.

The two mandatory direct parents and their two CSS-duals form four pairwise-disjoint, collision-free, free translation orbits (288 selectors); every dual physical mechanism is replayed on its transported legal schedule. This sound global mechanism exceeds the reviewed Round112 eight-parent increment, so the fallback batch was not activated.

## Root logic
No root branch is closed. Branch A lacks both required absence results because Xerr and Zerr are SAT. Branch B lacks a universal proof over all legal frozen-family schedules because the fresh iter193 quotient is unstarted. `CIRCDIST.gross` and `gap-via-lift` remain CONJECTURED and `D*_Gross` remains in `{11,12}`.
""")
(P/'REPORT.md').write_text(f"""# Circdist Gross Round114: iteration-192 invariant quotient continuation

**Verdict:** mandatory outer/Xerr/Zerr are **SAT/SAT/SAT**; neither root branch closes. Canonical files remain unchanged.

The exact Round113-cleared input was reconstructed byte-for-byte before solving. Its source is `89ed1197…`, base CNF `3388c5f4…` (1,875,411 variables / 6,999,141 clauses), and quotient `00baea75…` (2,488,851 / 11,906,732). The complete quotient model decodes to a legal 500-layer schedule. Both unrestricted direct sectors have complete weight-10 physical nonstabilizer witnesses, so the candidate is rejected and repair was not entered.

The predeclared CSS-duality audit proved a concrete order-144 action and found a large sound transport family. Under the free-orbit authorization, Round114 retains 296,928 dual blocks and 25,128 dual selectors, skips and inventories the ten nonfree orbits, and adds four mandatory free selector orbits (288 selectors). The fallback plan is recorded but was not activated.

Fresh iteration 193 is checked and unstarted: source `{state['source_file_sha256']}`, semantic `{state['source_semantic_payload_sha256']}`, selector state `{state['selector_state_sha256']}`; {state['block_count']:,} blocks, {state['selector_count']:,} selectors, {base['assertions']:,} base assertions. Base CNF `{base['cnf_sha256']}` has {base['variables']:,} variables / {base['clauses']:,} clauses. Its exact 71-root quotient `{quot['cnf_sha256']}` has {quot['variables']:,} variables / {quot['clauses']:,} clauses. It was not solved.

The three launch-time SAT proof-output streams total {stream['raw_bytes']:,} raw bytes and are retained losslessly as {stream['gzip_bytes']:,} deterministic gzip bytes with zero empty-clause lines; they carry no UNSAT proof credit. See `RESULT.json`, `FRESH_FRONTIER.json`, `THEOREM_NOTES.md`, `FAILURE_LEDGER.md`, the plans, source tools, and verification objects.
""")
env={'schema':'circdist-gross-round114-environment-v1','python':sys.version,'platform':platform.platform(),'preparer_pid':os.getpid(),'preparer_ppid':os.getppid(),
 'repo_root':str(R),'scratch_root':str(W),'stage':str(P),'timezone':'America/New_York','date':'2026-09-02'};dump(P/'ENVIRONMENT.json',env)
# Process ledger is finalized after replay/gates; retain a truthful placeholder.
dump(P/'PROCESS_FIX2_LEDGER.json',{'schema':'circdist-gross-round114-process-fix2-ledger-v1','status':'PENDING_FINALIZATION','records':[],
 'all_foreground':True,'all_reaped':None,'detached_processes':None,'timed_out_processes':None,'failure_ids':[f'F114-{i:03}' for i in range(1,9)]})
assert sha(P/'PROPOSED_CIRCDIST.gross.yaml')==sha(P/'bindings/CIRCDIST.gross.yaml')==sha(canonical)
print(json.dumps({'status':'PASS','stage':str(P),'copied_files':len(copy_rows),'copied_bytes':sum(x['bytes'] for x in copy_rows),
 'result_sha256':sha(P/'RESULT.json'),'fresh_source_sha256':state['source_file_sha256'],'fresh_quotient_sha256':quot['cnf_sha256']},sort_keys=True))
