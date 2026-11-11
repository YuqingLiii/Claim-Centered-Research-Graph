# Same-tuple positive coefficients: structured double-off-diagonal neighborhoods

Date: 2026-08-30

Status: proposer-side conditional lemmas and explicit positive families, pending independent
review.  Suggested nodes below should be assessed no higher than `CONJECTURED`.  No canonical YAML
is changed.  This note does not claim a theorem for arbitrary positive coefficients.

This note continues
[SAME_TUPLE_POSITIVE_ROOK_SUPPORT_20260830.md](SAME_TUPLE_POSITIVE_ROOK_SUPPORT_20260830.md).
That artifact proves the target for every positive rook-supported coefficient.  The present note
allows entries that change both coefficient labels.  The extension is structured: the rook part
must remain separately positive, and the double-off-diagonal part is measured by its projective
norm inside the two trace-zero one-leg spaces.

## 1. Setup

For `Y in M_m tensor M_m`, indexed by `(v,a),(w,b)`, write

\[
 \mathcal M_U(Y)
 ={1\over m^2}\sum_{v,a,w,b}Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b),
\tag{1}
\]

and

\[
 C^*(X)={1\over m}\sum_{v,w}X_{v,w}U_v^*U_w.
\tag{2}
\]

The target for `||Y||_F=1` is

\[
 \|\mathcal M_U(Y)\|_\infty\le {A\over m},
 \qquad
 A=1+{9(1+\eta)^2\over m}.
\tag{3}
\]

Put

\[
 \delta:=A-1,
 \qquad
 \alpha:=\sqrt{{A-1\over m}}=\sqrt{{\delta\over m}}.
\tag{4}
\]

The sole probabilistic premise is the existing uniform one-leg trace-zero event

\[
 \|C^*(X_0)\|_\infty\le\alpha\|X_0\|_F,
 \qquad \operatorname{Tr}X_0=0.
\tag{5}
\]

The event is used for complex matrices, so the projective decompositions below need not have
Hermitian factors term by term.

## 2. Rook and double-off coefficient sectors

Let `Delta_1` pinch onto `v=w`, let `Delta_2` pinch onto `a=b`, and define the Hilbert--Schmidt
orthogonal projections

\[
 \Pi_{\mathrm R}:=\Delta_1+\Delta_2-\Delta_1\Delta_2,
 \qquad
 \Pi_{\mathrm X}:=(I-\Delta_1)(I-\Delta_2).
\tag{6}
\]

Their ranges are complementary and orthogonal.  A matrix in `Ran(Pi_R)` is rook-supported.  A
matrix `E in Ran(Pi_X)` obeys

\[
 E_{(v,a),(w,b)}=0
 \quad\hbox{unless}\quad v\ne w\ \hbox{and}\ a\ne b.
\tag{7}
\]

Thus every row or column slice of `E` is off-diagonal and in particular trace zero.

For double-off `E`, define its off-diagonal Hilbert projective norm by

\[
 \pi_{\mathrm X}(E)
 :=\inf\left\{
 \sum_j\|X_j\|_F\|Z_j\|_F:
 E=\sum_jX_j\otimes Z_j,\quad
 \operatorname{diag}X_j=\operatorname{diag}Z_j=0
 \right\}.
\tag{8}
\]

Equivalently, it is the nuclear norm of `E` regarded as a vector in the Hilbert tensor product of
the two zero-diagonal matrix spaces.  In particular,

\[
 \pi_{\mathrm X}(E)\ge\|E\|_F,
\tag{9}
\]

with equality for every double-off simple tensor.

## 3. Exact two-use gain on the double-off sector

For each admissible simple tensor in (8), algebraic factorization and (5) give

\[
 \begin{aligned}
 \|\mathcal M_U(X_j\otimes Z_j)\|_\infty
 &=\|C^*(X_j)\|_\infty\|C^*(Z_j)\|_\infty\\
 &\le\alpha^2\|X_j\|_F\|Z_j\|_F.
 \end{aligned}
\tag{10}
\]

Taking the infimum over (8) yields the uniform interface

\[
 \boxed{
 \|\mathcal M_U(E)\|_\infty
 \le {\delta\over m}\pi_{\mathrm X}(E),
 \qquad E\in\operatorname{Ran}\Pi_{\mathrm X}.}
\tag{11}
\]

The extra factor `delta=A-1` is the available slack.  Using the full one-leg constant
`sqrt(A/m)` on either factor would lose it and would not give the extensions below.

## 4. A positive rook core plus one double-off Schmidt direction

Let

\[
 Y=Y_{\mathrm R}+E,
\tag{12}
\]

where

\[
 Y_{\mathrm R}\succeq0,\quad
 Y_{\mathrm R}\in\operatorname{Ran}\Pi_{\mathrm R},\quad
 E=X\otimes Z,\quad
 X=X^*,\ Z=Z^*,\quad
 \operatorname{diag}X=\operatorname{diag}Z=0.
\tag{13}
\]

