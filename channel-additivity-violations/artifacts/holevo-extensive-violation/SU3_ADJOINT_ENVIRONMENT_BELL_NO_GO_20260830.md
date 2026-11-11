# The adjoint-environment SU(3) qutrit channels have no conjugate-Bell gap

Date: 2026-08-30

Status: proposer-side exact finite-dimensional calculation; independent review pending.

All logarithms are base two.

## Setup

Let `B=C^3` carry the fundamental representation of `SU(3)` and let `E=C^8` carry the adjoint
representation. The multiplicity-free tensor product is

\[
 3\otimes8=15\oplus\bar6\oplus3.
\tag{1}
\]

For an irreducible summand `R` with projector `P_R` and dimension `d_R`, choose an isometry
`V_R:C^{d_R}->B tensor E` onto `R` and define

\[
 \Phi_R(X)=\operatorname{Tr}_E(V_RXV_R^*).
\tag{2}
\]

Covariance and irreducibility give

\[
 \Phi_R(I_{d_R}/d_R)=I_3/3,
\tag{3}
\]

and make `(3/d_R)Phi_R Phi_R^*` a qutrit depolarizing channel.

The highest summand `15` contains a product highest-weight vector, so `S_min(Phi_15)=0` and it
cannot have a positive Bell defect. The `3` summand has `d_R=k=3` and is already covered by the
depolarizing small-input no-go theorem. The only genuinely new oversized candidate is `R=bar6`.

## Theorem

For the channel `Phi_bar6:M_6->M_3`,

\[
 \boxed{
 \frac12\Phi_{\bar6}\Phi_{\bar6}^*=\Delta_{5/32},
 \qquad
 S_{\min}(\Phi_{\bar6})=1.}
\tag{4}
\]

Its conjugate-Bell output

\[
 Z_{\bar6}=(\Phi_{\bar6}\otimes\bar\Phi_{\bar6})(\Omega_6)
\tag{5}
\]

has spectrum

\[
 \left(\frac14,
 \underbrace{\frac3{32},\ldots,\frac3{32}}_{8}\right),
\tag{6}
\]

and therefore

\[
 \boxed{
 2\overline S_{\min}(\Phi_{\bar6})
 \le2
 <h_2(1/4)+\frac94
 =S(Z_{\bar6}).}
\tag{7}
\]

Thus the first nonsymmetric-environment oversized qutrit coupling also fails the fixed-channel
conjugate-Bell route.

## 1. Casimir projectors

Use fundamental generators `T_a=lambda_a/2`, normalized by
`Tr(T_a T_b)=delta_ab/2`, and Hermitian adjoint generators `F_a`. The total quadratic Casimir on
`3 tensor 8` is

\[
 C=\sum_{a=1}^8(T_a\otimes I+I\otimes F_a)^2.
\tag{8}
\]

For an `SU(3)` irrep `(p,q)`,

\[
 C_2(p,q)=\frac{p^2+q^2+pq+3p+3q}{3}.
\tag{9}
\]

The three eigenvalues of (8) are therefore

\[
 C_2(1,0)=\frac43,
 \qquad C_2(0,2)=\frac{10}{3},
 \qquad C_2(2,1)=\frac{16}{3},
\tag{10}
\]

with multiplicities `3,6,15`. In particular,

\[
 P_{\bar6}=-\frac14
 \left(C-\frac43I\right)
 \left(C-\frac{16}{3}I\right).
\tag{11}
\]

This polynomial gives a direct finite-matrix realization of the Stinespring subspace.

## 2. Exact Gram contraction

The adjoint representation occurs once in `End(bar6)`, so compression of a fundamental generator
to `bar6` is proportional to the total generator:

\[
 P_{\bar6}(T_a\otimes I)P_{\bar6}=cJ_a.
\tag{12}
\]

Taking the scalar product with the total generator and using

\[
 2J\mathbin{\cdot}T_B=C_{\bar6}+C_3-C_8
\tag{13}
\]

gives

\[
 c=\frac{C_{\bar6}+C_3-C_8}{2C_{\bar6}}
 =\frac{10/3+4/3-3}{20/3}=\frac14.
\tag{14}
\]

For `X=sqrt(2)T_a`, so that `Tr X^2=1`, the Dynkin-index identity gives

\[
 \operatorname{Tr}_{\bar6}J_X^2
 =\frac{d_{\bar6}C_{\bar6}}4=5.
\tag{15}
\]

Consequently

\[
 \operatorname{Tr}\Phi_{\bar6}^*(X)^2
 =\frac1{16}\operatorname{Tr}J_X^2=\frac5{16},
\tag{16}
\]

and the normalized Gram contraction is

\[
 t=\frac3{d_{\bar6}}\frac5{16}=\frac5{32}.
\tag{17}
\]

## 3. Exact minimum output entropy

For a unit output direction `u in C^3`, define the product-overlap block

\[
 B_u=(\langle u|\otimes I)P_{\bar6}(|u\rangle\otimes I)
 \quad\text{on }C^8.
\tag{18}
\]

Covariance makes its spectrum independent of `u`. Substituting `u=e_1` into the exact projector
(11) and using the Gell--Mann multiplication table gives

\[
 \operatorname{spec}(B_u)
 =\left(\frac12,\frac12,\frac12,
         \frac14,\frac14,0,0,0\right).
\tag{19}
\]

For every unit `psi in bar6`, its largest Schmidt coefficient across `B:E` is bounded by the
largest product overlap with the subspace:

\[
 \lambda_{\max}(\operatorname{Tr}_E|\psi\rangle\langle\psi|)
 \le\max_{u,v}\langle u\otimes v|P_{\bar6}|u\otimes v\rangle
 =\frac12.
\tag{20}
\]

The spectrum `(1/2,1/2,0)` majorizes every qutrit probability vector whose largest component is at
most `1/2`. Hence every output entropy is at least one bit. A highest-weight vector in `bar6`
has Schmidt spectrum exactly `(1/2,1/2,0)`, so the lower bound is attained and

\[
 S_{\min}(\Phi_{\bar6})=1.
\tag{21}
\]

## 4. Bell comparison

The Gram/realignment identity makes `Z_bar6` isospectral to the normalized Choi state of
`Delta_{5/32}`. Its exceptional eigenvalue is

\[
 \frac{1+8(5/32)}9=\frac14,
\tag{22}
\]

and each of the other eight eigenvalues is

\[
 \frac{1-5/32}{9}=\frac3{32}.
\tag{23}
\]

Thus

\[
 S(Z_{\bar6})=h_2(1/4)+\frac34\log 8
 =h_2(1/4)+\frac94>2,
\tag{24}
\]

which proves (7).

## 5. Scope and reproducibility

This closes every summand in the first nonsymmetric environment coupling `3 tensor 8`, but not
all `3 tensor V_(p,q)` couplings. The exact rational identities above are cross-checked by

```sh
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  holevo-extensive-violation/tools/check_su3_adjoint_coupling.py
```

The durable output is
`artifacts/SU3_ADJOINT_COUPLING_CHECK_20260830.txt`.

