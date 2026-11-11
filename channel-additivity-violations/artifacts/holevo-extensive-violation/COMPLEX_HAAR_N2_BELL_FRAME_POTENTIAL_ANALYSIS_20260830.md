# Complex-Haar two-copy Bell frame potential: exact one-layer mean

Date: 2026-08-30

Status: proposer-side calculation for the **maximally entangled input only**, for one finite
one-layer tuple.  No canonical YAML is changed.  This note neither proves nor disproves the
global `n=2` physical-output inequality.

All logarithms are base two unless `ln` is written explicitly.

## 1. Result

Let `U_1,...,U_m` be independent Haar unitaries in `U(d)`, with `d>=2`.  For the one-layer
random-unitary channel and its complement, define

\[
 |\phi_{v,a}\rangle=(U_v\otimes U_a)|\Omega_d\rangle
 =d^{-1/2}\operatorname{vec}(U_vU_a^T)
\tag{1}
\]

and the frame potential

\[
 F(U)=\sum_{v,a,w,b=1}^m
 \left|\frac1d\operatorname{Tr}\!\left[
   (U_vU_a^T)^*(U_wU_b^T)\right]\right|^2.
\tag{2}
\]

The Bell-input output purity is exactly

\[
 P_{\rm Bell}(U)
 :=\operatorname{Tr}[(L\otimes L)(\Omega_d)^2]
 =\operatorname{Tr}[(C\otimes C)(\Omega_d)^2]
 =\frac{F(U)}{m^4}.
\tag{3}
\]

The exact Haar expectation is

\[
 \boxed{
 \mathbb E F
 =m^2+\frac{m^4-m^2}{d^2}
   +\frac{2m(m-1)}{d(d+1)}.}
\tag{4}
\]

Equivalently, put

\[
 \delta_{m,d}
 =\frac{m^2-1}{d^2}
  +\frac{2(m-1)}{m d(d+1)}.
\tag{5}
\]

Then

\[
 \boxed{\mathbb E P_{\rm Bell}
 =\frac{1+\delta_{m,d}}{m^2}.}
\tag{6}
\]

For the one-layer target in
`HEXT.product-haar-physical-self-purity-multiplicativity`, write

\[
 c=(1+\eta)^2,\qquad A=1+\frac{9c}{m}.
\tag{7}
\]

The Bell test asks for `F<=A^2m^2`.  Since the `m^2` diagonal Gram terms are deterministically
one, `F-m^2>=0`; Markov's inequality applied only to this excess gives the rigorous tail bound

\[
 \boxed{
 \Pr\{F>A^2m^2\}
 \le \min\!\left\{1,\frac{\delta_{m,d}}{A^2-1}\right\}
 \le \min\!\left\{1,
   \frac{m(m^2+1)}{18c\,d^2}\right\}.}
\tag{8}
\]

Thus for every fixed `m,eta`, a complex product-Haar one-layer tuple passes the Bell test with
probability tending to one as `d->infinity`.  A sufficient dimension for Bell-failure probability
at most `epsilon` is

\[
 d^2\ge \frac{m(m^2+1)}{18c\,\epsilon}.
\tag{9}
\]

This is a Bell-input statement only.  It gives no upper bound on the supremum over all entangled
two-copy inputs.

## 2. Index form and Weingarten interface

Put

\[
 X_{v,a;w,b}
 =\frac1d\operatorname{Tr}\!\left[
  (U_vU_a^T)^*(U_wU_b^T)\right].
\tag{10}
\]

Writing out the trace gives

\[
 dX_{v,a;w,b}
 =\sum_{i,j,k,l=1}^d
 \overline{(U_a)_{ij}}\,
 \overline{(U_v)_{kj}}\,
 (U_w)_{kl}(U_b)_{il}.
\tag{11}
\]

For each distinct label among `v,a,w,b`, the product of (11) with its conjugate has the same
number `p` of `U` and `bar U` entries, where `1<=p<=4`.  Independence lets one integrate each
label separately.  The unitary Weingarten formula used for each label is

