---
id: "ADDGAP.matched-independent-tensors"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.matched-independent-tensors.md"
aliases: ["P2"]
kind: LEAF
role: proof
status: OPEN
status_source: "Montanaro gate negative in notes/MONTANARO_GATE_2026-08-29.md; improved leakage theorem still open"
disposition: null
parents: ["ADDGAP.goal"]
children: ["ADDGAP.montanaro-gate", "ADDGAP.fixed-r-diagonal-gate", "ADDGAP.hierarchical-strong-additivity"]
related: ["ADDGAP.pair-to-self"]
---

# ADDGAP.matched-independent-tensors — accumulate matched random-channel defects

## Claim

There exists a sequence of independently sampled channel pairs `(N_i, conjugate(N_i))` for which
the sum of the matched cross defects is linear in the number of factors, while the two single-side
minimum-output-entropy leakage terms are sublinear. This would produce an extensive pair defect,
which `ADDGAP.pair-to-self` would convert to a same-channel Holevo violation.

## Role in DAG

Active amplification route. It attacks the exact obstruction that naive tensor powers ignore:
additional low-entropy inputs can appear inside each tensor side.

## Current status

OPEN. The first child gate (Montanaro) is PARKED because its bound permits linear leakage. A second,
logically different gate is now active: for each desired finite factor count `s`, take the random-
channel dimension to infinity first and then diagonalise in `s`. This avoids demanding one
probability theorem uniform in unbounded `s`.

## Dependencies

One of `ADDGAP.montanaro-gate`, `ADDGAP.fixed-r-diagonal-gate`, or
`ADDGAP.hierarchical-strong-additivity`, plus a base random-channel
ensemble with a positive `p=1` matched-pair defect.

## Strategy blueprint

For `A_r=tensor_i N_i` and `B_r=tensor_i conjugate(N_i)`, define

`alpha_r=sum_i Smin(N_i)-Smin(A_r)` and
`beta_r=sum_i Smin(conjugate(N_i))-Smin(B_r)`.

Product Bell witnesses across the matched pairs give the exact lower bound

`gap(A_r,B_r) >= sum_i gap(N_i,conjugate(N_i)) - alpha_r - beta_r`.

Thus a uniform positive average matched gap plus `alpha_r+beta_r=o(r)` composes into an extensive
pair defect. The child gate asks whether published weak multiplicativity supplies precisely this
sublinear leakage estimate, with probability control uniform in growing `r`.

Alternative composition through `ADDGAP.fixed-r-diagonal-gate`: for every fixed `r`, first send an
auxiliary random-channel dimension `n` to infinity. If a theorem gives

`Smin(tensor_{i=1}^r N_i)=sum_i Smin(N_i)+o_n(1)`

for independent samples, while all `r` matched pairs have gap at least a common `g_0-o_n(1)`, then
the finite intersection has positive probability for sufficiently large `n=n(r)`. Choosing one
such deterministic tuple for each `r` gives pair gap at least `r g_0-o(1)`. No uniform-in-`r`
random theorem is needed; the dimension may grow along the diagonal sequence.

Hierarchical composition through `ADDGAP.hierarchical-strong-additivity`: choose the factors one at
a time, with the new auxiliary dimension much larger than all previously fixed factors. If the new
channel is asymptotically additive against every fixed partner but retains a positive defect with
its co-varying conjugate, choose its error at step `j` below `2^{-j}`. Induction makes both
single-side leakages bounded while the matched cross defects grow as `r g_0-O(1)`. This proves an
absolute gap unbounded in hierarchy depth if the two-factor theorem holds. To satisfy this parent's
extensive claim in the complete channel size, the auxiliary dimensions must also pass
`ADDGAP.growing-level-rate`; pointwise fixed-partner convergence alone does not control that cost.

## Work record

- 2026-08-29 — registered before checking Montanaro's theorem. The leakage identity above records
  why merely tensoring a known Hastings pair is not a proof.
- 2026-08-29 — child gate returned a negative scope result; route PARKED rather than extended into
  ungated numerical work. See `../../notes/MONTANARO_GATE_2026-08-29.md`.
- 2026-08-29 — re-opened with a distinct fixed-`r`, dimension-first diagonalisation blueprint;
  registered child `ADDGAP.fixed-r-diagonal-gate` before checking the Collins--Fukuda--Nechita
  product-random-channel literature.
- 2026-08-29 — registered the hierarchical fixed-partner child before checking arXiv:1311.7571;
  unlike the same-scale route, it allows the channel dimensions to grow successively.
- 2026-08-29 — corrected the hierarchy after round 5: fixed-partner additivity alone gives
  absolute-unbounded gap, not automatically a full-size extensive gap.

## Evidence

None yet beyond the algebraic blueprint.

## Adversarial reviews

None yet.

## Open obligations

- Resolve `ADDGAP.fixed-r-diagonal-gate`: its theorem must concern global minimum output entropy of
  a product of independent channels, not merely the entropy of a chosen input or the output spectrum
  at fixed moments.
- Resolve `ADDGAP.hierarchical-strong-additivity`: its fixed-partner theorem and its co-varying
  conjugate gap must hold for the same family, and its growing-level rate child must control the
  full dimension cost.

## Status history

- 2026-08-29 — created OPEN; active bounded literature/theorem gate commissioned.
- 2026-08-29 — retained OPEN but PARKED after the Montanaro gate failed quantitatively.
- 2026-08-29 — returned to OPEN under the new fixed-`r` diagonal gate; the Montanaro subroute stays
  PARKED.
- 2026-08-29 — added the hierarchical strong-additivity gate and cleared the parent PARKED tag.

