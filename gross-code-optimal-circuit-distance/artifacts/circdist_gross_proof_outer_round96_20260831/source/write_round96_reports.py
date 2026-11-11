#!/usr/bin/env python3
"""Write human-auditable Round96 reports from checked structured evidence."""
from pathlib import Path
import argparse, hashlib, json, os

ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); a=ap.parse_args(); R=a.root.resolve()
def load(rel): return json.loads((R/rel).read_text())
def sha(rel): return hashlib.sha256((R/rel).read_bytes()).hexdigest()
def write(rel,text): (R/rel).write_text(text.rstrip()+"\n")
audit=load('verification/independent_campaign_audit.json'); result=load('RESULT.json'); syn=load('synthesis/order4_gf2_closure.json')
proof=load('controls/proof_fixture_controls.json'); env=load('ENVIRONMENT.json'); bind=load('INPUT_BINDINGS.json')

table=[]
for row in audit['iterations']:
    i=row['iteration']; x=row['direct']['Xerr']; z=row['direct']['Zerr']; o=row['outer']
    xb=''.join(map(str,x['physical_logical_action'])); zb=''.join(map(str,z['physical_logical_action']))
    table.append(f"| {i} | {row['source_selector_count']} | SAT {o['solver_wall_seconds']:.6f} | SAT {x['solver_wall_seconds']:.6f} | {x['weight']}/{x['canonical_support_weight']}/{x['physical_support_weight']} | `{xb}` | SAT {z['solver_wall_seconds']:.6f} | {z['weight']}/{z['canonical_support_weight']}/{z['physical_support_weight']} | `{zb}` |")
candidate_table="\n".join(table)
initial=result['initial_frontier']; fresh=result['fresh_state']; sx=syn['sector_results']['Xerr']; sz=syn['sector_results']['Zerr']

