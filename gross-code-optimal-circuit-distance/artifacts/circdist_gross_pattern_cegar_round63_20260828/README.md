# Gross order-pattern CEGAR, round 63

**Date:** 2026-08-28  
**Target:** `CIRCDIST.gross#gap-via-lift`  
**Role:** proposer package for fresh independent review; this package does not license promotion.  
**Reasoning visibility:** this report gives the definitions, encodings, soundness arguments, quantifier coverage, commands, outputs, failures, controls, assumptions, and decision rules used here. It does not claim to reveal private hidden chain-of-thought.

## 0. Verdict

# **3) NOT CLOSED**

The exact residual remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

The strongest sealed result is a globally valid library of **1,440 five-comparison order clauses**, 720 in each sector. These clauses cover every local order admitting a weight-10 mechanism made from one suffix-three residual column and nine singleton columns completing a frozen weight-12 logical. The deterministic checker enumerates all 720 local orders for every check: 103,680 sector/check/order cases. Every one of the 1,440 clauses is deletion-minimal under its five retained atoms, with 7,200 explicit atom-deletion countercontrols. The clause library is complete only for this stated single-residual mechanism family.

A separate bounded exact-outer experiment completed 10 incremental SAT iterations and generated **15,874 distinct exact residual-support clauses**: 8,159 `Xerr` and 7,715 `Zerr`. Every inserted clause had an explicit raw-replayed weight-at-most-10 positive witness. The exploratory driver did not retain the ten raw schedule ledgers or independently replay later-schedule exclusions after the run, so this count is quantitative progress rather than sealed exhaustion evidence. Its self-contained replay source is included.

No complete direct-360 query reached checked `UNSAT`; no DRUP, DRAT, LRAT, or equivalent solver proof was checked. Two proof-requesting foreground runs were interrupted cleanly and have zero evidentiary use. The exact arbitrary-round repair-zero layer was therefore not invoked in round 63. Neither the distance-12 survivor criterion nor universal interleaved exhaustion was met.

Updated planning probabilities for one comparable next round are:

| branch | probability | basis |
|---|---:|---|
| reviewed-ready in-scope `D*=12` schedule | 0.02 | all observed unrestricted outer schedules have dense one/two-residual attacks, and no effective-absence proof exists |
| reviewed-ready universal `D*=11` proof | 0.21 | order clauses are much broader than witness blocks, but the proof-producing direct-360 and outer-exhaustion bottlenecks remain |
| neither | 0.77 | the full absence layers still dominate |

These are workflow estimates, not mathematical probabilities.

The concrete next action is: take one clause-saturated exact-outer candidate, emit its complete direct-360 `Xerr` and `Zerr` CNFs as DIMACS, run a proof-logging solver under an explicit foreground time limit, and retain a result only after `drat-trim` or an LRAT checker accepts the proof. Do not enter repair-zero unless both sector proofs pass.

## 1. Disk binding and conflicts

`bindings.json` binds the exact files read from disk. Disk wins over prior package metadata. The current governing hashes include:

| object | current SHA-256 |
|---|---|
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `operations/circdist/SCHEDULER.yaml` | `9b51ad558aec6c9fe986078c15723f2b0e2113974ed5f2b60d63e5c73bad3fc5` |
| frozen definitions | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |
| `CIRCDIST.gross.yaml` | `b50fd9cef17effa317bd8b433ac07f53d61161dc68a0c7d5fcb388e6c6437e59` |
| `CIRCDIST.gross.dext-cap.yaml` | `a2c89dac0a66bee9f4055fece6d7d4e032203ca2ad38d8a70c071ff7afc16f0d` |
| `CIRCDIST.gross.mc-equiv.yaml` | `0c75299358a4f6c63a53ff5b96bf2d3646e42daeb4edd776207dfdfea46a0aa3` |
| `CIRCDIST.lift.iff.yaml` | `7b7929628c48e7c75997d33661989ed61e7bf83ca775802d807f211a224b3a68` |

