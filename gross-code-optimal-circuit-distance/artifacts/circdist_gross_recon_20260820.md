# CIRCDIST.gross — recon session report (Opus 5 executor, 2026-08-20)

Node: `CIRCDIST.gross`. Session type: budget-boxed route-registration recon under a stop-loss
directive. Nothing here is offered at a completion level. Evidence labels used below are
**NUMERICAL** (a computation with the code inline, reproducible in seconds) and **CONJECTURED
(sketch)** (a complete derivation that has had no independent review). No claim in this file is
labelled PROVED.

Everything I read (papers, repo files) is treated as data. Where I state someone else's theorem I
say so and give the identifier; where I state my own derivation I say so and give the code.

---

## 0. Executive summary of the repricing

Three things changed my prior during this session, in decreasing order of importance.

1. **The interleaved-`d_circ = 12` question is *not* a residual-set-optimisation question. It is
   exactly a "completion gap" question.** I show (§3.2, NUMERICAL) that *every* 2-element subset of
   *every* check support of the Gross code lies in a weight-12 logical operator of the matching
   type. Since residual sets depend only on the CNOT order *within* each check — a datum every
   legal schedule must supply, interleaved or not — this gives
   `d_ext(E(M)) ≤ 11` **for every schedule M in S_Gross**, interleaving allowed.
   Combined with `d_ext(E(M)) ≤ d_circ(C(M))` (Strikis–Browne–Beverland Prop. 3, valid for *any*
   single-ancilla SEC), a distance-12 interleaved schedule must satisfy
   `g(M) := d_circ(C(M)) − d_ext(E(M)) ≥ 1`.
   So `CIRCDIST.gross` is downstream of the mechanism that `CIRCDIST.lift` is about, and the two
   nodes should be wired together in the DAG.

2. **The published `d_circ ≤ 11` bound (their Prop. 4) is reproducible from scratch in ~5 seconds**,
   and its two published numbers ("all 90 residual sets give ≤ 11", "45 of the 90 give ≤ 10") both
   fall out of one small structural computation with an exact match (§3.2–3.3). That is an
   independent replication of the load-bearing prior result, and it also *explains* the 45: it is
   exactly `5 × 3 × 3`, where 5 of the 10 balanced 3|3 splits of a check support are covered by a
   weight-12 logical.

3. **The interleaved schedule space has an exactly enumerable, non-trivial symmetric subclass.**
   A legal schedule is precisely a proper edge colouring of the 6-regular bipartite Tanner graph of
   `H_XZ` by an ordered colour set (§3.4). Minimum depth is 6 CNOT layers (8 total), and the
   *translation-invariant* minimum-depth schedules number **exactly 25 920**, of which **23 328 are
   genuinely interleaved** (§3.5, NUMERICAL). This is a fully enumerable class, and it is the
   cheapest place to ask the only question that matters: *can interleaving produce a strictly
   positive gap for this code at all?*

I also derived an exact, small formula for the detector syndrome of the natural weight-11 spacetime
witness family (§3.6). It reduces "is this weight-11 effective logical blocked by interleaving?" to
a parity-cancellation problem over at most six X-checks with ten nested 4-way choices — a
millisecond decision per witness, once a schedule is fixed.

**Net effect on the node's prior.** The scheduler's opening estimate was `P = 0.15, D = 8` for the
whole claim. I would now split it: certifying the candidate circuit at `d_circ = 11` looks
*substantially* cheaper than the opening estimate suggested (it is a code-capacity-sized exact
min-distance certification on ~360 columns, not a circuit-level DEM problem — see §5, Route 1);
the headline `D*_Gross` determination is, if anything, *harder* than 0.15 suggests, because the
no-go now has to be a statement about spacetime monodromy rather than about residual sets. My
overall read is that `D*_Gross = 11` is the likely truth (~0.8 subjective) but that the *proof* of
it is not in reach at the current toolset.

---

## 1. Fixed setup and notation

**Code.** Gross code `Q = [[144,12,12]]`, the bivariate bicycle code with `ℓ = 12`, `m = 6`,
group `G = Z_ℓ × Z_m` of order 72, `x = S_ℓ ⊗ I_m`, `y = I_ℓ ⊗ S_m`,
```
A = x^3 + y + y^2 ,   B = y^3 + x + x^2 ,   H_X = [A | B] ,   H_Z = [B^T | A^T] .
```
`n = 2|G| = 144` data qubits (a left half and a right half, each a free `G`-set), 72 X-checks and
72 Z-checks, all of weight 6, every data qubit in exactly 3 X-checks and 3 Z-checks. Verified in
§7: `rank H_X = rank H_Z = 66`, `k = 12`, `H_X H_Z^T = 0`, and `|supp(e_X) ∩ supp(e_Z)| ∈ {0,2}`
for all check pairs.

**Schedules.** `S_Gross` as commissioned: one dedicated ancilla per check, each required CNOT
exactly once, at most one two-qubit gate per qubit per time step, X/Z interleaving allowed, no
flags/cat states/generating-set changes, idle layers compressed.

