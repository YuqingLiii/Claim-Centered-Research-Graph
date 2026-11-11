import WHGAP.Interface
import WHGAP.Support.Entropy
import WHGAP.Support.Channel
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.Deriv.MeanValue

/-!
# `WHGAP.private-boundary` (P14) — the T2 flagship

* node id: `WHGAP.private-boundary`
* node file: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.private-boundary.md`
* epistemic status on disk (2026-07-30): **PROVED** at the R8-licensed scope.
* mechanization state: `proved` for the analytic core (`f_pos`, `argument_coincidence`,
  `prefactor_eq`/`prefactor_pos`, `Delta_closed_form_pos`); `stated` for `Claim`, with
  `Claim_of_delta_le` the T1 bridge, `rel`: the ensemble/Devetak step `Δ(x) ≤ P^{(1)}(Λ_x)`
  (the regularization step `P^{(1)} ≤ P` is then the cited interface field `lsd_devetak`).

## Frozen Claim (verbatim from the node file, `## Claim` section)

**Theorem (PROVED).** For every x in (0, 1/2),

  P^{(1)}(Lambda_x) >= Delta(x) = [(1-2x)(1-x)/(2-3x)] * f( (1-2x)/(sqrt2 (1-x)) )
                    >= (1-2x)^3 / (2(1-x)(2-3x)) > 0   nats,

with f(s) = (1+s)log(1+s) + (1-s)log(1-s), attained by the symmetric two-point ensemble
{1/2 : rho_eps + tX, 1/2 : rho_eps - tX} at eps = t = eps_c(x)/2 = (1-2x)/(2-3x), where
(rho_eps, X) is the frozen necessity witness of paper §5. Hence P(Lambda_x) > 0 there.

**Corollary.** {x in (0,1) : P(Lambda_x) = 0} = [1/2, 1) EXACTLY at PROVED tier; the
closed interval [1/2, 1] holds at CERTIFIED\* (the x = 1 endpoint inherits P4's cite-only
RK24 dependency; the paper's Lemma 4.1 self-complementarity argument covers it at
written-proof/external-review tier). **[PROVED at the stated scope]**

* frozen-claim SHA-256: `415bdc11d2a60d65716e8b8c23f8eb4e87ba63a00f3e708e815164f172a30aa9`

## Statement-fidelity note (G-L5)

Machine-checked here, outright and unconditionally:

1. `f_pos` — `f(s) > 0` for `0 < s < 1`, `f(s) = (1+s)log(1+s) + (1-s)log(1-s)`;
2. `argument_coincidence` — at `ε = t = ε_c(x)/2` the two Holevo arguments `u/b` and `v/e`
   are **equal**, both `= (1-2x)/(√2(1-x))`  (this is the executor's Lemma 3.2b, the exact
   coincidence that makes the whole theorem elementary);
3. `prefactor_eq` / `prefactor_pos` — `b(x,ε) - e(x,ε) = ε(1-x)`, hence `> 0`;
4. `Delta_closed_form_pos` — `0 < s*(x) < 1` and `Δ(x) = [(1-2x)(1-x)/(2-3x)]·f(s*(x)) > 0`
   for every `0 < x < 1/2`, with `Δ(x) = (b - e)·f(s*)` at the frozen parameter point;
5. `Delta_lower_bound` — the `(1-2x)³/(2(1-x)(2-3x))` bound, **unconditional since
   2026-08-01 (LEAN-3 WP-F)**: its former hypothesis `∀ s ∈ [0,1), s² ≤ f s` is now the
   proved `f_ge_sq` (Step 1b), so P14's analytic core carries no scalar hypothesis at all;
6. **(LEAN-2 WP-C, 2026-07-31)** paper **Lemma 7.1** itself — `chiB_collapse`
   (`χ(E,B) = b f(u/b)`) and `chiE_collapse` (`χ(E,E) = e f(v/e)`), where the two `χ`'s are
   *computed* as `S(avg) - ½ S(out₊) - ½ S(out₋)` from the explicit output matrices `outB`,
   `outE` via the real-symmetric von Neumann entropy of `WHGAP.Support.Entropy` (tier T3);
   and `Delta_eq_chi_diff` — `Δ(x) = χ(E,B) - χ(E,E)` at the frozen point `ε = t = ε_c(x)/2`.

**Not** machine-checked, and therefore the granularity loss of `Claim`.  **This note was
rewritten on 2026-07-31: the gap is now strictly smaller than it was.**  Previously the
whole displayed step

  "the symmetric two-point ensemble `{½ : ρ_ε + tX, ½ : ρ_ε - tX}` achieves
   `χ_B - χ_E = b f(u/b) - e f(v/e) = Δ(x)`, and `P^{(1)} ≥ χ_B - χ_E`"

was one opaque hypothesis (`hbridge` of `Claim_of_delta_le`).  Its *first* half — the entropy
collapse, i.e. everything strictly between the output matrices and `Δ(x)` — was proved on
2026-07-31 (item 6).  Its *second* half — the identification of `outB`/`outE` with the channel
outputs — was proved on 2026-08-01 by LEAN-3 WP-D.  **What is left, and only what is left:**

* **(i) the identification step — CLOSED 2026-08-01 (LEAN-3 WP-D).**  ~~`outB`, `outE` are
  *defined* by the displays of paper Theorem 5.2 / Lemma 7.1; there is still no channel, no
  Kraus set and no complementary map in this development, so "these matrices are
  `Λ_x(ρ_ε ± tX)` and `Λ^c_x(ρ_ε ± tX)`" is established outside Lean.~~  There **is** now a
  channel — `WHGAP.Support.Channel` builds the Kraus set and the padded complement — and
  `outB_eq`/`outE_eq` below prove entrywise, for both ensemble signs, that
  `Λ_x(ρ_ε + θX) = outB(α, b, u)` and `Λ^c_x(ρ_ε + θX) = outE(1−x, xε, e, −v)`.  This is
  residual (c) of `WHGAP/Trust.lean`, and it is **discharged inside Lean**; the older
  exact/symbolic gate G1 of `tools/whgap_lean2_wpc_check.py` is now a cross-check, not the
  evidence of record.  (Text corrected 2026-08-01, R13 m1: this header contradicted the
  section WP-D added 440 lines below it.)
