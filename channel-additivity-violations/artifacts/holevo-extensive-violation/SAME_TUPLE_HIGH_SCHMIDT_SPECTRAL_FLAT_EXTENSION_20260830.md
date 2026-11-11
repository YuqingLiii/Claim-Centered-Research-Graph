# Same-tuple positive coefficients: spectral-flat and maximal-Schmidt extensions

Date: 2026-08-30

Status: proposer-side deterministic and conditional base cases, pending independent review.
Suggested nodes below should be assessed no higher than `CONJECTURED`.  No canonical YAML is
changed.  The general positive same-tuple coefficient theorem remains **OPEN**.

This note continues
[SAME_TUPLE_POSITIVE_DOUBLE_OFF_NEIGHBORHOODS_20260830.md](SAME_TUPLE_POSITIVE_DOUBLE_OFF_NEIGHBORHOODS_20260830.md).
That artifact controls a direction-uniform double-off class of operator-Schmidt rank `Theta(m)` by
its projective/Frobenius ratio.  Here two different structural norms give positive coefficients of
maximal or nearly maximal operator-Schmidt rank.  Neither argument estimates the double-off
projective norm term by term.

## 1. Setup

For a coefficient `Y in M_m tensor M_m`, define

\[
 \mathcal M_U(Y)
 ={1\over m^2}\sum_{v,a,w,b}Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b).
\tag{1}
\]

The target for `||Y||_F=1` is

\[
 \|\mathcal M_U(Y)\|_\infty\le {A\over m},
 \qquad
 A=1+{9(1+\eta)^2\over m}.
\tag{2}
\]

No randomness is needed for Sections 2--5.

## 2. Coefficient operator-norm contraction

The one-leg map has the Stinespring form

\[
 C^*(X)=V^*(X\otimes I)V,
 \qquad
 V\xi={1\over\sqrt m}\sum_{v=1}^m|v\rangle\otimes U_v\xi.
\tag{3}
\]

Since `V` is an isometry, `C^*` is unital and completely positive.  Hence
`M_U=C^* tensor C^*` is also unital and completely positive.  For every Hermitian coefficient
`H`, order preservation applied to

\[
 -\|H\|_\infty I\preceq H\preceq\|H\|_\infty I
\tag{4}
\]

gives the deterministic contraction

\[
 \boxed{
 \|\mathcal M_U(H)\|_\infty\le\|H\|_\infty.}
\tag{5}
\]

This coefficient spectral-norm interface is independent of operator-Schmidt rank and independent
of the repeated use of the tuple.

## 3. A general positive spectral-flat cone

Let `Y>=0` and `||Y||_F=1`.  Equation (5) proves

\[
 \boxed{
 \|Y\|_\infty\le {A\over m}
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y)\|_\infty\le {A\over m}.}
\tag{6}
\]

Equivalently, define the coefficient spectral effective rank

\[
 r_\infty(Y):={\|Y\|_F^2\over\|Y\|_\infty^2}
 ={1\over\|Y\|_\infty^2}.
\tag{7}
\]

Then the sufficient condition is

\[
 r_\infty(Y)\ge {m^2\over A^2}.
\tag{8}
\]

This is a stable cone condition, not a rank-counting statement.  It permits arbitrary entry
support, arbitrary rook projection, and maximal coefficient operator-Schmidt rank.

### 3.1 High-rank projections and low-rank holes

For every orthogonal projection `P` of coefficient spectral rank `r`,

\[
 Y={P\over\sqrt r}
\tag{9}
\]

is positive, Hilbert--Schmidt normalized, and satisfies the target whenever

\[
 r\ge {m^2\over A^2}.
\tag{10}
\]

Equivalently, let `H` be a projection of rank `k` and set `P=I-H`.  Then `P/sqrt(m^2-k)` is safe
whenever

\[
 k\le m^2\left(1-{1\over A^2}\right).
\tag{11}
\]

At fixed `eta`, the right side is

