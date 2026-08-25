# k-Sum Lean audit — DELTA statement-fidelity review (node `KSUM.LEAN.statement-fidelity`)

**Date:** 2026-08-01 · **Reviewer:** fresh Opus 5 instance, independent · **Artifact:** immutable
· **Scope:** the four change sets that landed after the 2026-07-31 consolidated review — closeout
batch, manuscript-repair batch (paper v5.2), gap-closure batch 1, gap-closure batch 2 — against
`ksum/paper/ksum_small_alphabet.tex` and the on-disk Lean development at
`ksum/lean/`.

---

## 0. PRE-ACTION REPORT

**Files read from disk, completely, before any math or verdict**, in the order prescribed by
`research/PRETASK_RELOAD_PROMPT.md`: that template; `DAG_PROTOCOL.md` (whole file, §1–§7
including all of §7.10); `ksum/README.md`; `ksum/proof-dag/NODE_INDEX.md` (Lean
rows); the target node `ksum/proof-dag/nodes/KSUM.LEAN.statement-fidelity.yaml`; its parent
`KSUM.LEAN.yaml`; the three tier nodes `KSUM.LEAN.T{1,2,3}.*`; the prior review
`ksum/artifacts/ksum_lean_statement_fidelity_review_20260731.md` **in full (all 817 lines)**; and the
campaign ledger `ksum/notes/ksum_lean_campaign_state_20260730.md`.

- **Target node and status as read from disk:** `KSUM.LEAN.statement-fidelity` — **CERTIFIED\***
  (`status_source`: the 2026-07-31 consolidated review; single review ⇒ starred), LEAF, role `tool`,
  parent `KSUM.LEAN` (**CONJECTURED**, capped by its own census-table composition obligation), no
  children. Its **Open obligations** carry two explicit DELTA-FIDELITY QUEUES (batch 1, eight items;
  batch 2, eight items) — this review answers both.
- **ROLE: reviewer. Independence statement.** I did not author any part of this Lean development,
  any node file, the manuscript, the census table, or any prior artifact in this campaign. I was
  given **no desired outcome**; the commission is symmetric between confirming and rejecting
  verdicts. I have written no Lean, edited no node, and run no `git` command. My only write is this
  artifact.
