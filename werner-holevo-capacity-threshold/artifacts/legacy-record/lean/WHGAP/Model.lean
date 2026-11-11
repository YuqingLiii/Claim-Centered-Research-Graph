import WHGAP.goal
import WHGAP.«order-boundary»
import WHGAP.«private-boundary»

/-!
# `WHGAP.Model` — the in-tree satisfiability witness (DAG protocol §7.10.5)

**Provenance.**  This module is the R11 reviewer's satisfiability certificate, brought into the
project per R11 finding **m14**.  It was authored out-of-tree by the fresh-instance §7.10
reviewer as `artifacts/logs_whgap_lean_20260730/r11_audit_source.lean` (compiled with
`lake env lean`, exit 0) and is reproduced here — with credit — so that the vacuity check
*ships with the development* and the next reviewer has an in-tree artifact to point at.  The
only substantive change from the reviewer's file is that the P14 bridge is now discharged
**concretely** rather than abstractly, which the R11 m4 rewiring of `Claim_of_delta_le` (to the
one-shot `Pone`) makes possible.

**What this file establishes, and what it does not.**  It proves that

* `WHGAP.CapacityInterface` is **inhabited** — so no composition theorem is vacuously true
  from contradictory interface assumptions;
* every composition theorem's hypotheses are **jointly satisfiable**, and satisfiable
  *simultaneously in one model*;
* no composition's conclusion is trivially true: `goal.composition_conjectured` concludes the
  non-trivial set equality `{x ∈ (0,1) : Q x = 0} = [2/5, 1)` here, and `«order-boundary»`'s
  conclusion is instantiated at the non-trivial predicate `cBKM x := 1/2 ≤ x` (neither `True`
  nor `False`);
* the P14 bridge hypothesis is inhabited by an interface whose `Pone` really is `Δ` on
  `(0, 1/2)`;
* **(added 2026-07-31, R12 minor m3)** the two NEW LEAN-2 bridge hypotheses — `hach` of
  `«no-ascent-hierarchy».Claim_of_witness` (WP-B) and `hdev` of
  `«private-boundary».Claim_of_devetak` (WP-C) — are inhabited in the *same* model, and the
  WP-C conclusion is non-trivial there (`χ(E,B) − χ(E,E) > 0`, not `0 ≤ 0`).  See §3b.
