# Adversarial audit of the topology and measure claims

Date: 2026-08-30

Status: second proposer-side audit; independent review pending.

## 1. The entanglement-breaking ball meets the correct channel slice

For a channel `Phi:A->B`, use the normalized Choi state

\[
 \rho_\Phi=(\operatorname{id}_A\otimes\Phi)(\Omega_A).
\]

The trace-preserving constraint is the affine equation

\[
 \operatorname{Tr}_B\rho_\Phi=I_A/d_A.
\tag{1}
\]

The completely depolarizing channel has

\[
 \rho_0=I_A/d_A\otimes I_B/d_B,
\]

which is simultaneously the center of the Gurvits--Barnum separable ball and a point of the affine
slice (1). Intersecting a genuine ambient Frobenius ball around `rho_0` with (1) gives a nonzero
relative ball in the full trace-preserving affine hull. Every state in that intersection is
positive, normalized and separable, hence is the Choi state of an entanglement-breaking CPTP map.

Thus the argument does not confuse interior in the full bipartite-state space with interior in an
incompatible channel constraint: the common center lies on the required slice, and the
intersection is relatively open with full affine dimension inside that slice.

## 2. Strong additivity removes an open channel region

Shor's entanglement-breaking theorems state, for every finite partner `Psi`,

\[
 S_{\min}(\Phi_{EB}\otimes\Psi)
 =S_{\min}(\Phi_{EB})+S_{\min}(\Psi)
\]

and

\[
 \chi(\Phi_{EB}\otimes\Psi)=\chi(\Phi_{EB})+\chi(\Psi).
\]

Therefore:

- in a self-channel ambient space, the relative EB interior is an open set with no self
  counterexamples; and
- in a pair ambient space, `relint(EB) tensor C` is an open set with no pair counterexamples.

The counterexample set is consequently not dense. Since each finite-dimensional compact channel
space is Baire and every residual set is dense, it is not residual either.

## 3. Relative-open violation sets have positive intrinsic measure

The diamond norm induces the ordinary finite-dimensional topology on the channel affine hull.
Fannes--Audenaert gives a uniform entropy modulus, and diamond contraction makes that modulus
uniform over all inputs and all ensembles. Infima and suprema therefore preserve continuity of
`S_min` and `chi`; a strict gap persists on a relative-open neighborhood.

A nonempty relatively open subset of a convex body with nonempty relative interior has positive
Lebesgue measure in its affine hull. If the original witness lies on the boundary, move an
arbitrarily small distance toward the depolarizing interior point; convexity puts the moved point
in the relative interior while relative openness keeps it in the same violation set. A small
affine ball then lies inside the violation set.

Hence every fixed-dimensional strict witness produces positive **intrinsic** measure. This is not a
measure on a disjoint union of dimensions and not the probability law of a named random-channel
ensemble.

## 4. Full-measure conclusion

The additive EB relative ball has positive intrinsic measure. Therefore the counterexample set
cannot have full intrinsic measure in the same fixed-dimensional ambient space. This is compatible
with the counterexample set itself also containing positive-measure open neighborhoods elsewhere.

## Verdict

The topology/measure classification survives the audit:

- strict counterexamples are relative open and positive intrinsic measure wherever they exist;
- counterexamples are not dense, residual, or full measure in the whole fixed-dimensional CPTP
  space;
- high probability in a specified random ensemble is a separate statement.

The claims remain `CONJECTURED` only because this is not an independent review.

Primary sources: Gurvits--Barnum, local PDF Theorem 1 and Corollary 3; Shor's
entanglement-breaking additivity paper, local PDF Theorems 1 and 2; Audenaert, local PDF Theorem 1.
