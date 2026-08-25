# k-Sum Lean audit — GAP-CLOSURE COMMISSION #1 (items L-1 … L-7)

**Date:** 2026-07-31 · **Role:** executor (fresh instance) · **Artifact:** immutable
· **Input:** `ksum/artifacts/ksum_lean_statement_fidelity_review_20260731.md` (§5 T2, §6 T3
renderings/verdicts, §10 rollups) and `ksum/artifacts/ksum_lean_closeout_20260731.md` (what already
closed) · **Scope:** close the combinatorial/algebraic unformalized gaps that review recorded.
**No status changed anywhere. No `git` command run.**

---

## 0. PRE-ACTION REPORT

**Files read from disk, completely, before any math or edit**, in the order
`research/PRETASK_RELOAD_PROMPT.md` prescribes: that template; `DAG_PROTOCOL.md` (whole
file, §7 read closely — §7.6 check 3a is now an ERROR); `research/RESEARCH_STRUCTURE_PROTOCOL.md`;
`ksum/README.md`; `ksum/proof-dag/NODE_INDEX.md`;
`ksum/artifacts/ksum_lean_statement_fidelity_review_20260731.md` (all 817 lines);
`ksum/artifacts/ksum_lean_closeout_20260731.md`; `tools/proof_dag_check.py`; the target node
`ksum/proof-dag/nodes/KSUM.LEAN.T3.obstruction-theorems.yaml` and the nodes each item
touches (`KSUM.B4b.L2.FILT`, `.BANDMULT`, `.T4`, `.G2`, `KSUM.ROSMANIS`, `KSUM.B1`, `KSUM.B2`,
`KSUM.goal`, `KSUM.L11`, `KSUM.L12`); the manuscript sections `sec:dual-toolkit`,
`sec:dual-obstructions`, `sec:proof-search` and `prop:rosmanis`; and every Lean module touched.

