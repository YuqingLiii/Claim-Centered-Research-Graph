# No irreducible SU(3)-covariant qutrit Pieri channel has a Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem; independent review pending.

All logarithms are base two.

## Theorem

Let the qutrit output `B=C^3` carry the fundamental representation of `SU(3)`, let the environment
carry an arbitrary irreducible representation `V_(p,q)`, and let the input be any irreducible
summand `R` in the multiplicity-free Pieri decomposition

\[
 3\otimes V_{(p,q)}
 =V_{(p+1,q)}
 \oplus V_{(p-1,q+1)}
 \oplus V_{(p,q-1)},
\tag{1}
\]

where summands with negative labels are omitted. Let `V_R:R->B tensor V_(p,q)` be the corresponding
isometry and

\[
 \Phi_R(X)=\operatorname{Tr}_E(V_RXV_R^*).
\tag{2}
\]

Then, for

\[
 Z_R=(\Phi_R\otimes\bar\Phi_R)(\Omega_{\dim R}),
\tag{3}
\]

one has

\[
 \boxed{
 2\overline S_{\min}(\Phi_R)
 \le2S_{\min}(\Phi_R)
 \le S(Z_R).}
\tag{4}
\]

Thus no channel obtained from one irreducible `SU(3)` Stinespring summand can seed a positive
fixed-channel conjugate-Bell regularized defect.

This does not classify reducible or multiplicity-bearing covariant dilations, arbitrary
noncovariant qutrit Gram factors, or non-Bell collective inputs.

## 1. Exact Pieri-channel data

Covariance gives `Phi_R(I/d_R)=I_3/3`. Since the scalar and traceless sectors of `M_3` are
irreducible, the normalized Gram channel is depolarizing:

\[
 \frac3{d_R}\Phi_R\Phi_R^*=\Delta_{t_R}.
\tag{5}
\]

The highest summand `R_+=V_(p+1,q)` contains a product highest-weight vector. Hence

\[
 S_{\min}(\Phi_{R_+})=0,
\tag{6}
\]

which immediately implies (4) for that branch.

The two lower branches have the following exact data.

### Middle branch

For `p>=1`, set `R_m=V_(p-1,q+1)`. Then

\[
 \boxed{
 t_m(p,q)=
 \frac{(2p-1)q+5p-1}{8(p+1)(q+1)},}
\tag{7}
\]

and

\[
 \boxed{
 S_{\min}(\Phi_{R_m})
 =h_2\left(\frac1{p+1}\right).}
\tag{8}
\]

The minimizing output spectrum is

\[
 \left(\frac p{p+1},\frac1{p+1},0\right).
\tag{9}
\]

### Third branch

For `q>=1`, set `R_c=V_(p,q-1)`. Then

\[
 \boxed{
 t_c(p,q)=
 \frac{(2q-1)p+2(q^2-1)}{8(q+1)(p+q+2)},}
\tag{10}
\]

and the minimizing output spectrum is

\[
 \boxed{
 r_{p,q}=\left(
 \frac{q(p+q+1)}{(q+1)(p+q+2)},
 \frac{p+q+1}{(q+1)(p+q+2)},
 \frac1{p+q+2}
 \right).}
\tag{11}
\]

Thus

\[
 S_{\min}(\Phi_{R_c})=H(r_{p,q}).
\tag{12}
\]

## 2. Derivation of the Pieri data

This section records the finite representation-theoretic calculation behind (7)--(12).

For a summand `R`, write `P_R` for its orthogonal projector and, for a unit qutrit vector `u`,
define

\[
 A_R(u)=V_R^*(|u\rangle\langle u|\otimes I)V_R.
\tag{13}
\]

For every input state `rho`,

\[
 \langle u|\Phi_R(\rho)|u\rangle=\operatorname{Tr}(\rho A_R(u)).
\tag{14}
\]

The spectrum of `A_R(u)` is independent of `u` by covariance. To evaluate it, use the total
quadratic Casimir on `3 tensor V_(p,q)`,

\[
 C=\sum_{a=1}^8(T_a\otimes I+I\otimes F_a)^2,
\tag{15}
\]

and the Lagrange projector

