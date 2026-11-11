#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def sem(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p):
 p=Path(p);p=p if p.is_absolute() else R/p;return json.loads(p.read_text())
def dump(p,o):p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def wr(p,s):(R/p).write_text(s.rstrip()+'\n')

snapshots=[
 ('source_bindings/repository/DAG_PROTOCOL.md','DAG_PROTOCOL.md'),
 ('source_bindings/repository/FILE_PROTOCOL.md','FILE_PROTOCOL.md'),
 ('source_bindings/repository/SCHEDULER.yaml','operations/circdist/SCHEDULER.yaml'),
 ('source_bindings/repository/CIRCDIST.gross.yaml','circdist/proof-dag/nodes/CIRCDIST.gross.yaml')]
embedded=[]
for p in sorted((R/'source_bindings').rglob('*')):
 if p.is_file():embedded.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
engine_names=['src/round63_src/model.py','src/round63_src/outer.py','src/round68_build.py','src/round68_verify.py','src/build_online_candidate.py','src/verify_online_outer.py','src/replay_direct_candidate.py','src/append_dynamic_blocks.py','src/generalize_online.py','src/synthesize_cross_registry.py','src/run_round78_iteration.py','src/inputs/w12X.txt','src/inputs/w12Z.txt']
engine=[{'path':n,'bytes':(R/n).stat().st_size,'sha256':sha(R/n)} for n in engine_names]
start_paths={'dynamic':'restart/dynamic_blocks_iteration78.json','generalized':'restart/installed_generalized_terms_iteration78.json','registry':'restart/online_mechanism_registry_iteration78.json','raw_mechanisms':'restart/full_raw_mechanisms_iteration78.json'}
states={}
for k,n in start_paths.items():
 o=load(n);p=R/n;states[k]={'path':n,'uncompressed_bytes':p.stat().st_size,'uncompressed_sha256':sha(p),'semantic_sha256':sem(o),'count':len(o) if isinstance(o,list) else o.get('term_count',o.get('mechanism_count'))}
bindings={'schema':'round78-cross-registry-source-bindings-v1','status':'PASS',
 'round76_source':{'live_repo_path':'circdist/artifacts/circdist_gross_online_generalizing_round76_20260829','embedded_seal_file':'source_bindings/round76/SHA256SUMS.txt','seal_file_sha256':'e966770d8839eeeabbd672a4c4a647d1b92fb9a2955b6750834d7f6bda1cb87e','source_manifest_entries':1349},
 'round76_exact_review':{'live_repo_path':'circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md','embedded_path':'source_bindings/review/circdist_gross_round76_online_generalizing_exact_review_20260829.md','sha256':'1105df9cda3c9afb7b152ebd0cd6e7f5aff82b2a2441c52635169d13eb2cea39'},
 'R77_F1_final_compressor':{'path':'src/compress_deterministic.py','bytes':2760,'sha256':'d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde','provenance':'exact reviewed final compressor; stale pre-adaptation row is forbidden and not used as final provenance'},
 'reviewed_unstarted_iteration78':{'iteration':78,'installed_blocks':7359,'counts':{'base':1460,'dynamic':156,'generalized':5743,'registry':72,'raw_mechanisms':72},'semantic_sha256':{'dynamic':'656be42225ee1fb1f51426eb5544208a6d58df8ef6a015d981561b8048d57082','generalized':'031794ebbcad05fc81e1f028a7e4833ced91779c44c888b98db73f4ebd20c3cd','registry':'bafc7e4c7fb5ebdd5d090790a603b1dc8c956e2260d1047c9f4b825478b103a9','raw_mechanisms':'864e151dde3451a63a30ff960a02826f8d6a752fd3a4383cfe266caec890a3ce'},'states':states},
 'pre_outer_synthesis_transition':'cross_registry/pre_outer_synthesis_transition.json',
 'actual_direct_primary_domain':{'per_sector':360,'data_singletons':144,'residual_elementary_fault_columns':216,'residuals_per_check':3,'checks':72,'weight12_pool_role':'quotient basis and constructive positive completion only; not a primary-column restriction'},
 'environment_freeze':{'path':'requirements.freeze.txt','bytes':(R/'requirements.freeze.txt').stat().st_size,'sha256':sha(R/'requirements.freeze.txt'),'expected_sha256':'e5ace88d19150ff07d84704ca6e9f4a4a070c2f588a6502e4ca0bfe99ebf6ee6'},
 'embedded_source_copies':embedded,'engine_files':engine,
 'repository_start_snapshots':[{'snapshot':p,'live_path':live,'bytes':(R/p).stat().st_size,'sha256':sha(R/p)} for p,live in snapshots],
 'canonical_repository_mutated_during_computation':False,'source_package_mutated':False}
