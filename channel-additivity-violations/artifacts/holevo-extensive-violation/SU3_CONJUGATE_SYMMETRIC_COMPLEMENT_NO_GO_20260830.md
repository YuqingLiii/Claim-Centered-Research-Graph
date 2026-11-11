# The SU(3) conjugate-symmetric lower-summand family has no Bell gap

Date: 2026-08-30

Status: proposer-side exact family theorem; independent review pending.

All logarithms are base two.

## Family and theorem

For `n>=1`, consider

\[
 B=\mathbb C^3,
 \qquad
 E_n=\operatorname{Sym}^n(\overline{\mathbb C^3}),
\tag{1}
\]

and the lower summand in

\[
 3\otimes\operatorname{Sym}^n(\bar3)
 =(1,n)\oplus(0,n-1).
\tag{2}
\]

Its input space is

\[
 R_n=\operatorname{Sym}^{n-1}(\bar3),
 \qquad
 d_n=\dim R_n=\frac{n(n+1)}2.
\tag{3}
\]

The equivariant isometry `W_n:R_n->B tensor E_n` is

\[
 W_n|\psi\rangle
 =\frac1{\sqrt{n+2}}\sum_{i=1}^3
 |i\rangle\otimes a_i^\dagger|\psi\rangle,
\tag{4}
\]

where the creation operators act on the three conjugate bosonic modes. Indeed,

\[
 W_n^*W_n=\frac1{n+2}\sum_i a_i a_i^\dagger
 =\frac{N+3}{n+2}=I
\tag{5}
\]

on the `N=n-1` sector. Define

\[
 \Phi_n(X)=\operatorname{Tr}_{E_n}(W_nXW_n^*).
\tag{6}
\]

Then

\[
 \boxed{
 \frac3{d_n}\Phi_n\Phi_n^*=\Delta_{t_n},
 \qquad
 t_n=\frac{n-1}{4(n+2)},}
\tag{7}
\]

and

\[
 \boxed{
 S_{\min}(\Phi_n)
 =H\left(\frac n{n+2},\frac1{n+2},\frac1{n+2}\right).}
\tag{8}
\]

For the conjugate-Bell output

\[
 Z_n=(\Phi_n\otimes\bar\Phi_n)(\Omega_{d_n}),
\tag{9}
\]

one has equality at `n=1` and strict failure thereafter:

\[
 2S_{\min}(\Phi_1)=S(Z_1)=2\log3,
\tag{10}
\]

while

\[
 \boxed{
 2\overline S_{\min}(\Phi_n)
 \le2S_{\min}(\Phi_n)<S(Z_n),
 \qquad n\ge2.}
\tag{11}
\]

## 1. Maximally mixed output and depolarizing Gram form

Equivariance and irreducibility imply

\[
 \Phi_n(I_{d_n}/d_n)=I_3/3.
\tag{12}
\]

The same covariance makes `(3/d_n)Phi_n Phi_n^*` scalar on the scalar and traceless sectors of
`M_3`, hence depolarizing.

For a traceless `X in M_3`, equation (4) gives

\[
 \Phi_n^*(X)
 =\frac1{n+2}\sum_{i,j}X_{ij}a_i a_j^\dagger
 =\frac1{n+2}\,d\Gamma(X^T).
\tag{13}
\]

If `X` is Hermitian with `Tr X^2=1`, the occupation-number trace on
`Sym^{n-1}(bar3)` is

\[
 \operatorname{Tr}d\Gamma(X^T)^2=\binom{n+2}{4}.
\tag{14}
\]

Therefore

\[
 \operatorname{Tr}\Phi_n^*(X)^2
 =\frac{\binom{n+2}{4}}{(n+2)^2}
 =\frac{n(n+1)(n-1)}{24(n+2)},
\tag{15}
\]

and

\[
 t_n=\frac3{d_n}\operatorname{Tr}\Phi_n^*(X)^2
 =\frac{n-1}{4(n+2)}.
\tag{16}
\]

## 2. Exact minimum output entropy

For a pure input `psi`, define its one-particle matrix

\[
 \gamma_{ij}=\langle\psi|a_j^\dagger a_i|\psi\rangle.
\tag{17}
\]

It is positive semidefinite and has trace `n-1`. Directly from (4), the output is, up to a fixed
transpose convention,

\[
 \Phi_n(\psi)=\frac{I_3+\gamma}{n+2}.
\tag{18}
\]

If `mu_1>=mu_2>=mu_3>=0` are the eigenvalues of `gamma`, then their sum is `n-1`, and the output
spectrum is

\[
 \left(\frac{1+\mu_1}{n+2},
       \frac{1+\mu_2}{n+2},
       \frac{1+\mu_3}{n+2}\right).
\tag{19}
\]

The vector

\[
 q_n=\left(\frac n{n+2},\frac1{n+2},\frac1{n+2}\right)
\tag{20}
\]

majorizes every such spectrum. It is attained by a coherent bosonic input
`psi=w^{tensor(n-1)}`, for which `gamma=(n-1)|w><w|`. Schur concavity proves (8).

## 3. Bell spectrum

The Gram/realignment identity makes `Z_n` isospectral to the normalized Choi state of
`Delta_{t_n}`. Substituting (7), its spectrum is

\[
 \alpha_n=\frac{1+8t_n}{9}=\frac{n}{3(n+2)},
 \qquad
 \underbrace{\beta_n,\ldots,\beta_n}_{8},
 \qquad
 \beta_n=\frac{1-t_n}{9}=\frac{n+3}{12(n+2)}.
\tag{21}
\]

At `n=1`, `t_1=0`; both sides of (10) are maximally mixed and equality holds.

For `n=2`, `S_min=3/2` while

\[
 S(Z_2)=H\left(\frac16,\underbrace{\frac5{48},\ldots,\frac5{48}}_8\right)>3.
\tag{22}
\]

For `n=3`, `S_min=H(3/5,1/5,1/5)<3/2` while

\[
 S(Z_3)=H\left(\frac15,\underbrace{\frac1{10},\ldots,\frac1{10}}_8\right)
 =h_2(1/5)+\frac{12}{5}>3.
\tag{23}
\]

For `n>=4`, the spectra `q_n` become successively more peaked, so

\[
 2S_{\min}(\Phi_n)
 \le2H(2/3,1/6,1/6)
 =2h_2(1/3)+\frac23.
\tag{24}
\]

Also `t_n<1/4`, and isotropic Choi entropy decreases with its nonnegative depolarizing parameter.
Hence

\[
 S(Z_n)>S(J(\Delta_{1/4}))=h_2(1/3)+2.
\tag{25}
\]

Since `h_2(1/3)<1`, the right side of (24) is strictly smaller than the right side of (25). This
proves (11) for all `n>=2`.

## 4. Research consequence

Together with the symmetric-environment family, this closes both elementary `SU(3)` bosonic
towers. Neither making the environment a larger symmetric power nor a larger conjugate symmetric
power yields a qutrit fixed-channel Bell seed. The latter tower is especially unfavorable: its
Gram contraction remains below `1/4` while its exact side entropy tends to zero.

The surviving covariant search must use genuinely mixed highest weights `(p,q)` with both entries
nonzero and not merely the adjoint case already classified, or leave the depolarizing Gram class.