report=f"""# CIRCDIST Gross exact outer/direct continuation — Round96 proposer report

## Exact verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** This package is proposer evidence, not an independently reviewed theorem. All twelve exact outer queries at iterations 148–159 were SAT, and both complete unrestricted direct-360 CSS-sector queries were SAT for every outer model. No outer or direct UNSAT occurred, so no actual Gross DRAT/LRAT certificate exists and neither frozen branch closes. The canonical Gross node and root route remain **CONJECTURED** and the frozen claim remains **D*_Gross in {{11,12}}**.

The positive mechanisms close only their twelve concrete source schedules. They are not a universal cover and do not narrow {{11,12}}.

## Commissioned binding and reconstruction

The following inputs were checked byte-for-byte before the first solve and copied into `bindings/`:

- scheduler `3c8965b3cc30f6ebcdc5f051073f2c0eb0dc39d537cd9f3f171633d6eac7bab1`;
- Gross node `f84492190a1dad3b5d69bf38a9a62d3212f0c3844ee3338dc96517fbb0671135`;
- Round95 review `b6a23911b5f9974454a4f4291eaa09e30308547925aa71972d5199e3715c9450`;
- reviewed Round94 root and payload seals `1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c` and `c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54`.

All {load('reconstruction/input_bindings.json')['reviewed_round94_manifest']['root_rows']:,} Round94 root rows and {load('reconstruction/input_bindings.json')['reviewed_round94_manifest']['payload_rows']:,} payload rows were independently rehashed before use. Iteration 148 was verified fresh/unstarted with 14,484 inherited order predicates and 256 exact EFSSC selectors. Its state, selector-state, source-file, source-semantic, and CNF digests are respectively `{initial['state_file_sha256']}`, `{initial['selector_state_sha256']}`, `{initial['source_file_sha256']}`, `{initial['source_semantic_sha256']}`, and `{initial['cnf_sha256']}`. The exact formula has {initial['assertions']:,} assertions, {initial['variables']:,} variables, and {initial['clauses']:,} clauses.

Fresh deterministic compilation was byte-identical to the reviewed decompressed CNF, assertion map, and circuit trace; metadata agreed after excluding runtime-only timing. The independent encoding checker partitioned every clause once, reconstructed every source root, and proved every non-primary variable uniquely defined. See `reconstruction/correspondence.json` and `reconstruction/fresh.encoding_check.json`.

## Exact semantics checked

For a sector-specific set of named elementary fault locations F, the checker separately computes:

`N(F) = symmetric difference of named locations`, `C(F) = XOR of canonical column supports`, and `P(F) = XOR of physical suffix supports`.

A direct SAT witness is accepted only when `1 <= |N(F)| <= 10`, the complete DIMACS assignment satisfies every clause, the frozen schedule is legal, both detector syndromes vanish, both logical actions are nonzero, and canonical and physical logical parities agree. Named fault weight is never replaced by `|C(F)|` or `|P(F)|`. Every direct formula contains all 360 primary fault-selection variables and excludes pool, residual-pattern, check-count, and within-check-order restrictions.

## Exact order-4 synthesis census

Before blind continuation, the package exhaustively enumerated the reviewed post-i136 state137 same-sector order-4 domain. The exact split was independently verified as 125 Xerr selectors and 109 Zerr selectors. Therefore

`C(125,4) = 9,691,375`, `C(109,4) = 5,563,251`, total `15,254,626` unordered distinct quadruples.

The streaming MITM enumerator assigns every quadruple its unique sorted indices `a<b<c<d`, keeps exactly all left pairs `a<b<c`, and combines them only with `c<d`. Observed counts equal both binomial closed forms. It samples nothing.

| sector | full quadruples | named-weight <=10 | unique results | inherited results | novel eligible | canonical syndrome zero | physical syndrome zero | novel retained |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Xerr | {sx['unordered_distinct_quadruples_enumerated']:,} | {sx['eligible_weight_1_to_10_with_multiplicity']:,} | {sx['unique_eligible_named_results']:,} | {sx['unique_existing_predicate_results']:,} | {sx['unique_novel_eligible_results']:,} | {sx['canonical_syndrome_zero_results']:,} | {sx['physical_syndrome_zero_results']:,} | {sx['unique_novel_conservative_source_valid_retained']:,} |
| Zerr | {sz['unordered_distinct_quadruples_enumerated']:,} | {sz['eligible_weight_1_to_10_with_multiplicity']:,} | {sz['unique_eligible_named_results']:,} | {sz['unique_existing_predicate_results']:,} | {sz['unique_novel_eligible_results']:,} | {sz['canonical_syndrome_zero_results']:,} | {sz['physical_syndrome_zero_results']:,} | {sz['unique_novel_conservative_source_valid_retained']:,} |

All eligible exact-name multiplicities were one. Xerr canonical/physical support weights range 2–70/2–72; Zerr ranges 2–74/2–74. Complete support-weight histograms, location-weight histograms, checksums, and logical histograms are retained in `synthesis/order4_gf2_closure.json`. Xerr has no syndrome-zero logical action. Zerr has one conservative valid occurrence with logical action `100110100011`, but its exact named result is inherited; 106 eligible results are inherited in all and no novel predicate survives. Hence **zero selectors were appended from synthesis**.

The census explicitly separates zero named, canonical, and physical support (all zero counts); canonical and physical syndrome; canonical and physical logical triviality; sector; named-set multiplicity; inherited semantic dedup; overlapping pair decompositions; schedule-local validity; and support-weight substitution. Cross-sector XOR is excluded by a retained counterexample. See `SYNTHESIS_PROOF.md`.

## Strict-serial candidate campaign

Weights below are `named/canonical-support/physical-support`. Every syndrome is empty; every shown 12-bit physical logical action is nonzero and equals its canonical action.

| iter | selectors | outer | Xerr | X weights | X logical | Zerr | Z weights | Z logical |
|---:|---:|---|---|---|---|---|---|---|
{candidate_table}

Totals: 12 complete outer SAT assignments, 24 complete direct SAT assignments, zero UNSAT, zero unknown, zero timeout, zero repair entry. Solver intervals are pairwise non-overlapping. Each iteration appended exactly its two concrete schedule-valid selectors only after both sectors replayed, then atomically promoted a fresh next state.

SAT proof production was enabled on all 36 solver calls. Each SAT-side stream was fully read and summarized by SHA-256, byte count, LF count, and empty-clause count, then deleted because it is not an UNSAT certificate. All 36 summaries report zero empty-clause lines. Fixture controls establish tooling behavior only: valid DRAT and generated LRAT were accepted; corrupt and truncated DRAT and LRAT were rejected.

## Fresh frontier

Iteration {fresh['next_iteration']} is sealed fresh/unstarted with {fresh['selector_count']} selectors, selector-state `{fresh['selector_state_sha256']}`, state file `{fresh['state_file_sha256']}`, source file `{fresh['source_file_sha256']}`, semantic source `{fresh['source_semantic_sha256']}`, and CNF `{fresh['cnf_sha256']}`. Its formula has {fresh['assertions']:,} assertions, {fresh['variables']:,} variables, and {fresh['clauses']:,} clauses. There is no inherited solver, model, proof, or disposition for iteration 160.

## Branch accounting and limitations

The D*=11 branch is not closed because no checked outer UNSAT proves a universal selector cover. The D*=12 branch is not closed because no outer schedule had checked absence in both unrestricted direct sectors, so repair and a distance-12 certificate were never entered. The order-4 no-go applies only to the declared 15,254,626 post-i136, same-sector, four-distinct-selector domain; it says nothing about higher closure order, cross-sector constructions, selectors outside state137, or a universal Gross cover.

The package preserved frozen S_Gross, MC0, terminal residual semantics, both CSS sectors, strict serialization, and all canonical exclusions. It did not use morphing, Circ-Preserve substitution, an alternate conflict model, exploratory pair clauses, retroactive cuts, stale compressor provenance, mixed-sector XOR, support-weight substitution, or schedule-globalized dynamic predicates.

## Reproducibility and repository discipline

The bound interpreter is `{env['python_executable']}` with executable SHA-256 `{env['python_executable_sha256']}`, Python `{env['python'].splitlines()[0]}`, z3 `{env['z3']}`, and pysat `{env['pysat']}`. Native tool hashes are in `ENVIRONMENT.json`. Full replay rebuilds and checks all 13 exact outer formulas, all 12 candidate chains, all 24 direct formulas, the order-4 census, result/process crosschecks, protected bindings, and proof controls. Repository validators and FIX-2 results are recorded under `verification/` after installation. No canonical file was edited; no commit or push was made.
"""
write('REPORT.md',report)

