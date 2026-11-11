# Finite-subspace spatialization gate for the commuting-operator construction

Date: 2026-08-30

Status: proposer-side exact scope calculation; no independent review.

## Why finite restriction initially looks promising

Let `Phi_l` be a Collins--Youn/Kalantar--Shobeiri random-unitary channel built from a left regular
representation on an infinite Hilbert space `H`, and let `Phi_l^c` be its finite-output
complementary channel. If `J_K:K->H` is any finite-dimensional input isometry, then

\[
 N_K=\Phi_l^c\circ\operatorname{Ad}(J_K)
\]

is a genuinely finite-dimensional channel. For every tensor exponent `r`, its input set is a
subset of the infinite channel's input set, so

\[
 S_{\min}(N_K^{\otimes r})
 \ge S_{\min}((\Phi_l^c)^{\otimes r}).
\tag{1}
\]

Thus the infinite-dimensional all-copy **side lower bound** is inherited by every finite input
restriction. This observation by itself does not solve the finite-dimensional problem, because the
low-entropy joint witness is a separate obligation.

## The commuting witness is not a tensor-product witness

Collins--Youn use left and right regular Kraus systems on the same `H`. Those systems commute, and
their low output is obtained by composing the two channels on the vector `delta_e`. In infinite
dimension this commuting-operator product is not a spatial tensor product of two finite input
systems.

After restricting the two channels separately, `delta_e` is not automatically a state on
`K tensor K`, and the equality of the relevant left/right moments is not automatically represented
by a finite-dimensional entangled vector. Producing such a vector while retaining (1) is precisely
a finite spatialization problem; it is not supplied by input restriction.

## Exact calculation for the natural finite-set spatialization

Let `G` be a discrete group, `S={s_1,...,s_m}` a finite generator set and `F subset G` a nonempty
finite set. Put

\[
 K_F=\operatorname{span}\{\delta_x:x\in F\},
 \quad
 |u_F\rangle=|F|^{-1/2}\sum_{x\in F}|x\rangle,
\]

and use the restricted Stinespring isometry whose output vectors are the left translates
`lambda(s_i)K_F`. The most direct tensor-product surrogate of the commuting witness is

\[
 |\Omega_F\rangle=|F|^{-1/2}\sum_{x\in F}|x\rangle\otimes|x\rangle.
\]

For the single-side test vectors `|u_{s_iF}>` one has

\[
 \langle u_{s_iF}|u_{s_jF}\rangle
 =\frac{|s_iF\cap s_jF|}{|F|}.
\tag{2}
\]

For the equal-index joint vectors

\[
 |\Omega_{s_iF}\rangle
 =(\lambda(s_i)\otimes\overline{\lambda(s_i)})|\Omega_F\rangle,
\]

one has the identical formula

\[
 \langle\Omega_{s_iF}|\Omega_{s_jF}\rangle
 =\frac{|s_iF\cap s_jF|}{|F|}.
\tag{3}

Therefore the two uniform mixtures

\[
 \sigma_{\rm side}=m^{-1}\sum_i|u_{s_iF}\rangle\!\langle u_{s_iF}|,
 \qquad
 \sigma_{\rm match}=m^{-1}\sum_i|\Omega_{s_iF}\rangle\!\langle\Omega_{s_iF}|
\]

have the same Gram matrix and hence exactly the same nonzero spectrum:

\[
 \boxed{S(\sigma_{\rm side})=S(\sigma_{\rm match}).}
\tag{4}
\]

Equation (4) exposes the finite-set tradeoff. Making the matched joint vectors nearly coincide
requires the translates `s_iF` to overlap strongly. The same overlaps make the one-channel output
on `u_F` low entropy. Conversely, the nonamenable/free behavior that keeps the side entropy high
also keeps the natural matched tensor-product sector high entropy.

## Consequence for the Bell-style entropy estimate

Let `h_F=S(sigma_side)=S(sigma_match)`. Grouping the `m` equal-index outcomes in the joint pure-state
ensemble of the restricted random-unitary channel and its conjugate gives the upper bound below.
For a pure input, a channel and its complement have the same nonzero output spectrum; the same is
true for the product channel and the product of the two complements. Hence the bound applies to the
finite-output complementary pair `N_KF tensor bar(N_KF)`:

\[
 S_{\min}(N_{K_F}\otimes\overline{N_{K_F}})
 \le 2\log m-\frac{\log m}{m}+\frac{h_F}{m}.
\tag{5}
\]

The extra term `h_F/m` is absent in the true commuting witness, where all matched outcomes
coincide. But the same `h_F` is already a valid one-channel output entropy, so

\[
 S_{\min}(N_{K_F})\le h_F.
\tag{6}
\]

Equations (4)--(6) do not prove that every finite restriction is additive; another joint input
might work. They do prove that the obvious `Omega_F` spatialization cannot independently preserve
the commuting collision while evading its matching one-side entropy loss.

## Exact remaining requirement

A successful finite restriction route needs a finite-dimensional pair and a joint vector whose
mixed left/right moments reproduce the low commuting output **without** creating a comparably low
single-side test state. Equivalently, it must break the Gram-matrix identity (4) by a genuinely
different spatialization, while retaining the inherited all-copy side lower bound (1).

Finite-depth random-matrix microstates achieve the desired joint Bell collision, but their fixed
finite realizations lack the all-copy side estimate. Finite input restrictions inherit the
all-copy side estimate, but the natural spatial witness obeys (4). Bridging these two properties is
the unresolved finite-dimensional regularized-MOE gate.
