/-
`SE/Interface.lean` — the abstract carrier, and the CITED results the tier-1 assembly consumes.

This file contains no proofs. Everything is an explicit structure field.

Two structures live here.

* `SEFrame` is the **carrier**: at tier 1 there is no operator layer, so every operator norm,
  every representation-theoretic scalar, and the sector index set appear as abstract data.
* `SEFrame.Cited` collects the facts about that data which this development **assumes from
  elsewhere and does not reprove**: the adversary-bound framework (external literature) and the
  reviewed-proved analytic lemmas of `se/paper/se_explicit_witness.tex`.

  "A theorem proved against an abstract interface is exactly as strong as the results that
  interface cites, and not one notch stronger."

The four *unproved* obligations H1–H4 are NOT here; each lives in its own node module
(`SE/denom/Phi/legal/trace/t6.lean`, `SE/denom/Phi/legal/gram/interface.lean`,
`SE/denom/Phi/legal/omega/interface.lean`, `SE/denom/Phi/legal/sect.lean`) as a `def Claim`
consumed as an explicit hypothesis by `SE.denom.Phi.legal.tame.composition`.
-/
import SE.Support.Defs
import SE.Support.Hook
import SE.Support.Omega

namespace SE

/-- The abstract carrier of the tier-1 assembly.

Every field stands for an object of `se/paper/se_explicit_witness.tex` that tier 1 does
not construct.  Indices: `n` is the problem size (the alphabet is `q = 2n` throughout), `j`/`d` is
the alphabet defect, and `Sector n j` indexes the strict sectors `ξ = (κ,ν)` of eq:strict-sector
at level `j` (the Littlewood–Richardson multiplicity `c` is *inside* a sector, never a separate
index — see the uniformity note on `Cited`). -/
structure SEFrame where
  /-- The strict sectors `ξ = (κ,ν)` at defect `j`, paper eq:strict-sector. -/
  Sector : ℕ → ℕ → Type
  /-- Admissibility of a sector: `κ=(n-1-a,α)`, `ν=(n-b,β)` are partitions,
  `c^θ_{αβ} > 0`, and `n ≥ 3j` (paper, after eq:strict-sector). -/
  admissible : ∀ n j, Sector n j → Prop
  /-- `r_top(2n,j,θ) = q^j f^θ /(j! f^{(q-j,θ)})`, paper eq:rtop. -/
  rtopS : ∀ n j, Sector n j → ℝ
  /-- `ω = (1-p₀)/p₀` with `p₀ = f^{(q-j-1,θ)}/f^{(q-j,θ)}`, paper eq:parameters-can. -/
  omegaS : ∀ n j, Sector n j → ℝ
  /-- `B_θ(q) = binom(q,j) f^θ / f^λ`, paper eq:central-frame. -/
  btheS : ∀ n j, Sector n j → ℝ
  /-- `‖M_ξ‖`, the norm of the positive `c×c` multiplicity block `M_ξ = 𝔪_ξ(R* P_comp R) ⪰ 0`
  of paper eq:gcan2. -/
  mxiS : ∀ n j, Sector n j → ℝ
  /-- `‖𝖦_can^{λ,ξ}‖`, the canonical Gram norm of paper eq:gcan-def. -/
  gcanS : ∀ n j, Sector n j → ℝ
  /-- `‖C_{N,prob}‖`, the NO polar of paper §7. -/
  cnprobS : ∀ n j, Sector n j → ℝ
  /-- `‖C̃_{λ,ξ}‖`, the sector compression of the legal lower block. -/
  csectS : ∀ n j, Sector n j → ℝ
  /-- `ρ_j = max_{θ⊢j} r_top(2n,j,θ)`, paper eq:rtop.  Tier 2 no longer assumes anything
  quantitative about this field: `Cited.rho_isGreatest` ties it to the explicit hook product
  `SE.rtopHook` (as the genuine maximum) and the envelope of eq:rho-asymp is then PROVED
  (`SE/Support/RhoEnvelope.lean`). -/
  rho : ℕ → ℕ → ℝ
  /-- `Adv(SE(n,2n))`, the negative-weight adversary bound, paper eq:adv. -/
  adv : ℕ → ℝ
  /-- `‖Γ_n‖`, paper eq:witness-intro. -/
  gammaNorm : ℕ → ℝ
  /-- `max_i ‖Γ_n ∘ Δ_i‖`, the denominator of eq:adv. -/
  maskNorm : ℕ → ℝ
  /-- `‖D‖` for the diamond representative `D = Δ₁^leg ⋄ Γ_n` of paper eq:diamond-split. -/
  dNorm : ℕ → ℝ
  /-- `‖D_d‖`, the defect-`d` summand of paper eq:defect-D. -/
  blockNorm : ℕ → ℕ → ℝ
  /-- `‖X_d^L‖`, paper eq:xybounds. -/
  xNorm : ℕ → ℕ → ℝ
  /-- `‖Y_d^L‖`, paper eq:xybounds. -/
  yNorm : ℕ → ℕ → ℝ
  /-- `‖C_{d→d}‖`, the matched-defect `Φ` block, paper eq:phi-matched. -/
  cDiag : ℕ → ℕ → ℝ
  /-- `‖C_{d+1→d}‖`, the legal lower block, paper eq:omega-lower-global. -/
  cLower : ℕ → ℕ → ℝ
  /-- CARRIER DATUM (TIER 2b, 2026-08-17; node `SE.formal.t2`).  The first row length `θ₁` of the
  sector's own shape `θ ⊢ j`: a sector `ξ = (κ,ν)` of paper eq:strict-sector is built inside a fixed
  `λ = (q-j,θ)`, so `θ` is part of the sector datum.  Tier 1 could keep `θ` implicit because every
  fact about `r_top` and `ω` was assumed; tier 2b PROVES those facts from `θ`, so `θ` must be
  visible.  It is DATA, not an assumption. -/
  shapeLen : ∀ n j, Sector n j → ℕ
  /-- CARRIER DATUM (TIER 2b): the conjugate `θ'` of the sector's shape, in the coordinates of
  `SE.IsColumnData` (`shapeCol n j s i = θ'_{i+1}`).  Companion of `shapeLen`. -/
  shapeCol : ∀ n j, Sector n j → (ℕ → ℕ)