Round 62 bound older scheduler and Gross-node bytes:

| file | round-62 hash | current disk hash | resolution |
|---|---|---|---|
| scheduler | `e798dc85…39786` | `9b51ad55…3fc5` | current disk bound |
| Gross root | `80fb6afb…109e6` | `b50fd9ce…7e59` | current disk bound |

The normalized load-bearing statement texts and hashes are unchanged. The root remains `CONJECTURED`, the exact residual remains `{11,12}`, and no mathematical conflict was found. The current bytes changed because the scheduler and root recorded later work.

## 2. Round-62 reproduction gate

Round 62 was not trusted until all of the following passed from a scratch copy:

- its 26-entry manifest checked 26/26;
- its read-only verifier replayed 20 schedules, 20 traces, 190 prior-block exclusions, both 1,884-word pools, C1/Zerr, C2/Xerr, C2/Zerr, and all persisted negative controls;
- fresh audit and negative-control runs were byte-identical;
- a fresh CEGAR20 run reproduced all 20 schedule hashes, all 20 trace hashes, and all 20 outer SMT hashes after deleting timing fields only;
- the block atom sequence was `16,16,16,16,16,16,9,16,16,16,16,16,16,16,16,16,9,16,16,16`, totaling 306.

The copied raw ledgers are under `outputs/round62_*`; `verify.py` replays them without trusting their success flags. `outputs/round62_reproduction.json` records the reproduction comparison.

## 3. Frozen model and unrestricted exact outer schedule

Let

\[
G=\mathbb Z_{12}\times\mathbb Z_6,
\quad A=\{(3,0),(0,1),(0,2)\},
\quad B=\{(0,3),(1,0),(2,0)\}.
\]

The code has 144 data qubits, 72 X checks and 72 Z checks of weight six. `src/model.py` reconstructs the frozen supports. There are exactly 864 named CNOT edges, `X:a:q` or `Z:b:q`, and 648 nonempty X/Z check overlaps, each of size two.

`src/outer.py` is unchanged from the reproduced round-62 model. For every named edge it creates one integer `t(e)` with `0 <= t(e) < 864`. It asserts:

1. distinct times for the six edges of every X ancilla;
2. distinct times for the six edges of every Z ancilla;
3. distinct times for the six incident X/Z CNOTs of every data qubit;
4. for every overlap `{q0,q1}`,
   \[
   [t(Z,b,q_0)<t(X,a,q_0)]\iff[t(Z,b,q_1)<t(X,a,q_1)];
   \]
5. the negations of all-X-before-all-Z and all-Z-before-all-X.

Disjoint gates may share a time. No depth cap, tiling, translation invariance, fixed local order, hook-count cap, logical-weight cap, or schedule symmetry quotient is present.

The 864-value domain is lossless: any legal finite schedule has at most 864 used times, and increasing relabeling to `0,…,T-1` preserves every equality and strict comparison used by conflicts, MC, residual supports, voltage sets, and interleaving. Every SAT model is compressed and raw-audited before use.

The interleaved restriction is exact for the unresolved branch because the separately reviewed noninterleaved theorem and universal `d_ext<=11` cap already exclude a noninterleaved distance-12 maximizer. A universal-11 conclusion would still require checked exhaustion of the full encoded interleaved remainder.

## 4. Direct-360 normalization and complete effective adversary

Both sectors are constructed separately:

| label | physical error | hook checks | detector checks | logical duals |
|---|---|---|---|---|
| `Xerr` | X | X | Z | Z logical basis |
| `Zerr` | Z | Z | X | X logical basis |

For a local hook order `(i1,…,i6)`, earliest first, the normalized direct code contains 144 singleton columns plus three residual columns per hook check:

\[
\{i_1,i_2\},\qquad \{i_4,i_5,i_6\},\qquad \{i_5,i_6\}.
\]

Thus each sector has `144 + 72*3 = 360` columns. `src/model.py` asserts 216 residual supports and residual weights in `{2,3}`.

