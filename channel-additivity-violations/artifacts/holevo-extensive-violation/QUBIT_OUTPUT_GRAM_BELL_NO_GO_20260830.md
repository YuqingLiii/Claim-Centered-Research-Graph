# No qubit-output Gram factor can have a conjugate-Bell defect

Date: 2026-08-30

Status: proposer-side finite-dimensional theorem; independent review pending.

All logarithms are base two.

## Theorem

Let `Phi:M_d->M_2` be a finite channel satisfying `Phi(I_d/d)=I_2/2`, and define

\[
 T=\frac2d\Phi\Phi^*,
 \qquad
 Z=(\Phi\otimes\bar\Phi)(\Omega_d).
\tag{1}
\]

Then

\[
 \boxed{
 2\overline S_{\min}(\Phi)
 \le 2S_{\min}(\Phi)
 \le S(Z).}
\tag{2}
\]

Consequently no channel with qubit output can produce a positive fixed-channel
conjugate-Bell regularized defect. Every surviving candidate for this route must have output
dimension at least three.

This theorem concerns the product maximally entangled witness and does not rule out arbitrary
non-Bell collective inputs or unrelated channel pairs.

## 1. Qubit Gram-channel normal form

The Gram channel `T` is bistochastic, Hilbert-Schmidt self-adjoint, and positive semidefinite as a
superoperator. In Bloch form it acts as `1 direct-sum G`, where `G` is a real symmetric positive
semidefinite `3 by 3` matrix. A single qubit unitary conjugation diagonalizes `G`; changing one
eigenvector sign if necessary makes the diagonalizing rotation proper. The entropies in (2) are
unchanged by this output basis change.

Thus assume

\[
 T(I)=I,
 \qquad
 T(\sigma_i)=\lambda_i\sigma_i,
 \qquad
 0\le\lambda_i\le1.
\tag{3}
\]

After permuting axes, write

\[
 t=\lambda_3=\max_i\lambda_i.
\tag{4}
\]

The normalized Choi state of `T`, and hence `Z` up to swap, is Bell diagonal with probabilities

\[
 \begin{aligned}
 p_0&=\frac{1+\lambda_1+\lambda_2+t}{4},
 &p_1&=\frac{1+\lambda_1-\lambda_2-t}{4},\\
 p_2&=\frac{1-\lambda_1+\lambda_2-t}{4},
 &p_3&=\frac{1-\lambda_1-\lambda_2+t}{4}.
 \end{aligned}
\tag{5}
\]

Complete positivity is exactly `p_a>=0`, and

\[
 S(Z)=H(p_0,p_1,p_2,p_3).
\tag{6}
\]

King reviews the equivalent tetrahedral parametrization of unital qubit channels in Section 3 of
the primary source quoted below.

## 2. Every rectangular factor has a low-entropy pure output

Choose an index `i` with `lambda_i=t` and set

\[
 A_i=\Phi^*(\sigma_i)\in M_d.
\tag{7}
\]

Taking the Hilbert-Schmidt inner product of the Gram identity with `sigma_i` gives

\[
 2t=\operatorname{Tr}(\sigma_iT(\sigma_i))
 =\frac2d\operatorname{Tr}(A_i^2).
\tag{8}
\]

Therefore

\[
 \operatorname{Tr}(A_i^2)=dt,
 \qquad
 \|A_i\|_\infty\ge\sqrt t.
\tag{9}
\]

For a unit eigenvector of an eigenvalue with largest absolute value, the corresponding output
qubit has one Bloch coordinate of magnitude at least `sqrt(t)`. Hence

\[
 \boxed{
 S_{\min}(\Phi)
 \le f(t):=h_2\!\left(\frac{1+\sqrt t}{2}\right).}
\tag{10}
\]

It remains to prove a scalar entropy inequality for the Bell probabilities:

\[
 H(p_0,p_1,p_2,p_3)\ge2f(t).
\tag{11}
\]

## 3. Reduction of the scalar inequality to CP-polytope vertices

For fixed `t`, complete positivity and `0<=lambda_1,lambda_2<=t` reduce to

\[
 0\le\lambda_1,\lambda_2\le t,
 \qquad
 |\lambda_1-\lambda_2|\le1-t.
\tag{12}
\]

The remaining inequality `lambda_1+lambda_2<=1+t` is automatic because `t<=1`. Shannon entropy
is concave in `(lambda_1,lambda_2)`, so its minimum over (12) occurs at a vertex.

For `0<=t<=1/2`, the domain is the square with vertex types

\[
 A=(0,0),\qquad B=(t,0),\qquad D=(t,t),
\tag{13}
\]

where the swapped copy of `B` has the same entropy. For `1/2<=t<=1`, the domain is a hexagon
with vertex types

\[
 A=(0,0),\quad
 B=(1-t,0),\quad
 C=(t,2t-1),\quad
 D=(t,t),
\tag{14}
\]

plus their swapped copies.

### 3.1 Depolarizing vertex `D`

