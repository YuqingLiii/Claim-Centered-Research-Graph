# Complete spectral-bound extremizer classification

This note replaces the over-strong idea that the real/complex/quaternionic
commutant describes every extremizer.  The commutant describes invariant
weights.  The full extremizer set is a spectrahedron in the paired top
singular space.

## GOC-T1: setup

Let `A` be a nonzero real `m x n` matrix, let

```text
sigma = ||A||_op > 0,
```

and let the multiplicity of `sigma` be `r`.  Choose matrices
`U in R^(m x r)` and `V in R^(n x r)` with orthonormal columns such that

```text
A V = sigma U,       A^T U = sigma V.
```

For a vector strategy in `R^d`, write its row vectors as matrices
`X in R^(m x d)` and `Y in R^(n x d)`.  Feasibility is

```text
diag(X X^T) = 1_m,       diag(Y Y^T) = 1_n.
```

Define the paired-top-space balance spectrahedron

```text
S(A) = { H in Sym_r :
         H >= 0,
         diag(V H V^T) = 1_n,
         diag(U H U^T) = (n/m) 1_m }.
```

Changing the paired singular bases to `U R,V R` with `R` orthogonal sends
`H` to `R^T H R`, so this object is basis-independent up to canonical
orthogonal congruence.

## GOC-T2: equality-condition theorem

The universal chain

```text
<X,A Y>_F
  <= ||X||_F ||A Y||_F
  <= sigma ||X||_F ||Y||_F
  =  sigma sqrt(mn)
```

has equality if and only if there is a matrix `T in R^(r x d)` such that

```text
Y = V T,
X = sqrt(m/n) U T,
H = T T^T belongs to S(A).
```

### Proof

Assume equality.  Equality in
`||A Y||_F <= sigma ||Y||_F` says that every column of `Y` lies in the
top right singular space, hence `Y=V T`.  Equality in Frobenius
Cauchy--Schwarz has positive proportionality

```text
X = lambda A Y.
```

Because `||X||_F=sqrt(m)`, `||Y||_F=sqrt(n)`, and equality in the second
bound gives `||A Y||_F=sigma sqrt(n)`, the proportionality factor is
`lambda=sqrt(m/n)/sigma`.  Thus

```text
X = sqrt(m/n) U T.
```

Writing `H=T T^T`, the two unit-row conditions become exactly the two
diagonal equations defining `S(A)`.

Conversely, take any `H in S(A)` and any factorization `H=T T^T`.  The
displayed formulas for `X,Y` give unit rows.  Moreover,

```text
<X,A Y>_F
  = sqrt(m/n) sigma Tr(T^T T)
  = sqrt(m/n) sigma Tr(H).
```

The column-side diagonal constraint gives `Tr(H)=n`, so the value is
`sigma sqrt(mn)`.  This proves both directions.

## GOC-T3: classification and minimal vector dimension

Consequently, `A` saturates the spectral upper bound if and only if `S(A)`
is nonempty.  Whenever it does, all saturating vector strategies are obtained
from factorizations of matrices in `S(A)` by the formulas in GOC-T2.

For a fixed `H`, a factorization `H=T T^T` in width `d` exists exactly when

```text
d >= rank(H).
```

Therefore the minimum real vector dimension of a spectral-bound extremizer is

```text
d_min(A) = min { rank(H) : H in S(A) }.
```

Two factors of the same `H` give the same row-vector Gram data and differ only
by an ambient orthogonal isometry after zero-padding.  Thus the matrices
`H in S(A)`, together with their factorizations when a concrete coordinate
realization is wanted, classify the extremizers up to ambient orthogonal
equivalence.

## GOC-T4: transitive equivariant corollary

Suppose a finite group acts transitively on rows and columns and

```text
P_g A Q_g^T = A.
```

For `A != 0`, the paired top singular projectors have constant diagonals
`r/m` and `r/n`.  Hence

```text
H_0 = (n/r) I_r
```

belongs to `S(A)`.  GOC-T2 recovers

```text
beta_vec(A) = sigma sqrt(mn)
```

and the canonical singular-vector extremizer.  If `A=0`, the equality is
trivial and every feasible strategy has value zero.

This corollary closes the zero-matrix edge case left implicit in the earlier
draft.

## GOC-T5: why the R/C/H commutant is not the full classification

Take `A=I_3` and let `S_3` act simultaneously on rows and columns.  The
actions are transitive and `P_g A P_g^T=A`.  Here `U=V=I_3`, `r=3`, and

```text
S(A) = { H >= 0 : diag(H)=1 }.
```

For example,

```text
H = [ 1   1/2  0
      1/2 1    0
      0   0    1 ]
```

has eigenvalues `3/2,1/2,1`, hence is positive definite and belongs to
`S(A)`.  Any factor `H=T T^T` gives `X=Y=T`, a unit-row strategy of value
`3`, so it is an extremizer.  But `H` does not commute with all permutation
matrices: its off-diagonal entries are not constant.  It is therefore not in
the `S_3` commutant.

Thus an R/C/H commutant reduction cannot classify every extremizer.  It can
classify the invariant part of `S(A)` or produce a canonical invariant
representative.

## GOC-T6: correct invariant-weight statement

The group acts on the paired top singular space through an orthogonal
representation `R_g`, chosen compatibly so that

```text
P_g U = U R_g,       Q_g V = V R_g.
```

If `H in S(A)`, then `R_g H R_g^T` also lies in `S(A)`: the two diagonal
vectors are merely permuted, and they are constant.  Hence

```text
H_bar = (1/|G|) sum_g R_g H R_g^T
```

is an invariant member of `S(A)`.  Real Schur theory decomposes such invariant
self-adjoint weights into Hermitian positive-semidefinite multiplicity blocks
over `R`, `C`, and `H`.

This proves existence of an invariant extremizing weight whenever any
spectral-bound extremizer exists.  It does not say that a noninvariant
extremizer is equivalent to its average, and it does not replace the full
spectrahedral classification in GOC-T3.

The final R/C/H block formula and its source attribution remain to be written
and independently reviewed.

## GOC-T7: physical realization and dimension accounting

Let `H in S(A)` have rank `s` and choose a factor `T in R^(r x s)`.  GOC-T2
then gives real unit vectors in `R^s`.  Choose Hermitian Clifford generators
`Gamma_1,...,Gamma_s` with

```text
Gamma_a Gamma_b + Gamma_b Gamma_a = 2 delta_ab I,
Tr(Gamma_a Gamma_b)/D = delta_ab.
```

On the maximally entangled state in `C^D tensor C^D`, take Alice's observable
to be `Gamma(x_i)` and Bob's to be `Gamma(y_j)^T`.  The normalized trace
identity reproduces `<x_i,y_j>`.  The explicit construction in
`clifford-measurement-construction-20260829.md` gives

```text
D = 2^floor(s/2).
```

Thus minimizing `rank(H)` simultaneously minimizes the real vector dimension
within this classification and improves the explicit local quantum-dimension
bound.  No minimality claim for the complex Hilbert-space dimension is used.

## GOC-T8: status boundary

GOC-T1 through GOC-T6 are complete author-level linear-algebra arguments.
GOC-T7 is an explicit author-level construction with a concrete dimension
bound.  None has yet passed an independent adversarial review, so
the corresponding claim nodes remain below `PROVED`.