\[
 \mathbb E\!\left[
  \prod_{r=1}^p U_{x_r y_r}
  \prod_{s=1}^p \overline{U_{x'_s y'_s}}
 \right]
 =\sum_{\sigma,\tau\in S_p}
  \prod_{r=1}^p
  \delta_{x_r,x'_{\sigma(r)}}
  \delta_{y_r,y'_{\tau(r)}}
  \operatorname{Wg}_d(\sigma^{-1}\tau).
\tag{12}
\]

Contracting the row and column deltas in (12) gives the complete equality-pattern table below.
Only Haar moments of order at most four occur.  The final values simplify to second-moment-sized
expressions even for the patterns with a label appearing three or four times.

## 3. Complete equality-pattern classification

In the table, for example, `va|wb` means `v=a`, `w=b`, and the two displayed blocks have distinct
labels.  `(m)_r=m(m-1)...(m-r+1)` is the number of assignments of `r` distinct labels.

| exact label partition | number of quadruples | `E |X_{v,a;w,b}|^2` |
|---|---:|---:|
| `vawb` | `(m)_1` | `1` |
| `vaw|b` | `(m)_2` | `1/d^2` |
| `vab|w` | `(m)_2` | `1/d^2` |
| `va|wb` | `(m)_2` | `2/[d(d+1)]` |
| `va|w|b` | `(m)_3` | `1/d^2` |
| `vwb|a` | `(m)_2` | `1/d^2` |
| `vw|ab` | `(m)_2` | `1` |
| `vw|a|b` | `(m)_3` | `1/d^2` |
| `vb|aw` | `(m)_2` | `2/d^2` |
| `v|awb` | `(m)_2` | `1/d^2` |
| `v|aw|b` | `(m)_3` | `1/d^2` |
| `vb|a|w` | `(m)_3` | `1/d^2` |
| `v|ab|w` | `(m)_3` | `1/d^2` |
| `v|a|wb` | `(m)_3` | `1/d^2` |
| `v|a|w|b` | `(m)_4` | `1/d^2` |

These 15 disjoint rows contain all `m^4` ordered quadruples.  They can be consolidated into four
classes:

1. **Identical frame labels.**  If `v=w` and `a=b`, then `X=1`.  This includes `m` all-equal
   quadruples and `m(m-1)` instances of `vw|ab`, hence exactly `m^2` deterministic terms.
2. **Complex-symmetric diagonal family.**  The `m(m-1)` instances `va|wb` have expectation
   `2/[d(d+1)]`.
3. **Transpose-exchange family.**  The `m(m-1)` instances `vb|aw` have expectation `2/d^2`.
4. **Background.**  The remaining
   `m^4-3m^2+2m` quadruples each have expectation `1/d^2`.

For every background row, one may condition on all but one Haar variable and cyclically move the
fixed unitary factors through the trace.  The remaining matrix inside the trace is Haar, so
`d X` has the distribution of `Tr R` for a Haar `R`; hence `E|dX|^2=1`.  Thus the background
entries do not require an independence assumption between the two frame vectors.  This
conditioning argument also verifies the rows containing a triple-repeated label, where such an
assumption would be false.

Summing these four classes gives

\[
 \begin{aligned}
 \mathbb EF
 &=m^2
 +\frac{2m(m-1)}{d(d+1)}
 +\frac{2m(m-1)}{d^2}
 +\frac{m^4-3m^2+2m}{d^2}\\
 &=m^2+\frac{m^4-m^2}{d^2}
 +\frac{2m(m-1)}{d(d+1)},
 \end{aligned}
\tag{13}
\]

which proves (4).

## 4. Two exceptional contractions in elementary form

The two nontrivial exceptional values can also be checked without the full 15-row contraction.

### 4.1 The `va|wb` family

Let `v=a`, `w=b`, and `v!=w`.  With `R=U_v^*U_w`, Haar invariance gives a Haar unitary `R` and

\[
 dX_{v,v;w,w}
 =\operatorname{Tr}(RR^T).
\tag{14}
\]

The unitary second moment yields

\[
 \mathbb E|\operatorname{Tr}(RR^T)|^2=\frac{2d}{d+1},
\qquad
 \mathbb E|X_{v,v;w,w}|^2=\frac{2}{d(d+1)}.
\tag{15}
\]

For real orthogonal matrices, all the vectors `phi_{v,v}` coincide and these same
`m(m-1)` off-diagonal terms equal one.  Equation (15) is the precise way in which that real Bell
collision disappears in the complex-Haar model.

### 4.2 The `vb|aw` family

Let `v=b`, `a=w`, and `v!=a`.  With `R=U_v^*U_a`,

\[
 dX_{v,a;a,v}=\operatorname{Tr}(\overline R R).
\tag{16}
\]

The same unitary second moment gives

\[
 \mathbb E|\operatorname{Tr}(\overline R R)|^2=2,
\qquad
 \mathbb E|X_{v,a;a,v}|^2=\frac2{d^2}.
\tag{17}
\]

This transpose-exchange symmetry only doubles the `1/d^2` background moment.  It is not a
dimension-free collision.

## 5. Dominant terms and dimension scale

The deterministic `m^2` Gram diagonal gives the ideal baseline purity `1/m^2`.  For large `m,d`,
the correction classes scale as follows:

| class | total contribution to `E F` |
|---|---:|
| generic background | `m^4/d^2+O(m^2/d^2)` |
| complex-symmetric diagonal family | `2m^2/d^2+o(m^2/d^2)` |
| transpose-exchange family | `2m^2/d^2+O(m/d^2)` |

Thus the background, not a structured collision, is the leading correction when `m` is large.
The normalized relative excess is

\[
 \delta_{m,d}=\frac{m^2}{d^2}
 +O\!\left(\frac1{d^2}\right).
\tag{18}
\]

Meanwhile

\[
 A^2-1
 =\frac{18c}{m}+\frac{81c^2}{m^2}.
\tag{19}
\]

The mean transition therefore lies at

\[
 d\asymp \frac{m^{3/2}}{\sqrt{18c}}.
\tag{20}
\]

More rigorously:

- `E P_Bell<=A^2/m^2` holds exactly iff `delta_{m,d}<=A^2-1`.
- The simpler sufficient condition

  \[
   d^2\ge\frac{m^2+1}{A^2-1}
  \tag{21}
  \]

  guarantees mean safety.
- Conversely, if

  \[
   d^2<\frac{m^2-1}{A^2-1},
  \tag{22}
  \]

  then `delta_{m,d}>A^2-1`, so the Haar mean exceeds the Bell threshold.  Hence a set of positive
  Haar measure violates the Bell test.  Provided `A<m` (automatic in the intended `ln m>18`
  regime when `eta` is fixed, and in particular when it is chosen small), `F<=m^4` also gives

  \[
   \Pr\{F>A^2m^2\}
   \ge
   \frac{\delta_{m,d}-(A^2-1)}{m^2-A^2}>0.
  \tag{23}
  \]

Equation (23) is only an existence/positive-measure failure direction; it is not a high-probability
failure theorem.  No variance estimate is needed for the high-dimensional safety direction (8),
because the off-diagonal frame-potential excess is nonnegative.

## 6. Compatibility with the finite one-copy event

The finite absolute-unbounded construction fixes `m` first and then sends `d->infinity`.  In this
quantifier order, (8) shows that Bell failure has probability tending to zero.  The one-copy strong
coefficient event also has probability tending to one in the same fixed-`m` limit.  A union bound
therefore gives finite tuples that satisfy both the one-copy event and this Bell-input test.

This observation is deliberately narrow:

1. It is unconditional in the Haar tuple before the union bound; it does not claim an exact
   conditional distribution given the one-copy success event.
2. Passing the Bell test controls only the single state `Omega_d`.
3. The global `n=2` target still requires the physical Gram inequality for every entangled input,
   equivalently the centered state-dependent inequality isolated in
   `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md`.
4. No conclusion for `n>=3`, regularized minimum output entropy, or full-size extensive violation
   follows from (4)--(9).

## 7. Reproducibility and theorem interface

The table can be reproduced without simulation: insert the row/column indices from (11) into
(12), independently for every equality block of `v,a,w,b`, and count the remaining free indices.
For a block of size `p`, at most `(p!)^2` Weingarten contractions occur; the worst all-equal row
has `p=4`, hence only 576 symbolic contractions before simplification.  More economically, Haar
invariance reduces every background row to `Tr R`, and only the two exceptional families require
the unitary second moment.  No large-dimensional matrix is formed.

The external interface is exactly the unitary Haar integration formula (12).  It supplies the
mean and the Markov tail (8), but it does not optimize over physical input states.  In particular,
neither arbitrary cb coefficients nor an SDP relaxation enter this Bell calculation.

## Primary source and repository interfaces

1. Benoit Collins and Piotr Sniady, *Integration with respect to the Haar measure on unitary,
   orthogonal and symplectic group*, arXiv:math-ph/0402073, unitary Weingarten formula.
2. `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md`, especially equations (17),
   (28), and (43) there.
3. `FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`, fixed-`m` then `d->infinity`
   quantifier order.
