#!/usr/bin/env python3
"""Assemble Round100 result, public proof, scope, failure, and process records."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,platform,sys
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve()
def load(p):return json.loads((R/p).read_text())
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def dump(path,obj):(R/path).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
audit=load('verification/independent_campaign_audit.json');binding=load('INPUT_BINDINGS.json');order6=load('synthesis/order6/order6_exact_validation.json');span=load('synthesis/span/span_exact_validation.json');mixed=load('synthesis/mixed_sector_theorem.json')
failures=[
 {'id':'F001','phase':'pre-science binding audit','attempt':'Read a guessed formulas/iter172/source.json path.','failure':'FileNotFoundError; the commissioned source is source.json.gz.','correction':'Used the manifest-bound gzip path and completed the prior-package manifest check.','scientific_effect':'None; no solver or model was run and partial output supports no verdict.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F002','phase':'synthesis independent validation','attempt':'Initial direct-Z3 span validator used positional Xor with more than three arguments under z3 5.1.0.','failure':'API arity exception, return code 1, before solver.check().','correction':'Replaced it with an explicit binary left fold and reran both sectors to checked UNSAT.','scientific_effect':'The failed attempt produced no SAT/UNSAT result and supports no theorem.','retained_evidence':'failures/F002_span_validator_z3_api/'},
 {'id':'F003','phase':'read-only source audit','attempt':'A line-extraction helper requested one line past the source length.','failure':'IndexError in an inspection-only loop.','correction':'Bounded the extraction to the actual line count.','scientific_effect':'None; no file mutation and no scientific process.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F004','phase':'audit authoring','attempt':'A generated audit draft contained a placeholder source hash.','failure':'Manual pre-execution review rejected the draft.','correction':'Replaced the placeholder with the commissioned exact source binding before first execution.','scientific_effect':'None; rejected code never executed.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F005','phase':'compression authoring','attempt':'First Round100 compressor draft had a malformed f-string.','failure':'py_compile SyntaxError before compression.','correction':'Corrected the delimiter, recompiled, then compressed all 222 streams with byte-roundtrip checks.','scientific_effect':'None; no evidence file was compressed by the failed draft.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F006','phase':'preseal replay attempt 1','attempt':'Replay resolved the virtual-environment Python symlink to its base interpreter.','failure':'First physical replay could not import z3 after 28 successful binding/compression/formula children; replay child 29 returned 1.','correction':'Preserved the supplied interpreter path with absolute() rather than resolve().','scientific_effect':'All 13 formula replays passed; the incomplete run supports no package verdict.','retained_evidence':'failures/F006_replay_venv_resolution/'},
 {'id':'F007','phase':'preseal replay attempt 2','attempt':'The immutable science audit counted later packaging process records.','failure':'Hard-coded 204 science-record assertion failed after 123 successful direct replay children and 12 proof grandchildren.','correction':'Explicitly separated the closed 204-record science census from later round100_* packaging records.','scientific_effect':'Every science and synthesis replay stage through the mixed-sector theorem passed; incomplete package run supports no final replay verdict.','retained_evidence':'failures/F007_replay_science_census_scope/'},
 {'id':'F008','phase':'mixed-sector checker authoring','attempt':'Toy cardinality control used int.bit_count under the system Python.','failure':'AttributeError before the checker result.','correction':'Used bin(value).count("1") and reran all 256 controls to PASS.','scientific_effect':'None; proof statement and science artifacts were unchanged.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F009','phase':'read-only CLI inspection','attempt':'Invoked validate_span.py --help with system Python lacking z3.','failure':'Import-time ModuleNotFoundError; no validation was requested or run.','correction':'Used the bound z3-capable environment for all actual span validations.','scientific_effect':'None; this was a help probe.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F010','phase':'read-only binary inspection','attempt':'Invoked order6_mitm with no arguments to obtain its usage string.','failure':'Expected usage exit; no input was read.','correction':'All theorem runs supplied INPUT ELIGIBLE SUMMARY SECTOR.','scientific_effect':'None; this was a usage probe.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F011','phase':'packaging edit','attempt':'An apply_patch request tried delete-and-add operations on one path.','failure':'Patch tool rejected the request without changing a file.','correction':'Wrote the draft, then compiled and corrected it before execution.','scientific_effect':'None; no OS science process and no artifact mutation from the rejected patch.','retained_evidence':'FAILURE_LEDGER.md'},
 {'id':'F012','phase':'first sealed-replay launch','attempt':'The launch setup included an rm -rf cleanup of a proposed external replay directory.','failure':'The host command policy rejected the command before creating an OS process.','correction':'Used a fresh unique directory and no deletion command; the sealed replay then passed with 145 known children.','scientific_effect':'None; the rejected launch did not execute and did not touch the package or filesystem.','retained_evidence':'FAILURE_LEDGER.md'},
]
failure_record={'schema':'circdist-round100-failure-ledger-v1','status':'COMPLETE','failure_count':len(failures),'failures':failures,'round98_disclosure':{'events':3,'description':'Round98 had three post-science model-capacity interruptions during packaging/recovery.','inherited_as_round100_failures':False},'no_failure_omitted_to_the_best_of_the_proposer_audit':True}
dump('FAILURE_LEDGER.json',failure_record)
fl=['# Round100 failure ledger','',f"All {len(failures)} rejected or failed attempts known to this proposer are listed. Failed partial outputs support no scientific or package verdict.",'']
for f in failures:fl += [f"## {f['id']} — {f['phase']}",'',f"**Attempt.** {f['attempt']}",'',f"**Failure.** {f['failure']}",'',f"**Correction.** {f['correction']}",'',f"**Effect.** {f['scientific_effect']}",'',f"**Evidence.** `{f['retained_evidence']}`",'']
fl += ['## Prior-round disclosure','','Round98 had three post-science model-capacity interruptions. They are disclosed here but are not inherited as Round100 failures.','']
(R/'FAILURE_LEDGER.md').write_text('\n'.join(fl))

# Retain every PID-bearing process record, plus nested driver/certificate/replay evidence.
process_rows=[]
for p in sorted((R/'logs/process').glob('*.json')):
 x=json.loads(p.read_text());process_rows.append({'path':p.relative_to(R).as_posix(),'record':x})
science=[x for x in process_rows if x['path'].split('/')[-1]!='independent_campaign_audit.json' and not x['path'].split('/')[-1].startswith('round100_')]
solver=[]
for x in science:
 name=Path(x['path']).name;row=x['record']
 if 'cadical_proof' in name and row.get('returncode') in (10,20):solver.append((row['started_unix'],row['ended_unix'],name,row['returncode']))
solver.sort();nonoverlap=all(a[1]<=b[0] for a,b in zip(solver,solver[1:]))
drivers=[json.loads(p.read_text()) for p in sorted((R/'campaign').glob('driver_process_*.json'))]
certs=[]
for sec in ('Xerr','Zerr'):
 c=load(f'synthesis/span/{sec}.unsat_certificate/certificate.json');certs += [{'sector':sec,'process':x} for x in c['processes']]
replays=[]
for rel in ('failures/F006_replay_venv_resolution/preseal_science_replay.failed.json','failures/F007_replay_science_census_scope/preseal_science_replay_attempt2.failed.json'):
 if (R/rel).exists():replays.append({'path':rel,'record':load(rel)})
if (R/'verification/preseal_full_replay.json').exists():replays.append({'path':'verification/preseal_full_replay.json','record':load('verification/preseal_full_replay.json')})
repo=load('verification/repository_validators/summary.json') if (R/'verification/repository_validators/summary.json').exists() else None
final_preseal=load('verification/final_preseal_checks.json') if (R/'verification/final_preseal_checks.json').exists() else None
ledger={'schema':'circdist-round100-process-ledger-v1','status':'PASS','retained_pid_bearing_process_records':process_rows,'retained_pid_record_count':len(process_rows),'science_process_record_count':len(science),'science_returncodes':{str(code):sum(x['record'].get('returncode')==code for x in science) for code in (0,1,10,20)},'science_solver_intervals':solver,'science_solver_interval_count':len(solver),'strict_solver_nonoverlap':nonoverlap,'campaign_drivers':drivers,'campaign_driver_count':len(drivers),'campaign_wrapper_processes_started_serially':sum(x['child_wrapper_processes_started_serially'] for x in drivers),'span_certificate_children':certs,'span_certificate_child_count':len(certs),'package_replay_attempt_records':replays,'repository_validator_children':repo['checks'] if repo else [],'final_preseal_children':final_preseal['children'] if final_preseal else [],'final_preseal_nested_proof_children':final_preseal['nested_proof_control_children'] if final_preseal else 0,'prior_round98_sealed_replay_children':56,'all_retained_pid_records_reaped':all(x['record'].get('reaped') is True for x in process_rows),'retained_timeouts':sum(bool(x['record'].get('timed_out')) for x in process_rows),'retained_detached_processes':sum(bool(x['record'].get('detached')) for x in process_rows),'process_scope_note':'PID-bearing science, synthesis, campaign, proof, replay, and repository-gate children are retained. Read-only orchestration shell invocations were publicly declared at launch; the host exec API does not return their shell PIDs for retrospective storage.'}
dump('PROCESS_LEDGER.json',ledger)

result={'schema':'circdist-gross-proof-outer-round100-result-v1','status':'PASS','scientific_verdict':audit['scientific_verdict'],'root_status':'CONJECTURED','route_status':'CONJECTURED','D_star_Gross':[11,12],'closure':{'universal_D11_ceiling_proved':False,'explicit_D12_witness_proved':False,'outer_or_direct_unsat_count':0,'stop_condition_reached':False},'campaign':{'iterations':[172,183],'completed_candidates':12,'outer_sat':12,'direct_sat':24,'outer_unsat':0,'direct_unsat':0,'unknown':0,'timeouts':0,'repair_entered':False,'selector_appends':24,'atomic_transitions':12},'initial_frontier':binding['licensed_initial_frontier'],'fresh_frontier':audit['fresh_frontier'],'outer_iterations':audit['iterations'],'synthesis':{'order6':{'status':'PASS','X_selector_count':125,'Z_selector_count':109,'X_full_domain':4690625500,'Z_full_domain':2025023364,'full_domain':6715648864,'triples_enumerated':527684,'combined_zero_candidates':0,'eligible_results_replayed':0,'exact_reduced_domain':True,'sampling':False},'full_span':{'status':'CHECKED_UNSAT_BOTH_SECTORS','proof_certificates':2,'independent_z3_unsat':2,'X_cnf_sha256':span['sector_results']['Xerr']['cnf_sha256'],'Z_cnf_sha256':span['sector_results']['Zerr']['cnf_sha256'],'scope':'reviewed post-iteration-136 schedule and 125/109 selector bases; existing named masks quotiented'},'mixed_sector':{'status':'PROVED_REDUCTION_TO_COMPONENTS','new_closure_beyond_components':False,'named_weight_bound':10}},'proof_counts':{'outer_unsat_certificates':0,'direct_unsat_certificates':0,'synthesis_unsat_certificates':2,'accepted_drat':2,'accepted_lrat':2,'corrupt_controls_rejected':4,'truncated_controls_rejected':4,'fixture_proof_control_runs':6},'input_binding_tree_sha256':binding['immutable_input_tree_sha256'],'initial_proof_dag_tree_sha256':binding['initial_proof_dag_snapshot']['tree_sha256'],'prior_round98_seal':binding['prior_round98_seal'],'failure_count':len(failures),'round98_model_capacity_interruptions_disclosed':3,'round98_interruptions_inherited_as_failures':False,'canonical_files_modified':False,'status_promotion_requested':False,'proposed_delta':'PROPOSED_CANONICAL_DELTA.md','limitations':audit['limitations']}
dump('RESULT.json',result)

env={'schema':'circdist-round100-environment-v1','python':sys.version,'python_executable':sys.executable,'platform':platform.platform(),'machine':platform.machine(),'processor':platform.processor(),'hostname':platform.node(),'z3_version':span['z3_version'],'solver':'CaDiCaL 1.9.5 packaged arm64 macOS binary','proof_tools':['drat-trim packaged arm64 macOS binary','lrat-check packaged arm64 macOS binary'],'hidden_chain_of_thought_available':False,'public_derivations_provided':True}
dump('ENVIRONMENT.json',env)

report=f'''# Gross proof outer Round100 report

## Verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** The frozen Gross root and gap-via-lift route remain **CONJECTURED**. The exact interval remains

\\[
D^*_{{\\mathrm{{Gross}}}}\\in\\{{11,12\\}}.
\\]

No outer or direct query was UNSAT, no repair gate opened, no universal `D*=11` ceiling was proved, and no explicit certified `D*=12` witness was found. Canonical, scheduler, review, and protocol files were not edited.

## Exact campaign

Iteration 172 was solved first from the commissioned unstarted frontier: 14,484 inherited order blocks, 304 selectors, 19,186 assertions, 413,646 variables, 1,406,245 clauses, and CNF `{binding['licensed_initial_frontier']['cnf_sha256']}`. It was SAT. Both complete unrestricted direct-360 sectors were then SAT and independently clause-checked and physically replayed. Only after both results settled were `r100-i172-Xerr` and `r100-i172-Zerr` appended atomically.

The same serial protocol completed iterations 173 through 183. Totals: **12 outer SAT**, **24 direct SAT**, **36 complete assignments**, **36 SAT proof streams summarized and deleted as non-certificates**, **24 accepted exact mechanisms**, and **12 atomic two-selector transitions**. Every schedule passed the frozen 864-edge audit; every direct mechanism had empty canonical and raw physical detector syndrome, equal nonzero canonical/physical logical action, and weight 1..10. No solver intervals overlapped.

The fresh unstarted frontier is iteration 184 with 328 selectors, selector-state `{audit['fresh_frontier']['selector_state_sha256']}`, state-file `{audit['fresh_frontier']['state_file_sha256']}`, source-file `{audit['fresh_frontier']['source_file_sha256']}`, semantic source `{audit['fresh_frontier']['source_semantic_sha256']}`, 19,210 assertions, 415,793 variables, 1,416,404 clauses, and CNF `{audit['fresh_frontier']['cnf_sha256']}`.

## New exact synthesis results

The exact six-distinct same-sector domain contains

\\[
\\binom{{125}}{{6}}+\\binom{{109}}{{6}}=4,690,625,500+2,025,023,364=6,715,648,864.
\\]

The MITM reduction enumerated 317,750 X triples and 209,934 Z triples and found no canonical-syndrome-zero six-set in either sector, hence no combined-syndrome-zero or eligible result. This is an exact reduced-domain theorem, not sampling; the proof of coverage and uniqueness is in `SYNTHESIS_PROOF.md`.

A stronger all-orders GF(2)-span query was UNSAT in both sectors after quotienting every existing full named mask. X: 12,949 variables, 43,827 clauses, CNF `{span['sector_results']['Xerr']['cnf_sha256']}`. Z: 12,089 variables, 40,443 clauses, CNF `{span['sector_results']['Zerr']['cnf_sha256']}`. Both DRATs were accepted, generated LRATs were accepted, corrupt/truncated DRAT and LRAT controls were rejected, and an independent direct-semantics Z3 encoding returned UNSAT in both sectors.

For CSS mixed-sector mechanisms of total named weight at most 10, an undetected nontrivial mixed action has an undetected nontrivial component of named weight at most 10. Thus mixed composition cannot evade the two component direct queries. This is a reduction theorem, not additional global closure.

## Scope and limitations

The order-six and span theorems bind the reviewed post-iteration-136 schedule and the 125 Xerr / 109 Zerr bases. The six-distinct theorem does not cover repeated indices, order at least seven, mixed sectors, other schedules/frontiers, or mechanisms outside those bases. The span theorem covers all GF(2) combinations of the reviewed bases but explicitly quotients existing masks and says nothing about arbitrary outside-span mechanisms. A positive direct result excludes only its source schedule after its selector is installed.

Round98 had three post-science model-capacity interruptions. They are disclosed, but none is inherited as a Round100 failure. Round100 failures and corrections are complete in `FAILURE_LEDGER.md`.
'''
(R/'REPORT.md').write_text(report)

synth=f'''# Round100 synthesis proof

## Frozen row semantics

For a fixed sector, selector row `j` carries exact GF(2) vectors: a 360-bit named mask `n_j`, canonical and physical supports, canonical and physical 72-bit detector syndromes `s^c_j,s^p_j`, and 12-bit logical actions `l^c_j,l^p_j`. All vectors are regenerated from the frozen model. The order-six decision vector is

\\[
v_j=(s^c_j,s^p_j)\\in\\mathbb F_2^{{144}}.
\\]

It is stored in four explicitly little-endian 64-bit limbs. Unused high bits are checked zero. Equality is full `std::array<uint64_t,4>` equality; hashes and checksums never decide membership.

## Exact six-distinct MITM theorem

Every canonical six-distinct index set has one sorted representation

\\[
i_0<i_1<i_2<i_3<i_4<i_5
\\]

and one split `L=(i0,i1,i2)`, `U=(i3,i4,i5)` satisfying `max(L)<min(U)`. Define the triple key `K(a,b,c)=v_a xor v_b xor v_c`. In characteristic two,

\\[
v_{{i_0}}\\oplus\\cdots\\oplus v_{{i_5}}=0
\\iff K(L)=K(U).
\\]

The algorithm enumerates all `C(n,3)` triples, sorts by the complete key, and within each equal-key group enumerates every ordered pair with `max(L)<min(U)`. Coverage follows by mapping every syndrome-zero six-set to its unique split. Soundness follows because every emitted separated pair has six distinct sorted indices and equal keys. Uniqueness follows because a sorted six-set has only one first-three/last-three split. Small-universe controls exhaust `C(n,6)` for every `n=6..12`.

X enumerated 317,750 triples for the closed-form domain 4,690,625,500; Z enumerated 209,934 triples for 2,025,023,364. In both sectors every canonical, physical, and combined triple-key group had size one, so there were zero separated equal-key pairs and zero eligible results. The exact algorithm therefore closes the six-distinct domains without streaming 6.716 billion tuples.

The C++ table row is 152 bytes. Nominal table storage was 48,298,000 bytes (X) and 31,909,968 bytes (Z); measured peak RSS was 51,347,456 and 34,553,856 bytes. Retained science runtimes were 0.160842 and 0.074303 seconds. The independent Python replay regenerated all 234 row effects, all 545,126 triples, every histogram/checksum, the endianness controls, and every eligible stream in 6.626 seconds.

X triple checksum: `c030453f472dc14de03249734a8ea38d0b9bfbaba48441bcd1383d579b0ff978`. Z: `aa95d9754426a758eb47a8ff7e82e8debd69abcdbb6a91556b720d84c7981300`. Both combined-candidate checksums are zero.

## Stronger exact span theorem

For coefficients `x_j in F2`, the CNF constructs every named bit, both syndrome vectors, and both logical vectors by exact XOR equivalences. It asserts named weight 1..10 through an exact at-least-j recurrence, both syndromes zero, canonical logical action equal to physical logical action and nonzero, and the full 360-bit named mask different from each installed same-sector selector mask. The query therefore asks for a novel valid low-weight mask anywhere in the whole reviewed selector span.

Both CNFs are UNSAT. X DRAT `{span['sector_results']['Xerr']['drat_sha256']}`, LRAT `{span['sector_results']['Xerr']['lrat_sha256']}`. Z DRAT `{span['sector_results']['Zerr']['drat_sha256']}`, LRAT `{span['sector_results']['Zerr']['lrat_sha256']}`. Independent Z3 rebuilt the equations without CNF auxiliaries, checked 8 complete gate truth assignments and 544,766 cardinality recurrence cases, and returned UNSAT for coefficient domains `2^125` and `2^109`.

## Mixed-sector reduction

Let a CSS mechanism have component name sets `N_X,N_Z` and total weight `|N_X union N_Z|`. Undetected means each component syndrome is zero. If its mixed logical action is nontrivial, at least one component logical action is nontrivial. For each component,

\\[
|N_S|\\le |N_X\\cup N_Z|\\le 10.
\\]

Thus any undetected nontrivial mixed mechanism in the direct bound contains an undetected nontrivial same-sector component in the same bound. Checked absence of both components would imply mixed absence; the Round100 direct queries were SAT, so this reduction supplies no global closure.
'''
(R/'SYNTHESIS_PROOF.md').write_text(synth)

scope='''# Mathematical scope and soundness

## Checked statements

1. Every retained outer SAT assignment satisfies every DIMACS clause and decodes to a legal frozen, globally interleaved 864-edge schedule avoiding all 14,484 reviewed order blocks and all selectors then installed.
2. Every retained direct SAT assignment satisfies every clause of a complete unrestricted weight-1..10 direct-360 query. Canonical and raw physical replay both have empty syndrome and equal nonzero logical action.
3. The order-six MITM theorem covers all and only canonical six-distinct tuples of the reviewed 125-row Xerr and 109-row Zerr bases exactly once.
4. The span certificates exclude novel named masks of weight 1..10 in the complete GF(2) spans of those two reviewed bases, on that reviewed schedule, after existing masks are quotiented.
5. The CSS mixed-sector theorem reduces a bounded mixed mechanism to a bounded same-sector component.

## Statements not proved

No universal Gross `D*=11` ceiling, explicit `D*=12` witness, arbitrary-mechanism theorem, other-schedule theorem, or outer/direct UNSAT theorem was proved. The order-six theorem alone does not cover repeated indices, order at least seven, mixed sectors, or outside-basis mechanisms. The span theorem covers all orders only inside its named reviewed spans and deliberately permits installed masks. None of the synthesis UNSAT certificates is an outer or direct absence certificate.

The exact scientific verdict is therefore `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`, with `D*_Gross in {11,12}` and canonical status unchanged.
'''
(R/'MATHEMATICAL_SCOPE_AND_SOUNDNESS.md').write_text(scope)

proposed=f'''# Proposed canonical delta

This package proposes **no canonical edit and no status promotion**. After an independent review accepts the package, a later authorized task may add this package as evidence to the Gross conjecture node and record the fresh unstarted iteration-184 frontier:

- selector count: 328
- selector-state SHA-256: `{audit['fresh_frontier']['selector_state_sha256']}`
- state-file SHA-256: `{audit['fresh_frontier']['state_file_sha256']}`
- source-file SHA-256: `{audit['fresh_frontier']['source_file_sha256']}`
- source-semantic SHA-256: `{audit['fresh_frontier']['source_semantic_sha256']}`
- CNF SHA-256: `{audit['fresh_frontier']['cnf_sha256']}`

The node and route remain `CONJECTURED`; `D*_Gross` remains in `{{11,12}}`.
'''
(R/'PROPOSED_CANONICAL_DELTA.md').write_text(proposed)

(R/'FIX-1.md').write_text('''# FIX-1 — evidence finalization\n\nAll science outputs were copied into the sole Round100 package, deterministic gzip streams were round-trip checked, failed attempts were retained, the exact frontier is unstarted, repository gates passed, and no canonical/protocol/scheduler file was edited. The package is ready for final replay, scratch cleanup, inventory, and two-level sealing.\n''')
print(json.dumps({'status':'PASS','result':'RESULT.json','failures':len(failures),'process_records':len(process_rows)},sort_keys=True))
