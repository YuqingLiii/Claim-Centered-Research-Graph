# Amendment review: repaired fixed-dimensional full-support probability dichotomy

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q2_probability_review`, returning only to
verify the repairs required by the immutable review
`FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md`.

## Independence and amendment scope

I did not author the proposer artifacts, the repairs, or the canonical YAML. I did not modify
the original review. This amendment is limited to the two blockers in Finding HCP-FS-IR-06 and
the `d=1` edge case in Finding HCP-FS-IR-02:

1. the explicit one-dimensional-output branch added to
   `artifacts/STABILITY_AND_MEASURE_PROOF_20260829.md`;
2. the node-level assumptions added to `HCPREV.open-set-stability`;
3. the node-level assumptions added to `HCPREV.additive-open-region`; and
4. whether those repairs, together with the unchanged exact claims and route implication,
   license completion-level promotion.

The original review already independently reconstructed and passed the topology,
measure-theoretic implication, self/pair conventions, relative-open entanglement-breaking
complement, and MOE/Holevo separation. This amendment rechecks that the unchanged statements and
their hashes still match that review and that no new unstated input was introduced.

## Executive verdict

All blockers are closed. The `d=1` branch is correct and exhaustive. The imported Audenaert,
diamond-norm, Gurvits--Barnum, Shor, and Choi/entanglement-breaking inputs are now
machine-visible at the two route-free premise nodes with adequate statements and locators.

The exact promotion order licensed by this amendment is:

1. promote `HCPREV.open-set-stability` to `PROVED` at
   `sha256:5e48fcbc53334cc32e190854c3339a1c042116b5da998f877b152d81c3dd4310`;
2. promote `HCPREV.additive-open-region` to `PROVED` at
   `sha256:9d5a1f22a2f633e0b931441177a99c8b704b63fef0a3ad7ca99c190db9adb9a4`;
3. after those premise promotions, promote route
   `open-violation-and-open-additive-complement` to `PROVED` at
   `sha256:10eadfd4851f1fb6637ef01f264598c54a33223ef8583deda567b6ab7981461a`;
4. then promote `HCPREV.full-support-probability-dichotomy` to `PROVED` at
   `sha256:4cf4c6718cac0081c6dd806e0042d2f908caa2ecc9819972de0ce05c44a54178`.

The order matters only for protocol closure. Mathematically, the route implication was already
passed in Finding HCP-FS-IR-05. No `CERTIFIED*` intermediate is needed, and no unresolved premise
or caveat remains inside the exact fixed-dimensional qualitative claim.

The existing scope caveats must remain: full support is on the entire fixed-dimensional ambient
body, the result is qualitative rather than dimension-uniform, and MOE prevalence is not
transferred to Holevo prevalence for the same channels or law.

## Immutable repaired inputs

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| original independent review | `2d61dfb6d042daec639a4c8a4d6039f3b92c09b4571c20f7bcf47cf76a568bed` |
| unchanged full-support artifact | `f9e55d086e9b9fbd2929c0b822b64ff3f2ae37b55d1e6a0482e7a06ea8e4f80e` |
| repaired stability artifact | `94ab1b1fcb4ee74c73d90baf8117371d351f1291265ad612279ef060710bddbb` |
| unchanged additive-region artifact | `8fa6b701a9ca658ae8b091a685effc8ecb8010465a75882dae3258ed40ecc528` |
| repaired `HCPREV.open-set-stability` YAML | `d3ebcc12c1b20c10c37cf9ce079532bc9f98f1823ff39af5a0f655c383b26288` |
| repaired `HCPREV.additive-open-region` YAML | `f5ccc7fa27f834ed711788ebda41b3cbb88f41ea4865bf7e428f0c63a9cf38ba` |
| review-linked target YAML | `6d64a1c19d86dcfeffd3186c8dfbfeef0b91dd2f716b2568c009ccb3d2e9a79a` |
| Audenaert PDF | `dc2265209fd7fb86aa7ce03a541c15d8b9f5a29b70c281728650eef0ad87bdb7` |
| Shor EB PDF | `9e68b70e36383ceb42dbbfbd3cefdbad0d5757ee76941f1d590b6c15cefcbca4` |
| Gurvits--Barnum PDF | `c35027eb1e981bf70b2767c229daac7812d3226773ad5d0f7a7a335c363adf85` |

The three claim hashes and route implication hash are unchanged from the original review.

## Finding HCP-FS-AMD-01 -- PASS: one-dimensional-output branch

The repaired stability artifact now restricts the Audenaert formula

```text
f_d(eps)=eps log_2(d-1)+h_2(eps)
```

to `d>=2` and separately treats `d=1`. A CPTP map with one-dimensional output is the trace map,
so its output entropy and Holevo quantity are zero. For a partner channel `M`, applying the trace
map on one input leg and `M` on the other produces exactly `M` applied to the partner marginal.
Every partner input state or ensemble is conversely realized by tensoring with a fixed state on the
traced leg. Therefore

```text
S_min(Tr tensor M)=S_min(M),
chi(Tr tensor M)=chi(M),
```

and both pair gaps are zero. The self-channel scalar-output case is the same argument with both
outputs one-dimensional. Thus no strict witness is omitted by restricting every strict-witness
continuity branch to output dimensions at least two.

The tensor output dimension `d_B d_D` is then also at least two, so every displayed continuity
modulus in the strict-witness branch is defined.

**Verdict:** blocker fully closed. The unchanged stability claim at
`sha256:5e48fcbc53334cc32e190854c3339a1c042116b5da998f877b152d81c3dd4310`
is eligible for `PROVED`, jointly with Findings HCP-FS-IR-02 and HCP-FS-IR-03.

## Finding HCP-FS-AMD-02 -- PASS: stability assumptions are exact and locatable

The repaired `HCPREV.open-set-stability` node registers:

1. Audenaert's theorem for `d>=2`, trace distance
   `T=(1/2)||rho-sigma||_1`, and bound
   `T log_2(d-1)+h_2(T)`, sourced to Theorem 1, PDF p. 2; and
2. the diamond-norm channel facts needed by the proof: uniform output trace-norm control,
   tensor-product multiplicativity, CPTP diamond norm one, and the resulting two-factor
   perturbation estimate, sourced to the exact displayed derivation in
   `## Tensor-product perturbation`.

