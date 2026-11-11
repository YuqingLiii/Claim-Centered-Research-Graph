# Exact instance, rank-four Gram witness, and measurements

This note freezes and proves the locally closed part of the 300 by 300 H4
candidate.  It deliberately does **not** claim the unresolved classical upper
bound.  Indices below run from 0 to 299.

## D4-T1. Frozen Bell instance

Let `A` be the integer matrix stored in
`frozen-instance/d4_n1_300x300.mat`.  Its containing MAT-file has MD5

```text
b5223ca2fd5c4cbe52e93a23a4570b9f
```

and the canonical row-major signed-little-endian int64 serialization of `A`
has SHA-256

```text
5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5
```

The exact checker verifies that `A` is symmetric, integral, and 300 by 300.
The same archive contains two vectors `ax,by` whose entries are exactly
`+1` or `-1`.

## D4-T2. Exact reconstruction of the Gram matrix

For a nonzero integer `a`, write `sgn(a)` for its sign.  Define

\[
 P_{ij}=\operatorname{sgn}(A_{ij})q_{|A_{ij}|}
\]

when `A_ij` is nonzero, and use the displayed value directly when it is zero.
The exact level table is as follows.  The diagonal level uses the same rule:
both `A_ii` and its normalized value are negative, so `P_ii=1`.

| `|A_ij|` | `q` |
|---:|---:|
| 0 | 0 |
| 10293655277252 | 3/4 |
| 21631568804130 | (-1+sqrt(5))/8 |
| 27105449085782 | (1+3sqrt(5))/8 |
| 37229688645756 | (1+sqrt(5))/4 |
| 39431279593850 | (-5-sqrt(5))/8 |
| 51957372508648 | (-1+3sqrt(5))/8 |
| 58783195593460 | 1/4 |
| 68008930961612 | -1 |
| 72718584681592 | (3+sqrt(5))/8 |
| 77136371015016 | (3-sqrt(5))/8 |
| 101154567432113 | sqrt(5)/4 |
| 124502011454782 | 1/2 |
| 129160051828973 | (1+sqrt(5))/8 |
| 159311771904990 | 1/4 |
| 165039882863956 | 1/2 |
| 176026360267662 | (5-sqrt(5))/8 |
| 215287571516328 | (-1+sqrt(5))/4 |

Writing `P=(X+Y sqrt(5))/8` with integer matrices `X,Y`, the checker verifies
entrywise using integer arithmetic that

\[
 P=P^T,\qquad \operatorname{diag}P=\mathbf1,\qquad P^2=75P.
\]

Because `P` is real symmetric, its eigenvalues lie in `{0,75}`.  Its trace is
300, hence `rank(P)=4`; in particular `P` is positive semidefinite and is the
Gram matrix of 300 real unit vectors in dimension four.

## D4-T3. Exact dimension-four value

The same integer calculation gives

\[
 \langle A,P\rangle
 =1539823299061914600
  +706968072319078800\sqrt5.
\]

Thus the displayed number is an attained dimension-four vector value for the
frozen matrix.  This statement is an attainability result; it does not need a
claim that this is the largest dimension-four value.

## D4-T4. Unambiguous four-dimensional directions

The principal Gram submatrix on `S={0,1,2,3}` has exact determinant

\[
 \det P_{S,S}=\frac{9-4\sqrt5}{256}>0.
\]

Let `K=P_{S,S}` and let `L` be the unique lower-triangular Cholesky factor with
positive diagonal, so `K=LL^T`.  For every index `i`, set

\[
 b_i=P_{S,i},\qquad u_i=L^{-1}b_i\in\mathbb R^4.
\]

Since `P` has rank four and `K` is nonsingular, its Schur complement is zero,
and therefore

\[
 u_i^Tu_j=b_i^TK^{-1}b_j=P_{ij}.
\]

This is a deterministic coordinate prescription for all 300 directions.  It
uses only the exact table in D4-T2 and positive square roots arising in the
four-by-four Cholesky factorization.

## D4-T5. Explicit state and measurements

Let `X,Y,Z` be the Pauli matrices and define four Hermitian anticommuting
matrices on two qubits by

\[
 \Gamma_1=X\otimes I,\quad
 \Gamma_2=Z\otimes I,\quad
 \Gamma_3=Y\otimes X,\quad
 \Gamma_4=Y\otimes Z.
\]

For a real unit vector `u`, put

\[
 \Gamma(u)=\sum_{r=1}^4u_r\Gamma_r.
\]

The Clifford relations imply `Gamma(u)^2=I`, so each observable has outcomes
in `{+1,-1}`.  On the maximally entangled two-qubit state

\[
 |\Phi_4\rangle=\frac12\sum_{k=0}^3|k,k\rangle,
\]

use Alice observable `M_i=Gamma(u_i)` and Bob observable
`N_j=Gamma(u_j)^T`.  The maximally entangled trace identity gives

\[
 \langle\Phi_4|M_i\otimes N_j|\Phi_4\rangle
 =\frac14\operatorname{Tr}(\Gamma(u_i)\Gamma(u_j))
 =u_i^Tu_j=P_{ij}.
\]

Consequently these explicit measurements attain the value in D4-T3.

## D4-T6. Exact classical witness

The archived sign vectors satisfy, by direct arbitrary-precision integer
summation,

\[
 \sum_{i,j}A_{ij}\,\mathrm{ax}_i\,\mathrm{by}_j
 =2081044153087351400.
\]

This proves a classical lower bound of the stated size.  It does not prove
that no other sign pair is larger.

## D4-T7. Remaining theorem gate

The Grothendieck-ratio claim becomes valid only after proving

\[
 \max_{x_i,y_j\in\{\pm1\}}x^TAy
 \le 2081044153087351400.
\]

No such global upper bound is supplied here.  The recovered restricted
degree-four dual families were refuted, and the unrestricted dual feasibility
problem remains open.  The local contribution of this certificate is to remove
all ambiguity about the instance, vector witness, physical measurements, and
classical equality witness, leaving one sharply stated obstruction.