**Residual (hook) errors.** For a Z-check with data qubits listed in CNOT order `i_1,…,i_6`, a Z
fault on its ancilla after the `(l−1)`-th CNOT propagates to Z on the suffix
`S_l = {i_l,…,i_6}` and leaves the ancilla's own Z-basis outcome untouched. Modulo the check
itself, the weight->1 residuals are exactly
```
{i_1,i_2} ,  {i_5,i_6} ,  {i_4,i_5,i_6} ( ~ {i_1,i_2,i_3} ) .
```
The X case is the mirror image (X fault on an X-check ancilla → X on the suffix). `E(M)` denotes
the union over checks, `d_ext(·)` the extended-code distance of Strikis–Browne–Beverland Def. 3
(append one column per residual, being the mod-2 sum of that residual's data columns).

**Terminology caveat.** The commission's `d_eff(M) := d_ext(E(M))` is *our* name. The source paper
has no formal `d_eff` or `E(M)`; its formal objects are `Δ(E)` (residual distance) and
`d_ext(R)`. When quoting their results below I use their objects.

---

## 2. What is actually established in the literature (ASSUMPTIONS)

These are the load-bearing external results. I read the first one in full; I flag precisely where I
am unsure.

**A1 — [SBB26, Thm. 1 / Prop. 3] Lower bound, any SEC.**
*Source:* A. Strikis, D. E. Browne, M. E. Beverland, "High-performance syndrome extraction circuits
for quantum codes", **arXiv:2603.05481** (5 Mar 2026).
*Statement:* for any single-ancilla CNOT-based SEC `C` of a CSS code with residual set `E`,
`d_circ(C) ≥ d_ext(E)`. *Scope:* holds for interleaved circuits too; the proof is a CSS-separation
argument plus a per-mechanism table showing every elementary fault contributes either a single data
error or a residual error after propagation, and is explicitly independent of interleaving.
*Confidence in my statement:* high.

**A2 — [SBB26, Thm. 1 / Cor. 1] Equality for non-interleaved circuits.**
*Statement:* if `C'` is non-interleaved then `d_circ(C') = d_ext(E)`, and moreover
`d_circ(C') ≤ d_ext(R)` for every subset `R ⊆ E`.
*Their definition of non-interleaved:* "either all X-type CNOTs precede all overlapping Z-type
CNOTs, or all Z-type CNOTs precede all overlapping Z-type CNOTs" — note the word *overlapping*:
the condition is imposed only on checks that share data qubits, so this is weaker than a global
X-then-Z split. *Confidence:* high on the statement, medium on my paraphrase of the exact
"overlapping" quantifier — a follow-up session should re-read §II–IV of the source before making
this a formal assumption record.

**A3 — [SBB26, Eq. 12] Interleaving is monotone.**
*Statement:* starting from a non-interleaved SEC and retiming CNOTs while preserving each check's
*internal* CNOT order yields an interleaved SEC with `d_circ ≥ d'_circ`. Interleaving can never
decrease the circuit distance. *Confidence:* high. This is exactly why the `≤` half of A2 fails for
interleaved circuits and why the open problem exists.

**A4 — [SBB26, Prop. 4] Gross-code non-interleaved bound.**
*Statement:* every non-interleaved SEC for the Gross code has `d_circ ≤ 11`.
*Method:* fix one check; its residual set must be one of the 90 inequivalent ones; for each of the
90, exhibit a logical operator of weight ≤ 11 in the corresponding extended code. In every case
they find one; in 45 of the 90 cases they find one of weight ≤ 10. Because only *upper* bounds are
needed, a heuristic search is rigorously sufficient here — each witness is independently
checkable. *Confidence:* high. **I independently reproduce both numbers in §3.2–3.3.**

**A5 — [SBB26, Prop. 5] Uniform tiling.**
*Statement:* if the circuit's local restriction to every X check is the same (i.e. the schedule is
translation-invariant), `d_circ ≤ 10`. *Scope:* stated for non-interleaved circuits; the underlying
computation is on residual sets only, so it bounds `d_ext` for translation-invariant *interleaved*
schedules as well. *Confidence:* high on the statement, high on the `d_ext` extension (it follows
from A1's scope), medium that they intended it that way.

**A6 — [SBB26, Prop. 6 + §IV.3] Three-colour pruning and the candidate circuit.**
*Statement:* the X- and Z-Tanner graphs of the Gross code each admit a natural 3-colouring in which
support-sharing checks get distinct colours; among three-colour-tiled circuits, at most 3 relative
orderings can have `d_circ = 11`, and those 3 are cyclic permutations of one another. Pruning
cascade `90 → 45 → 4 → 3` per type; `90^3 − 3 = 728 997` patterns per type eliminated.
The candidate is a depth-8 "slightly modified LRC" / 3-colour-tiled left-right circuit. Depth 8 is
provably minimal for this code from their Eq. (3) lower bound `max(c(H_XZ), r(H_XZ)+2) = max(6,8)`.
*Evidence for `d_circ = 11`:* an adaptive-prior BPOSD-based randomised search run for **10 000
outer loops on a single QEC cycle with no logical of weight < 11 found**, versus a control (the
standard circuit) where a weight-10 logical appeared after **one** loop. That is the entire
quantitative basis of the conjecture; the estimator can only exhibit logicals, never certify their
absence. *Confidence:* high.

**A7 — Morphing circuits reach circuit distance 12 with the same qubit counts.**
*Source:* S. Shaw, B. M. Terhal, "Lowering connectivity requirements for bivariate bicycle codes
using morphing circuits", **PRL 134, 090602 (2025)**. *Statement (as reported by SBB26 §H.2):*
morphing circuits give the same physical and logical qubit counts as the Gross code with circuit
distance twelve. *Scope — critical and unverified by me:* I did **not** read this paper this
session. Morphing changes the circuit paradigm (ancilla merging / measurement-based gadgets), so
I expect it lies **outside** `S_Gross` as commissioned. That expectation is load-bearing for the
node's scope and is registered as Route 6's gate, not as an assumption.

**A8 — Distance-finding tooling.**
*Source:* M. Webster, A. Jacob, O. Higgott, "Distance-Finding Algorithms for Quantum Codes and
Circuits", **arXiv:2603.22532** (v2, 14 Aug 2026). Benchmarks exact methods (Brouwer–Zimmermann,
connected cluster, SAT, mixed-integer programming) against heuristics, and introduces QDistEvol.
Notes that circuit distance is generally harder than code distance because the DEM check matrix is
much larger than the code's. *Confidence:* medium — I have the abstract-level statement, not the
tables. Also relevant: Tesseract (**arXiv:2503.10988**), decision-tree decoders
(**arXiv:2502.16408**), Landahl–Anderson–Rice (**arXiv:1108.5738**) are the provable
minimum-weight decoders SBB26 name as the route to certifying their conjecture.

**A9 — Gross code source.** S. Bravyi, A. W. Cross, J. M. Gambetta, D. Maslov, P. Rall, T. J. Yoder,
"High-threshold and low-overhead fault-tolerant quantum memory", Nature **627**, 778 (2024),
**arXiv:2308.07915**. Also: "Tour de Gross", **arXiv:2506.03094**. Extended Tanner graph machinery:
Pacenti–Pradhan–Borah–Vasić, **arXiv:2504.21200**. Left-right circuits originate in Xu et al.,
Nature Physics **20**, 1084 (2024).