synth_report=f"""# Exact order-4 same-sector GF(2) synthesis proof

## Domain

Input is the independently reviewed, fresh post-i136 state137: 234 exact dynamic selectors split into 125 Xerr and 109 Zerr selectors. Only four distinct selectors from one sector are admitted. Thus the domain is exactly

`Q = {{(a,b,c,d): 0 <= a < b < c < d < n}}`, with `|Q| = C(n,4)`.

For Xerr this is {sx['unordered_distinct_quadruples_expected']:,}; for Zerr it is {sz['unordered_distinct_quadruples_expected']:,}; total {syn['finite_domain']['unordered_distinct_quadruples_expected']:,}. Repeated indices and mixed-sector tuples are outside this stated domain.

## Coverage and uniqueness

At each `c` from 2 through `n-2`, the algorithm first appends every pair `(a,c-1)` with `a<c-1`. Induction gives a left-pair list containing exactly all `(a,b)` with `a<b<c`. It then combines every such pair with every `(c,d)`, `c<d`. Every emitted tuple satisfies `a<b<c<d`. Conversely, any sorted quadruple appears when the loop reaches its unique third index `c`. Therefore every domain element appears exactly once.

The observed canonical counts equal the closed forms. Pair-pair enumeration would contain {sx['all_pair_pair_decompositions']:,}/{sz['all_pair_pair_decompositions']:,} X/Z decompositions. The code excludes {sx['overlapping_pair_decompositions_excluded']:,}/{sz['overlapping_pair_decompositions_excluded']:,} overlapping X/Z decompositions and {sx['noncanonical_disjoint_pairings_excluded']:,}/{sz['noncanonical_disjoint_pairings_excluded']:,} alternative disjoint pairings, retaining the unique canonical split.

## Effect algebra

Each selector is represented independently by a named-location bitset, canonical support bitset, physical support bitset, canonical/physical syndrome bitsets, and canonical/physical 12-bit logical actions. A quadruple effect is component-wise XOR. Named locations are symmetric-differenced before the fault-weight cap. Candidate retention requires named weight 1–10, both syndromes zero, both logical actions nonzero, equal canonical/physical actions, source-schedule validity, and a novel semantic predicate.

## Exact results

| quantity | Xerr | Zerr |
|---|---:|---:|
| domain | {sx['unordered_distinct_quadruples_enumerated']:,} | {sz['unordered_distinct_quadruples_enumerated']:,} |
| named weight <=10, multiplicity | {sx['eligible_weight_1_to_10_with_multiplicity']:,} | {sz['eligible_weight_1_to_10_with_multiplicity']:,} |
| unique eligible names | {sx['unique_eligible_named_results']:,} | {sz['unique_eligible_named_results']:,} |
| maximum multiplicity | {sx['maximum_result_multiplicity']} | {sz['maximum_result_multiplicity']} |
| zero named/canonical/physical support | {sx['zero_location_results']}/{sx['zero_canonical_support_results']}/{sx['zero_physical_support_results']} | {sz['zero_location_results']}/{sz['zero_canonical_support_results']}/{sz['zero_physical_support_results']} |
| canonical syndrome zero | {sx['canonical_syndrome_zero_results']:,} | {sz['canonical_syndrome_zero_results']:,} |
| physical syndrome zero | {sx['physical_syndrome_zero_results']:,} | {sz['physical_syndrome_zero_results']:,} |
| canonical logical trivial | {sx['canonical_logical_trivial_results']:,} | {sz['canonical_logical_trivial_results']:,} |
| physical logical trivial | {sx['physical_logical_trivial_results']:,} | {sz['physical_logical_trivial_results']:,} |
| inherited eligible names | {sx['unique_existing_predicate_results']:,} | {sz['unique_existing_predicate_results']:,} |
| novel eligible names | {sx['unique_novel_eligible_results']:,} | {sz['unique_novel_eligible_results']:,} |
| novel retained | 0 | 0 |

The one Zerr conservative valid occurrence has logical action `100110100011` and an inherited exact named predicate. Hence it cannot add a selector. All 33,654 novel eligible exact-name results fail conservatively: 32,456 Xerr and 1,198 Zerr have nonzero canonical syndrome. No sampling or probabilistic inference is used.

## Required audits

- Zero named support, canonical support, and physical support are counted separately.
- Logical triviality is counted independently from detector syndrome.
- Sector identity is never erased; a concrete mixed-sector ambiguity witness is retained.
- Every eligible exact name set is replayed; multiplicity is counted independently from semantic dedup.
- Dynamic predicates remain tied to their source schedule. A retained selector that is valid on its source schedule and invalid on iteration136 demonstrates why globalization is unsound.
- Named elementary-fault weight, canonical net-support weight, and physical net-support weight are distinct; the retained counterexample is 10/12/18.

## Scope

This is an exact no-go only for four distinct same-sector selectors in the frozen post-i136 state137. It neither proves Gross distance nor excludes higher closure order, other frontiers, or any cross-sector construction. The executable source, full histograms, counts, checksums, inputs, and replay output are retained.
"""
write('SYNTHESIS_PROOF.md',synth_report)

