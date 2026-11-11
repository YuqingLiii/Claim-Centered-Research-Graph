import WHGAP.Support.Basic

/-!
# WHGAP.Interface — the trust boundary (DAG protocol §7.3, §7.5)

This file contains **no invented proofs**.  It bundles, as fields of a structure, exactly the
external results that the WHGAP composition theorems consume.  Per `DAG_PROTOCOL.md` §7.5:

> A theorem proved against an abstract interface is exactly as strong as the results that
> interface cites, and not one notch stronger.

Nothing below is checked by Lean.  Each field is an assumption with its citation.

## The abstracted objects

`Q`, `P`, `Qone`, `Pone : ℝ → ℝ` are the quantum capacity, private capacity, and their
one-shot (single-letter) versions of the noisy Werner–Holevo channel `Λ_x`, indexed by the
noise parameter `x`.  They are *fields*, not definitions: no Hilbert space, channel, Choi
matrix, or entropy appears anywhere in this development.  A green build therefore says
nothing whatsoever about whether these four functions are the capacities of `Λ_x`.

`SignedLiftCP x` abstracts "the covariant signed lift `J_x` of `WHGAP.signed-lift-extension`
exists at `x` and its defect map is completely positive".

`IcLB x c` abstracts "the coherent information of `Λ_x` admits, at some input state and some
blocklength, the strictly positive lower bound `c`".
-/

namespace WHGAP

/-- The cited-external-results trust boundary for the WHGAP DAG.

Every composition theorem in this development takes an `I : CapacityInterface` and is exactly
as strong as the four citations below.  There are deliberately **no** other fields: an
obligation that is not one of these is carried as an explicit theorem hypothesis instead
(DAG protocol §7.5), so that it stays visible in the theorem type. -/
structure CapacityInterface where
  /-- Quantum capacity of `Λ_x` as a function of the noise parameter `x`. -/
  Q : ℝ → ℝ
  /-- Private capacity of `Λ_x`. -/
  P : ℝ → ℝ
  /-- One-shot (single-letter) quantum capacity `Q^{(1)}`. -/
  Qone : ℝ → ℝ
  /-- One-shot (single-letter) private capacity `P^{(1)}`. -/
  Pone : ℝ → ℝ
  /-- "The covariant signed lift is available and its defect is CP at `x`." -/
  SignedLiftCP : ℝ → Prop
  /-- "`c` is a strictly positive achievable coherent-information value at `x`." -/
  IcLB : ℝ → ℝ → Prop
  /-- **Cited: Lloyd–Shor–Devetak.**  Regularized capacities dominate their one-shot versions
  (superadditivity of the coherent information / private information over blocklengths).
  Local citation: Zhu–Wang arXiv:2607.24693, eq. **(2.3)/(2.4)** (the *quantum* pair: the
  definition of `Q^{(1)}` and the regularized `Q = lim_n (1/n) Q^{(1)}(N^{⊗n})`) **and
  (2.6)/(2.7)** (the *private* pair, likewise); Llo97, Dev05.  (ZW display (2.4) in limit form
  only, so the `Qone x ≤ Q x` half additionally rests on superadditivity of the coherent
  information over blocklengths, which is what makes the limit a supremum; the private half is
  displayed as a supremum in (2.7).) -/
  lsd_devetak : ∀ x, Qone x ≤ Q x ∧ Pone x ≤ P x
  /-- **Cited: the Zhu–Wang signed-lift zero-capacity criterion, tensorized.**  If the signed
  lift has CP defect at `x`, then all four capacities vanish at `x`.
  Local citation: Zhu–Wang arXiv:2607.24693 Thm 3.3 + Lem 3.2 + Cor 3.7 (criterion),
  BGSW25 (cBKM → cRE bridge), HRSF22 Lem 3.1 read through the local Zhu–Wang statement
  (hybrid tensorization, i.e. the step that upgrades the one-shot conclusion to every
  blocklength).  This is exactly the interface consumed by
  `WHGAP.zero-capacity-application` (P4, node status PROVED via the R3 review). -/
  zw_hrsf_zero : ∀ x, SignedLiftCP x → Qone x = 0 ∧ Pone x = 0 ∧ Q x = 0 ∧ P x = 0
  /-- **Cited: Lloyd–Shor–Devetak achievability.**  A strictly positive achievable coherent
  information at `x` forces `Q x > 0`.  Local citation: the same LSD/Devetak interface as
  `lsd_devetak`, as used by Theorem 8.1 of
  `notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` (R5d review, LICENSE A). -/
  q_pos_of_ic_pos : ∀ x c, 0 < c → IcLB x c → 0 < Q x

end WHGAP

