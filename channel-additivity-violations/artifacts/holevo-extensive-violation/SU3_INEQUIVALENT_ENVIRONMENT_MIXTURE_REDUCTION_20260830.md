# Exact Gram reduction for inequivalent SU(3) environment mixtures

Date: 2026-08-30

Status: exact proposer-side reduction plus finite numerical evidence; the final interior entropy
inequality remains open.

All logarithms are base two.

## 1. The three extreme channels

Fix an interior input irrep `R=V_(r,s)` with `r,s>=1` and dimension `d`. The three possible
irreducible Stinespring environments are

\[
 E_+=V_{(r-1,s)},
 \qquad E_m=V_{(r+1,s-1)},
 \qquad E_c=V_{(r,s+1)}.
\tag{1}
\]

Let their dimensions be `e_i` and define the dimension barycenter

\[
 \mu_i=\frac{e_i}{3d},
 \qquad
 \mu_++\mu_m+\mu_c=1.
\tag{2}
\]

Every irreducibly covariant qutrit-output channel with input `R` is a convex mixture

\[
 \Phi_\lambda
 =\lambda_+\Phi_++\lambda_m\Phi_m+\lambda_c\Phi_c,
 \qquad \lambda_i\ge0,
 \qquad \sum_i\lambda_i=1.
\tag{3}
\]

Orthogonal equivalent copies of each environment do not enlarge this simplex; they only realize
the same mixture weights after tracing the environment.

## 2. Exact Gram geometry

For a traceless qutrit `X` of Hilbert--Schmidt norm one, put

\[
 A_i=\Phi_i^*(X).
\tag{4}
\]

After aligning the common input representation bases, Schur orthogonality and the three Pieri
projectors give

\[
 \frac3d\operatorname{Tr}(A_iA_j)
 =-\frac18
 \quad(i\ne j),
\tag{5}
\]

and

\[
 \frac3d\operatorname{Tr}(A_i^2)
 =\frac1{8\mu_i}-\frac18.
\tag{6}
\]

The dimension-weighted mixture `lambda=mu` is the completely depolarizing channel. Equations
(5)--(6) imply the exact normalized Gram parameter

\[
 \boxed{
 t(\lambda)
 =\frac18\left(\sum_i\frac{\lambda_i^2}{\mu_i}-1\right)
 =\frac18\chi^2(\lambda\Vert\mu).}
\tag{7}
\]

Thus the full Gram problem is a classical chi-square distance on a two-dimensional simplex.

## 3. Highest-weight output

On one common highest-weight input, the three extreme output spectra have the common ordering

\[
 k_+= (1,0,0),
\tag{8}
\]

\[
 k_m=left(\frac1{r+2},\frac{r+1}{r+2},0\right),
\tag{9}
\]

and

\[
 k_c=\left(
 \frac1{r+s+3},
 \frac{r+s+2}{(s+2)(r+s+3)},
 \frac{(s+1)(r+s+2)}{(s+2)(r+s+3)}
 \right).
\tag{10}
\]

Therefore the explicit side-output distribution is

\[
 q(\lambda)=\lambda_+k_++\lambda_mk_m+\lambda_ck_c.
\tag{11}
\]

In particular,

\[
 S_{\min}(\Phi_\lambda)\le H(q(\lambda)).
\tag{12}
\]

## 4. The exact remaining scalar inequality

Let

\[
 B(t)=H\!\left(
 \frac{1+8t}{9},
 \underbrace{\frac{1-t}{9},\ldots,\frac{1-t}{9}}_{8\text{ times}}
 \right).
\tag{13}
\]

Equations (7) and (12) show that the entire interior covariant Bell route would be closed by

\[
 \boxed{
 B\!\left(\frac18\chi^2(\lambda\Vert\mu)\right)
 \ge2H(q(\lambda))
 \quad\text{for every }r,s\ge1\text{ and every }\lambda.}
\tag{14}
\]

This is now a two-variable classical entropy inequality with fully explicit rational coefficients.
It is not yet proved.

## 5. Numerical evidence and failed shortcut

A matrix-level scan aligned all extreme Stinespring maps for every input with `r+s<=4`, tested
1,554 mixture grid points, and minimized over 2,500 deterministic random states plus weight
vectors. It found no positive one-shot Bell candidate; the best sampled upper margin was numerical
zero at a completely depolarizing mixture.

An independent formula-only scan checked (14) for every interior `r+s<=30` on the denominator-120
simplex grid and found no negative value.

The simpler square-root-purity shortcut is false: for input `(1,1)` at the pure middle extreme,
the largest sampled output purity falls short of `1/3+2t/3` by exactly `1/36`. Hence (14) needs a
genuine Shannon-entropy proof rather than the earlier fixed-purity argument.

## 6. Research frontier

The next local target is to prove (14), preferably by converting (7) and the triangular stochastic
map (8)--(11) into a sharp relative-entropy inequality. A counterexample to (14) would not by
itself prove a Bell gap, because (12) is only an upper bound on the true minimum output entropy; it
would only invalidate this highest-weight certificate.