scope="""# Mathematical scope and soundness

## Status vocabulary

- **Theorem:** only a claim supported by a complete accepted proof object or an already reviewed canonical theorem.
- **Checked computation:** deterministic finite computation whose complete input/output and independent checker are retained.
- **Proposer result:** Round96 evidence awaiting independent review.
- **Numerical signal:** timing, weight frequency, or search behavior without theorem status.
- **Failed attempt:** a process or assertion failure with no scientific conclusion.

Round96 supplies checked proposer computation. It supplies no new Gross theorem.

## Positive selector soundness

Each accepted direct SAT mechanism is replayed from a complete unrestricted formula assignment on the exact frozen schedule. Its block is the negation of the exact conjunction of strict order atoms required by that mechanism. Consequently, the block excludes that concrete schedule family retaining the same antecedent. It does not exclude schedules where those atoms differ and does not establish a universal cover.

## Negative evidence soundness

No actual outer or direct query was UNSAT. Therefore no SAT trace is interpreted as a proof. The DRAT/LRAT controls are fixtures proving checker behavior, not Gross statements. The order-4 census is a finite-domain exhaustion theorem only for its explicitly defined domain.

## Frozen boundaries

S_Gross, MC0, terminal residual semantics, both CSS sectors, the canonical physical model, and inherited predicates are unchanged. Repair is forbidden unless both unrestricted direct sectors prove absence; that gate was never reached. Canonical and prior evidence remained read-only.
"""
write('MATHEMATICAL_SCOPE_AND_SOUNDNESS.md',scope)

