---
id: "WHGAP.more-capable-route"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.more-capable-route.md"
aliases: ["P8"]
kind: LEAF
role: proof
status: OPEN
status_source: "registered-2026-07-29 (relaxation exploration brainstorm)"
disposition: PARKED
reason: "For complement pairs, complete more-capable collapses to plain more-capable (HRSF22 Prop 3.3) which for our family is exactly Q^(1)=0; its tensorization IS the coherent-information regularization problem — no certificate shortcut on this axis."
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.order-boundary", "WHGAP.qpositive-onset"]
---

# WHGAP.more-capable-route — Certify the strip via the (weaker) more-capable order? PARKED

## Claim

Certify Q(Lambda_x) = 0 on part of the strip (x_1, 1/2) through the more-capable order
(the weakest order in the Watanabe hierarchy that still kills Q). **[OPEN, PARKED]**

## Role in DAG

Registered per rule 8b during the 2026-07-29 relaxation brainstorm as the third relaxation
axis (weaken the ORDER rather than the certificate). Parked immediately after the HRSF22
literature check.

## Current status

PARKED. Reason (decision-layer analysis, 2026-07-29): HRSF22 Proposition 3.3 shows that for a
channel and its complement the COMPLETE more-capable order is equivalent to the plain one,
and — via the pure-state identity I(A⟩B) = I(X:B) − I(X:E) with I(A⟩E) = −I(A⟩B) on pure
tripartite states — plain more-capable of the complement pair is equivalent to Q^{(1)} = 0.
By P3, Q^{(1)}(Lambda_x) = 0 (numerically) throughout (≈0.395, 1/2), so the order "holds"
there for free; but running the pipeline needs the order to TENSORIZE for complement pairs,
and that statement IS "coherent information does not superactivate for this family" — the
regularization problem itself, exactly what certificates were invented to bypass. Revival
condition: a proof of a tensorizing SUBCLASS of more-capable-for-complements that contains
our family (none known; HRSF22 leave general more-capable tensorization open/negative —
plain less-noisy tensorization is refuted by private-capacity superactivation).

## Dependencies

HRSF22 local PDF (Prop 3.3, Fig. 1, Lemma 3.1 context); P3 (single-letter picture in the strip).

## Work record

- 2026-07-29 — registered and parked in the same brainstorm session (rule 8b/8d); no
  commission.

## Evidence

None yet.

## Adversarial reviews

None yet.

## Open obligations

None while PARKED (revival condition stated in Current status).

## Status history

- 2026-07-29 — created OPEN + PARKED (decision-layer registration with reason).

## Lean

`lean: none` — PARKED (tensorization = the regularization problem); nothing to mechanize. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