\[
 18(1+\eta)^2m+O((1+\eta)^4),
\tag{12}
\]

so one may remove a coefficient subspace of dimension linear in `m` while retaining a positive
coefficient of spectral rank `m^2-O(m)`.

The projection formulation has an equivalent aligned-output proof.  Since `0<=P<=I` and `M_U` is
unital positive,

\[
 0\preceq\mathcal M_U(P)\preceq I,
 \qquad
 \left\|\mathcal M_U\left({P\over\sqrt r}\right)\right\|_\infty
 \le {1\over\sqrt r}.
\tag{13}
\]

No spectral decomposition of `P` is summed in norm.

### 3.2 An explicit maximal operator-Schmidt-rank positive example

Let

\[
 |\Omega\rangle={1\over\sqrt m}\sum_{v=1}^m|v,v\rangle,
 \qquad
 Q=I-|\Omega\rangle\langle\Omega|.
\tag{14}
\]

Then

\[
 Y_\Omega^\perp={Q\over\sqrt{m^2-1}}
\tag{15}
\]

is positive, Hilbert--Schmidt normalized, and has coefficient spectral rank `m^2-1`.  Equation
(13) gives

\[
 \|\mathcal M_U(Y_\Omega^\perp)\|_\infty
 \le {1\over\sqrt{m^2-1}}.
\tag{16}
\]

For `m>=2` and `eta>=0`, the right side is at most `A/m`, because
`A>=1+1/m>=m/sqrt(m^2-1)`.

The coefficient operator-Schmidt rank of `Q` is exactly `m^2`.  Indeed, in the matrix-unit bases,

\[
 |\Omega\rangle\langle\Omega|
 ={1\over m}\sum_{v,w}E_{v,w}\otimes E_{v,w}.
\tag{17}
\]

After realignment, `I` contributes the rank-one matrix `u u^*` on the `m`-dimensional diagonal
matrix-unit subspace, where `||u||^2=m`, while (17) contributes `I_(m^2)/m`.  Thus the realigned
coefficient matrix of `Q` is

\[
 u u^*-{1\over m}I_{m^2}.
\tag{18}
\]

It has eigenvalue `m-1/m` along `u` and eigenvalue `-1/m` on its `m^2-1` dimensional orthogonal
complement. It is invertible, proving maximal operator-Schmidt rank. The trace of (15) is
`sqrt(m^2-1)`, so it exceeds `A` whenever `A<sqrt(m^2-1)` (including the intended large-`m`,
small-`eta` regime). This is a non-rank-one positive coefficient far beyond the preceding
`Theta(m)` explicit operator-Schmidt rank.

## 4. A spectral-norm double-off interface

Let `D>=0` be fully diagonal and let `E=E^*` be double-off-diagonal, meaning

\[
 E_{(v,a),(w,b)}=0
 \quad\hbox{unless}\quad v\ne w\ \hbox{and}\ a\ne b.
\tag{19}
\]

Assume

\[
 Y=D+E\succeq0,
 \qquad \|Y\|_F=1,
 \qquad s:=\|D\|_F.
\tag{20}
\]

The two coefficient sectors are Hilbert--Schmidt orthogonal.  The diagonal identity and (5) give

\[
 \|\mathcal M_U(D)\|_\infty
 ={\operatorname{Tr}D\over m^2}
 \le {s\over m},
 \qquad
 \|\mathcal M_U(E)\|_\infty\le\|E\|_\infty.
\tag{21}
\]

Therefore

\[
 \boxed{
 s+m\|E\|_\infty\le A
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y)\|_\infty\le {A\over m}.}
\tag{22}
\]

Condition (22) is amplitude-sensitive.  Unlike the earlier projective interface, it becomes
stronger as the double-off direction has large coefficient stable rank
`||E||_F^2/||E||_infty^2`.

## 5. A positive-definite double-off family of Schmidt rank `Theta(m^2)`

Define the off-diagonal flip

