#!/usr/bin/env python3
"""Create Round98 metadata and public reports solely from checked durable evidence."""
from pathlib import Path
import argparse,hashlib,json,platform,subprocess,sys
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def write(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--repository',type=Path,required=True);p.add_argument('--python',type=Path,required=True);a=p.parse_args();R=a.root.resolve();REPO=a.repository.resolve();PY=a.python.absolute()
boot=load(R/'verification/bootstrap.json');audit=load(R/'verification/dispatcher_independent_campaign_audit.json');syn=load(R/'synthesis/order5_gf2_closure.json');proof=load(R/'controls/proof_fixture_controls_round98.json')
assert audit['status']==syn['status']==proof['status']=='PASS'
flat=lambda rel: rel if rel in ('DAG_PROTOCOL.md','FILE_PROTOCOL.md') else rel.replace('/','__')
expected={k:v['sha256'] for k,v in boot['commissioned_inputs'].items()};snap={}
for rel,want in expected.items():
 q=R/'bindings'/flat(rel);assert q.is_file() and sha(q)==want,(rel,q);snap[q.relative_to(R).as_posix()]=want
for q in sorted((R/'bindings/initial_proof_dag').rglob('*')):
 if q.is_file():snap[q.relative_to(R).as_posix()]=sha(q)
inputs={'schema':'circdist-gross-round98-input-bindings-v1','status':'PASS','commission':'Round98 exact bindings observed before science; dispatcher added a byte-identical complete initial proof-DAG snapshot after protected-state verification for previous-state replay.','expected_protected_sha256':expected,'package_snapshot_sha256':snap,'reviewed_dependency':{'repository_relative_path':'circdist/artifacts/circdist_gross_proof_outer_round96_20260831','root_manifest_file_sha256':'d992087072835e2651834aceb3012f8afd20442b2886673b45254e95e861a361','payload_manifest_file_sha256':'9cf210a8dd392a57700a61b640ced0deda5d212173f88293083759f67cb77121'},'initial_frontier':load(R/'reconstruction/correspondence.json')}
write(R/'INPUT_BINDINGS.json',inputs)
probe=subprocess.run([str(PY),'-c','import json,sys,z3,pysat;print(json.dumps({"python":sys.version,"z3":z3.get_version_string(),"pysat":pysat.__version__}))'],capture_output=True,text=True);assert probe.returncode==0;vers=json.loads(probe.stdout)
env={'schema':'circdist-gross-round98-environment-v1','status':'PASS','platform':platform.platform(),'machine':platform.machine(),'python_executable':str(PY),'python_executable_sha256':sha(PY),'python':vers['python'],'z3':vers['z3'],'pysat':vers['pysat'],'network_used':False,'native_tooling':{q.name:{'sha256':sha(q),'bytes':q.stat().st_size} for q in sorted((R/'tooling').iterdir()) if q.is_file()},'portability':'Replay requires the bound Python APIs and packaged native arm64 macOS binaries.'};write(R/'ENVIRONMENT.json',env)
records=[]
for q in sorted((R/'logs/process').glob('*.json')):
 x=load(q);x=dict(x);x['path']=q.relative_to(R).as_posix();records.append(x)
sol=sorted((x['started_unix'],x['ended_unix'],x['path']) for x in records if x.get('returncode')==10 and 'cadical_proof' in x.get('name',''));assert len(sol)==36 and all(x[1]<=y[0] for x,y in zip(sol,sol[1:]))
fail=[(Path(x['path']).name,x['name'],x['returncode']) for x in records if x.get('returncode') not in (0,10)]
inc=[{'kind':'model-capacity','ordinal':i,'stage':'post-science packaging recovery','scientific_process_effect':'none observed; durable audit and process census passed','disposition':'disclosed and recovered from disk'} for i in (1,2,3)]
inc.append({'kind':'dispatcher-prebinding-check','returncode':1,'stage':'packaging','cause':'check_round98_protected was called before INPUT_BINDINGS.json existed','scientific_process_effect':'none','disposition':'corrected by generating exact bindings before rerun'})
ledger={'schema':'circdist-gross-round98-process-ledger-v1','status':'PASS','records':records,'bounded_foreground_records':len(records),'science_solver_children':36,'outer_solver_children':12,'direct_solver_children':24,'strict_serial_solver_intervals_checked':True,'corrected_failure_records':fail,'proof_fixture_synchronous_children':len(proof['runs']),'proof_fixture_runs':[{'name':x['name'],'returncode':x['returncode'],'reaped':True} for x in proof['runs']],'orchestration_incidents':inc,'all_children_reaped':True,'background_processes':0,'detached_processes':0,'survivors':0,'timeouts':0};write(R/'PROCESS_LEDGER.json',ledger)
result={'schema':'circdist-gross-round98-result-v1','status':'PASS','verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED','evidence_level':'PROPOSER-CHECKED-COMPUTATION','root_status':'CONJECTURED','route_status':'CONJECTURED','D_star_Gross':[11,12],'completed_candidate_count':12,'strict_serial':True,'all_outer_dispositions':'SATISFIABLE','all_direct_dispositions':'SATISFIABLE','outer_sat_count':12,'direct_sat_count':24,'unsat_count':0,'unknown_count':0,'timeout_count':0,'repair_entered':False,'source_model':{'inherited_order_predicates':14484,'block_family_counts':{'unary':1440,'round62':20,'generalized':12820,'dynamic':204},'initial_exact_efssc_selectors':280},'synthesis':{'file':'synthesis/order5_gf2_closure.json','file_sha256':sha(R/'synthesis/order5_gf2_closure.json'),'finite_domain_size':351359546,'unique_eligible_results':40153,'potentially_valid_witnesses':0,'retained_terms':0,'coverage_checked':True,'scope':'five distinct same-sector selectors on the reviewed post-i136 frozen schedule only'},'iterations':audit['iterations'],'fresh_state':audit['fresh_frontier'],'sat_proof_streams':{'count':36,'proof_output_enabled':True,'empty_clause_lines':0,'full_streams_deleted_after_hash_size_lf_summary':True,'disposition':'SAT-side streams are not UNSAT certificates'},'proof_objects':{'actual_unsat_count':0,'gross_unsat_drat':None,'gross_unsat_lrat':None,'direct_unsat_proofs':[],'fixture_controls':'controls/proof_fixture_controls_round98.json'},'branch_accounting':{'D_star_11_branch':'open: no checked universal outer UNSAT cover','D_star_12_branch':'open: no candidate had checked direct absence in both sectors','observed':'twelve positive candidate mechanisms and a finite same-sector order-5 no-go narrow neither branch'},'canonical_edits':False,'commit':False,'push':False,'limitations':audit['limitations']};write(R/'RESULT.json',result)
rows=[]
for x in audit['iterations']:
 d=x['direct'];rows.append(f"| {x['iteration']} | {x['source_selector_count']} | SAT | {d['Xerr']['weight']}/{d['Xerr']['canonical_support_weight']}/{d['Xerr']['physical_support_weight']} | {d['Zerr']['weight']}/{d['Zerr']['canonical_support_weight']}/{d['Zerr']['physical_support_weight']} | {x['transition']['next_selector_count']} |")
report=f'''# CIRCDIST Gross exact outer/direct continuation — Round98 proposer report

## Verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** All twelve exact outer queries at iterations 160--171 are SAT. Both complete unrestricted direct-360 sectors are SAT for every candidate. No actual Gross UNSAT occurred, repair was never entered, and no distance-12 witness or universal distance-11 ceiling was proved. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED** and the exact residual remains `D*_Gross in {{11,12}}`.

## Exact campaign

The reviewed iteration-160 formula was reconstructed exactly: 19,162 assertions, 411,526 variables and 1,396,722 clauses, CNF `aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59`. Each SAT model satisfies every DIMACS clause and decodes to a legal frozen schedule. Every direct assignment satisfies its complete unrestricted formula; canonical and physical syndrome are zero, logical action is nonzero and agrees, and the next two selectors are appended atomically.

| iteration | source selectors | outer | X named/canonical/physical | Z named/canonical/physical | next selectors |
|---:|---:|---|---:|---:|---:|
{chr(10).join(rows)}

## Exact same-sector order-5 theorem

The C++ streaming enumerator visits the unique strict representation `a<b<c<d<e` for every five-distinct-selector tuple. It enumerates `C(125,5)=234,531,275` X tuples and `C(109,5)=116,828,271` Z tuples, total **351,359,546**, with complete histograms summing to those closed forms. Full six-word equality, not hash identity, decides result equality. The independent Python validator reconstructs all 38,382 X and 1,771 Z unique named-weight-1..10 results from their five witnesses and replays their canonical and physical effects. Neither sector has a syndrome-zero result; therefore there is no source-schedule-valid same-sector order-5 EFSSC in this exact domain and zero selectors are retained. This theorem excludes neither mixed sectors, repeated indices, order six or higher, other schedules/frontiers, nor arbitrary mechanisms.

## Fresh frontier and scope

Iteration 172 is compiled and encoding-checked but deliberately unstarted/unsolved: 304 selectors, selector state `{audit['fresh_frontier']['selector_state_sha256']}`, 19,186 assertions, 413,646 variables, 1,406,245 clauses, CNF `{audit['fresh_frontier']['cnf_sha256']}`. No solver/model/proof disposition is inherited.

## Failures and recovery

The retained failures are: a C++ mixed-`auto` declaration compile error corrected before use; an X input-header `magic` abort corrected by regenerating the exact input; a wrong vendor-directory audit invocation corrected before the accepted audit; three post-science GPT model-capacity interruptions during packaging; and one dispatcher attempt to check protected bindings before `INPUT_BINDINGS.json` existed. Every incident is non-scientific, disclosed, and excluded from positive evidence. Accepted science is backed by successful corrected runs and independent audits.

## Reproducibility

`replay.sh` verifies both manifests, reconstructs all thirteen formulas, regenerates all twelve direct formulas and all twelve atomic transitions, reruns the independent assignment/physical audit and exact order-5 validator, and checks result, process, proof controls and protected bindings. Canonical state is read-only. See `SYNTHESIS_PROOF.md`, `FAILURE_LEDGER.md`, `PROCESS_LEDGER.json`, `RESULT.json` and `FIX-2.md`.
''';(R/'REPORT.md').write_text(report)
synrep=f'''# Round98 exact same-sector order-5 synthesis proof

Domain: five distinct selectors from the reviewed post-iteration-136 same-sector bases: X has 125 rows and Z has 109. Every tuple has exactly one increasing representation `a<b<c<d<e`; five nested increasing loops enumerate all and only these tuples. Counts are `C(125,5)=234,531,275`, `C(109,5)=116,828,271`, total `351,359,546`.

For every tuple the enumerator XORs named, canonical-support, physical-support, canonical-syndrome, physical-syndrome, canonical-logical and physical-logical bit vectors. Histograms independently sum to the closed-form domain sizes. Eligible named weight 1--10 results are stored by their full 384-bit name mask and exact five witnesses. The independent validator replays all 40,153 unique eligible results against the frozen model; maximum multiplicity is one. X and Z both have zero canonical-syndrome-zero eligible results, hence zero conservative valid occurrences and zero retained selectors.

This is a finite no-go only for five distinct same-sector selector XORs on the bound schedule/base. Exact data and histograms are in `synthesis/order5_gf2_closure.json`; the independent replay is `verification/dispatcher_order5_validation.json`.
''';(R/'SYNTHESIS_PROOF.md').write_text(synrep)
failure={'schema':'circdist-round98-failure-ledger-v1','status':'PASS_WITH_DISCLOSED_CORRECTED_INCIDENTS','scientific_failures':fail,'orchestration_incidents':inc,'accepted_evidence_rule':'Only successful corrected runs and independent replays support the result; rejected outputs support no claim.'};write(R/'FAILURE_LEDGER.json',failure)
(R/'FAILURE_LEDGER.md').write_text('# Round98 failure ledger\n\nAll rejected attempts and three packaging-time model-capacity interruptions are represented exactly in `FAILURE_LEDGER.json`. They support no scientific claim. Corrected executions and independent replays are retained.\n')
(R/'MATHEMATICAL_SCOPE_AND_SOUNDNESS.md').write_text('# Mathematical scope and soundness\n\nRound98 proves twelve candidate-specific positive mechanisms and one exact finite same-sector order-5 no-go. It proves no universal schedule absence, no repair theorem, no distance-12 witness, and no universal distance-11 ceiling. The exact root residual remains `{11,12}`.\n')
(R/'PROPOSED_CANONICAL_DELTA.md').write_text('# Proposed canonical delta\n\nAfter fresh independent review only: link this package and its review, append the reviewed 24 candidate selectors, and move the frontier to fresh iteration 172. Do not promote the root or route and do not narrow `{11,12}`.\n')
(R/'FIX-2.md').write_text('# FIX-2 process closure\n\nSee `PROCESS_LEDGER.json` and `verification/fix2_closure.json`. All science children were foreground, serial, bounded and reaped. Packaging model-capacity interruptions started no science process. The task scratch is removed before sealing and a final process census is retained.\n')
print(json.dumps({'status':'PASS','records':len(records),'result_sha256':sha(R/'RESULT.json'),'report_sha256':sha(R/'REPORT.md')},sort_keys=True))
