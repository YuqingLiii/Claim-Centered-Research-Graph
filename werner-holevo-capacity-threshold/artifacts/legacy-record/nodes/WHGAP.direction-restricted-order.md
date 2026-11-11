---
id: "WHGAP.direction-restricted-order"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.direction-restricted-order.md"
aliases: ["P16"]
kind: LEAF
role: proof
status: REFUTED
status_source: "R10 review 2026-07-30 (artifacts/whgap_r10_review_20260730.md) confirming the P16-A note's recommendation and strengthening it with two corrections; applied by the decision layer 2026-07-30"
reason: "Isotypic-type direction restrictions are vacuous for the coherent-information step (exact theorem: every purification pair against any product anchor has strictly positive spin-2 norm), false inside the strip (certified violations at x = 0.42, 0.45, 0.46), and unstable under tensoring."
disposition: DEAD
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.restricted-order", "WHGAP.pure-anchor-order", "WHGAP.order-boundary"]
---

# WHGAP.direction-restricted-order — Orders that exclude the spin-2 breaking directions

## Claim

Is there a relative-entropy-domination order restricted by DIRECTION rather than by state
purity — one that excludes the spin-2 perturbation directions in which the necessity
witness breaks cBKM, while retaining the purification pairs the coherent-information proof
consumes — that (i) holds for Lambda_x at some x in [2/5, 1/2) and (ii) tensorizes?
**[OPEN — explicitly UNDECIDED, not dead]**

## Role in DAG