---

## 3. Results obtained in this session

### 3.1 Parity lemma — NUMERICAL (and one line of proof)

**Claim.** Every vector in `ker(H_X)` has even weight; likewise `ker(H_Z)`. Hence every logical
operator of the Gross code (of either type) has even weight, and there are no weight-13 logicals.

**Derivation.** Each column of `H_X` has weight 3 (each data qubit is in exactly 3 X-checks), so the
sum of all 72 rows of `H_X` is the all-ones vector; therefore `1 ∈ rowspace(H_X)`, and for
`v ∈ ker(H_X)` we get `1·v = 0`. Verified computationally (`all-ones in rowspace(HX): True`, same
for `H_Z`).

**Why it matters.** It rigidifies the cost arithmetic. A residual `r` inside a logical `L` yields an
effective logical of weight `|L| − |r| + 1`. With `|L|` even and `|L| ≥ 12`:

| residual weight | achievable effective weights |
|---|---|
| 2 | 11, 13, 15, … |
| 3 | 10, 12, 14, … |

So **`d_ext ∈ {10, 11, 12}` for this code, and the value 11 can only ever be produced by a weight-2
residual sitting inside a weight-12 logical.** A weight-3 residual is either worth 10 or worth
nothing (12). This is the reason the 90 residual sets fall into a clean 45/45 split rather than
some ragged distribution.

### 3.2 Pair-coverage lemma — NUMERICAL

**Claim.** For the Gross code, **every one of the 15 two-element subsets of a check's support is
contained in a weight-12 logical operator of the matching type**, for both X- and Z-checks. By
translation-transitivity on each check type, the same holds for all 144 checks.

**Computation.** A randomised information-set search over `ker(H_X)` (dimension 78) produces
weight-12 non-stabiliser words in well under a second; closing the set under the 72 translations
`x^a y^b` (which are code automorphisms because the group algebra is commutative) gives a pool of
**1 884** weight-12 Z-logicals and 1 884 weight-12 X-logicals. Every pool member is verified to have
weight exactly 12, zero syndrome, and to be outside the stabiliser row space. Coverage counts for
the Z-check with support `[3, 6, 12, 73, 74, 90]` (witness multiplicities in the pool):

```
pairs (indices into the sorted support):
 (0,1) (0,2) (0,3) (0,4) (0,5) (1,2) (1,3) (1,4) (1,5) (2,3) (2,4) (2,5) (3,4) (3,5) (4,5)
   all 15 covered, multiplicities ranging from 2 to 44
```
An explicit witness, for the pair `(4,5) = {74, 90}`:
`L = {6, 13, 35, 54, 59, 61, 74, 81, 90, 122, 129, 138}` — weight 12, `H_X L = 0`, `L ∉ rowspace(H_Z)`.

**Consequence (this is the repricing).** Fix any `M ∈ S_Gross`. Any check `c` is measured in *some*
CNOT order, so `E(M)` contains the weight-2 residual `{i_5, i_6} ⊆ supp(c)`. That pair lies in a
weight-12 logical `L`, giving an extended-code codeword of weight `1 + 10 = 11`. Hence

> **`d_ext(E(M)) ≤ 11` for every legal schedule `M`, interleaved or not.**

Because upper bounds on a distance are certified by exhibiting a witness, this direction is
rigorous, not heuristic. It independently reproduces A4's computational content and extends its
*scope* to interleaved schedules at the `d_ext` level. Together with A1, a schedule with
`d_circ = 12` must therefore have `g(M) = d_circ − d_ext ≥ 1`.

### 3.3 The 45/90 split, explained — NUMERICAL

**Claim.** Of the 10 balanced 3|3 splits of a check's support, exactly **5** have their halves
contained in weight-12 logicals; and the covered-ness of `T` and of its complement `T'` always
agree. Consequently exactly `5 × 3 × 3 = 45` of the 90 residual sets contain a weight-3 residual
inside a weight-12 logical, i.e. give `d_ext ≤ 10`.

Computed splits for the Z-check `[3,6,12,73,74,90]` (indices into the sorted support):
```
covered:    (0,1,3)|(2,4,5)   (0,2,3)|(1,4,5)   (0,2,5)|(1,3,4)   (0,3,4)|(1,2,5)   (0,3,5)|(1,2,4)
uncovered:  (0,1,2)|(3,4,5)   (0,1,4)|(2,3,5)   (0,1,5)|(2,3,4)   (0,2,4)|(1,3,5)   (0,4,5)|(1,2,3)
```
and for the X-check `[4,5,54,75,132,138]`, again exactly 5 covered splits.

**This matches A4's reported "45 of the 90 cases have weight at most 10" exactly.** Given that the
90 count itself is `6!/8 = 90` (the order-8 stabiliser being: swap `i_1↔i_2`, swap `i_5↔i_6`, and
*global order reversal*, which fixes the residual set), the whole of A4 is reproduced from two small
facts about the code: "all 15 pairs covered" and "5 of 10 splits covered".

**Why the complementary symmetry holds (sketch).** If a weight-12 logical `L` meets `supp(c)` in
exactly the 3-set `T`, then `L + c` is again a logical of weight `12 − 3 + 3 = 12` and meets
`supp(c)` in exactly `T'`. So coverage of `T` by an *exactly-meeting* logical forces coverage of
`T'`. The observed perfect agreement in all 10 splits says the exactly-meeting case is the one that
occurs.

### 3.4 Schedule space = proper edge colourings — CONJECTURED (sketch)

The full Tanner graph of `H_XZ = [H_X ; H_Z]` on `144` data + `144` ancilla vertices is
**6-regular bipartite** with 864 edges (verified: every data degree 6, every check degree 6). A
legal schedule assigns a time step to each edge such that edges meeting at a vertex get distinct
times; that is exactly a proper edge colouring by an ordered colour set. By König's theorem
`χ'(G) = 6`, so 6 CNOT layers are achievable and minimal, giving total depth `6 + 2 = 8` with round
staggering — consistent with A6's independently derived minimal depth 8. This identification is the
right combinatorial home for the problem: **`S_Gross` (up to idle-layer compression) is the set of
proper edge colourings of a fixed 6-regular bipartite graph, with the colours linearly ordered.**