The normalization is complete for a minimum mechanism under the frozen model:

- duplicate selections cancel over `F_2` and can be deleted at lower cost;
- a full-check suffix is a stabilizer and has zero MC voltage, so it can be deleted;
- a physical one-suffix is its last singleton;
- a five-suffix differs from the earliest singleton by the full check;
- a four-suffix differs from the two-prefix representative by the full check, while the representative retains the physical four-suffix voltage;
- two- and three-suffixes are the other two residuals.

For selection variables `x_j`, the complete weight-at-most-10 query in either sector is

\[
\sum_{j=0}^{359}x_j\le10,
\quad
\bigoplus_{j:c_{j,b}=1}x_j=0\ (b=0,…,71),
\quad
\bigvee_{r=0}^{11}\bigoplus_{j:\langle c_j,\ell_r\rangle=1}x_j=1.
\]

Tseitin chains encode XORs and a sequential counter encodes cardinality. A SAT model is accepted only after `verify_effective_selection` reconstructs its support, zero syndrome, nonzero logical parities, distinct valid columns, and weight. This CNF covers every direct-column selection at cost at most ten in both sectors. The 1,884-word weight-12 pools are positive-witness accelerators only; failure of any single/pair pool scan proves nothing.

Round 63 did not finish this complete query with a checked absence result. That is the current bottleneck.

## 5. Formal order-clause semantics

An atom is a strict comparison `e<f` between two named edges. A clause certificate consists of:

- a sector;
- one or more residual references `(check,residual-kind)`;
- a conjunction `A` of within-check comparison atoms;
- for every tuple of local six-edge orders satisfying `A`, an explicit pool word `V` and singleton completion.

Write `D(o)` for the XOR of the referenced residual supports under local-order tuple `o`, and let `r` be the number of residual columns. Soundness requires

\[
\forall o\models A\;\exists V\in P_{12}:\quad
r+|V\oplus D(o)|\le10.
\]

The selected residual columns plus singleton columns indexed by `V xor D(o)` reconstruct `V`, so they have zero detector syndrome and nonzero logical parity. Therefore every schedule satisfying `A` has a weight-at-most-10 effective logical. The sound outer block is

\[
\neg A = \bigvee_{a\in A}\neg a.
\]

This is an order-region theorem, not a fixed witness block: the residual support and completing pool word may vary across orders inside the region. Clause checking is independent of the outer solver and finite because each referenced check has only `6!` local orders.

## 6. Global single-residual clauses

For the suffix-three residual of check `a`, let `S` be its three late qubits and `O` the other three. An exact support region has nine atoms `q<r` for all `q in O, r in S`. A local suffix `S` is “bad” when some frozen weight-12 logical contains `S`; then that residual plus the nine singleton columns of `V xor S` has cost ten.

For every sector/check:

- exactly 10 of the 20 three-subsets are bad;
- the generator starts from each corresponding nine-atom exact region;
- it searches subsets in increasing size and lexicographic order using 720-bit order truth tables;
- the first sound region always has five atoms;
- the ten generalized regions catch all 360 bad permutations and zero of the 360 good permutations.

Results:

| sector | checks | clauses | atoms/clause | order cases | deletion controls | clause digest |
|---|---:|---:|---:|---:|---:|---|
| Xerr | 72 | 720 | 5 | 51,840 | 3,600 | `b5c85627…83f8` |
| Zerr | 72 | 720 | 5 | 51,840 | 3,600 | `9290efb7…3d65` |

For every retained atom, deleting that atom exposes a recorded good local order, so the final conjunction is deletion-minimal. “Deletion-minimal” is the proved claim; no uniqueness or globally largest region is asserted.

`src/pattern.py` is the proof object generator/checker. `outputs/global_single_clauses.json` fixes the aggregate counts and canonical digests. `verify.py --full-static` independently regenerates all clauses, all pool completions, coverage checks, and all 7,200 negative controls.

This family is complete only for single suffix-three residual plus weight-12 pool completion. It is not a complete direct-360 absence test.

