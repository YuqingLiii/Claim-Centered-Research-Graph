# Same-tuple coefficients: positive partial-trace contraction and polarized subclasses

Date: 2026-08-30

Status: proposer-side exact and conditional lemmas, pending independent review.  Suggested nodes
below should be assessed no higher than `CONJECTURED`.  No canonical YAML is changed, and the
general same-tuple two-leg scalar strong-norm claim remains **OPEN**.

This note continues
[SAME_TUPLE_RANK_ONE_GRAM_CONTRACTION_20260830.md](SAME_TUPLE_RANK_ONE_GRAM_CONTRACTION_20260830.md)
and asks how far its rank-one Gram contraction survives positivity, polarization, spectral
decomposition, and projective-norm summation.

## 1. Setup

For a coefficient `Y in M_(m^2)`, indexed by pairs `(v,a)`, write

\[
 \mathcal M_U(Y)
 ={1\over m^2}\sum_{v,a,w,b}Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b).
\tag{1}
\]

The one-leg map is

\[
 C^*(X)={1\over m}\sum_{a,b}X_{a,b}U_a^*U_b.
\tag{2}
\]

For `||Y||_2=1`, the target remains

\[
 \|\mathcal M_U(Y)\|_\infty\le {A\over m},
 \qquad
 A=1+{9(1+\eta)^2\over m}.
\tag{3}
\]

## 2. Exact positive partial-trace contraction

Let `Y>=0` and define its two coefficient partial traces

\[
 R:=\operatorname{Tr}_1Y,
 \qquad R_{a,b}=\sum_vY_{(v,a),(v,b)},
\tag{4}
\]

and

\[
 L:=\operatorname{Tr}_2Y,
 \qquad L_{v,w}=\sum_aY_{(v,a),(w,a)}.
\tag{5}
\]

Both are positive and have common trace

\[
 \tau:=\operatorname{Tr}Y=\operatorname{Tr}R=\operatorname{Tr}L.
\tag{6}
\]

Then the rank-one Gram argument extends to the following operator-order statement:

\[
 \boxed{
 0\preceq\mathcal M_U(Y)\preceq I\otimes C^*(R),
 \qquad
 0\preceq\mathcal M_U(Y)\preceq C^*(L)\otimes I.}
\tag{7}
\]

Consequently

\[
 \boxed{
 \|\mathcal M_U(Y)\|_\infty
 \le\min\{\|C^*(R)\|_\infty,\|C^*(L)\|_\infty\}.}
\tag{8}
\]

### Proof

Take a spectral decomposition

\[
 Y=\sum_k\lambda_k|z_k\rangle\langle z_k|,
 \qquad \lambda_k\ge0,
\tag{9}
\]

and let `Z_k=((z_k)_(v,a))`.  Set

\[
 B_{v,k}=\sqrt{\lambda_k}\sum_a\overline{(z_k)_{v,a}}U_a,
 \qquad
 T_k=\sum_vU_v\otimes B_{v,k}.
\tag{10}
\]

The rank-one factorization gives

\[
 \mathcal M_U(Y)={1\over m^2}\sum_kT_k^*T_k.
\tag{11}
\]

For each `k`, matrix Cauchy--Schwarz yields

\[
 T_k^*T_k\preceq m I\otimes\sum_vB_{v,k}^*B_{v,k}.
\tag{12}
\]

After summing in `k`, the square function is exactly

\[
 \sum_{k,v}B_{v,k}^*B_{v,k}
 =\sum_{a,b}R_{a,b}U_a^*U_b=mC^*(R).
\tag{13}
\]

Equations (11)--(13) give the first inequality in (7).  Grouping instead by `a` gives the second
one with `L`.  Positivity of `C^*(R)` and `C^*(L)` also follows directly from the square-function
representations.  Taking norms proves (8).

For rank-one `Y=|z><z|`, equations (4)--(5) reduce to
`R=overline(Z^*Z)` and `L=ZZ^*`, so (8) exactly recovers the preceding Gram lemma.

## 3. New positive target-tight subclasses

