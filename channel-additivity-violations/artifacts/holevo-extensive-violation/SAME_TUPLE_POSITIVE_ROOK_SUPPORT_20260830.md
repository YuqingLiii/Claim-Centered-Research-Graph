# Same-tuple positive coefficients: a target-tight rook-support class

Date: 2026-08-30

Status: proposer-side exact algebra and a conditional target-tight lemma, pending independent
review.  Suggested nodes below should be assessed no higher than `CONJECTURED`.  No canonical YAML
is changed, and the arbitrary positive-coefficient problem remains **OPEN**.

This note continues
[SAME_TUPLE_POSITIVE_POLARIZED_GRAM_EXTENSION_20260830.md](SAME_TUPLE_POSITIVE_POLARIZED_GRAM_EXTENSION_20260830.md).
That note showed that direct spectral summation loses the factor `Tr(Y)` and hence cannot prove a
uniform positive rank-two result.  Here a larger class is controlled without spectral summation.
The gain comes from an exact inclusion--exclusion identity for two commuting coefficient
pinchings, followed by Hilbert--Schmidt orthogonality of their three disjoint support sectors.

## 1. Setup and premise

For `Y in M_(m^2)`, indexed by `(v,a),(w,b)`, let

\[
 \mathcal M_U(Y)
 ={1\over m^2}\sum_{v,a,w,b}Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b),
\tag{1}
\]

and

\[
 C^*(X)={1\over m}\sum_{a,b}X_{a,b}U_a^*U_b.
\tag{2}
\]

For a Hilbert--Schmidt unit coefficient the target is

\[
 \|\mathcal M_U(Y)\|_\infty\le {A\over m},
 \qquad
 A=1+{9(1+\eta)^2\over m}.
\tag{3}
\]

The only probabilistic premise used below is the already isolated uniform one-leg trace-zero
event

\[
 \|C^*(X_0)\|_\infty\le\alpha\|X_0\|_F,
 \qquad
 \operatorname{Tr}X_0=0,
 \qquad
 \alpha:=\sqrt{{A-1\over m}}.
\tag{4}
\]

It is important that (4) is uniform in `X_0`.  No net over the two-leg positive class is added.

## 2. The positive rook-support class

Let `Delta_1` be coefficient pinching onto `v=w`, and let `Delta_2` be coefficient pinching onto
`a=b`.  They are commuting orthogonal projections in Hilbert--Schmidt space.  Define

\[
 P:=\Delta_1Y,
 \qquad
 Q:=\Delta_2Y,
 \qquad
 D:=\Delta_1\Delta_2Y.
\tag{5}
\]

Call `Y` rook-supported when

\[
 Y_{(v,a),(w,b)}=0
 \quad\hbox{whenever}\quad v\ne w\ \hbox{and}\ a\ne b.
\tag{6}
\]

Equivalently,

\[
 Y=P+Q-D.
\tag{7}
\]

This strictly contains both one-leg-diagonal classes.  It permits simultaneous coherences within
coefficient rows and within coefficient columns, as long as no entry changes both labels at once.

Assume henceforth that

\[
 Y\succeq0,
 \qquad \|Y\|_F=1,
 \qquad Y\text{ is rook-supported}.
\tag{8}
\]

Let

\[
 R:=\operatorname{Tr}_1Y,
 \qquad
 L:=\operatorname{Tr}_2Y,
 \qquad
 \tau:=\operatorname{Tr}Y.
\tag{9}
\]

## 3. Exact commuting-output identity

The `v=w` terms satisfy

\[
 \mathcal M_U(P)={1\over m}I\otimes C^*(R),
\tag{10}
\]

because the `Q-D` sector has zero first partial trace.  Similarly,

\[
 \mathcal M_U(Q)={1\over m}C^*(L)\otimes I.
\tag{11}
\]

The fully diagonal sector has the exact scalar output

\[
 \mathcal M_U(D)={\tau\over m^2}I.
\tag{12}
\]

Thus (7) gives the exact identity

\[
 \boxed{
 \mathcal M_U(Y)
 ={1\over m}I\otimes C^*(R)
 +{1\over m}C^*(L)\otimes I
 -{\tau\over m^2}I.}
\tag{13}
\]