namespace SEFrame

variable (F : SEFrame)

/-- The results this development **cites and does not reprove**.

Every field names its manuscript label and, where the project's DAG owns the statement, the node
id and that node's status at the time of writing (2026-07-30).

*Uniformity note.* Every sector-indexed field below is quantified over ALL admissible sectors, and
a sector carries its own Littlewood–Richardson multiplicity `c ≥ 1`; the norms `mxiS`, `gcanS`,
`csectS` are norms of the whole `c×c` block, never of a chosen copy.  This is the paper's
"uniformly for every Littlewood–Richardson multiplicity `c ≥ 1`". -/
structure Cited : Prop where
  /-- **Adversary bound** (external: Høyer–Lee–Špalek 2007; Lee–Mittal–Reichardt–Špalek–Szegedy
  2011), paper eq:adv: `Adv(F) = max_Γ ‖Γ‖ / max_i ‖Γ∘Δ_i‖`.  Only the `≥` half is used. -/
  adv_ge : ∀ n, 0 < F.maskNorm n → F.gammaNorm n / F.maskNorm n ≤ F.adv n
  /-- **Numerator** — paper Lemma `lem:numerator`, `‖Γ_n‖ ≥ K`.
  Node `SE.br.num`, status PROVED (2026-07-30). -/
  numerator : ∀ n, (K n : ℝ) ≤ F.gammaNorm n
  /-- The masked denominator is nonzero for `n ≥ 1` (the `k=0` atom has a nonzero masked row;
  `se/reviews/se_cor16_certification_20260723.md` §"Independent-construction checks" computes it
  exactly as `(2n-1)/(2n)`). -/
  maskNorm_pos : ∀ n, 1 ≤ n → 0 < F.maskNorm n
  /-- **Mask-from-`D`** — paper eq:diamond-two + eq:mask-from-D, together with the half-swap
  transitivity of paper §9 that makes `i = 1` the maximum over query positions:
  `max_i ‖Γ_n ∘ Δ_i‖ ≤ 2‖D‖`. -/
  mask_from_D : ∀ n, F.maskNorm n ≤ 2 * F.dNorm n
  /-- **Cross-defect orthogonality** — paper eq:phi-regroup + eq:defect-D + eq:orth-max:
  `D = ⨁_d D_d`, hence `‖D‖ = max_d ‖D_d‖`.  Only the `≤` half is used.
  Stated for `n ≥ 1`, where the index set `{d : d < K n}` is nonempty (`K n ≥ 1`); at `n = 0` the
  unrestricted form would be unsatisfiable (a vacuous premise would force `‖D‖ ≤ B` for negative
  `B`) and would make the whole development vacuously true — see `SE/SelfTest.lean`. -/
  defect_orth : ∀ n, 1 ≤ n → ∀ B, (∀ d, d < K n → F.blockNorm n d ≤ B) → F.dNorm n ≤ B
  /-- **Triangle inequality inside `D_d`** — paper eq:defect-D,
  `D_d = β_d X_d^L + α_d Y_d^L + α_d C_{d→d} + α_{d+1} C_{d+1→d}`. -/
  block_triangle : ∀ n d, F.blockNorm n d
    ≤ |beta (K n) d| * F.xNorm n d + alpha (K n) d * F.yNorm n d
      + alpha (K n) d * F.cDiag n d + alpha (K n) (d + 1) * F.cLower n d
  /-- **Legal `X` bound** — paper Theorem `thm:xy`, eq:xybounds: `‖X_d^L‖ ≤ ρ_d`.
  Node `SE.denom.X`, status PROVED (2026-07-30). -/
  x_bound : ∀ n d, d < K n → F.xNorm n d ≤ F.rho n d
  /-- **Legal `Y` bound** — paper Theorem `thm:xy`, eq:xybounds: `‖Y_d^L‖ ≤ ρ_d √2 √(d/n)`.
  Node `SE.denom.Y`, status PROVED (2026-07-30). -/
  y_bound : ∀ n d, d < K n →
    F.yNorm n d ≤ F.rho n d * (Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ)))
  /-- **Matched-defect `Φ` bound** — paper eq:phi-matched with the ambient estimate
  eq:phiambient: `‖C_{d→d}‖ ≤ ρ_d ‖T_d‖ ≤ ρ_d √6/√(n-2d+1)`.
  Node `SE.denom.Phi.ambient`, status PROVED (2026-07-30). -/
  cDiag_bound : ∀ n d, d < K n →
    F.cDiag n d ≤ F.rho n d * (Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1))
  /-- **Defect-zero vanishing** — paper Lemma `lem:phi-diag`: "For `k=1` only defect 1 occurs,
  and `C_0 = 0`."  Hence both defect-`0` `Φ` blocks vanish. -/
  cDiag_zero : ∀ n, F.cDiag n 0 = 0
  /-- Companion of `cDiag_zero`: the lower block into defect `0` vanishes (`lem:phi-diag`). -/
  cLower_zero : ∀ n, F.cLower n 0 = 0
  /-- **Hook-length evaluation of `ρ_d`, in the `IsGreatest` form** (TIER 2, 2026-08-17, sharpened
  TIER 2b; node `SE.formal.t2`).

  This single DEFINITIONAL field replaced the three tier-1 analytic assumptions
  `rho_ge_one : 1 ≤ ρ_d`, `rho_le : ρ_d ≤ 1 + rhoConst·n^{-1/3}` and `rhoConst_nonneg`
  (tier-1 baseline: `git:f0d686a:se/lean/SE/Interface.lean`), which are now
  the PROVED theorems `SEFrame.Cited.rho_ge_one`, `SEFrame.Cited.rho_le` and the explicit
  constant `SE.rhoConst = 4` of `SE/Support/RhoEnvelope.lean` / `SE/Support/Hook.lean`; at tier 2b
  it also replaced `rtop_le_rho`, now the theorem `SEFrame.Cited.rtop_le_rho`.

  What it says.  For every `d < n`, `ρ_d` is the GREATEST element of the set
  `SE.rtopHookSet n d` of hook-product values `SE.rtopHook (2n) d θ₁ θ'` over the shapes `θ ⊢ d` —
  i.e. exactly paper eq:rtop's `ρ_d = max_{θ⊢d} r_top(2n,d,θ)`, both halves: `ρ_d` is one of the
  values (attainment) and `ρ_d` dominates all of them (maximality).  Tier 2a assumed only the
  attainment half; the maximality half is what `rtop_le_rho` needs, and `SE.rowShape` shows the
  maximum really is attained (`SE.isGreatest_rtopHookSet`), so the field is satisfiable.

  What it cites, exactly (nothing quantitative):
  * the Frame–Robinson–Thrall hook-length formula, applied to `λ = (q-d,θ)` — absent from
    Mathlib v4.31.0 (verified 2026-08-17: `YoungDiagram` exists, hook-length formula, Specht
    modules, Littlewood–Richardson and Pieri do not), hence cited, not proved;
  * that the maximum over the (finite, nonempty) partitions of `d` is attained.

  DECLARED SCOPE CHANGE vs tier 2a: the window is `d < n` (where `λ = (2n-d,θ)` is a partition and
  the hook product is defined) rather than `d < K n`; `d < K n → d < n`, so every tier-1/2a call
  site is covered, and the wider window is what the sector-level `rtop_le_rho` needs, since
  admissibility gives only `3j ≤ n`. -/
  rho_isGreatest : ∀ n d, d < n → IsGreatest (rtopHookSet n d) (F.rho n d)
  /-- **The admissibility window** (TIER 2b, DEFINITIONAL) — paper, before eq:strict-sector:
  admissible strict sectors are defined inside the standing setup `q = 2n`, `j = k-1 ≥ 1`,
  `λ = (q-j,θ)`, `θ ⊢ j`, and admissibility itself requires `n ≥ 3j`.  This field says only that:
  `1 ≤ j` and `3j ≤ n`.  It carries no estimate; it is the index-set fact that makes the hook
  evaluation of `ω` meaningful (at `j = 0` the manuscript's `ω` is `0`, not positive).  The
  downstream window of `tame.Claim`/`sect.Claim` is the same one (`SE/Trust.lean` §D7). -/
  admissible_window : ∀ n j s, F.admissible n j s → 1 ≤ j ∧ 3 * j ≤ n
  /-- **Hook-length evaluation of the sector scalars `r_top` and `ω`** (TIER 2b, DEFINITIONAL;
  node `SE.formal.t2`).

  This single field replaced the tier-1 assumptions `rtop_pos`, `omega_pos` and `omega_le` (the
  manuscript's "reviewed-proved range" eq:omega-range), which are now the PROVED theorems
  `SEFrame.Cited.rtop_pos`, `SEFrame.Cited.omega_pos` and `SEFrame.Cited.omega_le`
  (`SE/Support/Omega.lean`, `SE/Support/RhoEnvelope.lean`).

  What it says, for every admissible sector, with `θ` its own shape (`shapeLen`/`shapeCol`):
  * `θ` is a shape of `j` (`SE.IsColumnData`, i.e. `θ' ≥ 1` inside the first row, non-increasing,
    `Σθ'_c = j`) — the statement that the carrier data really is the conjugate of a partition;
  * `r_top(2n,j,θ) = SE.rtopHook (2n) j θ₁ θ'` — paper eq:rtop under the hook-length formula;
  * `ω = SE.omegaHook (2n) j θ'` — paper eq:parameters-can, `ω = (1-p₀)/p₀` with
    `p₀ = f^{(q-j-1,θ)}/f^{(q-j,θ)}` under the hook-length formula.

  Both evaluations are EQUATIONAL and definitional: they say what the manuscript's two scalars ARE,
  and nothing about how big they are.  What they cite is the same single external fact as
  `rho_isGreatest`: the Frame–Robinson–Thrall hook-length formula, here applied to `λ = (q-j,θ)`
  and to `λ⁻ = (q-j-1,θ)` (whose first-row hooks are the `h_c - 1`). -/
  sector_hook : ∀ n j s, F.admissible n j s →
    IsColumnData (F.shapeLen n j s) (F.shapeCol n j s) j
      ∧ F.rtopS n j s = rtopHook (2 * n) j (F.shapeLen n j s) (F.shapeCol n j s)
      ∧ F.omegaS n j s = omegaHook (2 * n) j (F.shapeCol n j s)
  /-- Positivity of the sector scalar `B_θ(q)` (a ratio of dimensions). -/
  bthe_pos : ∀ n j s, F.admissible n j s → 0 < F.btheS n j s
  /-- `M_ξ ⪰ 0` (paper eq:gcan2), so its norm is nonnegative. -/
  mxi_nonneg : ∀ n j s, F.admissible n j s → 0 ≤ F.mxiS n j s
  csect_nonneg : ∀ n j s, F.admissible n j s → 0 ≤ F.csectS n j s
  /-- Norms of the four channel blocks are nonnegative. -/
  xNorm_nonneg : ∀ n d, 0 ≤ F.xNorm n d
  yNorm_nonneg : ∀ n d, 0 ≤ F.yNorm n d
  cDiag_nonneg : ∀ n d, 0 ≤ F.cDiag n d
  cLower_nonneg : ∀ n d, 0 ≤ F.cLower n d

end SEFrame

end SE
