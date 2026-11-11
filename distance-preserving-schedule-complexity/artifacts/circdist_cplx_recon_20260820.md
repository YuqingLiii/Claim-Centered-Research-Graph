# CIRCDIST.cplx — route recon (Eff-Preserve complexity)

Session: Opus 5 executor / proposer, budget-boxed recon, 2026-08-20.
Target node: `CIRCDIST.cplx`, problem statement `research/circdist/notes/CIRCDIST_PROBLEMS.md` (课题三).
Scope of this file: candidate route registration, one decisive gate, external assumptions, and one
small self-contained result set. **Nothing here is labelled PROVED.** Arguments written out below are
at most CONJECTURED (blueprint quality, no independent review); computational statements are
NUMERICAL and name the script that produced them.

This file does not modify the proof-DAG. Route registration into
`research/circdist/proof-dag/nodes/CIRCDIST.cplx.yaml` is left to the dispatcher.

---

## 0. Executive summary

Three things came out of this session that change how the node should be attacked.

1. **The problem definition has three inequivalent variants and they have different complexity for
   different reasons.** Which one is meant must be fixed *before* any hardness attempt, because two
   of the three admit near-trivial hardness proofs that say nothing about hook errors (§1).
2. **In the depth-unbounded variant, `d_eff` depends only on the tuple of per-check local CNOT
   orders**, so Eff-Preserve becomes a pure CSP whose variables are the checks, whose domains are
   the `w!` local orders, and whose constraints have arity `≤ d-1` (§2). This is the structural
   backbone of every route below, and it immediately yields several results — including one that
   *contradicts a restriction the problem statement proposed as a hardness target* (§5, Prop. D).
3. **The unary-vs-coupling dichotomy is the whole ballgame, and it is now measured, not guessed.**
   On every structured `d=3` CSS code probed (rotated surface, 3×3 toric, unrotated/HGP surface,
   Steane and the quantum Hamming family) the induced CSP has **no** constraint coupling two
   different checks — it factorises, so those instances are decided in polynomial time. On random
   self-orthogonal CSS codes with weight-6 checks, coupling constraints are **generic** (56 of 71
   `d=3` instances). So the raw material for a hardness reduction exists but does *not* live in any
   of the standard code families. The decisive gate (§6) is exactly about turning that raw material
   into a *controllable* gadget.

---

## 1. Model variants — pin this down first

The statement gives: `H_X, H_Z`; a promised static distance `d`; an "allowed CNOT
interaction/conflict graph"; an optional depth bound `T`. Those last two are load-bearing.

**V1 (pure / recommended headline).** No depth bound; the only scheduling constraint is the physical
one — a qubit does at most one two-qubit gate per time step. Then the conflict graph on CNOTs is
exactly "shares a qubit", the CNOT graph is the Tanner graph (bipartite: data qubits vs. ancillas),
and *every* tuple of local orders is realisable (schedule the checks sequentially). All hardness must
then come from the code's linear algebra. **This is the version where a hardness theorem would be
about hook errors.**

**V2 (+ depth bound `T`).** Feasibility alone is still easy: a depth-`T` schedule is a proper
`T`-edge-colouring of the bipartite Tanner graph, so by König's theorem a schedule exists iff
`T ≥ Δ` and one is found in polynomial time (Assumption A6). But at or near `T = Δ` the set of
*realisable order tuples* is a Latin-square-like object, and edge-colouring with pre-committed edges
is NP-complete (Assumption A7). So V2 has a second, independent hardness source that has nothing to
do with distance. This is a lever (route `depth-bound-scheduling-lever`) *and* a trap.

**V3 (+ arbitrary conflict graph).** If the input may specify an arbitrary conflict graph among
CNOTs, then "is there a legal depth-`T` schedule at all" is graph colouring, NP-complete for `T ≥ 3`
(Assumption A8), and Eff-Preserve is NP-hard for reasons entirely unrelated to `d_eff`. Any
NP-hardness proof in V3 should be regarded as vacuous unless it survives restriction to V1.

**Recommendation.** Make V1 the canonical statement; state V2 as an explicitly separate theorem;
declare V3 out of scope or record its hardness as a degenerate remark. If the lead wants the
"each check allows only two or a few local CNOT orders" restriction of the statement, note that the
restriction is *not* expressible in V1 as a property of the code — it has to be either extra input
(which makes the reduction easier and the theorem weaker) or a consequence of V2 timing.

---

## 2. Structural backbone (used by every route)

Notation: for a check `c` with support `supp(c)` of weight `w_c` and a local CNOT order
`π_c = (q_1,…,q_{w_c})`, write `S_i(π_c) = {q_{i+1},…,q_{w_c}}` for the `i`-th proper suffix.

**Lemma 1 (column set).** In the single-ancilla, prepare-once/measure-once model, the set of terminal
residual data errors produced by *one* elementary fault is exactly

```
  { e_q : q a data qubit }  ∪  { S_i(π_c) : c a check, 1 ≤ i ≤ w_c − 1 }
```

in each Pauli sector (X-type residuals from X-check ancillas, Z-type from Z-check ancillas).
*Reason:* an ancilla fault at position `i` propagates to the suffix `S_i`; a two-qubit gate fault at
position `i` gives residual `S_i` or `S_i ∪ {q_i} = S_{i-1}` or `{q_i}`; a preparation fault gives the
full support, which is a stabiliser; a measurement flip perturbs syndrome only, and `d_eff` discards
intermediate syndrome by definition. So nothing outside the displayed set arises, and everything in
it does.