* **(added 2026-08-01, R15 minor m3)** the NEW LEAN-5 entropy-level bridge hypothesis —
  `hach'` of `«no-ascent-hierarchy».Claim_of_entropy_witness` (WP-H) — is inhabited in the
  same model, the model's `IcLB` is not the trivial predicate, and `hach ↔ hach'` holds in
  both directions for an arbitrary interface.  See §3c.

It establishes **nothing whatsoever** about the actual Werner–Holevo channel: `R11I` is a model
of the *interface*, deliberately chosen for arithmetic convenience, not a construction of any
capacity.  Satisfiability is a soundness hygiene check, never evidence for a capacity theorem.
-/

namespace WHGAP.Model

open WHGAP

/-! ## 1. An explicit, non-trivial model of the interface -/

/-- Model quantum capacity: `1` below `2/5`, `0` above. -/
noncomputable def R11Q : ℝ → ℝ := fun x => if x < 2 / 5 then 1 else 0

/-- Model private capacity: the genuine closed-form gap `Δ(x)` below `1/2`, `0` above.  Using
`Δ` itself (rather than a constant) is what lets the P14 bridge be discharged concretely. -/
noncomputable def R11P : ℝ → ℝ := fun x => if x < 1 / 2 then Support.Delta x else 0

/-- The model interface.  `Pone := P` (so the LSD/Devetak field holds with equality), and
`SignedLiftCP`/`IcLB` are the non-trivial predicates the reviewer used. -/
noncomputable def R11I : CapacityInterface where
  Q := R11Q
  P := R11P
  Qone := fun _ => 0
  Pone := R11P
  SignedLiftCP := fun x => 1 / 2 ≤ x
  IcLB := fun x c => 0 < x ∧ x < 2 / 5 ∧ 0 < c
  lsd_devetak := by
    intro x
    refine ⟨?_, le_refl _⟩
    show (0:ℝ) ≤ R11Q x
    unfold R11Q; split <;> norm_num
  zw_hrsf_zero := by
    intro x hx
    refine ⟨rfl, ?_, ?_, ?_⟩
    · show R11P x = 0
      unfold R11P
      rw [if_neg]
      intro h; linarith
    · show R11Q x = 0
      unfold R11Q
      rw [if_neg]
      intro h; linarith
    · show R11P x = 0
      unfold R11P
      rw [if_neg]
      intro h; linarith
  q_pos_of_ic_pos := by
    rintro x c hc ⟨hx0, hx25, -⟩
    show (0:ℝ) < R11Q x
    unfold R11Q
    rw [if_pos hx25]
    norm_num

/-- The interface really is inhabited: no contradictory-hypothesis vacuity. -/
example : Nonempty CapacityInterface := ⟨R11I⟩

/-! ## 2. Every child Claim holds in this model — jointly -/

theorem R11_P2 : «signed-lift-extension».Claim R11I := by
  intro x hx _; exact hx

theorem R11_P9 : «no-ascent-hierarchy».Claim R11I := by
  intro x hx0 hx
  exact ⟨1, by norm_num, hx0, hx, by norm_num⟩

theorem R11_P3 : «qpositive-onset».Claim R11I :=
  «qpositive-onset».composition R11I R11_P9

theorem R11_P4 : «zero-capacity-application».Claim R11I :=
  «zero-capacity-application».composition R11I R11_P2

theorem R11_P13 : «onset-two-fifths».Claim R11I «onset-two-fifths».conjecturedS := by
  intro x hx25 hx12
  constructor
  · intro _
    exact ⟨hx25, hx12⟩
  · intro _
    show R11Q x = 0
    unfold R11Q
    rw [if_neg]
    intro h; linarith

/-- The goal composition instantiated: all four hypotheses simultaneously satisfied. -/
theorem R11_goal : WHGAP.goal.Claim R11I «onset-two-fifths».conjecturedS :=
  WHGAP.goal.composition R11I «onset-two-fifths».conjecturedS subset_rfl R11_P3 R11_P4 R11_P13

/-- ... and the conjectured-corollary form, whose conclusion is the concrete, **non-trivial**
set equality `{x ∈ (0,1) : Q x = 0} = [2/5, 1)`. -/
theorem R11_goal_conj :
    {x : ℝ | x ∈ Set.Ioo (0:ℝ) 1 ∧ R11I.Q x = 0} = Set.Ico (2 / 5 : ℝ) 1 :=
  WHGAP.goal.composition_conjectured R11I R11_P3 R11_P4 R11_P13

/-- The P6 composition is satisfiable too, with a *non-trivial* `cBKM` (not `True`, not
`False`): `cBKM x := 1/2 ≤ x`. -/
theorem R11_P6 : «order-boundary».Claim (fun x : ℝ => 1 / 2 ≤ x) :=
  «order-boundary».composition (fun x : ℝ => 1 / 2 ≤ x) R11I R11_P2
    (fun _ h => h) (fun _ _ hx hc => absurd hc (not_le.mpr hx))

/-! ## 3. The P14 bridge is inhabited too -/

/-- In this model the one-shot private capacity **is** `Δ` on `(0, 1/2)`, so the bridge
hypothesis of `«private-boundary».Claim_of_delta_le` holds with equality. -/
theorem R11_bridge : ∀ x : ℝ, 0 < x → x < 1 / 2 → Support.Delta x ≤ R11I.Pone x := by
  intro x _ hx
  show Support.Delta x ≤ R11P x
  unfold R11P
  rw [if_pos hx]

/-- Hence the P14 Claim itself is satisfiable, via the (now unused-hypothesis-free) bridge. -/
theorem R11_P14 : «private-boundary».Claim R11I :=
  «private-boundary».Claim_of_delta_le R11I R11_bridge

/-! ## 3b. The two NEW LEAN-2 bridge hypotheses are inhabited in the SAME model

**Provenance / credit (R12 minor m3, 2026-07-31).**  LEAN-2 shipped two new bridge theorems —
`«no-ascent-hierarchy».Claim_of_witness` (hypothesis `hach`, WP-B) and
`«private-boundary».Claim_of_devetak` (hypothesis `hdev`, WP-C) — without extending this
module, so neither had an *in-tree* §7.10.5 inhabitation certificate.  The four declarations
below are the fresh-instance R12 reviewer's out-of-tree certificate
(`artifacts/logs_whgap_lean2_20260731/r12_satisfiability.lean`, compiled with `lake env lean`,
exit 0, §§1–2), reproduced here **with credit and unchanged in substance** so that the vacuity
check ships with the development.  They use the same model `R11I`; only the `R11_`-style
naming prefix was adapted to `R12_`. -/

/-- `Claim_of_witness`'s `hach` is inhabited in the R11 model, so the new WP-B route into P9
is **not vacuous**.  (R12 §6.) -/
theorem R12_hach :
    ∀ x ε : ℝ, 0 < x → x < 2 / 5 → 0 < ε → ε < 1 → 0 < Support.IcScalar x ε →
      R11I.IcLB x (Support.IcScalar x ε) := by
  intro x ε hx0 hx25 _ _ hpos
  exact ⟨hx0, hx25, hpos⟩

/-- Hence the P9 Claim really follows through the NEW (witness) route. -/
theorem R12_P9_via_witness : «no-ascent-hierarchy».Claim R11I :=
  «no-ascent-hierarchy».Claim_of_witness R11I R12_hach

/-- `Claim_of_devetak`'s `hdev` is inhabited in the R11 model — with **equality**, discharged
using the LEAN-2 theorem `Delta_eq_chi_diff` itself — so the new WP-C route into P14 is **not
vacuous**.  (R12 §6.) -/
theorem R12_hdev :
    ∀ x : ℝ, 0 < x → x < 1 / 2 →
      «private-boundary».chiB x (Support.epsC x / 2) (Support.epsC x / 2) (Real.sqrt 2)
        - «private-boundary».chiE x (Support.epsC x / 2) (Support.epsC x / 2) (Real.sqrt 2)
        ≤ R11I.Pone x := by
  intro x hx0 hx
  have h := («private-boundary».Delta_eq_chi_diff hx0 hx).symm
  show _ ≤ R11P x
  unfold R11P
  rw [if_pos hx, h]

/-- Hence the P14 Claim really follows through the NEW, reduced (Devetak) route. -/
theorem R12_P14_via_devetak : «private-boundary».Claim R11I :=
  «private-boundary».Claim_of_devetak R11I R12_hdev

/-- Non-triviality of the WP-C conclusion in this model: the Holevo difference is a genuinely
positive number on `(0, 1/2)`, so `chiB` and `chiE` do not both collapse to `0`. -/
example : ∀ x : ℝ, 0 < x → x < 1 / 2 →
    0 < «private-boundary».chiB x (Support.epsC x / 2) (Support.epsC x / 2) (Real.sqrt 2)
        - «private-boundary».chiE x (Support.epsC x / 2) (Support.epsC x / 2) (Real.sqrt 2) := by
  intro x hx0 hx
  rw [← «private-boundary».Delta_eq_chi_diff hx0 hx]
  exact («private-boundary».Delta_closed_form_pos hx0 hx).2

/-! ## 3c. The NEW LEAN-5 (entropy-level) bridge is inhabited in the SAME model

**Provenance / credit (R15 minor m3, 2026-08-01).**  LEAN-5 WP-H shipped a third bridge
theorem — `«no-ascent-hierarchy».Claim_of_entropy_witness`, whose hypothesis `hach'` is
stated over the von Neumann entropy difference `S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` rather than
over the `IcScalar` formula — without extending this module, so it had no *in-tree* §7.10.5
inhabitation certificate (the executor disclosed the omission in its report §7.4).  The
three declarations below are the fresh-instance **R15 reviewer's** out-of-tree certificate
(`artifacts/logs_whgap_lean5_20260801/r15_satisfiability.txt`, compiled with
`lake env lean`, exit 0, standard axioms), reproduced here **with credit and unchanged in
substance** so that the vacuity check ships with the development; only the namespace
qualifiers were adapted to this file.  The reviewer's two non-triviality `example`s for
`IcLB` are reproduced as well.  Same model `R11I` as §§1–3b. -/

