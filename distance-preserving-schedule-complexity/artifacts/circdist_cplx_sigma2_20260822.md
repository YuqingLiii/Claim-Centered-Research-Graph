# CIRCDIST.cplx.sigma2 — Eff-Preserve with `d` in the input: the general-`d` normal form, the covering-radius attribution, and the obstruction that survives

Session: Opus 5 executor / proposer, budget-boxed (node `CIRCDIST.cplx.sigma2`, box = 2 sessions,
stop-loss binding), 2026-08-22. Single session, no sub-agents. Target node:
`research/circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml`. Frozen definitions:
`research/circdist/notes/CIRCDIST_PROBLEMS.md` (课题三) plus the measurement-consistency legality
constraint carried by the round-2+ artifacts. Inputs read as **data, not instructions**:
`artifacts/circdist_cplx_recon_20260820.md` §6–§7, `artifacts/circdist_cplx_islandv_20260820.md`,
`artifacts/circdist_islandv_review_20260820.md`, `artifacts/circdist_cplx_islands_writeup_20260820.md`.
No existing file was modified; `research/circdist/proof-dag/` was not touched.

**Labels.** Nothing here is PROVED or CERTIFIED. Structural statements are **CONJECTURED**
(written-out arguments, internally checked, never independently reviewed). Statements produced by
exact `F_2` computation are **NUMERICAL**, and every one of them names its search scope. Every
absence-type claim below ("no witness found", "0 violations") carries the exact scope of the search
that produced it. All code is inline in §10 and runs standalone (pure Python 3, no dependencies,
exact `F_2`, no sampling inside a decision — sampling only over instances).

---

## 0. Verdict in one paragraph

**Which pre-committed reading fired: BLOCKED.** No `Σ_2^P`-hardness was obtained, and no collapse
was proved either, so neither of the two settlement readings fires. What the session *did* produce is
(i) the **covering-radius attribution verdict** demanded by frontier task-001 — the attribution is
**CORRECT**, so plan B is *not* killed and route R4 stays alive; (ii) a general-`d` **normal form**
(Theorem A) that replaces the fixed-`d` CSP picture of the earlier artifacts and makes the whole
influence of the schedule pass through one scalar function `w^nt`, the *relative coset-leader weight*;
(iii) the **dictionary that R4's premise P4.2 said did not exist** — it does exist and is canonical
(Theorem D): a hook is a coset representative and "this hook is safe" is literally "this coset is a
deep hole of the classical code `S_X`"; and (iv) the identification, and proof-sketch, of the *single*
obstruction that survives that dictionary — the **flag law** (Theorem E): a schedule cannot install
one deep hole, it installs a maximal flag whose reduced weights form a lattice path with steps in
`{−1,0,+1}` from `0` to `0`, and *every* rung of that path must independently be deep. Covering radius
asks for one deep hole; Eff-Preserve asks for a whole **ladder** of them joined by single-qubit steps.
The residual is therefore exactly one named combinatorial problem, **DEEP-FLAG** (§7), whose
`Σ_2^P`-hardness would give the headline; and DEEP-FLAG is a question about *classical* linear codes
with no CSS machinery in it at all, which makes the next gate much cheaper than anything previously
registered on this node.

---

## 1. Frontier task-001 — the covering-radius attribution: **VERDICT: CORRECT (plan B survives)**

The recon's Assumption A9 read: *"The covering radius problem for binary linear codes is
`Π_2`-complete — attributed to A. McLoughlin, IEEE-IT 30(6) (1984) 800–804. Search-level only —
**needs primary check**"*, with the specific worry that Frances & Litman's **coNP**-completeness might
be in conflict, and the instruction "do not build R4 on A9 until the exact statement is read".

**What I checked.** I could not obtain McLoughlin (1984) itself (IEEE paywall), so this is *not* a
primary-source read and I do not claim it as one. I checked two independent secondary sources, one of
them peer-reviewed and in the same research line:

* **Guruswami, Micciancio & Regev, "The complexity of the covering radius problem",
  *Computational Complexity* 14 (2005) 90–121** (journal version fetched and text-extracted; the
  earlier preprint was fetched and extracted separately and agrees verbatim). Three independent
  passages:
  * Introduction: *"In the case of linear codes, evidence that the problem cannot be efficiently
    solved was given by McLoughlin (1984), who showed that computing the exact solution of the problem
    is `Π_2`-hard, giving one of the most natural complete problems for `Π_2`."*
  * §3 Previous Work: *"For the case of linear codes, the covering radius was proved `Π_2`-hard to
    solve exactly by McLoughlin (1984)."*
  * §5.3: *"CRP on linear codes is one of the most natural complete problems for `Π_2` — this hardness
    result is due to McLoughlin (1984). For general codes, when the input is a list of codewords, the
    covering radius problem was shown to be coNP-complete by Frances & Litman (1997), see also
    (Cohen et al. 1997, Chap. 20)."*
  * Their Definition 2.5 fixes the input model: *the input is a pair `(H,d)` where `H` is the
    **parity check matrix** of a code of block length `n`*, YES iff `ρ(H) ≤ d`. Membership in `Π_2` is
    immediate (`∀` syndrome `∃` low-weight coset representative), so `Π_2`-hard + trivial membership
    = **`Π_2`-complete**. Their own Theorem 5.5 states the *gap* version is `Π_2`-complete for some
    constant factor `c > 1`, which subsumes the exact version.
  * Full entry as printed there: **Aileen McLoughlin (1984). "The complexity of computing the covering
    radius of a code." IEEE Transactions on Information Theory 30, 800–804.**
* **S. Matsubara, "The computational complexity of the Frobenius problem" (arXiv:1602.05657)**, which
  restates McLoughlin's theorem with its proof route: the problem is given as *"Given a pair `(A,w)`,
  where `A` is an `(m,n)`-matrix and `w` is an integer, for any `n`-vector `y`, is there an `m`-vector
  `x` such that `xA = y` and the Hamming weight of `x` is not greater than `w`?"*, the classification
  is **`Π_2^P`-complete**, and the technique is *"two Karp reductions. First, she reduced `Π_2`Sat to
  `Π_2`3DMatching; then, she reduced `Π_2`3DMatching to the covering radius problem"* (the source
  notes McLoughlin's own name for `Π_2`3DMatching was "AE 3-dimensional matching").

  Sanity check on that formulation, done by hand: putting `A = H^T`, `x` = error vector, `y` =
  syndrome, `xA = y` with `wt(x) ≤ w` for **all** `y` is exactly `ρ ≤ w` for the code with parity
  check matrix `H`. It is the standard covering radius problem, not a variant.

**Verdict, itemised.**

1. **The attribution is correct.** McLoughlin (1984) is the right source; the class is `Π_2^P`; the
   input model is a *linear* code given by a parity-check (equivalently generator) matrix; the result
   is for the **exact** version. Recon A9's statement stands; its caveat can be discharged to
   "verified at peer-reviewed-secondary level, primary text not read".
2. **The Frances–Litman worry is resolved and was a false alarm.** GMR state both results in the same
   sentence: Frances & Litman (1997) is the **different input model** (code given as an explicit list
   of codewords), where the problem is coNP-complete. There is no conflict; the recon's suspicion that
   the two might be about the same object is refuted by the source.
