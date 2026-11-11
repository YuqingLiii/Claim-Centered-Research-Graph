# Gross integrated schedule/mechanism CEGAR, round 62

**Date:** 2026-08-28  
**Target:** `CIRCDIST.gross#gap-via-lift`  
**Authorship:** proposer package for fresh independent review; this package does **not** license canonical promotion.  
**Public-reasoning note:** this report exposes the definitions, encodings, equations, constraints, traces, commands, outputs, rejected attempts, assumptions, and decision rules needed to audit the work. It does not claim to expose private hidden chain-of-thought.

## 0. Verdict

# **3) NOT CLOSED**

The smallest exact residual remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

No schedule in this package is a distance-12 certificate, and no outer-space exhaustion is claimed. The strongest new result is a working integrated CEGAR implementation with an exact, unrestricted 864-edge outer scheduler, a complete direct-360 effective-logical SAT adversary, an exact arbitrary-round repair-zero SAT adversary, raw replay validators, and sound schedule blocks. A bounded 20-iteration run completed. All 20 distinct legal interleaved schedules were rejected in the X-error/Z-memory sector by verified weight-10 direct-column mechanisms whose normalized physical data residuals have weight 12. The loop added 20 sound order-region blocks comprising 306 comparison atoms. It did not reach the Z-sector adversary or the repair adversary because the first sector already supplied a counterexample at every iteration.

This is quantitative CEGAR progress, not a universal subclass theorem. The filters used to find the positive counterexamples are explicitly incomplete for absence. Only the direct CNF can certify absence at the effective layer, only the arbitrary-round repair CNF can certify absence at the repair layer, and only an `UNSAT` result from the full outer model after all sound blocks could certify exhaustion.

Updated heuristic probabilities for **one further comparable round** are:

| exact branch | probability | update rationale |
|---|---:|---|
| reviewed-ready in-scope `D*=12` schedule | **0.03** | twenty unrestricted outer proposals died immediately by simple one/two-residual weight-10 attacks; the complete absence and repair checks remain harder |
| reviewed-ready universal `D*=11` proof | **0.17** | sound integrated blocking now works, but 20 regions are negligible compared with the unexhausted order space and no proof-producing outer exhaustion exists |
| neither | **0.80** | full direct-CNF and arbitrary-round repair-CNF scaling, followed by outer exhaustion, remain the obstruction |

These are planning estimates, not mathematical probabilities.

The concrete next action is to replace the current witness-at-a-time outer blocking with a proof-producing order-level effective adversary that derives a compact clause for **all** direct-360 selections sharing the same residual-support pattern, then run it incrementally with a checked UNSAT backend. The next run must retain the unrestricted outer model and must not promote the weight-12 one/two-residual finder into an absence test.

## 1. Exact disk binding and the stale-hash conflict

Disk state wins. `bindings.json` contains the exact normalized statement text, character counts, statement hashes, governing-file hashes, and repository commit read by this run.

The load-bearing statement hashes are:

| object | characters | SHA-256 |
|---|---:|---|
| `CIRCDIST.gross` claim | 586 | `fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180` |
| `candidate-certification` implication | 300 | `4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598` |
| `gap-via-lift` implication | 279 | `915109fe708c63ce138b11d07aa87c3048d676c87d9d6b7a80d68c0e2025c5d1` |
| `CIRCDIST.gross.dext-cap` claim | 148 | `4bc0b5eb3b74b174e60f641357f5bea5b9e6a4240c390ced1bf8fd17746bff42` |
| `CIRCDIST.lift.iff` claim | 544 | `0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240` |

Two hashes printed in hunt3 were stale by the time round 62 began:

| file | hunt3 start hash | round-62 disk hash | explanation |
|---|---|---|---|
| `operations/circdist/SCHEDULER.yaml` | `786d06d7...21a87` | `e798dc85...39786` | scheduler now authorizes round 62 and records the spent session |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `dd8a9b94...2d32` | `80fb6afb...109e6` | root now records hunt3 as proposer evidence while retaining `CONJECTURED` and `{11,12}` |

No mathematical conflict was found. The current root, scheduler, frozen definitions, premise nodes, hunts, certification artifacts, and independent reviews agree that the root remains `CONJECTURED`, the candidate supplies the certified floor 11, `d_ext<=11` is universal, and the lift criterion is `PROVED` at its present hypotheses.

SBB Theorem 1 is used only for **noninterleaved** schedules. Shaw–Terhal's “second gross” code is outside frozen `S_Gross` and is not used.