- **Target node and status as read from disk:** `KSUM.LEAN.T3.obstruction-theorems` —
  **CERTIFIED\*** (`NODE_INDEX` Lean column: *"proved (unconditional) — fidelity
  PASS-WITH-CAVEATS; NARROWER 6 labels/9 clauses"*), LEAF, role `tool`, parent `KSUM.LEAN`.
  Items also touch `KSUM.LEAN.T2.rosmanis-kfloor` (CERTIFIED\*), `KSUM.B2` (OPEN),
  `KSUM.B1` (CONJECTURED), `KSUM.goal` (OPEN).
- **ROLE: executor.** This artifact is not a review and opens no completion gate.
- **Highest status this evidence could license (§2 ladder): NUMERICAL**, and only for work of my
  own authorship — a `lake build` is a run (command + log + SHA). Under rule 2 I may not write a
  completion tier on anything, and under this commission I write **no status at all**. Every new
  or changed Lean statement is appended to the delta-fidelity queue on
  `KSUM.LEAN.statement-fidelity` for an independent reviewer; I do not review my own work.
- **Gates / deliverables, one line each.** L-1 formalize `lem:factorial-filtration` and lift
  `thm:pair-tensor` to query polynomials; L-2 `lem:band-multiplication` clauses (a) and (d) plus the
  convolution reduction; L-3 `thm:block-obstruction` clauses (i) and (iii); L-4 the Maschke
  satellite ↔ augmentation dictionary for (G2); L-5 `prop:rosmanis`(1)'s orbit bijection and count;
  L-6 the `k`-indexed `DonorClaim`; L-7 the `KSUM/B1.lean` node module and the `goal` import; plus
  full green build, `#print axioms` manifest, logs, node records, views, ledger, both validators.
- **Conflicts between commission text and disk — three, reported, not silently resolved.**
  1. `RESEARCH_STRUCTURE_PROTOCOL.md` §9 lists `git diff --check` among the required closeout
     checks; the commission forbids `git`. **No `git` command of any kind was run** (the same
     recurring conflict every executor in this campaign has reported). Recorded as not performed.
  2. The commission's L-7 text says *"Wire into `KSUM.goal`-side? NO … B1 IS a child of goal…
     Add `import KSUM.B1` to `KSUM/goal.lean`"*. The disk settles it: `KSUM.goal`'s `children` are
     `[B1, B2, B3]`, so `import KSUM.B1` is required by §7.6 check 6 and was added. The
     parenthetical "NO" is read as the abandoned first thought that the sentence itself corrects.
  3. The commission's L-4 text prescribes *"using Mathlib's Maschke theorem (`MonoidAlgebra`
     complete reducibility)"*. The dictionary is proved **without** invoking
     `MonoidAlgebra.Submodule.exists_isCompl`, from the characteristic-zero Reynolds projection
     directly — which is the content Maschke packages and is strictly stronger here (Mathlib's
     theorem yields *some* complement; what is needed is *this* one). Recorded as a route
     deviation in `KsumAudit/ObstructionsTransfer.lean` and in §5 below, not as a silent choice.

Only after this report did any Lean or file edit begin.

---

## 1. RESULT TABLE

| Item | Verdict | Where it stands |
|---|---|---|
| **L-1** `lem:factorial-filtration` + pair-tensor lift | **DONE / PARTIAL** | The lemma is **PROVED, both directions**, plus the uniform orbit lift and its pushforward and `ℓ¹` identities — the whole reusable bridge (§2). The **pair-tensor-specific** lift is **RESISTED** at one named point (§2.4). |
| **L-2** `lem:band-multiplication` (a), (d), convolution | **DONE / PARTIAL** | (a) and (d) **PROVED** (§3). The convolution reduction is **RESISTED**; half of it (the orbit-size cancellation) landed under L-1 (§3.3). |
| **L-3** `thm:block-obstruction` (i), (iii) | **RESISTED (i partial, iii not started)** | The linearity half of (i) is proved; the residual is one named identity (§4). (iii) is blocked upstream (§4.2). |
| **L-4** `prop:transfer-facts` (G2) Maschke dictionary | **DONE** | `InNontrivialSatellite` ⟺ `augment`, and (G2) restated at the manuscript's own hypothesis (§5). |
| **L-5** `prop:rosmanis`(1) bijection + count | **RESISTED** | Precise resistance point in §6. Nothing was reworked in `RosmanisBarrier.lean`. |
| **L-6** `KSUM.B2.DonorClaim` `k`-uniformity | **DONE** | `L : ℕ → ℕ → ℕ → ℝ`; both compositions re-closed; witness added (§7). |
| **L-7** `KSUM/B1.lean` node module | **DONE (+ a finding)** | Module written, `Claim` proved, `import KSUM.B1` added to `goal.lean`; and the `A1 ⇒ B1` route turns out **not** to be an implication between the two Claims (§8). |
| **Build / evidence** | **DONE** | `lake build` **exit 0, 3015 jobs, zero warnings, zero errors**; **237 `#print axioms` records, 0 outside Lean's three standard axioms**; both validators exit 0. |

**Nothing was reshaped to make it compile.** Where a paper statement did not go through, the item
is reported RESISTED with the exact missing object, and no weaker statement is presented under the
paper's label.

---

## 2. L-1 — `lem:factorial-filtration`, PROVED both directions

New module: **`ksum/lean/KsumAudit/FactorialFiltration.lean`** (621 lines),
namespace `KsumAudit.Obstructions.Filtration`, imported by `KsumAudit/Obstructions.lean`.

### 2.1 The statement

For a finite alphabet `A`, a length `N`, an `S_N`-invariant signed measure `μ : A^N → ℚ` and a
degree `d`:

    factorial_filtration : AnnihilatesQueryBelow μ d ↔ FactorialMomentsVanishBelow μ d

where `AnnihilatesQueryBelow μ d` is *"`⟨μ, ∏_{l<m}[x_{ι l} = a_l]⟩ = 0` for every `m < d`, every
injection `ι : Fin m ↪ Fin N` and every word `a : Fin m → A"`, and
`FactorialMomentsVanishBelow μ d` is equation (38) verbatim, `∑_x μ(x) ∏_a (n_a(x))_{α_a} = 0` for
every `α` with `|α| < d`.

**Term of art resolved (rule 7g).** The manuscript never prints a definition of "query
polynomial"; its own proof supplies one (*"a compatible one-hot monomial on `m` distinct queried
positions"*), and that is what is formalized. The two reductions the manuscript disposes of in one
sentence — *"repeated variables at one position reduce by idempotence, and incompatible symbols
give zero"* — are discharged by the index set: a monomial is indexed by an **injection** plus a
word, so a repeated position is not expressible and a doubly-labelled position is not expressible.
`annihilates_linear_combination` proves that annihilating the monomials is the same as annihilating
every `ℚ`-linear combination of them, so restricting the definition to monomials is not a weakening.

### 2.2 The three steps, and the normalization

| Manuscript sentence | Lean |
|---|---|
| *"A compatible one-hot monomial on `m` distinct queried positions, after averaging over `S_N`, is `∏_a (n_a)_{α_a}/(N)_m` with `|α| = m`."* | `sum_hotMon` (the counting identity) and `descFactorial_mul_pair` (`(N)_m · ⟨μ, mon⟩ = ⟨μ, row⟩`) |
| *"Repeated variables … reduce by idempotence, and incompatible symbols give zero."* | the index set (see above) |
| *"Pairing an invariant measure against a polynomial is unchanged by averaging that polynomial over `S_N`."* | `pair_hotMon_const` |

**The `(N)_m` denominator is present and load-bearing** (standing failure mode 7e, dropped
normalization). It is written on the LEFT — `(N.descFactorial m : ℚ) * pair μ (hotMon ι a)
= pair μ (ffStr (wordType a))` — so the identity is unconditional, with no `m ≤ N` hypothesis and
no division; and `(N)_m` is *proved* to be the right constant, being `Fintype.card (Fin m ↪ Fin N)`
via `Fintype.card_embedding_eq`. The ⟸ direction divides by it, legitimately, because an injection
`Fin m ↪ Fin N` exists only when `m ≤ N`.

The combinatorial core is `card_valid` / `validEquiv`: the injections placing a word `a` compatibly
inside `x` split as a product over symbols,

    {ι : Fin m ↪ Fin N // ∀ l, x (ι l) = a l}  ≃  ∀ s : A, ({l // a l = s} ↪ {i // x i = s}),

giving `∏_s (n_s(x))_{α_s}` by `Fintype.card_embedding_eq`. `pair_hotMon_const` runs off
`Equiv.Perm.exists_extending_pair` (any two injections of a finite type differ by a permutation of
the codomain). The ⟹ direction additionally needs *every* `α` to be realized by a word, which is
`exists_word` (via `Σ s : A, Fin (α s) ≃ Fin |α|`), and the out-of-range case `|α| > N`, where the
row vanishes pointwise (`ffStr_eq_zero_of_lt`).

### 2.3 The uniform orbit lift — the second half of the bridge

The fidelity review recorded three things as unformalized in `ObstructionsPairTensor.lean`: the
uniform lift of an occupancy weight to its `S_N` string orbit, `S_N`-invariance on `Z_q^N`, and the
pushforward `ℓ¹` identity. All three are now proved, in general form:

* `occ_comp_perm` / `SNInvariant_of_occ` — every function of the occupancy vector is
  `S_N`-invariant, which is how the manuscript's invariant measures are built;
* `uniformLift ν x = ν (occ x) / |{y : occ y = occ x}|`;
* `sum_uniformLift_comp` — `∑_x uniformLift ν x · g(occ x) = ∑_{n achievable} ν n · g n`: the orbit
  sizes cancel exactly (this **is** the "hypergeometric block split cancels the block multinomial
  orbit sizes" step, isolated from any block structure and proved without ever computing a
  multinomial coefficient);
* `l1_uniformLift` — `∑_x |uniformLift ν x| = ∑_n |ν n|`, i.e. a unit-`ℓ¹` occupancy measure lifts
  to a unit-`ℓ¹` measure on `A^N`;
* `annihilates_query_of_occ_moments` — assembled: an occupancy-level measure whose
  falling-factorial moments below `d` vanish lifts to an `S_N`-invariant measure on `A^N` that
  annihilates every QUERY polynomial of degree `< d`, with the same `ℓ¹` norm.

### 2.4 What RESISTED: the pair-tensor-specific lift

Turning `thm:pair-tensor` itself into a query-degree statement over `Z_q^N` needs, on top of §2.3,
one further object that is **not** on disk and that I did not produce:

> **The residual, stated exactly.** For odd `q = 2r+1` and `t ∈ Z_q`, an orientation of the value
> symmetry: a bijection `Unit ⊕ (Fin r ⊕ Fin r) ≃ Z_q` sending `inl` to the unique fixed point
> `v = t/2` and `(c, ±)` to `v ± (c+1)`, together with the transport of `∏_{a ∈ Z_q}(n_a)_{α_a}`
> across it into `(n_v)_{α_v} · ∏_c (n_{a_c})_{α_{a_c}}(n_{b_c})_{α_{b_c}}`; and then the
> pushforward of the LABELED slice space `(slice, local states)` onto `Z_q`-occupancy vectors,
> which is **not injective** — for even pair totals `s` the two interior local states `(s/2, s−s/2)`
> and `(s−s/2, s/2)` collide — so the `ℓ¹` identity on the occupancy side needs the (true, but
> unproved here) observation that the colliding states carry the same sign, hence no cancellation.

Injectivity of the orientation is a `ZMod.val` computation (`ZMod.neg_val` on `[1..r]` versus
`[r+1..2r]`); the collision analysis is a four-case argument on `occLocal`. Neither is deep; both
are real work that did not fit this batch. Until they land, `thm:pair-tensor` keeps its NARROWER
verdict, but the **reason** has moved: it is no longer "the filtration bridge is unformalized" (it
is now formalized) but "the pair-indexing of `Z_q` and the labeled-to-occupancy pushforward are
unformalized".

### 2.5 Non-vacuity

Witness at `N = 2`, `A = Fin 2`: `μ = +1` on the two constant strings, `−1` on the two mixed
strings, written as a function of the occupancy vector so that `S_2`-invariance is by construction.
`wμ_moments` proves the order-`< 2` moments vanish; the ⟸ direction of the theorem then delivers
`AnnihilatesQueryBelow wμ 2`; and the order-`2` moment `∑_x μ(x)(n_0(x))_2 = 2 ≠ 0` shows the band
is **exactly** `2`, so nothing above is annihilating everything.

---

## 3. L-2 — `lem:band-multiplication` clauses (a) and (d)

In `KsumAudit/ObstructionsBandMult.lean`.

### 3.1 Clause (a), `ν ≠ 0` — the paper's integral-domain argument, formalized

The paper: *"Convolution is nonzero because the finite generating polynomials of the nonzero `μ_j`
have nonzero product in an integral domain."* Formalized literally:

* `push occ μ n = ∑_{i : occ i = n} μ i` — the **occupancy pushforward**, which is what "`ν`" means
  (the index-level product measure is trivially nonzero; the content is that no cancellation
  collapses the pushforward, and the previous module said nothing about it);
* `genPoly occ μ = ∑_i μ_i ∏_a X_a^{occ_i(a)} ∈ MvPolynomial A ℚ`;
* `coeff_genPoly` — the coefficients of `genPoly` **are** `push`;
* `genPoly_mul` — the generating polynomial of a convolution is the product of the generating
  polynomials;
* `push_ne_zero_iff` — `(∃ n, push ≠ 0) ↔ genPoly ≠ 0`;
* **`push_conv_ne_zero`** — clause (a): convolving two measures with nonzero pushforward gives a
  nonzero pushforward, by `mul_ne_zero` in the integral domain `MvPolynomial A ℚ`. Hence the `ℓ¹`
  norm is positive and clause (c)'s normalization is legal — which is the downstream weight the
  review flagged ("the clause with the most downstream weight").

Non-vacuity: the module's own one-block witness (`wOcc`/`wMu`, band exactly 1) has nonzero
pushforward, so its self-convolution does too, at the band `1 + 1 = 2` that `band_add` supplies.

### 3.2 Clause (d), common value-group invariance

`IsValueInvariant occ μ σ` says the alphabet relabelling `σ` is realized by a relabelling of the
carrier: `∃ e : I ≃ I, (∀ i, μ (e i) = μ i) ∧ (∀ i a, occ (e i) a = occ i (σ a))`.

* **`isValueInvariant_conv`** — clause (d): the convolution of two `σ`-invariant blocks is
  `σ`-invariant (carrier map `e₁ × e₂`);
* `isValueInvariant_smul` — invariance survives clause (c)'s rescaling, so it survives the `ℓ¹`
  normalization, which is what the paper's sentence is about ("so is the *normalized* average");
* `moment_of_isValueInvariant` — invariance is not a formal decoration: it transports to the
  falling-factorial moments, `M_μ(α ∘ σ) = M_μ(α)`.

### 3.3 What RESISTED: the convolution reduction

The paper *derives* `ν = μ₁ * ⋯ * μ_m` from "form the product of the uniformly orbit-lifted block
measures, average over `S_N`, take the occupancy pushforward"; the Lean still *defines* `ν` to be
the convolution. Half of the derivation landed under L-1 — `sum_uniformLift_comp` is exactly the
orbit-size cancellation, proved without any multinomial formula, and the `S_N`-average step is a
no-op for the pushforward because occupancy is already `S_N`-invariant (`occ_comp_perm`).

> **The residual, stated exactly.** The block splitting `A^{N₁+N₂} ≃ A^{N₁} × A^{N₂}` (as an
> `Equiv`), occupancy additivity across it (`occ (append y z) = occ y + occ z`), and the resulting
> identity `push (uniformLift ν₁ ⊗ uniformLift ν₂) = ν₁ * ν₂`. No multinomial coefficient is needed
> for any of it — that is the point of §2.3 — but the `Fin.append` bookkeeping is a genuine piece
> of work that did not fit this batch.

---

## 4. L-3 — `thm:block-obstruction` clauses (i) and (iii): RESISTED

### 4.1 Clause (i): the linearity half proved, one identity missing

The review's finding: `block_obstruction_band` proves clause (i) only for query rows that are
PRODUCTS `∏_j row_j`, and *"a general row is a linear combination of such products (Vandermonde,
which this very development proves as `descFactorial_add`), so the gap is closable by linearity —
but it is not closed in Lean"*.

Added: **`block_obstruction_band_combination`** in `KsumAudit/ObstructionsBlock.lean` — `ζ`
annihilates every `ℚ`-linear combination of product rows whose per-block orders satisfy the same
hypotheses. That is the linearity half, and it makes the remaining gap a single named identity:

> **The residual, stated exactly.** An `m`-fold multivariate Vandermonde: for occupancy vectors
> `n_1, …, n_m : A → ℕ` and `α : A → ℕ`,
> `∏_a ((∑_j n_j a).descFactorial (α a)) = ∑_{α = α^{(1)}+⋯+α^{(m)}} (∏_a multinomial) ∏_j ∏_a ((n_j a).descFactorial (α^{(j)} a))`,
> indexed by a `Finset` of splittings. `BandMult.descFactorial_add` is the `m = 2` case; the
> `m`-block generalization (and its splitting index set) is not on disk. With it,
> `block_obstruction_band_combination` closes clause (i) immediately, because every splitting has
> `∑_j |α^{(j)}| = |α| < dD`.

Why it did not fit: the abstract `ObstructionsBlock` setting has no alphabet or occupancy structure
at all (`X j` is an arbitrary `Fintype`), so closing clause (i) *at the paper's own quantifier*
means first instantiating the block setting with `X j = A^{N_j}` and re-deriving `zeta` there — a
re-statement of Part A, not an addition to it. That is a design decision about the module, and per
the commission's "do NOT reshape paper statements to make them compile" it is a lead call, not an
executor's.

### 4.2 Clause (iii): blocked upstream, not attempted

The paper's clause is *"for a logarithmic inner from `thm:tilted-log-band` containing at least five
complementary pairs, `ρ_j ≤ 4/5`"*. Deriving `ρ_j ≤ 4/5` from the tilted inner requires the tilted
inner to exist in Lean — and `KsumAudit/ObstructionsTiltedBand.lean` states, in its own header,
that **no theorem in that file is the LaTeX theorem**: the divided-difference construction on
`{0, 1, 5, …, 5^{m−1}}`, the ratio computation (44), and the activity→falling-factorial transfer
are all absent. Until `thm:tilted-log-band` is formalized there is no object from which the two
weight ratios `w_{K=1} ≥ (5/4) w_{K=0}` and `w_{K=5} ≥ (1/4) w_{K=0}` — the hypotheses of the
existing `rho_le_four_fifths` — can be derived. **Reporting this as the resistance point rather
than manufacturing a weaker "derivation" is the honest outcome**: clause (iii) is not one gap but
two, and the upstream one is `thm:tilted-log-band` itself.

---

## 5. L-4 — the Maschke dictionary for (G2): DONE

In `KsumAudit/ObstructionsTransfer.lean`, section `G2`.

The review graded (G2) NARROWER because *"the paper's hypothesis is `v` lies in a nontrivial
`H`-satellite, defined at (52) as a summand with nontrivial `U_λ`; the Lean's is `v ∈ augment ρ H`;
these coincide by Maschke in characteristic zero, which is not formalized"*.

`InNontrivialSatellite ρ H v` renders (52)'s hypothesis without reference to a decomposition: `v`
sits in an `H`-stable subspace with **no nonzero `H`-invariant vector** — which is exactly "all of
whose isotypic components are nontrivial", since the trivial isotypic component of a summand is its
invariant subspace. Then:

* `reynolds_of_invariant` — `R_H` is the identity on invariants;
* `reynolds_mem_invariant` — `R_H v` is `H`-invariant, for multiplicatively closed `H`;
* **`inNontrivialSatellite_iff_mem_augment`** — the dictionary, both directions (⟸ takes
  `W = ker R_H`; ⟹ observes `R_H v ∈ W` is invariant, so `W`'s hypothesis kills it);
* **`transfer_G2_of_satellite`** — (G2) restated at the manuscript's own hypothesis, with nothing
  granted.

**Route deviation, recorded (conflict 3 of §0).** Mathlib's `MonoidAlgebra.Submodule.exists_isCompl`
is not invoked. The characteristic-zero content Maschke packages is *"the Reynolds average is an
`H`-equivariant idempotent onto the `H`-invariants with kernel the augmentation submodule"*, and
that is what the three lemmas above prove; routing through Mathlib would require transporting `ρ`
to a `MonoidAlgebra ℚ H`-module structure only to obtain a *weaker* conclusion (that *some*
`H`-stable complement exists, not that it is this one). Nothing is assumed that Maschke would have
supplied.

Non-vacuity: the module's existing sign-representation witness now also certifies that the NONZERO
vector `−2` lies in a nontrivial satellite of `S₂` on `ℚ`, so `transfer_G2_of_satellite` is not
about an empty class.

---

## 6. L-5 — `prop:rosmanis`(1) bijection and count: RESISTED

Nothing in `KsumAudit/RosmanisBarrier.lean` was reworked (the commission's instruction: build on
the orbit-proper `≥ 2` core, do not rework it). The bijection and the count did not land.

> **The resistance point, stated exactly.** The claim is a classification of the
> `S_N × C(σ)`-ORBITS on `D₀`, and the Lean development has no orbit type: `RosmanisBarrier.lean`
> works with the action and with a separating invariant (the number of distinct values), which is
> exactly enough for "at least two orbits" and gives no handle on "exactly these orbits". Closing
> it needs three objects, none on disk:
> 1. the value group `C(σ)` as a group acting on `G`, with its structure `(C₂ ≀ S_m) × S_τ` — which
>    tier T2 itself declares NOT FORMALIZED, and which is what makes "only the number `f` of
>    occupied fixed points matters" and "only the multiset of cycle occupation multiplicities
>    matters" true;
> 2. the quotient `D₀ / (S_N × C(σ))` as a type with decidable equality, or an explicit complete
>    invariant map `D₀ → Σ f, Nat.Partition (N − f)` proved injective-on-orbits and surjective;
> 3. the enumeration `|{λ ⊢ n : λ has ≤ m parts}| = p_{≤m}(n)` — Mathlib's `Nat.Partition` gives
>    the type and its `Fintype` instance, but not the "at most `m` parts" refinement as a counting
>    function, so `∑_f p_{≤m}(N−f)` has no Mathlib name to be equal to.
>
> Item 1 is a prerequisite the fidelity review already lists as an open T2 caveat; formalizing it
> is a work package on its own scale, not a step inside this batch. Attempting 2 and 3 without 1
> would have produced a statement about a *different* group and is exactly the "quantifier drift"
> failure mode this commission's standing list names.

`KSUM.ROSMANIS`'s `lean` block note is therefore unchanged in substance; a dated work record
naming this resistance point is appended to the node.

---

## 7. L-6 — the `k`-indexed donor bound: DONE

`KSUM/B2.lean`. `DonorClaim` used to type the donor bound as `L : ℕ → ℕ → ℝ`, with `k` bound by the
`∀` but **absent from the bound's arguments** — so it demanded ONE bound uniform in `k`, which is
strictly stronger than `KSUM.k3.donor` (a `k`-collision bound is a bound *for each fixed `k`*, and
the manuscript's whole `k ≥ 3` discussion is `k`-indexed). The review graded it *"a real narrowing
of `B2.Claim`"* (§10, KSUM-layer caveat (2)).

Now `L : ℕ → ℕ → ℕ → ℝ` with `L k n R ≤ M.Q (Coll k n R)`, and `Claim` concludes
`L D.k D.n D.R / 2 ≤ M.Q (kSum …)`. `composition` and `composition_with_donor` both re-close; the
whole cost is threading one extra argument.

**Non-vacuity, chosen to exercise the new argument.** `demoDonor : DonorClaim demoModel
(fun k _ _ => -(k : ℝ))` — a family that genuinely varies with `k`, so the retype is not merely
typographic — and the transported conclusion at `KSUM.Support.demoEmbed` (`k = 3`, `q = 325`).
`KSUM.B2.yaml`'s frozen `## Claim` text is unchanged, so its `claim_hash` is unchanged; it was
re-verified under `tools/proof_dag_check.py`'s own `frozen_claim_hash` and `lean.synced` moved to
2026-07-31.

---

## 8. L-7 — `KSUM/B1.lean`, and a finding about the `A1 → B1` edge

New module `ksum/lean/KSUM/B1.lean` (node id = module name, §7.3), rendering
B1's Claim as frozen on 2026-07-30:

    Claim M : ∀ k ≥ 3, ∃ C > 0, ∀ N q K, K ≥ 2 → (k²−2)K + 2k−1 ≤ q → k+3 ≤ N → ∀ t,
      ∃ n m, 2 ≤ n ∧ k−2 ≤ m ≤ k−1 ∧ N = 2n+m ∧ Q(Claw_{n→K}) ≤ C · Q(kSum_{Z_q,t,N})

`Ω(·)` is made explicit with the constant OUTSIDE the quantifiers over `N, q, K, t` (the strong
reading), `holds` delivers the absolute `C = 4`, and the module carries a PROSE ↔ `Claim` DIFF
section. `M.abi`/`M.tani` are **not** used — B1's Claim is the reduction, not the numeric floor —
so the module is unconditional in the donor; its only interface dependence is `restrict`,
`relabel` and the unstated `freeze` (F1).

`composition_via_A1_inputs` is the route proof, from `A1a ∧ A1b ∧ A1c` — the identical hypothesis
set as `KSUM.A1.composition` (gate G-R3) — via the four steps A1 itself runs, minus its exponent
arithmetic. `import KSUM.B1` was added to `KSUM/goal.lean`, so §7.6 check-6 import-graph agreement
on `KSUM.goal` improves from 1 of 3 children to 2 of 3 (`KSUM.B3` still has no module — a declared
deviation, now stated in `goal.lean` rather than left implicit). `KSUM.L11` and `KSUM.L12`, B1's two
dead routes, received the `lean: none` records §7.4 requires ("silence is invalid"), so the OR-route
check has a justification for every child.

> **FINDING (new; queued for the delta-fidelity review).** `KSUM.B1`'s `composition` block records
> the route as *"B1's new Claim is what A1 delivers"*. That is true of **A1's PROOF** and false of
> **A1's CLAIM**: `KSUM.A1.Claim = KSUM.A1d.Claim` is a NUMERIC FLOOR (`A√N q^{1/6} ≤ Q(kSum)` in a
> window), and a floor on `Q(kSum)` says nothing about `Q(Claw_{n→K})`, so it cannot re-derive the
> reduction that produced it. `KSUM.A1.Claim M → Claim M` is therefore **not provable**, and the
> §7.4-mandated `composition_via_A1` is declared with its hypothesis explicitly **not consumed**,
> and with the mismatch written into the module header rather than hidden. The drawn edge
> `A1 → B1` is an edge between BRANCHES (shared machinery `A1a/A1b/A1c`, two different outputs),
> not between the two nodes' Claims. Repairing it is a graph decision — re-type the edge, or
> restate one of the two Claims — and is a lead call.

Non-vacuity: two witnesses at the smallest legal modulus `q₀(3) = 19`, `K = 2`, exercising **both**
core-size branches — `N = 10` gives `m = 2 = k−1` (the parked coordinate of `lem:core-odd`) and
`N = 11` gives `m = 1 = k−2` (the even branch of `prop:core-even`).

---

## 9. NEW-DECLARATION CENSUS

| Module | New declarations | Kind |
|---|---|---|
| `KsumAudit/FactorialFiltration.lean` (new file) | `occ`, `wordType`, `hotMon`, `pair`, `ffStr`, `SNInvariant`, `AnnihilatesQueryBelow`, `FactorialMomentsVanishBelow`, `occImage`, `occFiber`, `uniformLift`, `validEquiv` | 12 `def` |
| ″ | `occ_comp_perm`, `SNInvariant_of_occ`, `occ_total`, `rowOrder_wordType`, `annihilates_linear_combination`, `card_valid`, `sum_hotMon`, `pair_hotMon_const`, `descFactorial_mul_pair`, `exists_word`, `ffStr_eq_zero_of_lt`, **`factorial_filtration`**, `occFiber_card_pos`, `uniformLift_SNInvariant`, `sum_uniformLift_comp`, `l1_uniformLift`, `annihilates_query_of_occ_moments` | 17 `theorem` |
| ″ (private, witness) | `wf`, `wμ`, `wμ_inv`, `sum_two`, `wμ_row`, `occ_vals`, `wμ_vals`, `wμ_moments` | 8 |
| ″ (witnesses) | 2 `example` | 2 |
| `KsumAudit/ObstructionsBandMult.lean` | `push`, `genPoly`, `IsValueInvariant` | 3 `def` |
| ″ | `equivFunOnFinite_symm_add` (private), `coeff_genPoly`, `genPoly_mul`, `push_ne_zero_iff`, **`push_conv_ne_zero`**, **`isValueInvariant_conv`**, `isValueInvariant_smul`, `moment_of_isValueInvariant`, `wPush_ne_zero` (private) | 9 |
| ″ (witnesses) | 2 `example` | 2 |
| `KsumAudit/ObstructionsBlock.lean` | `block_obstruction_band_combination` | 1 `theorem` |
| `KsumAudit/ObstructionsTransfer.lean` | `InNontrivialSatellite` | 1 `def` |
| ″ | `reynolds_of_invariant`, `reynolds_mem_invariant`, **`inNontrivialSatellite_iff_mem_augment`**, **`transfer_G2_of_satellite`** | 4 |
| ″ (witnesses) | 2 `example` | 2 |
| `KSUM/B1.lean` (new file) | `Claim`; `composition_via_A1_inputs`, `holds`, `composition_via_A1` | 1 `def` + 3 `theorem` |
| ″ (witnesses) | 2 `example` | 2 |
| `KSUM/B2.lean` | `demoQ_nonneg` (private), `demoDonor` | 2 |
| ″ (witness) | 1 `example` | 1 |

`#print axioms` lines added: 30 (5 `KSUM.B1`/`KSUM.B2` in `KSUM/Trust.lean`, 6 in
`FactorialFiltration`, 9 in `BandMult`, 1 in `Block`, 5 in `Transfer`, 4 in `B1`).
Manifest total: **237 records** (193 before), **0 outside `propext, Classical.choice, Quot.sound`**.

## 10. WITNESS LIST (every new culminating theorem has one)

| Theorem | Witness | Parameters |
|---|---|---|
| `factorial_filtration` | `AnnihilatesQueryBelow wμ 2` via the ⟸ direction; and the order-2 moment `= 2 ≠ 0` | `A = Fin 2`, `N = 2`, band exactly `2` |
| `annihilates_query_of_occ_moments` | shares the `wμ` witness (`wμ` **is** a uniform lift: it is a function of `occ`) | ″ |
| `push_conv_ne_zero` | `∃ n, push (conv) n ≠ 0` from the module's own one-block witness | `A = Fin 1`, band `1+1 = 2` |
| `isValueInvariant_conv` | invariance of the self-convolution under `1 : Equiv.Perm (Fin 1)` | ″ |
| `block_obstruction_band_combination` | inherits Part A's two-block witness (`Fin 2` states per block) | `m = 2` |
| `inNontrivialSatellite_iff_mem_augment` | `−2 ≠ 0` lies in a nontrivial satellite of the sign rep of `S₂` on `ℚ` | `G = Equiv.Perm (Fin 2)` |
| `transfer_G2_of_satellite` | `R_G(−2) = 0` for that vector | ″ |
| `KSUM.B1.holds` | two instances at `k = 3`, `K = 2`, `q = 19 = q₀(3)`: `N = 10` (`m = k−1`, parked) and `N = 11` (`m = k−2`, even) | both core-size branches |
| `KSUM.B2.composition` (re-closed) | `demoDonor`, a `k`-DEPENDENT donor family, at `demoEmbed` (`k = 3`, `q = 325`) | exercises the new `k` argument |

---

## 11. BUILD, EVIDENCE, RECORDS

**Build.** `cd ksum/proof-dag/lean && lake build` → `Build completed successfully (3015
jobs).`, **true exit status 0**, **zero** warnings, **zero** errors, **zero** `declaration uses
'sorry'`. (3011 jobs before; +4 = the new `KsumAudit.FactorialFiltration` and `KSUM.B1` modules and
their two `.ilean`/`.c` targets.)

**Holes.** Grep over all 36  files outside : `axiom` 0, `sorry` 0 (outside backticked
prose), `native_decide` 0, `implemented_by` 0, `unsafe`/`opaque`/`admit`/`sorryAx` 0.

**Axioms.** 237 `#print axioms` records, line-unwrapped from this run's own transcript:
`[propext, Classical.choice, Quot.sound]` ×211, `[propext, Quot.sound]` ×15, `[propext]` ×4,
`[Quot.sound]` ×1, *"does not depend on any axioms"* ×6. **Outside the three standard axioms: 0.**
L-4 uses no Mathlib Maschke theorem, so the axiom profile is unchanged in kind.

**Evidence** — `ksum/artifacts/logs_ksum_lean_gapclose1_20260731/`: `build.log` (command + toolchain +
full transcript + `BUILD_RESULT: exit=0`), `print_axioms.txt`, `SHA256SUMS.txt` (LF/RAW dual rows,
the convention of the T2, repair-batch and closeout ledgers).

**Validators.** `python tools/proof_dag_check.py --problem ksum` → **exit 0**;
`--problem all` → exit 0; `python tools/literature_check.py` → **exit 0**. **Frozen-Claim hash
drift: 0** (now an ERROR, per closeout item C-3). `git diff --check` **not run** (commission forbids
`git`; conflict recorded in §0).

**Records written** (dated 2026-07-31, all citing this artifact and the evidence directory; **no
`status`, `status_source` or `caveat` field touched on any node**):

| Node | Entry |
|---|---|
| `KSUM.B4b.L2.FILT` | `lem:factorial-filtration` formalized both directions; `lean` block none → `proved`; the lift bridge |
| `KSUM.B4b.L2.BANDMULT` | clauses (a) and (d) proved; the convolution residual named |
| `KSUM.B4b.L2.G2` | the satellite ↔ augmentation dictionary proved; (G2) at the paper's hypothesis |
| `KSUM.B4b.L2.T4` | clause (i)'s linearity half; the `m`-fold Vandermonde residual named; clause (iii) blocked upstream |
| `KSUM.B4b.L2.M1` | the reason for `thm:pair-tensor`'s NARROWER verdict has moved (§2.4) |
| `KSUM.ROSMANIS` | L-5 resistance point (§6) |
| `KSUM.B1` | module written, Claim proved, the `A1 ⇒ B1` finding |
| `KSUM.B2` | `k`-indexed `DonorClaim`; `lean.synced` → 2026-07-31 |
| `KSUM.goal` | `import KSUM.B1` added; import-graph agreement 1/3 → 2/3 |
| `KSUM.L11`, `KSUM.L12` | `lean: none` records added (§7.4 "silence is invalid") |
| `KSUM.LEAN.T3.obstruction-theorems` | what this batch closed and what it did not, per clause |
| `KSUM.LEAN.T2.rosmanis-kfloor` | L-5 not closed; resistance point cited |
| `KSUM.LEAN.statement-fidelity` | **delta-fidelity queue entry** for every new/changed statement |

**Views and ledger.** `ksum/notes/KSUM_PROOF_DAG.md` gains a "Most recent change" block
(the previous one demoted, none deleted). The graph did **not** change: no node added or removed, no
edge re-typed, no status moved — so the Mermaid diagram and nested outline needed no edit.
`NODE_INDEX.md`'s Lean column was updated for the rows this batch touched
(`KSUM.B1`, `KSUM.B2`, `KSUM.B4b.L2.FILT`, `KSUM.goal`).
`ksum/notes/ksum_lean_campaign_state_20260730.md` records the batch.

---

## 12. TWO ITEMS FOR THE LEAD (not executed here — both are status-adjacent writes)

1. `KSUM.B4b.L2.FILT`'s frontmatter `caveat` still ends *"not mechanized — this is the gap behind
   `thm:pair-tensor`'s NARROWER Lean verdict"*. The first clause is now false and the second is now
   imprecise (the residual moved — see §2.4). Trimming a `caveat` is a status write.
2. The `A1 → B1` edge (§8). Either re-type it, or restate one of the two Claims so that the drawn
   edge is an implication between them. Both are graph decisions.

---

`GAPCLOSE1 RESULT: L-1 done (filtration both directions + lift bridge) / resisted: pair-tensor Z_q pair-orientation + labeled-to-occupancy pushforward | L-2 done (a),(d) / resisted: convolution reduction at the A^{N1+N2} block splitting | L-3 resisted: (i) at the m-fold multivariate Vandermonde (linearity half proved), (iii) at thm:tilted-log-band being unformalized | L-4 done | L-5 resisted: C(sigma) as a group with its (C2 wr Sm) x Stau structure is unformalized (a declared T2 caveat), and p_{<=m} has no Mathlib counting function | L-6 done | L-7 done + finding: A1.Claim does NOT imply B1.Claim | build exit=0 / 3015 jobs / 0 warnings | axioms 237/237 clean | hash drift 0 | validators 0, 0`