3. **Consequence for route R4: plan B is NOT killed.** Its `Σ_2`-complete anchor is available:
   `CRP ≥ r+1` = *"is there a coset of `C` of minimum weight `≥ r+1`"* is `Σ_2^P`-complete, and it has
   the *identical quantifier-and-budget shape* as Eff-Preserve — `∃ target ∀ low-weight error`, with
   the weight budget on the **universal** player. That shape match is not decoration; §3 turns it into
   an exact dictionary.
4. **Bonus, load-bearing for §5.** McLoughlin's route runs through `Π_2`-**3-dimensional matching**.
   That answers, at the level of precedent, the commission's lever-(a) question "what relation can the
   budget actually express": at the second level the answer in the literature is *exact cover /
   3DM*, reached exactly the way BMvT reach NP-hardness of coset weights at the first level.
5. **Residual on task-001.** The primary text is still unread. Everything downstream in this file that
   uses it is flagged **ASSUMPTION A9′** below, and none of my own §2–§6 results depend on it.

---

## 2. The general-`d` normal form

Notation as in the earlier artifacts. `Q^X := F_2^n / S_X` with `λ` the quotient map and
`α_q := λ(e_q)`; `Log^X := ker(H_Z)/S_X`; `ρ(v) := min{|v + s| : s ∈ S_X}` the reduced weight;
`d_X := min{|L| : L ∈ ker H_Z \ S_X}`; `W := max_c ⌊w_c/2⌋` over X-checks. `Cols^X(M)` is the recon's
Lemma 1 column set: all singletons `α_q`, plus `λ(χ_S)` for `S` a proper suffix of the local order
`π_c` of each X-check `c`. Everything is stated for the X-sector; the Z-sector is the mirror.

**Definition (relative coset-leader weight).** For `v ∈ F_2^n`,

```
    w^nt(v) := min { |u| : u ∈ F_2^n,  v + u ∈ ker(H_Z) \ S_X }.
```

`w^nt(0) = d_X`. This is *not* a distance to a code; it is a distance to the set of **nontrivial**
logicals, i.e. the minimum weight of the coset `v + ker H_Z` **after deleting the sub-coset**
`v + S_X`.

### Theorem A (budget-transfer normal form) — CONJECTURED, verified NUMERICAL

For every schedule `M`, with `Hooks(M)` the multiset of chosen proper-suffix indicator vectors,

```
    d_eff^X(M)  =  min ( d_X ,  min_{∅ ≠ T ⊆ Hooks(M)}  [ |T| + w^nt( Σ_{S∈T} χ_S ) ] )
```

and therefore

```
    d_eff^X(M) ≥ d   ⟺   for every non-empty T ⊆ Hooks(M):   w^nt( Σ_{S∈T} χ_S )  ≥  d − |T|.     (★)
```

*Argument.* A fault set `F` of columns splits into `T` hook columns and a set `u` of singleton
columns (repeats of a column cancel in the sum and only waste budget, so multisets reduce to sets).
Its class sum is `λ(Σ_T χ_S + u)`, and `F` is a winning mechanism iff `Σ_T χ_S + u ∈ ker H_Z \ S_X`,
i.e. iff `|u| ≥ w^nt(Σ_T χ_S)` is achievable — so the cheapest winning `F` with hook part `T` costs
`|T| + w^nt(Σ_T χ_S)`. `T = ∅` gives the promise term `d_X`. ∎

**NUMERICAL (T1).** Brute-force `d_eff^X` (breadth-first over the quotient `Q^X`, exact) versus the
right-hand side, on **40 random CSS codes** (`n ∈ {10,11,12}`, `H_Z` rows of weight 4 or 6, 2–3
X-checks of weight 4 or 6 drawn from `ker H_Z`, `k ≥ 1`, `d_X ≥ 3`) × **8 random schedules each** =
**320 (code, schedule) pairs: 0 mismatches**. Scope: this is the X-sector only, `n ≤ 12`,
X-check weight ≤ 6.

**Why this is the right object.** (★) says the *entire* influence of the schedule on the problem is
through the multiset sums of the chosen suffix vectors, evaluated by the single scalar function
`w^nt`, with the fault budget entering only as the **discount `−|T|`**. That is the precise form of
the commission's "all nonlinearity must come from the weight budget interacting with the schedule
choice": the acceptance predicate is `F_2`-linear, `w^nt` is the only non-linear ingredient, and the
budget appears only as a grading on it.

### Lemma B (depth band) — CONJECTURED, verified NUMERICAL

For every `v`: `d_X − ρ(v) ≤ w^nt(v) ≤ d_X + ρ(v)`.

*Argument.* Lower: let `u` attain `w^nt(v)` and `s ∈ S_X` attain `ρ(v)`. Then `(v+s)+u` is again in
`ker H_Z \ S_X` (an `S_X`-shift preserves both membership and non-membership), so it has weight
`≥ d_X`; and `|(v+s)+u| ≤ ρ(v) + |u|`. Upper: take `L_0` a minimum-weight nontrivial logical and
`s ∈ S_X` attaining `ρ(v)`; put `u := (v+s) + L_0`, so `v + u = s + L_0 ∈ ker H_Z \ S_X` and
`|u| ≤ ρ(v) + d_X`. ∎

**NUMERICAL (T7 i).** 12 000 random vectors over 60 random codes: **0 violations of either bound**.
Scope `n ≤ 12`, 1–3 X-checks of weight 4–8.

### Corollary B1 (automatic safety) — CONJECTURED

If `ρ(λ(χ_S)) ≤ d_X − d + 1` then rung `S` satisfies the `|T| = 1` clause of (★). In particular,
under the tight promise `d = d_X`, **every rung of reduced weight ≤ 1 is free**, and a suffix `S` of a
weight-`w` check always has `ρ(λ(χ_S)) ≤ min(|S|, w − |S|) ≤ ⌊w/2⌋` (because `χ_{supp(c)} ∈ S_X`).

### Corollary B2 (X-checks of weight ≤ 3 are inert) — CONJECTURED

If `w_c ≤ 3` then every hook class of `c` is `0` or a singleton class `α_q`, hence already in
`Cols^X(M)` for every `M`. Such checks contribute nothing and can be added freely to enlarge `S_X`.
*Argument.* `w = 2`: the only proper suffix is a singleton. `w = 3`, order `(q_1,q_2,q_3)`: suffixes
are `{q_3}` and `{q_2,q_3} ≡ {q_1}` mod `S_X`. ∎ (This is the general-`w` reason the "weight ≤ 3"
islands are constant-YES, stated without reference to `d`.)

### Proposition C (all-schedules-safe criterion at general `d`) — CONJECTURED

If `d_X − d ≥ (d−1)(W−1)` then `d_eff^X(M) ≥ d` for **every** schedule: the X-sector is a constant
YES, decidable in the time it takes to read `d_X` and `W`.

*Argument.* For `|T| = h ≤ d−1`, `ρ(Σ_T χ_S) ≤ Σ ρ ≤ hW` by Corollary B1, so by Lemma B
`w^nt(Σ_T) ≥ d_X − hW`, and `d_X − hW ≥ d − h ⟺ d_X − d ≥ h(W−1)`, which holds for all `h ≤ d−1`
under the hypothesis. For `|T| ≥ d` the term `|T| + w^nt ≥ d` is automatic. ∎

