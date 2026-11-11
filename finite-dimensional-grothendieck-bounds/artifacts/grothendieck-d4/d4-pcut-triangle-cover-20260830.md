# Exact triangle-cover certificate for the 217-variable p-cut gate

**Status.**  Complete exact proof for the whole archived fixed-support
\(217+83\) cell.  This closes the Boolean p-cut gate left open by
`d4-superlevel-cell-reduction-20260830.md`.  It does **not** yet prove
the global classical upper bound, because a competitor may change which 217
coordinates belong to \(\operatorname{supp}p\).

The proof certificate is replayed by

```text
grothendieck-d4/tools/h4_pcut_triangle_cover_checker.py
```

The frozen certificate is

```text
d4-pcut-triangle-cover-certificate-20260830.npz
```

with SHA-256

```text
fe1444390cc921aae3e1fb40b3389fc9ae94d1ae77fee83813f9198c06f7f504
```

The checker does not invoke an optimizer.  It reconstructs all inequalities
from the frozen H4 instance and verifies the certificate using Python
integers (and an exact rational LDL factorization for the q block).

## 1. Frozen objective map

For the archived signs \(x,y\in\{\pm1\}^{300}\), put

\[
 p=\frac{x+y}{2},\qquad q=\frac{x-y}{2}.
\]

Their supports are complementary and have sizes 217 and 83.  The exact
values are

\[
 p^TAp=1755221923705373102,
\]

\[
 q^TAq=-325822229381978298,
\]

and therefore

\[
 C=p^TAp-q^TAq=2081044153087351400.
\]

Let \(P=\operatorname{supp}p\), listed in increasing ambient-coordinate
order, and gauge the principal matrix by the archived p signs:

\[
 M=\operatorname{diag}(p_P)A_{PP}\operatorname{diag}(p_P).
\]

The canonical byte encoding consisting of the 217 ambient support indices,
the 217 archived signs, and the lexicographic upper triangle of \(M\) has
SHA-256

```text
5049871cbbb88448752b893e2157cef7377993c91215d4d99e7bc0467e9f4adf
```

This freezes both the Boolean variables and their exact objective map.

## 2. The p problem is a weighted cut inequality

For a competing p sign vector, let \(z_i\in\{0,1\}\) record whether the
archived sign at vertex \(i\in P\) is flipped, and put

\[
 y_{ij}=z_i\mathbin{\mathsf{xor}}z_j.
\]

Then the exact loss from the archived p value is

\[
 p^TAp-p'^TAp'=4\sum_{i<j}M_{ij}y_{ij}.                 \tag{2.1}
\]

Thus the missing gate is exactly

\[
 \sum_{i<j}M_{ij}y_{ij}\ge 0
 \quad\text{for every cut of }K_{217}.                  \tag{2.2}
\]

Among the 23,436 edges, 6,294 have negative weight, 15,066 have positive
weight, and 2,076 have zero weight.  The real Laplacian is indefinite, so
(2.2) cannot follow from an ordinary PSD argument.

## 3. Homogeneous triangle generators

For distinct \(i,j,k\), every cut semimetric satisfies

\[
 T_{ijk}(y)=y_{ik}+y_{jk}-y_{ij}\in\{0,2\}.             \tag{3.1}
\]

For each negative edge \(ij\), we retain triangles whose two legs \(ik\)
and \(jk\) have positive M-weight.  The exact stabilizer of the archived
pair \((p,q)\) inside the certified signed H4 action has order six.  After
quotienting by this stabilizer there are 80,819 admissible triangle orbits.

The frozen certificate supplies nonnegative **integer** multipliers
\(\lambda_\mathcal O\) for 26,627 of these orbits.  Expanding the selected
orbits gives 158,829 individual homogeneous triangle inequalities.  The
largest multiplier is

\[
 184955919316291.
\]

The checker reconstructs the following coefficient identity edge by edge:

\[
 \boxed{
 M\cdot y
 =\sum_e r_e y_e+
   \sum_{\mathcal O}\lambda_\mathcal O
       \sum_{(i,j,k)\in\mathcal O}T_{ijk}(y),
 }
                                                               \tag{3.2}
\]

where every \(r_e\) is an exact nonnegative integer.  The minimum residual
is exactly zero.  Equation (3.1) and \(y_e\ge0\) now prove (2.2) for all
\(2^{217}\) sign assignments, without enumeration or floating-point
tolerance:

\[
 \boxed{p'^TAp'\le p^TAp.}                              \tag{3.3}
\]

The graph formed by the 18,732 edges with \(r_e>0\) is connected.  Hence
equality in (3.2) forces every such edge to be uncut, so equality in (3.3)
occurs only at \(p'=p\) and \(p'=-p\).

## 4. Combination with the exact q SOS

The replay checker independently reconstructs the q-block result rather
than importing it as an assumption.  If

\[
 N=\operatorname{diag}(q_Q)A_{QQ}\operatorname{diag}(q_Q),
 \qquad L_Q=\operatorname{diag}(N\mathbf1)-N,
\]

then an exact rational LDL decomposition of a grounded 82 by 82 minor
proves

\[
 -L_Q\succeq0,
 \qquad
 q'^TAq'\ge q^TAq                                      \tag{4.1}
\]

for every one of the \(2^{83}\) sign assignments on the fixed q support.
Its equality cases are \(q'=q\) and \(q'=-q\).

Combining (3.3) and (4.1) gives the fixed-cell theorem

\[
 \boxed{
 p'^TAp'-q'^TAq'\le
 p^TAp-q^TAq=C
 }
                                                               \tag{4.2}
\]

for all \(2^{217+83}=2^{300}\) choices of signs with the archived
complementary support split.  Equality is possible only for the four
independent global sign choices

\[
 (p',q')\in\{(\pm p,\pm q)\}.
\]

## 5. Discovery versus proof

`d4-pcut-triangle-cover-discovery.py` records the symmetry-reduced LP/MILP
used to find the multipliers.  A direct 217-variable Boolean MILP did not
produce a useful global bound within its time limit, and that run is not
evidence used by the theorem.  The proof object is only the frozen integer
multiplier vector plus the exact replay above.

## 6. Remaining global gate

The archived support cell is now completely closed.  Any counterexample to
the proposed global classical bound must change the complementary support
split, equivalently it must move at least one coordinate between p and q.
The next proof target is therefore a support-changing inequality, not a
better optimizer on the 217-variable sign cell.
