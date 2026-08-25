/-
`SE/denom/Phi/legal/tame.lean` — linked node module.
This is the composition the whole project turns on: "H1 ∧ H2 ∧ H3 ∧ H4 ⟹ the legal `Φ` layer
is O(1)", the Lean mirror of the prose composition block on the node file.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom.Phi.legal.tame      (alias `PLT`)
node file      : se/proof-dag/nodes/SE.denom.Phi.legal.tame.yaml
decomposition / role    : AND / proof
children       : gram, omega, trace, found, sect (five)
epistemic status (read from the node file on 2026-07-30): **OPEN**
composition status on the node: **CERTIFIED\*** (external re-review T2': "H1∧H2∧H3∧H4 suffice for
                 Theorem B; no hidden H5"; stars = FOUND's rule-7b c≥2 caveat + the review verified
                 the DERIVATION, not the hypotheses)
mechanization  : composition-checked, relative to Cited + the four hypothesis Claims below
claim_hash     : sha256:d90c15dec4235220cf1370c0a9863598c18ee42326b51a5fbe4f8dfaf8d609bf
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.denom.Phi.legal.tame — make Phi legality O(1): 1(a) general structural vanishing REFUTED
  (witness: defect-1 block = 0.3 at (3,6,2)); OPEN: in-spec-only vanishing / uniform O(1) two-sided improvement / cross-channel cancellation

  (Indentation added only to nest the quote inside this comment; the hash above is of the
  UNINDENTED node text.)

────────────────────────────────────────────────────────────────────────────────────────────────
WHAT `Claim` BELOW RENDERS.  The frozen Claim is a STATUS LINE (a refuted route plus the open
routes), not a single displayed inequality.  The mathematical content the downstream node `SE.denom`
consumes from this node — the "uniform O(1)" reading, paper eq:omega-lower-global — is

  `‖C_{j+1→j}‖ ≤ √(15/8) · ρ_j · √(j/(n−j))`   on the active window `1 ≤ j`, `3j ≤ n`, `j < K−1`,

and that is what `Claim` states.  (Re-scoped 2026-07-30 per §7.10 review finding F1: the window
is exactly eq:omega-lower-global's `1 ≤ j < K−1` with Conjecture H's preamble `n ≥ 3j` — the
earlier `∀ j < n` form was wider than what H1–H4 as frozen can deliver.)  This is a place where
the Lean statement must differ in FORM from the frozen prose (reported in
`se/artifacts/se_lean_t1_20260730.md`); the composition proof below is the Lean mirror of the node's
own `## Composition proof` block (added 2026-07-30).

────────────────────────────────────────────────────────────────────────────────────────────────
PREMISE DECLARATION (under the current DAG premise rules, a composition premise may be a child, a cited external
interface, or an explicit relative hypothesis — coordinator ruling R3, 2026-07-30).

The node's five status-propagating children are `gram`, `omega`, `trace`, `found`, `sect`.
`composition` below does NOT consume five child Claims; its premises are:

  * `trace.t6.Claim`        — GRANDCHILD (via `trace`); the H1 obligation lives on `t6`, and
                              `SE.denom.Phi.legal.trace` itself has no `formalization` block;
  * `gram.interface.Claim`  — GRANDCHILD (via `gram`); H2; `gram` has no `formalization` block;
  * `omega.interface.Claim` — GRANDCHILD (via `omega`); H3; `omega` has no `formalization` block;
  * `sect.Claim`            — CHILD; H4;
  * `F.Cited`               — the cited interface (adversary bound + reviewed-proved analytic
                              lemmas, incl. the ω-range eq:omega-range used in step 3).

