# Adversarial audit of the finite-dimensional absolute-unbounded gap synthesis

Date: 2026-08-30

Status: second proposer-side pass, performed against the local primary PDFs. This is not the
independent review required for promotion to `PROVED`.

## Frozen claim under review

For every `G>0`, there are finite-dimensional channels `L,R` with

\[
 S_{\min}(L)+S_{\min}(R)-S_{\min}(L\otimes R)>G.
\]

The construction fixes `m>e^18`, then a finite depth `J`, and only afterward lets the per-leg
matrix dimension `D` grow. The audit must not replace this order by a simultaneous `J=J(D)` claim.

## 1. Match to Bordenave--Collins Theorem 9.2

For each `i in [m]` and `j in [J]`, the construction uses independent Haar unitaries
`U_{i,j}^{(D)}` placed on the `j`th tensor leg. Bordenave--Collins define exactly these matrices in
their Eq. (69) and Theorem 9.2: for fixed generator count and fixed tensor-leg count, the resulting
representation converges strongly in probability to the regular representation of the direct
product of free groups.

For `v in [m]^J`, the Kraus unitary

\[
 W_v^{(D)}=\bigotimes_{j=1}^J U_{v_j,j}^{(D)}
\]

therefore converges in the required polynomial sense to the canonical product word `u_v`. The
coefficient operator `sum a_{v,w}W_v^*W_w` is a fixed degree-two polynomial once `m,J` are fixed.

No step here permits `J` to grow inside the strong-convergence limit.

## 2. Uniformization over all coefficient matrices

Strong convergence is pointwise in each fixed matrix-valued polynomial. The proof needs one bound
simultaneously for every traceless `a in M_q`, where `q=m^J`.

For fixed `m,J`, the traceless Hilbert--Schmidt unit sphere is compact and finite dimensional. Both
the finite and free coefficient maps are Lipschitz there:

\[
 \left|\left\|\sum a_{v,w}V_{v,w}\right\|
 -\left\|\sum a'_{v,w}V_{v,w}\right\|\right|
 \le\sum_{v,w}|a_{v,w}-a'_{v,w}|
 \le q\|a-a'\|_2,
\]

because every `V_{v,w}` is unitary and the coefficient space has `q^2` coordinates. A finite net,
followed by a finite union of pointwise failure events, therefore gives the simultaneous estimate
with probability tending to one. The net size may be enormous in `m,J`, but is independent of `D`
after those parameters are fixed. This is enough for existence and for the stated high-probability
quantifier; it supplies no useful dimension rate.

## 3. Match to Collins--Youn Theorem 3.3

Collins--Youn Theorem 3.3 applies to every scalar coefficient matrix of trace zero and gives

\[
 \left\|\sum_{v,w}a_{v,w}u_v^*u_w\right\|
 \le m^{J/2}\sqrt{(1+9/m)^J-1}\,\|a\|_2.
\]

The index set, direct-product word, trace-zero hypothesis, Hilbert--Schmidt norm, and constant all
match the local construction. Combining this theorem with the finite net gives, for arbitrary
fixed `eta>0`, the same estimate with factor `1+eta` for a high-probability finite realization.

## 4. Complementary-channel duality check

The complementary channel of the product random-unitary channel is

\[
 L^c(S)_{v,w}=q^{-1}\operatorname{Tr}(W_vSW_w^*).
\]

Every diagonal entry is `1/q`. Set `X=L^c(S)-I_q/q`; then `X` is Hermitian, traceless, and has zero
diagonal. The identities used in the proof are exact:

\[
 \|X\|_2^2=\operatorname{Tr}(L^c(S)X)
 =\operatorname{Tr}(S(L^c)^*(X)).
\]

The adjoint is, up to the harmless transpose convention on coefficient indices,

\[
 (L^c)^*(X)=q^{-1}\sum_{v,w}X_{v,w}W_v^*W_w.
\]

Because `X` is Hermitian and `S` is a density matrix,

\[
 \operatorname{Tr}(S(L^c)^*(X))\le\|(L^c)^*(X)\|_\infty.
\]

The simultaneous coefficient estimate may therefore be applied to `X` itself, producing the
claimed Hilbert--Schmidt bound with no optimization/net interchange left over.

## 5. Entropy and minimization check

