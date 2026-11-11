# A nonempty open strongly additive region

Date: 2026-08-29

Status: proposer-side proof. Fixed finite input and output dimensions.

## Entanglement-breaking interior

Use normalized Choi states. The completely depolarizing channel has normalized Choi state equal to
the maximally mixed product state on the input-output bipartite space. Gurvits--Barnum Theorem 1
and Corollary 3 provide a nonzero Frobenius-norm ball of separable bipartite states around that
maximally mixed state.

Intersect that ball with the affine slice imposing the trace-preserving Choi marginal. The
intersection is a relative neighborhood of the depolarizing channel, every Choi state in it is
separable, and a channel is entanglement breaking exactly when its Choi state is separable.
Therefore the entanglement-breaking channels have nonempty relative interior in every fixed
finite-dimensional CPTP channel space.

## Strong additivity on that region

Shor's Theorem 1 proves, for an arbitrary channel `Psi` and an entanglement-breaking channel `Phi`,

`S_min(Psi tensor Phi) = S_min(Psi)+S_min(Phi)`.

Shor's Theorem 2 proves in the same regime

`chi(Psi tensor Phi) = chi(Psi)+chi(Phi)`.

Hence the interior entanglement-breaking neighborhood is a strongly additive self-channel region,
and `relint(EB) x C` is a nonempty relative-open additive region in the corresponding channel-pair
space.

## Consequences for prevalence language

Fix one finite-dimensional self-channel or pair-channel ambient space.

1. The counterexample set is not dense because it misses the nonempty open additive region.
2. The ambient channel space is compact metric and hence a Baire space. A residual set is dense,
   so the counterexample set is not residual/generic.
3. By the affine-ball argument in `STABILITY_AND_MEASURE_PROOF_20260829.md`, the additive open
   region has positive intrinsic Lebesgue measure. Therefore the counterexample set is not
   full-measure.

These conclusions coexist with positive-measure counterexample neighborhoods and with
high-probability counterexamples in specified random ensembles. They refer to different
quantifiers and measures.

## Dependencies

- `primary-sources/gurvits-barnum-0204159.pdf`, Theorem 1 and Corollary 3, PDF pp. 4-5.
- `primary-sources/shor-eb-0201149.pdf`, Theorems 1 and 2, PDF pp. 2 and 4.
