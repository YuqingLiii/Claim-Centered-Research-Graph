# One-copy coherent information: five-parameter normal form

Date: 2026-08-29  
Status: proposer-side exact algebraic reduction; independent review pending.

## Result

Modulo the `O(3)` covariance of the qutrit noisy Werner--Holevo channel, optimization of the
one-copy coherent information over all qutrit density matrices reduces exactly to five real
parameters on a compact semialgebraic domain.

This is a reduction for `Q^(1)`. It does not address entangled inputs across arbitrary blocklengths
and therefore cannot by itself prove `Q=0`.

## Real/imaginary decomposition and covariance

Every Hermitian qutrit state has a unique decomposition

\[
\rho=R+iA,
\]

where `R` is real symmetric and `A` is real antisymmetric. For every real orthogonal `O`,

\[
\Lambda_x(O\rho O^T)=O\Lambda_x(\rho)O^T.
\]

The corresponding complementary outputs are also related by a real orthogonal change of Kraus
basis, so both output entropies are invariant. Choose `O` that diagonalizes `R`.

Let `(A_i)_{jk}=epsilon_{ijk}` and write `A=sum_i a_i A_i`. Every covariance orbit therefore has
a representative

\[
\rho(r,a)=
\begin{pmatrix}
r_1&i a_3&-i a_2\\
-i a_3&r_2&i a_1\\
i a_2&-i a_1&r_3
\end{pmatrix},
\qquad r_1+r_2+r_3=1.
\]

There are two independent diagonal parameters and three components of `a`: five real parameters
in total.

## Exact state domain

The representative is a density matrix exactly when all principal minors are nonnegative:

\[
r_i\ge0,
\]

\[
r_2r_3\ge a_1^2,\qquad
r_3r_1\ge a_2^2,\qquad
r_1r_2\ge a_3^2,
\]

and

\[
r_1r_2r_3-r_1a_1^2-r_2a_2^2-r_3a_3^2\ge0.
\]

Together with `sum r_i=1`, these polynomial inequalities define a compact semialgebraic domain
`D`.

## Receiver output

Using `rho^T=R-iA`,

\[
B_x(r,a):=\Lambda_x(\rho)
=\frac{x}{2}I+\left(1-\frac{3x}{2}\right)\operatorname{diag}(r)
+i\left(1-\frac{x}{2}\right)A.
\]

Thus its diagonal entries are

\[
\frac{x}{2}+\left(1-\frac{3x}{2}\right)r_i
\]

and its off-diagonal pattern is the one displayed for `rho`, scaled by `1-x/2`.

## Complementary output

Use the Kraus operators

\[
K_0=\sqrt{1-x}I,\qquad K_i=\sqrt{x/2}A_i
\]

and the padded complement

\[
[\Lambda_x^c(\rho)]_{\alpha\beta}
=\operatorname{Tr}(K_\alpha\rho K_\beta^\dagger).
\]

The Levi--Civita contractions give

\[
\operatorname{Tr}(\rho A_i)=-2i a_i
\]

and

\[
\operatorname{Tr}(A_i\rho A_j^\dagger)=\delta_{ij}-\rho_{ji}.
\]

Putting `c_x=sqrt(x(1-x)/2)`, the complementary state is therefore

\[
E_x(r,a)=
\begin{pmatrix}
1-x&2i c_x a^T\\
-2i c_x a&\frac{x}{2}\left(I-\operatorname{diag}(r)+iA\right)
\end{pmatrix}.
\]

The trace is one and positivity follows automatically from the Kraus construction for `(r,a)` in
`D`.

## Exact reduced optimization problem

Consequently

\[
\boxed{
Q^{(1)}(\Lambda_x)
=\max_{(r,a)\in D}\left[S(B_x(r,a))-S(E_x(r,a))\right].
}
\]

The proposed single-letter threshold statement on the strip is exactly the five-variable
inequality

\[
S(B_x(r,a))\le S(E_x(r,a))
\quad
\text{for all }(r,a)\in D,
\quad 2/5\le x<1/2.
\]

Pure states lie on the boundary of `D` and give equality zero. The local numerical audit finds only
this boundary floor on the strip, but it is not a proof of the displayed inequality.

## Verification and next proof target

The block formulas were checked numerically on a random full-rank complex state by comparing them
against direct Kraus multiplication; the Frobenius residual was `6.94e-17`. The determinant formula
for the normal-form state agreed to `1.2e-17` in the same check.

A rigorous one-copy proof can now target a finite list of strata of `D` (interior, rank two, and
pure boundary), using certified eigenvalue/entropy bounds. Even a complete proof here is only a
necessary first layer: the project root still requires an all-blocklength tensorizing argument.