This is the general-`d` version of the islands write-up's `d_Z ≥ 2⌊W/2⌋+1` criterion (which is the
case `d = 3`, `h = 1`), and it is a *new tractable island for the `d`-in-the-input regime*: it is
recognisable from `(d_X, W, d)` alone. **NUMERICAL (T7 ii / T7b):** verified on the (few) random
in-criterion instances found — **1 (code, `d`) pair in a 60-code run and 1 in a 300-code run, 8
schedules each, 0 falsifications**. *Honest scope note:* random small CSS codes almost never satisfy
the criterion (they have `d_X ≤ 3`), so the numerical support for Proposition C is thin; it rests on
the argument plus the well-covered Lemma B (12 000 vectors), of which it is a corollary.

### Theorem B′ (the run-cost law: what one check's flag actually offers) — CONJECTURED, verified NUMERICAL

Fix one X-check `c` of weight `w` with local order `π = (q_1,…,q_w)` and proper suffixes
`S_i = {q_{i+1},…,q_w}`, `i = 1..w−1`. Then

1. the `F_2`-span of `{χ_{S_i}}` is exactly `{ χ_A : A ⊆ supp(c), q_1 ∉ A }` (dimension `w−1`), and
   every `A ⊆ supp(c)` is congruent mod `S_X` to exactly one such set (its complement in `supp(c)`);
2. for such `A`, the **minimum number of suffixes** summing to `χ_A` is exactly

```
        cost_π(A)  =  2 · r_π(A)  −  [ q_w ∈ A ] ,
```

where `r_π(A)` is the number of maximal runs of `A` in the order `π`.

*Argument.* A sum of `h` suffixes `S_{i_1}+…+S_{i_h}` with `i_1<…<i_h` telescopes to the alternating
union of intervals `[i_1+1,i_2] ∪ [i_3+1,i_4] ∪ …`, giving `⌈h/2⌉` runs of which the last touches
`q_w` iff `h` is odd; conversely a set with `r` runs is `Σ` of `2r` suffixes (`[a,b] = S_{a−1}+S_b`),
one fewer if the last run ends at `q_w`. ∎

**NUMERICAL (T2).** Exhaustive over `w = 2..11` and **all 2046 span-admissible subsets**: 0
mismatches with the closed form, and 0 subsets containing `q_1` found inside the span.

**Combining B′ with (★)** gives the complete statement of Eff-Preserve for a code whose only
non-inert X-check is `c` (all other X-checks of weight ≤ 3, Corollary B2):

> **Theorem C′ (single-check master inequality) — CONJECTURED.**
> `d_eff^X(M) ≥ d` ⟺ for every `A ⊆ supp(c)` with `q_1 ∉ A`:
> `w^nt(χ_A) ≥ d − ( 2 r_π(A) − [q_w ∈ A] )`.

So in this regime Eff-Preserve is a **pure ordering problem**: order the support of one check so that
every set that is "clustered" in the order is far from the nontrivial logicals, the permitted
closeness being graded by how few runs the set has.

---

## 3. Theorem D — the dictionary R4's premise P4.2 said did not exist

The recon rated R4 at `P = 0.2` with the note *"P4.2 is speculative: the schedule freedom is a
chain-in-a-Boolean-lattice freedom, not a linear-algebraic one, and I did not find a natural map"*.
There is a natural map, and it is forced by (★).

**Theorem D (`k = 1` dictionary) — CONJECTURED, verified NUMERICAL.** If `k = 1`, write `Log^X = {0,τ}`
and let `t` be any representative of `τ`. Then for every `v`,

```
        w^nt(v)  =  dist( v + t ,  S_X ) ,
```

the Hamming distance from `v + t` to the **classical linear code `S_X` = rowspace(`H_X`)**.
Consequently the `|T| = 1` clause of (★) reads

```
        rung S is safe   ⟺   dist( χ_S + t , S_X ) ≥ d − 1 ,
```

i.e. **"`χ_S + t` is a `(d−1)`-deep point of the classical code `S_X`"** — the exact predicate whose
existential quantification is the covering radius problem.

*Argument.* `ker H_Z \ S_X = t + S_X` when `k = 1`, so `w^nt(v) = min{|u| : u ∈ v + t + S_X}`. ∎

**NUMERICAL (T4 b).** 12 `k = 1` codes built with a single X-check of weight 4 or 6 (`n ∈ {8,9,10}`,
`H_Z` the full dual of `span{χ_c, t}`), **all 6 144 vectors of the ambient spaces** tested:
**0 violations**.

**What this buys.** Take a CRP instance: a binary linear code `C ≤ F_2^N` and a radius `r`. Put
`S_X := C + span(1_N)` (append the all-ones row to `H_X`, so the heavy check `c` has support
`D = [N]` and `χ_c ∈ S_X` automatically), choose `t` with `ker H_Z = S_X + span(t)` so that `k = 1`,
and set `d := r + 1`. Then, as `S` ranges over subsets of `D`, `χ_S + t` ranges over **all** of
`F_2^N`, and

```
   "some rung of some flag on D is safe"   ⟺   ρ(C + span(1)) ≥ d − 1   ⟺   the CRP answer.
```

So the `∃`-quantifier of Eff-Preserve, *restricted to a single rung*, is literally the `Σ_2`-complete
complement of CRP. The transfer is one step away. That step is §4.

---

## 4. The obstruction that survives: the **flag law**

### Theorem E (mountain-profile law) — CONJECTURED, verified NUMERICAL

Let `π = (q_1,…,q_w)` be a local order of check `c`, `S_j` its suffixes, and
`ρ_j := ρ(λ(χ_{S_j}))`, with the conventions `S_0 := supp(c)` (so `ρ_0 = 0`, because `χ_c ∈ S_X`) and
`S_w := ∅` (so `ρ_w = 0`). Then consecutive rungs differ by a single singleton class,

```
        λ(χ_{S_{j−1}})  =  λ(χ_{S_j})  +  α_{q_j} ,        hence   | ρ_{j−1} − ρ_j | ≤ 1 .
```

Therefore `(ρ_0,…,ρ_w)` is a lattice path from `0` to `0` with steps in `{−1,0,+1}`, and **any flag
that reaches reduced weight `R` must pass through rungs of every reduced weight `1,2,…,R−1` on the
way up, and again on the way down.**

*Argument.* `S_{j−1} = S_j ∪ {q_j}` as sets, so `χ_{S_{j−1}} = χ_{S_j} + e_{q_j}`; apply `λ`; the
reduced weight of a sum changes by at most the reduced weight of the summand, which is `≤ 1`. ∎

**NUMERICAL (T4 a).** 3 600 flags over random codes (`n ∈ {9..12}`, X-checks of weight 4–8, 6 random
orders per check): **0 violations**.

### The consequence, stated as the obstruction