This is where the earlier partial-trace contraction is sharpened.  Estimating the first two terms
separately would count the diagonal mass twice.  Equation (13) removes the duplicate exactly.
The two remaining non-scalar terms commute because they act on different physical tensor legs.

Since `Y>=0` and `M_U` is completely positive, the left side of (13) is positive.  Therefore its
operator norm is its largest eigenvalue, and the commuting tensor-sum spectrum gives

\[
 \|\mathcal M_U(Y)\|_\infty
 ={\lambda_{\max}(C^*(R))+\lambda_{\max}(C^*(L))\over m}
 -{\tau\over m^2}.
\tag{14}
\]

No eigenvalue or triangle inequality over a spectral decomposition of `Y` occurs in (13)--(14).

## 4. Orthogonal-sector budget

The matrices

\[
 D,\qquad P-D,\qquad Q-D
\tag{15}
\]

have pairwise disjoint entry supports.  Set

\[
 d:=\|D\|_F^2,
 \qquad x:=\|P-D\|_F,
 \qquad y:=\|Q-D\|_F.
\tag{16}
\]

The normalization in (8) is exactly

\[
 d+x^2+y^2=1.
\tag{17}
\]

All trace lies in `D`.  Since `D` has `m^2` diagonal entries and they are nonnegative,

\[
 {\tau\over m}\le\|D\|_F=\sqrt d.
\tag{18}
\]

Moreover, the off-diagonal part of `R` is obtained by summing the `m` row-coherence blocks of
`P-D`.  Cauchy--Schwarz only in this coefficient label gives

\[
 \|\operatorname{Off}(R)\|_F\le\sqrt m\,x.
\tag{19}
\]

The column version is

\[
 \|\operatorname{Off}(L)\|_F\le\sqrt m\,y.
\tag{20}
\]

The point is that (18)--(20) draw from the single orthogonal budget (17).  They must not be
maximized independently.

## 5. Target-tight theorem, including `tau>A`

On event (4), diagonal coefficient matrices map to their trace times `I/m`, so

\[
 \lambda_{\max}(C^*(R))
 \le {\tau\over m}+\alpha\|\operatorname{Off}(R)\|_F,
\tag{21}
\]

and likewise for `L`.  Combining (14), (19), and (20) gives

\[
 \|\mathcal M_U(Y)\|_\infty
 \le {1\over m}
 \left({\tau\over m}+\alpha\sqrt m(x+y)\right).
\tag{22}
\]

Equations (17)--(18) and `x+y<=sqrt(2(x^2+y^2))` imply

\[
 {\tau\over m}+\alpha\sqrt m(x+y)
 \le \sqrt d+\sqrt{2(A-1)}\sqrt{1-d}
 \le \sqrt{2A-1}.
\tag{23}
\]

The last step is the Euclidean inner-product inequality in two dimensions.  Since `A>=1`,

\[
 \sqrt{2A-1}\le A
\tag{24}
\]

with gap determined exactly by `A^2-(2A-1)=(A-1)^2`.  We have proved

\[
 \boxed{
 Y\succeq0,\quad \|Y\|_F=1,\quad Y\text{ rook-supported},\quad (4)
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y)\|_\infty
 \le {\sqrt{2A-1}\over m}\le {A\over m}.}
\tag{25}
\]

There is no restriction `tau<=A`.  In fact (18) allows `tau` up to `m`, and the proof remains
target-tight throughout that range.  The earlier `sqrt(r)` spectral-summation loss is absent
because the proof never resolves `Y` into positive rank-one terms.

## 6. Explicit full-rank, high-Schmidt examples with trace above `A`

Choose linearly independent Hermitian zero-diagonal matrices `K_1,...,K_m in M_m`, and choose a
nonzero Hermitian zero-diagonal matrix `H`.  Such a family exists for every `m>=2`.  With
`E_(v,v)=|v><v|`, set

\[
 S=\sum_{v=1}^m E_{v,v}\otimes K_v+H\otimes I.
\tag{26}
\]

For

\[
 0<\epsilon<\|S\|_\infty^{-1},
\tag{27}
\]

define

\[
 Y_\epsilon={I+\epsilon S\over\|I+\epsilon S\|_F}.
\tag{28}
\]