This is the candidate [[WHGAP.restricted-order]] itself proposed at registration ("a
viable restricted order must EXCLUDE those [spin-2] pairs while keeping the purification
pairs"). The P12-A note's §8 headline declared every class containing mixed pairs
arbitrarily close to a pure state to be dead; **R8 MAJOR 1 showed that quantifier is
broken** — the private-capacity witness kills only classes containing the SPECIFIC pairs
w(x,eps) = (rho_eps + eps X, rho_eps), and X lies in the spin-2 sector (R5b claim 5), so a
direction-restricted class can contain mixed pairs arbitrarily close to pure states and
still never contain the witness. Nothing proved so far bears on it, so it is registered
here rather than left buried inside a refuted headline (rule 8b/8d: every candidate
terminates in an explicit state).

## Current status

OPEN, no work done. Design questions to settle before any commission:
1. **Is a direction-restricted class even an order?** Restricting the admissible
   perturbation directions at each base point defines a cone field, not a state-pair class;
   the relative-entropy version needs the restriction to be stable under the operations the
   capacity proof performs (in particular under attaching references and under tensoring),
   or the induction cannot start.
2. **Does the exclusion survive covariance?** The spin-2 sector is an O(3)-isotypic
   component, so "exclude spin-2" is a covariant restriction — promising, since our whole
   certificate story is covariant. But the purification pairs must be checked to have
   nonzero spin-2 content or the restriction is vacuous/inconsistent.
3. **Falsification anchor (binding on any future commission):** the class must FAIL on
   (0, 2/5) where Q > 0 is PROVED, or it cannot imply Q = 0.

## Dependencies

Paper §5 / R5b (the witness lives in the spin-2 sector — the fact that makes this class
conceivable); [[WHGAP.private-boundary]] (what kills the unrestricted classes);
[[WHGAP.restricted-order]] (parent programme).

## Work record

- 2026-07-30 — node registered (rule 8b) by the decision layer while applying R8 MAJOR 1.
- 2026-07-30 — commission P16-A dispatched
  ([WHGAP_COMMISSION_P15A_P16A_20260730.md](../../notes/WHGAP_COMMISSION_P15A_P16A_20260730.md),
  Track B) and executed in full; note
  [WHGAP_P16A_DIRECTION_20260730.md](../../notes/WHGAP_P16A_DIRECTION_20260730.md).

## Evidence

- 2026-07-30 — **P16-A: three independent kills.** Calibration first (own BKM code, own
  complement, isotypic projectors built TWO ways — closed form and Casimir Σ ad², spectrum
  {0,2,6} with multiplicities 1/3/5, agreeing to 1.2e-15): reproduces R5b's closed forms
  and independently re-confirms that the necessity witness direction X is **exactly** pure
  spin-2 (fraction 1.000000).
  **Four definitions** were made precise: D1 pair class {(ρ,σ) : Π₂(ρ−σ) = 0}; D2 the
  constant cone field {Z : Π₂Z = 0}; D3 exclude only purely-spin-2 directions; D4 the
  quantitative cone ‖Π₂Z‖² ≤ (1−η)‖Z‖². Lemma 0 proves D1 ⟺ D2 via the integral identity
  D(ρ‖σ) = ∫₀¹(1−t) g_{σ+t(ρ−σ)}(ρ−σ) dt.
  **Kill 1 — vacuity, as an EXACT theorem (not "generically"):** for every pure ψ_RA and
  ANY product anchor ψ_R ⊗ σ_A,
  ‖Π₂(ψ_RA − ψ_R⊗σ_A)‖² = Σ_{j≠k} p_j p_k (1+|u_jᵀu_k|²)/2 + Σ_j p_j² ‖P₂(|u_j⟩⟨u_j| − σ_A)‖²
  ≥ (1 − Tr ρ_A²)/2 > 0 for every entangled ψ — the R-off-diagonal Schmidt blocks are
  untouched by any product anchor. So D1/D2 exclude **every** pair the
  coherent-information step consumes and cannot imply Q = 0. D3 dies by a density argument
  (Lemma 1: the admissible set is dense, so D3 ≡ unrestricted cBKM, PROVED false below
  1/2), which yields the design constraint that any usable direction restriction must
  exclude an OPEN cone.
  **Kill 2 — falsity inside the strip:** chart-aware rationalization (direction in a
  15-element rational basis of the spin-2-free subspace; base point rationalized,
  Hermitized, trace-normalized, faithful), 60 dps: q/‖Z‖² = −0.2748977983804598939 at
  x = 0.42 and −0.0280809901650730336 at x = 0.45, both at d_R = 2 non-product base points.
  Falsification anchor satisfied (−5.07 at x = 0.2).
  **Kill 3 — tensor instability (this node's design question 1 = NO):** stable under
  attaching references (Π₂ = id ⊗ P₂) but NOT under tensoring in either convention —
  diagonal action (1⊗1 contains spin 2; measured total-spin-2 fractions 0.17–0.64 for
  products of spin-2-free operators) and per-copy action (ρ₁⊗ρ₂ − σ₁⊗σ₂ =
  (ρ₁−σ₁)⊗ρ₂ + σ₁⊗(ρ₂−σ₂) has copy-1 spin-2 fraction 0.11–0.19).
  Logs + SHA256SUMS_p16a.txt (13/13) under `artifacts/logs_whgap_p16a_20260730/`.

## Adversarial reviews

- 2026-07-30 — **R10 (fresh Opus instance, rule-7 complete): FINDINGS — 2 MAJOR, and BOTH
  corrections STRENGTHEN the kill.** The reviewer rebuilt the spin-2 isotypic
  decomposition by THREE independent routes (closed form; Casimir; Haar averaging against
  the spin-2 character), validated it against the character identity χ_V(O)² = χ₀+χ₁+χ₂
  (max err 1.8e-15), checked O(3) covariance and that −I acts trivially, and validated its
  own BKM code against second-order finite differences of the relative entropy. CONFIRMED:
  the calibration table digit-for-digit, X purely spin-2, dim of the spin-2-free subspace
  (3 at d_R=1, 15 at d_R=2), **Theorem B2 as an exact identity re-derived by hand** (1.0e-15
  at 40 samples over d_R ∈ {2,3,4}, marginal and non-marginal anchors; maximally entangled
  case 5/9, 8/9, 5/8), Lemma 0, Lemma 1, the x = 0.2 anchor, kill 3 in both covariance
  conventions, and the note's own SHA256SUMS.
  **MAJOR 1 (refutes an executor reservation):** "D4 survives B2" is FALSE — along the
  near-pure isotropic Schmidt family (exactly the family carrying our PROVED Q > 0
  mechanism) the spin-2 fraction of coherent-information pairs has supremum **1**, not
  0.72, so EVERY η ∈ (0,1] excludes CI pairs and D4 dies at B2 together with D1/D2/D3.
  **MAJOR 2 (refutes the other reservation):** the "no violation found at
  x ∈ {0.46,…,0.49}" bounded null is wrong at its first point — a violation is CERTIFIED at
  **x = 46/100** with exact rational faithful well-conditioned inputs at 60 dps,
  q = −2.408289498713903668891301.
  Report: [whgap_r10_review_20260730.md](../../../../artifacts/whgap_r10_review_20260730.md).
  R10's verdict: P16 = DEAD, **but only for the definitions D1–D4 as written** — the note's
  non-generalization disclaimer is accurate and is carried into this status write.

## Open obligations

None (DEAD). Carried non-claim, per R10: this refutes restrictions defined by the
**O(3)-isotypic type** of the difference/tangent direction. It does NOT refute
restrictions by a different geometric feature (e.g. base-point-coupled ones); such a
proposal would need its own node.

## Status history

- 2026-07-30 — created OPEN (rule 8b registration; R8 MAJOR 1 established that the
  existing no-go does not cover this class).
- 2026-07-30 — OPEN → **REFUTED / DEAD** (decision layer, citing the completed R10 review;
  rule 2 satisfied — the kill was authored by the P16-A executor and independently
  confirmed AND strengthened by a fresh reviewer). Reason in the front matter; scope limit
  (definitions D1–D4, isotypic-type restrictions) recorded above.

## Lean

`lean: none` — REFUTED/DEAD; the kill is numerical+exact-witness, mechanization not warranted. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