Assume also that the total coefficient is positive and normalized:

\[
 Y\succeq0,
 \qquad \|Y\|_F=1.
\tag{14}
\]

Separate positivity of `Y_R` is a load-bearing premise; positivity of `Y` alone does not imply it,
because `Pi_R` is not a positive map.

Set

\[
 s:=\|Y_{\mathrm R}\|_F,
 \qquad e:=\|E\|_F.
\tag{15}
\]

The support sectors in (6) are Hilbert--Schmidt orthogonal, so

\[
 s^2+e^2=1.
\tag{16}
\]

The positive rook theorem, used homogeneously, gives

\[
 \|\mathcal M_U(Y_{\mathrm R})\|_\infty
 \le {\sqrt{2A-1}\over m}s.
\tag{17}
\]

Since the projective norm of the simple tensor `E` equals `e`, equation (11) gives

\[
 \|\mathcal M_U(E)\|_\infty\le{A-1\over m}e.
\tag{18}
\]

Combining (16)--(18) by Euclidean Cauchy--Schwarz produces the exact constant identity

\[
 \begin{aligned}
 \|\mathcal M_U(Y)\|_\infty
 &\le {1\over m}\left(\sqrt{2A-1}\,s+(A-1)e\right)\\
 &\le {1\over m}\sqrt{(2A-1)+(A-1)^2}\sqrt{s^2+e^2}\\
 &= {A\over m}.
 \end{aligned}
\tag{19}
\]

Thus

\[
 \boxed{
 \text{Premises (5), (12)--(14)}
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y)\|_\infty\le {A\over m}.}
\tag{20}
\]

There is no smallness assumption on `||E||_F` beyond positivity of the total coefficient.  The
new double-off direction can have entries with both `v!=w` and `a!=b`, which are excluded by the
rook theorem.

### 4.1 A checkable positivity neighborhood

If the positive rook core satisfies

\[
 Y_{\mathrm R}\succeq\rho I
\tag{21}
\]

and

\[
 \|E\|_\infty\le\rho,
\tag{22}
\]

then `Y_R+E>=0`.  After common Hilbert--Schmidt normalization, all premises of (20) remain true.
Equations (21)--(22) therefore give a direct, nonempty stable neighborhood rather than an abstract
positivity assumption.

For example, if `X,Z` are nonzero Hermitian zero-diagonal matrices, then

\[
 Y_t={I+tX\otimes Z\over\|I+tX\otimes Z\|_F}
\tag{23}
\]

is positive definite and covered by (20) whenever

\[
 |t|\,\|X\|_\infty\|Z\|_\infty<1.
\tag{24}
\]

It is full rank, has genuine double-off entries, and for `m>A` its trace is greater than `A` for
all sufficiently small nonzero `t`.

## 5. A higher-Schmidt neighborhood around a positive diagonal core

The simple-tensor condition can be relaxed substantially when the separately positive core is
fully diagonal.  Let

\[
 Y=D+E,
 \qquad
 D\succeq0\text{ fully diagonal},
 \qquad
 E=E^*\in\operatorname{Ran}\Pi_{\mathrm X},
 \qquad
 Y\succeq0,
 \qquad
 \|Y\|_F=1.
\tag{25}
\]

Put `s=||D||_F` and `e=||E||_F`, so again `s^2+e^2=1`.  The diagonal output is exact:

\[
 \mathcal M_U(D)={\operatorname{Tr}D\over m^2}I,
 \qquad
 \|\mathcal M_U(D)\|_\infty\le {s\over m},
\tag{26}
\]

where `Tr(D)<=m||D||_F` uses the `m^2` nonnegative diagonal entries.  Equations (11) and (26)
give the amplitude-sensitive sufficient condition

\[
 \boxed{
 s+(A-1)\pi_{\mathrm X}(E)\le A
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y)\|_\infty\le {A\over m}.}
\tag{27}
\]

Around every positive-definite diagonal core, this is already a stable neighborhood in each fixed
double-off direction: at `E=0`, its left side is at most one, strictly below `A`, and positivity is
preserved for a sufficiently small perturbation.

A direction-uniform form follows from the shared Hilbert--Schmidt budget.  Define

\[
 \kappa_A:=\sqrt{{A+1\over A-1}}.
\tag{28}
\]

If

\[
 \pi_{\mathrm X}(E)\le\kappa_A\|E\|_F,
\tag{29}
\]

then

\[
 \begin{aligned}
 s+(A-1)\pi_{\mathrm X}(E)
 &\le s+(A-1)\kappa_A e\\
 &\le\sqrt{1+(A-1)^2\kappa_A^2}\sqrt{s^2+e^2}\\
 &=A.
 \end{aligned}
\tag{30}
\]

Consequently every coefficient satisfying (25) and (29) reaches the target.  Since