**Lemma 2 (order-determinacy).** In V1, `d_eff(M)` is a function of the tuple `(π_c)_c` alone — global
timing and X/Z interleaving are irrelevant. Immediate from Lemma 1. (This is precisely the property
that *fails* for `d_circ`; cf. node `CIRCDIST.lift`.)

**Lemma 3 (CSP form).** Under the promise `d(Q) = d`, `d_eff(M) = d` iff no multiset of at most `d−1`
columns from Lemma 1 sums to a vector `v` with `H_Z v = 0` and `v ∉ rowspace(H_X)` (X-sector; and the
mirror in the Z-sector). Hence Eff-Preserve in V1 is the CSP

* variables: one per check, `x_c`;
* domain: the `w_c!` local orders (equivalently, maximal chains in the Boolean lattice on `supp(c)`);
* constraints: for every choice of `≤ d−1` columns whose sum is a nontrivial logical, forbid the
  corresponding tuple of orders. Arity `≤ d−1`.

Call a constraint **unary** if it involves the orders of a single check, and **coupling** otherwise.
The two sectors are independent CSPs on disjoint variable sets.

**Lemma 4 (factorisation).** If a code's induced CSP has no coupling constraint, Eff-Preserve on that
code is decided in time `O(poly(n) · Σ_c w_c!)` — test each check separately. In particular it is
polynomial for bounded check weight, and FPT in `max_c w_c`.

---

## 3. What the numerics said (NUMERICAL)

Scripts (scratchpad, reproducible; ~200 lines total, pure Python):
`gate1.py`, `gate1b.py`, `gate2.py`, `gate3.py`, `hgp.py`. All at `d = 3` (fault budget 2 columns),
X-sector and mirror; exhaustive over local orders; "safe order" = no proper suffix `h` with `h`
logical, `h+e_q` logical, or `h+h'` logical for two suffixes of the same order.

| code | safe local orders per check | coupling constraints |
|---|---|---|
| rotated surface `[[9,1,3]]` | 16/24 on each weight-4 check; 2/2 on weight-2 | **0** (safe set is exactly the product, 1024 = 16·16·2·2) |
| 3×3 toric `[[18,2,3]]` | 24/24 on all nine weight-4 checks | **0** |
| unrotated planar surface `[[13,1,3]]` = HGP(rep₃,rep₃) | 24/24 and 6/6 — *all* orders safe | **0** |
| Steane `[[7,1,3]]` | **0/24 on every check** — instance is a NO | 0 (vacuous) |
| quantum Hamming `[[15,7,3]]` | **0/40320 on every check** — NO | 0 (vacuous) |
| random self-orthogonal CSS, `n∈{10..16}`, weight-6 checks, `d_X = 3` | varies | **coupling in 56 of 71 instances**, typically 400–600 forbidden order pairs |

Three readings:

* The HGP rows corroborate Manes–Claes distance-robustness (Assumption A1) and sharpen it: the
  *rotated* surface code is **not** distance-robust (8 of 24 orders per weight-4 check are bad) while
  the unrotated HGP one is. The rotated code is not a hypergraph product, so there is no conflict;
  but it is a useful reminder that "surface code" is ambiguous in this context.
* The structured codes are all *unary-only*. By Lemma 4 they are trivial instances. So no reduction
  can be built inside the standard families; hardness must use unstructured codes.
* Coupling is nevertheless generic once structure is dropped. That kills the most economical possible
  outcome ("coupling never happens ⇒ Eff-Preserve is in P for bounded weight") and keeps the
  NP-hardness target alive.

---

## 4. Routes

Six routes. `P` = probability the route implication eventually closes; `D` = sessions to the next
evidence level or to decisive failure. Estimates are scheduler-only, not evidence.

### R1 `order-csp-fixed-d-hardness` — (a) fixed-`d` NP-hardness via an ordering/colouring CSP

**Premises.**
* P1.1 Lemmas 1–3 (column set, order-determinacy, CSP form) in V1, written and reviewed.
* P1.2 *Coupling gadget with prescribed relation*: a CSS gadget `G` of bounded check weight and
  certified distance `d`, with two designated checks whose induced binary constraint is a specified
  non-product relation `R` (target: `≠` on a 3-element sub-domain, or a NAE-style ternary relation
  at `d = 4`).
* P1.3 *Padding / composition lemma*: gluing gadgets on disjoint qubit sets through a fixed connector
  creates no `≤ (d−1)`-column mechanism other than the union of the gadgets' own mechanisms.
* P1.4 *Distance certificate*: the composed family provably has static distance exactly `d`
  (needed for the promise; note computing it is itself NP-hard in general, Assumption A5).
* P1.5 NP-hardness of the target CSP in the bounded-occurrence/bounded-degree form actually produced
  (3-colouring of bounded-degree graphs, or NAE-3SAT, or Betweenness — Assumptions A3, A4).

**Implication sketch.** By P1.1 the instance is the CSP of Lemma 3. Map each CSP variable of the hard
source problem to one gadget copy from P1.2, each constraint to a shared-qubit connector; P1.3 says
the induced constraint set is exactly the image of the source constraints plus per-gadget unary
constraints, and P1.4 supplies the promise. Then a legal schedule with `d_eff = d` exists iff the
source instance is satisfiable, and the reduction is polynomial because gadgets have bounded size.
NP-membership for fixed `d` is Corollary 2 of §5.