`found` has NO tier-1 rendering at all: it supplies the typed carrier objects, orbit identities,
twirl and output frames against which H1–H4 are *stated*; without an operator layer those are
invisible, and the abstract carrier `SEFrame` stands in for them.  FOUND's own rule-7b `c≥2`
identity-gate caveat therefore rides along with this composition (as it does with the prose
block).  Consequently §7.6 anti-drift check 4 ("composition parameters cover exactly the
status-propagating children") does NOT hold literally for this node; the deviation is declared
here, in `SE/Trust.lean` §D, and in the node's `lean.rel` field.

No `sorry`.  A green build says the DERIVATION below is machine-checked; it says nothing about
H1–H4 themselves (H1/H4 OPEN, H2/H3 CONJECTURED on disk as of 2026-07-30).
-/
import SE.denom.Phi.legal.trace.t6
import SE.denom.Phi.legal.gram.interface
import SE.denom.Phi.legal.omega.interface
import SE.denom.Phi.legal.sect
import SE.Support.RhoEnvelope

namespace SE.denom.Phi.legal.tame

section
variable (F : SE.SEFrame)

/-- The node's Lean claim — the "uniform O(1)" content of `SE.denom.Phi.legal.tame` that the
the downstream node `SE.denom` consumes: **`‖C_{j+1→j}‖ ≤ √(15/8)·ρ_j·√(j/(n-j))`** on the active window
`1 ≤ j`, `3j ≤ n`, `j < K n − 1` (paper eq:omega-lower-global, whose scope is `1 ≤ j < K−1`
under Conjecture H's preamble `n ≥ 3j`).  See the module header for why this differs in form
from the frozen status-line Claim. -/
def Claim : Prop :=
  ∀ n j : ℕ, 1 ≤ j → 3 * j ≤ n → j < SE.K n - 1 →
    F.cLower n j
      ≤ Real.sqrt (15 / 8) * F.rho n j * Real.sqrt ((j : ℝ) / ((n : ℝ) - (j : ℝ)))

end

section
variable {F : SE.SEFrame}

/-! ## Step 1+2 of the node's composition block — the canonical Gram bound
(paper Proposition `thm:gram`, eq:gram-main) -/

/-- **`‖𝖦_can^{λ,ξ}‖ ≤ (15/4)·r_top`**, uniformly in the LR multiplicity `c ≥ 1` — from
(H1) ∧ (H2).  Mirrors steps 1–2 of the node's prose composition block; per that block the bound
is **non-strict** (the strict form does not follow; `r_top < 6/5` is a separate condition not
equivalent to `n ≥ (j+2)³` — external re-review erratum, 2026-07-30). -/
theorem gcan_le (hC : F.Cited) (h1 : trace.t6.Claim F) (h2 : gram.interface.Claim F)
    {n j : ℕ} (s : F.Sector n j) (hs : F.admissible n j s) :
    F.gcanS n j s ≤ 15 / 4 * F.rtopS n j s := by
  have hb := hC.bthe_pos n j s hs
  have hw := hC.omega_pos n j s hs
  have hr := hC.rtop_pos n j s hs
  have hden : (0 : ℝ) < (F.btheS n j s) ^ 2 * F.omegaS n j s := by positivity
  rw [h2 n j s hs, div_mul_eq_mul_div, div_le_iff₀ hden]
  calc F.rtopS n j s * F.mxiS n j s
      ≤ F.rtopS n j s * (15 / 4 * (F.btheS n j s) ^ 2 * F.omegaS n j s) :=
        mul_le_mul_of_nonneg_left (h1 n j s hs) hr.le
    _ = 15 / 4 * F.rtopS n j s * ((F.btheS n j s) ^ 2 * F.omegaS n j s) := by ring

/-! ## Step 3 of the node's composition block — the per-sector lower-block bound
(paper `lem:omega-lower` (i), eq:omega-lower) -/

/-- **`‖C̃_{λ,ξ}‖ ≤ √(15/8)·r_top·√(j/(n-j))`** — from (H1) ∧ (H2) ∧ (H3) and the cited
reviewed-proved `ω`-range eq:omega-range (`Cited.omega_le`). -/
theorem csect_le (hC : F.Cited) (h1 : trace.t6.Claim F) (h2 : gram.interface.Claim F)
    (h3 : omega.interface.Claim F) {n j : ℕ} (s : F.Sector n j)
    (hs : F.admissible n j s) (hjn : (j : ℝ) < (n : ℝ)) :
    F.csectS n j s
      ≤ Real.sqrt (15 / 8) * F.rtopS n j s * Real.sqrt ((j : ℝ) / ((n : ℝ) - (j : ℝ))) := by
  have hnj : (0 : ℝ) < (n : ℝ) - (j : ℝ) := by linarith
  have hj0 : (0 : ℝ) ≤ (j : ℝ) := Nat.cast_nonneg j
  have hquot : (0 : ℝ) ≤ (j : ℝ) / ((n : ℝ) - (j : ℝ)) := div_nonneg hj0 hnj.le
  have hr := hC.rtop_pos n j s hs
  have hw := hC.omega_pos n j s hs
  have hcs := hC.csect_nonneg n j s hs
  set A : ℝ := Real.sqrt (15 / 8) * F.rtopS n j s * Real.sqrt ((j : ℝ) / ((n : ℝ) - (j : ℝ)))
    with hA
  have hAnn : 0 ≤ A := by
    rw [hA]; positivity
  have hA2 : A ^ 2 = 15 / 8 * (F.rtopS n j s) ^ 2 * ((j : ℝ) / ((n : ℝ) - (j : ℝ))) := by
    rw [hA, mul_pow, mul_pow, Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 15/8), Real.sq_sqrt hquot]
  -- the squared chain
  have hsq : (F.csectS n j s) ^ 2 ≤ A ^ 2 := by
    have step1 : (F.csectS n j s) ^ 2 ≤ F.cnprobS n j s * F.gcanS n j s := h3.1 n j s hs
    have step2 : F.cnprobS n j s * F.gcanS n j s
        = F.rtopS n j s * F.omegaS n j s * F.gcanS n j s := by rw [h3.2 n j s hs]
    have step3 : F.rtopS n j s * F.omegaS n j s * F.gcanS n j s
        ≤ F.rtopS n j s * F.omegaS n j s * (15 / 4 * F.rtopS n j s) :=
      mul_le_mul_of_nonneg_left (gcan_le hC h1 h2 s hs) (by positivity)
    have step4 : F.omegaS n j s ≤ (j : ℝ) / (2 * ((n : ℝ) - (j : ℝ))) := hC.omega_le n j s hs
    have step5 : F.rtopS n j s * F.omegaS n j s * (15 / 4 * F.rtopS n j s)
        ≤ F.rtopS n j s * ((j : ℝ) / (2 * ((n : ℝ) - (j : ℝ)))) * (15 / 4 * F.rtopS n j s) := by
      have : (0 : ℝ) ≤ 15 / 4 * F.rtopS n j s := by positivity
      nlinarith [step4, hr.le, this]
    have step6 : F.rtopS n j s * ((j : ℝ) / (2 * ((n : ℝ) - (j : ℝ)))) * (15 / 4 * F.rtopS n j s)
        = 15 / 8 * (F.rtopS n j s) ^ 2 * ((j : ℝ) / ((n : ℝ) - (j : ℝ))) := by
      field_simp
      ring
    rw [hA2]
    linarith [step1, step2.le, step3, step5, step6.le]
  -- undo the square
  calc F.csectS n j s = Real.sqrt ((F.csectS n j s) ^ 2) := (Real.sqrt_sq hcs).symm
    _ ≤ Real.sqrt (A ^ 2) := Real.sqrt_le_sqrt hsq
    _ = A := Real.sqrt_sq hAnn

/-! ## Step 4 of the node's composition block — the global lower-block bound
(paper `lem:omega-lower` (ii), eq:omega-lower-global) -/

/-- **The node's composition theorem** (§7.4): Cited ∧ H1 ∧ H2 ∧ H3 ∧ H4 ⟹ `Claim`.

Step 4 is the H4 step: per-sector compressions control the global block ONLY through the
exhaustive sectorization — this is the link that was missing until 2026-07-29 (external review
finding T3-G1); removing `h4` from the binder list makes this theorem fail to elaborate, which is
the mechanical demonstration the `sect` node asks for.

Premises per the header's PREMISE DECLARATION (R3): `t6`/`gram.interface`/`omega.interface` are
grandchild-level obligations, `sect` is a child, `Cited` is the interface; the child `found` has
no tier-1 rendering and its `c≥2` caveat rides along. -/
theorem composition (hC : F.Cited) (h1 : trace.t6.Claim F) (h2 : gram.interface.Claim F)
    (h3 : omega.interface.Claim F) (h4 : sect.Claim F) : Claim F := by
  intro n j hj1 hj3 hjK
  have hjnN : j < n := by omega
  have hjn : (j : ℝ) < (n : ℝ) := by exact_mod_cast hjnN
  have hnj : (0 : ℝ) < (n : ℝ) - (j : ℝ) := by linarith
  have hj0 : (0 : ℝ) ≤ (j : ℝ) := Nat.cast_nonneg j
  have hquot : (0 : ℝ) ≤ (j : ℝ) / ((n : ℝ) - (j : ℝ)) := div_nonneg hj0 hnj.le
  have hrho : (1 : ℝ) ≤ F.rho n j := hC.rho_ge_one n j (by omega)
  refine h4 n j _ hj1 hj3 hjK (by positivity) ?_
  intro s hs
  refine le_trans (csect_le hC h1 h2 h3 s hs hjn) ?_
  have h1' : F.rtopS n j s ≤ F.rho n j := hC.rtop_le_rho n j s hs
  have h2' : (0 : ℝ) ≤ Real.sqrt (15 / 8) := Real.sqrt_nonneg _
  have h3' : (0 : ℝ) ≤ Real.sqrt ((j : ℝ) / ((n : ℝ) - (j : ℝ))) := Real.sqrt_nonneg _
  exact mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left h1' h2') h3'

end

end SE.denom.Phi.legal.tame