\[
 \kappa_A^2={A+1\over A-1}
 =1+{2m\over9(1+\eta)^2},
\tag{31}
\]

this permits projective/Frobenius ratios of order `sqrt(m)`, not merely a single Schmidt
direction.

### 5.1 Explicit operator-Schmidt rank growing linearly in `m`

Choose Hilbert--Schmidt orthonormal Hermitian zero-diagonal families

\[
 X_1,\ldots,X_r,
 \qquad
 Z_1,\ldots,Z_r,
\tag{32}
\]

and set

\[
 E_0={1\over\sqrt r}\sum_{j=1}^rX_j\otimes Z_j.
\tag{33}
\]

Then

\[
 \|E_0\|_F=1,
 \qquad
 \pi_{\mathrm X}(E_0)=\sqrt r.
\tag{34}
\]

For every integer

\[
 r\le \min\left\{m(m-1),{A+1\over A-1}\right\},
\tag{35}
\]

condition (29) holds.  For sufficiently small nonzero `t`,

\[
 Y_t={I+tE_0\over\sqrt{m^2+t^2}}
\tag{36}
\]

is positive definite, Hilbert--Schmidt normalized, and has coefficient operator-Schmidt rank
`r+1`.  It has nonzero double-off entries and trace

\[
 \operatorname{Tr}Y_t={m^2\over\sqrt{m^2+t^2}},
\tag{37}
\]

which is greater than `A` for `m>A` and sufficiently small `t`.  Equation (31) allows `r` linear
in `m` at fixed `eta`.  This is genuinely beyond the rank-one or one-double-off-direction cases.

## 6. Scope of the projective control

For a general double-off coefficient with operator-Schmidt singular values `sigma_j`,

\[
 \pi_{\mathrm X}(E)=\sum_j\sigma_j,
 \qquad
 \|E\|_F=\left(\sum_j\sigma_j^2\right)^{1/2}.
\tag{38}
\]

Thus no dimension-free inequality can replace `pi_X(E)` by `||E||_F`.  Equal singular values at
rank `r` give the exact ratio `sqrt(r)`.  The zero-diagonal matrix space has dimension
`m(m-1)`, so this ratio can be of order `m`, whereas the direction-uniform allowance in (31) is
only of order `sqrt(m)`.

This is a precise obstruction to extending the proof of Section 5 to the entire double-off
Frobenius sphere by norm comparison.  It is not a counterexample to the desired same-tuple target:
closing the remaining directions would require a genuine two-leg improvement over the
projective triangle inequality in (11).

## 7. Suggested atomic nodes (not registered here)

### 7.1 `HEXT.same-tuple-double-off-projective-interface`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> On the uniform one-leg trace-zero event, every coefficient supported on entries changing both
> labels obeys `||M_U(E)|| <= (A-1) pi_X(E)/m`, where `pi_X` is the Hilbert projective norm over
> the two zero-diagonal coefficient spaces.

Equations (8)--(11) give the proof and exact norm convention.

### 7.2 `HEXT.same-tuple-positive-rook-plus-double-off-direction`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> If a positive Hilbert--Schmidt unit coefficient is the orthogonal sum of a separately positive
> rook-supported core and one Hermitian zero-diagonal simple tensor in the double-off sector, then
> it satisfies the same-tuple target on the one-leg trace-zero event.

Equations (12)--(20) are the proof.  Separate positivity of the rook core must be explicit.

### 7.3 `HEXT.same-tuple-positive-diagonal-core-projective-neighborhood`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> A positive Hilbert--Schmidt unit coefficient with a separately positive fully diagonal core and
> Hermitian double-off remainder reaches the target if
> `pi_X(E)<=sqrt((A+1)/(A-1)) ||E||_F`.  This includes positive definite examples of
> operator-Schmidt rank `r+1` for every `r<=min(m(m-1),(A+1)/(A-1))`.

Equations (25)--(37) give the proof and explicit family.

### 7.4 `HEXT.same-tuple-double-off-projective-frobenius-obstruction`

Suggested role: `obstruction`; suggested level before review: `CONJECTURED`.

Suggested claim:

> Projective-norm summation cannot cover the full double-off Hilbert--Schmidt sphere: its exact
> projective/Frobenius ratio is `sqrt(r)` on an equal-Schmidt rank-`r` direction and can be of order
> `m`.  This is an obstruction to that proof route, not to the original norm target.

Equation (38) and the dimension count give the precise scope.

## 8. Status boundary

The results above provide nonempty stable positive neighborhoods with genuine double-off entries.
They include full-rank coefficients with trace greater than `A`, and the diagonal-core theorem
allows coefficient operator-Schmidt rank growing linearly in `m`.

They do not cover a positive coefficient whose rook projection is indefinite, an arbitrary
double-off remainder of high projective/Frobenius ratio, or the general positive cone.  Positivity
of the total coefficient never silently replaces separate positivity of the retained core.  No
canonical assessment should be promoted from this note without independent review.