**P = 0.35.** The mechanism is real and now measured (coupling is generic), and the CSP frame is
clean; the risk is entirely in P1.3+P1.4 — controlling *all* low-weight mechanisms of a composed code
is where reductions of this shape historically die, and the promise forces a distance certificate on
top. **D = 4 sessions** (1 for the gate of §6, 2 for gadget+padding, 1 for the write-up), assuming the
gate comes back positive.

*Sharpening from §5:* the reduction must target `(d = 3, domain ≥ 3)` or `(d ≥ 4, domain 2)`.
`(d = 3, domain ≤ 2)` is provably tractable in V1 (Prop. D), so aiming there is wasted effort.

### R2 `sigma2-upper-bound-clean` — (b, upper) rigorous `Σ_2^P` membership, promise handled

**Premises.** P2.1 Lemma 1. P2.2 the schedule is a polynomially bounded object. P2.3 `d_eff(M) ≤ d`
always (a min-weight logical of `Q` is a sum of `d` singleton columns and stays nontrivial in `E(M)`,
since `E(M)` adds error generators, not stabilisers).

**Implication sketch.** Written out in §5, Theorem 1. `∃M` (poly bits) `∀F` (a list of `< d` column
indices, `O(d log n)` bits) `[ sum(F) is not an undetectable nontrivial logical ]`, the matrix
predicate being Gaussian elimination. The promise is handled by replacing `= d` with `≥ d`, which
gives a **total** `Σ_2^P` language agreeing with the promise problem on all promise inputs.

**P = 0.9** — routine, and the argument is already drafted below; the only work left is review. (Above
the CONJECTURED band of `VALUATION_PROTOCOL` §5; the adjustment is justified by the argument being
textbook-shaped and complete.) **D = 0.5 sessions.**

### R3 `qsat2-budget-gadget-hardness` — (b, lower) `Σ_2^P`-hardness from QSAT₂

**Premises.**
* P3.1 R1's gadget machinery, at unbounded `d` (existential layer: order choices ↦ `x`-variables).
* P3.2 *Universal-layer encoding*: a construction in which the fault budget `d−1` forces the adversary's
  `(d−1)`-subset to pick exactly one column from each of `m` designated groups, so that a
  `(d−1)`-subset encodes an arbitrary assignment `y ∈ {0,1}^m`.
* P3.3 *Clause realisation under linearity*: since "F is an undetectable nontrivial logical" is an
  `F_2`-linear predicate (plus one non-membership), the clause structure must come from the weight
  budget and group structure, in the style of Berlekamp–McEliece–van Tilborg / Vardy (Assumption A5),
  not from the predicate.
* P3.4 `Σ_2^P`-completeness of QSAT₂ (Assumption A2).

**Implication sketch.** Build a code whose columns are partitioned into `m` groups of two, one per
universal variable, plus clause-checking structure; the ancilla orders of designated checks toggle
which columns are available (existential variables). Arrange that a `(d−1)`-subset is an undetectable
logical iff its induced `(x,y)` falsifies `φ`. Then `∃M : d_eff(M) = d` iff `∃x ∀y φ(x,y)`.

**P = 0.15.** Two hard layers stacked, and the linearity of the acceptance predicate (P3.3) is a real
structural obstruction: everything nonlinear must be smuggled into the budget/group combinatorics
while the distance promise is simultaneously certified. Reference class: coding-theoretic
second-level completeness results are rare and long. **D = 6 sessions.**

### R4 `covering-radius-transfer` — (b, lower, alternative technique)

**Premises.**
* P4.1 `Π_2`-completeness of the covering radius problem for linear binary codes (Assumption A9),
  and the technique used to prove it.
* P4.2 A dictionary sending "for every syndrome there is a nearby codeword" to
  "for every low-weight fault set the residual is detectable-or-trivial", i.e. an identification of
  the schedule's degree of freedom with a code-modification degree of freedom in the covering-radius
  instance.
* P4.3 Closure of the constructed instances under the static-distance promise.

**Implication sketch.** CRP is the canonical natural `Π_2`-complete coding problem, with exactly the
`∀∃` shape whose complement matches Eff-Preserve's `∃∀`. If the schedule freedom can be encoded as a
choice of coset representatives / a choice of parity-check rows, the CRP hardness gadgetry transfers
and gives `Σ_2^P`-hardness without inventing the universal-layer encoding of R3 from scratch.

**P = 0.2.** Attractive because it imports an existing second-level lower bound instead of building
one, but P4.2 is speculative: the schedule freedom is a *chain-in-a-Boolean-lattice* freedom, not a
linear-algebraic one, and I did not find a natural map. Also, the attribution of the linear-code
`Π_2`-completeness needs primary-source verification (Assumption A9 caveat). **D = 5 sessions.**

### R5 `depth-bound-scheduling-lever` — V2 hardness through the timing layer

**Premises.**
* P5.1 Lemma 3 restricted to V2: the CSP of §2 plus a realisability predicate
  "the order tuple extends to a proper `T`-edge-colouring of the Tanner graph".
* P5.2 *Unary order-forcing gadget*: a code where the unary constraints of a check force a prescribed
  precedence "`q` before `q'`" (achievable if every subset containing `q` and not `q'` is dangerous —
  Lemma 3 makes this a linear-algebra design problem, and unlike P1.2 it needs no coupling).