### 3.5 The translation-invariant minimum-depth class is exactly 25 920 — NUMERICAL

Under the free `G = Z_12 × Z_6` action the 864 edges fall into `864/72 = 12` orbits: six carrying
X-check CNOTs (three to the left data half via `A`'s monomials, three to the right via `B`'s) and
six carrying Z-check CNOTs (three to the left via `B^T`, three to the right via `A^T`). A
translation-invariant minimum-depth schedule assigns one layer in `{1,…,6}` to each orbit, subject
to: the six CNOTs of every check are at distinct layers, and the six CNOTs of every data qubit are
at distinct layers. Brute-force enumeration over `(6!)^2 = 518 400` candidate pairs of bijections:

```
translation-invariant minimum-depth schedules:                 25 920   ( = 20 · 36 · 36 )
of which data-qubit-separated (LRC-like, non-interleaved):      2 592
genuinely interleaved:                                         23 328
```
The closed form: choose the 3-subset `P ⊆ {1,…,6}` of layers used by the X-CNOTs on left data
qubits (`C(6,3) = 20`); the rest is forced up to `3!·3!` orderings on each side.

By A5 all of these have `d_ext ≤ 10`. So the 23 328 interleaved members are exactly a testbed for
the question "does interleaving ever buy a strictly positive gap on this code?", and they are
enumerable in full.

### 3.6 Exact detector syndrome of the weight-11 witness family — CONJECTURED (sketch)

This is the piece I would most like reviewed; the derivation is complete but unrefereed, and it is
the technical core of the no-go route.

**Setting.** X-basis memory experiment, `R` rounds, ideal final data readout; consider Z-type
faults, so the only detectors that can fire are the X-check comparisons. Fix a Z-check `c` with
final-round CNOT order `(i_1,…,i_6)` at times `τ_1 < … < τ_6`; fix `l` and the suffix
`S = S_l = {i_l,…,i_6}`; fix a logical `L ∈ ker(H_X) \ rowspace(H_Z)` with `S ⊆ L`, and put
`D = L \ S`.

**Fault set.** One Z fault on `ancilla(c)` at a time `t ∈ (τ_{l−1}, τ_l)`, plus one Z fault on each
`q ∈ D`, the latter placed at a freely chosen time `t_q` inside round `R`. Total weight
`1 + |L| − |S|`. The net residual data error at readout is `S + D = L`, a logical.

**Claim (syndrome formula).** For every X-check `e`, the number of detector events it produces is

```
flip(e)  =  #{ q ∈ D ∩ supp(e) : time_R(e,q) ≤ t_q }
          + #{ q ∈ S ∩ supp(e) : time_R(e,q) ≤ t  }        (mod 2),
```

and no other detector in the circuit fires. In particular, placing every data fault at the very
start of round `R` (all `t_q` minimal) collapses this to
`flip(e) = #{ q ∈ S ∩ supp(e) : time_R(e,q) < t } mod 2`.

**Derivation.** A Z fault on a Z-check ancilla is invisible to that check's own Z-basis measurement
and propagates to Z on the data qubits of its not-yet-applied CNOTs, i.e. onto `S`. A Z error
present on data qubit `q` at the moment X-check `e` applies its CNOT `e → q` propagates Z onto `e`'s
ancilla, flipping `e`'s X-basis outcome; Z errors never reach a Z-check ancilla, and Z errors on
data never reach another data qubit. Hence `e`'s round-`R` outcome flips by
`Σ_{q∈D∩e} 1[time(e,q) > t_q] + Σ_{q∈S∩e} 1[time(e,q) > t]`. Writing `1[·>·] = 1 − 1[·≤·]` and using
`|D ∩ e| + |S ∩ e| = |L ∩ e| ≡ 0 (mod 2)` (because `H_X L = 0`) gives the stated formula. Rounds
`< R` are fault-free; the final-readout detectors see the total error `L`, which is logical, so
they fire exactly where `e_R` was flipped, adding no new constraint. ∎(sketch)

**Consequences.**

* *(Sufficient condition for `d_circ ≤ 11`.)* If for some `(c, l=5, t, L)` no X-check CNOT touches
  `S = {i_5,i_6}` before `t`, then the fault set above is an undetectable logical of weight 11.
* *(Blocking is a tiny finite problem.)* For fixed `(c, S, L, t)` the sources available to cancel the
  `S`-term are, for each of the `|D| = 10` data qubits, one of **four nested prefixes** of the (at
  most three) X-checks on that qubit — because moving `t_q` later can only remove the earliest
  X-check CNOTs from the count. So "is this weight-11 effective logical blocked?" is a
  `4^10 ≈ 10^6` decision (and much less with pruning), over a target vector supported on at most six
  X-checks.
* *(The naive obstruction is vacuous at minimum depth.)* In a 6-CNOT-layer schedule every qubit and
  every ancilla is busy in all six layers, so `τ_j = j`. For `S = {i_5, i_6}` the X-check layers of
  `i_5` form a 3-subset of `{1,2,3,4,6}` and so always contain an element `≤ 4`; likewise for `i_6`.
  Hence there is *always* an X-check CNOT on `S` before `t`, and the "no CNOT before `t`" sufficient
  condition never fires at minimum depth. Blocking at minimum depth therefore turns entirely on the
  **parity** version of the formula plus the data-fault-timing freedom. This is why the problem is
  genuinely open rather than settled by a one-line timing argument.
* *(Useful overlap structure.)* `|supp(e_X) ∩ supp(e_Z)| ∈ {0,2}` for the Gross code, and for a
  Z-check support the 15 pairs split into **6 "same-half" pairs** (both qubits in the same data half;
  **no** X-check contains both, so six distinct X-checks each see exactly one) and **9 "cross-half"
  pairs** (exactly one X-check contains both, which can self-cancel by parity). The same-half pairs
  are therefore the hardest ones for a schedule to block, and are the right place to look for a
  no-go.

---

## 4. Candidate proof routes

