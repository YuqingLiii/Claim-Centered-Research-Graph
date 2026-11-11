# Gross direct-360 proof-logging frontier, round 68

**Date:** 2026-08-29  
**Target:** `CIRCDIST.gross#gap-via-lift`  
**Package role:** proposer-grade checked computation for fresh independent exact review  
**Canonical state:** read-only; this package licenses no node, route, scheduler, protocol, review, or generated-view edit

## 0. Verdict

# **3) MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**

The exact root remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

One exact unrestricted outer candidate was selected after asserting every sound retained clause available at the round-63 frontier: all 1,440 globally checked five-atom single-residual clauses and all 20 raw-replayed round-62 order-region blocks. No member of the exploratory 15,874-clause pair-pattern collection was used. The candidate is legal, MC-valid, compressed, and globally interleaved.

Complete direct-360 DIMACS queries were emitted for both sectors, including complete column, variable, and clause dictionaries. Foreground CaDiCaL 1.9.5 proof-logging runs, each with a 600-second explicit wall limit, returned `SAT`:

| sector | variables | clauses | DIMACS SHA-256 | result | solver time | raw witness |
|---|---:|---:|---|---|---:|---|
| `Xerr` | 5,913 | 22,232 | `23baae8614d921d1289dbeff77c8ef893007b35e7b97cbd9f3c693d28bd86ecb` | SAT | 3.90 s | 10 faults, raw verified |
| `Zerr` | 5,969 | 22,456 | `ef7401f7d05e6e7ce84c6bcb07eecdfbfaecdff65d653b97529bea7d54a6022d` | SAT | <0.01 s | 8 faults, raw verified |

Every primary and auxiliary assignment literal was parsed, all DIMACS clauses were independently evaluated, and each selected mechanism was rebuilt from the candidate's raw CNOT times. The physical suffix residual has zero opposite-check syndrome and nonzero logical parity in each sector. The candidate is therefore killed, not a distance-12 witness.

Because both direct queries are SAT, there is no absence-side UNSAT claim and no candidate-specific DRAT/LRAT proof to check. The commission's gate was obeyed: arbitrary-round repair was not entered. The two positive mechanisms produced sound exact outer blocks. Five further exact outer iterations then yielded ten more raw-replayed positive mechanisms and ten more sound blocks. That continuation is positive CEGAR progress only; it is not an exhaustion.

## 1. Disk and inherited-package binding

`SOURCE_BINDINGS.json` binds 49 current repository paths expanding to 424 files. It includes the current protocols, frozen problem, scheduler, all repository paths directly bound by canonical `CIRCDIST.gross`, the Gross premise nodes, the lift premise, hunts 1–3, candidate/certification evidence and reviews, and both sealed CEGAR packages.

Both inherited manifests pass byte-for-byte:

- round 62: all 26 manifest entries pass, its verifier replays 20 schedules, 20 witnesses, 190 prior-block exclusions, both 1,884-word pools, and named/negative controls;
- round 63: all 24 manifest entries pass; the sealed `--full-static` replay reconstructs 1,440 clauses, 103,680 local-order cases, and 7,200 atom-deletion controls.

The round-63 verifier's optional live-binding mode now rejects two advanced files, as it should: the Gross node and scheduler changed after round 63. `BINDING_DRIFT.json` records old and current hashes. Disk wins. The three normalized load-bearing Gross texts are unchanged:

| text | characters | SHA-256 |
|---|---:|---|
| root claim | 586 | `fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180` |
| candidate implication | 300 | `4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598` |
| gap implication | 279 | `915109fe708c63ce138b11d07aa87c3048d676c87d9d6b7a80d68c0e2025c5d1` |

The sealed round-63 static result is therefore reused in its proved scope, while current governing bytes are separately bound. No stale byte hash is silently treated as current.

## 2. Frozen algebra and unrestricted outer model

Let

\[
G=\mathbb Z_{12}\times\mathbb Z_6,\qquad
A=\{(3,0),(0,1),(0,2)\},\qquad
B=\{(0,3),(1,0),(2,0)\}.
\]

For `g in G`, X check `g` acts on `g+A` in the left 72-qubit half and `72+g+B` in the right half. Z check `g` acts on `g-B` and `72+g-A`. The rebuild gives `rank(H_X)=rank(H_Z)=66`, `k=144-66-66=12`, 72 checks of each type, 864 distinct named CNOTs, and 648 nonempty X/Z overlaps, each of size two. Both frozen weight-12 logical pools expand to exactly 1,884 words; each pool supplies a 12-dimensional quotient basis, and the X/Z logical pairing has rank 12.