* P5.3 NP-hardness of bipartite edge-colouring with pre-committed/precedence constraints at `T = Δ`
  (Assumption A7 — Latin square completion; the precedence form still needs a citation or a proof).

**Implication sketch.** Use P5.2 to pin down parts of the colouring, then P5.3 to make the residual
timing question NP-hard. Distance is used only to *install* the precedence constraints, not to create
the hardness.

**P = 0.55** for the theorem as stated; but read the caveat. This is by far the easiest NP-hardness to
obtain, and by far the least informative — a referee will ask whether the result is about hook errors
at all. Register it as a **secondary/contrast** theorem, and never as the headline. **D = 2 sessions.**

### R6 `tractable-islands-and-factorisation` — (c) the third minimal-acceptance branch

**Premises.**
* P6.1 Lemma 4 (factorisation ⇒ poly) — argued above.
* P6.2 *Structured families are unary-only*: for HGP codes (and their higher-dimensional versions),
  every schedule is distance preserving, so Eff-Preserve is the constant YES on that class
  (Assumption A1). Verified numerically here for HGP(rep₃,rep₃) and the 3×3 toric code.
* P6.3 *Bounded-treewidth FPT*: for Tanner graphs of treewidth `≤ t`, check weight `≤ w`, and fixed
  `d`, the whole `∃orders ∀faults` statement is expressible in counting-MSO over the Tanner graph
  (order choice = a bounded vertex labelling; "even overlap with every check" and "not a sum of check
  neighbourhoods" are CMSO), so Courcelle's theorem gives a linear-time FPT algorithm (Assumption A10).
* P6.4 Prop. D of §5: `d = 3` with at most two allowed local orders per check is 2-SAT in V1.

**Implication sketch.** Each premise is an independent polynomial/FPT algorithm on a nontrivial
restricted class, which is one of the three minimal acceptance conditions of the node.

**P = 0.7.** P6.1, P6.4 are essentially done; P6.2 is a citation plus a scope check; P6.3 is standard
machinery with one honest caveat — bounded treewidth plus bounded check weight constrains `k·d²`
(Assumption A11), so the island may only be non-vacuous in the fixed-`d` regime. **D = 2 sessions.**

### Addendum A1 (optional, statement 课题三's "可选扩展") `circ-preserve-parity`

Circ-Preserve (`∃M : d_circ(C(M)) = d`) is *also* in `Σ_2^P` by the same argument: a fault set of
`< d` circuit locations is a poly-length certificate and "triggers no detector but flips a logical" is
linear algebra over the detector matrix. So the two problems sit at the same upper bound, and the
interesting question is whether the *lower* bounds differ. Concretely: the CSP of Lemma 3 is the
`d_eff` shadow of a strictly finer object for `d_circ`, because Lemma 2 fails — interleaving matters.
Conjecture worth registering: Circ-Preserve is at least as hard as Eff-Preserve under the reduction
that pads the code so that intermediate detectors are inert; the converse is open and is really a
`CIRCDIST.lift` question. **P = 0.5, D = 2**, but only after `CIRCDIST.lift` has a usable criterion.

---

## 5. Small concrete result set (labelled CONJECTURED / NUMERICAL — not PROVED)

### 5.1 Formal definition, promise handled

Fix the V1 model. Input: `H_X ∈ F_2^{m_X × n}`, `H_Z ∈ F_2^{m_Z × n}` with `H_X H_Z^T = 0`; an integer
`d ≥ 1`. Promise: the CSS code `Q(H_X,H_Z)` has minimum distance exactly `d` and `k ≥ 1`.
A **schedule** `M` assigns to each check `c` a linear order `π_c` of `supp(c)` (Lemma 2 makes any
finer notion redundant in V1). Define the **extended column set** `Cols(M)` by Lemma 1 and

```
  d_eff(M) = min { |F| : F ⊆ Cols(M) a multiset, Σ F ≠ 0,
                         Σ F undetectable (H_Z-orthogonal in the X sector, H_X-orthogonal in Z),
                         Σ F ∉ rowspace of the same-type check matrix }.
```

`Eff-Preserve` = { (H_X,H_Z,d) satisfying the promise : `∃M, d_eff(M) = d` };
NO-instances are promise-satisfying inputs with `∀M, d_eff(M) < d`.

**Total surrogate.** `Eff-Preserve≥` = { (H_X,H_Z,d) : `∃M, d_eff(M) ≥ d` } is a total language that
agrees with `Eff-Preserve` on every promise input, because `d_eff(M) ≤ d` always (Lemma 5 below).
All upper bounds should be stated for `Eff-Preserve≥`; all hardness must construct promise-satisfying
instances.

**Lemma 5 (CONJECTURED).** `d_eff(M) ≤ d(Q)` for every `M`. *Argument:* a minimum-weight nontrivial
logical `L` of `Q` is the sum of `d` singleton columns, all of which lie in `Cols(M)`; adding hook
columns to `E(M)` enlarges the error generator set but leaves the stabiliser group and hence the
nontriviality of `L` unchanged.

### 5.2 Theorem 1 (CONJECTURED): `Eff-Preserve≥ ∈ Σ_2^P`

*Proof sketch, fully written.* Write `N = Σ_c w_c ≤ n·max_c w_c`, polynomial in the input.

*Existential block.* A schedule is the tuple `(π_c)_c`, encoded in `Σ_c ⌈w_c log w_c⌉ = O(N log N)`
bits. Legality in V1 is the single syntactic condition that each `π_c` is a permutation of `supp(c)` —
checkable in linear time. (In V2 the existential block additionally carries the time assignment,
still `O(N log T)` bits, and legality is the linear-time check that no qubit repeats within a step.)

*Universal block.* By Lemma 1, `|Cols(M)| ≤ n + N`, and each column is named by `O(log(n+N))` bits.
A candidate mechanism is a multiset `F` of at most `d−1 ≤ n−1` column names, i.e. `O(n log(n+N))`
bits — polynomial. Note `d ≤ n`, so no encoding blow-up even when `d` is part of the input.

*Predicate.* Given `M` and `F`, compute `v = Σ F ∈ F_2^n` in time `O(|F|·n)`. Then:
`v ≠ 0`; `H_Z v = 0`; `v ∉ rowspace(H_X)` — the last by Gaussian elimination on `H_X` once, then a
reduction of `v`, total `O(n^3)`. `v` is an undetectable nontrivial logical iff all three hold. The
mirror computation handles the Z sector. So the predicate is polynomial-time.

*Assembly.* `M` witnesses `d_eff(M) ≥ d` iff no `F` with `|F| ≤ d−1` yields an undetectable
nontrivial logical, i.e. `∃M ∀F ¬R(M,F)` with `R` polynomial-time and both blocks polynomially
bounded. That is the definition of `Σ_2^P`. ∎

**Corollary 1 (CONJECTURED).** Under the promise, Eff-Preserve is in `Σ_2^P` as a promise problem.

**Corollary 2 (CONJECTURED).** For every fixed constant `d`, `Eff-Preserve ∈ NP`: the universal block
ranges over `O((n+N)^{d-1})` sets, so verification of a guessed `M` is polynomial. With bounded check
weight, verification is `O(poly(n))` with the exponent independent of `w`.

### 5.3 Proposition A (CONJECTURED + NUMERICAL): quantum Hamming codes are NO-instances

Let `r ≥ 3` and let `Q_r` be the CSS code `[[2^r−1, 2^r−1−2r, 3]]` built from the `[2^r−1, 2^r−1−r, 3]`
Hamming code `C_r` with `H_X = H_Z = H_r` (valid since the simplex code `C_r^⊥` is self-orthogonal).
Then **no** schedule preserves the effective distance: `d_eff(M) ≤ 2` for every `M`.

*Argument.* Each check has weight `2^{r−1} ≥ 4`, so every local order has a proper suffix `A` of size 2,
say `A = {i,j}`. The Hamming parity-check columns satisfy `h_i + h_j = h_k` for a unique third
coordinate `k ∉ {i,j}`, so `{i,j,k}` is a weight-3 codeword of `C_r = ker(H_r)`, hence undetectable;
and it is not a stabiliser because `rowspace(H_r) = C_r^⊥` is the simplex code, all of whose nonzero
weights are `2^{r−1} ≥ 4 > 3`. Therefore the hook `X_A` (one ancilla fault) together with the single
data fault `X_k` is an undetectable nontrivial logical of extended weight 2 < 3. ∎

Verified exhaustively for `r = 3` (Steane, 0 of 24 orders survive on each check) and `r = 4`
(`[[15,7,3]]`, 0 of 40320) by `gate1.py`/`gate2.py`. Generalisation worth registering: *any* code in
which every 2-subset of some check support extends to a weight-3 nontrivial logical is a NO-instance —
a 2-design/pair-covering condition. NO-instances of Eff-Preserve are therefore easy to exhibit, which
matters for R1: a hardness reduction must avoid accidentally producing them.

### 5.4 Proposition D (CONJECTURED): the statement's proposed hardness restriction is tractable

In V1, with `d = 3` fixed and at most two allowed local orders per check, Eff-Preserve is in P.

*Argument.* At `d = 3` the fault budget is 2 columns. Two singleton columns cannot form a logical
(static distance 3). So every constraint of Lemma 3 involves at most two hook columns, hence at most
two checks: arity `≤ 2`. With domain size 2 per check, identify each variable with a Boolean literal;
each forbidden pair becomes a 2-clause and each forbidden value a unit clause. In V1 every order tuple
is realisable, so Eff-Preserve is exactly the satisfiability of this 2-CNF, decidable in linear time. ∎

**Consequence for the programme.** 课题三 proposes "each check allows only two or a few local CNOT
orders" together with "fixed `d = 3`" as a target for a *strong* NP-completeness theorem. In V1 that
target is provably out of reach. The hardness frontier is instead:

| | domain ≤ 2 | domain ≥ 3 |
|---|---|---|
| `d = 3` (arity ≤ 2) | **P** (2-SAT, Prop. D) | open — 3-colouring-shaped, R1 target |
| `d ≥ 4` (arity ≤ 3) | open — NAE/1-in-3-shaped, R1 target | open |

(The general finite-domain CSP dichotomy, Assumption A12, says every fixed constraint language is P
or NP-complete, so the question is precisely *which* relations are realisable by CSS gadgets — that
is the content of the gate in §6.)

### 5.5 Proposition E (NUMERICAL): structured codes factorise, unstructured ones do not

As tabulated in §3. Stated carefully: for the five structured `d = 3` codes probed, the induced CSP has
no coupling constraint, so by Lemma 4 those instances are decided in time polynomial in `n` and
`max_c w_c!`; whereas 56 of 71 random self-orthogonal weight-6 CSS codes with `d_X = 3` do carry
coupling constraints, with an explicit witness recorded in `gate3.py`'s output, e.g. checks with
supports `(2,3,6,7,8,9)` and `(1,2,4,8,10,11)` whose locally safe suffixes `{2,8,9}` and `{2,11}` sum
to the nontrivial logical `{8,9,11}`.

---

## 6. The single cheapest decisive gate

**Gate name: `controllable-coupling-gadget`.**

The gadget lemma named in the commission — *a tiny CSS family where two CNOT orders of one check flip
whether a specific weight-`(d−1)` hook fault is detectable* — is a warm-up and **this session already
discharged it**: on the rotated `[[9,1,3]]` surface code, 8 of the 24 orders of a weight-4 check
produce a weight-2 hook contained in a weight-3 logical and 16 do not, so one check's order flips
`d_eff` between 2 and 3; and Prop. A gives an entire family where *every* order fails. Neither outcome
is decisive, because both are **unary** phenomena and Lemma 4 says a problem with only unary
constraints is polynomial.

The decisive object is therefore the *coupling* gadget, and specifically a **controllable** one.

**What to construct.** A CSS gadget `G` on `O(1)` qubits with check weight `≤ 6` and certified static
distance `d = 3` (or 4), containing two designated checks `c₁, c₂`, such that:

1. **(non-product)** the induced binary relation `R ⊆ D₁ × D₂` on their locally safe order sets is not
   a product `A₁ × A₂` — *already known to be achievable* (§3, `gate3.py`), but not yet with a
   certified distance and a controlled `R`;
2. **(prescribable)** `R`, together with the unary constraints and a fixed set of "wiring" identifications
   of gadget qubits, primitively positively defines a relation known to make binary CSP NP-hard —
   concretely `≠` on a 3-element sub-domain (`d = 3`), or a NAE-style ternary relation (`d = 4`);
3. **(paddable)** two copies of `G` glued on disjoint qubit sets through the wiring create no
   `≤(d−1)`-column mechanism beyond the union of each copy's mechanisms and the intended wiring
   constraints — i.e. no spurious low-weight logicals appear on composition;
4. **(certified)** the composed code's static distance is provably exactly `d`, so the promise holds.

**Cost.** One session. Items 1–2 are an exhaustive search over a designed family (the probe code in
`gate3.py` already does 71 codes/minute at weight 6, `d = 3`); item 3 is a two-copy exhaustive check;
item 4 is where a hand proof is needed and is the only part that is not a script.

**What each outcome implies.**

* **All four hold.** R1 drops from "invent a reduction" to "write a construction": fixed-`d`
  NP-completeness becomes a laborious but conventional gadget argument, and R3's existential layer is
  unlocked (`P(R1)` → ~0.6, `P(R3)` → ~0.3). Next action: pick the source problem by the table in
  §5.4 and build the wiring.
* **1–2 hold but 3 fails** (gluing always manufactures spurious low-weight logicals). The local
  gadget/pp-definability strategy is dead; the reduction must instead be global — e.g. build the whole
  code by one algebraic construction (hypergraph-product-of-a-hard-instance in the style of the
  recent quantum-distance hardness reductions, Assumption A5) so that distance and mechanism control
  come from a single theorem rather than from composition. `P(R1)` → ~0.2, `D(R1)` → 6+; R5 becomes
  the realistic near-term NP-hardness result and should be re-priced upward.
* **2 fails in a strong form** — every realisable binary relation over safe-order domains is closed
  under a majority/near-unanimity operation, i.e. "2-SAT-like". Then by the CSP dichotomy
  (Assumption A12) Eff-Preserve at fixed `d` and bounded check weight is **in P**, and the node's
  NP-completeness target is refuted for that regime. This is a genuine possible outcome — every
  structured code probed this session landed in the degenerate (unary-only) case — and it would be a
  publishable positive result, not a failure.
* **4 fails only** (relations fine, distance not certifiable). Fall back to reductions whose output
  distance is inherited from a classical code with known distance; note the promise cannot simply be
  dropped, since verifying it is itself NP-hard (Assumption A5).

**Why this is the cheapest decisive gate.** It is the unique yes/no question whose two answers send
the node to two different *theorems* (NP-completeness vs. a tractability dichotomy) rather than to
"keep trying"; it is settled by an exhaustive search over `O(1)`-size objects; and Lemma 4 makes it
logically necessary — no NP-hardness proof of any shape can exist without a coupling constraint.

---

## 7. Load-bearing external results (ASSUMPTIONS)

Format: exact statement, source, and my verification status this session. "Verified" = I looked at the
source or an authoritative secondary description during this session; "standard, not re-verified" =
textbook material I am confident of but did not re-check; "**needs primary check**" = flagged.

**A1 (HGP distance robustness).** *Hypergraph product codes are distance-robust: any single-ancilla
stabiliser measurement circuit preserves the effective distance; and the depth-optimal circuit of
Tremblay–Delfosse–Beverland is also effective-distance-optimal.* — A. G. Manes, J. Claes,
"Distance-preserving stabilizer measurements in hypergraph product codes", **Quantum 9, 1618 (2025)**,
arXiv:2308.15520. *Verified* (journal page fetched). *Caveat:* I read the abstract-level statement,
not the theorem's hypotheses; before this is used as a premise of R6, someone must check whether
"any circuit" is unconditional or carries conditions on the classical seed codes. Corroborated
numerically here for HGP(rep₃,rep₃) and the 3×3 toric code. Related and **unverified in scope**:
arXiv:2409.02193, "Effective distance of higher-dimensional HGPs and weight-reduced quantum LDPC
codes", which reportedly extends this to higher-dimensional HGPs under any single-ancilla schedule.

**A2 (QSAT₂).** *`QSAT_2 = { φ : ∃x ∀y φ(x,y) }` with `φ` a 3-DNF (equivalently `∃x ∀y ¬ψ`, `ψ` a
3-CNF) is `Σ_2^P`-complete under polynomial-time many-one reductions.* — L. Stockmeyer, "The
polynomial-time hierarchy", TCS 3 (1976) 1–22; C. Wrathall, "Complete sets and the polynomial-time
hierarchy", TCS 3 (1976) 23–33. *Standard, not re-verified.*

**A3 (Betweenness).** *Given a finite set and a collection of triples `(a,b,c)`, deciding whether a
total order exists in which `b` lies strictly between `a` and `c` for every triple is NP-complete.* —
J. Opatrný, "Total ordering problem", SIAM J. Comput. 8(1) (1979) 111–114. *Verified* (search, with the
exact citation and both of Opatrný's reductions — from 3SAT and from hypergraph 2-colouring).
MAX-SNP-hardness: B. Chor, M. Sudan, "A geometric approach to betweenness", SIAM J. Discrete Math.
11(4) (1998) 511–523. *Standard, not re-verified.* **Honest note:** I did **not** find a citable
bounded-occurrence version of Betweenness this session; if R1 needs bounded occurrence (it likely does,
to keep check weight and Tanner degree bounded), that has to be either located or proved, and it should
be registered as its own premise rather than assumed.

**A4 (bounded-degree colouring / NAE).** *3-colourability of graphs of maximum degree 4 is NP-complete;
NAE-3SAT and 1-in-3-SAT are NP-complete, with bounded-occurrence variants.* — Garey & Johnson (1979);
Schaefer (1978). *Standard, not re-verified.* These are the realistic sources for R1 given the table in
§5.4.

**A5 (code distance hardness).** *Computing the minimum distance of a binary linear code is NP-hard*
(A. Vardy, IEEE-IT 43 (1997) 1757–1766), building on the NP-completeness of coset weights
(Berlekamp–McEliece–van Tilborg, IEEE-IT 24 (1978) 384–386). *Standard, not re-verified.* *The quantum
analogue — the minimum distance problem for stabiliser and CSS codes is NP-hard* — U. Kapshikar,
S. Kundu, arXiv:2203.04262 (IEEE-IT); with a later hypergraph-product-based reduction and
inapproximability, arXiv:2509.21469 / FSTTCS 2025. *Verified* (search-level). **This is why the
promise is in the problem statement and why every reduction owes a distance certificate** (premise
P1.4).

**A6 (König).** *Every bipartite (multi)graph has chromatic index equal to its maximum degree `Δ`, and
a `Δ`-edge-colouring is computable in polynomial time.* *Standard, not re-verified.* Consequence used
in §1: in V2, existence of a depth-`T` schedule is decided in polynomial time.

**A7 (Latin square completion).** *Deciding whether a partial Latin square can be completed is
NP-complete* — C. Colbourn, "The complexity of completing partial Latin squares", Discrete Applied
Math. 8 (1984) 25–30; equivalently, extending a partial edge-colouring of a bipartite graph to a proper
`Δ`-edge-colouring is NP-complete. *Standard, not re-verified.* **Caveat for R5:** the form actually
needed is edge-colouring with *precedence* constraints, not pre-coloured edges. I did not find a
citation for that variant; treat it as an open premise (P5.3), not as an assumption.

**A8 (edge colouring).** *Deciding 3-edge-colourability of cubic graphs is NP-complete* — I. Holyer,
SIAM J. Comput. 10 (1981) 718–720. *Standard, not re-verified.* Used only to argue that V3 is
degenerate.

**A9 (covering radius).** *The covering radius problem for binary linear codes is `Π_2`-complete* —
attributed to A. McLoughlin, "The complexity of computing the covering radius of a code", IEEE-IT 30(6)
(1984) 800–804. *Search-level only —* **needs primary check**: the secondary descriptions I saw this
session say "`Π_2`-hard" and separately that Frances & Litman ("On covering problems of codes", Theory
of Computing Systems 30 (1997) 113–119) proved **coNP**-completeness for codes given as an explicit
list of codewords, which is a different problem. Do not build R4 on A9 until the exact statement is
read. Hardness of approximation: V. Guruswami, D. Micciancio, O. Regev, "The complexity of the
covering radius problem", Computational Complexity 14 (2005) 90–121.

**A10 (Courcelle).** *Every counting-MSO-definable property of graphs of treewidth `≤ t` is decidable
in time `f(t,|φ|)·O(n)`.* — B. Courcelle (1990). *Standard, not re-verified.* Used in R6/P6.3; the
CMSO encoding itself (parity of `|S ∩ N(c)|`, non-membership in the stabiliser group, bounded order
labels) is my own and is a premise, not an assumption.

**A11 (connectivity bounds).** *Quantum codes whose interaction graph has small separators/treewidth
obey trade-offs bounding `k` and `d` (e.g. `k d^{2/(D-1)} = O(n)`-type statements).* — N. Baspin,
A. Krishna, "Connectivity constraints on quantum codes" / "Quantifying nonlocality" (2021–2022).
*Standard, not re-verified, and the exact form matters.* Used only as an honest caveat that the
bounded-treewidth island may be non-vacuous mainly in the fixed-`d` regime.

**A12 (CSP dichotomy).** *Every finite-domain CSP with a fixed constraint language is in P or
NP-complete* — Bulatov (2017), Zhuk (2017); Boolean case Schaefer (1978). *Standard, not re-verified.*
Used to justify why the gate of §6 is decisive in both directions.

**A13 (hook errors).** *A single ancilla fault during a weight-`w` check measurement propagates to a
data error supported on the CNOT-order suffix, of weight up to `⌊w/2⌋` modulo the stabiliser.* —
Dennis, Kitaev, Landahl, Preskill, "Topological quantum memory", J. Math. Phys. 43 (2002) 4452;
Tomita & Svore, PRA 90 (2014) 062320 for the surface-code order dependence. *Standard, not
re-verified.* This is Lemma 1's physical content; Lemma 1 itself is stated and argued above rather
than assumed.

---

## 8. Recommended next action (one session)

Run the gate of §6 (`controllable-coupling-gadget`), items 1–3 by exhaustive search over designed
weight-6 `d = 3` CSS gadgets, item 4 by hand. Report the induced relation `R` explicitly as a truth
table and state which of the four outcomes in §6 obtained. Do **not** start R1's full construction, R3,
or R4 before that gate returns: R4 additionally needs the A9 primary-source check, which is a
15-minute action and should be folded into the same session.

Secondary cheap action, independent of the gate: promote R2 (Theorem 1) to review, since it is written.

---

*Session scope note.* Everything above is proposer-side. No node file, route, or assessment was
written. No result in this document has had independent adversarial review.

---

## Appendix — self-contained probe (reproduces §3 and the gate's items 1–3)

The scratchpad scripts are session-local; this is the whole probe, inlined so §3 is reproducible from
this file alone. `d = 3` (fault budget 2 columns), X-sector; swap `xchecks`/`zchecks` for the mirror.

```python
import itertools

def rref(rows, n):
    rows = list(rows); piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1): rows[i] ^= rows[r]
        piv.append(c); r += 1
        if r == len(rows): break
    return rows[:r], piv

def membership(rows, n):
    R, piv = rref(rows, n)
    def f(v):
        for rr, c in zip(R, piv):
            if (v >> c) & 1: v ^= rr
        return v == 0
    return f

def mask(s):
    m = 0
    for q in s: m |= 1 << q
    return m

def probe(name, n, xchecks, zchecks):
    """xchecks: supports whose ancilla faults make hooks; zchecks: detectors for that sector."""
    HX = [mask(s) for s in xchecks]; HZ = [mask(s) for s in zchecks]
    inHX = membership(HX, n)
    def is_logical(v):
        if v == 0: return False
        if any(bin(v & h).count("1") % 2 for h in HZ): return False
        return not inHX(v)
    singles = [1 << q for q in range(n)]
    reach, nsafe = [], []
    for s in xchecks:                      # locally safe orders + their reachable suffixes
        R = set(); cnt = 0
        for perm in itertools.permutations(s):
            hooks = [mask(perm[i:]) for i in range(1, len(perm))]
            bad = any(is_logical(h) or any(is_logical(h ^ e) for e in singles) for h in hooks)
            if not bad:
                bad = any(is_logical(a ^ b) for a, b in itertools.combinations(hooks, 2))
            if not bad:
                cnt += 1; R.update(hooks)
        reach.append(R); nsafe.append(cnt)
    coupling = [(j1, A, j2, B) for j1, j2 in itertools.combinations(range(len(xchecks)), 2)
                for A in reach[j1] for B in reach[j2] if is_logical(A ^ B)]
    print(name, "| safe orders/check:", nsafe, "| coupling pairs:", len(coupling))
    return nsafe, coupling

# rotated [[9,1,3]] surface code on the 3x3 grid 0..8
probe("rotated surface, X", 9, [(1,2,4,5),(3,4,6,7),(0,1),(7,8)],
                              [(0,1,3,4),(4,5,7,8),(2,5),(3,6)])
# unrotated [[13,1,3]] = HGP(rep3, rep3)
probe("HGP surface, X", 13, [(0,3,9),(1,4,9,10),(2,5,10),(3,6,11),(4,7,11,12),(5,8,12)],
                            [(0,1,9),(1,2,10),(3,4,9,11),(4,5,10,12),(6,7,11),(7,8,12)])
# Steane [[7,1,3]] (Hamming checks, self-dual construction)
probe("Steane, X", 7, [(3,4,5,6),(1,2,5,6),(0,2,4,6)], [(3,4,5,6),(1,2,5,6),(0,2,4,6)])
```

For the coupling census, generate `H` with rows of weight 6 and pairwise even overlaps (so
`H H^T = 0`), set `H_X = H_Z = H`, keep instances whose X-sector distance is exactly 3, and call
`probe`. Observed: coupling in 56 of 71 such instances, 400–600 forbidden order pairs each.
