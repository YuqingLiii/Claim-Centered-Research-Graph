# Public mathematical derivation

## 1. Schedule model and online state

Let `E` be the 864 named check-data CNOT edges, with 72 X checks and 72 Z checks. A schedule is an integer map `t:E→Z`. Each six-edge check has a strict total local order. Incident gates cannot share a qubit-time; the 648 measurement-collision constraints are explicit. Compression replaces occupied layer labels by consecutive integers while preserving every comparison `t_e<t_f`. A candidate is accepted only after the global audit proves every edge occurs once, every check has six distinct local times, no collision occurs, and X/Z checks are globally interleaved.

An installed positive term is a conjunction `A(t)` of local order comparisons with a proved physical failure selector whenever `A(t)` holds. Its sound outer block is `¬A(t)`. If the installed generalized library before iteration `r` is `G_r` and exact dynamic blocks are `D_r`, the outer contains

```text
1,440 unary + 20 round-62 + |G_r| generalized + |D_r| exact blocks.
```

Round 74 starts with `|G_42|=5,306`, `|D_42|=84`. Only terms retained after the current candidate's complete validation enter `G_(r+1)`. Both exact source blocks enter `D_(r+1)`. Thus no later candidate is priced against stale state.

## 2. Complete direct-360 query

For a sector, let `H_D` be the detecting matrix, `H_S` its stabilizer span, and `L_0,…,L_11` quotient-dual logical tests from the complete 1,884-word pool. The schedule defines 360 elementary columns. Selection variables `x_j` are unrestricted except for

```text
Σ_j x_j ≤ 10,
H_D (⊕_{j:x_j=1} c_j) = 0,
(⟨⊕c_j,L_0⟩,…,⟨⊕c_j,L_11⟩) ≠ 0.
```

The prefix-threshold cardinality recurrence is an exact CNF encoding of `Σx_j≤10`. There is no pool, residual-pattern, check-count, or within-check order-family restriction. The CNF has 360 primary variables plus auxiliaries; every satisfying assignment is complete over the full variable range and is checked against every clause.

For hook kind `k`, canonical residual positions are

```text
R0=(0,1), R1=(3,4,5), R2=(4,5),
```

and physical suffix positions are

```text
P0=(2,3,4,5), P1=(3,4,5), P2=(4,5).
```

For each selected hook the sealed local order independently produces canonical support `c_j` and physical support `p_j`. The replay verifies

```text
H_D c = H_D p = 0,
logical(c)=logical(p)≠0,
c,p ∉ span(H_S),
number of selected elementary faults ≤10.
```

All 24 X/Z assignments pass. Canonical net support weight and physical net support weight may differ; neither is the elementary fault bound.

## 3. Exhaustive 720-order catalogs

For every participating sector/check pair, all `6!=720` permutations are materialized. Each record stores the order, all three canonical residual supports, all three physical suffix supports, their exact 72 syndrome bits and 12 logical bits, and any constructive unary completion. Round 74 materializes 111 catalogs and 79,920 local orders.

For every local option the checker proves the identity

```text
signature(canonical support) = signature(physical suffix),
signature(v) = H_D v || (⟨v,L_0⟩,…,⟨v,L_11⟩).
```

The positive weight-14 pool is constructed from every weight-12 word XOR every stabilizer row, filtered by exact validity and weight, then unioned with reviewed positive words. The reviewed initial pool contains 9,438 Xerr and 9,435 Zerr words; one new positive Zerr word enters the online union by iteration 44, so the final counts are 9,438 and 9,436. A failed completion search is recorded only as a positive-library miss and never as absence.

## 4. Exact selected-mechanism joint GF(2) relation

Fix one direct mechanism. Let `d` be the signature of its fixed data singletons. If participating checks are `c_1,…,c_m`, and the mechanism selects hook-kind multiset `K_c` at check `c`, define the contribution for local order `o` by

```text
σ_c(o) = ⊕_{k∈K_c} signature(residual(c,o,k)).
```

The physical construction uses the corresponding suffixes and has the same signature by the catalog identities. For allowed order domain `A_c`, all and only reachable signatures are

```text
S_0={d},
S_r={s⊕σ_(c_r)(o): s∈S_(r-1), o∈A_(c_r)},
R=S_m.
```

### DP exactness

Induct on `r`. `S_0` is exactly the fixed data signature. If `S_(r-1)` is exactly the signatures of all prefixes, every transition appends a real allowed order and hence creates a real prefix of length `r`. Conversely, every real prefix has a length `r-1` prefix in `S_(r-1)` and its last order appears in the transition. Deduplicating equal bit states loses no information because acceptance depends only on the final signature. Therefore `S_m` is the exact joint relation. No pair-independence assumption occurs.

A multi term is sound exactly when every `s∈S_m` has zero syndrome bits and nonzero logical bits. Forward and reverse atom deletion runs use this same exact test. Round 74 builds 24 joint relations and 48 raw forward/reverse terms.

