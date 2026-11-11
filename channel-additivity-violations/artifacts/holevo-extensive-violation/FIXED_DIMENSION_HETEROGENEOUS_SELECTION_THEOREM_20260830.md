# Fixed-dimensional heterogeneous Bell amplification selects one regularized counterexample

Date: 2026-08-30

Status: proposer-side elementary reduction; independent review pending.

All logarithms are base two.

## Statement

Let `X` be a compact metric space and let

\[
 x\longmapsto\Phi_x:M_a\to M_b
\]

be diamond-norm continuous. Define the one-layer conjugate-Bell entropy

\[
 b(x)=S\!\left((\Phi_x\otimes\overline{\Phi_x})(\Omega_a)\right)
\tag{1}
\]

and the regularized one-channel minimum output entropy

\[
 \overline S(x)=\lim_{r\to\infty}\frac1rS_{\min}(\Phi_x^{\otimes r}).
\tag{2}
\]

For an arbitrary sequence `x_1,x_2,...`, put

\[
 L_J=\bigotimes_{j=1}^J\Phi_{x_j}.
\]

The tensor product of the `J` maximally entangled inputs gives a joint output of
`L_J tensor bar(L_J)` with entropy `sum_{j<=J}b(x_j)`. Define the defect certified by this
specific product-Bell input as

\[
 G_J=2S_{\min}(L_J)-\sum_{j=1}^J b(x_j).
\tag{3}
\]

If

\[
 \limsup_{J\to\infty}\frac{G_J}{J}=c>0,
\tag{4}
\]

then there exists one `x_* in X` such that

\[
 2\overline S(x_*)-b(x_*)\ge c.
\tag{5}
\]

Consequently the fixed finite pair `Phi_{x_*},bar(Phi_{x_*})` has positive regularized MOE defect:

\[
 \overline S_{\min}(\Phi_{x_*})
 +\overline S_{\min}(\overline{\Phi_{x_*}})
 -\overline S_{\min}(\Phi_{x_*}\otimes\overline{\Phi_{x_*}})
 \ge c>0.
\tag{6}
\]

Conversely, if one `x_*` satisfies `2 barS(x_*)-b(x_*)>0`, the constant sequence `x_j=x_*`
has a positive limiting certificate rate. Thus, within a compact fixed-dimensional family and
for the product of the layerwise Bell witnesses, heterogeneous extensive amplification is
equivalent to the existence of one fixed regularized counterexample with the stronger Bell upper
certificate.

## Proof

Choose a subsequence `J_l` along which `G_J/J -> c`. Compactness of the probability measures on
`X` gives a further subsequence, not relabeled, whose empirical measures

\[
 \nu_{J_l}=\frac1{J_l}\sum_{j=1}^{J_l}\delta_{x_j}
\]

converge weakly to a probability measure `mu`.

The deterministic heterogeneous-layer theorem in
`IID_LAYER_REGULARIZATION_UPPER_BOUND_20260830.md` gives

\[
 \limsup_{l\to\infty}\frac1{J_l}S_{\min}(L_{J_l})
 \le\int_X\overline S(x)\,d\mu(x).
\tag{7}
\]

The function `b` is continuous by diamond continuity, the product-channel telescoping estimate,
and entropy continuity in fixed output dimension. Hence

\[
 \frac1{J_l}\sum_{j=1}^{J_l}b(x_j)\longrightarrow\int_Xb(x)\,d\mu(x).
\tag{8}
\]

Combining (3)--(4) with (7)--(8) yields

\[
 c\le\int_X\bigl(2\overline S(x)-b(x)\bigr)\,d\mu(x).
\tag{9}
\]

The average in (9) cannot exceed the supremum of its integrand, so some `x_*` satisfies (5).
Conjugation preserves every tensor-power output spectrum, and the Bell input is a valid one-copy
input. Therefore

\[
 \overline S_{\min}(\Phi_{x_*}\otimes\overline{\Phi_{x_*}})
 \le S_{\min}(\Phi_{x_*}\otimes\overline{\Phi_{x_*}})
 \le b(x_*).
\tag{10}
\]

Equations (5) and (10) prove (6).

For the converse, take `L_J=Phi_{x_*}^{tensor J}`. By the definition of the regularized minimum
output entropy,

\[
 \frac1J S_{\min}(L_J)\longrightarrow\overline S(x_*),
\]

while the product Bell output entropy is exactly `J b(x_*)`. Dividing (3) by `J` proves the claimed
positive limit.

## Consequence for the product-Haar route

For fixed input dimension `D` and Kraus count `m`, the space `U(D)^m` is compact and its
random-unitary channels (or complementary channels) depend continuously on the tuple. Therefore
no deterministic, adaptive, oriented, or random choice of infinitely many fixed-`D` layers can
produce a positive product-Bell certificate rate unless at least one fixed finite tuple already
has positive regularized channel/conjugate-channel defect.

This does not prove that such a tuple is impossible. It identifies the exact remaining target and
shows that heterogeneous layer selection cannot postpone it to an easier averaging theorem.