/-- `Claim_of_entropy_witness`'s `hach'` is inhabited in the R11 model, so the new LEAN-5
(entropy) route into P9 is **not vacuous**.  (R15 §4c.) -/
theorem R15_hach' :
    ∀ x ε : ℝ, 0 < x → x < 2 / 5 → 0 < ε → ε < 1 →
      0 < Support.vnEntropyC (Support.Channel.LamWit_isHermitian x ε)
            - Support.vnEntropyC (Support.Channel.LamCWit_isHermitian x ε
                (Real.sqrt (x * (1 - x) / 2))) →
      R11I.IcLB x (Support.vnEntropyC (Support.Channel.LamWit_isHermitian x ε)
            - Support.vnEntropyC (Support.Channel.LamCWit_isHermitian x ε
                (Real.sqrt (x * (1 - x) / 2)))) := by
  intro x ε hx0 hx25 _ _ hpos
  exact ⟨hx0, hx25, hpos⟩

/-- Hence the P9 `Claim` really follows through the NEW (entropy) route: not vacuous. -/
theorem R15_P9_via_entropy : «no-ascent-hierarchy».Claim R11I :=
  «no-ascent-hierarchy».Claim_of_entropy_witness R11I R15_hach'

/-- Non-triviality of the model's `IcLB`: it is NOT `fun _ _ => True` — it fails at `c ≤ 0`
and off the interval — so the certificate above is not discharged by a degenerate
predicate. -/
example : ¬ R11I.IcLB (1 / 5 : ℝ) 0 := by
  rintro ⟨-, -, h⟩; exact lt_irrefl 0 h

example : ¬ R11I.IcLB (1 / 2 : ℝ) 1 := by
  rintro ⟨-, h, -⟩; norm_num at h

/-- The claimed equivalence `hach ↔ hach'` is real, in BOTH directions, and holds for an
ARBITRARY `CapacityInterface` (not just `R11I`), from `entropy_witness_eq_IcScalar` alone.
This is what makes the LEAN-5 reduction a change in *what the hypothesis is about* and not a
weakening of its logical strength — the over-claim guard recorded in `Trust.lean`. -/
theorem R15_hach_iff_hach' (I : CapacityInterface) :
    (∀ x ε : ℝ, 0 < x → x < 2 / 5 → 0 < ε → ε < 1 → 0 < Support.IcScalar x ε →
        I.IcLB x (Support.IcScalar x ε))
    ↔ (∀ x ε : ℝ, 0 < x → x < 2 / 5 → 0 < ε → ε < 1 →
        0 < Support.vnEntropyC (Support.Channel.LamWit_isHermitian x ε)
              - Support.vnEntropyC (Support.Channel.LamCWit_isHermitian x ε
                  (Real.sqrt (x * (1 - x) / 2))) →
        I.IcLB x (Support.vnEntropyC (Support.Channel.LamWit_isHermitian x ε)
              - Support.vnEntropyC (Support.Channel.LamCWit_isHermitian x ε
                  (Real.sqrt (x * (1 - x) / 2))))) := by
  constructor
  · intro h x ε hx0 hx25 hε0 hε1 hpos
    rw [«no-ascent-hierarchy».entropy_witness_eq_IcScalar hx0 hx25 ε] at hpos ⊢
    exact h x ε hx0 hx25 hε0 hε1 hpos
  · intro h x ε hx0 hx25 hε0 hε1 hpos
    have hE := h x ε hx0 hx25 hε0 hε1
      (by rw [«no-ascent-hierarchy».entropy_witness_eq_IcScalar hx0 hx25 ε]; exact hpos)
    rwa [«no-ascent-hierarchy».entropy_witness_eq_IcScalar hx0 hx25 ε] at hE

/-! ## 4. `Delta_closed_form_pos` really has no extra hypothesis -/

example (x : ℝ) (hx0 : 0 < x) (hx : x < 1 / 2) : 0 < WHGAP.Support.Delta x :=
  (WHGAP.«private-boundary».Delta_closed_form_pos hx0 hx).2

example (x r : ℝ) (hx0 : 0 < x) (hx : x < 1 / 2) (hr : 0 < r) :
    WHGAP.Support.u x (WHGAP.Support.epsC x / 2) r / WHGAP.Support.b x (WHGAP.Support.epsC x / 2)
      = WHGAP.Support.v x (WHGAP.Support.epsC x / 2) r
        / WHGAP.Support.e x (WHGAP.Support.epsC x / 2) := by
  obtain ⟨h1, h2⟩ := WHGAP.«private-boundary».argument_coincidence hx0 hx hr
  rw [h1, h2]

end WHGAP.Model