### 3.1 Diagonal partial trace with small spectral trace

If either `R` or `L` is diagonal, then

\[
 C^*(R)={\operatorname{Tr}R\over m}I={\tau\over m}I
\tag{14}
\]

or the analogous identity for `L`.  Hence

\[
 \boxed{
 R\text{ or }L\text{ diagonal},\quad \tau\le A
 \quad\Longrightarrow\quad
 \|\mathcal M_U(Y)\|_\infty\le {A\over m}.}
\tag{15}
\]

This is deterministic.  It contains genuinely non-rank-one positive matrices, although the trace
window is narrow because a positive Hilbert--Schmidt-normalized coefficient obeys

\[
 1\le\tau\le\sqrt{\operatorname{rank}Y}.
\tag{16}
\]

### 3.2 Near-diagonal positive partial traces

Let

\[
 \alpha:=\sqrt{{A-1\over m}}={3(1+\eta)\over m}.
\tag{17}
\]

On the uniform one-leg trace-zero event

\[
 \|C^*(X_0)\|_\infty\le\alpha\|X_0\|_F,
 \qquad \operatorname{Tr}X_0=0,
\tag{18}
\]

the diagonal part of a positive partial trace contributes exactly `tau I/m`, while its
off-diagonal part has trace zero.  Thus

\[
 \|\mathcal M_U(Y)\|_\infty
 \le {\tau\over m}
 +\alpha\min\{\|\operatorname{Off}(R)\|_F,
                    \|\operatorname{Off}(L)\|_F\}.
\tag{19}
\]

The target follows whenever

\[
 \boxed{
 \tau\le A,\qquad
 \min\{\|\operatorname{Off}(R)\|_F,
        \|\operatorname{Off}(L)\|_F\}
 \le {A-\tau\over\sqrt{m(A-1)}}
 ={A-\tau\over3(1+\eta)}.}
\tag{20}
\]

This condition is simultaneous over all positive `Y` on event (18); no positive-coefficient net
is introduced.

Deterministically, the entrywise estimate gives the alternative sufficient condition

\[
 \boxed{
 \tau+\min\{\|\operatorname{Off}(R)\|_{\ell_1},
             \|\operatorname{Off}(L)\|_{\ell_1}\}
 \le A.}
\tag{21}
\]

### 3.3 An explicit dense positive rank-two family

Choose two Hilbert--Schmidt-orthogonal unitaries `V_1,V_2 in U(m)` and let

\[
 z_j\leftrightarrow Z_j={V_j\over\sqrt m}.
\tag{22}
\]

The coefficient vectors `z_1,z_2` are orthonormal, dense when the `V_j` are dense, and each is
maximally entangled.  For `epsilon>0`, set

\[
 s_1={1\over\sqrt{1+\epsilon^2}},
 \qquad
 s_2={\epsilon\over\sqrt{1+\epsilon^2}},
 \qquad
 Y=s_1|z_1\rangle\langle z_1|+s_2|z_2\rangle\langle z_2|.
\tag{23}
\]

Then `Y>=0`, `rank Y=2`, and `||Y||_2=1`.  Both partial traces are

\[
 R=L={s_1+s_2\over m}I,
\tag{24}
\]

so (15) proves the target whenever

\[
 {1+\epsilon\over\sqrt{1+\epsilon^2}}\le A.
\tag{25}
\]

This is a concrete dense, non-rank-one, positive same-tuple base case.  Its allowed second
eigenvalue is `O(A-1)=O(1/m)`; it does not represent a uniform rank-two theorem.

## 4. Polarization without the four-term loss

For arbitrary unit coefficient vectors `z,w`, direct factorization is sharper than the usual
four-term polarization identity:

\[
 \mathcal M_U(|z\rangle\langle w|)
 ={1\over m^2}T_z^*T_w.
\tag{26}
\]

Define the rank-one Gram certificate value

\[
 g_U(z):=\min\left\{
 \|C^*(\overline{Z^*Z})\|_\infty,
 \|C^*(ZZ^*)\|_\infty
 \right\}.
\tag{27}
\]