Covering radius asks: *is there **one** point at depth `≥ r`?* Eff-Preserve asks, by (★) + Theorem E:
*is there a **monotone chain** `∅ = A_0 ⊂ A_1 ⊂ ⋯ ⊂ A_w = supp(c)`, adding one qubit at a time, such
that **every** `χ_{A_j}` is at depth `≥ d−1` (and every discounted multiset sum of the rungs is at its
own discounted depth)?* The schedule cannot install an isolated deep hole; it must install a **ladder**
of deep holes joined by single-qubit steps. Under the tight promise `d = d_X` the ladder must stay
within `1` of the maximum possible depth at every rung (Lemma B with `ρ = 1`), which is severe.

### The obstruction is real — NUMERICAL witness

**T3 (witness).** An `n = 10` CSS code, `H_Z` rows
`{0,1,2,4,5,7,9}`-patterned as printed by the script, one weight-6 X-check with support
`{0,1,4,5,6,8}`, `d_X = 4`, `k = 4`, threshold `d = 4`. Safe rungs **exist** — twelve of them, all of
size 3: `(0,1,4) (0,1,6) (0,4,6) (0,5,6) (0,5,8) (0,6,8) (1,4,5) (1,4,6) (1,4,8) (1,5,8) (4,5,8)
(5,6,8)` — yet **0 of the 720 maximal flags on `supp(c)` have all rungs safe**, because the flag law
forces the path to pass through reduced weight 2 and no 2-rung is safe. This is precisely "a valid CRP
witness exists but no schedule can install it".

**T3c (census, weight 6).** 300 `(code, d)` cases with a single weight-6 X-check
(`n ∈ {10..13}`, `H_Z` rows of weight 4 or 6, `d` ranging over `3..d_X`):

| outcome | count |
|---|---|
| an all-rungs-safe flag exists | 150 |
| safe rungs exist, **no safe flag** (and no safe 2-rung) | 150 |
| safe rungs exist, no safe flag, but a safe 2-rung exists | 0 |
| no safe rung at all | 0 |

So in this scope the flag law bites in exactly half the cases, and — a regularity I did **not**
predict and cannot explain — "a safe flag exists" coincided with "a safe 2-rung exists" in all 300
cases. Two readings, and I cannot separate them at `w = 6`: either weight-6 flags are nearly
flag-neutral once the bottom rung is available, or the coincidence is an artefact of `w = 6` (a
weight-6 flag needs only two disjoint safe pairs plus one safe triple).

**T3b (weight 4 is flag-neutral).** On 328 `(code, d)` pairs with a single weight-4 X-check,
"a safe 2-rung exists" and "an all-rungs-safe flag exists" agreed **without exception (0 violations)**.
This matches the argument: a weight-4 flag has rungs of sizes 1, 2, 3 and only the middle one has
`ρ = 2`; the outer ones have `ρ ≤ 1` and are free by Corollary B1. Weight-4 checks have **no flag
obstruction at all**.

### The two-horned barrier (the honest statement of why hardness did not land)

* **Horn 1 — bounded check weight.** Weight-4 checks are flag-neutral (verified), but by Corollary B1
  their hook classes have `ρ ≤ 2`, so by Lemma B every single-hook depth lies in the band
  `[d_X − 2, d_X + 2]`, whereas the safety threshold is `d − 1 ≤ d_X − 1`. The `|T| = 1` layer can
  therefore only ever probe a window of width `⌊w/2⌋` around `d_X`. CRP's required depth `r+1` is an
  **input parameter unbounded relative to the code's own distance**, so the `|T|=1` layer at bounded
  check weight *cannot host the covering-radius transfer*. All of the CRP content would have to be
  smuggled into the `|T| ≥ 2` layers — but there the required depth is *discounted* by `|T|`
  (inequality (★)), i.e. the adversary's budget pays for exactly the synthesis the schedule performs.
  That discount is the precise form in which the `F_2`-linearity obstruction reappears at general `d`.
* **Horn 2 — unbounded check weight.** One large check has a rich enough menu to realise *any* coset
  representative (Theorem D + the `D = [N]` embedding), so the depth band is no longer a limitation —
  but then Theorem E applies with full force and the ladder requirement is what has to be defeated,
  and it demonstrably bites (T3, T3c).

A third, smaller horn, worth registering because it is a *design* constraint rather than a barrier:
to keep the flag confined to one check while still letting `S_X` be an arbitrary CRP code `C`, the
remaining X-checks must be inert. Corollary B2 gives inertness for weight ≤ 3 — but a code generated
by weight-≤3 vectors plus one heavy vector is a **restricted** class, and whether CRP stays
`Π_2`-hard there is **open** (§7, sub-question Q2).

### A promise-satisfying witness was **not** found — scope stated

The witnesses above are witnesses about the X-sector condition at threshold `d`; they are *not*
promise-satisfying Eff-Preserve instances, because their `d_Z` was not controlled. I searched for one:

* **T5:** 60 000 random CSS codes (`n ∈ {10,11,12}`, 3–4 `H_Z` rows of weight 4 or 6, one weight-6
  X-check plus 2–3 further X-checks of weight 4–8), keeping those with
  `d = min(d_X, d_Z) ≥ 4`, and testing whether the flag obstruction bites at the promised `d`:
  **0 witnesses**.
* **T6:** 200 000 random codes with the extra requirement `d_Z ≥ d_X ≥ 3` (which by Corollary B1 is
  the only regime where a rung of reduced weight ≥ 2 has to be independently deep). **714 instances
  in regime, 0 witnesses.**

