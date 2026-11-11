# The SU(3) symmetric-complement channel family has no conjugate-Bell gap

Date: 2026-08-30

Status: proposer-side exact family theorem; independent review pending.

All logarithms are base two.

## The channel family

Let

\[
 B=\mathbb C^3,
 \qquad E_n=\operatorname{Sym}^n(\mathbb C^3),
 \qquad D_n=\dim E_n=\binom{n+2}{2}.
\tag{1}
\]

The standard bosonic splitting isometry

\[
 W_n:\operatorname{Sym}^{n+1}(\mathbb C^3)\longrightarrow B\otimes E_n
\tag{2}
\]

acts on occupation-number vectors as

\[
 W_n|m_1,m_2,m_3\rangle
 =\sum_{i=1}^3\sqrt{\frac{m_i}{n+1}}\,
 |i\rangle|m-e_i\rangle.
\tag{3}
\]

Write

\[
 Q_n=W_nW_n^*,
 \qquad P_n=I-Q_n,
 \qquad R_n=\operatorname{Ran}P_n.
\tag{4}
\]

This is the lower irreducible summand in

\[
 3\otimes\operatorname{Sym}^n(3)
 =\operatorname{Sym}^{n+1}(3)\oplus R_n,
\tag{5}
\]

with

\[
 d_n:=\dim R_n=3D_n-D_{n+1}=n(n+2).
\tag{6}
\]

Choose any isometry `V_n:C^{d_n}->B tensor E_n` onto `R_n` and define

\[
 \Phi_n(X)=\operatorname{Tr}_{E_n}(V_nXV_n^*).
\tag{7}
\]

Invariance of `P_n` under `U tensor Sym^n(U)` implies

\[
 \operatorname{Tr}_{E_n}P_n=\frac{d_n}{3}I_3,
 \qquad
 \Phi_n(I_{d_n}/d_n)=I_3/3.
\tag{8}
\]

Thus `Phi_n` is a maximally-mixed-preserving qutrit-output channel. The case `n=1` is the
three-dimensional antisymmetric channel; `n=2` is the first genuinely oversized factor,
`Phi_2:M_8->M_3`, arising from `3 tensor 6 = 10 direct-sum 8`.

## Theorem

For every integer `n>=1`, the Gram channel and minimum output entropy are

\[
 \boxed{
 \frac3{d_n}\Phi_n\Phi_n^*=\Delta_{t_n},
 \qquad
 t_n=\frac{5n-1}{8(n+1)},
 \qquad
 S_{\min}(\Phi_n)=h_2\left(\frac1{n+1}\right).}
\tag{9}
\]

Moreover, for

\[
 Z_n=(\Phi_n\otimes\bar\Phi_n)(\Omega_{d_n}),
\tag{10}
\]

one has the strict inequality

\[
 \boxed{
 2\overline S_{\min}(\Phi_n)
 \le2S_{\min}(\Phi_n)<S(Z_n).}
\tag{11}
\]

Hence this entire finite-dimensional qutrit covariant family fails the fixed-channel
conjugate-Bell route.

## 1. Exact depolarizing Gram parameter

For `X in M_3`,

\[
 \Phi_n^*(X)=V_n^*(X\otimes I_{E_n})V_n.
\tag{12}
\]

The Gram map is `SU(3)`-covariant. Since conjugation on `M_3` decomposes into the scalar and
irreducible traceless sectors, `(3/d_n)Phi_n Phi_n^*` is depolarizing. It remains to calculate its
traceless eigenvalue.

Take a traceless Hermitian `X` with `Tr X^2=1`. Using `P_n=I-Q_n`,

\[
 \begin{aligned}
 \operatorname{Tr}(\Phi_n^*(X)^2)
 &=\operatorname{Tr}\bigl(P_n(X\otimes I)P_n(X\otimes I)\bigr)\\
 &=D_n-2\frac{D_{n+1}}3
   +\operatorname{Tr}\bigl(Q_n(X\otimes I)Q_n(X\otimes I)\bigr).
 \end{aligned}
\tag{13}
\]

The compressed one-body observable satisfies

\[
 W_n^*(X\otimes I)W_n=\frac1{n+1}\,d\Gamma(X).
\tag{14}
\]

