import WHGAP.Interface
import WHGAP.Support.DefectChoi

/-!
# `WHGAP.signed-lift-extension` (P2)

* node id: `WHGAP.signed-lift-extension`
* node file: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.signed-lift-extension.md`
* epistemic status on disk (2026-07-30): **CERTIFIED\*** — certificate core PROVED-licensed
  by the R2 review; the capacity clause is delegated to `WHGAP.zero-capacity-application`.
* mechanization state: `stated` (Claim) + `proved` (the T2 algebraic core below);
  `rel`: the whole `SignedLiftCP` predicate is an interface field, see the fidelity note.

## Frozen Claim (verbatim from the node file, `## Claim` section)

The signed-lift CP-defect certificate extends to an interval x in [1/2, x_max] with x_max > 1/2, yielding Q(Lambda_x) = P(Lambda_x) = 0 there with exact rational certificates. **[CERTIFIED\* — certificate core PROVED-licensed by R2 (region [1/2,1), unique lift, exact certificates, twirling ingredients); the "yielding Q=P=0" clause is tracked at [[WHGAP.zero-capacity-application]]]**

* frozen-claim SHA-256 (LF bytes of the section body, blank-line-stripped):
  `6283cddf584e71b7bad87ca1c9dd0a836c1b3e19242ea882fe1e560d149cf757`

## Statement-fidelity note (G-L5)

`Claim I` below says only: *the signed-lift CP-defect predicate holds at every `x ∈ [1/2,1)`.*
The prose Claim additionally asserts (i) the concrete five-real-parameter covariant ansatz and
its unique residual point, (ii) exact rational certificates, and (iii) the `Q = P = 0`
consequence.  (iii) is deliberately elsewhere (`WHGAP.zero-capacity-application`), matching the
node's own scoping.  (i) and (ii) are **not** representable at this tier: `SignedLiftCP` is an
opaque interface field, so nothing about matrices, spins, or PSD-ness is checked here.  What
*is* machine-checked in this module is the displayed **algebraic core** of the R2 uniqueness /
spectrum computation: the two forcing identities of paper Prop 3.2 and the sign analysis of the
two defect eigenvalue branches.  Those are rational-function identities in `(x, p, d)`; they
verify the *displayed identities*, not the 27×27 construction they came from.
-/

namespace WHGAP.«signed-lift-extension»

open WHGAP WHGAP.Support

/-- **P2 Claim, tier-1 form.**  The signed-lift CP-defect certificate is available on all of
`[1/2, 1)`.  (The `Q = P = 0` clause of the prose claim is `WHGAP.zero-capacity-application`.) -/
def Claim (I : CapacityInterface) : Prop :=
  ∀ x : ℝ, 1 / 2 ≤ x → x < 1 → I.SignedLiftCP x

/-! ## T2 core — the forcing identities of paper Prop 3.2 (uniqueness computation) -/

/-- First forcing identity: the four displayed contributions of the `p`-sector collapse to
`(3p-1)²(x-1)/x`.  Rational-function identity, valid for every `x ≠ 0`. -/
theorem forcing_p (x p : ℝ) (hx : x ≠ 0) :
    (p - 1) * (x - 1) * (p + 2 * x - 1) / x
      + 4 * ((x - 1) * (2 * p ^ 2 + p * x - 2 * p + x)) / (2 * x)
      + 2 * ((x - 1) * (p ^ 2 - p * x - 2 * x + 1)) / x
      + 2 * ((x - 1) * (p ^ 2 - p * x + 2 * x - 1)) / x
    = (3 * p - 1) ^ 2 * (x - 1) / x := by
  field_simp
  ring

/-- Second forcing identity: the two displayed contributions of the `d`-sector collapse to
`-(3d + 2x - 2)²/x`.  Rational-function identity, valid for every `x ≠ 0`. -/
theorem forcing_d (x d : ℝ) (hx : x ≠ 0) :
    2 * (-(9 * d ^ 2 + 4 * d * x - 8 * d + 4 * x ^ 2 - 8 * x + 4) / (2 * x))
      + 2 * (-(2 * d * (2 * x - 1)) / x)
    = -(3 * d + 2 * x - 2) ^ 2 / x := by
  field_simp
  ring

/-! ## T2 core — sign analysis of the two defect eigenvalue branches

**R12 minor m4 (2026-07-31).**  This section used to carry its OWN copies of `lam5`/`lam3`,
definitionally identical to `WHGAP.DefectChoi.lam5`/`lam3` but formally unrelated to them, so
that the "serves P2" relation asserted in `WHGAP/Support/DefectChoi.lean` was merely nominal
and editing one copy would silently desynchronize the other.  The duplicates are **deleted**;
the three sign theorems below are now stated about `DefectChoi.lam5`/`DefectChoi.lam3`
themselves, which is the smaller of the two repairs R12 offered (delete-and-reuse rather than
add-two-bridging-lemmas) and makes the dependency real: `defect_eigenvalues_sign` now
genuinely consumes the WP-A spectrum core. -/

/-- On `0 < x < 1` the `λ₅` branch is nonnegative exactly on `x ≥ 1/2`: this is the
threshold that pins the lower endpoint of the defect-PSD region at `1/2`. -/
theorem lam5_nonneg_iff {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    0 ≤ DefectChoi.lam5 x ↔ 1 / 2 ≤ x := by
  unfold DefectChoi.lam5
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have hneg : 4 * (1 - x) * (2 * x - 1) / x < 0 :=
      div_neg_of_neg_of_pos (by nlinarith) hx0
    linarith
  · intro h
    exact div_nonneg (by nlinarith) hx0.le

/-- On `0 < x < 1` the `λ₃` branch is nonnegative exactly on `x ≥ 1/3`. -/
theorem lam3_nonneg_iff {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    0 ≤ DefectChoi.lam3 x ↔ 1 / 3 ≤ x := by
  unfold DefectChoi.lam3
  have h9 : (0:ℝ) < 9 * x := by linarith
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have hneg : 16 * (1 - x) * (3 * x - 1) / (9 * x) < 0 :=
      div_neg_of_neg_of_pos (by nlinarith) h9
    linarith
  · intro h
    exact div_nonneg (by nlinarith) h9.le

/-- Both branches are simultaneously nonnegative exactly on `x ≥ 1/2` (the `λ₅` branch is the
binding one), which is the sign statement behind the R2 feasible region `[1/2, 1)`. -/
theorem defect_eigenvalues_sign {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    (0 ≤ DefectChoi.lam5 x ∧ 0 ≤ DefectChoi.lam3 x) ↔ 1 / 2 ≤ x := by
  constructor
  · rintro ⟨h5, -⟩
    exact (lam5_nonneg_iff hx0 hx1).mp h5
  · intro h
    exact ⟨(lam5_nonneg_iff hx0 hx1).mpr h,
           (lam3_nonneg_iff hx0 hx1).mpr (by linarith)⟩

end WHGAP.«signed-lift-extension»

