---
id: "WHGAP.choi-distillation-necessary"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.choi-distillation-necessary.md"
aliases: ["P10"]
kind: LEAF
role: proof
status: NUMERICAL
status_source: "P9-E2 bounded filtered-hashing scan 2026-07-29; pending-review"
disposition: null
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.no-ascent-hierarchy", "WHGAP.qpositive-onset"]
---

# WHGAP.choi-distillation-necessary — Q = 0 forces one-way undistillability of the Choi state

## Claim

Necessary condition: Q(Lambda_x) = 0 implies the Choi state omega_x has zero one-way
distillable entanglement, D_→(omega_x) = 0 (teleportation reduction: one channel use
distributes omega_x, so D_→(omega_x) ≤ Q(Lambda_x)). Contrapositive program: exhibit a
one-way distillation protocol with positive rate on omega_x for some x in the strip
(x_1, 1/2) to PROVE Q > 0 there. **[NUMERICAL — pending-review]**

## Role in DAG

Second prong of the 2026-07-29 necessary-condition brainstorm: imports the
entanglement-distillation toolbox (hashing on filtered states, recurrence + hashing,
breeding variants — see the sibling field tree `entanglement-distillation/`) into the strip.
Note omega_x is NPT for all x < 1 while (if Q = 0 persists below 1/2) it would be one-way
undistillable — making the strip's Choi states one-way-NPT-bound-entanglement candidates,
directly connected to the NPTBE campaign.

## Current status

NUMERICAL (`pending-review:` P9-E2 bounded-null). Direct Choi hashing matched
\(I_c(\pi)\) and crossed zero at
\(x_1=0.3909102320761813234827218531342\ldots\). At each strip point
\(\{21/50,11/25,23/50,12/25,49/100\}\), 273 direction-valid one-copy filtered-hashing
trials and 36 direction-valid correlated two-copy trials found no rate above
\(10^{-10}\) bits/use. The \(77/200\) anchor was positive, while \(1/2\) and \(11/20\)
were at floor. This is a searched-family bounded null, not evidence of
undistillability. A preliminary arbitrary two-sided-postselection pass was rejected
because it produced false positives at the proved-zero anchors; Bob-side success
conditioning would require backward communication and is outside the registered
one-way \(A\to B\) interpretation.

## Dependencies

P4 (calibration regime); P3 (strip picture); entanglement-distillation field literature.

## Work record

- 2026-07-29 — P9-E2 completed D2 and S3 in 14.750 s. D2 reproduced the exact Choi
  spectrum \(\{1-x,x/3,x/3,x/3,0^5\}\), the hashing formula, and the \(x_1\)
  sign change. The direction-valid S3 inventory per point was 117 diagonal
  rank-\(\le3\)/projector starts, 36 real \(O(3)\)-adapted projectors, 120 random
  complex low-rank Alice filters, six named correlated two-copy projectors, and 30
  random correlated low-rank two-copy Alice filters. G2-E2 outcome: bounded-null.

- 2026-07-29 — node registered (rule 8b) at brainstorm time; first bounded scan folded into
  commission [WHGAP_COMMISSION_P9_20260729.md](../../notes/WHGAP_COMMISSION_P9_20260729.md)
  (E2 part; queued behind P6).

## Evidence

- 2026-07-29 — P9-E2:
  [P9 execution artifact](../../../../artifacts/whgap_p9_necessary_20260729.md),
  [direction-valid JSON](../../../../artifacts/logs_whgap_p9_20260729/distillation_scan_direction_valid.json),
  [raw log](../../../../artifacts/logs_whgap_p9_20260729/distillation_scan_direction_valid.log),
  and [script](../../../../tools/whgap_p9_distillation.py). Script SHA-256
  `f3caa03064103a0e12d7f67cef38955889883d5cf778e1d7f0f728f9c43f1823`;
  JSON SHA-256
  `0e433f81ef3df6e9f10eef9428c47121691774784606ce90ac0031e81d1701bf`.
  The rejected two-sided-postselection calibration is preserved as
  [JSON](../../../../artifacts/logs_whgap_p9_20260729/distillation_scan.json) and
  [log](../../../../artifacts/logs_whgap_p9_20260729/distillation_scan.log), JSON
  SHA-256 `863ea5010bc204499f8266b9f96a95603d46e1396181ac27c49eb41a9012d9c3`.
  `pending-review:` no independent rule-7 review has been completed.

## Adversarial reviews

None yet.

## Open obligations

Independent rule-7 review of P9-E2; then assess whether deeper genuinely one-way
distillation attacks warrant their own registered campaign.

## Status history

- 2026-07-29 — OPEN -> NUMERICAL after P9-E2 D2/S3 bounded scan
  (`pending-review:`; no positive strip rate found in the registered families).

- 2026-07-29 — created OPEN (decision-layer registration).

## Lean

`lean: none` — numerical probe evidence only; no scalar core. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