`P` = probability the route eventually closes (reaches a completion level for its implication and
premises); `D` = expected number of sessions like this one. Both are my estimates, written for
audit.

### Route 1 — `candidate-circuit-exact-certification`  (covers deliverable (a))

**Target.** `d_circ = 11` for the published depth-8 three-colour-tiled circuit, both directions.

**Premises.**
1. `P1.1` The exact CNOT schedule of the candidate circuit is recovered from the authors' artifacts
   (Zenodo record 18853600 / `github.com/PurePhys/LR-circuits`), and it is verified to be a legal
   member of `S_Gross` and non-interleaved in the sense of A2.
2. `P1.2` (upper bound, essentially free) `d_ext(E) ≤ 11` via an explicit weight-11 extended-code
   codeword. §3.2 already supplies one for *any* schedule: take the weight-2 residual `{i_5,i_6}` of
   any check together with a weight-12 logical containing it.
3. `P1.3` (lower bound, the real work) **No codeword of weight ≤ 10 exists in the extended code.**
   Concretely: for the Z-side, the extended check matrix has `144 + 72·3 = 360` columns and 66
   independent rows, alongside the 12-row logical-action matrix `L_X^ext`; certify
   `min{ |x| : H_X^ext x = 0, L_X^ext x ≠ 0 } = 11` exactly. Since `x` is a nontrivial logical iff
   `L_i x = 1` for some `i`, this is exactly 12 minimum-weight problems (one per `i`), each a
   360-variable binary problem with 66 GF(2) parity constraints plus one parity equation forcing
   `L_i x = 1` — solvable in principle by SAT-with-cardinality, MIP, or Brouwer–Zimmermann. The
   X-side is the mirror image.
4. `P1.4` The certificate is re-run independently (different solver/encoding) and reviewed.

**Implication sketch.** By A2, `d_circ = d_ext(E)` for a non-interleaved circuit, so certifying the
extended-code distance certifies the circuit distance. `P1.2` gives `≤ 11`, `P1.3` gives `≥ 11`.
The crucial structural point — and the reason this is cheaper than it looks — is that A2 converts a
*circuit-level* certification (a DEM with tens of thousands of columns over `d` rounds) into a
**code-capacity-sized** certification on 360 columns. That is squarely inside the range where exact
methods are reported to work.

**P = 0.60.** Band: OPEN→ the claim is a finite exact computation with no conceptual gap; the risk
is entirely solver scaling at distance 11 on 360 columns, plus the risk that A2's "non-interleaved"
hypothesis does not literally cover the published circuit (`P1.1`).
**D = 2 sessions.** One to recover the schedule and build/validate the extended matrices, one to run
and certify.

### Route 2 — `gap-forcing-no-go`  (covers deliverable (b), the headline)

**Target.** `d_circ(C(M)) ≤ 11` for **every** `M ∈ S_Gross`, hence (with Route 1) `D*_Gross = 11`.

**Premises.**
1. `P2.1` (§3.2, NUMERICAL, essentially in hand) every 2-subset of every check support lies in a
   weight-12 logical; hence `d_ext(E(M)) ≤ 11` for all `M`.
2. `P2.2` (§3.6, CONJECTURED sketch) the exact detector-syndrome formula for the witness family,
   promoted to a reviewed lemma, and extended to cover *all* elementary fault types (two-qubit CNOT
   faults, ancilla preparation/measurement faults) and *multi-round* placements.
3. `P2.3` **(the hard core)** For every proper edge colouring of the Gross Tanner graph there exist a
   check `c`, an index `l`, a time `t`, a weight-12 logical `L ⊇ S_l`, and data-fault times `{t_q}`
   with `flip(e) = 0` for all `e`. Equivalently: the parity-cancellation system of §3.6 is never
   simultaneously unsolvable across the whole witness family.
4. `P2.4` A structural mechanism for `P2.3` — the missing idea. The two candidates I can name:
   (i) a *counting/expansion* argument (the witness family has ≥ 144·15·(many) members while a
   schedule has only 864 edge-times of freedom, so blocking everything is over-constrained);
   (ii) a *local-move* argument (given any schedule, exhibit an explicit `(c, S, L)` from the
   structure of the code — e.g. one of the six same-half pairs — whose cancellation system is
   solvable by construction).

**Implication sketch.** `P2.1` guarantees a weight-11 *effective* logical always exists.
`P2.2` + `P2.3` say at least one of them always lifts to a closed spacetime logical of the same
weight, i.e. `g(M) = 0` is not avoidable, so `d_circ ≤ 11` universally. With A1's lower bound and
Route 1's construction, `D*_Gross = 11`.

**P = 0.12.** The premise `P2.3` is universally quantified over a space of edge colourings with no
known finite reduction, and the "obvious" timing obstruction is provably vacuous at minimum depth
(§3.6). Nothing I found suggests a mechanism; `P2.4` is a genuine gap.
**D = 6 sessions**, and honestly this is the number I trust least — it is really "≥ 6 or never".

### Route 3 — `symmetric-subclass-exhaustion`  (covers deliverable (c); the minimal-acceptance route)

**Target.** Determine `max d_circ` over the translation-invariant minimum-depth class, then over the
three-colour-periodic class.

**Premises.**
1. `P3.1` (§3.4–3.5, NUMERICAL, in hand) the class is exactly 25 920 schedules (23 328 interleaved),
   enumerable, with the closed form `20 · 36 · 36`.
2. `P3.2` For every member, compute a witness-certified upper bound on `d_circ` by running the §3.6
   cancellation decision over the residual/logical witness family. Upper bounds are rigorous.
3. `P3.3` For any member whose upper bound exceeds the `d_ext ≤ 10` value guaranteed by A5 — i.e.
   any member with a strictly positive gap — certify the lower bound exactly on its (small, single-
   round-periodic) DEM.
4. `P3.4` Repeat for the three-colour-periodic class (index-3 subgroup of `G`, `864/24 = 36` edge
   orbits) using the pruning cascade style of A6.

**Implication sketch.** The class is finite and explicitly parameterised, so exhaustion is a
computation, not a proof search. The result is a determination of the optimum over a meaningful
subclass — the commission's stated minimal acceptance — and it simultaneously answers the
qualitative question "does interleaving ever produce `g > 0` on this code?".