## 5. Symbolic universal tuple proof

The retained `iter42-Xerr` multi term permits exactly 2,985,984 tuples. Instead of repeating a redundant Python loop over that product, the sealed proof is universal and factorized as follows:

1. every allowed order in every check domain is explicitly present in the 720-order catalog;
2. for each such order, canonical and physical selected-hook contributions have identical exact signatures;
3. the joint DP above exhausts every signature state and transition for the Cartesian domain;
4. every terminal state is zero-syndrome and logically nonzero;
5. for any tuple, a fixed selector takes the mechanism's data singletons and selected hook kinds at the tuple's actual orders; and
6. the exact tuple count is the product of the allowed-domain cardinalities.

Items 1–6 quantify over every tuple. The three stored sample selectors are readable examples only and carry no proof burden. This is a symbolic all-tuples proof, not sampling. The full verifier reruns the catalog construction, exact DP, minimization, semantic filtering, and certificate hashes byte-for-byte.

## 6. Conservative structural pair relation

For checks `(a,b)` and orders `(i,j)`, the positive relation is

```text
T_ab(i,j)=U_a(i) ∨ U_b(j) ∨ E_ab(i,j),
```

where `U` is an explicit unary completion and `E` is the union of explicit two-hook completions from the weight-12/positive-weight-14 catalogs. Each relation stores all 720 rows as exact 720-bit masks. Round 74 constructs 249 relations representing 129,081,600 cells: 65 relations have explicit pair positives, 184 are unary-only, 70 positive configurations cover 30,576 explicit positive cells.

A comparison conjunction on `(a,b)` induces masks `A,B`. It is retained only if

```text
∀i∈A, B⊆T_ab(i,*).
```

For every covered tuple the selector is constructed deterministically: the `a` unary witness, else the `b` unary witness, else a stored explicit pair completion. All 1,137,096 retained pair tuples are enumerated literally, producing canonical and physical 144-bit masks, checking zero syndrome/nontrivial quotient, and hashing the complete tuple stream.

## 7. Deletion minimality

Every seed is minimized in forward and reverse atom order. Removing atom `α` is allowed only if the exact pair test or exact joint DP remains sound. Each retained atom has a deletion control. For a pair term, deletion exposes a tuple outside the conservative positive relation. For a multi term, deletion exposes a tuple on which the fixed selected mechanism has an invalid terminal signature. There are 1,372 controls.

These countertuples prove finite-library or fixed-selector minimality only. They do not prove that no other physical mechanism exists.

## 8. Semantic duplicate and dominance filtering

A term is represented by sector and a 720-bit allowed-order mask for every constrained check; an omitted check means all 720 orders. Two terms are duplicates when these finite domains are equal. Sound term `U` dominates sound term `V` iff every tuple allowed by `V` is allowed by `U`.

Filtering is against the current installed library: the reviewed 5,306 starting terms plus retained terms from earlier round-74 iterations. Only installed terms whose checks are relevant to the current mechanism need evaluation; this is an exact semantic index, not sampling. Predecessors are never removed. Across the run:

```text
raw pair candidates                   140
raw exact multi candidates             48
duplicate-old                           0
duplicate-new                          31
dominated-old                           0
dominated-new                          23
retained                               134
merged generalized library           5,440
```

Exact pair-domain coverage differences give 1,098,444 library-relative new tuples. No high-dimensional global union count is claimed for the retained multi term; its exact total and semantic dominance are recorded instead.

## 9. Strict online induction

At iteration `r`, the recorded order is:

```text
fresh outer → independent schedule replay → X direct → Z direct
→ assignment/raw replay → two exact blocks
→ catalogs/pair/joint DP → deletion controls → tuple validation
→ semantic dedup → retained install → iteration r+1.
```

The after-state of each iteration equals the before-state of the next byte-for-byte. Therefore every outer after iteration 42 includes every earlier retained sound term. The final state has 5,440 generalized and 108 exact dynamic blocks, so iteration 54 would start with 7,008 blocks.

## 10. Limits and rejected directions

All twelve outers and all 24 direct sectors are SAT. Hence this package contains no candidate-specific Gross DRAT/LRAT proof, never enters arbitrary-round repair, and proves no exhaustion. The DRAT/LRAT files under controls only establish that the independent checkers accept a valid fixture and reject deterministic corrupt truncations.

The following implications are explicitly rejected:

```text
zero conservative pair cell       ⇏ physical absence,
no weight-12/weight-14 completion  ⇏ physical absence,
deletion countertuple              ⇏ physical absence,
SAT mechanism frequency            ⇏ completeness,
finite twelve-iteration limit       ⇏ outer exhaustion.
```

The result is checked positive progress. A fresh independent exact review is mandatory before canonical installation or restart.