* **(ii) Devetak's formula, applied to a valid ensemble.**  `P^{(1)} = max over ensembles of
  [χ(·,B) - χ(·,E)]`, applied to this one ensemble, is the cited external interface, and with
  it the *validity of the ensemble members* themselves: that `ρ_ε ± tX` are states (PSD, trace
  one) and that `|t| ≤ √2 ε` as `eq:ens` requires.  Nothing in Lean checks positivity of the
  inputs — `outB_trace`/`outE_trace` check trace-one of the two *averages* only — and the
  constraint `|t| ≤ √2 ε` is nowhere represented here; both are discharged in the manuscript
  (and spot-verified at the frozen point `ε = t = ε_c/2` by the R13 reviewer, gate R8d).
  Together these are the hypothesis `hdev` of `Claim_of_devetak`, stated with the *one-shot*
  `I.Pone` (R11 m4), the passage to the regularized `P` remaining the interface field
  `I.lsd_devetak`.

`Claim_of_delta_le` is retained unchanged as the general bridge; `Claim_of_devetak` is the
strictly weaker-hypothesis route that supersedes it for this witness.  The prose Claim's
`≥ Δ(x)` and its Corollary `{x : P = 0} = [1/2,1)` are still not derivable here: the
`[1/2,1)` half is `WHGAP.zero-capacity-application`'s business.

Also note what `vnEntropy` is **not**: it is `∑ negMulLog λᵢ` of a real symmetric matrix,
with no positivity, normalization or density-matrix structure attached (see the scope block
of `WHGAP/Support/Entropy.lean`).  `outB_trace`/`outE_trace` check trace-one for the two
averages, and nothing more is claimed.

## Append-only deviation record (derive-and-verify, commission LEAN-1)

* 2026-07-30 — every algebraic identity of the commission's design section 3 was re-derived
  independently (sympy cross-check, `artifacts/logs_whgap_lean_20260730/sympy_identity_check.log`)
  **before** formalization and all of them closed as stated.  In particular
  `b(x, ε_c/2) = (1-x)/2`, `e(x, ε_c/2) = x(1-x)/(2(2-3x))`, `u = (1-2x)/(2√2)`,
  `v = x(1-2x)/(2√2(2-3x))`, and both ratios equal `(1-2x)/(√2(1-x))`.  No discrepancy.
* 2026-07-30 — `Delta_lower_bound` is the one commissioned item **not** closed outright.  Its
  only missing ingredient is the elementary inequality `f(s) ≥ s²` on `[0,1)`, whose short
  proofs all need either a power series or a second-derivative monotonicity argument that did
  not fit the budget; per the commission ("NEVER use `sorry`; an unclosable obligation becomes
  an explicit hypothesis parameter") it is an explicit hypothesis of that one theorem and of
  nothing else.  It is *not* used by `Delta_closed_form_pos`, which is unconditional.
* 2026-07-30 (R11 m15) — **`hsq` is a FORMALIZATION gap, not a mathematical one.**  The
  manuscript's own `eq:fdef` series display, `f(s) = Σ_{k≥1} s^{2k}/(k(2k-1))`, has `s²` as its
  `k = 1` term, so `f(s) ≥ s²` on `[0,1)` is immediate in the prose and the paper does not
  treat it as an open step.  What did not fit the budget is the *Lean* proof (the series or a
  two-level derivative-monotonicity argument), so the obligation is carried as a hypothesis
  parameter here for formalization reasons only.
* 2026-07-30 (R11 MAJOR-1) — `blockA_trace_det` was **moved out of this module** to
  `WHGAP.«no-ascent-hierarchy»`.  It supports paper **Lemma 6.1 (`lem:exactspec`, §6)**, an
  ingredient of the positivity layer (P9/P3), not of the P14 private-boundary witness of
  §5/§7; it was mis-attributed to Lemma 7.1 and mis-filed here.  The identity itself was and
  is correct; only its attribution and placement changed (DAG protocol §7.3: anything used by
  only one node belongs in that node's module).
* 2026-07-30 (R11 m4) — `Claim_of_delta_le`'s bridge hypothesis was restated with `I.Pone`
  (was `I.P`), and the regularization step now goes through `I.lsd_devetak`.  The theorem is
  formally *weaker* than the old form and is the honest mirror of the prose; it also makes
  `lsd_devetak` an interface field that the checked content actually consumes.
* 2026-07-31 (LEAN-2 WP-C) — paper Lemma 7.1 formalized; `Claim_of_devetak` added.  Route
  deviation from the frozen commission, reported not silent: the commission's lemma (b) was
  "invariance under explicit **orthogonal** conjugation, `U Uᵀ = 1`".  That is delivered
  (`WHGAP.Support.vnEntropy_conj_orthogonal`), but the payoff does **not** use it, because
  the orthogonal diagonalizer of `!![b, u; u, b]` carries a `1/√2` and would drag
  `Real.sqrt 2` into every entrywise certificate.  Used instead:
  `vnEntropy_of_conj_diagonal`, which needs only a **one-sided rational inverse**
  `V * U = 1` — `U = !![1,0,0; 0,1,1; 0,1,-1]`, `V = !![1,0,0; 0,½,½; 0,½,-½]` (and the
  `4×4` analogue).  Strictly more general hypothesis, entirely rational certificates, same
  conclusion; both `U V = V U = 1` and `U D V = out` were pre-verified in exact sympy
  (gate G4 of `tools/whgap_lean2_wpc_check.py`).
* 2026-07-31 (LEAN-2 WP-C) — the commissioned core lemma (c), block-diagonal additivity at
  the explicit `2 ⊕ 2` level, is delivered in `WHGAP.Support.Entropy` as
  `vnEntropy_fromBlocks_add` + `vnEntropy_two_by_two_blocks`.  It is **not** on the payoff
  path: `outE` is a literal `4×4` in the paper's frame (index set `Fin 4`, not `Fin 2 ⊕ Fin 2`),
  and the single rational similarity handles it in one step.  Recorded as a *substitution*,
  not an omission — a reviewer wanting the block route should read those two theorems.
* 2026-08-01 (LEAN-3 WP-F) — **`hsq` is discharged and REMOVED.**  Append-only record of the
  removal: the hypothesis parameter `hsq : ∀ s : ℝ, 0 ≤ s → s < 1 → s ^ 2 ≤ f s` of
  `Delta_lower_bound`, carried since 2026-07-30 for formalization reasons only (see the two
  entries above), is now the **theorem** `f_ge_sq` of Step 1b, and `Delta_lower_bound` is
  restated with hypotheses `0 < x` and `x < 1/2` only.  Nothing else in the statement changed
  (same bound, same conclusion) and no other declaration in the tree consumed `hsq`, so this
  is a strict strengthening: any previous use `Delta_lower_bound h1 h2 hsq` becomes
  `Delta_lower_bound h1 h2`.  The corresponding row was struck from `WHGAP/Trust.lean`'s
  hypothesis census, with its own append-only removal note there.  Route actually used —
  reported, not silent: the commission's suggested template was "the `StrictMonoOn` derivative
  route that `f_pos` already uses"; `f_pos` in fact uses no derivative at all (it is the
  single-term Gibbs inequality `mul_log_gt`), so there was no template to reuse.  What was
  written instead is the two-level `monotoneOn_of_deriv_nonneg` argument described at Step 1b,
  through one shared private helper.  Elementary alternatives were considered and rejected on
  paper *before* any Lean was written: the Padé bound `log t ≥ 2(t-1)/(t+1)` (for `t ≥ 1`)
  together with `log t ≥ (t - 1/t)/2` (for `t ≤ 1`) yields only `f(s) ≥ s²/2 + s²/(2+s)`,
  which is strictly *weaker* than `s²` for every `s > 0` — both one-sided bounds lose at order
  `s³` whereas `f(s) - s² = s⁴/6 + O(s⁶)` — and `Real.log_le_sub_one_of_pos` alone yields only
  `f(s) ≥ 0`, which is exactly `f_pos`.  The inequality is tight Pinsker for a two-point
  distribution; no Pinsker inequality in a usable form was found in Mathlib v4.31.0.
-/

namespace WHGAP.«private-boundary»

open WHGAP WHGAP.Support

/-! ## Step 0 — the strict `a log a > a - 1` inequality -/

/-- For `a > 0`, `a ≠ 1`: `a - 1 < a log a`.  (Strict form of Gibbs' inequality for a single
term; obtained from `log t < t - 1` applied to `t = a⁻¹`.) -/
theorem mul_log_gt {a : ℝ} (ha : 0 < a) (ha1 : a ≠ 1) : a - 1 < a * Real.log a := by
  have hinvpos : (0:ℝ) < a⁻¹ := inv_pos.mpr ha
  have hinvne : a⁻¹ ≠ 1 := by
    intro h
    apply ha1
    have : (a⁻¹)⁻¹ = (1:ℝ)⁻¹ := by rw [h]
    rwa [inv_inv, inv_one] at this
  have h := Real.log_lt_sub_one_of_pos hinvpos hinvne
  rw [Real.log_inv] at h
  -- `h : -log a < a⁻¹ - 1`
  have hmul : a * (-Real.log a) < a * (a⁻¹ - 1) :=
    mul_lt_mul_of_pos_left h ha
  have hrw : a * (a⁻¹ - 1) = 1 - a := by
    field_simp
  rw [hrw] at hmul
  linarith

/-! ## Step 1 — `f_pos` (MUST-LAND) -/

/-- **`f_pos`.**  The binary Holevo function is strictly positive on `(0,1)`. -/
theorem f_pos {s : ℝ} (hs0 : 0 < s) (hs1 : s < 1) : 0 < f s := by
  have hA : (0:ℝ) < 1 + s := by linarith
  have hC : (0:ℝ) < 1 - s := by linarith
  have hAne : (1:ℝ) + s ≠ 1 := by intro h; linarith
  have hCne : (1:ℝ) - s ≠ 1 := by intro h; linarith
  have h1 := mul_log_gt hA hAne
  have h2 := mul_log_gt hC hCne
  unfold f
  linarith

/-! ## Step 1b — `f_ge_sq` (LEAN-3 WP-F, 2026-08-01): `s² ≤ f s` on `[0,1)`

This discharges the hypothesis `hsq` that `Delta_lower_bound` carried from LEAN-1 (R11 m15).
The route is the two-level derivative comparison announced in the deviation record: with
`g(s) = f(s) - s²` one has `g(0) = 0` and `g'(s) = log(1+s) - log(1-s) - 2s`, which is itself
the value at `s` of a function vanishing at `0` with derivative
`1/(1+s) + 1/(1-s) - 2 = 2s²/(1-s²) ≥ 0`.  Both levels are the same `MonotoneOn` step, so
they share the private helper `nonneg_of_deriv_nonneg` below.  No series expansion, no
second-derivative API, no `sorry`, no new hypothesis. -/

