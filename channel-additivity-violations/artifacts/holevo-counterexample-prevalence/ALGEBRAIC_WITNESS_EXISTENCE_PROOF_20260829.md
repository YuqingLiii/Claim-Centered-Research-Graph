# Algebraic witnesses and an effective exhaustive search

Date: 2026-08-29

Status: proposer-side computability/topology argument.

This note separates three notions often hidden behind the word “explicit”:

1. probabilistic existence;
2. deterministic/computable existence; and
3. a compact witness actually printed with a practical global certificate.

The product-Haar theorem plus openness upgrades (1) to (2), even with algebraic matrix entries.
It does not supply (3).

## Algebraic densification

Fix a finite dimension `D`. Gaussian-rational unitary matrices are dense in `U(D)`. One direct
parameterization is the Cayley transform

\[
 U=(I-A)(I+A)^{-1},
\]

where `A` ranges over skew-Hermitian matrices with entries in `Q(i)` and `I+A` is invertible.
These transforms are unitary, have Gaussian-rational entries, and are dense away from the usual
measure-zero `-1` chart boundary. The boundary itself can be approximated arbitrarily closely, so
no exact second chart is needed for the density argument.

For fixed finite channel dimensions, the minimum output entropy and Holevo quantity are continuous
in diamond norm. Therefore every strict random-unitary pair witness has an open neighborhood of
strict witnesses. Approximate every unitary in one successful tuple closely enough by a Gaussian-
rational unitary. The resulting equal-weight random-unitary channels have algebraic Kraus entries
and retain the strict inequality.

Apply this to the product-Haar construction. For every rational target `G>0`, there exist finite
integers `m,J,D` and a finite tuple of Gaussian-rational unitaries whose channel/conjugate-channel
pair has `p=1` minimum-output-entropy defect greater than `G`. Weyl-flag extension uses finite
algebraic data, and the pair-to-self reduction adds only a finite noiseless classical branch factor
and a flagged direct sum. Thus the same existential statement holds for Holevo pair and
same-channel witnesses. An exhaustive implementation may simply enumerate the finite branch
factor as well, rather than deciding an exact ceiling involving an optimized entropy value.

## A terminating exhaustive search exists in principle

There is an algorithm that eventually outputs such a deterministic witness for each rational
target `G`:

1. enumerate dimensions and finite tuples of Gaussian-rational skew-Hermitian matrices;
2. apply the Cayley transform and form the corresponding rational/algebraic random-unitary
   channels;
3. enumerate increasingly fine rational nets of the pure-state input spheres;
4. evaluate output entropies with certified rational interval arithmetic; and
5. combine the net values with an explicit finite-dimensional entropy-continuity modulus to obtain
   converging lower and upper bounds on each global minimum output entropy.

Concretely, if `E_delta` is a `delta`-net and `omega(delta)` is the continuity modulus, then

\[
 \min_{\psi\in E_\delta}f(\psi)-\omega(\delta)
 \le \min_\psi f(\psi)
 \le \min_{\psi\in E_\delta}f(\psi).
\]

For a pair gap use the two side lower bounds and subtract the joint upper bound. This specifies the
certificate direction needed to semidecide a strict positive gap.

For a fixed rational channel, compactness of the pure-state sphere and uniform continuity of output
entropy make the net bounds converge to `S_min`. Dovetailing candidates and precisions semidecides
the strict inequality `gap>G`: whenever the certified lower bound on the gap exceeds `G`, halt and
print the matrices, net mesh and interval certificate.

The algebraic densification above guarantees that at least one enumerated candidate has positive
margin. Hence the dovetailed search terminates for every rational `G`.

## Why the practical explicit-witness frontier remains open

The argument gives no usable bound on:

- the first successful `D`;
- the denominator or bit complexity of the rational unitaries;
- the net size required for a global entropy lower bound; or
- the runtime before the dovetailed search halts.

The known sufficient construction already uses `m>e^18`, an enormous depth for a one-bit target,
and a still larger unquantified matrix dimension. Thus “a deterministic algebraic witness is
computably guaranteed to exist” is rigorous but is not the compact, human-checkable deterministic
counterexample meant by the usual literature frontier.

## Dependencies

- `PRODUCT_HAAR_UNBOUNDED_PREVALENCE_PROOF_20260829.md` supplies a strict finite-dimensional
  witness with arbitrary target margin.
- `STABILITY_AND_MEASURE_PROOF_20260829.md` supplies the fixed-dimensional continuity/open-set
  step.