## 2. Frozen code and schedule space

Let

\[
G=\mathbb Z_{12}\times\mathbb Z_6,\qquad
A=\{(3,0),(0,1),(0,2)\},\qquad
B=\{(0,3),(1,0),(2,0)\}.
\]

The 72 X checks have supports `g+A` in the left half and `72+g+B` in the right half. The 72 Z checks have supports `g-B` and `72+g-A`. There are 144 data qubits, 144 single ancillas, and exactly

\[
72\cdot6+72\cdot6=864
\]

named CNOT edges. `src/model.py` constructs the edge set as strings `X:a:q` and `Z:b:q` and asserts both cardinality 864 and uniqueness.

A schedule is an integer map `t(e)` on these 864 named edges. The exact outer constraints are:

1. `0 <= t(e) < 864` for every named edge.
2. The six edges incident on each X ancilla have distinct times.
3. The six edges incident on each Z ancilla have distinct times.
4. The six X/Z check edges incident on each data qubit have distinct times.
5. For each of the 648 nonempty X/Z check overlaps `{q0,q1}`, measurement consistency is
   \[
   [t(Z,b,q_0)<t(X,a,q_0)]\iff[t(Z,b,q_1)<t(X,a,q_1)].
   \]
6. The outer search requires global X/Z interleaving by negating both `all X before all Z` and `all Z before all X` using exact minimum/maximum witnesses.

There are no flags, cat states, alternate generators, omitted edges, or repeated edge variables. Disjoint gates may share a time, as the frozen model permits.

### 2.1 Why the 864-value time domain and post-solve compression are lossless

Any legal finite schedule uses at most 864 distinct time values because it has 864 edges. Relabel its used times increasingly by `0,...,T-1`. This preserves every strict order comparison. All conflict constraints, MC constraints, within-check residual supports, singleton voltage sets, rigid hook voltages, and the global interleaving predicate depend only on equality or order of incident edge times. Therefore the compressed schedule satisfies exactly the same relevant predicates and lies in `0,...,863`.

Conversely, a model may contain unused integer values. `compress_schedule` removes them before any adversary runs, and `audit_schedule(..., require_compressed=True)` independently checks the resulting contiguous range. Thus allowing gaps inside Z3 is a satisfiability-preserving implementation choice, not a depth restriction.

### 2.2 Why searching the interleaved remainder is lossless for the exact branch

The current `PROVED` universal cap gives `d_ext<=11`. In the separately reviewed scope of SBB Theorem 1, a noninterleaved circuit has the extended-code equality needed to conclude `d_circ<=11`. This package never applies that theorem to an interleaved schedule. Hence an in-scope distance-12 witness, if one exists, must lie in the interleaved remainder encoded by `src/outer.py`. A future universal-11 closure would combine: the already reviewed noninterleaved result, plus certified exhaustion of this exact interleaved outer model. The present package does not supply that exhaustion.

No depth, translation-invariance, colour-tiling, check-serial, fixed-order, logical-weight, or bounded-hook-count restriction occurs in the outer model. No symmetry quotient is used.

## 3. Direct 360-column effective adversary

The two sectors are built independently:

| sector label | physical memory error | hook checks | detector rows | stabilizer rows | logical duals |
|---|---|---|---|---|---|
| `Xerr` | X | X checks | `H_Z` | `H_X` | Z logical basis |
| `Zerr` | Z | Z checks | `H_X` | `H_Z` | X logical basis |

For a hook-check order `i1,...,i6`, earliest first, the direct extended code has 144 singleton columns and exactly three normalized residual columns:

\[
\{i_1,i_2\},\qquad \{i_4,i_5,i_6\},\qquad \{i_5,i_6\}.
\]

The first representative carries the voltage of the **physical 4-suffix** `{i3,i4,i5,i6}`. Each sector therefore has `144+72*3=360` columns. Every build asserts 216 distinct residual supports and residual weight in `{2,3}`.

For Boolean column-selection variables `x_j`, the exact `d_eff<=W` query is

\[
\sum_{j=0}^{359}x_j\le W,
\]
\[
\bigoplus_{j:c_{j,b}=1}x_j=0\quad(b=0,\ldots,71),
\]
\[
\bigvee_{r=0}^{11}\left(\bigoplus_{j:\langle c_j,\ell_r\rangle=1}x_j\right)=1.
\]