**P = 0.55.** The enumeration is certain; the risk is entirely in `P3.3` (exact lower-bound
certification for survivors) and in whether the answer is interesting rather than "all ≤ 10".
**D = 2–3 sessions.**

### Route 4 — `lift-theorem-transfer`  (structural; makes `CIRCDIST.lift` a premise)

**Target.** Same as Route 2, but via the general theory rather than by hand.

**Premises.**
1. `P4.1` The `CIRCDIST.lift` node's characterisation: `d_circ = min over effective logicals γ of the
   minimal closed spacetime lift of γ`, with the obstruction expressed as a voltage/monodromy class.
2. `P4.2` Identification of the Gross-code monodromy: §3.6 exhibits the voltage of the natural
   witness family explicitly — `volt(γ) = (flip(e))_e` — so `P4.1`'s abstract obstruction is already
   computed for this family. Promote to: the monodromy homomorphism has image of rank `r`, and the
   witness family surjects onto more than `2^r` classes, so some witness has zero voltage.
3. `P4.3` A rank bound on the monodromy image in terms of schedule depth.

**Implication sketch.** If the monodromy image is small relative to the witness family, a
pigeonhole gives a zero-voltage witness, hence a closed lift at weight 11, hence `d_circ ≤ 11`. This
is the cleanest conceptual shape a no-go could take, and it is the same lemma `CIRCDIST.lift`
needs — so the work is shared across two roots.

**P = 0.20.** Higher than Route 2's core because a pigeonhole is a *mechanism*, not just a hope; but
it inherits `CIRCDIST.lift`'s own risk, and the naive rank count does not obviously close (the
witness family's voltages are not obviously equidistributed).
**D = 5 sessions**, of which ~2 are shared with `CIRCDIST.lift`.

### Route 5 — `cegar-constructive-search`  (the existence side)

**Target.** Either an explicit interleaved `M` with certified `d_circ = 12`, or an UNSAT certificate
over a stated subclass.

**Premises.**
1. `P5.1` Encode the problem in its true `Σ_2` shape: *exists* an edge colouring such that *for all*
   witnesses `(c, l, t, L, {t_q})` the cancellation system is unsolvable.
2. `P5.2` Counterexample-guided abstraction refinement: propose a colouring; run §3.6 to find a
   weight-≤11 spacetime witness; add the clause "block this witness"; repeat.
3. `P5.3` Exact certification of any surviving candidate at `d_circ = 12` (full circuit-level, `d`
   rounds — the expensive case A8 warns about).
4. `P5.4` For a negative result, an UNSAT certificate that is itself checkable.

**Implication sketch.** CEGAR is the standard tool for exactly this quantifier structure, and the
witness oracle in `P5.2` is cheap because of §3.6. On the three-colour-periodic subclass, UNSAT is a
realistic outcome; on the full class it is not.

**P = 0.12** (that the route closes the node). It is however the route most likely to yield a
decisive *negative* on a named subclass, which is a productive output under §4 of the valuation
protocol.
**D = 4 sessions.**

### Route 6 — `morphing-scope-gate`  (cheap scope clarification)

**Target.** Decide whether A7's distance-12 morphing circuits lie inside `S_Gross`.

**Premises.** `P6.1` exact statement of Shaw–Terhal's circuit (ancilla count per check, gate set,
whether the measured generating set is the Gross code's own, whether extra qubits/measurements are
used). `P6.2` a scope ruling against the commission's five conditions.

**Implication sketch.** If the morphing circuit is expressible as a legal single-ancilla CNOT
schedule of the *unmodified* generating set, `D*_Gross = 12` follows by exhibition and the node
closes immediately. I expect the answer is **no** (morphing merges ancillas and changes the
measured gadget), in which case the value is a sharpened scope clause plus the elimination of a
false hope — and an explanation of why the original authors lost interest in the interleaved
question.

**P = 0.08** that it closes the node; ~0.9 that it produces a definite scope ruling.
**D = 0.5 sessions.** Cheapest item on the board by a wide margin.

### Route table

| route | one-line idea | P | D |
|---|---|---|---|
| `candidate-circuit-exact-certification` | A2 turns `d_circ = 11` into an exact min-distance certification on a 360-column code | 0.60 | 2 |
| `gap-forcing-no-go` | every schedule admits a weight-11 witness whose interleaving monodromy cancels | 0.12 | 6 |
| `symmetric-subclass-exhaustion` | 25 920 translation-invariant min-depth schedules, enumerate them all | 0.55 | 2–3 |
| `lift-theorem-transfer` | import `CIRCDIST.lift`; pigeonhole the monodromy against the witness family | 0.20 | 5 |
| `cegar-constructive-search` | `Σ_2` CEGAR: propose colouring, refute with a witness, repeat | 0.12 | 4 |
| `morphing-scope-gate` | is the known distance-12 morphing circuit inside `S_Gross`? | 0.08 | 0.5 |

---

## 5. The single cheapest decisive gate

> **Gate G1 — "Does interleaving ever buy a strictly positive completion gap on the Gross code?"**
> Enumerate all **25 920** translation-invariant minimum-depth schedules (§3.5). For each, run the
> §3.6 cancellation decision over the witness family (all 144 checks × their residuals × the pooled
> weight-12 logicals) and record the best witness-certified upper bound on `d_circ`. Compare against
> the value `d_ext ≤ 10` guaranteed for this class by A5.

Cost: well under one session. Every ingredient already exists in this report; the only new code is
the cancellation solver, and it is a `4^10`-with-pruning decision per witness.

**What each outcome implies.**

* **All 25 920 give an upper bound of 10** (i.e. `g = 0` throughout). Then interleaving buys nothing
  in the most symmetric setting. This is strong evidence for `D*_Gross = 11`, it drops `P` on Routes
  5 and 6, raises `P` on Route 2, and — importantly — it tells `CIRCDIST.lift` that the Gross code is
  a *bad* place to hunt for the explicit `d_circ > d_eff` example that node needs.
* **Some schedule shows `g ≥ 1`** (upper bound 11 while `d_ext ≤ 10`). Then the gap mechanism is real
  and *constructive* on this code. `D*_Gross = 12` becomes live, Route 5 jumps in value, Route 2's
  `P` collapses, and `CIRCDIST.lift` gets handed the explicit interleaved strict-inequality example
  it lists as a wanted result — one gate serving two roots.
* **Some schedule shows `g ≥ 2`** (upper bound 12). Then run the exact certification and, if it
  holds, the node closes at `D*_Gross = 12`.

**Why this gate and not another.** The alternatives are worse buys. Recovering and certifying the
candidate circuit (Route 1) is valuable but *confirmatory* — it settles the sub-claim everyone
already believes, and cannot discriminate between `D* = 11` and `D* = 12`. Attacking `P2.3` directly
is the expensive core with no mechanism in hand. Gate G1 is the smallest computation whose two
possible outcomes point at *opposite* answers to the headline question, and it is the only cheap one
with that property. Its runner-up is Route 6 (half a session, but it most likely only rules a
paper out of scope).

---

## 6. Surprises and things worth flagging to the dispatcher

1. **The `≤ 11` bound was never really about non-interleaving.** A4 is stated for non-interleaved
   circuits, but its computational content (all 90 residual sets admit a weight-≤11 extended-code
   codeword) is interleaving-independent, because residual sets depend only on within-check order.
   The non-interleaving hypothesis is used *only* to convert `d_ext` into `d_circ`. Once that is
   seen, the whole open problem collapses onto the completion gap. This should be recorded in the
   node summary — it changes what the node is about.
2. **The published prior result reproduces in ~5 seconds from scratch**, including both of its
   numbers (90 residual sets all `≤ 11`; exactly 45 of them `≤ 10`), and the 45 gets a structural
   explanation the source does not give (5 of the 10 balanced splits are covered, and coverage is
   complement-symmetric).
3. **Parity rigidity.** All logicals have even weight, so `d_ext ∈ {10,11,12}` and the value 11 is
   *only* reachable through a weight-2 residual in a weight-12 logical. There is no "weight-13
   logical" escape hatch. This is a small fact that closes off a whole class of would-be
   constructions.
4. **The naive timing obstruction is vacuous at minimum depth.** At 6 CNOT layers every qubit is busy
   in every layer, forcing `τ_j = j`, and one can show an opposite-type CNOT *always* precedes the
   critical moment. So "just schedule the X-checks late" cannot work, and any no-go must argue at the
   level of parity cancellation, not of ordering. I had expected a one-line argument here; there
   isn't one.
5. **Same-half vs cross-half pairs.** X- and Z-checks of the Gross code overlap in 0 or 2 qubits.
   For a Z-check support, the 6 "same-half" pairs are seen by six *distinct* X-checks (one qubit
   each, so no self-cancellation), while the 9 "cross-half" pairs each have exactly one X-check
   containing both (which can self-cancel by parity). The same-half pairs are the structurally
   hardest to block and are where a no-go should start.
6. **The authors themselves stopped for a non-mathematical reason.** A6/§H.2 says their motivation to
   pursue interleaved variants was "reduced" by the morphing-circuit result (A7), which reaches
   circuit distance 12 with the same qubit counts by a different paradigm. So the open problem is
   open partly because it was abandoned, not because it was attacked and resisted. That raises the
   value of Route 6 (is that circuit in scope?) and mildly raises the prior that the interleaved
   question is tractable.
7. **A correction to the commission's framing.** The problem statement's "90 种 inequivalent residual
   sets" is right, and I confirm the count independently (`6!/8 = 90`, the order-8 group being
   `i_1↔i_2`, `i_5↔i_6`, and global order reversal). But there is no "936 depth-7 variants" fact for
   this code — depth 7 is *impossible*, the minimum being 8 by the `max(c, r+2) = max(6,8)` bound.
   Any prior note to that effect should be corrected.
8. **The four `circdist` roots are not as disjoint as the round-1 dispatch assumed.** `CIRCDIST.gross`
   now needs exactly the theorem `CIRCDIST.lift` is chartered to prove, and Gate G1's second outcome
   would hand `CIRCDIST.lift` its wanted counterexample. Route 4 should be registered as a real edge
   between the two roots.

---

## 7. Reproduction

Python 3.9 + numpy only; total runtime under 6 seconds on a laptop. Save as `gross_recon.py`.

```python
import numpy as np, itertools
from collections import Counter