The Audenaert assumption is slightly narrower than the primary theorem because it says
"sufficiently small" trace distance; this is exactly the regime used to prove local persistence
and is therefore sufficient. The source page states the stronger all-distance theorem.

The diamond facts are correctly classified as model facts. Uniform output control follows from
the defining stabilized supremum; tensor multiplicativity and CPTP norm one give

```text
|| (N-N') tensor M ||_diamond
    = ||N-N'||_diamond ||M||_diamond,
```

and similarly for the second term. The artifact's expansion and triangle inequality then give the
claimed perturbation estimate. No optimizer-continuity assumption is hidden.

**Verdict:** assumption-registry blocker fully closed. Promote
`HCPREV.open-set-stability` to `PROVED` at the hash above.

## Finding HCP-FS-AMD-03 -- PASS: additive-region assumptions are exact and locatable

The repaired `HCPREV.additive-open-region` node registers all three imported interfaces:

1. Gurvits--Barnum's nonzero separable Frobenius ball in arbitrary finite bipartite dimensions,
   with Theorem 1 and Corollary 3 on PDF pp. 4--5;
2. Shor's minimum-output-entropy and one-shot Holevo strong-additivity theorems for every finite
   partner, with Theorems 1 and 2 on PDF pp. 2 and 4; and
3. the normalized Choi/trace-preserving marginal and Choi-separable/entanglement-breaking
   correspondence, sourced to the exact affine-slice section of the local proof.

The Choi statement is correct in the convention used. If a normalized Choi state is separable,
write it as a convex sum of input/output product states. The fixed input marginal converts the
transposed input factors, with their weights, into a POVM, yielding a measure-and-prepare channel.
Conversely a measure-and-prepare channel has a separable normalized Choi state. Hence the
Gurvits--Barnum ball intersected with the trace-preserving affine slice is genuinely a relative-open
entanglement-breaking neighborhood, not merely an open set in an incompatible state space.

Shor's Theorem 2 is exactly about `chi*`, the one-shot Holevo quantity used in the canonical claim.
No regularized-capacity or Shor-equivalence substitution occurs.

**Verdict:** assumption-registry blocker fully closed. Promote
`HCPREV.additive-open-region` to `PROVED` at
`sha256:9d5a1f22a2f633e0b931441177a99c8b704b63fef0a3ad7ca99c190db9adb9a4`.

## Finding HCP-FS-AMD-04 -- PASS: route and target completion closure

After Findings HCP-FS-AMD-01--03, both load-bearing premise claims have complete direct proofs,
machine-visible inputs, and independent hash-bound review. The route has exactly those two premises
and no hidden third hypothesis.

Finding HCP-FS-IR-05 already established the route implication: a nonempty relatively open
violation subset has positive mass, and a disjoint nonempty relatively open additive subset has
positive mass, so a nonempty violation set has probability in `(0,1)`. The empty case gives
probability zero. The target node lists that single route and preserves every required scope caveat.

**Verdict:** after the two premise promotions, promote route
`open-violation-and-open-additive-complement` to `PROVED` at
`sha256:10eadfd4851f1fb6637ef01f264598c54a33223ef8583deda567b6ab7981461a`,
then promote `HCPREV.full-support-probability-dichotomy` to `PROVED` at
`sha256:4cf4c6718cac0081c6dd806e0042d2f908caa2ecc9819972de0ce05c44a54178`.

## Finding HCP-FS-AMD-05 -- PASS: strict scope remains unchanged

The repair does not alter the ambient space, probability law, self/pair convention, or capacity
quantity. The result remains one fixed finite-dimensional qualitative statement. In particular,
it proves none of the following:

- a dimension-uniform positive lower bound or upper bound separated from one;
- asymptotic high probability in a Haar/Stinespring or induced-channel model;
- full support when the named ensemble is supported on a proper subset of the CPTP body;
- existence of a strict witness in any specified dimension; or
- transfer of a MOE violation set or probability to Holevo for the same channels.

**Verdict:** PASS. The original caveats remain accurate and should be retained after promotion.

## Final amendment disposition

There is no remaining mathematical, evidential, or dependency blocker for the four exact objects
listed in the Executive verdict. Promotion should add ordinary level-change events, link this
amendment at the relevant finding and exact reviewed hash, remove only the completed independent
review frontier, and retain the separate quantitative-model-bound frontier.