Then `Y_epsilon` is positive definite, Hilbert--Schmidt normalized, full rank, and rook-supported.
The first term in (26) has `v=w` coherences and the second has `a=b` coherences, so it belongs to
neither one-leg-diagonal class.  More strongly, its operator-Schmidt rank is `m+1`: the left
factors `E_(1,1),...,E_(m,m),H` are independent, and the corresponding right factors
`I+epsilon K_1,...,I+epsilon K_m,I` are independent because `I` is orthogonal to the span of the
zero-diagonal `K_v`.  Since `Tr(S)=0`,

\[
 \operatorname{Tr}Y_\epsilon
 ={m^2\over
 \sqrt{m^2+\epsilon^2\|S\|_F^2}}.
\tag{29}
\]

Whenever `m>A`, this trace is greater than `A` for all sufficiently small positive `epsilon`.
Thus (25) is not a reformulation of the near-pure trace window from the preceding artifact; it
contains full-rank coefficients whose trace is close to its maximal value `m`.

## 7. A precise obstruction to extending by rook truncation

The natural projection onto rook support is

\[
 \Pi_{\mathrm{rook}}
 :=\Delta_1+\Delta_2-\Delta_1\Delta_2.
\tag{30}
\]

Although both pinchings are completely positive, their inclusion--exclusion combination is not
positive.  Let `e in C^m` be the all-ones unit vector and let

\[
 z=e\otimes e,\qquad Y=|z\rangle\langle z|.
\tag{31}
\]

Writing `J=|e><e|`, direct evaluation gives

\[
\Pi_{\mathrm{rook}}(Y)
 =J\otimes {I\over m}+{I\over m}\otimes J-{I\otimes I\over m^2},
\tag{32}
\]

On `e^perp tensor e^perp`, (32) has eigenvalue

\[
 -{1\over m^2}.
\tag{33}
\]

Thus `Pi_rook(Y)` is indefinite even though `Y` is positive rank one.  Consequently one cannot
extend (25) to arbitrary positive coefficients by declaring the rook part positive and then
controlling the double-off-diagonal remainder with a positive Schur complement.  The proposed
positive decomposition already fails at its first step.

This does not say that every block/Schur-complement refinement fails.  It says precisely that a
refinement based on positivity of the inclusion--exclusion rook truncation is invalid.  A valid
extension must either assume positivity of the retained structured part separately or control the
double-off-diagonal sector jointly with it.

## 8. Suggested atomic nodes (not registered here)

### 8.1 `HEXT.same-tuple-positive-rook-support-base-case`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> On the uniform one-leg trace-zero coefficient event with constant
> `alpha=sqrt((A-1)/m)`, every positive Hilbert--Schmidt unit two-leg coefficient supported on
> pairs sharing at least one coefficient label satisfies
> `||M_U(Y)|| <= sqrt(2A-1)/m <= A/m`.  No restriction on `Tr(Y)` is required.

Equations (13)--(25) are the proof.  The positivity, rook-support condition, and uniform one-leg
event are all load-bearing premises.

### 8.2 `HEXT.same-tuple-rook-truncation-positivity-obstruction`

Suggested role: `obstruction`; suggested level before review: `CONJECTURED`.

Suggested claim:

> The inclusion--exclusion projection onto entries with `v=w` or `a=b` is not a positive map.  It
> sends the projector onto the uniform product coefficient vector to an operator with eigenvalue
> `-1/m^2` on `e^perp tensor e^perp`.  Therefore the positive rook-support theorem cannot be
> extended to arbitrary positive coefficients by a positive rook-part/remainder decomposition.

Equations (30)--(33) give the exact counterexample and scope.

## 9. Status boundary

The class in (25) is a genuinely broader non-rank-one positive class and includes full-rank
examples with `Tr(Y)>A`.  It uses aligned commuting outputs and exact removal of the duplicated
diagonal contribution, not termwise spectral triangle inequality.

The argument does not control positive coefficients with nonzero entries that change both labels,
nor does it prove a stable neighborhood of rook support.  The truncation obstruction prevents a
formal extension by coefficient pinching alone.  No canonical assessment should be promoted from
this note without independent review.