assert sha(R/'source_bindings/round76/SHA256SUMS.txt')==bindings['round76_source']['seal_file_sha256']
assert sha(R/bindings['round76_exact_review']['embedded_path'])==bindings['round76_exact_review']['sha256']
assert sha(R/'src/compress_deterministic.py')==bindings['R77_F1_final_compressor']['sha256'] and (R/'src/compress_deterministic.py').stat().st_size==2760
assert sha(R/'requirements.freeze.txt')==bindings['environment_freeze']['expected_sha256']
dump('SOURCE_BINDINGS.json',bindings)

cegar=load('cegar/summary.json');cl=load('classification/summary.json');xr=load('cross_registry/summary.json');res=load('RESULT.json');neg=load('controls/negative_controls.json')
rows=[]
for x in cegar['iterations']:
 rows.append(f"| {x['iteration']} | `{x['candidate_sha256'][:12]}…` | {x['before_counts']['total_blocks']:,} | {x['direct_fault_weights']['Xerr']}/{x['direct_fault_weights']['Zerr']} | {x['increments']['online_generalized']} | {x['increments']['cross_registry']} | {x['after_counts']['generalized']:,} | {x['after_counts']['dynamic']} | {x['after_counts']['registry']} | {x['after_counts']['total_blocks']:,} |")
itable='\n'.join(rows)

