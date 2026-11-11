---
id: "ADDGAP.pair-to-self"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.pair-to-self.md"
aliases: ["P1"]
kind: LEAF
role: proof
status: CONJECTURED
status_source: "notes/PAIR_TO_SELF_REDUCTION_2026-08-29.md; proposer-side proof pending independent review"
disposition: null
parents: ["ADDGAP.goal"]
children: []
related: ["ADDGAP.matched-independent-tensors"]
---

# ADDGAP.pair-to-self — quantitative pair-to-self Holevo reduction

## Claim

Let `chi` denote the one-shot Holevo quantity. If channels `N,M` have cross defect

`g = chi(N tensor M) - chi(N) - chi(M) > 0`,

then, after tensoring the smaller-`chi` side with a noiseless classical channel, there is a flagged
direct-sum channel `T` such that

`chi(T tensor T) - 2 chi(T) >= log2(1 + w(2^g-1)) >= g-log2(9/4)`,

where `w >= 4/9`. Consequently, any family of pair defects `g_n >= c n` with logarithmic channel
dimensions `O(n)` yields a same-channel family with the same linear coefficient up to an `O(1)`
loss, and

`C(T_n)-chi(T_n) >= (1/2)(g_n-log2(9/4))`.

This claim is **CONJECTURED pending independent review**; the displayed derivation is not yet a
completion-tier result.

## Role in DAG

Quantitative reduction separating two questions: construction of a large pair defect and conversion
to the same-channel/capacity language used in the boss's question.

## Current status

CONJECTURED from a complete proposer-side derivation in
`../../notes/PAIR_TO_SELF_REDUCTION_2026-08-29.md`. The remaining mathematical gap is not the
direct-sum arithmetic but construction of an extensive pair defect. Independent review is still
required before any completion-tier status.

## Dependencies

The standard direct-sum identity
`chi(A direct-sum B)=log2(2^chi(A)+2^chi(B))`, exact additivity of a noiseless classical side channel,
and the definition `C(T)=sup_k chi(T^tensor-k)/k`.

## Work record

- 2026-08-29 — registered before verification. Put `x=chi(N')`, `y=chi(M)`,
  `a=2^x`, `b=2^y`, where a classical side channel is chosen so `|x-y|<1` while preserving `g`.
  For `T=N' direct-sum M`, the four flagged sectors of `T tensor T`, together with ordinary
  superadditivity on the two diagonal sectors, give

  `2^chi(T^2) >= a^2 + 2ab 2^g + b^2`.

  Dividing by `2^(2chi(T))=(a+b)^2` gives

  `chi(T^2)-2chi(T) >= log2(1+w(2^g-1))`,

  with `w=2ab/(a+b)^2`. From `a/b in (1/2,2)`, `w>=4/9`; and
  `1+w(2^g-1) >= w2^g`, yielding the second inequality. Taking the `k=2` term in the regularisation
  gives the capacity lower bound.
- 2026-08-29 — expanded the sketch into a standalone proof: derived the direct-sum identity from
  arbitrary ensembles, proved exact classical balancing, checked all four tensor-square sectors,
  and bounded the logarithmic dimension overhead.

## Evidence

Full unreviewed derivation: `../../notes/PAIR_TO_SELF_REDUCTION_2026-08-29.md`. Supporting literature
audit: `../../notes/chatgpt-four-rounds/round-4-audit.md`.

## Adversarial reviews

None yet.

## Open obligations

- Obtain an independent derivation/review of the direct-sum identity, balancing construction, four
  tensor sectors, and dimension overhead.
- Keep Holevo, minimum-output-entropy, and regularised capacity quantifiers separate.

## Status history

- 2026-08-29 — created CONJECTURED from an unreviewed derivation; no completion tier claimed.