The candidate-selection SMT model has one integer `t(e)` for every named edge and imposes:

1. `0 <= t(e) < 864`;
2. distinct times on the six CNOTs of each check ancilla;
3. distinct times on the six CNOTs incident to each data qubit;
4. for every two-qubit overlap `{q0,q1}`,
   \[
   [t(Z,b,q_0)<t(X,a,q_0)]\iff[t(Z,b,q_1)<t(X,a,q_1)];
   \]
5. negations of all-X-before-all-Z and all-Z-before-all-X.

Disjoint gates may share a layer. The 864-value time domain is lossless because increasing compression of any finite legal schedule preserves every equality and strict comparison used by conflicts, MC, local residual support, voltage, and interleaving. No depth cap, tiling, translation invariance, order family, check-count cap, logical-weight stratum, or symmetry quotient occurs.

The complete SMT-LIB object is `candidate/candidate_outer.smt2`. The chosen candidate has SHA-256

```text
4a6d61d23b1e3655cdd10f31189827e6f8a22168bb0a815525517e703c32ba29
```

and the raw audit is:

```text
864/864 named edges
122 used layers, exactly 0..121
0 shared-node conflicts
0/648 MC violations
globally X/Z interleaved
13/648 overlap-support pairs interleaved
67/648 whole-check pairs interleaved
```

`candidate/candidate.json` contains every raw edge time, every X and Z within-check order with times, both full 360-column dictionaries, the complete pool/basis bindings, and the audit. The candidate falsifies every antecedent of all 1,460 asserted sound blocks. `candidate/global_single_clause_certificates.json` retains the full 1,440-clause ledger rather than only round 63's aggregate digests.

## 3. Clause retention discipline

The asserted outer blocks were exactly:

- 720 round-63 five-atom clauses in `Xerr`;
- 720 round-63 five-atom clauses in `Zerr`;
- 20 round-62 source-schedule blocks, each replayed from its raw direct witness.

The static clause semantics are

\[
A\Longrightarrow \exists\text{ direct mechanism of weight }\le 10,
\]

where `A` is a conjunction of five within-check comparisons. Its sound outer clause is `not A`. The full local proof checks all `6!` orders for every check and records a weight-12 pool completion for every order in the retained region. Every retained atom is deletion-minimal, witnessed by an exposed good order when deleted.

The 15,874 pair-pattern clauses from the bounded round-63 experiment were not loaded, consulted as an absence oracle, or used to choose the candidate. Their missing raw schedule/clause/exclusion ledgers remain a hard retention boundary.

## 4. Direct-360 query and DIMACS encoding

For local hook order `(i1,...,i6)`, earliest first, each sector uses 144 singleton columns and three residual columns per hook check:

\[
\{i_1,i_2\},\qquad \{i_4,i_5,i_6\},\qquad \{i_5,i_6\}.
\]

The first is the canonical representative of the physical four-suffix `{i3,i4,i5,i6}` and retains that physical suffix's voltage. The other two are physical three- and two-suffixes. Each sector therefore has 360 columns, including 216 distinct residual supports of weight two or three.

For primary selections `x_j`, the complete query is

\[
\sum_{j=0}^{359}x_j\le10,
\]

\[
\bigoplus_{j:(s_j)_b=1}x_j=0\quad(b=0,\ldots,71),
\]

\[
\bigvee_{r=0}^{11}\left(\bigoplus_{j:\langle c_j,\ell_r\rangle=1}x_j\right)=1.
\]

Binary XORs use a four-clause equivalence. The nonzero logical condition has twelve explicit parity-output variables. Cardinality uses an exact prefix-threshold recurrence: `s(i,j)` is equivalent to “at least `j` of the first `i` primaries are true,” with every overflow `s(i-1,10) and x_i` forbidden. Exhaustive controls cover all assignments for `(n,k)=(5,1),(5,2),(6,5)` and all eight binary-XOR output rows.

For each sector:

- `*.cnf` is the exact DIMACS;
- `*.columns.json` names all 360 columns and their canonical/physical supports, syndromes, and voltage options;
- `*.variables.json` names every primary, parity, XOR, and cardinality variable;
- `*.clauses.jsonl` gives every clause ID, literal list, derivation family, and context;
- `*.summary.json` binds dimensions and hashes.