wr('README.md',f'''# CIRCDIST Gross cross-registry proposer — round 78

**Verdict:** `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`.

This sealed proposer begins only from the exact reviewed, unstarted iteration-78 state (`G=5,743`, `D=156`, registry/raw `72`, total `7,359`). Before the first outer call it performs a separate cross-registry synthesis over all 72 reviewed raw mechanisms and retains 2,826 exhaustively validated pair regions, giving first-outer state `G=8,569`, total `10,185`. It then closes 12 candidates, iterations 78–89, with a fresh outer process and both unrestricted direct-360 sectors for each candidate. Every one of the 24 direct sectors is SAT and passes complete-assignment, every-clause, canonical and physical replay. No UNSAT, UNKNOWN, timeout, repair, or absence conclusion occurs.

The final exact restart is unstarted iteration 90: `G=10,595`, `D=180`, registry/raw `96`, total `12,235`. The round contributes 4,852 generalized terms: 2,826 pre-outer cross-registry, 62 online, and 1,964 post-candidate cross-registry. Candidate-exact blocks are preserved. `D*_Gross` remains in `{{11,12}}`.

## Audit map

- `SOURCE_BINDINGS.json` binds the source seal, exact review, reviewed restart, live snapshots, environment, engine, and R77-F1 final compressor.
- `cross_registry/` contains every catalog, option registry, completion attempt, 720×720 relation, raw candidate, semantic classification, retained term, selector replay and state transition.
- `cegar/iter78` … `iter89` contain the actual outer SMT, candidate, both direct-360 formulae and assignments, raw mechanisms, online catalogs/relations/DP, cross-registry synthesis, and four-state commit journals.
- `classification/`, `cegar/summary.json`, and `restart/restart_state.json` are aggregate and restart ledgers.
- `controls/` contains fresh valid, corrupt, and truncated DRAT/LRAT controls. They test only the proof toolchain and are not Gross proofs.
- `FIX-2.md` and `development/` disclose every interrupted or failed development attempt, including memory incidents and the temporary v6 staging rollback.
- `verify.py --quick` verifies the seal, compression, bindings, state chain, ledgers and controls. `verify.py --full` additionally rebuilds every outer/direct formula in fresh processes, replays all 96 raw mechanisms, all local catalogs, every retained pair tuple, and every multi-check DP/product.

Fresh independent exact review is required before any continuation or node mutation.
''')
wr('VERDICT.txt','MATERIAL-CHECKED-PROGRESS-NOT-CLOSED')
wr('REVIEW_LICENSE.txt','Fresh independent exact review is required. This proposer is not licensed for canonical node mutation, branch closure, repair, or a D*_Gross conclusion until that review accepts the seal, source bindings, all retained domains, state transitions, proof controls, and exact iteration-90 restart.')
wr('RESTART_LICENSE.md',f'''# Exact restart license

The only proposed continuation state is the unstarted iteration 90 recorded in `restart/restart_state.json`:

- dynamic exact blocks: 180, semantic `{res['final']['semantic_sha256']['dynamic']}`;
- generalized terms: 10,595, semantic `{res['final']['semantic_sha256']['generalized']}`;
- mechanism registry: 96, semantic `{res['final']['semantic_sha256']['registry']}`;
- raw mechanisms: 96, semantic `{res['final']['semantic_sha256']['raw_mechanisms']}`;
- installed outer blocks: 1,460 + 10,595 + 180 = 12,235.

Continuation is licensed only after fresh independent exact review. It must start a fresh outer process at iteration 90, consume exactly these four files, retain complete unrestricted direct-360 sectors, preserve candidate-exact blocks, validate raw physical mechanisms before semantic classification, and commit the four-state bundle only after retained validation. UNKNOWN, timeout, signal, a negative search result, zero cell, or deletion witness has no mathematical disposition. Repair requires independently accepted candidate-specific DRAT and LRAT absence proofs for both direct sectors.
''')
wr('ITERATION_LEDGER.md',f'''# Iteration ledger

Every row is a fully committed candidate. The `X/Z` column is direct fault weight; every formula has 144 singleton plus 216 residual primary columns, a complete assignment, and every clause plus raw canonical/physical replay checked.

| Iteration | candidate SHA | blocks before | X/Z | online + | cross + | G after | D after | registry | blocks after |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
{itable}

Outer verdicts: 12 SAT, zero UNSAT/UNKNOWN/timeout. Direct verdicts: 24 SAT, zero accepted absence proofs. Repair never ran and the branch is not closed.
''')
wr('CLASSIFICATION_LEDGER.md',f'''# Classification ledger

Online generalization retains {cl['online_retained_terms']} terms from 24 new raw mechanisms. It materializes {cl['local_order_records']:,} local order records, literally replays {cl['literal_retained_tuple_replays']:,} retained pair tuples, and proves {cl['factorized_symbolically_proved_tuples']:,} multi-check tuples by exact signature-class GF(2) products. Four retained multi terms carry every allowed local record, all DP layers and multiplicities, canonical=physical local signatures, a fixed selector mechanism, and exact Cartesian products.

Cross-registry synthesis runs in 13 batches across registry sizes 72 through 96. It retains {xr['retained_terms_total']:,} terms, represents {xr['pair_truth_cells']:,} exact truth cells and {xr['explicit_positive_pair_cells']:,} explicit positive cells, and literally replays {xr['literal_pair_tuples_replayed']:,} retained tuple selectors. All retained cross-registry terms are positive pair rectangles; the bounded two-selector multi pilot generated candidates but retained none after exact positive-domain and full-library classification. That is not a global multi-term absence claim.

The combined literal pair replay count is {res['validation_domains']['total_literal_tuples']:,}. Semantic equality is equality of sector plus normalized 720-order masks on normalized checks. Dominance is finite-region containment. Classification uses the full evolving installed library and whole current batch before any retained-state mutation. Candidate-exact blocks are never replaced.

Deletion controls total {neg['counts']['retained_term_deletion_controls_total']:,}. They license only atom minimality for the named relation or fixed selector. They never license installed-union minimality, global physical-mechanism minimality, exhaustion, or absence.
''')
wr('CROSS_REGISTRY_SYNTHESIS.md',f'''# Exact cross-registry synthesis

## Input and separate transition

The pre-outer batch binds all 72 reviewed raw mechanisms and replays each physical selector. It builds 129 complete 6! catalogs ({92880:,} records), 349 distinct residual options, and all 30,037 eligible distinct-check option-pair attempts. There are 1,938 constructive positive configurations, 1,835 of them joining different source candidates, and 1,051 positive relations. The relations cover 409,437,920 truth cells with 809,120 explicit positive cells. Exact full-library classification of 3,884 raw candidates retains 2,826 pair rectangles. Literal canonical/physical selector replay covers 25,685,232 tuples. Only after all validation does the staging generalized state move from 5,743 to 8,569. `pre_outer_synthesis_transition.json` records this transition before a new iteration-78 outer process starts.

## Cross-registry option union

For sector `s`, check `c`, residual kind `k`, and canonical support `u`, the option registry stores every reviewed mechanism that realizes `(s,c,k,u)`. Options from different candidates may be combined only on distinct checks. A completion is accepted constructively when an explicit singleton mask `d` gives fault count `2+|d|≤10` and `u_a⊕u_b⊕d` has zero detector syndrome and nonzero logical quotient. Weight-12 and positive weight-14 pools are completion sources, never restrictions on the 360-column direct search.

For order identifiers `(i,j)`, the exact pair truth relation is

`T(i,j) = U_a(i) ∨ U_b(j) ∨ ⋁_c (A_c(i) ∧ B_c(j))`,

where `U` is a constructive unary witness and `A_c,B_c` are exact 720-bit option masks for a positive completion. No zero cell or failed completion is interpreted as absence.

## Physical selector mapping

Every retained tuple uses the deterministic priority `a_unary`, then `b_unary`, then the first listed global explicit configuration. Unary selection returns its stored logical word for both canonical and physical support. Explicit selection returns canonical `u_a⊕u_b⊕d` and physical `p_a(i)⊕p_b(j)⊕d`, with fault count from the completion. Every tuple verifies equal canonical/physical signatures, zero syndrome, nonzero quotient and at most ten faults; stream encodings and SHA-256 digests are recorded.

## Online batches and limits

After each new candidate, online generalization runs first on its two mechanisms, then cross-registry synthesis reruns over the expanded registry. Post batches retain 1,964 more regions and replay 17,679,480 tuples. Independent Cartesian products across Xerr and Zerr add no blocking power because their atom sets are disjoint; the exact no-gain lemma is stored per batch. Coupled MC-aware cross-sector synthesis is explicitly unclassified.
''')
wr('MATH_DERIVATION.md','''# Public mathematical derivation

## 1. Schedule domain

There are 864 named CNOT-edge time variables. A valid schedule is a permutation with all reviewed causal inequalities and 648 multi-check constraints. Every candidate stores all times and passes the schedule audit. An outer block is a conjunction of local order atoms; the scheduler asserts the negation of each installed conjunction.

## 2. Unrestricted direct-360 formula

For each sector there are exactly 360 primary columns: 144 data singletons and 72×3 residual elementary fault columns. For check row `r_c` and within-check permutation `π`, residual kind `k` has canonical support `u_{c,k}(π)` at the reviewed residual positions and physical suffix/prefix support `p_{c,k}(π)`. A Boolean selector is created for every primary column, with only the exact cardinality bound `Σx_j≤10`, all 72 syndrome parity equations, and a disjunction that one of 12 logical quotient parities is nonzero. The formula excludes pool, residual-pattern, check-count, and order-family restrictions.

Every SAT assignment is complete on all DIMACS variables and every clause is evaluated. Selected columns map back to names, then to canonical and physical supports. Both must have zero detector syndrome, the same nonzero logical quotient, and at most ten faults. A nonzero quotient proves stabilizer nonmembership.

## 3. Local order catalogs

Each participating weight-six check has all `6!=720` permutations. Every record contains the six qubits, all three canonical residual supports, corresponding physical supports, their detector/logical signatures, and any constructive unary witness. Canonical and physical option signatures are checked equal for all records. An atom `q<r` becomes the exact 720-bit mask of orders where `q` precedes `r`; a term is the intersection of its atom masks.

## 4. Exact pair relations and rectangles

For checks `a,b`, the exact positive truth relation is a 720×720 Boolean matrix. Unary witnesses cover a whole partner row or column. Each explicit configuration contributes a Cartesian product of two option masks. A retained term has masks `A,B` derived from its atoms and is sound only if `A×B⊆T`. Its physical construction is replayed literally for every `(i,j)∈A×B`, using the published selector priority and completion.

## 5. Multi-check GF(2) proof

For a fixed selected mechanism, each allowed order at check `c` has canonical and physical local contributions with identical signature `σ_c(o)`. With data constant `σ_0`, the exact reachable multiplicities are

`N_0(σ_0)=1`, and `N_{t+1}(z)=Σ_o N_t(z⊕σ_{c_t}(o))`.

Orders with the same signature are aggregated with their exact multiplicity. Every allowed record, every signature class, every transition, layer hash, terminal multiplicity and Cartesian product is stored. Soundness requires total multiplicity positive, invalid terminal multiplicity zero, and every terminal signature to have zero syndrome and nonzero quotient. The physical selector is the named fixed mechanism with its exact data and residual-kind mapping. This proves every tuple in a large product without sampling.

The cross-registry two-selector pilot uses shared/exclusive signature classes and meet-in-the-middle terminal products with explicit selector-choice multiplicities. No such term survived the accepted batches; this says nothing about all possible higher-dimensional constructions.

## 6. Exact semantic classification

A term is normalized by sector, ordered check list and exact 720-bit masks. Exact duplicates have identical normalized regions. `U` dominates `V` precisely when every normalized local mask/product of `V` is contained in `U`. Pair-domain union coverage is counted row by row over all 720×720 cells. Tentative classifications remain in memory; raw soundness and retained exhaustive validation finish before ledgers and installed states are finalized.

## 7. Scope

All conclusions are positive constructive soundness. Sampling, solver negatives, zero cells, positive misses and deletion countertuples never imply absence. No candidate-specific Gross UNSAT proof exists here, so no repair or branch closure is licensed.
''')
wr('TERM_LIBRARY_AND_DEDUP.md','''# Term library, deduplication and dominance

Every source candidate retains its two exact outer blocks. Generalized terms are additional conservative blocks with a physical witness for every covered local-order tuple.

For each batch, `raw_term_candidates.json` precedes `semantic_dedup_ledger.json`. The ledger exposes the exact normalized finite region and one of: duplicate old, duplicate new, dominated old, covered by the full evolving union, or retained. Installed predecessors are preserved. The batch is validated against the full state it consumed, not against a sample or only the named seed mechanisms. Pair unions are exact rowwise 720-bit unions; online multi membership is decided by an exact complement CSP over local membership classes.

Deletion witnesses address a different question. Removing one atom may expose a tuple outside the named positive relation or fixed selector, but another installed term may cover it. Therefore deletion controls do not prove installed-union minimality, global minimality, necessity, or absence.
''')
wr('DIRECT360_AND_PROOF_POLICY.md','''# Complete direct-360 and proof policy

Every actual direct sector has 360 primary columns: 144 singletons and 216 residual elementary columns, a complete assignment, all clauses checked, and assignment→column→canonical→physical replay. The weight-12/14 pools are only constructive completion resources.

An UNSAT string, timeout, signal, partial assignment, or one-sector result has no mathematical disposition. Direct absence requires a candidate-specific proof-producing run, retained DRAT, independent DRAT acceptance, generated LRAT, independent LRAT acceptance, and separate corrupt and truncated rejection controls. Both sectors must satisfy that gate before repair. Outer exhaustion requires a separately proof-producing equivalent encoding with independent proof acceptance and exact state binding.

No outer or direct sector is UNSAT in this package. The fresh PHP(6,5) valid/corrupt/truncated controls exercise the binaries only; they are not Gross proof objects.
''')
wr('ATTACK_LEDGER.md',f'''# Attacks and negative controls

The package checks complete assignments, every DIMACS clause, first-selected-primary flips, first-fault removal, schedule collisions, assignment truncation, all raw canonical/physical selectors, all retained pair tuples, exact multi DP products, zero-domain rejection, state-chain hashes, source/live bindings, manifest coverage, deterministic gzip dual hashes, and fresh valid/corrupt/truncated proof controls.

Counts: 24 assignment flips rejected, 24 fault removals rejected, 12 schedule collisions rejected, one assignment truncation rejected, {neg['counts']['retained_term_deletion_controls_total']:,} atom deletion controls, two valid proof accepts, two corrupt rejects and two truncated rejects.

Prohibited inference counters are all zero: zero truth cells, zero domains, completion misses, positive finder misses, solver negatives and deletion countertuples are never used as absence.
''')
wr('FIX-2.md','''# FIX-2: complete correction and incident disclosure

All attempts were serial and occurred in external staging. The canonical repository and round-76 source package were never mutated.

1. **Cross-registry v1:** naive full vector DP was interrupted after 508.46 s; maximum RSS 17,801,838,592 bytes, peak footprint 40,066,248,976 bytes. No state mutation.
2. **v2:** terminal DP was interrupted after 292.84 s at maximum RSS 9,262,628,864 bytes. No state mutation.
3. **v3:** broader eight-pair meet-in-the-middle was interrupted after 377.95 s after breaching the renewed memory guard; maximum RSS 20,533,542,912 bytes, peak footprint 35,033,834,240 bytes. No state mutation.
4. **v4:** safe two-pair design stayed near 1.073 GB RSS but repeated RREF made literal replay impractical; interrupted after 715.44 s. No state mutation.
5. **v5:** memoized replay reached an assertion because a retained candidate was already covered by the full evolving installed union. It failed before mutation after 149.72 s. The correction uses exact evolving-union coverage, not a per-candidate novelty assumption.
6. **v6:** computation exited successfully but post-run audit found three retained multi candidates with empty exact domains caused by contradictory local atoms. It temporarily mutated staging only to `G=8,572`, semantic `e26c650f41a653774305a17871670a32cd7481115ffd589d74025ed9cc73aa7f`. That staging result was rejected and rolled back byte-for-byte to reviewed `D=156`, `G=5,743`, registry/raw 72 and all four reviewed semantic hashes before any outer process. Canonical and source packages were untouched.
7. **v7 accepted:** candidates with zero DP total or zero local mask are rejected; the minimizer cannot seed from an empty or unsound region; selector replay is memoized; exact full-evolving-union coverage is used. It passed in 148.11 s at maximum RSS 2,111,930,368 bytes, retaining 2,826 nonempty pair terms and replaying 25,685,232 tuples.
8. **Fresh proof-control v1:** a corrupt fixture prefixed the out-of-domain literal `999999999`. `drat-trim` attempted pathological allocation and reached about 17.57 GB RSS. It was immediately TERM/KILLed. The four mathematical staging states were rehashed unchanged. The failed control and partial logs are isolated under `development/proof_control_v1_failed_oversized_literal`.
9. **Proof-control v2:** an attempted `RLIMIT_AS` pre-exec guard failed in `preexec_fn` before the checker child started. No state or proof disposition. It is isolated under `development/proof_control_v2_failed_preexec_limit`.
10. **Proof-control v3 accepted:** syntactically corrupt low-memory fixtures plus independent ten-line truncations are used with a 30-second subprocess hard limit. Fresh CaDiCaL generates the valid DRAT; drat-trim accepts it and generates LRAT; lrat-check independently accepts; both checkers reject their corrupt and truncated fixtures.

The accepted state begins only after item 7. The proof-control incidents happen after the final CEGAR state and do not mutate it. No failed/UNKNOWN/interrupted attempt is assigned mathematical meaning.
''')
wr('PROCESS_LEDGER.md','''# Process ledger

`PROCESS_LEDGER.json` contains every accepted foreground subprocess record from the 12 iterations and all cross-registry development dispositions. There are 96 accepted subprocess records, no accepted timeout or signal, and no detached load-bearing process. Each iteration is serial: fresh outer build, independent outer replay, X direct solver, Z direct solver, direct replay, candidate-exact pending append, online pending generalization, cross-registry pending synthesis, then validated four-state commit.

Development memory incidents, failed assertions, the v6 rollback, and proof-control corrections are not omitted. Raw stdout/time logs are retained under `development/`. Absolute staging paths in historical argv records identify the actual run; package verification uses package-relative live paths.
''')
wr('COMMANDS.txt','''# Reproducible entry points (replace PACKAGE and VENV with absolute paths)
VENV/python PACKAGE/src/synthesize_cross_registry.py --root PACKAGE --generalized-state PACKAGE/restart/installed_generalized_terms_iteration78.json --registry-state PACKAGE/restart/online_mechanism_registry_iteration78.json --raw-mechanisms-state PACKAGE/restart/full_raw_mechanisms_iteration78.json --dynamic-blocks-state PACKAGE/restart/dynamic_blocks_iteration78.json --output-root OUT --batch-id pre78
VENV/python PACKAGE/src/run_round78_iteration.py --iteration N --engine-root PACKAGE --work-root WORK --python VENV/python
VENV/python PACKAGE/src/build_round78_proof_controls.py --root PACKAGE
VENV/python PACKAGE/verify.py --quick --allow-unsealed
VENV/python PACKAGE/verify.py --full --allow-unsealed
VENV/python PACKAGE/src/compress_round78.py --root PACKAGE
VENV/python PACKAGE/verify.py --quick --allow-unsealed
VENV/python PACKAGE/verify.py --full --allow-unsealed
VENV/python INSTALLED/verify.py --full --repo-root REPOSITORY
VENV/python INSTALLED/verify.py --quick --repo-root REPOSITORY
''')
wr('MANIFEST.md','''# Manifest and release stages

Development full verification runs on the uncompressed staging tree and is not an accepted release gate. Deterministic gzip then writes `COMPRESSED_INVENTORY.json` with compressed and uncompressed SHA-256 plus `mtime=0`. Accepted quick and full verification run on that final compressed tree with `--allow-unsealed`; their logs remain external because inserting them would change the certified tree.

Only then are `PAYLOAD_SHA256SUMS.txt` and the non-self `SHA256SUMS.txt` created. No payload or gzip member may change after accepted preseal full verification. The sealed directory is renamed atomically from same-device external staging into the authorized target. Post-copy sealed full and quick verification use `--repo-root` for live bindings. Repository inventory and Git tripwires exclude the authorized target and must match before/after exactly.
''')
wr('FINAL_AUDIT.txt','Preseal placeholder: accepted release-gate and post-copy results are intentionally external to the immutable package. See verification/RELEASE_GATES.json and MANIFEST.md. The final user-facing audit must report their exact hashes, timings, inventory/Git tripwire results, process cleanup, and installed seal.')
dump('verification/RELEASE_GATES.json',{'schema':'round78-release-verification-gates-v1','accepted_preseal_quick':{'command':['VENV/python','PACKAGE/verify.py','--quick','--allow-unsealed'],'must_exit':0,'must_status':'PASS'},'accepted_preseal_full':{'command':['VENV/python','PACKAGE/verify.py','--full','--allow-unsealed'],'must_exit':0,'must_status':'PASS','scope':'final deterministic-gzip staging tree before seal manifests'},'package_mutation_after_accepted_preseal_full':'only PAYLOAD_SHA256SUMS.txt and SHA256SUMS.txt may be created','post_copy_sealed_full_live':{'command':['VENV/python','INSTALLED/verify.py','--full','--repo-root','REPOSITORY'],'must_exit':0,'must_status':'PASS'},'post_copy_sealed_quick_live':{'command':['VENV/python','INSTALLED/verify.py','--quick','--repo-root','REPOSITORY'],'must_exit':0,'must_status':'PASS'},'external_run_log_reason':'accepted gate logs remain outside immutable package'})
print(json.dumps({'status':'PASS','documents':len([p for p in R.iterdir() if p.is_file()]),'source_bindings_sha256':sha(R/'SOURCE_BINDINGS.json')},sort_keys=True))