failure="""# Failure ledger

All failures were foreground, bounded, and reaped. Neither failure mutated selector state or produced accepted scientific evidence.

1. **Bootstrap command rejected before process creation.** An initial command combined scratch removal with setup. The tool safety layer rejected it, with no filesystem effect and no OS child. Setup was retried only after asserting the target absent. This is recorded in `logs/bootstrap-processes.tsv`.
2. **Order-4 attempt 1, rc=1, 2.904381 s.** The script incorrectly required inherited `selected_names` to be lexically sorted. Reviewed selectors preserve direct-column order; GF(2) set algebra requires uniqueness, not lexical order. The assertion was corrected. See `logs/process/order4_exact_synthesis.json` and its stderr.
3. **Order-4 repair 1, rc=1, 3.056889 s.** Python 3.9 lacks `int.bit_count`. It was replaced by the frozen model's `popcount`, preserving exact semantics. See `logs/process/order4_exact_synthesis_repair1.json`.
4. **Order-4 repair 2, rc=0, 60.963179 s wrapper / 60.838360 s census.** The full 15,254,626-element run passed. See `logs/process/order4_exact_synthesis_repair2.json`.
5. **Transient model-capacity interruption, orchestration only.** The proposing agent turn was interrupted after the foreground preseal replay had already exited rc=0 and written its complete 116-child record. No OS science process remained live, no file was rolled back or mutated by the interruption, and work resumed from the retained disk state without repeating candidate solving or the order-4 census. This has no mathematical disposition.

No timeout, unknown solver disposition, detached process, repair branch, proof-checker failure, or weight<=8 event occurred.
"""
write('FAILURE_LEDGER.md',failure)
write('verification/orchestration_events.json', json.dumps({
    'schema':'circdist-round96-orchestration-events-v1', 'status':'DISCLOSED',
    'events':[{
        'kind':'transient_model_capacity_interruption',
        'level':'orchestration_non_os', 'os_process_started':False,
        'science_process_affected':False, 'disk_evidence_affected':False,
        'resume_basis':'preseal replay record already complete: rc0, 116 serial children, all reaped, stderr empty',
        'candidate_science_repeated':False, 'order4_census_repeated':False,
    }]
}, indent=2, sort_keys=True))

write('PROPOSED_CANONICAL_DELTA.md',"""# Proposed canonical delta

No canonical edit is proposed before independent review. Round96 is a sealed proposer package only. The Gross/root route remains CONJECTURED and D*_Gross remains {11,12}. A reviewer may link the package as checked progress, but this package does not justify changing the canonical mathematical status.
""")

fix=load('verification/fix2_closure.json') if (R/'verification/fix2_closure.json').exists() else None
if fix:
    fixtext=f"""# FIX-2 closure

Status: **PASS**. Scratch `{fix['scratch_path']}` existed before cleanup and is absent after cleanup. It was removed only after the complete package draft was installed in the sole permitted repository directory. Process scan found zero task survivors; no background or detached process was started. All replay and validator children were reaped.

The sole unavoidable external replay dependency is `{fix['retained_external_dependency']['path']}`, SHA-256 `{fix['retained_external_dependency']['sha256']}`. It is explicitly handed off and is not Round96 scratch. Structured evidence is `verification/fix2_closure.json`.
"""
else:
    fixtext="""# FIX-2 closure

Pre-install draft: the exact scratch root will be removed by `source/fix2_cleanup.py` only after successful full replay, repository validators, installation into the sole permitted package directory, and a zero-survivor scan. The bound external interpreter will be explicitly handed off. The sealed package must contain `verification/fix2_closure.json`; this placeholder is not a completion claim.
"""
write('FIX-2.md',fixtext)

key=[
 'INPUT_BINDINGS.json','ENVIRONMENT.json','PROCESS_LEDGER.json','RESULT.json','verification/independent_campaign_audit.json',
 'reconstruction/correspondence.json','synthesis/order4_gf2_closure.json','controls/proof_fixture_controls.json',
 'verification/orchestration_events.json',
 'verification/validation_summary.json','REPORT.md','SYNTHESIS_PROOF.md','MATHEMATICAL_SCOPE_AND_SOUNDNESS.md','FAILURE_LEDGER.md','PROPOSED_CANONICAL_DELTA.md','FIX-2.md'
]
lines=['# Evidence hashes','', '| file | SHA-256 |','|---|---|']
for rel in key: lines.append(f'| `{rel}` | `{sha(rel)}` |')
write('EVIDENCE_HASHES.md','\n'.join(lines))

manifest=f"""# Round96 package manifest

This self-contained proposer package retains exact sources, formulas, maps, complete SAT assignments, decoded schedules, canonical and physical replays, state transitions, synthesis inputs/output, solver-stream summaries, proof-tool fixtures, independent checkers, process records, protected input snapshots, environment hashes, validator evidence, replay evidence, reports, and deterministic two-level seals.

Scientific verdict: **{result['verdict']}**. Completed candidates: {result['completed_candidate_count']}. Fresh frontier: iteration {fresh['next_iteration']}, {fresh['selector_count']} selectors. Order-4 domain: {syn['finite_domain']['unordered_distinct_quadruples_enumerated']:,}, zero novel retained predicates.

`FILE_INVENTORY.jsonl`, `PAYLOAD_SHA256SUMS.txt`, and `SHA256SUMS.txt` are created only after all evidence is final. `replay.sh` verifies the sealed manifests and runs the full scientific replay.
"""
write('MANIFEST.md',manifest)
print(json.dumps({'status':'PASS','candidate_rows':len(table),'report_sha256':sha('REPORT.md'),'result_sha256':sha('RESULT.json')},sort_keys=True))