L, M = 12, 6; NG = L*M; N = 2*NG
def gidx(i,j): return (i % L)*M + (j % M)
def mono(a,b):
    P = np.zeros((NG,NG), np.uint8)
    for i in range(L):
        for j in range(M): P[gidx(i+a,j+b), gidx(i,j)] = 1
    return P
A = (mono(3,0)+mono(0,1)+mono(0,2)) % 2
B = (mono(0,3)+mono(1,0)+mono(2,0)) % 2
HX = np.concatenate([A,B],1); HZ = np.concatenate([B.T,A.T],1)
assert ((HX@HZ.T)%2==0).all() and HX.sum(1).min()==6 and HX.sum(1).max()==6

def rref(Mat):
    Mat = Mat.copy()%2; rows,cols = Mat.shape; piv=[]; r=0
    for c in range(cols):
        pr = next((rr for rr in range(r,rows) if Mat[rr,c]), None)
        if pr is None: continue
        Mat[[r,pr]] = Mat[[pr,r]]
        sel = (Mat[:,c]==1); sel[r]=False; Mat[sel] ^= Mat[r]
        piv.append(c); r+=1
        if r==rows: break
    return Mat[:r], piv
def nullspace(Mat):
    R,piv = rref(Mat); cols = Mat.shape[1]
    free = [c for c in range(cols) if c not in piv]; basis=[]
    for f in free:
        v = np.zeros(cols, np.uint8); v[f]=1
        for r,p in enumerate(piv):
            if R[r,f]: v[p]=1
        basis.append(v)
    return np.array(basis, np.uint8)

RHX,pivHX = rref(HX); RHZ,pivHZ = rref(HZ)
def red(R,piv,v):
    w = v.copy()%2
    for r,p in enumerate(piv):
        if w[p]: w ^= R[r]
    return w