## 7. Ten-step aggregated support-pattern CEGAR

`src/pattern_cegar.py` enumerates, on each exact outer schedule and in both sectors, every one-residual and every two-residual selection completable against the full frozen weight-12 pool at total cost at most ten. It canonicalizes each mechanism to the union of its exact support-preserving order atoms, raw-replays a witness, deduplicates clauses globally, and adds all new clauses to the incremental outer solver.

| iteration | Xerr new | Zerr new | total new |
|---:|---:|---:|---:|
| 0 | 754 | 720 | 1,474 |
| 1 | 801 | 356 | 1,157 |
| 2 | 745 | 697 | 1,442 |
| 3 | 996 | 752 | 1,748 |
| 4 | 893 | 965 | 1,858 |
| 5 | 955 | 1,091 | 2,046 |
| 6 | 815 | 912 | 1,727 |
| 7 | 851 | 727 | 1,578 |
| 8 | 598 | 754 | 1,352 |
| 9 | 751 | 741 | 1,492 |
| **total** | **8,159** | **7,715** | **15,874** |

All ten outer calls were SAT and used the full 864-edge/648-MC interleaved model. Every inserted pattern passed raw effective-witness replay. The source run did not serialize its schedules, schedule hashes, clause bodies, or independent exclusion replay. Consequently this package reports the exact completed counts and source algorithm but does not count the run as an exhaustion certificate. A future run must retain every source schedule, every clause certificate, every later-schedule exclusion, and canonical hashes.

The first schedule alone had 754 Xerr clauses (one single-residual and 753 pair-residual) and 720 Zerr pair-residual clauses. Its Xerr atom histogram was `{9:1,16:737,17:10,18:6}`; all Zerr clauses had 16 atoms.

## 8. Exploratory two-residual generalization

The first 200 enumerated Xerr mechanisms on the reproduced iteration-0 schedule were greedily minimized while rechecking every consistent local-order support tuple against an explicit pool completion. The retained-atom histogram was:

| original → retained | mechanisms |
|---|---:|
| 16 → 12 | 93 |
| 16 → 14 | 26 |
| 16 → 15 | 21 |
| 16 → 13 | 19 |
| 16 → 8 | 19 |
| 16 → 7 | 14 |
| 16 → 9 | 7 |
| 9 → 5 | 1 |

The experiment removed 833 of 3,193 atoms and checked 2,360 final individual atom deletions. These were mechanisms before clause deduplication, and the full certificate ledger was not retained. They are an algorithmic milestone only and are excluded from the sealed clause count.

## 9. Proof backend and absence discipline

PySAT 1.9.dev15 probes found proof text support in Glucose4, Glucose42, Lingeling, and MapleSAT on toy formulas. The available CaDiCaL wrappers returned no proof text. No external DRAT/LRAT checker was installed or invoked under the timebox.

Two complete direct-360 `published/Xerr/W=10` runs used the same 16,317-clause formula, SHA-256 `02fa87c8…f4cf`:

| solver | seconds | terminal status | proof retained | verdict use |
|---|---:|---|---:|---|
| Glucose42 | 131.688818 | caught foreground interrupt; `ERROR` | 0 lines | none |
| Lingeling | 97.033181 | caught foreground interrupt; `ERROR` | 0 lines | none |

No solver process remained. The failed `drat-trim` clone request never launched because its requested working directory did not exist; no installation or check followed after the seal timebox.

The decision rule is strict: `UNKNOWN`, timeout, interruption, `ERROR`, an unchecked solver summary, zero proof lines, or merely finding no counterexample is no verdict. Any future absence-side `UNSAT` must ship the exact DIMACS, proof object, solver command/return code, checker command/return code, and checker output.

## 10. Repair-zero gate and allocator audit

The exact arbitrary-round repair model in `src/model.py` remains the reproduced round-62 implementation. It allocates `y[j,r,u]` for every direct column, round `0,…,10`, and allowed voltage. It enforces distinct columns, exactly eleven choices, zero terminal syndrome, nonzero logical parity, and for every detector component and round