By unitary covariance take `X=diag(1,-1,0)/sqrt(2)`. Summing over the occupation-number basis of
`Sym^{n+1}(C^3)` gives

\[
 \operatorname{Tr}_{\operatorname{Sym}^{n+1}}
 d\Gamma(X)^2
 =\frac12\sum_{m_1+m_2+m_3=n+1}(m_1-m_2)^2
 =\binom{n+4}{4}.
\tag{15}
\]

Substitution into (13) yields

\[
 \operatorname{Tr}(\Phi_n^*(X)^2)
 =D_n-\frac{2D_{n+1}}3+\frac{\binom{n+4}{4}}{(n+1)^2}
 =\frac{n(n+2)(5n-1)}{24(n+1)}.
\tag{16}
\]

Multiplying by `3/d_n` proves

\[
 t_n=\frac3{d_n}\operatorname{Tr}(\Phi_n^*(X)^2)
 =\frac{5n-1}{8(n+1)}.
\tag{17}
\]

## 2. Exact minimum output entropy

For a unit vector `psi in R_n`, the largest eigenvalue of its `B` marginal is its largest squared
product overlap. Hence

\[
 \lambda_{\max}(\operatorname{Tr}_{E_n}|\psi\rangle\langle\psi|)
 \le\max_{u,v}\langle u\otimes v|P_n|u\otimes v\rangle.
\tag{18}
\]

Here `u in B` and `v in E_n` are unit vectors. Bosonic creation and annihilation give

\[
 \langle u\otimes v|Q_n|u\otimes v\rangle
 =\frac{1+\langle v|N_u|v\rangle}{n+1}
 \ge\frac1{n+1},
\tag{19}
\]

so

\[
 \lambda_{\max}\le\frac{n}{n+1}.
\tag{20}
\]

The probability vector `(n/(n+1),1/(n+1),0)` majorizes every qutrit spectrum satisfying (20).
Schur concavity therefore gives

\[
 S_{\min}(\Phi_n)\ge h_2\left(\frac1{n+1}\right).
\tag{21}
\]

Equality is attained. Choose orthogonal unit vectors `u,w in C^3` and set `v=w^{tensor n}`.
The normalized vector proportional to `P_n(u tensor v)` has Schmidt spectrum

\[
 \left(\frac{n}{n+1},\frac1{n+1},0\right).
\tag{22}
\]

This proves the entropy formula in (9).

## 3. Exact Bell spectrum and strict failure

The Gram/realignment identity makes `Z_n` isospectral to the normalized Choi state of
`Delta_{t_n}`. Its spectrum is

\[
 \alpha_n=\frac{1+8t_n}{9}=\frac{2n}{3(n+1)},
 \qquad
 \underbrace{\beta_n,\ldots,\beta_n}_{8},
 \qquad
 \beta_n=\frac{1-t_n}{9}=\frac{n+3}{24(n+1)}.
\tag{23}
\]

For `n=1`,

\[
 S(Z_1)=h_2(1/3)+2>2=2S_{\min}(\Phi_1).
\tag{24}
\]

For `n>=2`, binary entropy is increasing on `[0,1/2]`, so

\[
 2S_{\min}(\Phi_n)
 =2h_2\left(\frac1{n+1}\right)
 \le2h_2(1/3).
\tag{25}
\]

Also `t_n<5/8`, and the entropy of the isotropic Choi spectrum decreases with `t>=0`. Therefore

\[
 S(Z_n)>S(J(\Delta_{5/8}))
 =h_2(1/3)+1
 >2h_2(1/3),
\tag{26}
\]

where the final inequality is `h_2(1/3)<1`. Equations (25)--(26) prove (11).

## 4. Research consequence

This family was the most direct structured way to enter the surviving qutrit oversized regime:
the lower `SU(3)` summand has no product vectors, is exactly analyzable, and automatically has a
depolarizing Gram channel. Nevertheless the side entropy decreases while the Bell entropy stays
bounded away from it. The first member `M_8->M_3` misses the one-shot Bell threshold by about
`0.821151` bits, and the deficit grows again along the family after that point.

The result excludes this representation-theoretic branch, not all qutrit covariant channels. A
surviving search must use a different input/environment irrep coupling or a nondepolarizing qutrit
Gram channel, while still proving an all-copy side-entropy lower bound.

