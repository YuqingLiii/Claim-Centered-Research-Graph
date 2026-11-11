# Kernel-compatible polar-orientation criterion for self-adjoint support channels

Date: 2026-08-30

Status: proposer-side finite-dimensional theorem; independent review pending.

## Setting

Let `T:M_D->M_D` be a Hilbert--Schmidt-self-adjoint quantum channel, not necessarily invertible.
Write

\[
 T=Q|T|
\tag{1}
\]

for its polar decomposition.  Because `T=T^*`, its initial and final support spaces agree:

\[
 \mathcal S=(\ker T)^\perp=\operatorname{ran}T,
\tag{2}
\]

and `Q` is the spectral sign of `T` on `S`, extended by zero on the kernel.  For unitaries `U,W`
define

\[
 T_{W,U}=\operatorname{Ad}_W\circ T\circ\operatorname{Ad}_U.
\tag{3}
\]

## Criterion

There exist `U,W` for which `T_{W,U}` is Hilbert--Schmidt positive semidefinite if and only if
there is a unitary `R` such that

\[
 \operatorname{Ad}_R(\mathcal S)=\mathcal S,
 \qquad
 \left.\operatorname{Ad}_R\right|_{\mathcal S}
 =\left.Q\right|_{\mathcal S}.
\tag{4}
\]

Thus the polar sign need only be the restriction of an inner automorphism, but that inner
automorphism must preserve the support and its orthogonal kernel.  In the invertible case
`S=M_D`, equation (4) reduces to the previously recorded inner-polar-unitary criterion.

## Proof of necessity

Let `L=Ad_W` and `R_U=Ad_U`.  The initial and final supports of `C=L T R_U` are

\[
 \mathcal S_{\rm in}=R_U^\dagger\mathcal S,
 \qquad
 \mathcal S_{\rm out}=L\mathcal S.
\tag{5}
\]

If `C` is positive semidefinite, these spaces are the same space `K`, and the polar partial
isometry of `C` is the orthogonal projector `P_K`.  Unitary covariance of polar decomposition
gives

\[
 P_K=L Q R_U.
\tag{6}
\]

For `x in S`, put `y=R_U^dagger x in K`.  Applying (6) to `y` gives

\[
 LQx=y=R_U^\dagger x,
\tag{7}
\]

so

\[
 Qx=L^\dagger R_U^\dagger x
 =\operatorname{Ad}_{W^\dagger U^\dagger}x.
\tag{8}
\]

Equality of the two spaces in (5) also gives

\[
 \operatorname{Ad}_{W^\dagger U^\dagger}(\mathcal S)=\mathcal S.
\tag{9}
\]

Taking `R=W^dagger U^dagger` proves (4).

## Proof of sufficiency

Conversely, assume (4).  Choose `W=I` and `U=R^dagger`.  Since `Ad_R` preserves `S`, it also
preserves `ker T=S^perp`.  On `S`, self-adjointness makes `Q` a Hermitian involution commuting with
`|T|`, while (4) gives `Ad_{R^dagger}=Q`.  Therefore

\[
 T\operatorname{Ad}_{R^\dagger}
 =Q|T|Q=|T|
\tag{10}
\]

on `S`, and both sides vanish on `ker T`.  The oriented channel is exactly the positive
semidefinite modulus `|T|`.

## Research use and limitations

The criterion is an exact first Gram gate for square, self-adjoint support channels with a kernel.
It does not assert that `|T|^{1/2}` is completely positive, does not produce a rectangular CP
factor, and does not prove a global minimum-output-entropy bound.  Those remain separate gates.