The exact Gram contraction gives `||T_z||^2/m^2<=g_U(z)`, and therefore

\[
 \boxed{
 \|\mathcal M_U(|z\rangle\langle w|)\|_\infty
 \le\sqrt{g_U(z)g_U(w)}.}
\tag{28}
\]

This avoids the numerical factor from writing a cross term as four positive rank-one terms.  It
does not avoid summing singular components.

Let

\[
 Y=\sum_k s_k|z_k\rangle\langle w_k|
\tag{29}
\]

be a singular-value decomposition.  Equation (28) yields

\[
 \boxed{
 \|\mathcal M_U(Y)\|_\infty
 \le\sum_ks_k\sqrt{g_U(z_k)g_U(w_k)}.}
\tag{30}
\]

In particular, if every left and right singular vector has a diagonal left or right coefficient
Gram, then `g_U<=1/m` deterministically and

\[
 \|\mathcal M_U(Y)\|_\infty\le {\|Y\|_1\over m}.
\tag{31}
\]

Thus a further target-tight subclass is

\[
 \boxed{
 \|Y\|_2=1,\quad \|Y\|_1\le A,\quad
 \text{all singular vectors Gram-diagonal}
 \quad\Longrightarrow\quad (3).}
\tag{32}
\]

Here `||Y||_1` is the spectral nuclear norm of the `m^2 by m^2` coefficient matrix, not the
entrywise norm and not the operator-Schmidt projective norm.  Positive example (23) is the
self-adjoint specialization of (32).

## 5. Exact obstruction to pure spectral norm summation

Suppose only that every normalized eigenvector in (9) has the sharp rank-one bound `1/m`.
Positivity and the triangle inequality give

\[
 \|\mathcal M_U(Y)\|_\infty
 \le{1\over m}\sum_k\lambda_k
 ={\operatorname{Tr}Y\over m}.
\tag{33}
\]

For `||Y||_2=1`, an equal-weight positive rank-`r` coefficient has `TrY=sqrt(r)`.  Already at
`r=2`, (33) is `sqrt(2)/m`, while `A/m` tends to `1/m` as `m` grows.  Hence **rank-one sharp bounds
plus spectral summation cannot prove a uniform positive rank-two theorem**.  It succeeds only in
the near-pure trace window `TrY<=A` or when additional output geometry improves the sum.

Coefficient-space orthogonality does not supply that geometry.  Distinct coordinate vectors
`e_i,e_j in C^(m^2)` are orthogonal, but

\[
 \mathcal M_U(|e_i\rangle\langle e_i|)
 =\mathcal M_U(|e_j\rangle\langle e_j|)
 ={1\over m^2}I.
\tag{34}
\]

Thus orthogonal coefficient eigenvectors can have perfectly aligned positive outputs.  Equation
(34) does not refute the target--these particular outputs are smaller by another factor `m`--but
it decisively refutes the inference “orthogonal eigenvectors imply orthogonal output supports.”

## 6. Where block Cauchy--Schwarz loses information

The partial-trace contraction (7) is exact as an inequality but can be far from the exact map.
For a fully diagonal positive coefficient, the earlier base-case identity is

\[
 \mathcal M_U(Y)={\tau\over m^2}I.
\tag{35}
\]

In contrast, (7) sees only the diagonal partial trace and gives `tau/m`.  It loses a full factor
`m`.  Therefore (7) should be used for coherent dense coefficients, where its square function is
informative; it must not replace the exact diagonal and one-leg-diagonal formulas.

More generally, matrix Cauchy--Schwarz discards all cross-`v` cancellation in

\[
 \left(\sum_vU_v\otimes B_v\right)^*
 \left(\sum_wU_w\otimes B_w\right).
\tag{36}
\]

The remaining square function remembers only a coefficient partial trace.  If `TrY>A`, its
diagonal contribution is already `tau/m` in this upper bound, so no off-diagonal Frobenius estimate
can recover the target.  This is a no-go for the unrefined block-Cauchy route, not for the original
same-tuple inequality.

## 7. Projective/operator-Schmidt summation has the same obstruction