There is no 1,884-pool, residual-pattern, check-count, logical-support-weight, or order-family restriction in either DIMACS.

## 5. Solver, checker, and proof discipline

The exact solver source is preserved as `tooling/cadical-rel-1.9.5-source.tar.gz`:

```text
remote  https://github.com/arminbiere/cadical.git
commit  146207318796f094dcded87349a64f0c6927309e
tree    185d31987f2c0ca947f2735fd4a7b3a624f8f030
version 1.9.5
binary  fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9
build   ./configure ; make -j1
```

The included binary is the exact binary used for the retained direct runs. Its full upstream test suite passed; `tooling/cadical_make_test.log` records 35/35 usage tests, 77/77 regression traces, API tests, and 1,000/1,000 model-based traces.

The independent checker source is separately preserved as `tooling/drat-trim-source.tar.gz`:

```text
remote    https://github.com/marijnheule/drat-trim.git
commit    2e3b2dc0ecf938addbd779d42877b6ed69d9a985
tree      b4e75a5f8c89d664652727458369cb5e0b610e31
drat bin  f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47
lrat bin  bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea
```

This is a distinct source tree and code path, not CaDiCaL reprinting its own result.

Exact retained direct commands, relative to this package, were:

```text
tooling/cadical-1.9.5-arm64-macos -t 600 --no-binary direct360/Xerr.cnf solver/Xerr.replay.drat
tooling/cadical-1.9.5-arm64-macos -t 600 --no-binary direct360/Zerr.cnf solver/Zerr.replay.drat
```

Both exited 10 with `s SATISFIABLE`. The compressed `.drat.gz` files are SAT-run traces, not UNSAT certificates; no checker acceptance is claimed for them. Their uncompressed SHA-256 values are:

```text
Xerr cabff801a919ed181b8fe370799c9aedebb6ce1ef8d5a243df751609afb1a479
Zerr abedaf6e08d514378443ed7c5607127cb2140d27b25f361bf51c2e46dd9f069c
```

The strict absence rule was applied literally: only solver `UNSAT` plus independent proof acceptance could establish absence. Neither direct formula is UNSAT. `UNKNOWN`, timeout, interruption, missing proof, or an unchecked trace carries no absence verdict.

## 6. Raw Xerr mechanism

The selected ten direct columns are

```text
D:84, D:139, D:140,
R:32:1, R:33:2, R:34:2, R:41:1, R:44:2, R:46:0, R:46:1
```

This is three singleton faults and seven physical hook faults on checks 32, 33, 34, 41, 44, and 46, with two distinct hook locations on check 46. The canonical net has support

```text
{33,36,42,47,50,51,52,59,62,64,84,115,116,117,118,125,128,130,139,140}
```

and weight 20. Replacing every canonical residual by its actual physical suffix read from the raw within-check order gives

```text
{33,36,50,51,52,59,62,84,116,117,118,124,125,128,139,140}
```

of weight 16. Both have zero `H_Z` syndrome and logical parity

```text
(1,1,0,0,1,0,0,0,1,0,0,0).
```

The canonical-to-physical differences are X-check stabilizers, so syndrome and logical class agree exactly. `verification.json` lists each hook's check, residual kind, physical suffix positions, qubits, raw six-edge order, and raw times. The preserving antecedent has 53 unique strict comparisons; its negation is a sound exact outer block.

## 7. Raw Zerr mechanism

The selected eight direct columns are

```text
D:138, D:140, D:141, D:143,
R:6:2, R:8:2, R:9:2, R:11:2
```

This is four singleton faults and four physical two-suffix hooks, one on each of Z checks 6, 8, 9, and 11. Canonical and physical net supports coincide:

```text
{66,68,69,71,132,134,135,137,138,140,141,143}.
```

The net has weight 12, zero `H_X` syndrome, lies outside `rowspace(H_Z)`, and has logical parity

```text
(0,0,0,0,1,0,0,0,0,0,0,0).
```

The preserving antecedent has 32 comparisons; its negation is another sound exact outer block.

An independent Glucose42 run on the same complete Zerr DIMACS also returned SAT under a 60-second enclosing timeout. It found a different raw-verified ten-fault mechanism, so the SAT result does not depend on one CaDiCaL assignment.

## 8. Proof-checker controls

A nontrivial `PHP(6,5)` control has 30 variables and 141 clauses. The retained control chain is:

1. CaDiCaL, 60-second limit: `UNSAT`, exit 20, 140 conflicts;
2. `drat-trim`, separate binary, 60-second limit: `s VERIFIED`, and LRAT emitted;
3. `lrat-check`, separate checker path under a 60-second enclosing timeout: `c VERIFIED`;
4. DRAT truncated to its first 10 of 219 lines: exit 1, `s NOT VERIFIED`, `ERROR: no conflict`;
5. LRAT truncated to its first 10 lines: exit 1, `c NOT VERIFIED`.

The DRAT file has SHA-256 `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd`; the LRAT has `0723e34b24bfa7b1b8432f1606f5ba9c43e325e1c8e9eab6195b45d3cedcfd0f`.

One deliberately weaker corruption, deleting only the terminal empty-clause line, still verified. This is not hidden: the remaining proof already contained enough information for backward checking, so that line was redundant. The stronger truncation controls above demonstrate actual rejection. See `ATTACK_LEDGER.md`.

## 9. Retained CEGAR continuation

The two primary raw mechanisms were added as sound blocks. Starting with

```text
1,440 round-63 static clauses
   20 round-62 sound blocks
    2 primary round-68 blocks
```

five further exact outer models were solved. Every model is a full 864-edge legal, MC-valid, compressed, globally interleaved schedule. In every iteration, the positive one/two-residual weight-12-pool finder returned a raw-valid mechanism in each sector. All ten mechanisms were replayed against raw local orders and converted to exact support-preserving blocks. Every later schedule violates all earlier new block antecedents.

This continuation is deliberately labelled positive-only. The finder is incomplete for absence, and no `NO_WITNESS` outcome is promoted. It proves neither direct absence nor outer exhaustion.

## 10. Why the root does not close

The candidate fails before repair: it has direct effective logical mechanisms of weights 10 and 8. Therefore it cannot be a distance-12 schedule. The arbitrary-round repair layer is logically irrelevant for this candidate and was not run.

The twelve new round-68 blocks exclude twelve explicit order regions. Together with the 1,460 inherited blocks they remain negligible relative to the unrestricted outer order space. No checked outer UNSAT exists. A universal `D*=11` conclusion would require a complete checked exhaustion of every interleaved schedule not already covered by the reviewed noninterleaved theorem. One killed candidate and five positive continuation schedules do not supply that.

The result therefore narrows no root value:

\[
\boxed{D^*_{\mathrm{Gross}}\in\{11,12\}.}
\]

## 11. Reproduction

Create an external virtual environment with `requirements.txt`; do not install into the repository. From the package directory:

```text
PYTHONDONTWRITEBYTECODE=1 /path/to/venv/bin/python verify.py \
  --repo-root <repo>
```

The read-only verifier:

- checks the package manifest;
- checks all 49 live source bindings when `--repo-root` is supplied;
- rebuilds both 1,884 pools and logical bases;
- regenerates all 1,440 global clauses and all deletion controls;
- replays the 20 round-62 blocks and 190 exclusions;
- rebuilds the candidate and all direct columns;
- checks every DIMACS/dictionary row and every SAT assignment clause;
- raw-replays both primary and all ten continuation mechanisms;
- repeats the encoder truth-table controls;
- rechecks the independent Glucose SAT control;
- reruns positive and corrupted DRAT/LRAT controls with explicit timeouts.

`SHA256SUMS.txt` covers every package file except itself.

The repository structural check `python3 tools/proof_dag_check.py --problem circdist` exits 0. The repository evidence-closure check exits 1 because this intentionally unpromoted package and its contained evidence are not linked from a canonical node. Its complete output is retained. Editing a canonical node merely to make that check pass was outside the authorization and would have misrepresented the review state.

## 12. Review and dispatcher license

This package licenses the dispatcher or a fresh independent reviewer to state only:

- one clause-saturated unrestricted exact outer candidate was killed by complete direct-360 SAT witnesses in both sectors;
- the complete Xerr and Zerr DIMACS encodings and dictionaries are retained and raw replay clean;
- twelve new sound outer blocks were generated, including ten from a five-step positive continuation;
- the proof/checker toolchain accepts valid DRAT/LRAT and rejects strongly truncated proofs;
- no direct absence, repair absence, outer exhaustion, `D*=11`, or `D*=12` conclusion was obtained.

No canonical promotion is authorized. Even a future root-closing computation needs fresh independent exact review.

## 13. Required final verdict

# **MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**
