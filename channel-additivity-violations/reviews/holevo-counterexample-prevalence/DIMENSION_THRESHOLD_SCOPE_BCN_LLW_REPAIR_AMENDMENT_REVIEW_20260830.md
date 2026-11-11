# Repair amendment review: BCN/LLW dimension-threshold source interfaces

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Scope and immutable inputs

This amendment rechecks only the two node-level assumptions added after Finding HCP-DT-IR-07 of
`DIMENSION_THRESHOLD_SCOPE_BCN_LLW_INDEPENDENT_REVIEW_20260830.md`. It does not revisit or enlarge
the canonical claim.

| object | SHA-256 |
|---|---|
| repaired `HCPREV.dimension-threshold-scope.yaml` | `0e42eb4fc4d5b35a1174031f892c51d0bce4bdfdc0c4845d5fd35ac7e80c497b` |
| BCN PDF | `5dd55c810f5bb3b244c6abd234600befd302f35ffd9d5610fa1303d22920b810` |
| LLW PDF | `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0` |

The canonical claim is unchanged at
`sha256:2d14346b2131fe7a261882d51d53a25bbbb81018ed98ed0ff9fddbc321e9580c`.

## Amendment finding HCP-DT-AR-01 -- PASS: BCN interface

The BCN assumption now records the correct Haar-Stinespring dimensions and limit
`d_n ~ tkn`, fixed output `k`, environment `n -> infinity`, conjugate partner, and Bell input.
Its wording accurately separates the explicit limiting entropy expression from the numerical
finite-range study locating `183`. It also preserves the paper's PDF p. 22 boundary: below `183`
only this Bell test in this model is excluded, not other joint inputs or all channels. The locator
to PDF pp. 17--22 contains the Stinespring definition, scaling, Theorem 6.3, proof, and scope remark.

**Verdict:** PASS. The assumption does not call `183` a purely analytic or global threshold.

## Amendment finding HCP-DT-AR-02 -- PASS: LLW interface

The repaired LLW assumption states the complete fixed-parameter regime
`k >= 2`, `t in (k^-2,1)`, `0 < p < infinity`, and `d_n/(nk) -> t`. It correctly attributes
almost-sure eventual violation under the strict conjugate/Bell criterion to Proposition 5.1,
analytic sufficiently-large-`k` existence to Proposition 5.3, and the exact displayed
`k_high(1)=182` only to the separate high-precision numerical optimization.

The repaired locator is exact: Proposition 5.1 and the fixed-`k` criterion are on PDF p. 13;
the high-`p` threshold lemma, Proposition 5.3, the definition of `k_high`, the value
`k_high(1)=182`, and the explicit non-universality sentence are on PDF p. 14; the introduction's
ensemble comparison is on PDF pp. 3--5. The locator deliberately names the high-`p` lemma without
its decimal number so the structural anchor parser does not misread the source.

**Verdict:** PASS. The assumption does not call `182` a theorem-proved analytic value or a global
minimum.

## Final amendment verdict

**PASS.** The machine-visible external inputs now match the local primary sources and close the
only dossier gate identified by the initial review. The exact claim at
`sha256:2d14346b2131fe7a261882d51d53a25bbbb81018ed98ed0ff9fddbc321e9580c`
is eligible for proposer-side promotion to `PROVED`, with this amendment and the initial review
linked. This reviewer does not change the canonical level.

No result here transfers either threshold to Holevo additivity, establishes a deterministic
finite witness, or proves a global minimum output dimension.