\[
\bigoplus_{j:r_j=t}u_j=
\bigoplus_{j:r_j<t}s_j.
\]

The round-62 auxiliary-variable bug is visibly fixed: all semantic and XOR variables are allocated first; cardinality encodings are then created with a monotone `top`, updated to each `CardEnc.nv`. This prevents counter auxiliaries from aliasing later semantic variables. The named C2 repair-zero witnesses replay in both sectors, and an invalid-voltage negative control is rejected.

Round 63 never obtained checked effective `UNSAT` in both sectors for a schedule. Under the gate, it therefore did not invoke repair-zero. A distance-12 survivor would require checked effective absence and, when `d_eff=11`, checked arbitrary-round repair absence at every required sector/layer under the current `PROVED` lift criterion.

## 11. Controls and disclosed gaps

Already checked controls include:

- all 20 round-62 source schedules satisfy their own blocks;
- all 190 later-schedule/prior-block exclusions replay;
- swapping one comparison endpoint breaks every round-62 source block control;
- duplicate direct columns are rejected;
- an invalid repair voltage is rejected;
- a shared-qubit collision and an MC-only corruption are rejected;
- all 7,200 static generalized-clause atom deletions expose a good local order;
- C1/Zerr direct normalization and C2 repair traces in both sectors replay from raw selections.

The requested per-column corruption campaign for every newly aggregated witness was not completed before the seal timebox. The exploratory 15,874-clause run also lacks a retained raw schedule/clause ledger and independent post-run exclusion replay. These gaps are explicit reasons this is not a closure package.

## 12. Commands and validation

The sealed package is read-only. With the versions in `requirements.txt`:

```bash
shasum -a 256 -c SHA256SUMS.txt
PYTHONDONTWRITEBYTECODE=1 python verify.py \
  --repo-root <repo>
PYTHONDONTWRITEBYTECODE=1 python verify.py --full-static \
  --repo-root <repo>
```

The first verifier checks the manifest, live disk bindings, pools/bases, all 20 copied round-62 schedules and witnesses, 190 exclusions, named controls, persisted pattern totals, proof/process ledgers, and static certificate hashes. `--full-static` additionally regenerates all 1,440 clauses and 7,200 deletion countercontrols; the seal replay took 8.043775 seconds.

The heavy bounded pattern run can be independently regenerated, but was not rerun during sealing:

```bash
PYTHONDONTWRITEBYTECODE=1 python src/pattern_cegar.py \
  --iterations 10 --timeout-ms 30000 --output /tmp/round63-pattern-cegar.json
```

That output must be treated as positive bounded evidence unless it is extended with proof-producing complete absence checks and a retained/replayed ledger.

## 13. Decision rules and limitations

A reviewed-ready `D*=12` result needs an explicit legal interleaved schedule plus checked absence at every effective and repair layer required by the proved lift criterion, in both sectors. A reviewed-ready universal `D*=11` result needs checked exhaustion of the full unrestricted interleaved outer model, combined only with the separately reviewed noninterleaved result. Neither occurred.

No tiled, depth-limited, translation-invariant, fixed-order, hook-count, or logical-weight subclass result is promoted to an exact claim. The fast one/two-residual pool routines are witness-only. The static clause library is a precise family theorem, not full direct-360 completeness.

## 14. Process cleanliness and promotion

`process_accounting.json` is the complete FIX-2 ledger. No detached/background process or compute handoff was used. Both long proof attempts were foreground and stopped cleanly. The seal scan found no running Python, Z3, SAT solver, proof checker, or package process. Two interrupted wrapper shell return codes were not retained; their serialized status is `ERROR`, their proof count is zero, and they have no evidentiary use.

Exactly one repository path was created for this round: this package directory. No canonical node, scheduler, protocol, prior package, review, tool, or generated view was edited by this worker.

This package is proposer evidence for fresh review. It does not authorize changing any canonical status.