\[
 P_R=\prod_{R'\ne R}
 \frac{C-C_2(R')I}{C_2(R)-C_2(R')},
 \qquad
 C_2(a,b)=\frac{a^2+b^2+ab+3a+3b}{3}.
\tag{16}
\]

Substitute `u=e_1` and evaluate (16) in the Gelfand--Tsetlin basis. The extremal eigenvalues are

\[
 \lambda_{\max}(A_{R_m}(u))=\frac p{p+1},
\tag{17}
\]

and

\[
 \lambda_{\min}(A_{R_c}(u))=\frac1{p+q+2},
 \qquad
 \lambda_{\max}(A_{R_c}(u))
 =\frac{q(p+q+1)}{(q+1)(p+q+2)}.
\tag{18}
\]

The highest-weight vectors in the two lower summands have output spectra (9) and (11),
respectively. Equation (17) bounds every largest output eigenvalue in the middle branch, and (9)
majorizes every allowed spectrum. Equations (18) bound both the largest and smallest eigenvalues
in the third branch; consequently (11) majorizes every allowed spectrum. Schur concavity gives
(8) and (12), with equality on the stated highest-weight vectors.

For the Gram parameters, take `X=diag(1,-1,0)/sqrt(2)`. The same projector calculation gives

\[
 \frac3{d_{R_m}}
 \operatorname{Tr}\bigl(P_{R_m}(X\otimes I)P_{R_m}(X\otimes I)\bigr)
 =\frac{(2p-1)q+5p-1}{8(p+1)(q+1)},
\tag{19}
\]

and

\[
 \frac3{d_{R_c}}
 \operatorname{Tr}\bigl(P_{R_c}(X\otimes I)P_{R_c}(X\otimes I)\bigr)
 =\frac{(2q-1)p+2(q^2-1)}{8(q+1)(p+q+2)}.
\tag{20}
\]

These are (7) and (10). The calculation uses only (16), the Weyl dimension formula
`dim V_(a,b)=(a+1)(b+1)(a+b+2)/2`, and the Gelfand--Tsetlin action of the eight generators.

For auditability, the repository checker reconstructs the representations from Gell--Mann
generators and verifies (7), (9)--(11), (17)--(20) for all 30 mixed lower branches with
`p+q<=6`. The all-parameter conclusion below is symbolic and does not truncate at that cutoff.

## 3. The middle branch reduces monotonically to the symmetric boundary

For fixed `p`, equation (7) is a decreasing function of `q`, because

\[
 t_m(p,q)=\frac{(2p-1)q+5p-1}{8(p+1)(q+1)}
\tag{21}
\]

and `(5p-1)-(2p-1)=3p>0`. The side entropy (8) is independent of `q`.

The entropy of the isotropic Choi state `J(Delta_t)` decreases with `t>=0`. Therefore

\[
 S(J(\Delta_{t_m(p,q)}))
 \ge S(J(\Delta_{t_m(p,0)})).
\tag{22}
\]

The boundary `q=0` is exactly the symmetric-complement family already classified, for which

\[
 S(J(\Delta_{t_m(p,0)}))
 >2h_2\left(\frac1{p+1}\right).
\tag{23}
\]

Equations (8), (22), and (23) prove (4) strictly for the middle branch.

## 4. The third-branch gap worsens monotonically away from the conjugate boundary

Fix `q>=1` and put

\[
 x=p+q+2,
 \qquad c=\frac1x,
 \qquad A=\frac q{q+1},
 \qquad a=A(1-c).
\tag{24}
\]

Equation (11) becomes

\[
 r_{p,q}=\left(a,\frac{1-c}{q+1},c\right),
\tag{25}
\]

so its entropy is

\[
 S_c(c)=h_2(c)+(1-c)h_2\left(\frac1{q+1}\right).
\tag{26}
\]

Using (10), the exceptional eigenvalue of the isotropic Bell output is exactly `a/3`. Hence

\[
 S_B(c)=h_2(a/3)+3-a.
\tag{27}
\]

Define the nonnegative-direction margin

\[
 D_q(c)=S_B(c)-2S_c(c).
\tag{28}
\]

Differentiation gives

\[
 D_q'(c)=
 A\left[1-\frac13\log\frac{3-a}{a}\right]
 -2\left[\log\frac{1-c}{c}
          -h_2\left(\frac1{q+1}\right)\right].
\tag{29}
\]

For `q>=2`, the first bracket is at most one, while `c<=1/(q+2)` gives

\[
 \log\frac{1-c}{c}-h_2\left(\frac1{q+1}\right)
 \ge\log(q+1)-h_2\left(\frac1{q+1}\right)
 =A\log q.
\tag{30}
\]

Therefore `D_q'(c)<=A-2A log q<0`.

For `q=1`, direct substitution gives `D_1'(1/3)=0` and

\[
 D_1''(c)=\frac1{\ln2}
 \left[\frac{11}{6(1-c)}+\frac2c-\frac1{6(5+c)}\right]>0.
\tag{31}
\]

Thus `D_1'(c)<0` for `0<c<1/3` as well. Since increasing `p` decreases `c`, the margin `D_q`
can only increase away from the boundary `p=0`.

At `p=0`, this is exactly the conjugate-symmetric lower-summand family: its first member saturates
and every `q>=2` member has `D_q>0`. Hence (4) holds for every third-branch channel, strictly except
at the trivial singlet boundary.

## 5. Scope and reproducibility

The deterministic audit is run by

```sh
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  holevo-extensive-violation/tools/check_su3_pieri_channel_formulas.py
```

with durable output in
`artifacts/SU3_PIERI_CHANNEL_FORMULA_CHECK_20260830.txt`.

The theorem closes a broad structured qutrit route, but it does not solve the full fixed-channel
regularized problem. A surviving qutrit Bell candidate must break at least one assumption of this
classification: irreducible input/environment covariance, multiplicity-free single-summand
Stinespring form, or `SU(3)` covariance itself.