\[
 E_\times:=\sum_{v\ne w}E_{v,w}\otimes E_{w,v}.
\tag{23}
\]

It is Hermitian, double-off-diagonal, and satisfies

\[
 \|E_\times\|_F^2=m(m-1),
 \qquad
 \|E_\times\|_\infty=1.
\tag{24}
\]

Its displayed expansion is already an operator-Schmidt decomposition: the two matrix-unit
families are orthonormal.  Hence

\[
 \operatorname{OSR}(E_\times)=m(m-1),
 \qquad
 \pi_{\mathrm X}(E_\times)=m(m-1),
 \qquad
 {\pi_{\mathrm X}(E_\times)\over\|E_\times\|_F}=\sqrt{m(m-1)}.
\tag{25}
\]

The last ratio is order `m`, beyond the direction-uniform projective/Frobenius allowance of order
`sqrt(m)` in the preceding artifact.

For real `q`, put

\[
 Y_q={I+qE_\times\over
 \sqrt{m^2+q^2m(m-1)}}.
\tag{26}
\]

On the span of `|v,w>,|w,v>` with `v!=w`, `E_times` is the two-dimensional flip; on the span of
`|v,v>` it vanishes.  Consequently `Y_q` is positive definite for `|q|<1` and positive
semidefinite for `|q|=1`.

Using (5) directly as an operator-norm contraction, or using (22), gives

\[
 \begin{aligned}
 \|\mathcal M_U(Y_q)\|_\infty
 &\le {1+|q|\over\sqrt{m^2+q^2m(m-1)}}\\
 &\le {1+|q|\over m}.
 \end{aligned}
\tag{27}
\]

Thus the deterministic target holds throughout the explicit interval

\[
 \boxed{
 |q|\le\min\{1,A-1\}
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y_q)\|_\infty\le {A\over m}.}
\tag{28}
\]

For nonzero `q`, the coefficient operator-Schmidt rank of the numerator in (26) is

\[
 1+m(m-1).
\tag{29}
\]

Indeed `I tensor I` has Schmidt factors orthogonal to all off-diagonal matrix units in (23), so no
Schmidt direction cancels.  The coefficient spectral rank is the full `m^2` when `|q|<1`.  For
`m>A` and sufficiently small nonzero `q`, its trace is greater than `A`.

This family is not certified by a low operator-Schmidt-rank surrogate.  It is controlled because
the double-off direction has coefficient operator norm one despite Hilbert--Schmidt and projective
norms of order `m` and `m^2`, respectively.

### 5.1 Exact same-tuple image and the unresolved large-amplitude gate

Let `F_m` be the full coefficient flip and let

\[
 D_\times:=\sum_vE_{v,v}\otimes E_{v,v}.
\tag{30}
\]

Then `E_times=F_m-D_times`.  With

\[
 R_U={1\over m^2}\sum_{v,w}U_v^*U_w\otimes U_w^*U_v,
\tag{31}
\]

direct substitution gives

\[
 \mathcal M_U(E_\times)=R_U-{1\over m}I.
\tag{32}
\]

Therefore (26) has the exact output

\[
 \mathcal M_U(Y_q)
 ={I+q(R_U-I/m)\over\sqrt{m^2+q^2m(m-1)}}.
\tag{33}
\]

Extending (28) to `q=Theta(1)` would require nontrivial spectral control of the centered repeated-
tuple operator `R_U-I/m`; the coefficient operator-norm contraction alone gives only (27).  Thus
(28) is a genuine stable neighborhood, not a claimed solution of the Werner/flip spectral gate.

## 6. Why a naive square-function refinement does not solve the whole sector

Take an operator-Schmidt expansion

\[
 E=\sum_js_jX_j\otimes Z_j
\tag{34}
\]

with zero-diagonal Hilbert--Schmidt unit factors.  The operator Haagerup inequality gives