Tseitin XOR chains encode long parity rows; a sequential counter encodes the cardinality. The 360 Boolean variables inherently select distinct columns. A returned SAT model is discarded unless `verify_effective_selection` rebuilds its data mask from the selected indices, obtains zero detector syndrome, finds it outside the stabilizer rowspace, sees a nonzero logical-parity vector, and confirms weight at most `W`.

This formulation does **not** enumerate a weight-12 logical pool. It covers every logical residual weight, every hook count, and every distinct selection of at most ten direct columns. It is the only effective adversary in the loop allowed to turn absence into `UNSAT`.

### 3.1 Duplicate and full-check normalization

The direct columns are complete for a minimum effective mechanism under the frozen fault model:

- Selecting the same extended column twice cancels over `F_2` while costing two faults. Deleting the pair preserves syndrome and logical class and lowers weight. Therefore a minimum mechanism has no duplicate selected column.
- A 6-suffix equals the full check stabilizer. Under MC its voltage is zero. Deleting it preserves the effective logical class and repair data. If it occurred in a weight-11 minimum mechanism, deletion would give an effective logical of weight at most ten, a contradiction.
- A physical 1-suffix is the last data singleton; its rigid voltage is a member of that singleton's four-element prefix-voltage set.
- A physical 5-suffix differs from the earliest singleton by the full check stabilizer. Under MC their voltages agree modulo the zero full-check voltage, so the singleton represents it.
- A physical 4-suffix differs from the two-prefix representative by the full check stabilizer; syndrome and logical parities agree, while the column retains the physical 4-suffix voltage.
- Physical 2- and 3-suffixes are the other two direct residuals.

Thus no refuted four-shape screen, `|V|=12` restriction, or `j<=4` recursion is used as a completeness argument. The imported 1884-word pools are used only by fast **positive-witness finders** and named controls.

### 3.2 Solver result discipline

`_solve_cnf` records `SAT`, `UNSAT`, `UNKNOWN`, or `ERROR`, the exact clause-stream SHA-256, clause count, conflict budget, solver statistics, elapsed solver time, and whether a proof was requested. Models are read only on literal Python `True`. An `UNKNOWN` result stops the CEGAR loop and cannot support absence. No timeout or partial model is converted into a verdict.

The bounded direct C1 query reached 200,000 conflicts and returned `UNKNOWN` after 6.855120 solver seconds (`16173` clauses, formula hash `e6d7da4...74fd`). It is preserved as `outputs/bounded_direct_effective_unknown.json` solely to show return-code handling. The explicit C1 witness is independently normalized and replayed, so the UNKNOWN result is not needed.

## 4. Exact arbitrary-round repair adversary

This layer is reached only after the direct effective adversary has certified `UNSAT` at weight at most ten in **both** sectors. With the universal cap, that establishes `d_eff=11`.

For every direct column `j`, round `r in {0,...,10}`, and allowed voltage choice `u in U_j`, the model has a Boolean `y_{j,r,u}`. Residual hook columns have one rigid `u`; singleton columns include all four relevant prefix choices induced by their three detector-CNOT times. Constraints are:

1. At most one `(r,u)` choice for each direct column `j`.
2. Exactly eleven choices over all `y` variables.
3. Zero terminal effective syndrome and nonzero logical parity, using the same direct supports as Section 3.
4. For each round `t` and detector check `b`, the current `PROVED` lift equation
   \[
   \bigoplus_{j:r_j=t}u_{j,b}
   =
   \bigoplus_{j:r_j<t}s_{j,b}.
   \tag{LIFT'}
   \]

The span bound translates any relevant eleven-fault assignment to rounds `0,...,10`; no same-round, two-group, canonical-family, or fixed-partition assumption occurs in this CNF. A SAT model must pass `verify_repair_trace`, which checks eleven distinct columns, every chosen `u in U_j`, effective-logical validity, all 72 components of all eleven round equations, and zero terminal syndrome.

The first implementation mixed PySAT `IDPool` allocation with `CardEnc(top_id=p.top)` and then allocated more semantic variables. Because `CardEnc` does not advance `IDPool`, auxiliary IDs aliased later variables and manufactured a spurious fast `UNSAT` on C2. The raw C2 witness exposed the contradiction. The fix allocates every semantic and XOR variable first, then builds all counters while monotonically advancing `top=enc.nv`. The rejected output is retained under the explicit filename `rejected_pre_fix_repair_unsat_DO_NOT_USE.json` and has no evidentiary role. A post-fix full repair run was interrupted in the foreground after about two minutes with no verdict. No output or claim was harvested from it.

The incomplete `canonical_same_round_repair0` routine searches all canonical two-suffix weight-11 mechanisms derived from the complete weight-12 pool and all singleton voltage choices by meet-in-the-middle. A found trace is a valid arbitrary-round trace with all faults in round zero. Failure of this finder is never absence evidence.

## 5. CEGAR loop and sound blocking lemma

At iteration `i`:

1. Solve the exact interleaved outer constraints plus every previous sound block.
2. Compress times and replay all 864 edges, all qubit-sharing conflicts, and all 648 MC equations.
3. In `Xerr`, then `Zerr`, run the fast positive finder. If it finds nothing, run the complete direct-360 SAT adversary.
4. If an effective counterexample is returned, replay it from raw schedule times and add a sound effective block.
5. Only after complete effective `UNSAT` in both sectors, run the repair-positive finder and then the exact arbitrary-round repair SAT adversary.
6. If a repair-zero counterexample is returned, replay every LIFT' equation and add a sound repair block.
7. A schedule is review-ready for distance 12 only if both complete effective queries are `UNSAT` and, where `d_eff=11`, both complete repair queries are `UNSAT` under the current lift hypotheses.
8. A universal distance-11 result is review-ready only after the outer model itself is certified exhausted, combined with the separately scoped noninterleaved theorem.

### 5.1 Effective block soundness

Singleton supports are schedule-independent. For a selected residual support `S` in hook check `a`, let `O` be the other four, three, or four check qubits as appropriate. The block antecedent contains:

- `q<r` for every `q in S, r in O` for a two-prefix representative; or
- `q<r` for every `q in O, r in S` for a three- or two-suffix representative.

These cross-boundary inequalities are necessary and sufficient to preserve that residual support; internal order inside `S` and `O` remains free. If all antecedent atoms remain true, every selected direct column has the same data support. Hence the same XOR residual has zero syndrome and the same nonzero logical parity. Negating the conjunction is therefore a sound schedule block. It may be conservative, but it never removes a schedule on which the returned witness has disappeared.

### 5.2 Repair block soundness

A repair block contains the effective support atoms above, every raw hook/detector comparison that determines each selected rigid hook voltage, and the cross-boundary detector-order comparisons that preserve each chosen singleton prefix-voltage set. It also fixes the returned round assignment. Any schedule satisfying all atoms preserves the direct supports, the selected voltages, and every LIFT' equation, so it preserves the repair-zero counterexample. Again, negating the conjunction is sound and deliberately conservative.

### 5.3 Raw replay and block tests

`verify.py` recomputes every persisted schedule digest, schedule audit, direct witness, block conjunction, and trace digest. It also checks all 190 pairs `(current iteration, earlier block)` and confirms each later schedule violates every earlier preserving conjunction. `outputs/negative_controls.json` confirms that each source schedule satisfies its own block and that swapping the endpoints of one block atom falsifies the conjunction.

## 6. Bounded CEGAR result

Command wall time was 6.333751209 seconds. The solver completed all 20 requested iterations.

| quantity | result |
|---|---:|
| exact outer SAT schedules | 20/20 |
| distinct schedule SHA-256 values | 20 |
| raw schedule audits passing | 20/20 |
| raw effective witnesses passing | 20/20 |
| counterexample sector | `Xerr` in 20/20 |
| direct mechanism weight | 10 in 20/20 |
| normalized net data weight | 12 in 20/20 |
| one-residual finder hits | 2 |
| two-positive-residual finder hits | 18 |
| residual candidates inspected before hits | 228,763 single tests and 26 pair tests total |
| sound blocks added | 20 |
| total block atoms | 306 |
| atoms per block | 9 to 16 |
| distinct comparison atoms across blocks | 168 |
| compressed schedule layers | 65 to 128 |
| overlap-interleaved check pairs | 35 to 98 of 648 |
| whole-check interleaved pairs | 95 to 147 of 648 |
| total recorded outer solve time | 2.383183 seconds |

The first witness is

```text
R:2:0, R:5:0, D:6, D:7, D:9, D:10, D:72, D:73, D:75, D:76
```

with net support

```text
{0,1,3,4,6,7,9,10,72,73,75,76}
```

and logical-parity vector

```text
(1,0,0,1,1,0,0,0,0,0,0,0).
```

The full 864 raw times, selected indices and names, net supports, syndromes, logical parities, outer audits, block atoms, and trace hashes for all iterations are in `outputs/cegar20.json`. `outputs/cegar20_summary.json` is a compact index, not a replacement for the decisive ledger.

Because every iteration stopped at the first-sector positive witness, this run says nothing absence-side about `Zerr` for those schedules and never enters the repair layer. The exact residual therefore cannot narrow below `{11,12}`.

## 7. Positive and negative controls

### 7.1 Schedule reconstruction

`outputs/audit.json` reconstructs the published noninterleaved candidate and hunt3 schedules C1/C2 from their raw definitions:

| schedule | edges | used layers | conflicts | MC violations | global interleaving |
|---|---:|---:|---:|---:|---|
| published candidate | 864 | 864 | 0 | 0/648 | no |
| hunt1 | 864 | 36 | 0 | 0/648 | yes |
| C1 | 864 | 36 | 0 | 0/648 | yes |
| C2 | 864 | 36 | 0 | 0/648 | yes |

Every sector/schedule pair constructs exactly 360 direct columns with 216 distinct residual supports.

### 7.2 Expected positive failures

- **C1/Zerr:** the hunt3 physical mechanism normalizes to ten distinct direct columns
  `D:1,R:31:2,D:25,R:6:1,R:62:0,D:18,D:26,D:76,D:100,D:116`.
  Replay gives zero syndrome, logical parities `(1,1,0,0,1,0,0,0,1,0,0,0)`, and net support weight 14. This explicitly demonstrates why a `|V|=12` absence screen is incomplete.
- **C2/Xerr and C2/Zerr:** both named eleven-column mechanisms replay with all faults in round zero, every LIFT' equation zero, and nontrivial weight-12 net support.
- **hunt1/Xerr and hunt1/Zerr:** the positive finder reconstructs weight-10 mechanisms with two direct residuals and eight singleton columns in both sectors. These are fresh positive controls on the earlier schedule, not absence claims about hunt1's historical family.
- **published candidate/Xerr and Zerr:** the same-round repair finder reconstructs repair-zero weight-11 mechanisms in both sectors, as expected for the certified distance-11 circuit. This uses no interleaved extension of SBB Theorem 1.

### 7.3 Deliberate corruptions

All negative controls passed:

1. assigning two edges sharing data qubit 0 the same time is rejected as a qubit conflict;
2. swapping one X/Z edge-time pair in the globally serial schedule preserves global timestamp uniqueness and conflict freedom but is rejected by MC;
3. duplicating one selected C1 direct-column index is rejected by the distinct-column verifier;
4. changing C2's rigid hook voltage to a value outside its allowed set is rejected;
5. all 20 CEGAR witnesses replay, every source schedule satisfies its preserving block, and an endpoint swap falsifies that block.

These controls check the failure paths that matter for this run. They are not a substitute for fresh independent adversarial review.

## 8. Rejected approaches and exact limitations

- The four individually gain-positive shapes are not a completeness theorem; C1 refuted that screen.
- Restricting logical residuals to weight 12 is not complete; the normalized C1 direct witness has net weight 14.
- Limiting contributing hook checks to four is not complete and the old recursion did not enforce distinct checks. The direct Boolean-column formula does enforce distinct selections and has no hook-count bound.
- Same-round, two-group, and canonical repair searches are positive finders only. The exact repair CNF includes every round assignment within the proved eleven-fault span.
- Translation-invariant, three-colour-tiled, minimum-depth, check-serial, and fixed-order families are not used as outer quotients.
- CaDiCaL `UNKNOWN` is not `UNSAT`; an interrupted process supplies no model or verdict.
- No DRAT/LRAT checker was available in this session. No UNSAT result from this package is load-bearing. The positive certificates are independently replayable from raw integers.
- The complete 1884 logical pools are inherited from the independently reviewed wave-36 enumeration. This package re-expands and validates their members but does not independently re-prove pool completeness. Pool completeness is not needed by the direct CNF; it affects only the speed and stated scope of positive finders.
- No proof of outer exhaustion exists. Twenty order regions are blocked, but their fraction of the full space is unknown.
- The repair CNF has not completed after the allocator fix. Its encoding is present and checkable; its absence side remains unvalidated computationally.
- No claim here applies to Shaw–Terhal's second-gross code or any circuit outside frozen `S_Gross`.

## 9. Reproduction

Environment used:

```text
macOS 26.6.2 (25G83), arm64
Python 3.9.6
numpy 2.0.2
python-sat 1.9.dev15
six 1.17.0
z3-solver 5.1.0.0
CaDiCaL 1.9.5 through python-sat
repository HEAD e40a7ac40972ad5186018797efa390a8e3f784f0 (main)
```

From this package directory:

```bash
python3 -m venv /tmp/gross62-verify-venv
/tmp/gross62-verify-venv/bin/pip install -r requirements.txt
/tmp/gross62-verify-venv/bin/python verify.py
```

Re-run the raw schedule/control audit:

```bash
/tmp/gross62-verify-venv/bin/python src/run.py \
  --w12x inputs/w12X.txt --w12z inputs/w12Z.txt \
  audit --output /tmp/gross62-audit.json
```

Re-run the exact same bounded CEGAR frontier:

```bash
/tmp/gross62-verify-venv/bin/python src/run.py \
  --w12x inputs/w12X.txt --w12z inputs/w12Z.txt \
  cegar --iterations 20 --outer-timeout-ms 30000 \
  --conf-budget 20000 --repair-conf-budget 10000 \
  --output /tmp/gross62-cegar20-rerun.json
```

Z3 model selection is not promised deterministic across library builds, so a rerun may produce different legal schedules and witnesses. The sealed ledger itself is deterministic to replay. The decisive validation command is `verify.py`, which does not invoke a solver.

Re-run the deliberate corruptions:

```bash
/tmp/gross62-verify-venv/bin/python src/negative_controls.py \
  --w12x inputs/w12X.txt --w12z inputs/w12Z.txt \
  --cegar outputs/cegar20.json --output /tmp/gross62-negative-controls.json
```

## 10. Decision criteria for a future exact package

An **exact 12** author package must contain one legal raw schedule and checked `UNSAT` certificates for the direct `W<=10` effective query in both sectors and for every applicable exact repair-zero query after `d_eff=11`, all under the present lift hypotheses. It then requires fresh independent adversarial review before any canonical action.

An **exact 11** author package must contain checked exhaustion of the full interleaved outer model under only sound generalized blocks, plus the already scoped noninterleaved result. Subclass exhaustion, sampling, or failure of a positive finder is insufficient. It likewise requires fresh independent review.

This package meets neither threshold.

## 11. FIX-2, scratch, and mutation accounting

`process_accounting.json` is the complete machine-readable ledger.

- No subagent was spawned.
- No background or detached process was started.
- Every solver and checker ran in the foreground and was awaited or interrupted cleanly.
- The pre-existing scheduler PIDs 43443 and 5675 were absent.
- Post-fix repair PID 63915 was interrupted with SIGINT after approximately two minutes; no child remained and no verdict was recorded.
- Negative-control scan PID 60665 was interrupted with SIGINT at 30 seconds and replaced with a constant-time deterministic corruption; its exit was 130 and no partial result was used.
- Scratch is `/tmp/circdist_gross_cegar_round62_20260828`; it is retained only for diagnosis and has no running process.
- The repository had 1,391 pre-existing dirty/untracked status lines before this package. The before/after comparison permits exactly this one new package directory and finds no mutation to a pre-existing path.
- No canonical node, scheduler, protocol, prior artifact/review, tool, or generated view was edited.

`SHA256SUMS.txt` hashes every package file except itself. Its own SHA-256, total package byte size, and file count are reported after final sealing and in the commissioning response.

## 12. Read-only repository and package validation

All validation commands were read-only; `--write-generated` was not used.

```text
$ python3 tools/proof_dag_check.py --problem circdist
circdist: 16 node files structurally valid
exit 0

$ python3 tools/check_circdist_migration.py
Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies
exit 0

$ python3 tools/evidence_closure_check.py --problem circdist
26 unlinked-evidence errors, one for every non-README package file
exit 1
```

The evidence-closure failure is expected and honest: the durable-write boundary forbids editing a canonical node to link this proposer package, and this report explicitly does not license promotion. It is not a mathematical validation failure and must not be hidden; a future authorized review/install round would either link reviewed evidence or remove/reclassify it under protocol.

The final sealed-package replay command returned:

```json
{
  "cegar_iterations_replayed": 20,
  "frozen_pool_sizes": {"X": 1884, "Z": 1884},
  "manifest_entries_verified": 26,
  "named_controls_rebuilt": [
    "C1/Zerr effective",
    "C2/Xerr repair0",
    "C2/Zerr repair0"
  ],
  "negative_controls_pass": true,
  "prior_block_exclusions_checked": 190,
  "status": "PASS",
  "unique_counterexample_traces": 20,
  "unique_schedules": 20
}
```
