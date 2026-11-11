# Stability and intrinsic-measure proof

Date: 2026-08-29

Status: proposer-side proof. Fixed finite-dimensional channel spaces only.

## Setup

Let `C(A -> B)` and `C(C -> D)` be the compact convex sets of CPTP maps between fixed
finite-dimensional systems, with the relative topology of their trace-preserving Hermiticity-
preserving affine hulls. Put

`eps_N = (1/2) ||N - N'||_diamond`,

`eps_M = (1/2) ||M - M'||_diamond`.

For output dimension `d`, define the capped modulus

`F_d(eps) = f_d(min{eps,1-1/d})`,

where `f_d(t) = t log_2(d-1) + h_2(t)`. The cap makes `F_d` nondecreasing on
`[0,1]`, with `F_d(eps)=log_2(d)` once `eps>=1-1/d`. Thus if the actual trace
distance is bounded above by `eps`, Audenaert's inequality gives the sound
substitution `|S(rho)-S(sigma)|<=F_d(eps)` even when the upper bound is larger
than the actual distance.

The formula is used only for `d>=2` and sufficiently small `eps`. If either channel in a proposed
self or pair violation has one-dimensional output, that channel is the unique scalar-output
channel, its output entropy and Holevo quantity are zero, and tensoring it with the partner leaves
the partner's output state, minimum output entropy, and Holevo quantity unchanged. Hence both
additivity gaps are exactly zero and no strict witness exists in that branch. Every strict-witness
branch below therefore has all relevant output dimensions at least two.

Audenaert's Theorem 1 gives

`|S(rho)-S(sigma)| <= f_d((1/2)||rho-sigma||_1)`

for `d`-dimensional states.

## Uniform continuity of the optimized quantities

For every input state, diamond-norm contraction and Audenaert's inequality give

`|S(N(rho))-S(N'(rho))| <= F_{d_B}(eps_N)`.

Taking infima on both sides yields

`|S_min(N)-S_min(N')| <= F_{d_B}(eps_N)`.

For any fixed input ensemble, both the average-output entropy and the averaged individual-output
entropy change by at most `F_{d_B}(eps_N)`. The ensemble Holevo information therefore changes by
at most twice that number. Taking suprema over the common finite-dimensional ensemble domain gives

`|chi(N)-chi(N')| <= 2 F_{d_B}(eps_N)`.

No continuity of an optimizer is assumed; the uniform bound passes directly through an infimum or
supremum.

## Tensor-product perturbation

Since every CPTP map has diamond norm one,

`N tensor M - N' tensor M'`

`= (N-N') tensor M + N' tensor (M-M')`

implies

`(1/2)||N tensor M - N' tensor M'||_diamond <= eps_N + eps_M`.

The capped modulus is nondecreasing, so the upper bound `eps_N+eps_M` may be
substituted directly. For the local persistence statements below, choose the
neighborhood small enough that all displayed moduli tend to zero; no optimizer
continuity is needed.

## Persistence of a strict minimum-output-entropy gap

Suppose

`g_S = S_min(N)+S_min(M)-S_min(N tensor M) > 0`.

For the perturbed pair, the corresponding gap `g'_S` obeys

`g'_S >= g_S - F_{d_B}(eps_N) - F_{d_D}(eps_M)`

`             - F_{d_B d_D}(eps_N+eps_M)`.

The error tends to zero with `(eps_N,eps_M)`. Hence all sufficiently nearby CPTP pairs still have
`g'_S>0`.

## Persistence of a strict Holevo gap

Suppose

`g_chi = chi(N tensor M)-chi(N)-chi(M) > 0`.

The same calculation with the factor-two Holevo continuity bound gives

`g'_chi >= g_chi - 2 F_{d_B}(eps_N) - 2 F_{d_D}(eps_M)`

`                 - 2 F_{d_B d_D}(eps_N+eps_M)`.

Thus every strict Holevo counterexample also has a sufficiently small relative-open diamond-norm
neighborhood of counterexamples.

## Positive intrinsic measure

Let `K` be either the fixed-dimensional channel space or a fixed-dimensional product of two channel
spaces, viewed inside its finite-dimensional real affine hull. Its relative interior is nonempty
(the completely depolarizing channel is an interior point of the channel space).

Let `U` be any nonempty relatively open subset of `K`, and choose `x in U` and `y in relint(K)`.
For every `t in (0,1]`, the point `(1-t)x+t y` lies in `relint(K)`; for sufficiently small `t` it
also lies in `U`. Relative openness of `U` and relative interior of `K` then provide a nonzero-radius
affine ball contained in `U`. Consequently `U` has strictly positive Lebesgue measure in the affine
hull of `K`.

Combining this observation with either strict-gap calculation proves: whenever one strict witness
exists at fixed dimensions, the counterexample set at those dimensions is nonempty relatively open
and has positive intrinsic Lebesgue measure.

## Scope limits

This proof does not show density, probability one under an unrelated random model, or a positive
measure after mixing different dimensions. It also does not transfer a minimum-output-entropy
neighborhood to a Holevo neighborhood for the same channels; Shor's equivalence is universal and
existential, not pointwise.

## Dependencies

- `primary-sources/audenaert-0610146.pdf`, Theorem 1, PDF p. 2.
- Standard diamond-norm facts: output trace-distance contraction and multiplicativity under tensor
  products; for CPTP maps the diamond norm is one.