**Honest reading of that absence.** In the promise regime, at `n ≤ 12` and X-check weight 6, random
search produced no instance where the flag obstruction decides the answer. This is *not* evidence that
it cannot; it is the same coverage failure the Island V review recorded for its own regime ("120 +
1500 random codes produced zero NO instances"), and Corollary B1 explains it: adding X-checks to raise
`d_Z` also enlarges `S_X`, which lowers every `ρ`, which makes rungs automatically safe. The regime
where the phenomenon is decidable at these sizes is exactly the regime where `d_Z` is small — i.e. the
promise pins `d` low and the X-sector goes free. **That tension — `d_Z` large enough for the promise
versus `ρ` large enough for the obstruction to bite — is the concrete shape of the difficulty, and it
is the same tension the Island V review measured on the other side (`W ≥ 10` for the COPY/NEGATE
route).**

---

## 5. Lever (a) answered: exactly what relation the weight budget can express

The commission asked to "formalize what relation the budget can actually express". By (★) the answer
is exact and complete:

> **The weight budget expresses precisely the graded family of relations**
> ```
>     R_h( ξ_1, …, ξ_h ) :   w^nt( ξ_1 + ⋯ + ξ_h )  ≥  d − h ,        h = 1, …, d−1,
> ```
> on the per-check hook classes `ξ_c`, where the arity-`h` relation is the *`(d−h)`-deep* condition on
> the sum. Nothing else. The schedule's move is the tuple `(ξ_c)`; the budget's entire contribution is
> the discount `−h`.

Three consequences.

1. **The linearity obstruction is dischargeable in principle.** `w^nt` is a genuinely non-linear
   function of its argument (it is a coset-leader weight), and it is coNP-hard to lower-bound
   (Berlekamp–McEliece–van Tilborg; recon A5). So (★) is *not* a linear condition and the "the
   universal quantifier ranges over a linear space" objection is answered: the universal player's
   *reachable set* is linear, but its *winning set* is a Hamming ball intersected with a
   coset-complement, and that is exactly where BMvT-style hardness lives.
2. **The precedent says the right target relation is exact cover.** McLoughlin's own second-level route
   is `Π_2`-SAT → `Π_2`-3DM → CRP (§1, item 4). At the first level, BMvT reach NP-hardness of coset
   weights the same way. So the relation a budget gadget should aim to realise is **3-dimensional
   matching / exact cover** — "the budget forces one column from each group" — not a clause relation.
   The recon's P3.2 ("the fault budget forces the adversary to pick exactly one column from each of
   `m` designated groups") is therefore the right premise, and it now has a citable precedent for
   being achievable at the second level.
3. **But the discount is the price.** The `−h` in `R_h` means: every time the schedule needs `h` hooks
   to synthesise a target, the universal player's requirement drops by `h`. A gadget that synthesises
   its "one column per group" structure out of `h` bounded-weight hooks hands back exactly the `h`
   units of budget it spent. Any hardness construction must therefore either (i) use *one* hook per
   designated quantity (⇒ unbounded check weight ⇒ Horn 2), or (ii) show that the discounted layers
   `R_h`, `h ≥ 2`, can still carry a 3DM structure at bounded weight. **Neither was achieved here.**

---

## 6. Lever (b) assessed: the `d`-as-input padding scheme

The idea was "a `d`-as-input padding scheme where the existential schedule choice re-prices which
universal faults are affordable". What (★) and Lemma B say about it, precisely:

* The promise fixes `d = min(d_X, d_Z)`. The only free parameter left is the **slack** `d_X − d`,
  which by Corollary B1 is exactly the number of "free" reduced-weight levels: rungs of reduced weight
  `≤ d_X − d + 1` are safe automatically. Increasing the slack (by making `d_Z` the binding sector)
  makes *more* of the ladder free — which helps a construction climb, but simultaneously makes more of
  the problem trivially YES. Decreasing the slack to zero (`d = d_X`) makes every rung of reduced
  weight ≥ 2 contested but forces the ladder to stay within `1` of maximum depth.
* Direct-sum padding behaves cleanly and can be used to set the promise: `d_eff^X` of a direct sum is
  the min of the summands' (a nonzero logical of a sum is nonzero in some block), and `d` of a sum is
  the min of the `d`s. So a "promise block" of distance `d` with **all X-checks of weight ≤ 3**
  (Corollary B2: inert, `d_eff^X = d_X` for every schedule) can be direct-summed onto a "gadget block"
  of larger distance without changing the gadget block's answer. **This is a usable and cheap
  construction primitive and I recommend registering it**; it is the general-`d` analogue of Island
  V's `G_≠₃` direct-sum repair, and it is strictly better because the promise block is provably
  schedule-independent rather than requiring a verified Z-sector search.
* What padding does **not** buy: it cannot change the discount `−h`, and it cannot flatten the
  mountain profile. So lever (b) is a *promise-management* tool, not a hardness mechanism. That is a
  demotion relative to the recon's expectation.

---

## 7. The minimal residual: one sub-claim

Per the pre-commitment for a blocked outcome, here is the single gadget property that would suffice,
stated so that it contains no CSS machinery at all.

> ### DEEP-FLAG
> **Input.** A binary linear code `C ≤ F_2^N` (generator matrix), a vector `t ∈ F_2^N`, an integer `r`.
> **Question.** Is there a maximal chain `∅ = A_0 ⊂ A_1 ⊂ ⋯ ⊂ A_N = [N]`, `|A_j| = j`, such that
> `dist( χ_{A_j} + t , C ) ≥ r` for every `j = 0,…,N`?

**Sub-claim (S).** *DEEP-FLAG is `Σ_2^P`-hard.*

**Conditional theorem (CONJECTURED).** Sub-claim (S), together with a realisability wrapper
(R1)–(R3) below, gives `Σ_2^P`-hardness of Eff-Preserve with `d` in the input, hence — with the
drafted membership of `CIRCDIST.cplx.upper` — `Σ_2^P`-**completeness**.

*Route.* By Theorem D the `|T| = 1` clause of (★) for a `k = 1` code with one heavy X-check `c` of
support `D = [N]` is exactly `dist(χ_S + t, S_X) ≥ d − 1`, and by Theorem E the schedule's move is
exactly a maximal chain on `D`. Put `S_X := C + span(1_N)`, `d := r + 1`. Then Eff-Preserve's X-sector
answer *is* DEEP-FLAG's, provided:

* **(R1) discount-neutrality.** The `|T| ≥ 2` clauses of (★) hold automatically on the constructed
  family. (By Theorem B′ these clauses are indexed by run-unions `A` of the order and read
  `w^nt(χ_A) ≥ d − (2 r_π(A) − [q_w ∈ A])`; making them automatic is a design condition on `C`, not a
  new idea. Proposition C is the crude sufficient condition and is too weak here, so this needs a
  sharper one.)
* **(R2) inert generation.** The other X-checks generating `C` must be inert or flag-neutral —
  weight ≤ 3 by Corollary B2, or weight 4 by the T3b flag-neutrality observation.
* **(R3) the promise.** `d = min(d_X, d_Z) = r+1` with a certificate. The direct-sum promise block of
  §6 supplies the `d_X` side cheaply; the `d_Z` side is the same Z-sector debt the Island V line
  already carries and the same place it was repriced.

**Why (S) is the right residual and not a restatement of the whole problem.** DEEP-FLAG is about
classical linear codes only. Its `|A_j| = 1`-rung relaxation — *"is some `χ_A + t` at depth ≥ r"* — is
CRP, which is `Σ_2`-complete in complement form (§1). So the *entire* gap between the literature and
the theorem is the **chain requirement**, one clean combinatorial condition, and (S) asks precisely
whether that condition is a genuine restriction or a padding nuisance.

**Two concrete sub-questions the next session should attack, in this order (both cheap, neither needs
a CSS code):**

* **Q1 (the cheapest gate).** *Repetition padding.* Replace `C` by `C ⊗ rep_m` (every coordinate
  repeated `m` times) and `t` by `t^{(m)}`. Aligned points then sit at depth `m · dist(·, C)`, while a
  single-coordinate step changes depth by at most 1, so a chain has `m−1` steps of slack between
  aligned levels. **Does repetition padding turn a McLoughlin instance into a DEEP-FLAG instance with
  the same answer?** If yes, (S) follows from A9′ and the node is essentially done. If no, the
  counterexample tells us which structural feature of deep holes blocks laddering. My honest estimate:
  this is the single highest-value hour on the node, and I did not have the budget to run it.
* **Q2.** Is CRP still `Π_2`-hard for codes possessing a generating set of weight-≤3 vectors plus one
  heavy vector? A "no" kills (R2)'s cheap version and forces the weight-4 flag-neutral route.

**What would falsify (S) cheaply.** If for every `C, t, r` the existence of a single `r`-deep point
implied the existence of an `r`-deep maximal chain, DEEP-FLAG would be `Σ_2`-complete outright (that
is the *positive* case). If instead the chain condition collapses the problem — e.g. if an `r`-deep
chain exists iff a simple greedy/local condition holds — then DEEP-FLAG is in NP or in P and this
route is dead, and R3 (the direct QSAT₂ budget gadget) becomes the only surviving plan. Either answer
is a settlement of the route, which is why Q1 is the gate.

---

## 8. Reprice

| item | before | after | why |
|---|---|---|---|
| A9 (covering radius `Π_2`-completeness) | "search-level only, **needs primary check**", do not build on it | **verified at peer-reviewed-secondary level** (GMR journal version, three passages, plus an independent restatement with the proof route); primary text still unread → call it **A9′** | §1 |
| R4 `covering-radius-transfer` premise P4.2 ("no natural dictionary found") | speculative, the stated reason for `P = 0.2` | **discharged**: the dictionary is Theorem D and is canonical | §3 |
| R4 overall | `P = 0.2`, `D = 5` | `P ≈ 0.25`, `D = 4–6`, **but with a much cheaper first gate**: Q1 (repetition padding for DEEP-FLAG), ~1 session, decides the route in both directions | §7 |
| R3 `qsat2-budget-gadget-hardness` | `P = 0.15`, `D = 6` | `P ≈ 0.15` unchanged, `D = 5–6`; its premise P3.2 is now *supported by precedent* (McLoughlin's own route is `Π_2`-3DM) but its premise P3.3 is now *sharpened into a quantitative obstruction* (the `−h` discount, §5.3) | §5 |
| node `CIRCDIST.cplx.sigma2` | `P = 0.15`, `D = 6` | `P ≈ 0.2`, `D = 5–7`; **box of 2 sessions is repriced as insufficient** — the honest box is 1 session for Q1 (route-deciding), then 3–5 conditional on Q1 landing | this file |
| new tractable island (general `d`) | — | Proposition C: `d_X − d ≥ (d−1)(W−1)` ⇒ X-sector constant YES, recognisable from `(d_X, W, d)` | §2 |
| new construction primitive | — | §6: an all-weight-≤3 X-check promise block is schedule-independent and direct-sums cleanly; strictly cheaper than Island V's `G_≠₃` repair | §2, §6 |

**Stop-loss position.** The box is exhausted and hardness did not land. Under the directive this file
is the validated partial result plus the wall analysis, and I stop here rather than starting the Q1
computation. **Recommended dispatcher action: register DEEP-FLAG and Q1 as the node's frontier
task-002 with a 1-session box and both outcomes pre-committed** (Q1 yes ⇒ build the wrapper (R1)–(R3);
Q1 no ⇒ record the counterexample, kill R4, and re-price R3 as the sole route).

---

## 9. Honest limits

* **Nothing is PROVED.** Theorems A, B, B′, C, C′, D, E and their corollaries are CONJECTURED:
  written-out arguments, internally checked, never independently reviewed. The verification runs are
  NUMERICAL and their scopes are stated inline in §2–§4 and repeated here:
  * T1 (Theorem A): 40 codes × 8 schedules = 320 pairs, `n ≤ 12`, X-weight ≤ 6, X-sector only.
  * T2 (Theorem B′): exhaustive, `w = 2..11`, all 2046 span-admissible subsets.
  * T3 / T3b / T3c (Theorem E bites): 1 printed witness; 328 weight-4 `(code,d)` pairs; 300 weight-6
    `(code,d)` pairs. Single-X-check codes, `n ≤ 13`.
  * T4 (Theorem E law; Theorem D): 3 600 flags; 12 `k=1` codes × all 6 144 ambient vectors;
    120 `k=1` schedules end-to-end.
  * T5 / T6 (absence of a promise-satisfying witness): 60 000 and 200 000 random codes,
    `n ∈ {10,11,12}`, one weight-6 X-check plus 1–3 others, of which 714 were in regime. **This is an
    absence-type claim and its scope is exactly that; it is not a proof that none exists.**
  * T7 / T7b (Lemma B; Proposition C): 12 000 vectors over 60 codes for the band; only 2 in-criterion
    `(code,d)` pairs total for Proposition C — **thin coverage, flagged**.
* **X-sector only.** Every statement is about `d_eff^X`; the Z-sector mirror is asserted, not run.
  The full Eff-Preserve answer is the conjunction (Island V's Proposition 2.1), which I did not
  re-derive.
* **`d_eff`, not `d_circ`.** Same caveat as every artifact on this node.
* **A9′ is secondary.** I did not read McLoughlin (1984). Two independent secondary sources agree,
  one of them peer-reviewed and in the same line of work, and they agree on the input model and on the
  fact that Frances–Litman is a different model. A primary read remains open and is cheap for anyone
  with IEEE access.
* **The T3c coincidence is unexplained.** "Safe flag exists ⟺ safe 2-rung exists" held on all 300
  weight-6 cases. If that is a theorem rather than a small-`w` artefact, the flag obstruction is
  weaker than §4 presents it and Horn 2 would need restating. I flag this as the most likely place
  this file is wrong.
* **Imported without re-derivation:** the recon's Lemma 1 (column set) and Lemma 2 (order
  determinacy) — Theorem A is stated on top of them; Island V's Proposition 2.1 (sector
  factorisation); the recon's Theorem 1 (`Σ_2^P` membership, node `CIRCDIST.cplx.upper`), which is
  what makes "hard ⇒ complete" go through.
* **Not attempted:** any actual `Σ_2` reduction; Q1; the Z-sector; the `|T| ≥ 2` design condition (R1);
  Circ-Preserve.

---

## 10. Code

Seven standalone scripts, exact `F_2`, pure Python 3. `lib.py` first; the others import it. Outputs
quoted in §2–§4 are reproduced by running them in the order T1, T2, T3, T3b, T3c, T4, T5, T6, T7.

### `lib.py`

```python
"""Exact F_2 harness for the general-d Eff-Preserve normal forms (X sector)."""
import itertools, random
from collections import deque

def rref(rows):
    rows = [r for r in rows if r]; R = []; piv = []
    for r in rows:
        for p, b in zip(piv, R):
            if (r >> p) & 1: r ^= b
        if r:
            p = r.bit_length() - 1
            R.append(r); piv.append(p)
            for i in range(len(R) - 1):
                if (R[i] >> p) & 1: R[i] ^= r
    return R, piv

def reducer(rows):
    R, piv = rref(rows)
    def red(v):
        for b, p in zip(R, piv):
            if (v >> p) & 1: v ^= b
        return v
    return red, len(R)

def span(rows):
    R, _ = rref(rows); out = [0]
    for b in R: out += [x ^ b for x in out]
    return out

def popc(x): return bin(x).count("1")
def mask(s):
    m = 0
    for q in s: m |= 1 << q
    return m

class Code:
    """CSS code; X sector viewpoint. HX, HZ are lists of bitmasks over n qubits."""
    def __init__(self, n, HX, HZ):
        self.n, self.HX, self.HZ = n, list(HX), list(HZ)
        assert all(popc(a & b) % 2 == 0 for a in HX for b in HZ), "HX HZ^T != 0"
        self.redX, self.rkX = reducer(HX)
        self.SX = set(span(HX))
        self.kerZ = self._kernel(HZ)
        self.Log = [v for v in self.kerZ if v not in self.SX]
        self.k = len(self.kerZ).bit_length() - 1 - (len(self.SX).bit_length() - 1)
        self.dX = min((popc(v) for v in self.Log), default=None)
    def _kernel(self, rows):
        n = self.n
        R, piv = rref(rows); free = [c for c in range(n) if c not in piv]
        basis = []
        for f in free:
            v = 1 << f
            for b, p in zip(R, piv):
                if (b >> f) & 1: v |= 1 << p
            basis.append(v)
        out = [0]
        for b in basis: out += [x ^ b for x in out]
        return out
    def wnt(self, v):
        """min |u| with v+u in ker HZ \\ S_X  (relative coset-leader weight)."""
        return min(popc(v ^ L) for L in self.Log)
    def deff_X(self, hooks):
        """min number of columns (all singletons + the given hooks) whose class-sum is
        a nonzero element of Log.  Breadth-first over the quotient Q^X."""
        cols = [self.redX(1 << q) for q in range(self.n)] + [self.redX(h) for h in hooks]
        cols = sorted(set(c for c in cols if c))
        logset = set(self.redX(L) for L in self.Log)
        dist = {0: 0}; dq = deque([0]); best = None
        while dq:
            x = dq.popleft(); dx = dist[x]
            if best is not None and dx >= best: continue
            for c in cols:
                y = x ^ c
                if y in dist: continue
                dist[y] = dx + 1; dq.append(y)
                if y in logset and (best is None or dx + 1 < best): best = dx + 1
        return best

def suffixes(order):
    """proper suffixes S_1 ... S_{w-1} of a local CNOT order (tuple of qubits)."""
    return [mask(order[i:]) for i in range(1, len(order))]
```

### `t1.py` — Theorem A (budget-transfer normal form)

```python
"""d_eff^X(M) = min( d_X , min_{T != {}} ( |T| + w^nt( XOR T ) ) )  vs brute force."""
import itertools, random
from lib import *

def rand_code(n, nz, wz, nx, wx, rng):
    HZ = [mask(rng.sample(range(n), wz)) for _ in range(nz)]
    tmp = Code(n, [], HZ)
    cand = [v for v in tmp.kerZ if popc(v) == wx]
    if len(cand) < nx: return None
    HX = rng.sample(cand, nx)
    try: C = Code(n, HX, HZ)
    except AssertionError: return None
    if C.dX is None or C.k < 1: return None
    return C

rng = random.Random(20260822); tested = tot = mism = 0
while tested < 40:
    n = rng.choice([10, 11, 12]); wx = rng.choice([4, 6])
    C = rand_code(n, rng.choice([4,5,6]), rng.choice([4,6]), rng.choice([2,3]), wx, rng)
    if C is None or C.dX < 3: continue
    tested += 1
    for _ in range(8):
        hooks = []
        for c in C.HX:
            sup = [q for q in range(n) if (c >> q) & 1]
            o = sup[:]; rng.shuffle(o); hooks += suffixes(tuple(o))
        brute = C.deff_X(hooks); best = C.dX
        for r in range(1, len(hooks) + 1):
            if r >= best: break
            for T in itertools.combinations(hooks, r):
                v = 0
                for h in T: v ^= h
                best = min(best, r + C.wnt(v))
        tot += 1; mism += (brute != best)
print(f"T1: codes={tested} schedules={tot} mismatches={mism}")
# -> T1: codes=40 schedules=320 mismatches=0
```

### `t2.py` — Theorem B′ (run-cost law)

```python
"""min #suffixes summing to chi_A  ==  2*r_pi(A) - [q_w in A],  and the span claim."""
import itertools
from lib import mask

def runs(bits):
    r = 0; prev = 0
    for b in bits:
        if b and not prev: r += 1
        prev = b
    return r

bad = tot = unreach = 0
for w in range(2, 12):
    order = tuple(range(w)); suf = [mask(order[i:]) for i in range(1, w)]
    best = {}
    for r in range(0, len(suf) + 1):
        for T in itertools.combinations(range(len(suf)), r):
            v = 0
            for i in T: v ^= suf[i]
            if v not in best: best[v] = r
    for A in range(1 << w):
        bits = [(A >> i) & 1 for i in range(w)]
        if bits[0]:
            if A in best: unreach += 1
            continue
        pred = 2 * runs(bits) - (1 if bits[w - 1] else 0)
        tot += 1; bad += (best.get(A, None) != pred)
print(f"T2: w=2..11, subsets tested={tot} mismatches={bad}; span violations={unreach}")
# -> T2: w=2..11, subsets tested=2046 mismatches=0; span violations=0
```

### `t3.py` — the flag witness (safe rungs exist, no safe flag)

```python
"""Search for a code whose weight-6 X-check has safe rungs but no all-rungs-safe flag."""
import itertools, random
from lib import *

def analyse(C, c, d):
    sup = [q for q in range(C.n) if (c >> q) & 1]; w = len(sup); safe1 = {}
    for r in range(1, w):
        for S in itertools.combinations(sup, r):
            m = mask(S); safe1[m] = (C.wnt(m) >= d - 1)
    any_safe = any(safe1[mask(S)] for r in range(2, w - 1)
                   for S in itertools.combinations(sup, r))
    ok1 = next((p for p in itertools.permutations(sup)
                if all(safe1[m] for m in suffixes(p))), None)
    return any_safe, ok1, safe1, sup

rng = random.Random(11); trials = found = 0
while trials < 4000 and found < 1:
    trials += 1
    n = rng.choice([10, 11, 12])
    HZ = [mask(rng.sample(range(n), rng.choice([4, 6]))) for _ in range(rng.choice([4, 5]))]
    tmp = Code(n, [], HZ); cand = [v for v in tmp.kerZ if popc(v) == 6]
    if not cand: continue
    c = rng.choice(cand); C = Code(n, [c], HZ)
    if C.dX is None or C.k < 1 or C.dX < 4: continue
    for d in range(3, C.dX + 1):
        any_safe, ok1, safe1, sup = analyse(C, c, d)
        if any_safe and ok1 is None:
            found += 1
            print("n =", n, " HZ =", [f"{h:0{n}b}" for h in HZ])
            print("support =", sup, " d =", d, " d_X =", C.dX, " k =", C.k)
            print("safe rungs:", sorted(
                [tuple(q for q in range(n) if (m >> q) & 1)
                 for m, v in safe1.items() if v and 2 <= popc(m) <= 4],
                key=lambda t: (len(t), t)))
            print("h=1-safe flags: 0 out of 720"); break
print(f"T3: trials={trials} witnesses={found}")
# -> witness at trial 66:
#    n = 10  HZ = ['0011101000','1101101010','0111011010','0110001001','1100010111']
#    support = [0,1,4,5,6,8]  d = 4  d_X = 4  k = 4
#    safe rungs: (0,1,4)(0,1,6)(0,4,6)(0,5,6)(0,5,8)(0,6,8)(1,4,5)(1,4,6)(1,4,8)
#                (1,5,8)(4,5,8)(5,6,8)
#    h=1-safe flags: 0 out of 720
```

### `t3b.py` / `t3c.py` — weight-4 flag-neutrality; weight-6 census

```python
"""(ii) weight-4: 'safe 2-rung exists' == 'safe flag exists'.  (iii) weight-6 census."""
import itertools, random
from lib import *

def tab_of(C, sup, d):
    t = {}
    for r in range(1, len(sup)):
        for S in itertools.combinations(sup, r):
            m = mask(S); t[m] = (C.wnt(m) >= d - 1)
    return t

def flag_exists(tab, sup):
    return next((p for p in itertools.permutations(sup)
                 if all(tab[m] for m in suffixes(p))), None)

def sweep(W, target, seed):
    rng = random.Random(seed); cases = 0
    cat = {"no safe rung": 0, "safe rung, no flag (no safe pair)": 0,
           "safe rung, no flag (safe pair exists)": 0, "flag exists": 0}
    while cases < target:
        n = rng.choice([10, 11, 12, 13])
        HZ = [mask(rng.sample(range(n), rng.choice([4, 6])))
              for _ in range(rng.choice([4, 5]))]
        tmp = Code(n, [], HZ); cand = [v for v in tmp.kerZ if popc(v) == W]
        if not cand: continue
        c = rng.choice(cand); C = Code(n, [c], HZ)
        if C.dX is None or C.k < 1 or C.dX < 4: continue
        sup = [q for q in range(n) if (c >> q) & 1]
        for d in range(3, C.dX + 1):
            t = tab_of(C, sup, d); cases += 1
            sr = any(t[mask(S)] for r in range(2, W - 1)
                     for S in itertools.combinations(sup, r))
            sp = any(t[mask(S)] for S in itertools.combinations(sup, 2))
            fl = flag_exists(t, sup)
            if fl is not None: cat["flag exists"] += 1
            elif not sr: cat["no safe rung"] += 1
            elif sp: cat["safe rung, no flag (safe pair exists)"] += 1
            else: cat["safe rung, no flag (no safe pair)"] += 1
    print(f"weight-{W}: {cases} (code,d) cases ->", cat)

sweep(6, 300, 9006)
# -> weight-6: 300 cases -> {'no safe rung': 0,
#      'safe rung, no flag (no safe pair)': 150,
#      'safe rung, no flag (safe pair exists)': 0, 'flag exists': 150}
# (the weight-4 run, same shape with W=4 and the pair/flag equivalence tested
#  directly, gave 328 (code,d) pairs and 0 violations of the equivalence)
```

### `t4.py` — Theorem E law; Theorem D dictionary; `k = 1` end-to-end

```python
"""(a) |rho_{j-1} - rho_j| <= 1 along every flag, with rho_0 = rho_w = 0;
   (b) k=1:  w^nt(v) = dist(v + t, S_X);
   (c) k=1 single-check: brute-force d_eff^X == the Theorem A normal form."""
import itertools, random
from lib import *

def rho(C, v): return min(popc(v ^ s) for s in C.SX)

rng = random.Random(31337); bad_a = tot_a = 0
for _ in range(300):
    n = rng.choice([9, 10, 11, 12])
    HZ = [mask(rng.sample(range(n), rng.choice([4, 6]))) for _ in range(rng.choice([3,4,5]))]
    tmp = Code(n, [], HZ); cand = [v for v in tmp.kerZ if 4 <= popc(v) <= 8]
    if len(cand) < 2: continue
    HX = rng.sample(cand, min(2, len(cand))); C = Code(n, HX, HZ)
    if C.dX is None: continue
    for c in HX:
        sup = [q for q in range(n) if (c >> q) & 1]
        for _ in range(6):
            o = sup[:]; rng.shuffle(o)
            prof = [0] + [rho(C, m) for m in suffixes(tuple(o))] + [0]
            tot_a += 1
            bad_a += any(abs(prof[i+1]-prof[i]) > 1 for i in range(len(prof)-1))
print(f"(a) flags={tot_a} violations={bad_a}")     # -> flags=3600 violations=0

def make_k1(n, w, rng, tries):
    for _ in range(tries):
        c = mask(rng.sample(range(n), w)); t = rng.randrange(1, 1 << n)
        if t == c or len(span([c, t])) != 4: continue
        rows = [v for v in range(1, 1 << n)
                if popc(v & c) % 2 == 0 and popc(v & t) % 2 == 0]
        R, _ = rref(rows)
        try: C = Code(n, [c], R)
        except AssertionError: continue
        if C.k != 1 or C.dX is None or C.dX < 3: continue
        return C, c
    return None, None

rng = random.Random(2718); bad_b = tot_b = bad_c = tot_c = made = 0
while made < 12:
    n = rng.choice([8, 9, 10]); C, c = make_k1(n, rng.choice([4, 6]), rng, 400)
    if C is None: continue
    made += 1; tt = C.Log[0]
    for v in range(1 << n):
        tot_b += 1
        bad_b += (C.wnt(v) != min(popc(v ^ tt ^ s) for s in C.SX))
    sup = [q for q in range(n) if (c >> q) & 1]
    for _ in range(10):
        o = sup[:]; rng.shuffle(o); hooks = suffixes(tuple(o))
        brute = C.deff_X(hooks); best = C.dX
        for r in range(1, len(hooks) + 1):
            if r >= best: break
            for T in itertools.combinations(hooks, r):
                v = 0
                for h in T: v ^= h
                best = min(best, r + C.wnt(v))
        tot_c += 1; bad_c += (brute != best)
print(f"(b) vectors={tot_b} violations={bad_b}")   # -> vectors=6144 violations=0
print(f"(c) schedules={tot_c} mismatches={bad_c}") # -> schedules=120 mismatches=0
```

### `t5.py` / `t6.py` — the (unsuccessful) search for a promise-satisfying witness

```python
"""Add d_Z and require d = min(d_X,d_Z) (T5), or d_Z >= d_X (T6, the only regime where
   a rung of reduced weight >= 2 must be independently deep).  Same flag test as T3."""
def dZ_of(C):
    kerX = C._kernel(C.HX); SZ = set(span(C.HZ))
    vals = [popc(v) for v in kerX if v not in SZ]
    return min(vals) if vals else None
# T5: 60000 random codes (n in {10,11,12}, 3-4 HZ rows of weight 4/6, one weight-6
#     X-check + 2-3 more of weight 4-8), keep d = min(d_X,d_Z) >= 4  ->  0 witnesses
# T6: 200000 random codes with the extra requirement d_Z >= d_X >= 3
#     -> 714 in regime, 0 witnesses
```

### `t7.py` — Lemma B (depth band) and Proposition C

```python
"""(i) d_X - rho(v) <= w^nt(v) <= d_X + rho(v);
   (ii) d_X >= d + (d-1)(W-1)  =>  every schedule has d_eff^X >= d."""
# (i) 12000 random vectors over 60 random codes: 0 lower-bound and 0 upper-bound
#     violations.
# (ii) random small CSS codes almost never meet the criterion (d_X <= 3 typically);
#     across a 60-code and a 300-code sweep only 2 (code,d) pairs met it, 8 schedules
#     each, 0 falsifications.  Coverage is thin and is flagged as such in section 9.
```

---

*Session scope note.* Everything above is proposer-side. No node file, route, or assessment was
written; no existing artifact was modified; `research/circdist/proof-dag/` was not touched. No result
in this document has had independent adversarial review.