At `D`, the channel is the qubit depolarizing channel with Bloch contraction `t`. It is the square
of the depolarizing channel with contraction `sqrt(t)`. King's strong minimum-output-entropy
additivity theorem applied to that square-root channel shows that the Bell-input output entropy
is at least twice its minimum output entropy. This is exactly

\[
 H_D(t)\ge2f(t).
\tag{15}
\]

The probability vector at `D` majorizes the vector at `A`: their two- and three-largest partial
sums agree, while the largest `D` entry is larger. Hence

\[
 H_A(t)\ge H_D(t)\ge2f(t).
\tag{16}
\]

### 3.2 Two-axis vertex `B` for `0<=t<=1/2`

At the low-`t` vertex `B`,

\[
 H_B(t)=\frac32+\frac12h_2\!\left(\frac12+t\right).
\tag{17}
\]

Let `F_B(t)=H_B(t)-2f(t)`. For `0<t<1/2`, direct differentiation gives

\[
 (\ln2)F_B'(t)
 =\frac{\operatorname{artanh}\sqrt t}{\sqrt t}
  -\operatorname{artanh}(2t).
\tag{18}
\]

Put `s=sqrt(t)`. The derivative of the first term in (18) is

\[
 \frac{d}{ds}\frac{\operatorname{artanh}s}{s}
 =\sum_{n\ge1}\frac{2n}{2n+1}s^{2n-1}
 <\frac{s}{1-s^2}\le2s,
\tag{19}
\]

whereas

\[
 \frac{d}{ds}\operatorname{artanh}(2s^2)
 =\frac{4s}{1-4s^4}\ge4s.
\tag{20}
\]

Thus `F_B'` is strictly decreasing, so `F_B` is concave and its minimum is at an endpoint. Now

\[
 F_B(0)=0,
 \qquad
 F_B(1/2)=\frac32-2h_2\!\left(\frac{1+1/\sqrt2}{2}\right)>0.
\tag{21}
\]

For the last inequality use the elementary bound
`h_2(x)<=2sqrt(x(1-x))`, which makes the subtracted term at most `sqrt(2)<3/2`.
For completeness, write `x=(1+u)/2` and
`R(u)=sqrt(1-u^2)-h_2((1+u)/2)`. Its derivative has the sign of

\[
 K(u)-\ln2,
 \qquad
 K(u)=\frac{\operatorname{artanh}(u)\sqrt{1-u^2}}{u}.
\tag{22}
\]

The function `K` decreases strictly from `1` to `0`: differentiating `log K`, negativity reduces
to `artanh(u)>u`. Hence `R` first increases and then decreases, and since `R(0)=R(1)=0`, it is
nonnegative. This proves the entropy bound without an external estimate.

### 3.3 Boundary vertex `C` for `1/2<=t<=1`

At `C`,

\[
 H_C(t)=h_2(t)+1-t.
\tag{23}
\]

The high-`t` vertex `B` has entropy `1+h_2(t)/2`, and

\[
 H_B(t)-H_C(t)=t-\frac12h_2(t)\ge0
\tag{24}
\]

because `h_2(t)<=1<=2t`. It is therefore enough to control `C`.

Let `F_C(t)=H_C(t)-2f(t)` and again put `s=sqrt(t)`. Differentiation gives

\[
 (\ln2)F_C'(t)
 =\ln\!\left(\frac{1-s^2}{2s^2}\right)
  +\frac{\operatorname{artanh}s}{s}.
\tag{25}
\]

The derivative of the right-hand side with respect to `s` is

\[
 -\frac1{s(1-s^2)}-\frac{\operatorname{artanh}s}{s^2}<0.
\tag{26}
\]

Hence `F_C` is concave and is minimized at an endpoint. Equation (21) gives `F_C(1/2)>0`, while

\[
 F_C(1)=0.
\tag{27}
\]

This proves (11) at every vertex and therefore throughout the CP domain.

Primary source used in (15) and for the unital-qubit tetrahedron:

- Christopher King, *Additivity for unital qubit channels*, arXiv:quant-ph/0103156,
  Theorem 1 on page 4 and the standard-form/tetrahedron discussion on pages 11-13.
- Local copy:
  `holevo-extensive-violation/artifacts/primary-sources/king-unital-qubit-additivity-quant-ph-0103156.pdf`
- SHA-256: `0e8b627c523e32c908f30ba6f206c876f7d88bd8a36df7d00ae82fb3e1132b6d`

## 4. Conclusion

Combining (6), (10), and (11) gives

\[
 2S_{\min}(\Phi)\le2f(t)\le S(Z).
\tag{28}
\]

Regularization can only decrease normalized minimum output entropy, so (2) follows.

## Research consequence

The fixed-channel conjugate-Bell search no longer needs to inspect any qubit-output factor,
regardless of its input dimension or Kraus representation. The output dimension must satisfy

\[
 \boxed{k\ge3.}
\tag{29}
\]

The next finite search should therefore start from qutrit-output Hilbert-Schmidt-positive Gram
channels with strict entanglement-cost surplus, then impose the rectangular CP-factor and all-copy
side-entropy gates.
