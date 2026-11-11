---
id: "ADDGAP.hierarchical-strong-additivity"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.hierarchical-strong-additivity.md"
aliases: ["P2c"]
kind: LEAF
role: proof
status: OPEN
status_source: "round-5 audit split absolute-unbounded and full-size-extensive gates 2026-08-29"
disposition: null
parents: ["ADDGAP.matched-independent-tensors"]
children: ["ADDGAP.fixed-partner-global-entropy", "ADDGAP.growing-level-rate"]
related: ["ADDGAP.fixed-r-diagonal-gate", "ADDGAP.pair-to-self"]
---

# ADDGAP.hierarchical-strong-additivity — co-varying conjugate gap with fixed-partner additivity

## Claim

Determine whether there is a sequence of finite-dimensional channels `Phi_n` such that:

1. for every **fixed** finite-dimensional channel `Xi`,
   `Smin(Xi tensor Phi_n) >= Smin(Xi)+Smin(Phi_n)-epsilon_n(Xi)` with
   `epsilon_n(Xi) -> 0`, and likewise with `conjugate(Phi_n)`; while
2. the co-varying matched pair retains a uniform defect
   `gap(Phi_n,conjugate(Phi_n)) >= g_0-o(1)` for some `g_0>0`.

If both statements hold with compatible quantifiers, use them to construct a heterogeneous sequence
of channels with a pair defect linear in hierarchy depth. Determine separately whether quantitative
dimension control makes that defect extensive in the complete channel size.

## Role in DAG

Third stop/go gate for matched-pair amplification. It replaces a global theorem about a product of
many same-scale random channels by an inductive construction in which every new channel is chosen
at a larger auxiliary dimension than the already-fixed product. Its two children now distinguish
absolute-unbounded amplification from full-size extensive amplification.

## Current status

OPEN. Collins--Fukuda--Nechita, arXiv:1311.7571, proves existence of a limiting output set
after tensoring with any fixed channel, but does not identify that set or prove minimum-output-
entropy additivity. The authors explicitly say that the limiting set is difficult to analyze in
general. That literature shortcut is PARKED, but the exact missing global-entropy statement is now
an active child proof/counterexample target. Round 5 also exposed a distinct quantitative rate
gate: fixed-partner convergence alone gives no control of auxiliary dimension growth.

## Dependencies

A fixed-partner minimum-output-entropy lower bound and a common positive `p=1` matched
channel/conjugate-channel defect for the same co-varying family.

## Strategy blueprint

Let `A_{j-1}=tensor_{i<j} Phi_{n_i}` and
`B_{j-1}=tensor_{i<j} conjugate(Phi_{n_i})`, which are fixed finite-dimensional channels once the
first `j-1` choices have been made. Choose `n_j` so large that the fixed-partner theorem gives

`Smin(A_{j-1} tensor Phi_{n_j}) >= Smin(A_{j-1})+Smin(Phi_{n_j})-epsilon_j`

and its conjugate analogue for `B_{j-1}`, with a summable sequence such as
`epsilon_j=2^{-j}`. Induction then bounds both single-side leakages by `sum_j epsilon_j=O(1)`.
Product matched witnesses give a cross advantage at least `sum_j(g_0-o_j(1))`. Choosing the
matched-gap errors summable as well yields pair defect `r g_0-O(1)`. The separate
`ADDGAP.pair-to-self` reduction would convert this to a same-channel Holevo-capacity gap with only
constant additional loss.

This blueprint is conditional: it does not compose unless the fixed-partner theorem controls the
**global minimum over all inputs**, applies on both unbarred and conjugate sides, and its family is
the same one carrying the co-varying conjugate-pair defect.

Child composition through `ADDGAP.fixed-partner-global-entropy`: that child freezes the two-factor
entropy assertion. If it is proved for the BCN family and the known matched conjugate gap is applied
at each chosen scale, the summable-error induction gives finite-dimensional pair gaps unbounded in
absolute size.

Full-size extensive composition additionally requires `ADDGAP.growing-level-rate`. The new child
must control the auxiliary thresholds strongly enough that

`sum_j(g_j-2 ell_j) >= c sum_j c_j-O(1)`.

Without it, the chosen `n_j` may grow super-exponentially, so a gap linear in depth can be sublinear
in the full input/output/environment qubit cost. Thus the fixed-partner child alone does not
complete this parent in the extensive interpretation.

## Work record

- 2026-08-29 — registered before detailed verification of arXiv:1311.7571. The route was generated
  after fixed-input Weingarten results proved insufficient for `ADDGAP.fixed-r-diagonal-gate`.
- 2026-08-29 — checked Theorem 8.1 and Section 8 against the PDF. The theorem gives convergence to
  an unidentified convex body, not the required entropy equality; bounded primary-source search
  found no replacement theorem. Route PARKED, not REFUTED, because the conditional construction
  remains valid if a stronger result is later proved.
- 2026-08-29 — reopened the mathematical route under child
  `ADDGAP.fixed-partner-global-entropy`; the failed literature shortcut remains recorded rather than
  erased.
- 2026-08-29 — round-5 audit accepted the conditional absolute-unbounded induction but rejected the
  unstated implication to full-size extensivity; registered `ADDGAP.growing-level-rate`.

## Evidence

Negative scope audit: `../../notes/HIERARCHICAL_STRONG_ADDITIVITY_GATE_2026-08-29.md`.
Round-5 audit: `../../notes/chatgpt-four-rounds/round-5-audit.md`.

## Adversarial reviews

None yet.

## Open obligations

- Find or prove a theorem stronger than arXiv:1311.7571 that controls global minimum output von
  Neumann entropy, rather than just existence of a limiting output set.
- Check whether the same channel family has a uniform positive `p=1` conjugate-pair defect.
- Check whether the theorem is deterministic, almost sure, or in probability and whether a
  deterministic inductive selection is licensed.
- Resolve `ADDGAP.growing-level-rate` before claiming extensivity in the complete channel size.
- If the gate passes, write the induction with explicit error bookkeeping and commission an
  independent rule-6/7 review.

## Status history

- 2026-08-29 — created OPEN before theorem verification.
- 2026-08-29 — retained OPEN but PARKED after the candidate theorem failed the required scope.
- 2026-08-29 — returned to OPEN under a direct global-entropy lemma.
- 2026-08-29 — retained OPEN with the additional growing-level quantitative child.

