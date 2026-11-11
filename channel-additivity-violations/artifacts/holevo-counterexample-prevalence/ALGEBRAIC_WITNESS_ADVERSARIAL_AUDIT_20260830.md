# Adversarial audit: algebraic witness existence is not a printed explicit witness

Date: 2026-08-30

Status: second proposer-side audit; independent review pending.

## Claim checked

For every rational target `G>0`, the strict product-Haar existence theorem and openness imply the
existence of a finite algebraic `p=1` witness with gap greater than `G`. Moreover, a dovetailed
finite-net search is guaranteed to print one eventually. This must not be reported as a practical
small explicit witness.

## 1. Effective dense channel data

For a Gaussian-rational skew-Hermitian matrix `A`,

\[
 U=(I-A)(I+A)^{-1}
\]

is unitary and has Gaussian-rational entries. Since the eigenvalues of `A` are purely imaginary,
`I+A` is automatically invertible. Cayley images are dense in the unitary group: the omitted
eigenvalue-`-1` chart boundary can be approximated arbitrarily closely and does not obstruct
density. Thus a successful finite Haar tuple can be approximated entrywise, and hence in channel
diamond norm, by an enumerable algebraic tuple.

Strict MOE gaps are stable under sufficiently small finite-dimensional diamond perturbations, so
an algebraic approximation preserves a chosen positive margin.

## 2. What a global finite-net certificate must compute

For a fixed algebraic channel `N` with output dimension `d`, define

\[
 f_N(\psi)=S(N(|\psi\rangle\langle\psi|)).
\]

Let `E` be an explicit finite `delta`-net of the pure-state sphere and let `omega_N(delta)` be an
entropy-continuity error obtained from trace-distance contraction and Fannes--Audenaert. Then

\[
 \min_{\psi\in E}f_N(\psi)-\omega_N(\delta)
 \le S_{\min}(N)
 \le\min_{\psi\in E}f_N(\psi).
\tag{1}
\]

The left inequality is the important direction: a true minimizer has a nearby net point, so the
sampled minimum cannot lie more than the continuity modulus above the global minimum.

For a pair `N,M`, certified intervals from (1) give the gap lower bound

\[
 \Delta(N,M)
 \ge L_N+L_M-U_{N\otimes M},
\tag{2}
\]

where `L` denotes the net-minus-modulus lower bound and `U` the sampled upper bound. Refining the
nets and arithmetic intervals makes the right-hand side converge to the true gap.

Algebraic matrices have computable eigenvalues, and logarithms of positive computable reals admit
certified rational intervals. Zero eigenvalues are handled by the continuous convention
`0 log 0=0`. Dense rational points on the complex unit sphere can be enumerated by a standard
rational sphere parametrization, so every object in (1)--(2) is effective.

## 3. Termination and the strict-margin quantifier

For the requested rational `G`, the product-Haar theorem gives some finite witness with gap
strictly larger than `G`, not merely equal to it. Openness gives an algebraic witness with a
remaining margin `eta>0`. Dovetail over dimensions, algebraic tuples, state nets and interval
precisions. For the successful tuple, (2) eventually exceeds `G`, so that branch halts and prints
the tuple together with its finite certificate.

No prior knowledge of `eta`, the successful dimension, or the necessary precision is required for
termination. Their absence only destroys any useful runtime bound.

## 4. Holevo and same-channel outputs

The safest effective route does not attempt a fresh unrestricted Holevo optimization. Apply the
finite Weyl-flag extension, whose roots-of-unity entries are algebraic, and use the exact
MOE-to-Holevo identity. For pair-to-self balancing, dovetail over the finite classical branch size
and certify the resulting log-sum-exp lower bound; this avoids deciding an exact ceiling of an
optimized entropy value in advance.

Thus computable algebraic Holevo pair and same-channel witnesses follow from the certified MOE
witness and exact finite reductions.

## 5. Verdict

The computable-existence argument survives the audit. It proves:

- a finite algebraic witness exists for every rational target gap;
- a terminating exhaustive certified program exists in principle.

It does **not** provide:

- a currently printed successful tuple;
- a practical dimension or denominator bound;
- a feasible net size or runtime; or
- a global minimum-dimension theorem.

Accordingly `HCPREV.algebraic-witness-existence` remains `CONJECTURED`, while
`HCPREV.explicit-witness-frontier` remains `OPEN`.
