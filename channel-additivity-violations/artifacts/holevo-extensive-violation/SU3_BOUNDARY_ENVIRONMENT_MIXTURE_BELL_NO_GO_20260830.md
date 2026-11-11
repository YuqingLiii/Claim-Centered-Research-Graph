# Inequivalent environment mixtures for SU(3) boundary inputs have no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem; independent review pending.

All logarithms are base two. Define

\[
 H_3(z)=H\!\left(\frac{1+2z}{3},\frac{1-z}{3},\frac{1-z}{3}\right),
 \qquad -\frac12\le z\le1,
\tag{1}
\]

and let `B(t)` be the entropy of the isotropic qutrit Gram-Choi spectrum

\[
 \left(\frac{1+8t}{9},
 \underbrace{\frac{1-t}{9},\ldots,\frac{1-t}{9}}_{8\text{ times}}\right).
\tag{2}
\]

## Theorem

Fix an irreducible input representation `R_(r,0)` or `R_(0,r)`, with `r>=1`. Every
`SU(3)`-covariant qutrit-output channel with this input is a convex mixture of its two irreducible
Stinespring extreme channels. Every such mixture `Phi` satisfies

\[
 \boxed{
 2\overline S_{\min}(\Phi)
 \le2S_{\min}(\Phi)
 \le S\!\left((\Phi\otimes\bar\Phi)(\Omega_{\dim R})\right).}
\tag{3}
\]

Thus coherent mixing of the two inequivalent environments does not reopen either boundary tower.

## 1. Symmetric input `R_(r,0)`

The two possible environments are `V_(r-1,0)` and `V_(r,1)`. Give the first extreme weight
`alpha`. Their dimension barycenter is

\[
 \mu=\frac{r}{3(r+2)}.
\tag{4}
\]

On a highest-weight input, the two output spectra, in a common ordering, are

\[
 (1,0,0),
 \qquad
 \left(\frac1{r+3},\frac{r+2}{2(r+3)},\frac{r+2}{2(r+3)}\right).
\tag{5}
\]

Their mixture has entropy `H_3(z)`, where

\[
 z=\frac{3(\alpha-\mu)(r+2)}{2(r+3)}.
\tag{6}
\]

The exact Gram simplex formula gives

\[
 t=\frac{(\alpha-\mu)^2}{8\mu(1-\mu)}
 =\frac{r+3}{4r}z^2.
\tag{7}
\]

Since `(r+3)/(4r)<=1`, one has `t<=z^2`.

## 2. Conjugate-symmetric input `R_(0,r)`

The two environments are `V_(1,r-1)` and `V_(0,r+1)`. If `alpha` is the first weight, the
dimension barycenter is

\[
 \mu=\frac{2r}{3(r+1)}.
\tag{8}
\]

The highest-weight output spectra are

\[
 \left(\frac12,\frac12,0\right),
 \qquad
 \left(\frac1{r+3},\frac1{r+3},\frac{r+1}{r+3}\right).
\tag{9}
\]

Up to a permutation, their mixture again has entropy `H_3(z)`, now with

\[
 z=-\frac{3(\alpha-\mu)(r+1)}{2(r+3)},
 \qquad
 t=\frac{r+3}{4r}z^2\le z^2.
\tag{10}
\]

## 3. Entropy inequality

The isotropic Bell entropy `B(t)` decreases on `0<=t<=1`. Strong minimum-output-entropy
additivity of the qutrit depolarizing channel gives, for `0<=a<=1`,

\[
 B(a^2)\ge2H_3(a).
\tag{11}
\]

For `0<=a<=1/2`, direct differentiation gives

\[
 \frac{d}{da}\bigl(H_3(a)-H_3(-a)\bigr)
 =\frac23\log_2\!\left(\frac{1-a^2}{1-4a^2}\right)\ge0.
\tag{12}
\]

Hence `H_3(-a)<=H_3(a)`. In both boundary families the allowed negative part of `z` lies in
`[-1/2,0]`. Combining (7), (10), (11), and (12) yields

\[
 B(t)\ge B(z^2)\ge2H_3(|z|)\ge2H_3(z).
\tag{13}
\]

The highest-weight state is an admissible side input, so `S_min(Phi)<=H_3(z)`. This proves (3).

## 4. Remaining covariant case

Only interior input weights `R_(r,s)` with `r,s>=1` retain three inequivalent environment
extremes. Their exact Gram geometry is finite-dimensional, but its two-parameter entropy inequality
is not proved here.