section FGeSq

open Set

/-- A function vanishing at `0` whose derivative exists on `(-1,1)` and is nonnegative on
`(0,1)` is nonnegative on `[0,1)`.  (Both levels of the `f_ge_sq` argument are instances.) -/
private lemma nonneg_of_deriv_nonneg {g g' : ℝ → ℝ} (hg0 : g 0 = 0)
    (hd : ∀ y : ℝ, -1 < y → y < 1 → HasDerivAt g (g' y) y)
    (hnn : ∀ y : ℝ, 0 < y → y < 1 → 0 ≤ g' y) :
    ∀ s : ℝ, 0 ≤ s → s < 1 → 0 ≤ g s := by
  intro s hs0 hs1
  have hmono : MonotoneOn g (Ico (0:ℝ) 1) := by
    refine monotoneOn_of_deriv_nonneg (convex_Ico 0 1) ?_ ?_ ?_
    · intro y hy
      exact ((hd y (by linarith [hy.1]) hy.2).continuousAt).continuousWithinAt
    · rw [interior_Ico]
      intro y hy
      exact ((hd y (by linarith [hy.1]) hy.2).differentiableAt).differentiableWithinAt
    · rw [interior_Ico]
      intro y hy
      rw [(hd y (by linarith [hy.1]) hy.2).deriv]
      exact hnn y hy.1 hy.2
  have h := hmono (left_mem_Ico.mpr one_pos) ⟨hs0, hs1⟩ hs0
  rw [hg0] at h
  exact h

/-- Level 1: `log(1+s) - log(1-s) ≥ 2s` on `[0,1)`.  (Derivative `2s²/(1-s²) ≥ 0`.) -/
private lemma log_diff_ge_two_mul {s : ℝ} (hs0 : 0 ≤ s) (hs1 : s < 1) :
    0 ≤ Real.log (1 + s) - Real.log (1 - s) - 2 * s := by
  refine nonneg_of_deriv_nonneg (g := fun z : ℝ => Real.log (1 + z) - Real.log (1 - z) - 2 * z)
    (g' := fun y : ℝ => 1 / (1 + y) + 1 / (1 - y) - 2) ?_ ?_ ?_ s hs0 hs1
  · simp
  · intro y hy1 hy2
    have h1 : (1:ℝ) + y ≠ 0 := ne_of_gt (by linarith)
    have h2 : (1:ℝ) - y ≠ 0 := ne_of_gt (by linarith)
    have hA : HasDerivAt (fun z : ℝ => Real.log (1 + z)) (1 / (1 + y)) y := by
      simpa using (((hasDerivAt_id y).const_add (1:ℝ)).log h1)
    have hB : HasDerivAt (fun z : ℝ => Real.log (1 - z)) (-1 / (1 - y)) y := by
      simpa using (((hasDerivAt_id y).const_sub (1:ℝ)).log h2)
    have hC : HasDerivAt (fun z : ℝ => 2 * z) (2:ℝ) y := by
      simpa using ((hasDerivAt_id y).const_mul (2:ℝ))
    have hsum := (hA.sub hB).sub hC
    -- R13 m9: the three later alternatives are reported "never executed" by the linter, and
    -- that report is DELIBERATELY KEPT — it is the evidence that this `congr_deriv` side goal
    -- was closed by the genuine rewrite `neg_div`/`sub_neg_eq_add`, i.e. that the stated `g'`
    -- is the derivative Lean actually computes and a mis-stated `g'` could not have survived.
    exact hsum.congr_deriv
      (by first
            | rw [neg_div, sub_neg_eq_add]
            | (field_simp; try ring)
            | (simp; try ring)
            | ring)
  · intro y hy0 hy1
    have h1 : (0:ℝ) < 1 + y := by linarith
    have h2 : (0:ℝ) < 1 - y := by linarith
    have hid : 1 / (1 + y) + 1 / (1 - y) - 2 = 2 * y ^ 2 / ((1 + y) * (1 - y)) := by
      field_simp
      ring
    rw [hid]
    exact div_nonneg (by positivity) (le_of_lt (mul_pos h1 h2))

/-- **`f_ge_sq` (LEAN-3 WP-F).**  `s² ≤ f s` for every `s ∈ [0,1)` — the `k = 1` term of the
manuscript's series display `eq:fdef`, now proved in Lean.  This is exactly the hypothesis
`hsq` that `Delta_lower_bound` used to carry; that theorem is now unconditional. -/
theorem f_ge_sq {s : ℝ} (hs0 : 0 ≤ s) (hs1 : s < 1) : s ^ 2 ≤ f s := by
  have key : ∀ z : ℝ, 0 ≤ z → z < 1 →
      0 ≤ (1 + z) * Real.log (1 + z) + (1 - z) * Real.log (1 - z) - z ^ 2 := by
    refine nonneg_of_deriv_nonneg
      (g := fun z : ℝ => (1 + z) * Real.log (1 + z) + (1 - z) * Real.log (1 - z) - z ^ 2)
      (g' := fun y : ℝ => Real.log (1 + y) - Real.log (1 - y) - 2 * y) ?_ ?_ ?_
    · simp
    · intro y hy1 hy2
      have h1 : (1:ℝ) + y ≠ 0 := ne_of_gt (by linarith)
      have h2 : (1:ℝ) - y ≠ 0 := ne_of_gt (by linarith)
      have hu : HasDerivAt (fun z : ℝ => 1 + z) (1:ℝ) y := by
        simpa using ((hasDerivAt_id y).const_add (1:ℝ))
      have hu2 : HasDerivAt (fun z : ℝ => 1 - z) (-1:ℝ) y := by
        simpa using ((hasDerivAt_id y).const_sub (1:ℝ))
      have hA : HasDerivAt (fun z : ℝ => Real.log (1 + z)) (1 / (1 + y)) y := by
        simpa using (((hasDerivAt_id y).const_add (1:ℝ)).log h1)
      have hB : HasDerivAt (fun z : ℝ => Real.log (1 - z)) (-1 / (1 - y)) y := by
        simpa using (((hasDerivAt_id y).const_sub (1:ℝ)).log h2)
      have hsq2 : HasDerivAt (fun z : ℝ => z ^ 2) (2 * y) y := by
        simpa using (hasDerivAt_pow 2 y)
      have hsum := ((hu.mul hA).add (hu2.mul hB)).sub hsq2
      -- R13 m9: same as in `log_diff_ge_two_mul` above — the two later alternatives are
      -- reported "never executed" and are KEPT, because that report is the evidence that the
      -- product-rule derivative had to be normalized to the stated `g'` by real work.
      exact hsum.congr_deriv
        (by first
              | (field_simp; try ring)
              | (simp; try ring)
              | ring)
    · intro y hy0 hy1
      exact log_diff_ge_two_mul hy0.le hy1
  have h := key s hs0 hs1
  unfold f
  linarith

end FGeSq

/-! ## Step 2 — the frozen parameter point `ε = t = ε_c(x)/2` -/

section FrozenPoint

variable {x r : ℝ}

lemma b_at (hx0 : 0 < x) (hx : x < 1 / 2) : b x (epsC x / 2) = (1 - x) / 2 := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h23' : (2 - x * 3) ≠ 0 := two_sub_x_three_ne hx0 hx
  unfold b epsC
  field_simp
  ring

lemma e_at (hx0 : 0 < x) (hx : x < 1 / 2) :
    e x (epsC x / 2) = x * (1 - x) / (2 * (2 - 3 * x)) := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h23' : (2 - x * 3) ≠ 0 := two_sub_x_three_ne hx0 hx
  unfold e epsC
  field_simp
  ring

lemma u_at (hx0 : 0 < x) (hx : x < 1 / 2) (hr : r ≠ 0) :
    u x (epsC x / 2) r = (1 - 2 * x) / (2 * r) := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h23' : (2 - x * 3) ≠ 0 := two_sub_x_three_ne hx0 hx
  unfold u epsC
  field_simp

lemma v_at (hx0 : 0 < x) (hx : x < 1 / 2) (hr : r ≠ 0) :
    v x (epsC x / 2) r = x * (1 - 2 * x) / (2 * r * (2 - 3 * x)) := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h23' : (2 - x * 3) ≠ 0 := two_sub_x_three_ne hx0 hx
  unfold v epsC
  field_simp

/-- **`argument_coincidence` (MUST-LAND).**  At `ε = t = ε_c(x)/2` the receiver-side and
environment-side Holevo arguments coincide exactly, both equal to `(1-2x)/(r(1-x))` with
`r = √2`.  This is a rational identity in `r`: it does **not** use `r² = 2`. -/
theorem argument_coincidence (hx0 : 0 < x) (hx : x < 1 / 2) (hr : 0 < r) :
    u x (epsC x / 2) r / b x (epsC x / 2) = (1 - 2 * x) / (r * (1 - x)) ∧
    v x (epsC x / 2) r / e x (epsC x / 2) = (1 - 2 * x) / (r * (1 - x)) := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h1x : (1 - x) ≠ 0 := one_sub_x_ne hx0 hx
  have hxne : x ≠ 0 := ne_of_gt hx0
  have hrne : r ≠ 0 := ne_of_gt hr
  have hden1 : ((1 - x) / 2 : ℝ) ≠ 0 := by
    intro h; apply h1x; field_simp at h; linarith
  have hden2 : (x * (1 - x) / (2 * (2 - 3 * x)) : ℝ) ≠ 0 :=
    div_ne_zero (mul_ne_zero hxne h1x) (mul_ne_zero two_ne_zero h23)
  have hden3 : (r * (1 - x) : ℝ) ≠ 0 := mul_ne_zero hrne h1x
  constructor
  · rw [u_at hx0 hx hrne, b_at hx0 hx, div_eq_div_iff hden1 hden3]
    field_simp
  · rw [v_at hx0 hx hrne, e_at hx0 hx, div_eq_div_iff hden2 hden3]
    field_simp

/-- **`prefactor_eq`.**  `b(x,ε) - e(x,ε) = ε(1-x)` identically (no side condition). -/
theorem prefactor_eq (x ε : ℝ) : b x ε - e x ε = ε * (1 - x) := by
  unfold b e
  ring

/-- **`prefactor_pos`.**  Consequently `b(x,ε) - e(x,ε)` is strictly positive for `0 < ε`
and `x < 1`. -/
theorem prefactor_pos {ε : ℝ} (hε : 0 < ε) (hx : x < 1) : 0 < b x ε - e x ε := by
  rw [prefactor_eq]
  exact mul_pos hε (by linarith)

end FrozenPoint

/-! ## Step 3 — `Δ` in closed form and its positivity (MUST-LAND) -/

section Delta

variable {x : ℝ}

/-- `0 < s*(x)` for `0 < x < 1/2`. -/
theorem sStar_pos (hx0 : 0 < x) (hx : x < 1 / 2) : 0 < sStar x := by
  unfold sStar
  exact div_pos (by linarith) (mul_pos (Real.sqrt_pos.mpr (by norm_num)) (by linarith))

/-- `s*(x) < 1` for `0 < x < 1/2`; the ring content is `(1-2x)² < 2(1-x)²`, i.e. `1 - 2x² > 0`. -/
theorem sStar_lt_one (hx0 : 0 < x) (hx : x < 1 / 2) : sStar x < 1 := by
  obtain ⟨hr, hr2⟩ := sqrt_two_spec
  have hA : 0 < Real.sqrt 2 * (1 - x) := mul_pos hr (by linarith)
  have hB : (0:ℝ) < 1 - 2 * x := by linarith
  have hsq : (1 - 2 * x) ^ 2 < (Real.sqrt 2 * (1 - x)) ^ 2 := by
    have hp : (Real.sqrt 2 * (1 - x)) ^ 2 = 2 * (1 - x) ^ 2 := by
      rw [mul_pow, hr2]
    rw [hp]
    nlinarith
  have key : 1 - 2 * x < Real.sqrt 2 * (1 - x) := by nlinarith
  unfold sStar
  rw [div_lt_one hA]
  exact key

/-- `Δ(x)` really is `(b - e) · f(s*)` at the frozen parameter point. -/
theorem Delta_eq_prefactor_mul (hx0 : 0 < x) (hx : x < 1 / 2) :
    (b x (epsC x / 2) - e x (epsC x / 2)) * f (sStar x) = Delta x := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h23' : (2 - x * 3) ≠ 0 := two_sub_x_three_ne hx0 hx
  unfold Delta
  rw [prefactor_eq]
  congr 1
  unfold epsC
  field_simp

/-- **`Delta_closed_form_pos` (MUST-LAND).**  For every `0 < x < 1/2`,
`0 < s*(x) < 1` and `Δ(x) = [(1-2x)(1-x)/(2-3x)] f(s*(x)) > 0` — unconditionally. -/
theorem Delta_closed_form_pos (hx0 : 0 < x) (hx : x < 1 / 2) :
    (0 < sStar x ∧ sStar x < 1) ∧ 0 < Delta x := by
  refine ⟨⟨sStar_pos hx0 hx, sStar_lt_one hx0 hx⟩, ?_⟩
  unfold Delta
  refine mul_pos (div_pos (by nlinarith) (by linarith)) ?_
  exact f_pos (sStar_pos hx0 hx) (sStar_lt_one hx0 hx)

/-- **`Delta_lower_bound`** — UNCONDITIONAL since LEAN-3 WP-F (2026-08-01).  The hypothesis
`hsq : ∀ s ∈ [0,1), s² ≤ f s` that this theorem carried from LEAN-1 (R11 m15) is now the
proved `f_ge_sq` of Step 1b; the statement is otherwise unchanged. -/
theorem Delta_lower_bound (hx0 : 0 < x) (hx : x < 1 / 2) :
    (1 - 2 * x) ^ 3 / (2 * (1 - x) * (2 - 3 * x)) ≤ Delta x := by
  obtain ⟨hr, hr2⟩ := sqrt_two_spec
  have h23 : (0:ℝ) < 2 - 3 * x := two_sub_three_x_pos hx0 hx
  have h1x : (0:ℝ) < 1 - x := one_sub_x_pos hx0 hx
  have hK : (0:ℝ) < (1 - 2 * x) * (1 - x) / (2 - 3 * x) :=
    div_pos (by nlinarith) h23
  have hs2 : (sStar x) ^ 2 = (1 - 2 * x) ^ 2 / (2 * (1 - x) ^ 2) := by
    unfold sStar
    rw [div_pow, mul_pow, hr2]
  have hstep : ((1 - 2 * x) * (1 - x) / (2 - 3 * x)) * (sStar x) ^ 2 ≤ Delta x := by
    unfold Delta
    exact mul_le_mul_of_nonneg_left
      (f_ge_sq (sStar_pos hx0 hx).le (sStar_lt_one hx0 hx)) hK.le
  have heq : ((1 - 2 * x) * (1 - x) / (2 - 3 * x)) * (sStar x) ^ 2
      = (1 - 2 * x) ^ 3 / (2 * (1 - x) * (2 - 3 * x)) := by
    rw [hs2]
    field_simp
    all_goals ring
  rw [← heq]
  exact hstep

end Delta

/-! ## T1 layer — the node Claim and its bridge -/

/-- **P14 Claim, tier-1 form.**  `P(Λ_x) > 0` for every `x ∈ (0, 1/2)`. -/
def Claim (I : CapacityInterface) : Prop :=
  ∀ x : ℝ, 0 < x → x < 1 / 2 → 0 < I.P x

/-- The T1 bridge: the analytic core discharges the Claim as soon as the (unformalized,
explicitly hypothesised) **one-shot** ensemble/Devetak step `Δ(x) ≤ P^{(1)}(Λ_x)` is granted.

This is deliberately the *honest* shape (R11 m4): the prose and `thm:private` prove the
inequality for `P^{(1)}`, and the passage to the regularized `P` is the cited interface field
`I.lsd_devetak` (superadditivity of the private information), which is therefore consumed here
rather than sitting unused in the trust boundary. -/
theorem Claim_of_delta_le (I : CapacityInterface)
    (hbridge : ∀ x : ℝ, 0 < x → x < 1 / 2 → Delta x ≤ I.Pone x) : Claim I := by
  intro x hx0 hx
  have hΔ : 0 < Delta x := (Delta_closed_form_pos hx0 hx).2
  have hone : Delta x ≤ I.Pone x := hbridge x hx0 hx
  have hreg : I.Pone x ≤ I.P x := (I.lsd_devetak x).2
  linarith

/-! ## Step 4 (LEAN-2 WP-C, 2026-07-31) — paper Lemma 7.1 in Lean

The two Holevo quantities of the symmetric two-point ensemble `E(ε,t)` of `eq:ens` are now
*computed* from the explicit output matrices, using the real-symmetric von Neumann entropy
layer `WHGAP.Support.Entropy` (tier T3, lead-authorized).  The matrices are the ones of
paper Theorem 5.2 / Lemma 7.1; that they are the actual outputs of `Λ_x` and `Λ_x^c` is the
sympy/mpmath gate G1 of `tools/whgap_lean2_wpc_check.py` (Kraus rebuild, entrywise, symbolic
in `x, ε, t`), not Lean — see the honesty note in the module header. -/

section Holevo

open Matrix WHGAP.Support

/-- **Receiver-side output matrix** `Λ_x(ρ_ε + tX)` of paper Lemma 7.1, in the frame
`(|0⟩, |1⟩, |2⟩)`: `diag(α)` on the untouched direction and the degenerate `{1,2}` block
`!![b, u; u, b]`.  The average `Λ_x(ρ_ε)` is the same expression at `u = 0`. -/
noncomputable def outB (α b u : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![α, 0, 0; 0, b, u; 0, u, b]

/-- **Environment-side output matrix** `Λ^c_x(ρ_ε + tX)` of paper Lemma 7.1: the
`(1-x)` direction, the `xε` direction, and the degenerate pair `!![e, w; w, e]` (with
`w = ∓v` for the `±t` ensemble member).  The average is the same expression at `w = 0`. -/
noncomputable def outE (a c e w : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![a, 0, 0, 0; 0, c, 0, 0; 0, 0, e, w; 0, 0, w, e]

/-- The receiver-side scalar `α(x,ε) = 1 - x - (2-3x)ε`, i.e. `Λ_x(ρ_ε)`'s eigenvalue on the
non-degenerate direction (`α + 2b = 1`, so the output is a state). -/
noncomputable def alphaB (x ε : ℝ) : ℝ := 1 - x - (2 - 3 * x) * ε

theorem outB_isHermitian (α b u : ℝ) : (outB α b u).IsHermitian := by
  refine isHermitian_of_transpose ?_
  ext i j
  fin_cases i <;> fin_cases j <;> simp [outB, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

theorem outE_isHermitian (a c e w : ℝ) : (outE a c e w).IsHermitian := by
  refine isHermitian_of_transpose ?_
  ext i j
  fin_cases i <;> fin_cases j <;> simp [outE, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

/-- `α + 2b = 1` — the receiver output really is a trace-one matrix. -/
theorem outB_trace (x ε : ℝ) : (outB (alphaB x ε) (b x ε) 0).trace = 1 := by
  simp [outB, alphaB, b, Matrix.trace, Matrix.diag, Fin.sum_univ_three, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]
  ring

/-- `(1-x) + xε + 2e = 1` — the environment output really is a trace-one matrix. -/
theorem outE_trace (x ε : ℝ) : (outE (1 - x) (x * ε) (e x ε) 0).trace = 1 := by
  simp [outE, e, Matrix.trace, Matrix.diag, Fin.sum_univ_four, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  ring

/-! ### LEAN-3 WP-D (2026-08-01) — the identification of `outB`/`outE` with the channel

Residual (c) of `WHGAP/Trust.lean`: `outB`/`outE` were *defined* by the displays of paper
Lemma 7.1, and that they are `Λ_x(ρ_ε ± tX)` and `Λ^c_x(ρ_ε ± tX)` was an exact-sympy gate.
`WHGAP.Support.Channel` now builds the channel out of its Kraus set, so the two identities
below are theorems.  Both signs of the ensemble are the single statement at `±θ`, because
`u`/`v` are odd in `θ` (`u_neg`, `v_neg`). -/

section Identification

theorem u_neg (x θ r : ℝ) : WHGAP.Support.u x (-θ) r = -WHGAP.Support.u x θ r := by
  simp [WHGAP.Support.u]; ring

theorem v_neg (x θ r : ℝ) : WHGAP.Support.v x (-θ) r = -WHGAP.Support.v x θ r := by
  simp [WHGAP.Support.v]; ring

/-- **Residual (c), receiver side.**  `Λ_x(ρ_ε + θX) = outB(α, b, u)` entrywise.

*(LEAN-3.2, R13 m10: the former hypothesis `hr0 : r ≠ 0` is dropped.  It advertised a
non-degeneracy requirement that does not exist — at `r = 0` Lean's junk convention gives
`Xwit 0 = 0` and `u x θ 0 = 0`, so the identity still holds.  The theorem is strictly
stronger without it; every call site passes `r = √2`.)* -/
theorem outB_eq (x ε θ r : ℝ) :
    Channel.Lam x (Channel.rhoDiag ε + θ • Channel.Xwit r)
      = outB (alphaB x ε) (WHGAP.Support.b x ε) (WHGAP.Support.u x θ r) := by
  ext i j
  simp only [Channel.Lam, Matrix.add_apply, Matrix.smul_apply, Matrix.sub_apply,
    Matrix.transpose_apply, Matrix.one_apply, Matrix.trace, Matrix.diag, Fin.sum_univ_three,
    smul_eq_mul]
  fin_cases i <;> fin_cases j <;>
    simp [Channel.rhoDiag, Channel.Xwit, outB, alphaB, WHGAP.Support.b, WHGAP.Support.u,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons] <;>
    try (field_simp; ring)

/-- **Residual (c), environment side.**  `Λ^c_x(ρ_ε + θX) = outE(1−x, xε, e, −v)` entrywise.
The lift parameter `β` drops out: the input is symmetric, so its antisymmetric vector
vanishes and the whole first row/column of `eq:comp` collapses.

*(LEAN-3.2, R13 m10: the former hypothesis `hr0 : r ≠ 0` is dropped, for the same reason as
in `outB_eq` — at `r = 0`, `Xwit 0 = 0` and `v x θ 0 = 0`.)* -/
theorem outE_eq (x ε θ r β : ℝ) :
    Channel.LamC x β (Channel.rhoDiag ε + θ • Channel.Xwit r)
      = outE (1 - x) (x * ε) (WHGAP.Support.e x ε) (-(WHGAP.Support.v x θ r)) := by
  ext i j
  simp only [Channel.LamC, Channel.LamCgen, Channel.aVec, Matrix.of_apply, Matrix.add_apply,
    Matrix.smul_apply, Matrix.trace, Matrix.diag, Fin.sum_univ_three, smul_eq_mul]
  fin_cases i <;> fin_cases j <;>
    simp [Channel.rhoDiag, Channel.Xwit, outE, WHGAP.Support.e, WHGAP.Support.v,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons] <;>
    first
      | tauto
      | (field_simp; ring)
      | ring
  all_goals tauto

end Identification

/-- **Spectrum of the receiver output** (via the rational similarity of `Entropy.lean`):
`S(Λ_x(ρ_ε ± tX)) = negMulLog α + negMulLog (b+u) + negMulLog (b-u)`, i.e. the eigenvalues
are `{α, b±u}` exactly as displayed in the proof of paper Lemma 7.1. -/
theorem vnEntropy_outB (α b u : ℝ) :
    vnEntropy (outB_isHermitian α b u)
      = Real.negMulLog α + Real.negMulLog (b + u) + Real.negMulLog (b - u) := by
  have hUV : (!![1, 0, 0; 0, 1/2, 1/2; 0, 1/2, -1/2] : Matrix (Fin 3) (Fin 3) ℝ)
      * !![1, 0, 0; 0, 1, 1; 0, 1, -1] = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  have hconj : (!![1, 0, 0; 0, 1, 1; 0, 1, -1] : Matrix (Fin 3) (Fin 3) ℝ)
      * Matrix.diagonal ![α, b + u, b - u] * !![1, 0, 0; 0, 1/2, 1/2; 0, 1/2, -1/2]
      = outB α b u := by
    rw [Support.diagonal_fin_three]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_three, outB, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons] <;> ring
  rw [vnEntropy_of_conj_diagonal (outB_isHermitian α b u) _ hUV hconj]
  simp [Fin.sum_univ_three, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]

/-- **Spectrum of the environment output**: the eigenvalues are `{1-x, xε, e±v}`. -/
theorem vnEntropy_outE (a c e w : ℝ) :
    vnEntropy (outE_isHermitian a c e w)
      = Real.negMulLog a + Real.negMulLog c
        + Real.negMulLog (e + w) + Real.negMulLog (e - w) := by
  have hUV : (!![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1/2, 1/2; 0, 0, 1/2, -1/2] :
      Matrix (Fin 4) (Fin 4) ℝ) * !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 1; 0, 0, 1, -1] = 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      norm_num [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  have hconj : (!![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 1; 0, 0, 1, -1] : Matrix (Fin 4) (Fin 4) ℝ)
      * Matrix.diagonal ![a, c, e + w, e - w]
      * !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1/2, 1/2; 0, 0, 1/2, -1/2] = outE a c e w := by
    rw [Support.diagonal_fin_four]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_four, outE, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons] <;> ring
  rw [vnEntropy_of_conj_diagonal (outE_isHermitian a c e w) _ hUV hconj]
  simp [Fin.sum_univ_four, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
    Matrix.tail_cons]

/-- The receiver-side Holevo quantity of the symmetric two-point ensemble `E(ε,t)`:
`χ(E,B) = S(Λ_x(ρ̄)) - ½ S(Λ_x(ρ_ε+tX)) - ½ S(Λ_x(ρ_ε-tX))`, all three entropies computed
from the explicit output matrices. -/
noncomputable def chiB (x ε t r : ℝ) : ℝ :=
  vnEntropy (outB_isHermitian (alphaB x ε) (b x ε) 0)
    - (1/2) * vnEntropy (outB_isHermitian (alphaB x ε) (b x ε) (u x t r))
    - (1/2) * vnEntropy (outB_isHermitian (alphaB x ε) (b x ε) (-u x t r))

/-- The environment-side Holevo quantity of the same ensemble. -/
noncomputable def chiE (x ε t r : ℝ) : ℝ :=
  vnEntropy (outE_isHermitian (1 - x) (x * ε) (e x ε) 0)
    - (1/2) * vnEntropy (outE_isHermitian (1 - x) (x * ε) (e x ε) (-v x t r))
    - (1/2) * vnEntropy (outE_isHermitian (1 - x) (x * ε) (e x ε) (v x t r))

/-- **PAYOFF, receiver side (paper Lemma 7.1, first half of `eq:chis`): `χ(E,B) = b f(u/b)`.**
Unconditional apart from the three non-degeneracy side conditions `b, b±u ≠ 0` that the
logarithms need. -/
theorem chiB_collapse (x ε t r : ℝ) (hb : b x ε ≠ 0)
    (hp : b x ε + u x t r ≠ 0) (hm : b x ε - u x t r ≠ 0) :
    chiB x ε t r = b x ε * f (u x t r / b x ε) := by
  set B := b x ε
  set U := u x t r
  unfold chiB
  rw [vnEntropy_outB, vnEntropy_outB, vnEntropy_outB]
  have e1 : B + 0 = B := by ring
  have e2 : B - 0 = B := by ring
  have e3 : B + -U = B - U := by ring
  have e4 : B - -U = B + U := by ring
  rw [e1, e2, e3, e4]
  linarith [two_point_collapse hb hp hm]

/-- **PAYOFF, environment side (paper Lemma 7.1, second half of `eq:chis`):
`χ(E,E) = e f(v/e)`.** -/
theorem chiE_collapse (x ε t r : ℝ) (he : e x ε ≠ 0)
    (hp : e x ε + v x t r ≠ 0) (hm : e x ε - v x t r ≠ 0) :
    chiE x ε t r = e x ε * f (v x t r / e x ε) := by
  set E := e x ε
  set V := v x t r
  unfold chiE
  rw [vnEntropy_outE, vnEntropy_outE, vnEntropy_outE]
  have e1 : E + 0 = E := by ring
  have e2 : E - 0 = E := by ring
  have e3 : E + -V = E - V := by ring
  have e4 : E - -V = E + V := by ring
  rw [e1, e2, e3, e4]
  linarith [two_point_collapse he hp hm]

/-! ### The frozen witness point `ε = t = ε_c(x)/2` -/

section Frozen

variable {x : ℝ}

/-- At the frozen point the receiver-side denominators are all nonzero: `b = (1-x)/2 > 0` and
`b ± u = b(1 ± s*) > 0` because `0 < s*(x) < 1`. -/
theorem frozen_B_ne (hx0 : 0 < x) (hx : x < 1 / 2) :
    b x (epsC x / 2) ≠ 0 ∧
    b x (epsC x / 2) + u x (epsC x / 2) (Real.sqrt 2) ≠ 0 ∧
    b x (epsC x / 2) - u x (epsC x / 2) (Real.sqrt 2) ≠ 0 := by
  obtain ⟨hr, _⟩ := sqrt_two_spec
  have hbpos : 0 < b x (epsC x / 2) := by rw [b_at hx0 hx]; linarith
  have hbne : b x (epsC x / 2) ≠ 0 := ne_of_gt hbpos
  have harg := (argument_coincidence hx0 hx hr).1
  have hs : u x (epsC x / 2) (Real.sqrt 2) = sStar x * b x (epsC x / 2) := by
    have := (div_eq_iff hbne).mp harg
    rw [this]
    unfold sStar
    ring
  have hs0 : 0 < sStar x := sStar_pos hx0 hx
  have hs1 : sStar x < 1 := sStar_lt_one hx0 hx
  refine ⟨hbne, ?_, ?_⟩
  · rw [hs]; nlinarith
  · rw [hs]; nlinarith

/-- The environment-side counterpart of `frozen_B_ne`. -/
theorem frozen_E_ne (hx0 : 0 < x) (hx : x < 1 / 2) :
    e x (epsC x / 2) ≠ 0 ∧
    e x (epsC x / 2) + v x (epsC x / 2) (Real.sqrt 2) ≠ 0 ∧
    e x (epsC x / 2) - v x (epsC x / 2) (Real.sqrt 2) ≠ 0 := by
  obtain ⟨hr, _⟩ := sqrt_two_spec
  have h23 : (0:ℝ) < 2 - 3 * x := two_sub_three_x_pos hx0 hx
  have hepos : 0 < e x (epsC x / 2) := by
    rw [e_at hx0 hx]
    apply div_pos (by nlinarith) (by linarith)
  have hene : e x (epsC x / 2) ≠ 0 := ne_of_gt hepos
  have harg := (argument_coincidence hx0 hx hr).2
  have hs : v x (epsC x / 2) (Real.sqrt 2) = sStar x * e x (epsC x / 2) := by
    have := (div_eq_iff hene).mp harg
    rw [this]
    unfold sStar
    ring
  have hs0 : 0 < sStar x := sStar_pos hx0 hx
  have hs1 : sStar x < 1 := sStar_lt_one hx0 hx
  refine ⟨hene, ?_, ?_⟩
  · rw [hs]; nlinarith
  · rw [hs]; nlinarith

/-- **`Delta_eq_chi_diff` — the whole of paper Theorem 5.2's entropy content, in Lean.**
At the frozen parameter point `ε = t = ε_c(x)/2` the closed-form scalar `Δ(x)` IS the
Holevo difference of the explicit two-point ensemble:

  `Δ(x) = χ(E,B) - χ(E,E) = b f(u/b) - e f(v/e)`,

the two arguments having already been shown equal by `argument_coincidence`. -/
theorem Delta_eq_chi_diff (hx0 : 0 < x) (hx : x < 1 / 2) :
    Delta x = chiB x (epsC x / 2) (epsC x / 2) (Real.sqrt 2)
              - chiE x (epsC x / 2) (epsC x / 2) (Real.sqrt 2) := by
  obtain ⟨hr, _⟩ := sqrt_two_spec
  obtain ⟨hb, hbp, hbm⟩ := frozen_B_ne hx0 hx
  obtain ⟨he, hep, hem⟩ := frozen_E_ne hx0 hx
  rw [chiB_collapse _ _ _ _ hb hbp hbm, chiE_collapse _ _ _ _ he hep hem]
  obtain ⟨hu, hv⟩ := argument_coincidence hx0 hx hr
  have hs : sStar x = (1 - 2 * x) / (Real.sqrt 2 * (1 - x)) := rfl
  rw [hu, hv, ← hs, ← Delta_eq_prefactor_mul hx0 hx]
  ring

end Frozen

/-! ### The reduced trust boundary -/

/-- **THE REDUCTION (LEAN-2 WP-C).**  `Claim_of_delta_le`'s hypothesis `hbridge` — "the
ensemble achieves `Δ(x)`, and `P^{(1)}` dominates it" — is now implied by *exactly* the
Devetak/HSW reading of the explicit ensemble:

  `χ(E,B) - χ(E,E) ≤ P^{(1)}(Λ_x)` for the one ensemble `E(ε_c/2, ε_c/2)`,

with `χ(E,B)`, `χ(E,E)` computed here from the explicit output matrices by
`chiB_collapse`/`chiE_collapse`.  Nothing about `f`, about the coincidence of the two Holevo
arguments, or about the entropy collapse is assumed any more: all of that is proved.

**What remains outside Lean (corrected 2026-08-01, R13 m1).**  The identification of
`outB`/`outE` with `Λ_x(ρ_ε ± tX)` and `Λ^c_x(ρ_ε ± tX)` is **no longer** outside Lean: it is
`outB_eq`/`outE_eq` above (LEAN-3 WP-D), so residual (c) of `WHGAP/Trust.lean` is closed.
What `hdev` still carries is (i) Devetak's formula
`P^{(1)} = max_ensembles [χ(·,B) - χ(·,E)]`, the cited external interface, and (ii) the
*validity of the ensemble* it is applied to — that `ρ_ε ± tX` are states (PSD, trace one) and
that `|t| ≤ √2 ε`, neither of which is represented anywhere in this development. -/
theorem Claim_of_devetak (I : CapacityInterface)
    (hdev : ∀ x : ℝ, 0 < x → x < 1 / 2 →
      chiB x (epsC x / 2) (epsC x / 2) (Real.sqrt 2)
        - chiE x (epsC x / 2) (epsC x / 2) (Real.sqrt 2) ≤ I.Pone x) :
    Claim I := by
  refine Claim_of_delta_le I ?_
  intro x hx0 hx
  rw [Delta_eq_chi_diff hx0 hx]
  exact hdev x hx0 hx

end Holevo

end WHGAP.«private-boundary»

