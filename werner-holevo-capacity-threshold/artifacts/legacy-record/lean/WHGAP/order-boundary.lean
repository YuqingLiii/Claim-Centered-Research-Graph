import WHGAP.«signed-lift-extension»

/-!
# `WHGAP.order-boundary` (P6)

* node id: `WHGAP.order-boundary`
* node file: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.order-boundary.md`
* epistemic status on disk (2026-07-30): **PROVED** (R5b review, LICENSE A; `x_B = 1/2`).
* mechanization state: `composition-checked` rel `{hHolds, hFails}` + `proved` for the T2
  algebraic core below.
* DAG child: `WHGAP.signed-lift-extension` (imported).

## Frozen Claim (verbatim from the node file, `## Claim` section)

Determine the boundary x_B of the set {x : Lambda_x^c dominates Lambda_x in the complete
Bogoliubov–Kubo–Mori (cBKM) sense} within the strip (x_1, 1/2), where
x_1 = 0.390910... is the P3 max-mixed crossing. **[PROVED — ANSWERED: x_B = 1/2 exactly.
Domination FAILS for every x in (0, 1/2) (lead's analytic BKM-necessity witness; paper §5;
R5b review) and HOLDS on [1/2, 1) (P2/P4 signed lift). The cBKM and cRE domination sets both
equal [1/2, 1).]**

* frozen-claim SHA-256: `db0301276dd9cb7382a3553ab2cfc717a47cf104462987ecc912f6c64c69e611`

## Statement-fidelity note (G-L5)

`Claim cBKM` below is `∀ x ∈ (0,1), cBKM x ↔ 1/2 ≤ x`, i.e. exactly "the cBKM domination set
is `[1/2, 1)`", which is the ANSWER recorded in the prose Claim.  Granularity loss: `cBKM` is
an *abstract predicate parameter*, not a definition — no Bogoliubov–Kubo–Mori inner product,
no complete positivity, and no complementary channel exists in this development.  The prose
Claim's extra content ("the cRE domination set coincides") is not represented.

What is machine-checked outright is the **algebraic core of the necessity direction**: the
paper-§5 gap function, its factorization in `ε`, and the strict-violation window
`0 < ε < ε_c(x)` on which the second-order test is negative.  `gap_identity` is the `ε = 0`
specialization used in the note; `threshold_factorization` is the exact finite-`ε` form;
`strict_violation_window` is the sign conclusion.  These are the *scalar identities* behind
the witness pair `(ρ_ε, X)`, not a proof that the witness violates BKM domination.
-/

namespace WHGAP.«order-boundary»

open WHGAP WHGAP.Support

/-- **P6 Claim, tier-1 form.**  The complete-BKM domination set of the family is exactly
`[1/2, 1)`: `x_B = 1/2`.  `cBKM` is an abstract predicate (see the fidelity note). -/
def Claim (cBKM : ℝ → Prop) : Prop :=
  ∀ x : ℝ, 0 < x → x < 1 → (cBKM x ↔ 1 / 2 ≤ x)

/-! ## T2 core — the paper-§5 gap and its finite-`ε` threshold -/

/-- The `ε = 0` gap identity of paper §5:
`x/2 - (2/x)(1 - 3x/2)² = 2(1-x)(2x-1)/x`. -/
theorem gap_identity {x : ℝ} (hx : x ≠ 0) :
    x / 2 - (2 / x) * (1 - 3 * x / 2) ^ 2 = 2 * (1 - x) * (2 * x - 1) / x := by
  field_simp
  ring

/-- The gap is strictly negative on `(0, 1/2)` — the `ε = 0` shadow of the necessity witness. -/
theorem gap_neg_below_half {x : ℝ} (hx0 : 0 < x) (hx : x < 1 / 2) :
    2 * (1 - x) * (2 * x - 1) / x < 0 :=
  div_neg_of_neg_of_pos (by nlinarith) hx0

/-- Exact finite-`ε` factorization of the gap:
`x·b(x,ε) - 2(1 - 3x/2)²(1-ε) = 2(1-x)[(2x-1) + (1 - 3x/2) ε]`.
Polynomial identity — no side condition. -/
theorem threshold_factorization (x ε : ℝ) :
    x * b x ε - 2 * (1 - 3 * x / 2) ^ 2 * (1 - ε)
      = 2 * (1 - x) * ((2 * x - 1) + (1 - 3 * x / 2) * ε) := by
  unfold b
  ring

/-- **Strict violation window.**  For `0 < x < 1/2` and `ε < ε_c(x) = 2(1-2x)/(2-3x)`,
the finite-`ε` gap is strictly negative.  This is the sign statement that makes `ε_c` the
exact threshold of the necessity witness (R5b).

The physical window is `0 < ε < ε_c(x)`, but the hypothesis `0 < ε` is **not needed** and was
dropped per R11 m12: the conclusion holds for every `ε < ε_c(x)`, so the theorem as stated is
strictly stronger than the window it is used on. -/
theorem strict_violation_window {x ε : ℝ} (hx0 : 0 < x) (hx : x < 1 / 2)
    (hεc : ε < epsC x) :
    x * b x ε - 2 * (1 - 3 * x / 2) ^ 2 * (1 - ε) < 0 := by
  have h23 : 0 < 2 - 3 * x := two_sub_three_x_pos hx0 hx
  have h1x : 0 < 1 - x := one_sub_x_pos hx0 hx
  have h := mul_lt_mul_of_pos_right hεc h23
  rw [epsC_mul_denom hx0 hx] at h
  -- `h : ε * (2 - 3x) < 2 (1 - 2x)`
  rw [threshold_factorization]
  have hinner : (2 * x - 1) + (1 - 3 * x / 2) * ε < 0 := by
    rw [show (1 - 3 * x / 2) * ε = (ε * (2 - 3 * x)) / 2 by ring]
    linarith
  have h2 : (0:ℝ) < 2 * (1 - x) := by linarith
  exact mul_neg_of_pos_of_neg h2 hinner