The purity decomposition

\[
 \operatorname{Tr}(L^c(S)^2)=q^{-1}+\|X\|_2^2
\]

is exact. Von Neumann entropy dominates order-two Renyi entropy, so the purity bound is a global
all-input entropy lower bound for `L^c`.

Minimum output entropy is attained on a pure input because entropy is concave. On every pure input
a channel and a complementary channel have the same nonzero output spectrum. Hence the global
bound for `L^c` is a valid bound for `S_min(L)`, not merely a bound on selected complementary
outputs. Complex conjugation preserves the spectrum, so the same bound holds for `bar L`.

Letting `eta` tend to zero after `m,J` are fixed yields

\[
 S_{\min}(L),S_{\min}(\bar L)
 \ge J[\log m-\log(1+9/m)]-\varepsilon.
\]

## 6. Bell upper bound check

For one layer, the `m^2` equal-weight Kraus outcomes on a maximally entangled input include `m`
equal-index outcomes. Each equals the same Bell vector because

\[
 (U\otimes\bar U)|\Omega_D\rangle=|\Omega_D\rangle.
\]

Merging those labels gives probabilities `1/m` and `m^2-m` copies of `1/m^2`. Entropy of a
mixture of pure states is at most the Shannon entropy of any realizing ensemble, even if further
linear dependencies occur. Thus the one-layer joint output entropy is at most

\[
 2\log m-\frac{\log m}{m}.
\]

The product of the `J` Bell inputs gives a tensor product of these outputs, so the entropy upper
bound adds exactly over the layers.

## 7. Positive coefficient and probability order

Combining the two side lower bounds and the joint upper bound gives

\[
 \Delta_{J,D}\ge Jc_m-2\varepsilon,
 \qquad
 c_m=\frac{\log m}{m}-2\log(1+9/m).
\]

For `ln m>18`, `log(1+9/m)<9/(m ln2)` proves `c_m>0`. For a prescribed `G`, first choose finite
`J>2G/c_m`, set `epsilon=Jc_m/4`, choose the corresponding fixed `eta`, and then let `D` grow.
The simultaneous coefficient event has probability tending to one and implies `Delta>G`.

The valid order is therefore

\[
 \forall G\;\exists J\;\exists\eta\;\lim_{D\to\infty}
 \Pr[\Delta_{J,D}>G]=1.
\]

No diagonal `J(D)` conclusion is used.

## 8. Finite-dimensional Holevo transfer and pair-to-self check

Fukuda Lemma 6.2 states the required identity for every pair of nonnegative tensor exponents,
including exponent zero. Subtracting the `(1,0)` and `(0,1)` cases from `(1,1)` preserves the
numerical pair defect exactly. The extension remains finite dimensional.

For the final same-channel reduction, the log-sum-exp formula for a flagged direct sum is exact.
The transferred conjugate pair has equal one-shot Holevo quantities, so the balance parameter is
`w=1/2` and

\[
 \chi(T^{\otimes2})-2\chi(T)
 \ge\log[1+\tfrac12(2^g-1)]\ge g-1.
\]

Thus an unbounded pair gap remains unbounded after conversion to one channel. The dimension
overheads are finite and linear in logarithmic size, but the uncontrolled `D(J)` still prevents a
full-size-extensive conclusion.

## Verdict and remaining review boundary

This adversarial pass found no mathematical or quantifier failure in the absolute-unbounded
synthesis. It repaired one stale evidence locator in the pair-to-self node. The proof remains
`CONJECTURED`, not `PROVED`, because this pass is not independent and the key theorem is a new
cross-paper synthesis rather than a quoted primary theorem.

The unresolved issue is not absolute unboundedness inside the derivation; it is the rate of the
finite-dimensional realization versus full logarithmic dimension cost, and independently the
need for an external reviewer before claim-level promotion.

## Primary sources

- Collins--Youn, arXiv:1907.07856v2, Theorem 3.3, statement and proof on local PDF pp. 11--12.
- Bordenave--Collins, arXiv:2304.05714v2, Eq. (69), Theorem 9.2 and Lemmas 9.3--9.4, local PDF
  pp. 62--65.
- Fukuda, arXiv:1307.0707, Lemma 6.2 and Eqs. (6.9)--(6.17), local PDF pp. 11--12.
