#!/usr/bin/env python3
from pathlib import Path
import argparse,collections,datetime,gzip,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve()
def data(p):
 p=Path(p)
 if not p.exists() and Path(str(p)+'.gz').exists():p=Path(str(p)+'.gz')
 b=p.read_bytes();return gzip.decompress(b) if p.suffix=='.gz' else b
def load(p):return json.loads(data(p))
def put(name,s):(R/name).write_text(s.rstrip()+'\n')
res=load(R/'RESULT.json');ce=load(R/'cegar/summary.json');cl=load(R/'classification/summary.json');xr=load(R/'cross_registry/summary.json');wh=load(R/'whole_registry/hitting_synthesis/summary.json');rs=load(R/'restart/restart_state.json');sb=load(R/'SOURCE_BINDINGS.json');chain=load(R/'cegar/iteration_state_chain.json')['iterations'];proofs=load(R/'whole_registry/hitting_synthesis/factorized_selector_proofs.json')['proofs'];pc=load(R/'controls/round80_proof_checker/summary.json');nc=load(R/'controls/negative_controls.json')
fmt=lambda n:f'{n:,}'
rows='\n'.join(f"| {x['iteration']} | {x['outer_status']} | {x['direct_sector_statuses']['Xerr']} | {x['direct_sector_statuses']['Zerr']} | {x['increments']['online_generalized']} | {x['increments']['cross_registry']} | 2 | {x['after_counts']['generalized']} | {x['after_counts']['dynamic']} | {x['after_counts']['registry']} | {x['after_counts']['total_blocks']} |" for x in chain)
put('VERDICT.txt','MATERIAL-CHECKED-PROGRESS-NOT-CLOSED')
put('README.md',f'''# Gross whole-registry exact proposer, Round 80

This is a self-contained proposer package. It binds the freshly reviewed, unstarted iteration-90 state and adds a broader exact multi-mechanism whole-registry construction before running twelve strict-serial CEGAR candidates (iterations 90 through 101).

## Verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** No load-bearing branch closed; no candidate-specific or outer UNSAT certificate was accepted; `D*_Gross` remains in `{{11,12}}` and did not change. Fresh independent review is required. No canonical node, scheduler, protocol, review, or generated view was edited by this proposer.

## Exact transition

- Licensed start: G=10,595, D=180, registry/raw=96, installed blocks=12,235, next iteration 90.
- Pre-outer whole-registry synthesis: +24 strict installed-union expansions, G=10,619, first outer total=12,259.
- CEGAR: 12 outer SAT schedules, 24 complete direct-360 SAT assignments, +{ce['online_generalized_terms_added']} online terms, +{ce['post_outer_cross_registry_terms_added']} cross-registry terms, +24 candidate-exact blocks.
- Frozen restart: G={rs['counts']['generalized']:,}, D={rs['counts']['dynamic']}, registry/raw={rs['counts']['registry']}, installed blocks={rs['counts']['total_blocks']:,}, fresh unstarted iteration 102.

Run `python verify.py --quick --repo-root /path/to/Claim-Centered-Research-Graph` for structure, hashes, ledgers, controls, and live bindings. Run `python verify.py --full --repo-root ...` for fresh outer formula reconstruction, complete direct formula/assignment replay, every raw mechanism replay, all retained literal/factorized term domains, and independent whole-registry selector replay.
''')
put('MATH_DERIVATION.md',f'''# Exact mathematical derivation

For every physical check `c`, let `Ω_c=S_6`; therefore `|Ω_c|=720`. A generalized term `T` is a conjunction of strict local order atoms. Its exact local domain is

`M_c(T) = {{o in Ω_c : every atom of T on c holds in o}}`.

Masks are 720-bit integers rebuilt from all `6!` permutations. Empty masks are rejected before classification.

For checks `a,b`, the reviewed raw mechanism family induces the exact positive relation

`R_ab = (U_a × Ω_b) ∪ (Ω_a × U_b) ∪ ⋃_r (A_r × B_r)`,

where unary sets and every explicit rectangle carry constructive canonical and physical raw selectors. The pair reconstruction used 96 raw mechanisms, 138 catalogs ({fmt(99_360)} order records), 459 residual options, 1,557 pair relations and {fmt(wh['pair_truth_positive_cells'])} positive truth cells.

For a star with center `c`, leaves `L`, and candidate box `∏ M_j`, define

`G_l = {{o_c in M_c : for all o_l in M_l, (o_c,o_l) in R_cl}}`.

The star is sound exactly when `M_c ⊆ ⋃_(l∈L) G_l`. In fixed leaf priority, make disjoint partitions

`P_l = M_c ∩ G_l \ ⋃_(k before l) G_k`.

For each `(o_c,o_l) ∈ P_l×M_l`, literal replay reconstructs an explicit raw selector and checks canonical/physical syndrome identity, nontrivial logical signature and fault weight at most 10. Other leaves are independent, so that selector proves

`|P_l| |M_l| ∏_(k≠l)|M_k|`

full tuples. Summing over the disjoint center partition gives exactly `∏_j |M_j|`. The 24 retained terms replay {fmt(wh['literal_pair_cells_replayed'])} literal pair cells and prove {fmt(wh['complete_factorized_product_tuples'])} complete product tuples. Every one also has an exact Z3 witness satisfying the new term while avoiding the full evolving installed union; hence the union grew strictly 24 times.

Dominance and equality are semantic: sector plus every exact local-order mask, never text syntax. A term dominates another only if its check support and local masks contain the other's full domain. Deletion countertuples certify only the named fixed star/relation atom test. Zero cells, positive misses, budget exclusions, sampled domains, and deletion tests are never absence evidence.

Each outer formula is rebuilt in a fresh process from 1,440 unary blocks, 20 round-62 blocks, the exact committed generalized library, and candidate-exact dynamic blocks. It names all 864 edges and independently audits all 648 MC overlaps, legality, global interleaving, and geometry. The stored SMT2 byte stream and fixed schedule are replayed independently.
''')
put('WHOLE_REGISTRY_SYNTHESIS.md',f'''# Whole-registry synthesis and comparison

Four approaches were compared before the outer loop.

1. Installed-union prime implicates can be strong, but exact enumeration/proof extraction over 144 local checks was less feasible under the memory limit.
2. Multi-selector BDD/SAT universal projection is general, but a monolithic diagram risks obscuring raw selector provenance and proof memory.
3. Factorized GF(2) relations compress signatures well, but signature equality alone does not supply a physical selector for every retained tuple.
4. Exact star hitting-cuts over the complete raw pair truth preserve constructive selectors, permit an exhaustive/disjoint center partition, and support compact full-product proofs.

The fourth method was selected. Search examined {fmt(wh['star_seed_attempts'])} star seeds. Classification: raw sound={fmt(wh['raw_sound_star_candidates'])}; zero-domain rejected={fmt(wh['initial_zero_domain_attempts'])}; unsound={fmt(wh['initial_unsound_attempts'])}; non-synergistic={fmt(wh['initial_not_synergistic_attempts'])}; dominated-old={wh['classification_counts']['dominated_old']}; covered by the full evolving union={wh['classification_counts']['covered_by_full_evolving_union']}; retained strict expansions=24; sound but not selected under the deterministic packaging budget={wh['classification_counts']['sound_not_selected_after_deterministic_packaging_budget']}. Budget exclusions are positive sound candidates, not absence results.

All 24 strict-outside witnesses are complete 144-check local-order assignments. Every stored selector stream is deterministic and binds center order, leaf order, canonical support, physical support, and fault count. See `whole_registry/hitting_synthesis/factorized_selector_proofs.json(.gz)`.
''')
put('DIRECT360_AND_PROOF_POLICY.md',f'''# Complete direct-360 sectors and proof gate

For each SAT outer schedule, both sectors are rebuilt with the unrestricted primary domain: 72 checks, 144 singleton data columns, 216 elementary residual columns, 360 primary selection variables per sector, and W=10. There is no pool, residual-pattern, check-count, or within-check order-family restriction.

A SAT result is retained only with a complete DIMACS assignment, all-clause replay, canonical mechanism replay, physical mechanism replay, zero physical syndrome, nontrivial logical action and fault count at most 10. All 24 sector queries passed.

For every candidate, the branch with the greatest complete CNF clause count (then variable count and label) receives a candidate-specific direct-absence attempt. Iteration 90 enabled proof output even though the result was SAT, producing a {fmt(load(R/'cegar/iter90/direct_absence_attempt.json')['proof_output_bytes'])}-byte non-certificate trace; later SAT attempts omit such traces. Any UNSAT result would have required fresh DRAT generation, independent DRAT acceptance with LRAT emission, independent LRAT acceptance, and valid/corrupt/truncated controls before repair. No candidate returned UNSAT, so no absence was accepted and repair was never entered.

The PHP(6,5) toolchain control independently demonstrates one generated UNSAT proof, valid DRAT acceptance, generated LRAT acceptance, and rejection of two corrupt and two truncated proofs. These controls validate the checker path only; they are not Gross proofs.
''')
put('TERM_LIBRARY_AND_DEDUP.md',f'''# Term library, exact domains, and deduplication

Round 80 added 24 pre-outer whole-registry terms, {ce['online_generalized_terms_added']} online terms, and {ce['post_outer_cross_registry_terms_added']} post-candidate cross-registry terms. Final G={rs['counts']['generalized']:,}.

Online retained validation covers {fmt(cl['literal_retained_tuple_replays'])} literal tuples and {fmt(cl['factorized_symbolically_proved_tuples'])} factorized tuples. Cross-registry retained validation covers {fmt(xr['literal_pair_tuples_replayed'])} literal pairs. Whole-registry validation adds {fmt(wh['literal_pair_cells_replayed'])} literal pair selectors and {fmt(wh['complete_factorized_product_tuples'])} factorized full tuples.

Every candidate is normalized to exact per-check 720-bit masks. Duplicate and dominance tests run against the full evolving library. A retained term has a nonempty exact product domain and explicit constructive selectors. Relation failures and deletion countertuples have only their explicitly tested scope.
''')
put('ITERATION_LEDGER.md',f'''# Atomic iteration ledger

Every row is a completed commit. Pending states are absent from this table.

| iter | outer | Xerr direct | Zerr direct | online + | cross + | exact + | G | D | R/raw | total |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
{rows}

Totals: outer SAT=12, direct SAT=24, UNSAT/UNKNOWN/TIMEOUT=0, accepted absence proofs=0, repair entries=0. Each next process consumed the four exact state objects published by the preceding atomic commit.
''')
put('CLASSIFICATION_LEDGER.md',f'''# Classification ledger

Whole-registry raw sound candidates were split into exact semantic classes before installation: {json.dumps(wh['classification_counts'],sort_keys=True)}. Only 24 strict installed-union expansions were installed. The 302 sound budget exclusions remain explicitly positive and uninstalled.

Online raw candidates={fmt(cl['raw_term_candidates'])}; covered by evolving union={fmt(cl['covered_by_full_evolving_union'])}; retained={ce['online_generalized_terms_added']}. Cross-registry raw candidates={fmt(xr['raw_candidates'])}; retained={ce['post_outer_cross_registry_terms_added']}.

No negative class is promoted to global absence. See the JSON ledgers for every candidate and term.
''')
put('ATTACK_LEDGER.md',f'''# Closure attack ledger

The closure-oriented attack was the exact whole-registry star hitting-cut construction, followed by 12 candidate-specific direct-absence attempts on the most constrained branches.

- Strict installed-union expansions: 24.
- Fully closed outer candidates: 12 SAT outer schedules with both complete direct sectors checked.
- Candidate-specific direct attempts: 12 SAT, 0 UNSAT, 0 UNKNOWN/TIMEOUT.
- Accepted candidate Gross proofs: 0.
- Repair entries: 0.
- Load-bearing branch closures: 0.

Finite positive progress does not prove a stopping theorem. `D*_Gross` therefore remains undecided within {{11,12}}.
''')
put('RESTART_LICENSE.md',f'''# Exact restart license

The only mathematical continuation licensed by this proposer is a **fresh, unstarted outer iteration 102** using exactly the four objects in `restart/restart_state.json`.

Counts: unary=1,440; round-62=20; G={rs['counts']['generalized']:,}; D={rs['counts']['dynamic']}; registry/raw={rs['counts']['registry']}; installed sound blocks={rs['counts']['total_blocks']:,}.

Semantic hashes:

```json
{json.dumps(rs['semantic_sha256'],indent=2,sort_keys=True)}
```

A continuation must bind these exact semantic objects after decompression, start a fresh process, and preserve the proof gate and atomic pending/commit rules. Earlier Round-78 defective seals, stale compressor provenance, or any intermediate pending state are forbidden inputs.
''')
put('REVIEW_LICENSE.txt',f'''FRESH INDEPENDENT REVIEW REQUIRED.

This proposer licenses no canonical edit. After full independent verification, the sole possible canonical delta is an evidence/frontier link to the final sealed package plus the exact iteration-102 restart. It does not license changing D*_Gross, adding a closure theorem, editing SCHEDULER.yaml/protocols/reviews/generated views, or treating any failed search, zero cell, deletion countertuple, or budget exclusion as absence.
''')
put('MANIFEST.md','''# Artifact map

- `SOURCE_BINDINGS.json`: commissioned dispatcher, accepted Round-78 package, fresh Round-79 review, exact restart and engine hashes.
- `whole_registry/`: complete pair-leaf reconstruction, star search, classification, selector proofs and strict-outside witnesses.
- `cegar/iter90..iter101/`: fresh outer formula, schedule, direct CNFs, assignments, raw mechanisms, generalization, cross-registry proof data, pending/commit journals and resource records.
- `classification/`, `cross_registry/`, `restart/`: aggregate ledgers and exact frozen state.
- `controls/`: assignment, geometry, deletion and proof-checker controls.
- `development/`, `FIX-2.md`, `PROCESS_LEDGER.*`: failed/interrupted attempts, rollbacks and process accounting.
- `verify.py`: package-local quick/full verifier.
- `COMPRESSED_INVENTORY.json`: deterministic gzip compressed/uncompressed hashes.
- `PAYLOAD_SHA256SUMS.txt`, `SHA256SUMS.txt`: root-relative manifests; external root seal is SHA-256 of `SHA256SUMS.txt`.
''')
put('COMMANDS.txt','''# Representative commands; all paths were package-local or disposable scratch.
python src/synthesize_cross_registry.py --root PACKAGE --generalized-state START_G --registry-state START_R --raw-mechanisms-state START_RAW --dynamic-blocks-state START_D --output-root whole_registry/pair_leaf_reconstruction --batch-id pair-leaf-pre090
python src/synthesize_whole_registry.py --root PACKAGE --leaf-root whole_registry/pair_leaf_reconstruction --generalized-state classification/installed_generalized_terms.json --output-root whole_registry/hitting_synthesis --batch-id pre090 --max-retained 24
python src/run_round80_range.py --start 90 --end 101 --root PACKAGE --python VENV/python
python src/build_round80_aggregate.py --root PACKAGE
python src/build_round80_proof_controls.py --root PACKAGE
python src/build_round80_negative_controls.py --root PACKAGE
python verify.py --quick --allow-unsealed --repo-root REPOSITORY
python verify.py --full --allow-unsealed --repo-root REPOSITORY
python src/compress_round80.py --root PACKAGE
python verify.py --quick --allow-unsealed --repo-root REPOSITORY
python verify.py --full --allow-unsealed --repo-root REPOSITORY
# Then generate root-relative payload/root manifests, hash SHA256SUMS.txt externally, atomically install, and repeat quick/full with live bindings.
''')
print(json.dumps({'status':'PASS','documents':13,'final_counts':rs['counts']},sort_keys=True))
