# Polar-orientation criterion for Gram-positive support channels

Date: 2026-08-30

Status: proposer-side finite-dimensional theorem; independent review pending.

## Setting

Let `T:M_D->M_D` be an invertible quantum channel. Regard `T` as an operator on Hilbert-Schmidt
space and write its right polar decomposition as

\[
 T=Q|T|,
 \qquad
 |T|=(T^*T)^{1/2},
\tag{1}
\]

where `Q` is a unitary superoperator. For input and output unitaries `U,W`, define

\[
 T_{W,U}=\operatorname{Ad}_W\circ T\circ\operatorname{Ad}_U.
\tag{2}
\]

Such two-sided orientations are exactly what arise when an isometry onto a fixed Stinespring
support is reparametrized on its input and the support is changed by a local unitary on the channel
output.

## The criterion

There exist unitaries `U,W` for which `T_{W,U}` is positive definite as a Hilbert-Schmidt
superoperator if and only if the polar unitary `Q` is an inner automorphism:

\[
 \boxed{
 \exists U,W:\ T_{W,U}\succ0
 \quad\Longleftrightarrow\quad
 \exists R:\ Q=\operatorname{Ad}_R.}
\tag{3}
\]

Because unitary pre- and post-composition preserve complete positivity and trace preservation, the
positive orientation in (3), when it exists, is again a quantum channel. Equation (3) only tests
the Hilbert-Schmidt positivity required of a Gram channel; it does not prove that the positive
square root is CP or that a rectangular CP factor exists.

## Proof

Let `L_W=Ad_W` and `R_U=Ad_U`. Both are unitary on Hilbert-Schmidt space. Set

\[
 C=L_WTR_U.
\tag{4}
\]

Then

\[
 C^*C=R_U^*T^*TR_U,
 \qquad
 |C|=R_U^*|T|R_U.
\tag{5}
\]

Since `T` is invertible, so is `C`, and uniqueness of the polar decomposition gives

\[
 Q_C=C|C|^{-1}=L_WQR_U.
\tag{6}
\]

If `C` is positive definite, its polar unitary is the identity. Thus (6) implies

\[
 Q=L_W^*R_U^*=\operatorname{Ad}_{W^\dagger U^\dagger},
\tag{7}
\]

which proves necessity.

Conversely, suppose `Q=Ad_R`. Choose `W=I` and `U=R^dagger`. Equation (6) gives `Q_C=I`, so
the invertible operator `C` equals its positive modulus and is positive definite. This proves
sufficiency.

## Candidate-screening consequences

For a normalized rank-`D` projector `sigma_BE` with `sigma_B=I_D/D`, choose an isometry from the
input onto its support and form the associated square bistochastic support channel `T`. Then:

1. if `T` is invertible and its polar unitary is not an inner automorphism, no input/output local
   basis choice can make it a Gram channel;
2. if the polar unitary is inner, a Hilbert-Schmidt-positive channel orientation exists, but the
   rectangular CP-square and all-copy side-entropy gates remain;
3. the test is invariant under the original choice of support parametrization, because changing
   that choice only multiplies `Q` on the left and right by inner automorphisms.

The noninvertible case needs a partial-isometry version with explicit kernel compatibility and is
not claimed here.

## Research consequence

The finite fixed-channel search can be ordered as follows:

1. compute the entanglement-cost surplus of the normalized support projector;
2. construct one square support channel and compute its Hilbert-Schmidt polar unitary;
3. reject the candidate if that unitary is not an inner automorphism;
4. only for survivors, test whether the positive orientation admits a CP square of the required
   rectangular form and whether that factor has an all-copy output-entropy bound.

This converts the previously vague phrase "choose a favorable orientation" into an exact
finite-dimensional algebraic gate.