/-! ## T2 core, continued — the two trivial-reference BKM scalars of the §5 witness
(LEAN-3 WP-F item 3, 2026-08-01)

Paper Theorem 5.2 (`thm:necessity`) evaluates the BKM quadratic form of the witness pair
`ρ_ε = diag(1-2ε, ε, ε)`, `X = (E₁₂ + E₂₁)/√2` on both sides.  Because `X` couples exactly the
two *degenerate* eigendirections of each output, the eigenbasis formula
`g_θ(Y) = ∑_{jk} |Y_{jk}|²/θ_j` collapses to a single eigenvalue on each side, giving the two
scalars

    g_B(x,ε) = (1 - 3x/2)² / b_ε        (receiver: `Λ_x(X) = (1-3x/2) X`, eigenvalue `b_ε`)
    g_E(x,ε) = x / (2(1-ε))             (environment: `Λ^c_x(X) = 0 ⊕ (-x/2)X`, eigenvalue `e_ε`)

*These two lines are definitions here, not theorems*: the collapse of the eigenbasis formula
to them is the paper's computation, and there is no BKM form, no output state and no channel
in this development (see the fidelity note).  What is proved below is the **strict violation**
`g_E < g_B` on the exact window `0 < ε < ε_c(x)` for `0 < x < 1/2` — the inequality the
necessity argument needs — and it is *wired* to `strict_violation_window` /
`threshold_factorization` above rather than re-deriving the factorization. -/

section BKMScalars

/-- Receiver-side trivial-reference BKM scalar of the §5 witness,
`g_B(x,ε) = (1 - 3x/2)²/b_ε`. -/
noncomputable def gB (x ε : ℝ) : ℝ := (1 - 3 * x / 2) ^ 2 / b x ε

/-- Environment-side trivial-reference BKM scalar of the §5 witness,
`g_E(x,ε) = x/(2(1-ε))`. -/
noncomputable def gE (x ε : ℝ) : ℝ := x / (2 * (1 - ε))

/-- `ε_c(x) < 1` on `(0, 1/2)`, so the violation window sits strictly inside `(0,1)` where
both outputs of the witness are faithful. -/
theorem epsC_lt_one {x : ℝ} (hx0 : 0 < x) (hx : x < 1 / 2) : epsC x < 1 := by
  have h23 : (0:ℝ) < 2 - 3 * x := two_sub_three_x_pos hx0 hx
  unfold epsC
  rw [div_lt_one h23]
  linarith

/-- `b_ε > 0` on the witness window (the receiver output is faithful there). -/
theorem b_pos_of {x ε : ℝ} (hx0 : 0 < x) (hx : x < 1 / 2) (hε : 0 < ε) : 0 < b x ε := by
  have h : (0:ℝ) < 1 - 3 * x / 2 := by linarith
  have := mul_pos h hε
  unfold b
  linarith

/-- **Strict BKM violation by the §5 witness.**  For `0 < x < 1/2` and `0 < ε < ε_c(x)`,
`g_E(x,ε) < g_B(x,ε)` — the environment-side BKM form is strictly *smaller* than the
receiver-side one, which is exactly the failure of the domination inequality
`g_E ≥ g_B` that `cRE`/`cBKM` would force (paper Lemma 5.1 + Theorem 5.2).  Proof: the
inequality is `strict_violation_window` after clearing the two positive denominators. -/
theorem gE_lt_gB {x ε : ℝ} (hx0 : 0 < x) (hx : x < 1 / 2) (hε0 : 0 < ε)
    (hεc : ε < epsC x) : gE x ε < gB x ε := by
  have hb : 0 < b x ε := b_pos_of hx0 hx hε0
  have hε1 : ε < 1 := lt_trans hεc (epsC_lt_one hx0 hx)
  have hden : (0:ℝ) < 2 * (1 - ε) := by linarith
  have h := strict_violation_window hx0 hx hεc
  unfold gE gB
  rw [div_lt_div_iff₀ hden hb]
  nlinarith [h]

end BKMScalars

/-! ## T1 composition (DAG protocol §7.4): P2 ⟹ the holding side of the boundary -/

/-- **Composition theorem for P6.**  The child `WHGAP.signed-lift-extension` (P2) supplies the
signed lift on `[1/2, 1)`; the ZW criterion step `SignedLiftCP x → cBKM x` and the R5b
necessity theorem `0 < x < 1/2 → ¬ cBKM x` are carried as *explicit hypotheses* (§7.5), since
neither is representable against this interface.  Together they give `x_B = 1/2`. -/
theorem composition (cBKM : ℝ → Prop) (I : CapacityInterface)
    (h2 : «signed-lift-extension».Claim I)
    (hHolds : ∀ x : ℝ, I.SignedLiftCP x → cBKM x)
    (hFails : ∀ x : ℝ, 0 < x → x < 1 / 2 → ¬ cBKM x) :
    Claim cBKM := by
  intro x hx0 hx1
  constructor
  · intro hb
    by_contra hc
    push_neg at hc
    exact hFails x hx0 hc hb
  · intro hhalf
    exact hHolds x (h2 x hhalf hx1)

end WHGAP.«order-boundary»