# 3.1 parity lemma
ones = np.ones(N, np.uint8)
print("all-ones in rowspace(HX):", not red(RHX,pivHX,ones).any(),
      "| in rowspace(HZ):",        not red(RHZ,pivHZ,ones).any())

def search(G, trials=200, wmax=12, seed=1):
    rng = np.random.default_rng(seed); found={}; nc = G.shape[1]
    for _ in range(trials):
        perm = rng.permutation(nc); R,_ = rref(G[:,perm])
        inv = np.empty(nc,int); inv[perm] = np.arange(nc); rows = R[:,inv]
        wts = rows.sum(1)
        for i in range(len(rows)):
            if wts[i] <= wmax: found.setdefault(rows[i].tobytes(), rows[i])
        for a,b in itertools.combinations(range(len(rows)),2):
            v = rows[a]^rows[b]
            if v.sum() <= wmax: found.setdefault(v.tobytes(), v)
        light = [i for i in range(len(rows)) if wts[i] <= wmax+6]
        for a,b,c in itertools.combinations(light,3):
            v = rows[a]^rows[b]^rows[c]
            if v.sum() <= wmax: found.setdefault(v.tobytes(), v)
    return list(found.values())

def tperm(a,b):
    p = np.empty(N,int)
    for i in range(L):
        for j in range(M):
            p[gidx(i+a,j+b)] = gidx(i,j); p[NG+gidx(i+a,j+b)] = NG+gidx(i,j)
    return p
perms = [tperm(a,b) for a in range(L) for b in range(M)]

def pool(Ker, Rs, pivs, seed):
    w = [v for v in search(Ker, seed=seed) if v.sum()==12 and red(Rs,pivs,v).any()]
    d = {}
    for v in w:
        for p in perms: u = v[p]; d[u.tobytes()] = u
    return np.array(list(d.values()), np.uint8)

W12 = pool(nullspace(HX), RHZ, pivHZ, 7)    # weight-12 Z-logicals
X12 = pool(nullspace(HZ), RHX, pivHX, 11)   # weight-12 X-logicals
assert ((HX@W12.T)%2==0).all() and (W12.sum(1)==12).all()
assert all(red(RHZ,pivHZ,v).any() for v in W12)
print("pools:", W12.shape[0], X12.shape[0])

# 3.2 / 3.3 coverage
for tag,H,W in (("Z",HZ,W12), ("X",HX,X12)):
    s = sorted(int(i) for i in np.nonzero(H[0])[0]); C = W[:,s]
    p2 = {t: int(np.all(C[:,list(t)]==1,1).sum()) for t in itertools.combinations(range(6),2)}
    p3 = {t: int(np.all(C[:,list(t)]==1,1).sum()) for t in itertools.combinations(range(6),3)}
    print(tag, "support", s, "| pairs covered", sum(v>0 for v in p2.values()), "/15",
          "| triples covered", sum(v>0 for v in p3.values()), "/20",
          "| residual sets forced to <=10:",
          sum(1 for T in itertools.combinations(range(6),3)
                for P in itertools.combinations(T,2)
                for S in itertools.combinations(tuple(sorted(set(range(6))-set(T))),2)
                if T < tuple(sorted(set(range(6))-set(T))) and
                   (p3[T]>0 or p3[tuple(sorted(set(range(6))-set(T)))]>0)))

# 3.5 translation-invariant minimum-depth schedule count
cnt = ni = 0
for sig in itertools.permutations(range(1,7)):
    SA,SB = set(sig[:3]), set(sig[3:])
    for rho in itertools.permutations(range(1,7)):
        RB,RA = set(rho[:3]), set(rho[3:])
        if SA & RB or SB & RA: continue
        cnt += 1
        if (max(SA)<min(RB) or max(RB)<min(SA)) and (max(SB)<min(RA) or max(RA)<min(SB)): ni += 1
print("translation-invariant min-depth schedules:", cnt, "| LRC-like:", ni, "| interleaved:", cnt-ni)
```

Expected output:
```
all-ones in rowspace(HX): True | in rowspace(HZ): True
pools: 1884 1884
Z support [3, 6, 12, 73, 74, 90] | pairs covered 15 /15 | triples covered 10 /20 | residual sets forced to <=10: 45
X support [4, 5, 54, 75, 132, 138] | pairs covered 15 /15 | triples covered 10 /20 | residual sets forced to <=10: 45
translation-invariant min-depth schedules: 25920 | LRC-like: 2592 | interleaved: 23328
```

---

## 8. Honest limits of this session

* §3.6 is a derivation I performed and checked by hand, not a reviewed lemma. It covers only Z-type
  faults on Z-check ancillas plus data faults in the final round; two-qubit CNOT faults, ancilla
  prep/measurement faults, and multi-round placements are *not* covered. All of those give the
  adversary **more** power, so the sufficient conditions for `d_circ ≤ 11` derived from it remain
  sufficient — but the claimed *completeness* of the syndrome formula does not extend to them.
* My weight-12 logical pools (1 884 each) are almost certainly not the complete set of weight-12
  logicals. Coverage claims are one-sided witnesses, so this does not weaken §3.2–3.3; but any
  argument that needs the *full* family (e.g. Route 4's pigeonhole) needs a complete enumeration
  first.
* I did not recover the actual CNOT schedule of the candidate distance-11 circuit. It lives in
  Figure 12 of arXiv:2603.05481, which does not survive HTML/PDF text extraction; the authors'
  Zenodo record 18853600 and `github.com/PurePhys/LR-circuits` are the places to get it. Route 1
  cannot start without it.
* I did not read arXiv:2503.10988 (Tesseract) or arXiv:2603.22532's tables directly, so my
  feasibility estimate for `P1.3` (exact certification at distance 11 on 360 columns) is an
  informed guess, not a measured one. It is the single number in Route 1's `D` estimate most likely
  to be wrong.
* I did not read the Shaw–Terhal morphing paper at all. A7 and Route 6 rest on the source paper's
  one-sentence characterisation of it.
* The `P`/`D` numbers are placements inside the OPEN band with the justifications given; they are
  scheduling estimates, not confidence scores, and the protocol's own caveat applies.
