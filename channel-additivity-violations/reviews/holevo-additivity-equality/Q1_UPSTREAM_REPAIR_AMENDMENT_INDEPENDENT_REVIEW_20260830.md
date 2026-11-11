# Independent amendment review: Q1 upstream source-interface repairs

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Independence and exact scope

This is a post-repair amendment to
`Q1_UPSTREAM_DEPENDENCY_AND_QUANTIFIER_INDEPENDENT_REVIEW_20260830.md`. I did not author the
canonical repairs or promotions. I checked only the exact Fukuda--Wolf assumption on
`HAEQ.pair-to-self-reduction`, the node-level and route-level HSW assumptions, the repaired root
proof sketch, the primary-PDF locators, unchanged statement hashes, and dependency order. I made no
canonical level change and did not reopen the Weyl calculation or any unrelated project.

## Final verdict

**PASS.** An initial amendment pass found that the two HSW assumptions incorrectly appended
`=sup_n`; Shor PDF page 3 states the regularized-capacity limit, while the supremum equality is a
local consequence of product-ensemble superadditivity and Fekete. The proposer removed that source
overclaim from both assumptions and made the Fekete step explicit in the root proof sketch. The
current files now pass.

The current completion levels are dependency-closed:

```text
Hastings existential MOE pair          PROVED
Weyl MOE-to-Holevo transfer            PROVED
Fukuda pair-to-self reduction          PROVED
  => root route                        PROVED
  => Q1 root claim                     PROVED
```

`HAEQ.fixed-channel-regularization` is independently `PROVED` after its own source repair, but is
not a root premise and was not needed to close the root route.

## Immutable repaired inputs

| object | SHA-256 |
|---|---|
| Hastings node YAML | `8ede82302255127641ad875d2eb3e87522c5144c95f16db86362d1a5eab01407` |
| repaired pair-to-self node YAML | `f6b781e2cbf78e78b8f70160eed9bcd56568206fcbbb3462c20660db067c1cb4` |
| repaired fixed-channel node YAML | `fabee5e22897b2172951cf500b170df257517d299477218238d4e585ee1d40e5` |
| repaired root node YAML | `8ff2534f04d6e46bc8935c99448badef3f788a8a1bc4861825eac6cba088ba2b` |
| prior dependency review | `15c84e6d0f44e402d8f7f59ec835deaffb3bd351d87625c6a7e8278f709c5844` |
| Hastings PDF | `b303560e5794e9b12b7c7f4145b4cd7958a6dd8ab83b61eb7947befca3348b98` |
| Shor PDF | `300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6` |
| Fukuda--Wolf PDF | `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7` |

The exact unchanged statement hashes are:

| object | exact hash |
|---|---|
| Hastings claim | `sha256:e6f972b2ec4389be96a66d39628b67af0d0c053573a4184e5b63d2c897f14374` |
| pair-to-self claim | `sha256:0fc7daa37324f6e68dc4987f959c831fc4dc48ad8c6c4054df16a397d9143c9f` |
| fixed-channel claim | `sha256:ae6bd7c5b610c197e3a5c418633dab91b67e1f9ebc5e8e9c2991134799909b8f` |
| root route implication | `sha256:2b2940d578ed8f68e77161ff1b093258781ac2e90f365b97953b0f8206ad3d4d` |
| root claim | `sha256:9e8fb7187a75cbc4455edea653a8c7f241bf0af92d3f8d9cb25094457dadea11` |

## Findings

### Finding Q1RA-01 -- PASS: exact Fukuda--Wolf interface and locator

The repaired assumption states, for every finite family of finite-dimensional channels,

```text
chi(direct_sum_i T_i)=log_2(sum_i 2^(chi(T_i))).
```

This is exactly Proposition 1 item 4, equations (5)--(6), for the classical-flag/direct-sum channel
defined in Section 2. The locator `Section 2, Proposition 1(4) and Eq. (6), PDF pp. 1-2` is precise:
the proposition and closed formula begin on PDF page 1 and the proof is on page 2. The local
four-block strictness argument and claim hash are unchanged. The pair-to-self `PROVED` promotion is
licensed.

### Finding Q1RA-02 -- PASS: node-level HSW interface

The fixed-channel assumption now imports only the primary-source statement

```text
C(N)=lim_(n->infinity) chi(N tensor n)/n
```

for every finite-dimensional channel. Shor Section 1, PDF page 3, defines the regularized Holevo
capacity by this limit and identifies it as the classical transmission capacity when entangled
inputs across channel uses are allowed. The locator is exact. The separate proposer proof supplies
superadditivity and Fekete, hence the supremum equality and both directions of the fixed-channel
claim. The node-level promotion at unchanged hash `ae6bd...` is licensed.

### Finding Q1RA-03 -- PASS: route-level HSW interface and final implication

The root route imports the same exact finite-dimensional limit theorem for `T`, with the same
precise Shor locator. Its proof sketch now explicitly records product-ensemble superadditivity and
Fekete, giving

```text
C(T) >= chi(T tensor T)/2 > chi(T).
```

The `=sup` assertion is no longer misattributed to Shor. The route implication hash remains
`2b2940...`, and the prior review already checked the existential witness changes and sign. The
source-interface repair introduces no new unresolved premise.

### Finding Q1RA-04 -- PASS: promotion order and root scope

At the repaired snapshot every premise of the root route is `PROVED`: Hastings, direct Weyl
transfer, and pair-to-self. The events record the root route as promoted only after those premises
and the HSW interface were closed, followed by the root claim. That order satisfies the DAG
protocol. The root concludes existence of one finite channel with a two-copy Holevo violation and
strict regularization gain; it does not assert failure for every channel or preserve the original
Hastings witness.

## Final recommendation

Retain the current `PROVED` levels of the Hastings, pair-to-self, fixed-channel, root-route and root
objects. Link this amendment to Findings Q1RA-01--Q1RA-04 so the prior conditional review is visibly
closed by a post-repair review. No further Q1 source-interface or dependency gate remains in this
route.