For an operator-Schmidt decomposition across the two coefficient legs,

\[
 Y=\sum_st_sY_{1,s}\otimes Y_{2,s},
 \qquad \|Y_{1,s}\|_2=\|Y_{2,s}\|_2=1,
\tag{37}
\]

the existing simple-tensor bound gives

\[
 \|\mathcal M_U(Y)\|_\infty
 \le {A\over m}\sum_s|t_s|.
\tag{38}
\]

For `||Y||_2=1`, `sum|t_s|>=1`, with equality exactly at operator-Schmidt rank one.  Therefore the
condition needed to retain the target from (38), namely `sum|t_s|<=1`, does not enlarge the
normalized simple-tensor class.  Positivity does not change this nuclear-versus-Hilbert norm fact.

An actual enlargement is possible only when each summand has a sharper constant such as `1/m`,
leaving the small nuclear-norm window up to `A`; equation (32) is one such spectral, rather than
operator-Schmidt, realization.  Any claimed larger projective class must state where this unused
constant comes from.

## 8. Suggested atomic nodes (not registered here)

### 8.1 `HEXT.same-tuple-positive-partial-trace-contraction`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> For every deterministic unitary tuple and positive coefficient `Y`, the same-tuple output obeys
> `0 <= M_U(Y) <= I tensor C^*(Tr_1 Y)` and
> `0 <= M_U(Y) <= C^*(Tr_2 Y) tensor I`.  Hence its norm is at most the smaller one-leg
> partial-trace norm.

This is a route-free direct algebraic node supported by equations (7)--(13).

### 8.2 `HEXT.same-tuple-near-diagonal-positive-base-case`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> On the uniform one-leg trace-zero coefficient event, a positive unit-Hilbert--Schmidt
> coefficient with trace `tau<=A` satisfies the two-leg target whenever one coefficient partial
> trace has off-diagonal Frobenius norm at most
> `(A-tau)/sqrt(m(A-1))`.  Deterministically, `tau` plus the smaller off-diagonal entrywise norm at
> most `A` is sufficient.

The one-leg event must be recorded as a premise or exact established interface.  The trace
restriction is load-bearing.

### 8.3 `HEXT.same-tuple-gram-safe-spectral-nuclear-base-case`

Suggested role: `proof`; suggested level before review: `CONJECTURED`.

Suggested claim:

> If every left and right singular vector of a unit-Hilbert--Schmidt coefficient has diagonal
> left or right coefficient Gram and the spectral nuclear norm of the coefficient is at most `A`,
> then the same-tuple target holds deterministically.  This includes explicit dense positive
> rank-two coefficients with a sufficiently small second eigenvalue.

Equations (26)--(32) are the proof.  This node must not be phrased as a general rank-two theorem.

### 8.4 `HEXT.same-tuple-positive-summation-obstruction`

Suggested role: `obstruction`; suggested level before review: `CONJECTURED`.

Suggested claim:

> Combining target-sharp rank-one estimates only by positivity, spectral triangle inequality, or
> unrefined block matrix Cauchy--Schwarz yields a trace/nuclear-norm factor.  On the
> Hilbert--Schmidt unit sphere this factor is `sqrt(r)` for equal-weight positive rank `r`, so the
> route cannot prove a uniform rank-two target as `A` tends to one.  This refutes only the stated
> summation route, not the positive rank-two claim itself.

Equations (33)--(38) give the exact scope and the output-alignment warning.

## 9. Status boundary

The positive partial-trace inequality is a genuine extension of the rank-one Gram contraction,
and equations (23)--(25) give a concrete dense non-rank-one positive subclass.  Polarization also
extends the sharp Gram-safe bound to a small spectral nuclear-norm neighborhood of rank one.

None of these results controls arbitrary positive rank two, arbitrary positive `Y`, arbitrary
Hermitian `Y`, or a general operator-Schmidt/projective class.  The trace/nuclear factor is not a
bookkeeping artifact: it is the exact loss incurred by norm summation without additional output
orthogonality or cancellation.  No canonical assessment should be promoted from this note alone.
