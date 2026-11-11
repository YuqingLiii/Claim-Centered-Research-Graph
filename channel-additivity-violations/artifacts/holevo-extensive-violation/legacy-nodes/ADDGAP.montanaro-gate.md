---
id: "ADDGAP.montanaro-gate"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.montanaro-gate.md"
aliases: ["P2a"]
kind: LEAF
role: proof
status: OPEN
status_source: "negative scope audit in notes/MONTANARO_GATE_2026-08-29.md; independent review pending"
disposition: PARKED
parents: ["ADDGAP.matched-independent-tensors"]
children: []
related: ["ADDGAP.goal"]
---

# ADDGAP.montanaro-gate — does weak multiplicativity control leakage?

## Claim

Determine whether Montanaro's weak multiplicativity theorem for random quantum channels implies,
in a regime compatible with a positive `p=1` matched-pair gap and uniformly for a growing number of
independent factors,

`alpha_r+beta_r=o(r)`

for the leakage terms defined in `ADDGAP.matched-independent-tensors`.

## Role in DAG

Pre-registered stop/go gate for the matched-independent amplification route.

## Current status

OPEN / PARKED. Exact source extraction gives a negative scope result: the theorem supplies a
constant-fraction or constant-additive loss per factor, not the sublinear-in-copy-number leakage
required by the parent blueprint. This is not stamped REFUTED because no independent rule-6/7 review
has been completed.

## Dependencies

Ashley Montanaro, *Weak Multiplicativity for Random Quantum Channels*, Commun. Math. Phys. 319
(2013), arXiv:1112.5271; the random-channel parameter regime used by the `p=1` additivity violation.

## Work record

- 2026-08-29 — Fukuda's concluding remarks identified Montanaro as the relevant published weak-
  additivity result. Initial abstract-level inspection suggests the balanced regime may only give a
  constant-fraction entropy bound, which would leave `Theta(r)` leakage and fail this gate; exact
  formulas are being checked before adjudication.
- 2026-08-29 — exact arXiv source checked. The theorem's exponents are
  `1/2-9/log2(d_A d_B/r)` and `1-9/log2(d_A)`; the von-Neumann corollary loses a universal constant
  per copy even in the stronger regime. For BCN, `(d_A,d_B,r)=(k,n,tkn)` and every fixed-`t`
  violation, especially `t=1/2`, lies in the first regime, where the lower bound per copy collapses
  to `(1/2)log(1/t)-C` while one-copy entropy is order `log k`. The full audit and diagnostic BCN
  boundary computation are in `../../notes/MONTANARO_GATE_2026-08-29.md`.

## Evidence

Primary-source locators: `https://arxiv.org/abs/1112.5271` and
`https://arxiv.org/abs/1305.1567`; extracted comparison:
`../../notes/MONTANARO_GATE_2026-08-29.md`.

## Adversarial reviews

None yet.

## Open obligations

- Obtain an independent rule-6/7 scope review before any REFUTED/DEAD status.
- Restart only with an improved theorem giving per-factor loss `o(g_k)` uniformly in tensor power,
  or a base gap exceeding twice an explicit constant-loss coefficient.

## Status history

- 2026-08-29 — created OPEN before theorem verification.
- 2026-08-29 — retained OPEN but disposition changed to PARKED after negative quantitative scope
  audit; independent review pending.

