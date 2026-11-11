---
id: "WHGAP.order-converse"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.order-converse.md"
aliases: ["P11"]
kind: LEAF
role: proof
status: OPEN
status_source: "registered-2026-07-29 (necessary-condition brainstorm)"
disposition: null
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.order-boundary", "WHGAP.relaxed-lift", "WHGAP.more-capable-route"]
---

# WHGAP.order-converse — The exact characterization frame: regularized vs complete orders

## Claim

Organizing frame (definitional, to be written up and reviewed): for a channel/complement
pair, P(N) = 0 ⟺ N^c is REGULARIZED-less-noisy than N, and Q(N) = 0 ⟺ N^c is
REGULARIZED-more-capable than N (superadditivity of P^{(1)}, Q^{(1)} under self-tensoring
turns "limit = 0" into "every level = 0"). Hence the necessary-and-sufficient
characterization of zero capacity IS an order statement; the tractable sufficient side
(cBKM/cRE/complete-less-noisy) strengthens "regularized" to "complete". Research object:
the GAP between the regularized and complete orders on the Werner–Holevo family — does
reg-l.n. plus O(3)-covariance imply c-l.n. here (which would collapse necessary to
sufficient and decide the whole strip)? **[OPEN]**

## Role in DAG

Third prong of the necessary-condition brainstorm: instead of new inequalities, recognize
that the exact characterization already exists at the order level, and the entire strip
problem is the reg-vs-complete gap. E1 (`WHGAP.order-boundary`) measures the complete-side
boundary x_B; the strip's reg-side status is exactly "Q^{(1)}(Λ^{⊗n}) = 0 for all n" —
unknown beyond n = 2 probes. A covariance-collapses-the-gap theorem is the dream endgame;
a counterexample family (reg holds, complete fails, capacity still 0 or not) would be
equally decisive.

## Current status

OPEN. No commission yet — deliberately: this node's first work item is decision-layer
theory (write the equivalences rigorously; survey whether any collapse theorems exist),
gated on the outcomes of P6 (x_B) and P9 (no-ascent + distillation scans), which will say
where the gap actually bites on this family.

## Dependencies

HRSF22 local PDF (order definitions; Prop 3.3; Watanabe footnote); P6/P9 outcomes.

## Work record

- 2026-07-29 — node registered (rule 8b) at brainstorm time; deliberately not commissioned
  (theory-first item, sequenced after P6/P9 data).

## Evidence

None yet.

## Adversarial reviews

None yet.

## Open obligations

Write the reg-order equivalences as a reviewed lemma; then decide the collapse-question
attack after P6/P9 land.

## Status history

- 2026-07-29 — created OPEN (decision-layer registration).

## Lean

`lean: none` — OPEN frame, no proof content yet. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