\[
 \left\|\sum_js_jC^*(X_j)\otimes C^*(Z_j)\right\|_\infty
 \le
 \left\|\sum_js_jC^*(X_j)C^*(X_j)^*\right\|_\infty^{1/2}
 \left\|\sum_js_jC^*(Z_j)^*C^*(Z_j)\right\|_\infty^{1/2}.
\tag{35}
\]

Kadison's inequality for the unital CP map only yields

\[
 C^*(X_j)C^*(X_j)^*\preceq C^*(X_jX_j^*),
\tag{36}
\]

and similarly on the other side.  Even in the ideal flat-square-function case

\[
 \sum_js_jX_jX_j^*={\sum_js_j\over m}I,
 \qquad
 \sum_js_jZ_j^*Z_j={\sum_js_j\over m}I,
\tag{37}
\]

equations (35)--(37) give

\[
 \|\mathcal M_U(E)\|_\infty\le {\sum_js_j\over m}.
\tag{38}
\]

The nuclear sum remains.  For a Hilbert--Schmidt unit equal-Schmidt rank-`r` direction it is
`sqrt(r)`, so (38) is order one at `r=Theta(m^2)`, rather than the required order `1/m`.

This is a precise obstruction to the unrefined Kadison/Haagerup route.  The special family in
Section 5 is instead seen by the coefficient operator norm, or by using the exact fact that every
matrix-unit image is a scaled unitary before applying any Kadison relaxation.  The obstruction is
to the proposed proof route, not to the original target.

## 7. Suggested atomic nodes (not registered here)

### 7.1 `HEXT.same-tuple-positive-spectral-flat-base-case`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> The same-tuple scalar coefficient map is unital completely positive and hence contracts the
> coefficient operator norm on Hermitian inputs.  Every positive Hilbert--Schmidt unit coefficient
> with spectral effective rank at least `m^2/A^2` satisfies the target deterministically.

Equations (3)--(8) give the proof.

### 7.2 `HEXT.same-tuple-maximal-Schmidt-complement-projector`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> The normalized coefficient projector orthogonal to the canonical maximally entangled vector is
> positive, has coefficient spectral rank `m^2-1` and operator-Schmidt rank exactly `m^2`, and
> satisfies the same-tuple target deterministically.

Equations (14)--(18) give the construction and rank proof.

### 7.3 `HEXT.same-tuple-positive-maximal-Schmidt-double-off-neighborhood`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> The family `(I+q E_times)/sqrt(m^2+q^2m(m-1))`, with `E_times` the off-diagonal coefficient flip, is
> positive for `|q|<=1`, has operator-Schmidt rank `1+m(m-1)` for `q!=0`, and satisfies the target
> deterministically for `|q|<=min(1,A-1)`.

Equations (23)--(29) are the proof.  The amplitude restriction must not be dropped.

### 7.4 `HEXT.same-tuple-high-Schmidt-kadison-haagerup-obstruction`

Suggested role: `obstruction`; suggested level before review: `CONJECTURED`.

Suggested claim:

> Applying operator Haagerup followed only by Kadison's inequality retains the coefficient
> nuclear sum even when both square functions are perfectly flat.  At equal Schmidt rank
> `Theta(m^2)` this route gives order one, not order `1/m`.

Equations (34)--(38) give the exact scope.

## 8. Status boundary

The spectral-flat cone and the explicit off-diagonal-flip neighborhood contain positive
coefficients of maximal or `Theta(m^2)` operator-Schmidt rank.  They rigorously pass beyond the
previous `Theta(m)` explicit-rank class without a projective/Frobenius assumption.

Operator-Schmidt rank by itself is not a sufficient invariant: Section 3 succeeds through
coefficient spectral flatness, while Section 5 succeeds only in a quantified amplitude interval.
No result here controls arbitrary high-Schmidt positive coefficients, constant-amplitude Werner
directions, or a positive coefficient with large coefficient operator norm.  No canonical
assessment should be promoted from this note without independent review.