- **Highest status my evidence could license (§2 ladder):** a *second* completed independent review
  on `KSUM.LEAN.statement-fidelity` (raising it from CERTIFIED\* toward PROVED is an independent
  checker's write, not mine to make here), and — via DF-9 — the evidence the **lead** needs to move
  `KSUM.LEAN`'s composition off CONJECTURED. **I write no status.**
- **Gates / deliverables (one line each).** DF-1 reproduce `lake build`, true exit + jobs; DF-2
  hole/axiom census + `#print axioms` coverage; DF-3 per-statement F/N/W/D on every new or changed
  statement, 7c order enforced; DF-4 re-grade every prior verdict whose LaTeX side moved in v5.2,
  plus M-10 overclaim check; DF-5 vacuity of the new witnesses; DF-6 value-vs-formula for JointLP +
  F-LP-1 reproduction; DF-7 honesty of README/Trust/nodes/ledger after four batches; DF-8 residual
  audit; DF-9 census verification row by row.
- **Conflicts between commission text and disk:** **two, reported not resolved.**
  1. `RESEARCH_STRUCTURE_PROTOCOL.md` §9 lists `git diff --check` among required closeout checks;
     the commission forbids `git`. **No `git` command was run** — the same standing conflict every
     executor and the prior reviewer reported.
  2. The commission says the census expects "283/283 at the three standard axioms — verify the
     count yourself". Disk agrees on 283 *printed lines* but they carry **268 distinct names**
     (15 names are printed both in their owning module and in `KSUM/Trust.lean`). Both statements
     are true of different objects; recorded, and used precisely in §2 below.

**Method note (7c, anchoring ban).** For every statement ruled on below I read the Lean source and
wrote the English rendering (§3.A worksheets W-1 … W-11) **before opening the LaTeX**; the LaTeX was
opened only at §3.B; the executors' batch reports and the census table were read **last**, after my
verdicts were fixed. Two coincidences with the executors' wording are disclosed at §3.C. One
coincidence of a different kind is disclosed up front: **`sandwichModel` is the model the PRIOR
review sketched in its §7.3**, so its existence is not independent invention — I verify it, I do not
claim to have found it.

---

## VERDICT TABLE (up front)

| Duty | Result |
|---|---|
| **DF-1** build | `lake build` **exit 0**, **`Build completed successfully (3017 jobs)`**, zero warnings/errors/`sorry` |
| **DF-2** census | **0** `axiom` / `sorry` / `native_decide` / `implemented_by` / `unsafe` / `opaque` in declaration position across 37 sources; **283 printed lines, 268 distinct names, 268/268 at exactly `propext, Classical.choice, Quot.sound`** |
| **DF-3** new statements | **F 21 / N 7 / W 1 / D 0**, + 1 declared NOT-FORMALIZED, + 2 infra/witness (32 rows) |
| **DF-4** paper-delta re-grades | 8 re-grades; **4 prior caveats DISCHARGED** (F1, F2, F6/F7, F-T9), 1 prior **WIDER → FAITHFUL**, 2 NARROWER unchanged |
| **M-10** | **HONEST — no overclaim.** One sentence now UNDER-states batch-2 coverage (the "(51) enters as a hypothesis" clause) |
| **DF-5** vacuity | **PASS** on all four families; the `r ≥ 1` witnesses carry an explicit anti-degeneracy lemma |
| **DF-6** JointLP | **VERIFIED THREE INDEPENDENT WAYS** (certificate re-check, exact re-solve without the duals, data reconstruction from the paper's recipe). One overclaim found on what the six *decide* |
| **F-LP-1** | **REPRODUCED** independently (sympy 1.13.1, fresh process) |
| **DF-7** honesty | **FAIL on record-accuracy** — 7 defects; 6 conservative, **1 (D-5) over-states axiom-census coverage** |
| **DF-8** residuals | **ALL NAMED**, no silent drops (one is actively contradicted by the census — see C-1) |
| **DF-9** census | **CORRECTIONS** — 4 substantive (C-1 … C-4) + 4 minor (m-1 … m-4). Scope-identity verdict **not justified as written**; justified after C-2 + C-4 |
| **B1 route fix** | **FAITHFUL** — and the propagation it induces is conservative (proof in §9) |

---

## 1. DF-1 — BUILD REPRODUCTION

Command, run by me from `ksum/lean/`:

```
lake build
```

- **True exit status: `0`** (captured separately as `EXIT_STATUS=0`, not inferred from the last line).
- **Final line: `Build completed successfully (3017 jobs).`** — matches the batch-2 record exactly
  (3011 → 3015 after batch 1 → 3017 after batch 2).
- Grep over the full transcript for `^warning|^error|declaration uses 'sorry'|sorryAx` returns
  **nothing**.
- Toolchain `leanprover/lean4:v4.31.0`; Mathlib required at `v4.31.0`; `.lake/packages` is a
  junction to the machine-local prebuilt cache, so the two project libraries are the only things
  elaborated here.

---

## 2. DF-2 — AXIOM / HOLE CENSUS

### 2.1 Grep census (37 `.lean` files outside `.lake/`; was 34 before the delta)

New files: `KsumAudit/FactorialFiltration.lean`, `KsumAudit/JointLP.lean`, `KSUM/B1.lean`.

| pattern | declaration-position hits | comment/docstring hits |
|---|---|---|
| `^\s*axiom\s+` | **0** | — |
| `sorry` | **0** | 28, all of the form ``No `sorry`.`` |
| `native_decide` | **0** | 8 |
| `implemented_by` | **0** | 2 |
| `unsafe` / `opaque` / `partial` / `sorryAx` / `admit` | **0** | 2 (the English word "admit") |
| `set_option` | 11 | 10 × `linter.unusedSectionVars false`, 1 × `maxHeartbeats 2000000` |

The single `maxHeartbeats` still sits on `KsumAudit.KFloor.core_reduction_at`; a resource bound, not
a soundness escape. **No hole of any kind exists in this development.**

### 2.2 `#print axioms` — I counted from MY OWN build log, not from the reports

- **283 `#print axioms` directives** in the sources; **283 printed lines** in my transcript;
  **268 distinct declaration names**.
- Axiom sets observed: `[propext, Classical.choice, Quot.sound]` ×235, `[propext, Quot.sound]` ×15,
  `[propext]` ×4, `[Quot.sound]` ×1, *"does not depend on any axioms"* ×6.
  **Nothing outside Lean's three standard axioms. 283/283 lines, 268/268 names, clean.**
- Every printed short name resolves to a real source declaration (checked mechanically against a
  comment-stripped parse of all 37 files): **0 unresolved**.

### 2.3 Source-side denominators — and a defect

With block comments and line comments stripped, the sources hold:

| kind | count |
|---|---|
| `theorem` | 294 |
| `lemma` | 107 |
| `def` | 156 |
| `structure` | 6 |
| `instance` | 5 |
| `abbrev` | 1 |
| **named total** | **569** |
| `example` (witnesses) | **127** |

So coverage is **268 distinct printed / 401 `theorem`+`lemma`** — about **133 unprinted**, each a
helper consumed by a printed result (spot-checked: `equivFunOnFinite_symm_add`, `sq_pow_comm`,
`erase0/1/2`, `wμ_row`, `occ_vals`, the `hcard`-style privates). The census is therefore **sound**.
But `lean/README.md` states the denominators as *"276 `theorem`/`lemma`s (377 declarations, plus 96
`example` witnesses)… the ~80 unprinted ones are helper lemmas"* — **stale, and the stale form reads
as full coverage** (283 printed > 276 theorem/lemmas). Recorded as honesty defect **D-5**, §7. This
is the one defect in the delta that errs toward over-stating rather than under-stating.

**VERDICT (DF-2): CENSUS CLEAN, denominators stale.**

---

## 3. DF-3 — FIDELITY OF NEW / CHANGED STATEMENTS

### 3.A 7c worksheets — English renderings written from the Lean source ALONE

> These were written before the `.tex` was opened. They are reproduced verbatim from my working
> notes so the anchoring ban is auditable.

**W-1 `factorial_filtration`** *(`KsumAudit/FactorialFiltration.lean:375`)* — For any finite
alphabet `A`, length `N`, ℚ-valued signed measure `μ` on `A^N` invariant under permuting positions,
and any `d`: `μ` kills every one-hot query monomial `∏_{l<m}[x_{ι l}=a_l]` of degree `m < d` (over
an *injection* `ι : Fin m ↪ Fin N`) **iff** every falling-factorial occupancy moment
`∑_x μ(x)∏_a (n_a(x))_{α_a}` with `|α| < d` vanishes. No positivity, no normalization on `μ`. The
`(N)_m` factor appears as `descFactorial_mul_pair` in denominator-free form
`(N)_m·⟨μ,monomial⟩ = ⟨μ,row⟩`; `annihilates_linear_combination` shows the monomial-only
quantification loses nothing.

**W-2 tilted-band chain** *(`ObstructionsTiltedBand.lean`)* — `tnode 0 = 0`, `tnode(i+1) = 5^i`, so
the node set indexed by `range(m+1)` is `{0,1,5,…,5^{m-1}}`, `m+1` points.
`lam m i = ∏_{j≠i}(tnode i − tnode j)⁻¹`. `tilt_annihilates_low_degree`: for every rational
polynomial `P` of degree `< m`, `∑_i P(tnode i)·λ_i = 0` — **no hypothesis beyond `deg P < m`**.
`Afac j = ∏_{d=1}^{j}(5^d−1)^{-1}`, `Cfac h = ∏_{d=1}^{h}(1−5^{-d})^{-1}`.
`lam_ratio (i<m)`: `|λ_{i+1}| = |λ_0|·A_i·C_{m−1−i}` — an identity, derived from `dpr_zero`,
`dpr_succ`, `exponent_identity`. `Cfac_le`: `C_h ≤ 25/19` for every `h`, **hypothesis-free**.
`sum_Afac_le`: `∑_{j<m}A_j ≤ 29/23`, hypothesis-free. `tilt_corr_eq`:
`2|λ_0|/Z = 2/(1+∑_j A_jC_{m−1−j})`. `tilt_corr_ge (m)`: `437/581 ≤ 2|λ_0|/Z ∧ 3/4 < 2|λ_0|/Z`,
**no hypothesis at all**. `tilt_rho_le_four_fifths (m≥2)`: `2|λ_0|/Z ≤ 4/5`.
*Nothing in the module is a statement about a measure on `ℤ_q^N`; `2|λ_0|/Z` is a pure arithmetic
quantity of the coefficients.*

**W-3 ORIENT chain** *(`ObstructionsOrientation.lean`)* — `axisVal s θ = cos(sθ)`,
`intVal s θ = 1` (even `s`) / `cos θ` (odd). `endpoint_even (2≤s, Even s)`: at `θ=π/s`,
`I = −A` and `|A| = 1`. `endpoint_odd (3≤s, ¬Even s)`: at `θ=π/(s+1)`, `I = −A` and `A² ≥ 1/2`.
`blockFourier_eq`: if the layer support `T` contains `0`, every layer index is `≤ r`, every nonzero
layer index is odd, and `∑_{k∈T}W_k = 0`, then evaluating `∑_k W_k A^{r−k}I^k` at `I = −A` gives
**exactly `2W_0A^r`**. `abs_pairing_le_l1`: `‖∑_x p(x)φ(x)‖ ≤ ∑_x|p(x)|` for `‖φ‖ ≡ 1`.
`l1_ge_fourier`: *given* that the phase evaluation equals `(2W_0A^r)^m`, the ℓ¹ norm is
`≥ (2|W_0|)^m|A|^{rm}`. `orientation_corr_le_half_even (r≥2, m≥2, W_0≠0)`: from
`Z ≥ (2|W_0|)^m` and `num·2^{r(m−1)} = 2|W_0|^m`, `num/Z ≤ 1/8`. `_odd`: same with `A² ≥ 1/2` and
`Z ≥ (2|W_0|)^m|A|^{rm}`, giving `≤ 1/2`; `r≥2` is present but **unused** (`_hr`).
*My own exponent arithmetic:* `num/Z ≤ 2^{1−r(m−1)−m}|A|^{−rm}`, and
`1−r(m−1)−m = r+1−m(r+1)`.

**W-4 block clause (iii)** *(`ObstructionsBlock.lean`)* — `tilted_rho_le_four_fifths (m≥2)`:
`2(|λ_{m,0}|/Z_m) ≤ 4/5`, proved by instantiating the three-weight lemma `rho_le_four_fifths` at the
normalized weights `|λ_i|/Z`, `i ∈ {0,1,2}`, using `abs_lam_one_ge` and `abs_lam_two_ge` (both now
theorems). `block_obstruction_two_blocks_tilted`: two proper inner blocks + proper outer Ψ + the
global-NO conjunction + `m ≥ 2` + **`hident : ∀ j, ρ_j = 2(|λ_{m,0}|/Z_m)`** ⇒ `|corr| ≤ 16/25` and
`16/25 < 2/3`.

**W-5 `genEmbed`** *(`KSUM/Support/Embed.lean`)* — For every `k ≥ 3, n ≥ 1, R ≥ 2`, an `EmbedData`
with `ω = 2R−1`, `U = ∑_{i<k−1}ω^i`, `P = k(R−1)U`, `M = k∑_{i<k−1}(2k+1)^i`, `c_P = k(k−1)2^{k−2}`,
`enc p a = w_{⌊p/n⌋} + u_{⌊p/n⌋}·a mod (P+1)(M+1)`, discharging `k ∣ P`,
`2(M+1) = (2k+1)^{k−1}+1`, `R^{k−1} ≤ P ≤ c_P R^{k−1}`, and per-position injectivity.
**`EmbedData` has no field asserting `kSum(encoded) = Coll`.**

**W-6 `KSUM.B1.Claim`/`holds`** — For every `k ≥ 3` there is `C > 0`, **uniform in `N,q,K,t`** (and
in fact in `k`, since `C` is extracted before `intro k`), such that for every `N ≥ k+3`, `K ≥ 2`,
`q ≥ (k²−2)K+2k−1` and every `t`, the length splits as `N = 2n+m` with `n ≥ 2`, `k−2 ≤ m ≤ k−1`, and
`Q(Claw_{n→K}) ≤ C·Q(kSum_{ℤ_q,k,t,N})`. `holds` delivers `C = 4`. `composition_via_A1` takes
`KSUM.A1.Claim` and **does not consume it** (`_hA1`).

**W-7 JointLP** — `lp_weak_duality` is the Chebyshev-dual weak duality for
`max{⟨c,w⟩ : Mw = 0, ‖w‖₁ ≤ 1}`. `lp_optimum` upgrades a primal attaining `B` plus a dual with
`‖c−Mᵀy‖_∞ ≤ B` to `IsGreatest (lpValues M c) B` — **two-sided** (membership + upper bound). Six
`opt_*` theorems instantiate it at rational literals.

**W-8 `KSUM.B4a.Claim`** — `∀ε>0 ∃C_ε>0 ∃N₀ ∀N q [NeZero q], N₀ ≤ N → **2 ≤ q** → ∀t,
Q(2Sum) ≤ C_ε·N^{1/2+ε}·q^{1/4}`. Type audit (7a): the exponents are `Real.rpow` (the exponent
`1/2+ε : ℝ` forces it), so no ℕ-truncation; `C_ε`,`N₀` depend on `ε` only.

**W-9 `sandwichModel`** — `Q(f) = 0` if `f` constant, else `M^{1/2}·(max_i|Alph i|)^{1/4}`. All nine
`QueryModel` fields discharged; `relabel` holds with constant `1`. `sandwich_B4a` (C_ε=1, N₀=1),
`sandwich_B4b` (c=1, N₀=0), `sandwich_nonvacuous = composition sandwichModel sandwich_B4a
sandwich_B4b`.

**W-10 Maschke dictionary** — `InNontrivialSatellite ρ H v := ∃ W ≤ V, v ∈ W, W is H-stable, and W
has no nonzero H-invariant vector`. `inNontrivialSatellite_iff_mem_augment` (H nonempty,
multiplicatively closed): that condition ⟺ `v ∈ augment ρ H` ⟺ `R_H v = 0`.
`transfer_G2_of_satellite`: hence `R_G v = 0 = R_G R_H v`.

**W-11 band-mult (a)/(d)** — `push_conv_ne_zero`: nonzero pushforwards ⇒ nonzero convolution
pushforward, via `genPoly_mul` and `MvPolynomial ℚ` being a domain. `isValueInvariant_conv`:
`IsValueInvariant occ μ σ := ∃ e : I ≃ I, μ∘e = μ ∧ occ(e i) = occ i ∘ σ`; closed under convolution;
`moment_of_isValueInvariant` shows it transports to the falling-factorial moments.

### 3.B Diff against the LaTeX, and verdicts

| # | Lean statement(s) | LaTeX target | verdict | verified (7f) | notes |
|---|---|---|---|---|---|
| 1 | `factorial_filtration` + `annihilates_linear_combination`, `descFactorial_mul_pair`, `sum_hotMon`, `pair_hotMon_const`, `exists_word`, `ffStr_eq_zero_of_lt` | `lem:factorial-filtration` / (38) | **FAITHFUL** | statement + proof read | Both directions, as printed. Alphabet generalized `ℤ_q → any finite `A`` (**WIDER, safe**). `(N)_m` present, denominator-free, load-bearing. Rule 7g: the paper never defines "query polynomial"; the module's DEFINITIONAL NOTE resolves it to the paper's own proof phrase ("a compatible one-hot monomial on `m` distinct queried positions") and `annihilates_linear_combination` closes the monomial-vs-polynomial gap. **The prior review's headline "NOT FORMALIZED" is closed.** |
| 2 | `uniformLift`, `uniformLift_SNInvariant`, `sum_uniformLift_comp`, `l1_uniformLift`, `annihilates_query_of_occ_moments` | no label (the paper's implicit orbit-lift step) | **FAITHFUL** (infra) | statement + proof read | `l1_uniformLift` **is** the pushforward ℓ¹ identity the prior review recorded as missing (§6.B, `thm:pair-tensor` row). The orbit sizes cancel exactly; no multinomial appears. |
| 3 | `tnode`, `lam` | (42) | **FAITHFUL** | statement + proof read | `T_m = {0,1,5,…,5^{m−1}}`, `m+1` nodes, `λ_k = (∏_{u≠k}(k−u))^{-1}` — exact. The indexing convention the commission flagged (`tnode 0 = 0`, `tnode(i+1)=5^i`) **is** the paper's node set. |
| 4 | `tilt_annihilates_low_degree` | "there are `m+1` nodes in `T_m`, so divided differences give `∑λ_k p(k)=0` for every `p` of degree below `m`" | **FAITHFUL** | statement + proof read | **Proved, not assumed**, via `Lagrange.coeff_eq_sum`. |
| 5 | `Afac`, `Cfac`, `lam_ratio` (+ `dpr_zero`, `dpr_succ`, `exponent_identity`) | (44) | **FAITHFUL** | statement + proof read | `A_j`, `C_h` are the paper's products verbatim; `|λ_{5^i}|/|λ_0| = A_iC_{m−1−i}` is an identity, derived by the paper's own "cancellation of common powers of five". |
| 6 | `Cfac_le` : `C_h ≤ 25/19` | (44)'s first bound | **FAITHFUL + NEW MANUSCRIPT FINDING** | statement + proof read, **and re-derived by hand** | The bound is true and now proved. **But the paper's printed justification does not give it.** The paper writes *"The elementary inequality `∏(1−x_i) ≥ 1−∑x_i` gives `C_h ≤ 25/19`"*; applied flat to `d = 1…h` that inequality gives `∏(1−5^{-d}) ≥ 1−1/4 = 3/4`, i.e. only `C_h ≤ 4/3 = 1.3333 > 25/19 = 1.31578`. The Lean route (peel the `d=1` factor exactly, bound the tail `∑_{d≥2}5^{-d} = 1/20`: `(4/5)(19/20) = 19/25`) is what yields `25/19`. **One sentence of the manuscript proof is a genuine gap; the formalization closes it.** Independently confirmed: `C_∞ ≈ 1.31520 ≤ 25/19`, so the bound itself is sound and near-tight. |
| 7 | `sum_Afac_le` : `∑_j A_j ≤ 29/23` | (44)'s second bound | **FAITHFUL** | statement + proof read, re-derived | `1 + 1/4 + (1/96)(24/23) = 29/23` exactly; the paper's `A_0,A_1,A_2` and "every later ratio at most `1/24`" are the Lean's `Afac_zero/one`, `Afac_tail_le`, `geom24`. |
| 8 | `tilt_corr_eq`, `Ssum_le`, `tilt_corr_ge` | (43) + (41) | **NARROWER** | statement + proof read | The *value* `2|λ_0|/Z ≥ 437/581 > 3/4` is now **hypothesis-free** — the prior review's specific complaint ("the two paper bounds are HYPOTHESES") is **discharged**. What remains unformalized: the measure on `ℤ_q^N`; the identification `⟨μ,F⟩ = 2|λ_0|/Z` that **is** (43); the activity-degree ⇒ falling-factorial-order transfer; the ℓ¹/invariance bookkeeping. The module header states all four. |
| 9 | `abs_lam_one_ge`, `abs_lam_two_ge`, `tilt_rho_le_four_fifths` | block clause (iii)'s "the `K=1` and `K=5` absolute weights are at least `5/4` and `1/4` times the `K=0` weight, so `ρ ≤ 2/(1+5/4+1/4) = 4/5`" | **FAITHFUL** | statement + proof read | Word-for-word the paper's three-weight step, on the paper's own weights, with both ratios now theorems. `m ≥ 2` ⟺ the paper's "at least five complementary pairs" (`r ≥ 5 ⇒ m = 1+⌊log₅r⌋ ≥ 2`) — **exact**. |
| 10 | `endpoint_even` | ORIENT proof, even `s` | **FAITHFUL** | statement + proof read, re-derived | `cos(s·π/s) = −1`, `I = 1 = −A`, `|A| = 1`. Exactly as printed. |
| 11 | `endpoint_odd` | ORIENT proof, odd `s` | **FAITHFUL** | statement + proof read, re-derived | `cos(s·π/(s+1)) = −cos(π/(s+1))`, `I = −A`, `A² ≥ 1/2` ⟺ the paper's `|A_s| ≥ 2^{-1/2}`. The Lean's `3 ≤ s` is forced by the paper's own `s ≥ 2` + odd — no gap. |
| 12 | `blockFourier_eq` | *"If `W_0` is the all-axis outer weight and `ρ = 2\|W_0\|`, the positive support nodes are odd and `∑_kW_k = 0`, whence the one-block Fourier modulus is `ρ\|A_s\|^r`"* | **FAITHFUL** | statement + proof read, re-derived | **The commission's hardest check passes:** the four hypotheses (`0 ∈ T`, `k ≤ r`, nonzero layers odd, `∑W = 0`) are the paper's own sentence about the *construction*, not a restatement of the conclusion. And they are consistent with the tilted inner: all `5^i` are odd, and `∑λ_k = 0` is `tilt_annihilates_low_degree` at `P = 1`. |
| 13 | `abs_pairing_le_l1`, `l1_ge_fourier` | *"the triangle inequality lower-bounds the post-average norm by `ρ^m\|A_s\|^{rm}`"* | **NARROWER** | statement + proof read | The triangle inequality is proved. *"Convolution raises this to the `m`th power"* enters `l1_ge_fourier` as the hypothesis `hfourier`. Declared in the module header. |
| 14 | `orientation_corr_le_half_even`, `_odd` | (51) and *"at most `1/8` for even `s`, `1/2` for odd `s`"* | **NARROWER** | statement + proof read, **exponent re-derived by hand** | The derived exponent `1−r(m−1)−m` **equals** the paper's `r+1−m(r+1)`, and `\|A\|^{−rm}` matches — so what the kernel now checks *is* (51), not an approximation of it. The prior review's "the analytic norm lower bound that PRODUCES (51) is absent" is **substantially discharged**. Residual: `hnum` and `hZ`/`hfourier` are structural hypotheses about the named construction. `_odd` drops `r ≥ 2` (declared WIDER on that axis, harmless). **One presentational point:** the four links are each kernel-checked but are **not composed into a single declaration** — the end-to-end chain is assembled in prose. |
| 15 | `block_obstruction_two_blocks_tilted` | clause (iii) sentence | **NARROWER** | statement + proof read | **The commission's check passes: `hident` is structural, not numeric.** `ρ_j = 2\|W_0\| = 2\|λ_0\|/Z` is the paper's *own* equation (ORIENT proof + (43)); what is assumed is *which measure the block carries*, and `ρ ≤ 4/5` is then derived. Residual: reading `ρ_j` off the tilted measure needs the inner pair tensor on `ℤ_q^N`. |
| 16 | `block_obstruction_band_combination` | clause (i) | **NARROWER** | statement + proof read | Correctly presented as the **linearity half only**, with the `m`-fold multivariate Vandermonde named as the whole residual, in the docstring, *not* as closing clause (i). Matches the prior review's finding exactly. |
| 17 | `push_conv_ne_zero` (+ `genPoly`, `coeff_genPoly`, `genPoly_mul`, `push_ne_zero_iff`) | `lem:band-multiplication` (a) | **FAITHFUL** | statement + proof read | This **is** the paper's integral-domain argument on generating polynomials. `push` is the occupancy pushforward and `coeff_genPoly` proves it is the coefficient vector — so the rendering of `ν` is verified, not asserted. |
| 18 | `isValueInvariant_conv` (+ `isValueInvariant_smul`, `moment_of_isValueInvariant`) | `lem:band-multiplication` (d) | **FAITHFUL** | statement + proof read | `IsValueInvariant` is per-`σ`, hence per-element of any common value group; `moment_of_isValueInvariant` shows the notion is not decorative. Mildly *stronger* as a hypothesis (an index bijection is demanded) but the clause is a closure property, so the strength cuts both ways symmetrically. |
| 19 | `splitEquiv`, `occ_append`, `sum_prod_uniformLift`, `l1_prod_uniformLift`, `moment_prod_uniformLift` | `lem:band-multiplication`'s derivation of `ν` | **NARROWER** | statement + proof read | The three objects batch 1 named as the residual are all proved, and the test-function form **is** "take the occupancy pushforward" (`g` arbitrary on `A → ℕ`). Remaining residual, named in the header: the `S_N`-average operator itself. |
| 20 | `genEmbed` + `embedOmega/U/P/M/u/w`, `geom_mul_add_one`, `embed_two_mul_M`, `embed_P_lower`, `embed_P_upper`, `embed_enc_inj` | `lem:embed`'s **parameter display** | **FAITHFUL** | statement + proof read, arithmetic re-derived | Every symbol matches after the 1-index→0-index shift: `u_j = ω^{j−1}` / `u_k = −(ω^{k−1}−1)/(ω−1)`; `w_j = V(2k+1)^{j−1}` / `w_k = −∑`; `P = k(R−1)(ω^{k−1}−1)/(ω−1)`; `M = ((2k+1)^{k−1}−1)/2`; `q = (P+1)(M+1)`. Both ℕ-divisions are the geometric sums they abbreviate (`geom_mul_add_one`), so no truncated subtraction enters a claim. **`c_P = k(k−1)2^{k−2}` depends only on `k`** — I re-derived it: `U ≤ (k−1)(2R)^{k−2}`, `P ≤ kR·(k−1)2^{k−2}R^{k−2}`. Anchors check: `k=3,R=2 ⇒ q=325` (= `demoEmbed`), `k=4,R=3 ⇒ q=249·365=90885`. |
| 21 | `genEmbed` vs the **encoding identity** | `prop:embed` (`kSum_{ℤ_q,0,kn}(encoded) = Coll_{k,n→R}(g)`) | **NOT FORMALIZED** (declared) | — | **The commission's check passes at the Lean level: `genEmbed` claims only the `EmbedData` fields.** The module header (lines 178–184) and `lean/README.md` line 114 both say so explicitly. `KSUM.A2a.Claim` / `KSUM.A2b.Claim` carry the identity and are **`def Claim : Prop`, with no proving theorem anywhere** (verified by declaration scan). **The census contradicts this — see C-1.** |
| 22 | `lp_weak_duality` | — | **FAITHFUL** (infra) | statement + proof read, re-derived | Textbook Chebyshev weak duality, correct. |
| 23 | `lp_optimum` | "exact rational LP-certified" (the optimum, two-sided) | **FAITHFUL** | statement + proof read | `IsGreatest` = membership **and** upper bound. **Yes, it really proves a two-sided optimum.** |
| 24 | the six `opt_*` | (39)'s optima table | **FAITHFUL on the values** | **re-verified three ways, §6** | Every one of the six matches the paper's printed optima table exactly. The *inference to (39)'s rows* is where the overclaim is — §6.3 and C-3. |
| 25 | `KSUM.B1.Claim`, `composition_via_A1_inputs`, `holds` | the frozen `## Claim` of `KSUM.B1` (hash `aa324409…`) | **NARROWER** | statement + proof read | Three checks the queue asked for: **(a)** `k+3 ≤ N` is added and is not in the prose — NARROWER, declared, and it is exactly what forces `n ≥ 2` (`2n = N−m ≥ (k+3)−(k−1) = 4`). **(b)** `∃C` sits outside `∀N,q,K,t` — the strong reading of `Ω(·)` ✓, and in fact outside `∀k` too, so the delivered `C = 4` is absolute. **(c)** `Ω(·)` made explicit, no claw bound imported (`abi`/`tani` unused) — verified from the proof term. Arithmetic check: `(k^2-2)*K+2*k-1` in ℕ parses as `((k²−2)K+2k)−1`, which equals `(k²−2)K+2k−1` since the minuend is ≥ 2 for `k ≥ 3` — **no truncation**. |
| 26 | `composition_via_A1` | §7.4's required route theorem for child `A1` | **WIDER (disclosed, harmless)** | statement + proof read | It proves the conclusion **without** its hypothesis (`_hA1`). As a rendering of "A1 ⇒ B1" it is logically true and informationally empty. The module header and the node both say so at length. This is the delta's single WIDER. |
| 27 | `DonorClaim` (`L : ℕ→ℕ→ℕ→ℝ`), `composition`, `composition_with_donor`, `demoDonor` | `KSUM.B2`'s composition claim / `KSUM.k3.donor` | **FAITHFUL** | statement + proof read | The prior review's KSUM-layer caveat (2) — "`L` has no `k` argument, so it demands one `L` uniform in `k`, a real narrowing" — is **closed**: `L` now carries `k`. *Note:* `demoDonor` uses `L k n R = −(k:ℝ)`, so the `k`-dependence is exercised only in a degenerate (negative) direction; it witnesses satisfiability of the retyped hypothesis, nothing more. The module says exactly that. |
| 28 | `sandwichModel`, `sandwich_B4a`, `sandwich_B4b`, `sandwich_nonvacuous` | the `KSUM.B4` matching (sandwich) claim | **FAITHFUL** (non-vacuity witness) | statement + proof read, all nine fields re-checked | See §5.3. Not a claim about the paper; a consistency witness for `KSUM.B4.composition`. |
| 29 | `InNontrivialSatellite`, `inNontrivialSatellite_iff_mem_augment`, `transfer_G2_of_satellite` (+ `reynolds_of_invariant`, `reynolds_mem_invariant`) | `prop:transfer-facts` (G2) + (52) | **FAITHFUL** | statement + proof read, dictionary re-derived | **The commission's hardest question, answered YES.** The paper's (52) satellite is a summand `U_λ⊗M_λ` with `λ` nontrivial; the Lean's condition is "`v` lies in *some* `H`-stable subspace with no nonzero `H`-invariant vector". Since `R_H` is the projection onto the trivial isotypic, the two coincide up to the Lean condition being the *sum* of all nontrivial isotypics rather than a single summand — i.e. **the Lean hypothesis is weaker, so the theorem is stronger**: the safe direction. The recorded route deviation (Mathlib's Maschke deliberately not invoked) is legitimate: the char-0 content actually needed is "`R_H` is an `H`-equivariant idempotent onto the invariants with kernel the augmentation submodule", and that is what the two lemmas prove — routing through `MonoidAlgebra.Submodule.exists_isCompl` would give a *weaker* conclusion. **`hclosed` + `hH` is equivalent to "subgroup" for finite `H` in a group, and is stated more weakly (no inverse-closure), so nothing is granted.** The prior review's NARROWER is **closed**. |
| 30 | `KSUM.B4a.Claim` with `2 ≤ q` | `thm:k2-upper` ("every integer `q ≥ 2`") | **FAITHFUL** | statement + proof read | The prior review's single **WIDER is CLOSED**. `KSUM.B4.composition` still closes because it invokes the Claim only at `5 ≤ q` — verified in the proof term. |
| 31 | `demoEmbed`, `demoEmbed_q` | — | infra/witness | statement read | §5.2. |
| 32 | five `core_reduction_at` witnesses at `r ≥ 1` | — | infra/witness | statement + proof read | §5.4. |

**Tally (counting unit: one row per Lean statement-group × LaTeX target ruled on above):
21 FAITHFUL, 7 NARROWER, 1 WIDER, 0 DIVERGENT, 1 declared NOT-FORMALIZED, 2 infra/witness.**

### 3.C Coincidences with the executors' own wording (7c disclosure)

- Row 6's observation that flat Weierstrass gives only `4/3` coincides with the batch-2 report §2.4.
  I derived it independently while checking whether `Cfac_le` was "the cruder `4/3` in disguise" (the
  commission's prompt), and only then read §2.4. The substance — that the *manuscript's printed
  one-liner is insufficient* — is my own verdict and is **not** stated in the batch report as a
  manuscript defect; the report frames it as a proof-engineering note.
- Row 28: `sandwichModel` implements the construction the **prior review** prescribed in its §7.3.
  Disclosed above; I verify it rather than claim independent discovery.

---

## 4. DF-4 — PAPER-DELTA RE-GRADING (v5.1 → v5.2)

| Prior verdict (2026-07-31) | LaTeX side in v5.2 | **NEW verdict** | caveat discharged? |
|---|---|---|---|
| `restrict` vs fact (i): **NARROWER (safe)** | `sec:prelim` now states *"every restriction we invoke in fact (i) below is to such a product subdomain `∏_i D_i`"* | **NARROWER (safe), now DISCLOSED IN THE PAPER** | **YES** — the narrowing is no longer undocumented; the field matches the paper's declared usage exactly |
| `relabel` vs fact (ii): **FAITHFUL** | untouched | **FAITHFUL** | n/a |
| `freeze`: **NOT-A-PAPER-CLAIM (finding F1)** | fact **(iii) singleton-coordinate deletion** added, with the explicit *"This is not an instance of (i)"* note; `lem:oddN` and the `sec:k3` freeze step now cite (i)+(iii) | **FAITHFUL** — `freeze` is exactly (i) then (iii), composed at the last position | **YES.** F1 is discharged, in the sharper form the prior review itself recommended (§3.B(c)) |
| `constQ`: **NOT-A-PAPER-CLAIM (finding F2)** | fact **(iv)** added; `thm:oabarrier`'s proof cites it | **FAITHFUL** | **YES.** F2 discharged |
| `cor:threshold` Case 2 / `threshold_small_abi`: **FAITHFUL + F6** | Case 2 rewritten ABI-only, with the ABI-form arithmetic `κ ≤ (q−1)/2 ≤ (N−3)/2 < (N−1)/2 ≤ n`; the statement gained *"Theorem `thm:tani` is not needed for this corollary"* | **FAITHFUL** | **YES.** F6 discharged; Lean and LaTeX now cite the same theorem |
| `cor:threshold` Case 2 parity detour (F7) | *"`2κ+1 ≤ q` for either parity … Lemma `lem:encode` applies as it stands, with no detour through Theorem `thm:main-general`"* | **FAITHFUL** | **YES.** F7 discharged |
| hidden `c`-dependence | the statement now names both places (`c^{1/6}`; the validity threshold `cN ≥ 5`), both confined to `cN ≤ q < N−1`, and records that `q ≥ N−1` needs only `N ≥ 6` | **FAITHFUL — exact match to `threshold_small`/`threshold_large`'s hypotheses** | **YES** |
| `cor:threshold` (whole) / `threshold`: **NARROWER (declared)** | unchanged (`Θ_c`; upper half out of scope) | **NARROWER (declared)** | no change |
| `thm:block-obstruction` (49): **FAITHFUL**, with the `OR_m` term-of-art flagged (F-T9) | the disambiguating sentence is now in the theorem **STATEMENT** | **FAITHFUL, rule 7g fully satisfied** | **YES.** F-T9 discharged |
| `thm:kfloor` transfer step / `KSUM.A1d.Claim`: **NARROWER (safe)** — plateau nested under `q ≤ C_kN` where the paper has no ceiling | the paper now names the **claw range condition `2 ≤ K ≤ 2m−1`** ("not optional"), defines `m,K`, prints `q/q₀(k) ≤ K ≤ q/(k²−2)` and `q ≤ 2k²K`, and takes `K = m−1` for the plateau | **NARROWER (safe) — UNCHANGED.** The paper's plateau really is ceiling-free (`K = m−1` does not depend on `q`), so the Lean's nesting is still a narrowing. The v5.2 prose does, however, make it visible *why* the ceiling appears in the non-plateau range | partially — the *reason* is now printed |
| `thm:k2-upper` / `KSUM.B4a.Claim`: **WIDER** (dropped `q ≥ 2`) | untouched | **FAITHFUL** (closed on the *Lean* side, closeout C-5) | **YES.** The audit's single WIDER is gone |

### 4.1 M-10 (the `A machine-checked layer` remark) — overclaim check

**Verdict: HONEST. No overclaim.** Line by line:

1. *"the imported quantum content enters as hypotheses: Theorems `thm:abi` and `thm:tani` with facts
   (i)–(iv) of Section `sec:prelim`, and nothing else."* — **ACCURATE, and true only since v5.2.**
   The nine `QueryModel` fields map onto exactly: `restrict`=(i) [narrower], `relabel`=(ii),
   `freeze`=(i)+(iii), `constQ`=(iv), `abi`/`tani`= the two theorems, `Q` a definition,
   `cABI`/`cABI_pos` bookkeeping. Field-by-field enumeration is exhaustive; **no third unstated
   assumption has appeared** in the delta.
2. Both §7.9 clauses appear **verbatim** — checked character by character.
3. *"The `k ≥ 3` cores and the obstruction theorems carry no interface hypothesis and are
   unconditional."* — **ACCURATE at the statement level**: no theorem in `T2KFloor`,
   `RosmanisBarrier`, `Obstructions*`, `FactorialFiltration`, `JointLP` mentions `QueryModel`
   (verified by grep over all of them). *(Correcting the prior review on a detail:
   `KsumAudit/T2KFloor.lean` **does** `import KsumAudit.MainLine`, hence transitively imports
   `QueryModel`; the prior review said "neither imports it". The unconditionality claim is
   unaffected — importing is not using.)*
4. The kernel-confirms / does-not-confirm split. **This is where the remark now UNDER-states**, which
   the commission pre-authorized as acceptable: after batches 1–2, (51) is *derived* from the
   construction's structural facts, `ρ_j ≤ 4/5` is *derived* from the tilted inner, and the
   tilted-band arithmetic chain is hypothesis-free. **One sentence is now factually stale, not merely
   conservative:** *"whose analytic inputs — among them the bound (51) … — enter the formalization as
   hypotheses, not as proved content."* On disk, `orientation_obstruction_half` still takes (51) as a
   hypothesis, but `orientation_corr_le_half_even/odd` derive the same bound from the paper's own
   construction facts. Recorded as honesty item **D-3'** (§7), in the conservative direction.

---

## 5. DF-5 — VACUITY AND SATISFIABILITY

### 5.1 `sandwich_nonvacuous` — **PASS**

`sandwichModel` discharges all nine `QueryModel` fields (I re-checked each proof term):
`restrict`/`relabel`/`freeze` all reduce to the single monotonicity lemma `sandwichQ_le_of`
(shorter length, smaller alphabet, constancy inherited); `constQ` by construction; `abi`/`tani` with
`cABI = 1` from `√n·κ^{1/6} ≤ (2n)^{1/2}κ^{1/4}` (`κ ≥ 2`, `n ≥ 1`).
`sandwich_B4a`: `Q(2Sum) = N^{1/2}q^{1/4} ≤ N^{1/2+ε}q^{1/4}` with `C_ε=1, N₀=1`.
`sandwich_B4b`: in the regime `q` odd, `5 ≤ q ≤ N`, `twoSum_nonconst` applies (it needs `N ≥ 2`,
`q ≥ 3`, both implied), so `Q(2Sum)` is **exactly** `N^{1/2}q^{1/4}`, giving `c = 1`.
`sandwich_nonvacuous := composition sandwichModel sandwich_B4a sandwich_B4b` — **both hypotheses of
`KSUM.B4.composition` are simultaneously satisfied by one model.** The prior review's §7.3 gap is
genuinely closed.
*Honest qualification, as for `demoModel`:* the witness satisfies `relabel` with constant `1`, so the
factor-2 slack remains untested; and it says nothing about the true `Q`. Both stated in the module.

### 5.2 `demoEmbed` / `genEmbed` — **PASS**

`demoEmbed` (`k=3,n=1,R=2,P=12,Mv=24,c_P=3`, `q=325`) discharges every `EmbedData` field, none by a
hypothesis-free restatement; `P_upper` is **tight** (`12 = 3·4`), so `c_P` is not slack there.
`genEmbed` supersedes it: the four `∀ D : EmbedData` Claims are now about a **family** indexed by
every `k ≥ 3, n ≥ 1, R ≥ 2`, which is what removes the prior review's KSUM-layer caveat (3)
(`Θ_k(R^{k−1})` per-instance rather than uniform in `R`). Anchors: `genEmbed 3 1 2` reproduces
`demoEmbed`'s modulus `325` from the formulas; `genEmbed 4 1 3` gives `q = 249·365 = 90885`
(I recomputed both).

### 5.3 `KSUM.B4.composition` — **PASS** (see 5.1). `KSUM.A2`/`KSUM.B2` — **PASS** (see 5.2).

### 5.4 `core_reduction_at` at `r ≥ 1` — **PASS, and better than asked**

Five declarations at `k=3, K=2, q=19 = q₀(3)`: `witness_even_pos_at`, `witness_even_neg_at` at
`r = 2 = k−1` (the **rightmost** window target, where the modulus hypothesis
`(k²−2)K+2k−1 ≤ q` is **tight**: `7·2+5 = 19 = q`), and `witness_odd_pos_at`,
`witness_odd_neg_at` at `r = 1` (parked-coordinate branch). All five hypotheses of
`core_reduction_at` are discharged at each. **The fifth declaration is the one that matters:**
`witness_coreVecAt_shifted` proves `coreVecAt … r=2` carries `9` where `coreVec` carries `7` — so
the witnesses **cannot be read as `r = 0` in disguise**. That is precisely the anti-degeneracy check
the prior review's §7.4 gap called for.

### 5.5 Tilted-band / ORIENT tight witnesses — **PASS**

`lam_two_values` (`λ = 1/5, −1/4, 1/20` at `m=2`) — I recomputed all three from (42) directly;
`Znorm_two = 1/2` (`1/5+1/4+1/20 = 1/2` ✓); `tilt_corr_two`: `2(1/5)/(1/2) = 4/5` **exactly**, so
clause (iii)'s `4/5` is **tight**, not vacuous. `Afac 0·Cfac 1 = 5/4` and `Afac 1·Cfac 0 = 1/4`
confirm (44) numerically at `m = 2`.
ORIENT: `orientation_corr_le_half_even` tight at `r=m=2` (`1/8` exactly);
`orientation_corr_le_half_odd` tight at `A = √2/2` (`A² = 1/2`, `corr = 1/2` exactly);
`blockFourier_eq` witnessed at `T = {0,1}`, `W = (−1/2, 1/2)` (unit ℓ¹, zero total, nonzero node
odd); `l1_ge_fourier` witnessed tight. `endpoint_odd`'s `A² ≥ 1/2` shown tight at `s = 3`.
Block clause (iii): the `Fin 3` witness `tμ`/`tNO` has `ρ_j = 4/5` **and** satisfies `hident` exactly
via `tilt_corr_two` — a genuine joint witness for `block_obstruction_two_blocks_tilted`.

---

## 6. DF-6 — VALUE-VS-FORMULA (rule 7f) FOR `JointLP`, AND F-LP-1

**I did not accept the certificates. I verified them three independent ways.** Script:
`scratchpad/df6_verify.py` (exact `Fraction` arithmetic throughout; literals parsed **from
`KsumAudit/JointLP.lean`**, not from the JSON, so the check is on what the kernel checked).

### 6.1 (A) Re-verification of all four `lp_optimum` goals, all six LPs

| case | `Mw = 0` | `‖w‖₁ = 1` | `⟨c,w⟩ = B` | `max_j\|c−Mᵀy\|_j ≤ B` | B |
|---|---|---|---|---|---|
| `s330_single_d1` | ✓ | ✓ | ✓ | ✓ (`= 2/3`) | `2/3` |
| `s330_joint_d2` | ✓ | ✓ | ✓ | ✓ (`= 1`) | `1` |
| `s330_joint_d3` | ✓ | ✓ | ✓ | ✓ (`= 1/2`) | `1/2` |
| `s541_single_d3` | ✓ | ✓ | ✓ | ✓ (`= 11/21`) | `11/21` |
| `s541_joint_d3` | ✓ | ✓ | ✓ | ✓ (`= 5/7`) | `5/7` |
| `s541_joint_d4` | ✓ | ✓ | ✓ | ✓ (`= 3/5`) | `3/5` |

**ALL SIX VERIFIED.** (In each case the dual residual *attains* `B`, so the certificates are tight,
not slack.)

### 6.2 (C) Independent exact RE-SOLVE, not using the duals at all

I re-solved each LP from `(c, M)` alone by exact vertex enumeration over signed supports (Fraction
Gaussian elimination, no floating point, `y` never referenced): **all six optima recomputed and
identical** (`2/3, 1, 1/2, 11/21, 5/7, 3/5`). So the certified values are the true optima
independently of the certificate scheme.

### 6.3 (B) **Is the LP data the manuscript's program, or a re-encoding of the answer?**

This is the load-bearing 7f question, and the answer is **it is the manuscript's program.** I
rebuilt the LP data from the paper's own recipe by brute force over `ℤ_q^N`:

- **Objective.** For `(N,q,t) = (3,3,0)`: enumerate all `27` strings, evaluate
  `2Sum_t(x) = ∃i<j, x_i+x_j = t`, form the orbits, and take the **orbit mean of the ±1 indicator
  (+1 on YES)**. Single basis (sorted occupancy → partitions of 3): `c = (−1/3, 1/3, 1)` —
  **identical to `c_s330_single_d1`**. Joint basis (occupancy modulo the value symmetry
  `{fixed point 0}`, `{pair {1,2}}`): 6 orbits, `c = (−1,1,−1,1,1,1)` — **identical, element by
  element, to `c_s330_joint_d2` and `_d3`**. For `(5,4,1)` (no fixed point, pairs `{0,1},{2,3}`):
  single 6 orbits `c` matches `c_s541_single_d3` as a multiset; joint 10 orbits
  `c = (−1,1,1,−1,1,1,−1,1,1,1)` — **identical, element by element, to `c_s541_joint_d3` and `_d4`.**
- **Moment matrix.** For `(3,3,0)` joint I rebuilt the rows as orbit averages of
  `∏_a(n_a)_{α_a}` over the value-relabeling orbit of `α`, for every `α`-class of order `< d`:
  **3 rows at `d = 2` and 7 rows at `d = 3`, both matching the Lean literals as row multisets.**
  By hand: row₁ = `(n_1+n_2)/2`, row₂ = `n_0`, and at `d=3` additionally `(n_0)_2`,
  `n_0(n_1+n_2)/2`, `((n_1)_2+(n_2)_2)/2`, `n_1n_2` — the four order-2 `α`-classes over
  `{0}∪{1,2}`, exactly.

**7f STATEMENT: the kernel verifies the PROVED FORMULA, not an independent construction of the same
number — and, separately, I have independently constructed the same LP data from the manuscript's
definition and it agrees. The literals are the program.**

### 6.4 Do the kernel-checked six really decide rows 1 and 3 of (39)? — **NOT ENTIRELY**

Paper (39): `(3,3,0): 0 | 2`; `(4,3,0): 0 | 2`; `(5,4,1): 2 | 3`, where the certified degree is
*"the largest `d` whose exact optimum is strictly greater than `2/3`"*.

| row half | what the six give | decided? |
|---|---|---|
| `(3,3,0)` single `= 0` | `opt(d=1) = 2/3`, **not** `> 2/3` | **yes**, given monotonicity |
| `(3,3,0)` joint `= 2` | `opt(2) = 1 > 2/3` **and** `opt(3) = 1/2 ≤ 2/3` | **yes**, given monotonicity |
| `(5,4,1)` joint `= 3` | `opt(3) = 5/7 > 2/3` **and** `opt(4) = 3/5 ≤ 2/3` | **yes**, given monotonicity |
| `(5,4,1)` single `= 2` | `opt(3) = 11/21 ≤ 2/3` ⇒ certified degree **≤ 2** only | **NO** — the matching half `opt(2) > 2/3` is JSON-certified but **not kernel-checked** |

Two gaps, both small and both real:

1. **`(5,4,1)` single `= 2` is not decided by the six** — only bounded above. The module's docstring
   writes *"optimum `11/21 ≤ 2/3`, so the single certified degree is `2`"*, which does not follow;
   the batch report and the census repeat "decide rows 1 and 3". Recorded as **C-3**.
2. **Monotonicity of the optimum in `d` is argued in a docstring, not proved in Lean.** It is true
   and trivial (higher `d` = more equality constraints = smaller feasible set), but every "largest
   `d`" reading of the four verdicts depends on it, and there is no Lean theorem. Recorded as
   **C-3(b)**.

### 6.5 F-LP-1 — **INDEPENDENTLY REPRODUCED**

Script `scratchpad/flp1_repro.py`, fresh process, sympy **1.13.1**:

```
[lpmin]   objective = 0   solution = {s: 0, y: -1/3}
          constraints VIOLATED at: [(1/3, 2/3), (1, 4/3)]   -> INFEASIBLE
[linprog] objective = 0   solution = [0, 1/3, 0]  (y = -1/3, s = 0)
          constraints VIOLATED at: [(1/3, 2/3), (1, 4/3)]   -> INFEASIBLE
[brute force] true min_y max_j |c_j - y| = 2/3 at y = 1/3
```

Both `sympy.solvers.simplex.lpmin` and `linprog` return an **infeasible** point violating their own
constraints (`|1−(−1/3)| = 4/3 ≰ 0`) and an objective of `0` where the truth is `2/3`. **The finding
is real and is not a one-run artifact.** Scope note for the record: this is sympy **1.13.1** on this
machine; the finding should be recorded version-scoped. **Consequence for the manuscript: none** — I
confirm the ancillary script uses `lpmax` on the primal and every primal witness re-verifies exactly
(§6.1), and the duals in the Lean literals come from `tools/exact_simplex.py` and are re-checked by
the kernel and, now, by me.

---

## 7. DF-7 — HONESTY OF THE RECORD AFTER FOUR BATCHES

### 7.1 What is exemplary

- `lean/README.md` is genuinely current on the delta: `FactorialFiltration.lean`, `JointLP.lean`
  (with *"the other 18 are not kernel-checked"*), `genEmbed` (with **"The encoding IDENTITY is still
  A2a/A2b's Claim, not `EmbedData`'s"** — the honest statement the census fails to make),
  `sandwichModel`, and the 283-declaration figure.
- The §7.9 scope clauses are still verbatim; the "what a green build does not establish" list is
  intact; the m-1 phrasing defect the prior review found is explicitly annotated as corrected.
- Every module that under-delivers says so in its own header, in the right place: `TiltedBand`
  ("the LaTeX theorem as a whole … is still not a theorem of this file"), `Orientation` ("STILL an
  explicit hypothesis"), `Block` ("the precise residual gap"), `Embed` ("What is NOT proved here is
  the encoding identity"), `JointLP` ("the other 18 … not kernel-checked").
- The campaign ledger records both gap batches with build figures, per-item verdicts including
  **RESISTED / NOT REACHED / NOT ATTEMPTED**, and an explicit "Owed next" — including the
  self-flagged *"the stale caveat text on `KSUM.LEAN.T3` that batch 2's closures made inaccurate (a
  re-grading call for the reviewer, not the executor)"*. That is the protocol working.
- 19 node files carry dated batch-1/batch-2 records (rule 8c).

### 7.2 Honesty defects found (7 items)

- **D-1 (systematic, 7 files, conservative).** The Lean layer still asserts that `freeze` and
  `constQ` are **not in the manuscript**, which paper v5.2 falsified: they are facts **(iii)** and
  **(iv)**. Locations: `KSUM/Interface.lean` L27, L34 (*"NOT STATED IN THE MANUSCRIPT"*);
  `KSUM/Trust.lean` L53, L55 (*"**NOT IN THE MANUSCRIPT**"* in the trust table);
  `KsumAudit/QueryModel.lean` (both field docstrings, *"NOT stated in `sec:prelim`"*);
  `KSUM/A1.lean` L19, L50, L133, L267; `KSUM/B1.lean` L16, L138, L198;
  `KSUM/Support/Freeze.lean` L13; `KsumAudit/MainLine.lean` L14. **Consequence:** the development's
  standing conditionality statement ("conditional on ABI21 + Tani24 + facts (i)/(ii) + two unstated
  principles") should now read **"conditional on ABI21 + Tani24 + facts (i)–(iv), all stated"** — a
  materially better position than the record claims. Conservative direction; no soundness impact;
  but it is the H-4/H-5 pattern recurring, this time introduced by the manuscript batch not syncing
  back to the Lean layer.
- **D-2 (`KSUM/Trust.lean`, conservative).** §(b) says of `EmbedData`'s fields *"none of them is
  proved here"*. False since batch 2: `genEmbed` proves `k_dvd_P`, `two_mul_Mv`, `P_lower`,
  `P_upper`, `cP_pos` and `enc_inj` **for the manuscript's own formulas**, for every `k,n,R`.
- **D-3 (`KSUM.LEAN.T3.obstruction-theorems.yaml` frontmatter `caveat`, conservative).** Stale in four
  places after batches 1–2: *"(iii) rho<=4/5 ASSUMED"* (now derived), *"transfer (G2)
  satellite-replaced-by-augmentation-submodule (Maschke granted)"* (now proved), *"kernel does NOT
  confirm the orientation obstruction"* ((51) now derived from structural facts), *"or the
  tilted-band witness"* (outer half now hypothesis-free). The node **body** records the closures;
  only the frontmatter caveat is stale. The executor flagged this as a reviewer call — **I make it
  here: the caveat needs re-writing, and the four re-gradings are rows 8, 9, 14, 29 of §3.B.**
- **D-3′ (paper, conservative).** The M-10 sentence naming (51) as entering "as a hypothesis, not as
  proved content" is now inaccurate; see §4.1(4). Under-claims, so acceptable, but stale.
- **D-4 (`KSUM.B1.yaml`, conservative + an arithmetic slip).** `status_source` and "## Current status"
  both still say the route proof *"is statable and near-trivial, but unwritten and unreviewed"*.
  It **is** written (`composition_via_A1_inputs`, `holds`, `C = 4`) — the `lean.note` field says so,
  four lines below the frontmatter that denies it. Separately, the node computes
  `min(A1 = PROVED, route = CONJECTURED) = CONJECTURED`, while the node's own `composition` block
  records the A1 route at **NUMERICAL**; per §1 the recompute is `min(PROVED, NUMERICAL) =
  **NUMERICAL** · pending-review`, one rung *above* what is displayed. Conservative, so nothing
  downstream is over-claimed, but the record is internally inconsistent.
- **D-5 (`lean/README.md` L123, THE ONE NON-CONSERVATIVE DEFECT).** *"the sources hold 276
  `theorem`/`lemma`s (377 declarations, plus 96 `example` witnesses), and the ~80 unprinted ones are
  helper lemmas"*. Disk (comment-stripped count, §2.3): **401 `theorem`+`lemma`, 569 named
  declarations, 127 `example`s**, and **268 distinct names printed**, i.e. **~133 unprinted**. As
  printed the sentence is internally inconsistent (283 printed > 276 theorem/lemmas reads as total
  coverage) and understates the unprinted set by ~53. The census itself remains **sound** — every
  unprinted lemma I sampled is a transitive dependency of a printed result — but the *stated*
  coverage is too favourable. **This is the only place in the delta where the record errs toward
  over-statement.**
- **D-6 (campaign ledger, minor).** The `CAMPAIGN CLOSED (2026-07-31)` section's list of *"What
  remains is deliberately OUT of this campaign"* is not annotated for the items batches 1 and 2
  subsequently closed (only the manuscript-repair item is struck through) — it still names FILT,
  JOINTLP dual certificates, tilted-band witness, orientation (51), block (iii) `ρ` derivation,
  `prop:embed`, B2 `DonorClaim` `k`-uniformity and the B1 route proof as open. The two later sections
  supply the correction chronologically, and the ledger is append-only by design, so a reader going
  top-to-bottom is not misled; a reader of that section alone is.

**Is the two-batch/CAMPAIGN-CLOSED sequence itself consistent?** Structurally yes: both batches are
recorded *below* the closure with their own dates, DONE/RESISTED verdicts, build figures and "Owed
next" lists, and both explicitly state "no status changed anywhere; no `git` command run". The only
defect is D-6's un-annotated list.

**HONESTY VERDICT: FAIL — on record-accuracy, not on scope-overstatement.** Seven defects; six err
in the conservative direction (the record claims *less* than the disk delivers) and one (**D-5**)
over-states axiom-census coverage. As in the prior round, **the load-bearing §7.10(6) question —
does any wording imply a theorem is verified where only a relative composition was checked? — is
answered NO**, and the new modules are, if anything, more scrupulous than required.

---

## 8. DF-8 — RESIDUAL AUDIT (every resisted item must be a named residual somewhere durable)

| Resisted / not-reached item | Batch | Named where | verdict |
|---|---|---|---|
| pair-tensor lift: `ℤ_q` pair-orientation + non-injective labeled→occupancy pushforward | L-1, H-4(a) | `KSUM.B4b.L2.M1`, `KSUM.B4b.L2.FILT`, census "explicitly open" ¶, module header | **named** |
| `S_N`-average operator (convolution reduction) | L-2 → H-4(b) | `FactorialFiltration.lean` header, `KSUM.B4b.L2.BANDMULT`, census | **named** |
| block clause (i): `m`-fold multivariate Vandermonde | L-3, H-3 | `ObstructionsBlock.lean` docstring, `KSUM.B4b.L2.T4`, census | **named** |
| block-module design decision (`X j = A^{N_j}`) | L-3 escalation, H-3 | `KSUM.B4b.L2.T4.yaml` L83 (*"a module design decision, still a lead call"*) | **named** |
| `prop:rosmanis`(1) bijection + `Σ_f p_{≤m}(N−f)`; part (2) rep sentence; `C(σ) ≅ (C₂≀S_m)×S_τ` | L-5, H-7 | `KSUM.LEAN.T2`, `KSUM.ROSMANIS`, census (three rows + the open ¶) | **named** |
| tilted-band: inner pair tensor as a measure on `ℤ_q^N` (⇒ (43) identification) | H-1 | `ObstructionsTiltedBand.lean` header, `KSUM.B4b.L2.L2P3`, census | **named** |
| ORIENT: named-construction genPoly ↔ phase-function identification | H-2 | `ObstructionsOrientation.lean` header, `KSUM.B4b.L2.ORIENT`, census | **named** |
| `prop:embed`'s **encoding identity** | H-5 | `Support/Embed.lean` header, `lean/README.md` L114, `KSUM.A2.yaml` L174 | **named — but ACTIVELY CONTRADICTED by the census (C-1)** |
| the other 18 `prop:joint-lp` LPs (JSON-certified, not kernel-checked) | H-6 | `JointLP.lean` header, `KSUM.B4b.L2.JOINTLP` `rel`, `lean/README.md`, census | **named** |
| **F-LP-1** (sympy dual infeasibility) | H-6 | `KSUM.B4b.L2.JOINTLP.yaml` L87–94, batch report §7.3 | **named** |
| the `A1 → B1` edge decision | L-7 | `KSUM.B1.yaml` composition `claim` + `reason`, `B1.lean` header | **named** |
| the `oabarrier`(ii) `Q = 0` clause (still unstated in Lean) | pre-delta, still open | `KSUM.LEAN.T1` caveat + prior review §10 | **named**, but invisible in the census row (m-4) |

**DF-8 VERDICT: ALL NAMED — no silent drops.** One item (`prop:embed`'s encoding identity) is named
in three durable places and simultaneously *denied* by the census; that is a census error (C-1), not
a dropped residual.

---

## 9. THE `KSUM.B1` ROUTE-ENTRY CORRECTION — **FAITHFUL**

The gap-closure finding was: (a) `KSUM.A1.Claim` (= `A1d`'s numeric floor on `Q(kSum)`) does **not**
imply `KSUM.B1.Claim` (a statement about `Q(Claw)`); (b) the route that runs is from A1's own three
children; (c) repairing the graph is a lead call.

The node now records exactly that. Its A1 composition entry reads *"A1's INPUT SUBTREE (A1a…, A1b…,
A1c…) implies B1. [CORRECTED 2026-07-31 … the prior claim 'A1 implies B1' is FALSE at the Claim
level …]"*, cites `composition_via_A1_inputs` as the machine-checked route, and notes that
`composition_via_A1` is declared per §7.4 with its hypothesis explicitly not consumed. The `reason`
field carries the graph decision in full: *"A1a/A1b/A1c are not B1's children — they enter via A1's
subtree, recorded here as the §1-permitted explicit premise list rather than by rewiring edges
(rewiring would make A1 and B1 siblings over the same children and double the composition
obligations for zero gain)."*

**Three checks:**

1. **Is the premise hidden in prose (§1's prohibition)?** No. §1 forbids a premise being *"hidden
   only in prose"* and requires it to be a child, a cited interface, or an explicit relative
   hypothesis. Here A1a/A1b/A1c are the **antecedents of the composition claim itself** — the claim
   is literally "A1a ∧ A1b ∧ A1c ⇒ B1". That is the strongest of the three positions, not a
   loophole.
2. **Is the induced propagation sound?** Yes, and conservative. `KSUM.A1` is an AND node, so
   `status(A1) = min(composition, A1a, A1b, A1c) ≤ min(A1a, A1b, A1c)`. The OR recompute at B1 uses
   `min(status(A1), route)`, which therefore never exceeds `min(min(A1a,A1b,A1c), route)` — the
   value the corrected claim would give. **Using `A1` as the propagating child under-estimates; it
   cannot over-promote B1.**
3. **§7.6 check 5 (`composition_via_*` matches children exactly).** `lean.composition` declares
   `["composition_via_A1"]` against `children = [L11, L12, A1]`, with L11/L12 recorded `lean: none`
   for a stated reason (both REFUTED·DEAD). `proof_dag_check --problem ksum` exits 0 (142 nodes).
   On disk `B1.lean` additionally declares `composition_via_A1_inputs`, which the checker does not
   see because it compares against the declared list rather than scanning the module. **Not a
   defect** — the extra declaration is documented on the node and in the module header — but worth
   recording as an observation about the checker's reach.

**VERDICT: the correction faithfully implements the gap-closure finding.** The residual defect is
D-4 (the node's `status_source` and "Current status" text still say the route proof is unwritten,
and the displayed status sits one rung below its own composition entry).

---

## 10. DF-9 — CENSUS VERIFICATION, ROW BY ROW

`ksum/artifacts/ksum_lean_census_20260731.md` is the discharge object of `KSUM.LEAN`'s restated
composition claim, so it is checked mechanically and semantically.

### 10.1 Mechanical checks — all PASS

- **166 declaration names** named by the census or by the two delta queues were checked against a
  comment-aware parse of all 37 sources: **0 missing**.
- **29 LaTeX labels** named in the census were checked against `\label{…}` in
  `ksum_small_alphabet.tex`: **0 absent**.
- Every state word is drawn from the census's own declared vocabulary.

### 10.2 Substantive corrections (4)

**C-1 — `prop:embed | proved-uncond` is WRONG.** The row credits `genEmbed` to `prop:embed`.
`prop:embed` is the **encoding identity** `kSum_{ℤ_q,0,kn}(encoded) = Coll_{k,n→R}(g)`. `genEmbed`
proves that the manuscript's parameter display satisfies `EmbedData`'s fields — that is
**`lem:embed`'s data**, at full generality. The identity is `KSUM.A2a.Claim`/`KSUM.A2b.Claim`, and
both are `def Claim : Prop` with **no proving theorem anywhere in the development** (verified by
declaration scan; the composition-layer row correctly lists A2a/A2b as `stated`). Under the census's
own vocabulary, `proved-uncond` = "kernel-proved" — which the encoding identity is not.
**Repair:** move `genEmbed` to the `lem:embed` row; set `prop:embed` to `stated` (or `partial`) with
the note *"parameter display + all `EmbedData` fields proved for every `k ≥ 3, n ≥ 1, R ≥ 2`
(`genEmbed`); the encoding identity itself is `KSUM.A2a`/`A2b`'s Claim and is NOT formalized"*. Note
that `lean/README.md` L114 and `Support/Embed.lean`'s header both state this correctly — the census
is the only place that gets it wrong, and it is the place that discharges a composition claim.

**C-2 — `lem:embed-allt` is a DECLARED T2 target and has NO row.** `KSUM.LEAN.T2`'s Scope section
names the target list verbatim: *"The combinatorial core-validity conditions (`lem:core`,
`prop:core-even`, `lem:core-odd`, `lem:transl-cover`, `prop:embed`, `lem:embed-allt`) … are the real
target here."* The census's T2 table has no `lem:embed-allt` row. The work exists and the prior
review graded it **FAITHFUL** in two halves (`KSUM.A2.coprime_k_q` for the gcd half;
`nsmul_surjective` + `KSUM.A1c.Q_le_of_coprime` for the translation half), so this is a missing row,
not missing work — **but it falsifies the census's scope-identity verdict sentence as written**
(*"no declared target is silently absent"*).

**C-3 — `prop:joint-lp`'s "6 kernel-checked (decide rows 1+3 of (39))" over-states.** Per §6.4:
(a) `(5,4,1)` single `= 2` needs `opt(deg 2) > 2/3`, which is **not** among the six — the six give
only `≤ 2`; (b) every "largest `d`" reading additionally needs the optima to be non-increasing in
`d`, which is argued in a docstring and is **not** a Lean theorem. **Repair:** *"6 kernel-checked:
`(3,3,0)` single `= 0` and joint `= 2` and `(5,4,1)` joint `= 3` decided (modulo the unformalized
monotonicity of the optimum in `d`); `(5,4,1)` single bounded above by 2, its matching half
JSON-certified only."*

**C-4 — `thm:kfloor` has no row under its own LaTeX label.** It is named in `KSUM.LEAN.T2`'s Claim
(*"`prop:rosmanis` part (1) … and `thm:kfloor` … are formalizable"*). The census's T2 table lists
only its constituent lemmas; the theorem is accounted for solely through the composition-layer rows
(`KSUM.A1 | proved-rel`, `A1d | stated`). Given that the census's promised format is *"LaTeX label →
tier → module → state"*, the label is owed a row (state: `partial` — `KSUM.A1.composition`/`holds`
proved-rel, the assembled statement `A1d.Claim` stated, plateau NARROWER under the `q ≤ C_kN`
ceiling).

### 10.3 Minor corrections (4)

- **m-1.** `prop:core-even` and `lem:core-odd` are listed `proved-uncond` with no mention of the
  **three declared narrowings** the prior review recorded and this review re-confirms (target range
  is the `k`-element sub-window `[t₀,t₀+k)`, not all of `W_even`; the modulus hypothesis used is the
  stronger odd-case one; the conclusion is `2Sum` at `0`, one `lem:encode` step short of `Claw`).
  The `lem:core` row *does* declare its narrowing — the practice should be uniform.
- **m-2.** `thm:product-obstruction | proved-uncond` omits the declared modelling caveat (condition 1
  — "NO is the all-axis event" — enters as the hypothesis `hNO`), which the prior review recorded.
- **m-3.** `thm:orientation-obstruction`'s note *"(51) produced end-to-end … `corr ≤ 1/8` (even) /
  `≤ 1/2` (odd) **outright**"*. Two softenings owed: the four links are individually kernel-checked
  but **not composed into a single declaration** (the chain is assembled in prose), and the `corr`
  bounds are conditional on `hnum` and `hZ`, so "outright" should read *"from the paper's own
  structural facts about the construction"*.
- **m-4.** `thm:oabarrier | proved-rel | (i)+(ii); constancy form` does not surface that clause
  **(ii)'s `Q = 0` conclusion is still not stated in Lean** (no `oabarrier_kSum_Q`; verified — the
  only `Q`-valued oabarrier theorem is `oabarrier_ED_Q`, which is clause (i)). That is a live prior
  caveat and belongs in the row.

### 10.4 Rows verified accurate (no change)

T1: `lem:encode`, `lem:shift`, `lem:oddN`, `thm:main-odd`, `thm:main-general`, `cor:threshold`
(including the v5.2 alignment note), `thm:k2-upper` (declared exclusion).
T2: `lem:core`, `lem:transl-cover`, `lem:embed` (data), `prop:rosmanis`(1)(2)(3), the `C(σ)` row.
T3: `lem:factorial-filtration`, `thm:pair-tensor`, **`thm:tilted-log-band`** (its note is precise and
matches my verdict row-for-row), `lem:band-multiplication`, `thm:product-obstruction` (modulo m-2),
`thm:block-obstruction` (accurate), `prop:transfer-facts`, the β1 row.
Composition layer: `KSUM.A1`, `KSUM.A2`, `KSUM.B1`, `KSUM.B2`, `KSUM.B4`, **`KSUM.B4a | stated |
faithful incl. `q ≥ 2``** (verified), `KSUM.goal`, the leaves row, and the no-module row (`KSUM.B3`
confirmed `REFUTED`/`PARKED` on disk).

### 10.5 Scope-identity verdict — the paragraph the composition claim rests on

> *"Every label in T1/T2/T3's **declared target lists** appears above with a Lean artifact at
> `partial` or better — no declared target is silently absent…"*

**As written, NOT JUSTIFIED**: `lem:embed-allt` (C-2) and `thm:kfloor` (C-4) are declared targets
without rows, and `prop:embed`'s row asserts a state the disk does not support (C-1). I verified the
three tier target lists directly against their node files:
T1's Claim names 7 labels — **all 7 present**;
T2's Claim + Scope name `prop:rosmanis`(1)(2), `thm:kfloor`, and six core-validity conditions —
**7 of 9 present**;
T3's target table names 9 labels — **all 9 present**.

**With C-1 through C-4 applied, the scope-identity paragraph becomes true and the census does
discharge the composition obligation.** Until then it does not, and per the commission's own framing
this **blocks promotion of `KSUM.LEAN`'s composition above CONJECTURED**.

**CENSUS VERDICT: CORRECTIONS (C-1, C-2, C-3, C-4; m-1 … m-4).**

---

## 11. RULE-7 RECORD (7a–7g, applied to the delta)

- **(7a) Type audit.** Every displayed identity ruled on above was typed. Specifically:
  `factorial_filtration`'s `μ : (Fin N → A) → ℚ` over `A : Type` with `[Fintype A] [DecidableEq A]`
  and `α : A → ℕ`, `rowOrder α = ∑_a α_a` — domains and codomains match (38) with `A = ℤ_q`;
  the `(N)_m` factor is `Nat.descFactorial` cast to ℚ and appears on the *left*, so the identity is
  unconditional and no division is hidden. `KSUM.B4a.Claim`'s exponents are `Real.rpow` (forced by
  `ε : ℝ`), **not** `Monoid.npow` — no ℕ-truncation of `1/2` or `1/4`. `KSUM.B1.Claim`'s
  `(k^2-2)*K+2*k-1` is ℕ-truncated subtraction but the minuend is `≥ 2` for `k ≥ 3`, so it equals
  the intended value. `genEmbed`'s two ℕ-divisions are replaced by the geometric sums they
  abbreviate, so truncated subtraction never enters a claim. `blockFourier`'s `A^{r−k}` uses ℕ
  subtraction, guarded by the hypothesis `k ≤ r`. `orientation_*`'s exponents are `zpow` over ℤ,
  so the negative exponents of (51) are genuine.
- **(7b) Regime-complete gates.** The multiplicity-style branches here are the parity/branch splits,
  and each is exercised at the **identity** level, not aggregate: `core_reduction_at` witnessed at
  both `m = k−2` (even) and `m = k−1` (odd, parked) **and** at both `r = 1` and the tight
  `r = k−1 = 2`, each with a positive and a negative instance; `endpoint_even`/`endpoint_odd`
  witnessed at the smallest legal `s` of each parity, with the odd bound shown tight;
  `orientation_corr_le_half_even/odd` witnessed tight at `r = m = 2`; `KSUM.B1` witnessed on both
  the `m = k−2` and `m = k−1` split branches (`N = 11` and `N = 10`). **Untested regimes named:**
  the `relabel` factor-2 slack is exercised by no witness model (both `demoModel` and
  `sandwichModel` satisfy it with constant 1); the 18 non-kernel-checked LPs; `q` even in the B4
  sandwich (excluded by design).
- **(7c) Anchoring ban.** Eleven worksheets in §3.A, all written from the Lean source before the
  `.tex` was opened; batch reports and the census read **last**. Two coincidences disclosed in §3.C.
  Four verdicts (rows 6, 14, 20, 29) rest on arithmetic I re-derived by hand or in exact code before
  comparing (the `4/3`-vs-`25/19` gap, the (51) exponent identity, `c_P = k(k−1)2^{k−2}`, the
  satellite dictionary), and **row 6 produced a finding the executors did not report as such**.
- **(7d) No frozen-input immunity.** Nothing was taken as frozen on the strength of the prior
  review. I re-ran the build, recounted the axiom census from my own log, re-derived the interface
  field table against v5.2 (which the prior review could not have seen), and re-verified the
  `KSUM.B4a` `q ≥ 2` repair and the `KSUM.B2` retype in their new forms. Where I lean on the prior
  review — `lem:embed-allt`'s two FAITHFUL halves (C-2) — I name the scope of that reliance.
- **(7e) Failure-mode diversity.** Checked, beyond the last war: **dropped normalization** — the
  `(N)_m` factor (present, load-bearing) and the `/2` on the pair-class LP rows (a legitimate row
  scaling, which cannot change feasibility since `y` absorbs it); **hypotheses smuggled into
  definitions** — `blockFourier_eq`'s four hypotheses are properties of the construction, not the
  conclusion, and `hident` is the paper's own equation, not a numeric assumption (both were the
  commission's designated hard checks and both pass); **undefined terms of art** —
  "query polynomial" (resolved by the module's DEFINITIONAL NOTE), "block label" (now resolved in
  the paper's own statement), "nontrivial satellite" (resolved to (52) and proved equivalent);
  **colored-orbit sums substituted for full sums** — the JointLP rows are orbit *averages* over the
  value-relabeling orbit of `α`, which I rebuilt from scratch and matched; **numerics validating
  values while the derivation is broken** — see (7f).
- **(7f) Value-vs-formula decoupling.** Stated per family. §3.B's "verified" column distinguishes
  statement-and-proof-read from statement-only. For **JointLP** specifically: the kernel exercises
  the **proved formula** (the certificate scheme applied to the literals); *separately*, I built the
  LP data independently from the manuscript's recipe and it agreed, and *separately again*, I
  re-solved every optimum without touching the duals. Those are three different objects and the
  report says which is which. For the **tilted band** and **ORIENT**, what is machine-checked is the
  *arithmetic chain*, not the existence statement about a measure on `ℤ_q^N` — the modules say so and
  I confirm it.
- **(7g) Quantifier hygiene.** Every term of art in a ruled statement resolves: "query polynomial"
  → `FactorialFiltration`'s DEFINITIONAL NOTE + `annihilates_query_of_occ_moments`; "pure high
  degree" → `ObstructionsCore.PureHighDegree`; "block label" → the paper's v5.2 statement sentence;
  "nontrivial `H`-satellite" → (52) in the paper, `InNontrivialSatellite` in Lean, **with the bridge
  now proved**; "certified degree" → `CertifiesAt` + the paper's own cut-off sentence; "at least
  five complementary pairs" → `m ≥ 2` via `m = 1+⌊log₅r⌋`. **One term still resolves only by
  convention:** the census's state word `proved-uncond`, which its own vocabulary defines as
  "kernel-proved" but which rows m-1/m-2 use where a *narrowed* statement is what was proved — the
  vocabulary conflates provenness with fidelity, and C-1 is the failure that conflation produced.

---

## 12. RECOMMENDED ACTIONS FOR THE LEAD (no status is written by this review)

1. **Census repair (blocking).** C-1 … C-4 plus m-1 … m-4. Until C-1/C-2/C-4 land, the
   scope-identity paragraph is false as written and `KSUM.LEAN`'s composition cannot rise above
   CONJECTURED on this discharge object.
2. **F1/F2 desync sweep (D-1, D-2).** Seven Lean files still call facts (iii)/(iv) "not in the
   manuscript". The standing conditionality statement should be restated repo-wide as
   *"conditional on ABI21 + Tani24 + `sec:prelim` facts (i)–(iv)"* — a strictly better position than
   the record currently claims. Same batch: `Trust.lean`'s "none of them is proved here" for
   `EmbedData`.
3. **Re-grade `KSUM.LEAN.T3`'s frontmatter caveat (D-3)** using §3.B rows 8, 9, 14, 29, and refresh
   the M-10 sentence that still calls (51) a hypothesis (D-3′).
4. **`KSUM.B1` record (D-4):** the route proof is written; the node says it is not, and the displayed
   status sits one rung below its own composition entry (`NUMERICAL · pending-review` is what §1
   computes).
5. **README census denominators (D-5)** — the one over-statement in the delta: 401 theorem/lemma,
   569 named declarations, 127 examples, 268 distinct printed, ~133 unprinted.
6. **Two cheap closures worth their cost:** a Lean lemma that the LP optimum is non-increasing in `d`
   (three lines; it is what makes every (39) verdict a decision — C-3(b)), and
   `opt_s541_single_d2` (closing C-3(a) and making "rows 1 and 3 decided" true).
7. **A manuscript finding worth a sentence:** the printed justification of `C_h ≤ 25/19` in
   `thm:tilted-log-band` does not yield `25/19` — flat Weierstrass gives only `4/3`. The bound holds;
   the paper needs the `d = 1`-peeled form the Lean uses (§3.B row 6). This is a **new** finding, not
   on any existing repair list.
8. **Still open from the prior round:** `oabarrier_kSum_Q` (one line), and the `A1 → B1` edge
   decision (the current explicit-premise recording is faithful and conservative — my recommendation
   is to keep it and close the item).

---

**Counting unit** for the tally: one row per (Lean statement-group × LaTeX target) ruled on in §3.B
— 21 FAITHFUL, 7 NARROWER, 1 WIDER, 0 DIVERGENT, 1 declared NOT-FORMALIZED, 2 infrastructure/witness
(32 rows).

`DELTA-FIDELITY: build 0/3017 | census 283/283 lines (268/268 distinct names) at the three standard axioms, zero holes | new-statement verdicts F 21 / N 7 / W 1 / D 0 (+1 declared-unformalized, +2 infra) | paper-delta re-grades: freeze NOT-A-CLAIM→FAITHFUL (fact iii), constQ NOT-A-CLAIM→FAITHFUL (fact iv), restrict NARROWER-now-disclosed, cor:threshold F6+F7 discharged, c-dependence exact match, block-label 7g resolved, B4a WIDER→FAITHFUL, thm:kfloor plateau NARROWER unchanged | M-10 honest (one stale under-statement: the "(51) enters as a hypothesis" clause) | JointLP verified three ways — all 4 lp_optimum goals re-checked in exact rationals from the Lean literals, all 6 optima independently re-solved by exact vertex enumeration without the duals, and the (3,3,0) + (5,4,1) objective vectors and (3,3,0) moment matrices independently reconstructed from the manuscript's recipe and matched | F-LP-1 reproduced (sympy 1.13.1, fresh process: lpmin and linprog both return an infeasible point, objective 0 vs true 2/3) | residuals all named | census table CORRECTIONS: C-1 prop:embed is NOT proved-uncond (encoding identity unformalized; genEmbed is lem:embed's data), C-2 lem:embed-allt is a declared T2 target with no row, C-3 the six do not decide (5,4,1)-single and monotonicity in d is unformalized, C-4 thm:kfloor has no row under its label, plus m-1..m-4; scope-identity verdict NOT justified as written, justified after C-1/C-2/C-4 | B1-route fix faithful (and its propagation is conservative: status(A1) <= min over its three children) | honesty defects: D-1 freeze/constQ still "not in the manuscript" in 7 Lean files, D-2 Trust says EmbedData's fields are unproved, D-3 T3 caveat stale in 4 places (+D-3' M-10 (51) sentence), D-4 B1 status_source says the route proof is unwritten and the node sits one rung below its own composition entry, D-5 README census denominators stale AND over-stating coverage (401 not 276 theorem/lemma; ~133 unprinted not ~80), D-6 ledger CAMPAIGN CLOSED list un-annotated for what batches 1-2 closed`
