#!/usr/bin/env python3
from pathlib import Path
import argparse,collections,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();C=R/'cegar'
def load(p):return json.loads(Path(p).read_text())
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def sha_obj(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha_file(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
cs=load(C/'summary.json');gs=load(R/'classification/summary.json');dd=load(R/'classification/dedup_ledger.json');rs=load(R/'restart/restart_state.json');sc=load(R/'classification/iteration_state_chain.json');pl=load(R/'PROCESS_LEDGER.json')
rows=[]
for i in range(54,78):
 p=C/f'iter{i}';o=load(p/'iteration_outcome.json');s=load(p/'generalization/summary.json');d=load(p/'generalization/dedup_ledger.json');cand=load(p/'candidate.json');dv=load(p/'direct_verification.json')
 rows.append({'i':i,'before':o['installed_blocks_before'],'after':o['installed_blocks_after'],'layers':cand['audit']['used_layers'],'Xw':o['sector_fault_weights']['Xerr'],'Zw':o['sector_fault_weights']['Zerr'],'Xvars':dv['sectors']['Xerr']['formula_summary']['variables'],'Xclauses':dv['sectors']['Xerr']['formula_summary']['clauses'],'Zvars':dv['sectors']['Zerr']['formula_summary']['variables'],'Zclauses':dv['sectors']['Zerr']['formula_summary']['clauses'],'cats':s['participating_catalogs'],'pairs':s['structural_pair_relations'],'raw':s['raw_term_candidates'],'dup_old':d['duplicate_old'],'dup_new':d['duplicate_new'],'dom_old':d['dominated_old'],'dom_new':d['dominated_new'],'ret':s['retained_increment'],'lit':s['literal_retained_tuple_replays'],'fac':s['factorized_symbolically_proved_tuples'],'G':s['installed_generalized_after'],'D':o['dynamic_blocks_after'],'schedule':cand['schedule_sha256']})
# Main machine result.
result={'schema':'circdist-gross-online-generalizing-round76-result-v1','date':'2026-08-29','status':'PASS','verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED','claim':'twenty-four fully closed exact online CEGAR candidates with immediate sound generalization; no Gross-root branch closure','licensed_start':{'iteration':54,'unstarted':True,'installed_blocks':7008,'round63_unary':1440,'round62':20,'round69_generalized':4740,'round72_generalized':566,'round74_generalized':134,'merged_generalized':5440,'dynamic_exact':108,'registry':24,'exploratory_round63_pair':0,'source_seal_file_sha256':'321eb6ccaae3795e866b0cad409571b35dff7b7b17a84c614c8ab1a23b8e498c','review_sha256':'a6ee9d2c18291f3474672fb13682e6720a0f2d313da138da26397e67ccd48cc8'},'online_result':{'iteration_range':[54,77],'fully_closed_candidates':24,'outer_sat':24,'direct_sector_sat':48,'complete_assignment_clause_replays':48,'raw_canonical_physical_replays':48,'candidate_exact_blocks_added':48,'raw_generalization_candidates':gs['raw_term_candidates'],'retained_generalization_terms':gs['retained_increment'],'duplicate_old':dd['duplicate_old'],'duplicate_new':dd['duplicate_new'],'dominated_old':dd['dominated_old'],'dominated_new':dd['dominated_new'],'literal_pair_tuple_replays':gs['literal_retained_tuple_replays'],'factorized_symbolically_proved_multi_tuples':gs['factorized_symbolically_proved_tuples'],'factorized_validation_is_universal_not_sampling':True,'retained_deletion_controls':gs['retained_deletion_controls'],'accepted_absence_proofs':0,'repair_entered':False,'outer_exhaustion_proof':False,'branch_closed':False,'root_closed':False},'frozen_restart':{'next_iteration':78,'unstarted':True,'installed_blocks':rs['total_installed_blocks'],'merged_generalized_terms':rs['counts']['merged_generalized_blocks'],'round76_retained_terms':rs['counts']['round76_generalized_blocks'],'dynamic_exact_blocks':rs['counts']['dynamic_blocks_total'],'registry_entries':72,'state_semantic_sha256':rs['state_semantic_sha256']},'limits':{'D_star_Gross':'remains in {11,12}','candidate_specific_unsat_proofs_present':False,'outer_exhaustion_proof_present':False,'zero_truth_cells_are_absence':False,'positive_finder_or_pool_misses_are_absence':False,'deletion_countertuples_are_absence':False,'fresh_independent_review_required':True},'restart_license':'RESTART_LICENSE.md','self_contained_verifier':'verify.py'}
dump(R/'RESULT.json',result);(R/'VERDICT.txt').write_text('MATERIAL-CHECKED-PROGRESS-NOT-CLOSED\n')
# Iteration and classification ledgers.
lines=['# Iteration ledger','','Every row is one completed transaction: fresh outer -> independent outer replay -> both direct sectors -> full assignment/raw replay -> two candidate-exact blocks -> exact online generalization -> retained validation -> finalized dedup/install.','','| iter | blocks before→after | layers | X/Z faults | X vars/clauses | Z vars/clauses | catalogs | pair rels | raw→retained | dup old/new | dominated old/new | literal tuples | factorized tuples | schedule SHA-256 |','|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|']
for x in rows:lines.append(f"| {x['i']} | {x['before']}→{x['after']} | {x['layers']} | {x['Xw']}/{x['Zw']} | {x['Xvars']}/{x['Xclauses']} | {x['Zvars']}/{x['Zclauses']} | {x['cats']} | {x['pairs']} | {x['raw']}→{x['ret']} | {x['dup_old']}/{x['dup_new']} | {x['dom_old']}/{x['dom_new']} | {x['lit']:,} | {x['fac']:,} | `{x['schedule']}` |")
lines+=['',f"Final unstarted iteration: **78**, with **{rs['total_installed_blocks']:,}** installed blocks.",'','No row contains direct UNSAT, accepted absence, repair entry, outer UNSAT, or branch closure.']
(R/'ITERATION_LEDGER.md').write_text('\n'.join(lines)+'\n')
cl=['# Classification ledger','',f"Across iterations 54–77, {gs['raw_term_candidates']} exact raw candidates were built and {gs['retained_increment']} retained.",'','| quantity | count |','|---|---:|']
for k in ['participating_catalogs','local_order_records','structural_pair_relations','structural_pair_cells_represented','positive_pair_relations','unary_only_pair_relations','positive_pair_configurations','positive_pair_cells','positive_finder_misses','multi_check_exact_relations','pair_terms_generated','multi_check_terms_generated','raw_term_candidates','retained_increment','literal_retained_tuple_replays','factorized_symbolically_proved_tuples','pair_domain_library_relative_new_tuples','retained_deletion_controls']:cl.append(f"| {k} | {gs[k]:,} |")
cl += ['', 'Semantic dispositions:', '', f"- duplicate-old: {dd['duplicate_old']}; duplicate-new: {dd['duplicate_new']}", f"- dominated-old: {dd['dominated_old']}; dominated-new: {dd['dominated_new']}", f"- retained pair rectangles: {gs['retained_relation_kinds']['positive_pair_rectangle']}", f"- retained multi-check exact fixed-selector domains: {gs['retained_relation_kinds']['multi_check_exact_selected_mechanism']}", '', 'The 793 positive-finder misses and every zero conservative truth cell carry no absence meaning.']
(R/'CLASSIFICATION_LEDGER.md').write_text('\n'.join(cl)+'\n')
# README.
readme=f'''# Gross exact online-generalizing CEGAR — round 76

Date: 2026-08-29  
Verdict: **MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**

This sealed proposer package continues the exact unrestricted Gross-code search from the round-75 reviewed, unstarted iteration-54 frontier. It completes twenty-four online iterations, 54 through 77, in strict serial foreground processes. It modifies no canonical claim, scheduler, protocol, generated view, review, or predecessor artifact. It supplies positive checked progress and freezes iteration 78; it does not prove physical absence, outer exhaustion, or either branch of the Gross root.

## Bound start

- round-74 package `SHA256SUMS.txt` SHA-256: `321eb6ccaae3795e866b0cad409571b35dff7b7b17a84c614c8ab1a23b8e498c`;
- round-75 exact review SHA-256: `a6ee9d2c18291f3474672fb13682e6720a0f2d313da138da26397e67ccd48cc8`;
- exact reviewed unstarted state: `1,440 + 20 + 4,740 + 566 + 134 + 108 = 7,008` blocks, `G=5,440`, `D=108`, registry `24`;
- exploratory round-63 pair clauses installed: **0**.

## Result

All 24 fresh unrestricted outer queries are SAT. Every stored schedule has all 864 named CNOT edges, all 648 measurement-collision constraints, one edge once, one gate per qubit-time, compressed idle layers, and global X/Z interleaving. Each formula and fixed schedule has a separate independent reconstruction.

Both direct sectors were generated unconditionally for every candidate. All 48 formulas are SAT. Their actual primary domain is exactly **360 elementary columns = 144 data singletons + 216 residual elementary-fault columns** per sector. The 1,884-member weight-12 pool is not the primary domain; it binds quotient representatives and positive completions. Every complete assignment satisfies every DIMACS clause and raw-reconstructs canonical and physical zero-detector-syndrome, stabilizer-nonmember mechanisms of nonzero logical quotient and at most ten elementary faults.

The run preserves 48 candidate-exact blocks. Immediate online generalization constructs all participating `6!=720` local-order catalogs, exact positive pair completions, and exact joint GF(2) relations. From {gs['raw_term_candidates']} raw candidates, semantic filtering against the full current library retains {gs['retained_increment']}. Every retained pair tuple was literally visited and physically replayed ({gs['literal_retained_tuple_replays']:,} tuples). The two retained multi-check domains cover {gs['factorized_symbolically_proved_tuples']:,} tuples by universal factorization over every allowed local record, explicit canonical=physical signature identity, all exact DP states/transitions, fixed selector construction, and exact product counts.

The unstarted restart is iteration 78:

```text
1,440 unary + 20 round-62 + 4,740 round-69 + 566 round-72
+ 134 round-74 + 303 round-76 generalized + 156 dynamic exact
= 7,359 installed blocks; G=5,743; D=156; registry=72.
```

No direct sector was UNSAT, so no candidate-specific Gross DRAT/LRAT absence proof exists and repair was never licensed. No outer UNSAT proof exists. `D*_Gross` remains in `{{11,12}}`.

## Audit map

- `RESULT.json`: machine-readable claim boundary and restart hashes.
- `MATH_DERIVATION.md`: definitions, formulas, direct completeness, catalogs, selectors, DP proof, and limitations.
- `ITERATION_LEDGER.md`: all 24 online transactions.
- `CLASSIFICATION_LEDGER.md`: aggregate catalog/relation/term/tuple counts.
- `cegar/iter*/`: outer formulas, schedules, complete direct CNFs/assignments, raw mechanisms, and online objects.
- `classification/round76_retained_terms.json.gz`: all retained terms and deletion controls.
- `classification/installed_generalized_terms.json.gz`: complete iteration-78 generalized library.
- `cegar/dynamic_blocks.json.gz`: complete iteration-78 dynamic state.
- `restart/`: exact reviewed iteration-54 and proposer iteration-78 restart files.
- `controls/round76_proof_checker/`: fresh valid and corrupt DRAT/LRAT toolchain controls; not Gross proofs.
- `SOURCE_BINDINGS.json`, `PROCESS_LEDGER.json`, `FIX-2.md`: source, process, and incident audit.
- `COMPRESSED_INVENTORY.json`: deterministic gzip compressed/uncompressed dual hashes.
- `verify.py`: quick and full self-contained replay.
- `SHA256SUMS.txt`: external non-self package seal.

## Verification

```bash
python3 -m venv /tmp/circdist-r76-review-venv
/tmp/circdist-r76-review-venv/bin/pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 /tmp/circdist-r76-review-venv/bin/python verify.py --quick
PYTHONDONTWRITEBYTECODE=1 /tmp/circdist-r76-review-venv/bin/python verify.py --full
```

Add `--repo-root /absolute/path/to/Claim-Centered-Research-Graph` to verify live source-package, review, protocol, scheduler, and node bindings. The proposer verifier is reproducibility evidence, not independent review. **Fresh independent exact review is required before canonical use or restart.**
'''
(R/'README.md').write_text(readme)
# Direct policy.
(R/'DIRECT360_AND_PROOF_POLICY.md').write_text('''# Complete direct-360 and proof policy

For each sector the primary selection variables correspond exactly to 360 elementary fault columns: 144 data singletons and three normalized residual hook columns for each of 72 checks. The 1,884 weight-12 words are used only for quotient-basis binding and positive completions. No pool, residual pattern, residual-check count, local-order family, or logical-weight restriction occurs in the direct query.

Every SAT result is retained only after a complete `1..n` assignment, evaluation of every DIMACS clause, assignment-to-column reconstruction, canonical and physical support replay, zero detector syndrome, equal nonzero 12-bit logical quotient, stabilizer nonmembership, and fault count at most ten.

An UNSAT string, timeout, signal, or partial proof has no mathematical disposition. Direct absence would require a candidate-specific DRAT proof, independent DRAT acceptance, generated LRAT, independent LRAT acceptance, and corrupt/truncated rejection controls. Both sectors must meet that gate before arbitrary-round repair. No candidate in this package reaches it. The valid/corrupt checker fixtures test only the toolchain and are not Gross proofs.
''')
# Dedup policy.
(R/'TERM_LIBRARY_AND_DEDUP.md').write_text(f'''# Term library and semantic deduplication

A generalized term is a sector plus a finite conjunction of within-check order atoms. For each constrained check, the atoms determine an exact subset of its 720 local orders. Its semantic key is the sector together with those exact 720-bit masks; omitted checks have the all-720 mask.

Terms are equal exactly when all masks agree. A sound term `U` dominates `V` exactly when `region(V) subseteq region(U)`. Every comparison uses the full installed library of 5,440 inherited terms plus terms retained earlier in round 76. Installed predecessor terms are never removed. Candidate-exact blocks are preserved independently of generalized coverage.

Aggregate disposition: {gs['raw_term_candidates']} raw; {dd['duplicate_old']} duplicate-old; {dd['duplicate_new']} duplicate-new; {dd['dominated_old']} dominated-old; {dd['dominated_new']} dominated-new; {gs['retained_increment']} retained.

Tentative classification occurs only in memory after raw candidate soundness is established. The public dedup ledger and generalized/registry state are written only after every retained pair tuple has been literally replayed or every retained multi domain has passed its factorized universal proof.

Deletion controls prove only atom minimality relative to the candidate positive relation or fixed selector. They do not prove installed-union minimality, global physical-mechanism minimality, or absence. A countertuple may already be covered by another installed term.
''')
# Attack ledger.
(R/'ATTACK_LEDGER.md').write_text('''# Attacks, negative controls, and prohibited inferences

The package attacks each positive result through complete assignment parsing, every-clause evaluation, first-selected-primary flips, first-fault removal, schedule collision mutations, assignment truncation, retained atom deletions, source-state hash links, semantic dedup against the full current library, and valid/corrupt DRAT/LRAT controls.

The following never prove absence: zero conservative pair cells; failed positive completions; weight-12 or weight-14 misses; positive-library misses; deletion countertuples; SAT frequency; or a candidate's selected-mechanism failure outside a retained region. The 15,874 exploratory round-63 pair clauses remain forbidden and installed at zero.

No timeout, UNKNOWN, solver signal, one-sector result, or checker fixture is promoted into a mathematical verdict. Deletion controls establish only minimality of the named candidate relation or fixed selector. They do not establish installed-union minimality, global physical-mechanism minimality, or absence.
''')
# Process/FIX2.
(R/'PROCESS_LEDGER.md').write_text(f'''# Foreground process ledger

`PROCESS_LEDGER.json` contains {pl['candidate_records']} load-bearing records in strict time order: 24 outer builds, 24 independent outer replays, 48 CaDiCaL direct runs, 24 direct raw replays, 24 exact-block appends, and 24 online generalizations. The 48 solver records exit 10 (SAT); the other 120 exit 0. None timed out, received SIGTERM/SIGKILL, detached, or overlapped the next load-bearing stage.

The sole nonzero author attempt was a read-only source-package quick check with live bindings. It exited 1 on the scheduler snapshot because the live scheduler had expected post-round-74/75 drift. No research state was touched. The sealed package was then verified without the stale live comparison, and the reviewed iteration-54 states were separately rebound to their exact hashes.
''')
(R/'FIX-2.md').write_text('''# FIX-2 incident and process disclosure

All computation was foreground and serial. No detached solver, driver, verifier, or generalizer was launched or handed off.

## Corrected/nonzero attempt

The first round-74 `verify.py --quick --repo-root ...` call returned exit 1 at `operations/circdist/SCHEDULER.yaml`. This is the expected live scheduler drift already described by the round-75 review, not a seal or mathematical-input failure. The exact log and run record are retained under `preflight/`. It was followed by a successful sealed offline quick verification and an explicit independent binding of the exact reviewed iteration-54 state. No candidate or installed state existed yet, so the failed read-only check mutated nothing.

## Successful candidate processes

All 168 load-bearing child runs are in `PROCESS_LEDGER.json`. They are serial; 120 exit zero and 48 CaDiCaL runs exit ten. Timeout and signal counts are zero. Exact per-stage logs and run records survive under each iteration.

## Proof-control expected failures

The corrupted/truncated DRAT and LRAT controls exit one with `NOT VERIFIED` by design. They are recorded as successful negative controls, not computation incidents or Gross proof objects.

## Cleanup contract

Before final response, all solver/generalizer/verifier processes, the temporary venv, scratch package, and pointer are removed after atomic installation and post-copy verification. The package records the final process and residue scans.
''')
# Restart/review.
(R/'RESTART_LICENSE.md').write_text(f'''# Exact restart license

This proposer package freezes an **unstarted iteration 78** frontier:

```text
1,440 reviewed unary
+   20 round-62
+4,740 reviewed round-69 generalized
+  566 reviewed round-72 generalized
+  134 reviewed round-74 generalized
+  303 round-76 proposer generalized
+  156 exact dynamic
=7,359 installed blocks; registry=72.
```

The exact files and semantic hashes are in `restart/restart_state.json`. Continuation is licensed only after fresh independent exact review accepts this package and all 303 new generalized terms. A continuation must use a fresh outer process; generate both actual unrestricted 360-primary sectors for every SAT schedule; retain complete assignments; replay canonical and physical mechanisms; preserve candidate-exact blocks; validate retained generalized domains before final dedup/install; treat UNKNOWN/timeouts/signals as no conclusion; require candidate-specific accepted DRAT/LRAT for direct absence; and enter arbitrary-round repair only after checked absence in both sectors.

This is not canonical installation, root closure, exhaustion, or evidence for either `D*=11` or `D*=12`.
''')
(R/'REVIEW_LICENSE.txt').write_text('FRESH INDEPENDENT EXACT REVIEW REQUIRED BEFORE CANONICAL USE OR ITERATION-78 RESTART.\nThis proposer package licenses no claim rewrite, route change, level change, repair entry, D* narrowing, or root closure.\n')
# Commands.
(R/'COMMANDS.txt').write_text('''# Source sealed quick verification
PYTHONDONTWRITEBYTECODE=1 $VENV/bin/python source-package/verify.py --quick

# One fresh serial online iteration (author loop used N=54..77)
PYTHONDONTWRITEBYTECODE=1 $VENV/bin/python src/run_online_iteration.py --iteration N --engine-root PACKAGE --work-root PACKAGE --python $VENV/bin/python

# Quick and full package verification
PYTHONDONTWRITEBYTECODE=1 $VENV/bin/python verify.py --quick
PYTHONDONTWRITEBYTECODE=1 $VENV/bin/python verify.py --full
PYTHONDONTWRITEBYTECODE=1 $VENV/bin/python verify.py --full --repo-root /absolute/path/to/Claim-Centered-Research-Graph

# External seal digest
shasum -a 256 SHA256SUMS.txt
''')
# Mathematical derivation.
math=f'''# Mathematical derivation and exact finite certificates

This document exposes the definitions, equations, encodings, selector maps, finite catalogs, DP construction, state transitions, controls, and scope limits needed to audit the result. It does not claim to expose private hidden chain-of-thought.

## 1. Gross incidence and schedule space

Let `G=Z_12 x Z_6`, with `g(i,j)=6i+j`, and

```text
A={{(3,0),(0,1),(0,2)}},  B={{(0,3),(1,0),(2,0)}}.
```

For each `g in G`, the X and Z check supports are

`X_g=(g+A) union (72+g+B)` and `Z_g=(g-B) union (72+g-A)`.

There are 72 checks of each type, each weight six, 144 data qubits, 864 uniquely named CNOT edges, and 648 X/Z check pairs of overlap two. The replayer reconstructs `rank(H_X)=rank(H_Z)=66`, commutation, and `k=144-66-66=12`.

A schedule assigns an integer time `t(e) in {{0,...,863}}` to each edge. The outer formula enforces: all six edges of every check are distinct; all six incident edges of every data qubit are distinct; each overlap pair has the same X-before-Z comparison on both shared qubits; and neither all-X-before-all-Z nor all-Z-before-all-X holds. Relabeling used times in increasing order preserves every equality/order predicate, so post-solve idle compression is lossless.

The exact outer assertion base has 4,398 assertions before installed sound blocks. At iteration `r`, it appends 1,440 reviewed unary blocks, 20 round-62 blocks, every term in the current generalized library, and every current dynamic exact block. Every next solve consumes exactly the state installed by the previous completed transaction.

## 2. Canonical residuals and physical hooks

For an earliest-first order `o=(q0,...,q5)`, the three canonical residual supports and physical suffix supports are

```text
R0={{q0,q1}},       P0={{q2,q3,q4,q5}},
R1={{q3,q4,q5}},    P1={{q3,q4,q5}},
R2={{q4,q5}},       P2={{q4,q5}}.
```

For kind zero, `P0 xor R0` is the complete stabilizer row; kinds one and two are identical. Hence canonical and physical contributions have identical detector syndrome and identical 12-bit logical quotient.

## 3. Complete unrestricted direct formula

Each sector has exactly 360 primary selection variables: 144 singleton data columns plus `72*3=216` residual elementary-fault columns. The reviewed 1,884-word logical pool is not the primary domain.

For primary variables `x_j`, `j=0,...,359`, the query is

`sum_j x_j <= 10`,

`xor_{{j : detector bit b of c_j = 1}} x_j = 0` for all 72 detector bits, and

`OR_{{r=0}}^{{11}} xor_{{j : <c_j,L_r>=1}} x_j = 1`.

Tseitin chains encode parity and a prefix sequential counter encodes cardinality. There is no pool, hook-count, residual-pattern, logical-weight, or within-check-order-family restriction. Every solver log supplies every variable `1..n` exactly once. The checker evaluates every DIMACS clause, maps selected variables to column records, reconstructs canonical and physical supports, and requires zero syndrome, equal nonzero logical quotient, stabilizer nonmembership, and at most ten faults.

All 48 candidate-sector formulas return SAT and pass this replay. Therefore none licenses direct absence or repair.

## 4. Candidate-exact sound blocks

For a selected residual support `S` in check row `Q`, the preserving atoms are all cross-boundary comparisons `S<O` for prefix kind zero or `O<S` for suffix kinds one/two, where `O=Q\\S`. Singleton columns add no schedule atom. If all atoms hold, every selected column and hence its nontrivial zero-syndrome XOR is unchanged. Negating their conjunction is a sound outer exclusion. All 48 source blocks remain installed even when generalized terms cover their source schedules.

## 5. Complete local-order catalogs

For every participating `(sector,check)`, the package materializes all `6!=720` permutations. Every record contains: order ID and qubits; all three canonical residual and physical suffix supports; their exact 84-bit signature (72 syndrome + 12 logical bits); and, where applicable, a constructive unary completion. The checker verifies canonical=physical signature identity for every option. Round 76 contains {gs['participating_catalogs']} catalogs and {gs['local_order_records']} order records.

## 6. Exact positive pair relations and selectors

For checks `a,b` and local order IDs `i,j`, define

`T_ab(i,j)=U_a(i) OR U_b(j) OR E_ab(i,j)`.

`U` carries an explicit unary selector. `E` is the exact union of stored positive two-hook configurations, each with explicit residual kinds, supports, singleton completion, fault count at most ten, zero syndrome, and nonzero quotient. Every one of the 720 rows is stored as a 720-bit integer, with separate explicit-good-good rows.

A retained pair antecedent induces masks `A,B` and is sound exactly when for every `i in A`, `B subseteq T_ab(i,*)`. Its selector is deterministic: choose the `a` unary witness if available; else the `b` unary witness; else the first stored explicit pair configuration covering `(i,j)`. The replay reconstructs both 144-bit canonical and physical supports for every retained tuple, verifies signature equality and nontriviality, and hashes the complete tuple stream. Exactly {gs['literal_retained_tuple_replays']:,} retained pair tuples were literally visited.

Positive-finder misses and zero cells say only that this conservative positive library supplied no selector; they do not prove physical absence.

## 7. Exact multi-check GF(2) universal proof

For a retained fixed-selector mechanism, each constrained check `c` has an allowed local-order mask `A_c`. Every allowed order is materialized with its canonical and physical local contributions and their identical signature `sigma_c(o)`. Let `d` be the signature of fixed singleton data faults. The exact joint DP is

`S_0={{d}}`,

`S_r={{s xor sigma_{{c_r}}(o) : s in S_{{r-1}}, o in A_{{c_r}}}}`.

Induction is exact: every transition appends a real allowed local order, and every real allowed prefix has its predecessor and last transition. Merging equal GF(2) signatures loses no acceptance information because terminal validity depends only on the signature. The package records every signature class, allowed-order intersection, layer state count, sorted-state hash, and terminal set. Every terminal has zero syndrome and nonzero logical quotient. Canonical=physical signature identity lifts the conclusion to both supports.

The fixed selector uses the same recorded singleton set and same selected residual kinds for every tuple. Fault count is constant. The domain size is exactly `product_c |A_c|`; the two retained domains total {gs['factorized_symbolically_proved_tuples']:,} tuples. Stored sample tuples illustrate the construction but carry no universal burden.

## 8. Transaction and semantic state safety

The process order is:

```text
fresh outer build/solve
-> independent outer replay
-> complete Xerr solve
-> complete Zerr solve
-> complete clause/canonical/physical replay
-> append both candidate-exact blocks
-> exact catalogs, relations, raw candidates and deletion controls
-> tentative semantic classification in memory
-> exhaustive retained pair replay / multi universal proof
-> finalized dedup ledger and atomic generalized/registry writes
-> next fresh outer process.
```

No tentative semantic decision mutates installed state. `classification/iteration_state_chain.json` supplies exact before/after hashes for all 24 transitions.

## 9. Deletion controls and limits

Forward and reverse atom deletion is tested against the candidate positive pair relation or fixed-selector DP. A retained atom has an explicit exposed countertuple when removed. This proves only minimality of that named candidate relation/selector. It does not prove that the installed union loses coverage, that no different selector works, global physical-mechanism minimality, or absence.

The 15,874 exploratory round-63 pair clauses are never installed. Weight-12/14 misses, positive-library misses, zero pair cells, and countertuples have zero absence weight. Only checked direct absence in both sectors could license the arbitrary-round repair stage; only a checked repair result could classify that candidate; only proved outer exhaustion could support a universal interleaved ceiling. None occurs here.

## 10. Exact result boundary

The 24 candidates add 48 exact blocks and {gs['retained_increment']} generalized terms. The unstarted iteration-78 state is `G=5,743`, `D=156`, registry `72`, total `7,359`. There are no candidate-specific Gross UNSAT proofs and no outer proof. Thus `D*_Gross` remains in `{{11,12}}`; the package is material checked progress, not closure.
'''
(R/'MATH_DERIVATION.md').write_text(math)
# Manifest explanation and final audit placeholder.
(R/'MANIFEST.md').write_text('''# Seal convention

`SHA256SUMS.txt` is the accepted external root seal. It contains every package file except itself, each exactly once, with repository-independent relative paths and SHA-256 of physical stored bytes. `PAYLOAD_SHA256SUMS.txt` excludes itself, `SHA256SUMS.txt`, and mutable verification-output slots, and acts as a non-self payload manifest. `COMPRESSED_INVENTORY.json` separately binds compressed and uncompressed bytes for every deterministic gzip file. No basename filtering is used.
''')
(R/'FINAL_AUDIT.txt').write_text('PRESEAL VERIFICATION PENDING\n')
print(json.dumps({'docs_written':15,'result':result},sort_keys=True))
