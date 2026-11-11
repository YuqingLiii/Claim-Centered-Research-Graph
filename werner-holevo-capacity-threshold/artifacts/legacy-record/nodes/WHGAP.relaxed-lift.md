---
id: "WHGAP.relaxed-lift"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.relaxed-lift.md"
aliases: ["P7"]
kind: LEAF
role: proof
status: CONJECTURED
status_source: "decision-layer derivation 2026-07-29 (criterion W soundness argued in-node; pending review)"
disposition: null
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.order-boundary", "WHGAP.signed-lift-extension"]
---

# WHGAP.relaxed-lift — The two-sided defect criterion (W): a strictly more permissive certificate

## Claim

**(Criterion W, soundness):** Let M, N be channels with M(1) ≻ 0, N(1) ≻ 0, and let J be ANY
complex-linear map (adjoint preservation NOT required) with J† ∘ N = M such that BOTH
operator-valued defects
Δ^L_J(τ) = L_{M(τ)} − J† L_{N(τ)} J  and  Δ^R_J(τ) = R_{M(τ)} − J† R_{N(τ)} J
are completely positive. Then N ⪰_cBKM M (and the ZW capacity pipeline applies).
Secondary conjecture (completeness): every cBKM domination admits such a (W)-certificate,
possibly after group averaging. **[CONJECTURED — pending-review]**

## Role in DAG

Decision-layer answer to "is the signed-lift condition optimal?" — NO, at the formal level:
ZW's hypothesis (adjoint-preserving J + LEFT defect CP) is one sufficient route to the
inequality family J† A_{ω,t} J ⪯ A_{σ,t}, A_{θ,t} = (1−t)L_θ + tR_θ, t ∈ [0,1], that the
proof actually consumes. Since A_{θ,t} is LINEAR in t, the t-family holds iff it holds at
t = 0 AND t = 1 — i.e., iff both one-sided defects are CP — with NO reality/adjoint condition
on J. Every ZW certificate is a (W)-certificate (adjoint preservation + left CP ⟹ right CP by
mirroring); the converse enlarges the search space by the complex directions (e.g. Im-parts of
all five covariant coefficients, the direction flagged by the external R2-era review).

## Current status

CONJECTURED (proposer = decision layer; pending-review). Soundness derivation (in-context,
2026-07-29): Lemma 3.5 of ZW amplifies each one-sided CP defect to references verbatim;
Lemma 3.6's variational step ⟨W, A^{-1}W⟩ = sup_V [2Re⟨W,V⟩ − ⟨V, A V⟩] uses only
J† A_ω J ⪯ A_σ and linearity of J — nowhere adjoint preservation; the t-integral
Γ_θ^{-1} = ∫ A_{θ,t}^{-1} dt then yields the BKM comparison. Needs: a written lemma +
independent review; then the (W)-feasibility scan below 1/2 for our family becomes the
operational question (commissioned as E2). Note the a-priori bound: (W)-certificates exist at
x only if the cBKM order holds at x, so the feasible region is contained in the
[[WHGAP.order-boundary]] region.

## Dependencies

- ZW local PDF Lemmas 3.5/3.6 (the proof skeleton being relaxed).
- P2 machinery (covariant ansatz, spin reduction) — reusable wholesale for the complex ansatz.

## Work record

- 2026-07-29 — node registered (rule 8b) with the soundness derivation recorded above;
  commission [WHGAP_COMMISSION_P6_20260729.md](../../notes/WHGAP_COMMISSION_P6_20260729.md)
  (E2 part) authored the same day: symbolic soundness check of (W) + complex-covariant
  feasibility scan below 1/2.
- 2026-07-29 - P6 E2 completed without changing this decision-layer-owned status. D2
  passed 200 complex-linear instances and 4,000 random Hermitian-direction inequalities.
  S3 used the true Hilbert--Schmidt adjoint, found real constraint rank 6 (residual real
  dimension 6), recovered the real forced solutions at 13/25 and 1/2, and found no
  two-sided-defect feasibility at 49/100, 47/100, or 9/20 under 100 restarts per point.
  Artifact: [whgap_p6_relaxation_20260729.md](../../../../artifacts/whgap_p6_relaxation_20260729.md).

## Evidence

- 2026-07-29 - proposer-authored numerical/symbolic evidence only:
  [P6 artifact](../../../../artifacts/whgap_p6_relaxation_20260729.md),
  [D2 JSON](../../../../artifacts/logs_whgap_p6_20260729/d2_soundness.json),
  [S3 JSON](../../../../artifacts/logs_whgap_p6_20260729/s3_feasibility.json), and
  [SHA256 provenance](../../../../artifacts/logs_whgap_p6_20260729/SHA256SUMS.txt).
  G2-E2(b) applies within the complex covariant ansatz; no below-1/2 certificate was found.
  The spin commutator residual is at most 6.1e-16. Status remains CONJECTURED.

- 2026-07-29 (late) — direction closed below 1/2: the lead's analytic BKM-necessity witness
  (see [[WHGAP.order-boundary]]) shows the TARGET order itself fails for every x < 1/2, so
  no certificate — (W) or otherwise — that implies cRE can reach below 1/2. (W) remains a
  sound and paper-worthy formal relaxation lemma; its below-1/2 feasibility question is
  resolved negatively in principle (consistent with the P6-E2 empirical null, now explained).
  The genuinely-new-mechanism target moves to [[WHGAP.restricted-order]].

## Adversarial reviews

None yet.

## Open obligations

E2 execution; then a written soundness lemma + rule-7 review (the completion gate); the
completeness conjecture is a separate later work item.

## Status history

- 2026-07-29 — created CONJECTURED (decision-layer derivation; pending-review).

## Lean

`lean: none` — conjectured criterion, no reviewed scalar core yet. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

