# Exact spectral–geometry reduction for the H4 candidate

This note isolates an exact structural fact that was not explicit in the
recovered proof record.  It narrows the classical problem but does not claim
the unresolved global sign bound.

## D4-S1. Projector and candidate eigenvalue

Let `P=(X+Y sqrt(5))/8` be the exact Gram matrix from
`d4-exact-instance-certificate-20260829.md` and put

\[
 E=P/75,
 \qquad
 \lambda=5132744330206382+2356560241063596\sqrt5.
\]

The already checked identities `P^2=75P`, `P=P^T`, and `rank(P)=4` show that
`E` is the orthogonal projector onto a four-dimensional subspace.  Moreover,

\[
 300\lambda
 =1539823299061914600+706968072319078800\sqrt5
 =\langle A,P\rangle.
\]

## D4-S2. Exact intertwining identity

Writing both sides in the basis `1,sqrt(5)`, direct integer matrix
multiplication verifies

\[
 AP=PA=\lambda P.
\]

Thus `A` acts by `lambda` on `range(P)`.  Define

\[
 R=A-\lambda E.
\]

Then `R=R^T` and `RE=ER=0` exactly.

## D4-S3. Strict residual spectral bound

If

\[
 \lambda^2=c+d\sqrt5,
\]

then the checker forms, without floating arithmetic,

\[
 R^2=A^2-\frac{\lambda^2}{75}P.
\]

Every row has the same exact absolute row sum

\[
 \rho^2=
 \frac{
 45128986920383753829374689905666816
 +7379598965220731379807703012657824\sqrt5}{600}.
\]

The numerator of `lambda^2-rho^2` after multiplication by 600 is

\[
 -12661819795539156167440312434064416
 +7135146494110017205090537470948576\sqrt5.
\]

This is positive already from `sqrt(5)>2`, because twice the positive
coefficient exceeds the absolute value of the negative coefficient by

\[
1608473192680878242740762507832736>0.
\]

Since `R^2` is symmetric,

\[
 \|R\|_{\mathrm{op}}^2
 =\|R^2\|_{\mathrm{op}}
 \le \|R^2\|_{\infty}
 =\rho^2<\lambda^2.
\]

Together with `A=lambda E+R` and `ER=0`, this proves

\[
 \|A\|_{\mathrm{op}}=\lambda,
\]

and `range(P)` is the strict top singular/eigenspace of `A`.

## D4-S4. Exact form of the remaining sign problem

For sign vectors `x,y`, orthogonality of the two invariant subspaces gives

\[
 x^TAy
 =\lambda\langle Ex,Ey\rangle
  +\langle (I-E)x,R(I-E)y\rangle.
\]

This explains why the rank-four vector witness saturates the universal
spectral bound `300 lambda`: its Gram projector is precisely the top space.
The desired classical theorem is the stronger discrete assertion that the
right-hand side is at most

\[
C=2081044153087351400
\]

for all sign vectors.  The generic estimate using only `||R||` is not sharp
enough, so a publishable completion must additionally exploit the restricted
Fourier/projection profiles of sign vectors, or provide the primal SOS or an
exact exhaustive certificate.

