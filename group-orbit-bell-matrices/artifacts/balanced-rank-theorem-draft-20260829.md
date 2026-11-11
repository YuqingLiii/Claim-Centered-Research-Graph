# Balanced-rank theorem for group-orbit Bell matrices

## GO-T1: vector relaxation and spectral upper bound

For a real `m x n` matrix `A`, define

```text
beta_vec(A) = sup sum_ij A_ij <x_i,y_j>,
```

where every `x_i` and `y_j` is a real unit vector and the common ambient
dimension is unrestricted.  Put the row vectors into matrices `X` and `Y`.
Then the objective is `Tr(X^T A Y)`, while `||X||_F^2=m` and
`||Y||_F^2=n`.  Hence

```text
beta_vec(A) <= ||A||_op sqrt(mn)
```

by the operator/Frobenius norm inequality and Cauchy--Schwarz.

## GO-T2: balanced top-singular-space criterion

Let `sigma=||A||_op>0`.  Choose paired orthonormal bases `U` and `V` for the
left and right top singular subspaces, with the same column rank `r` and
`A V = sigma U`.

A sufficient balanced-rank certificate is

```text
diag(U U^T) = (r/m) 1_m,
diag(V V^T) = (r/n) 1_n.
```

Indeed, set

```text
X = sqrt(m/r) U,
Y = sqrt(n/r) V.
```

All rows are unit, and

```text
Tr(X^T A Y)
  = sqrt(mn)/r Tr(U^T A V)
  = sqrt(mn)/r (r sigma)
  = sigma sqrt(mn).
```

Together with GO-T1 this proves equality.  More generally, saturation is
equivalent to a positive-semidefinite weight on the paired top singular space
whose two leverage-score diagonals have the required relative normalization;
the displayed scalar weight is the canonical group-invariant solution.

## GO-T3: invariant-projector rank lemma

Let a finite group act transitively on a set of size `m` by permutation
matrices `P_g`.  If an orthogonal projector `Pi` commutes with every `P_g`,
then its diagonal is constant: transitivity conjugates any diagonal entry to
any other.  Since `Tr(Pi)=rank(Pi)=r`, every diagonal entry equals `r/m`.

The same statement holds independently for a transitive column action of size
`n`.

## GO-T4: transitive equivariant optimum theorem

Suppose a finite group has transitive permutation actions `P_g` on the rows
and `Q_g` on the columns and

```text
P_g A Q_g^T = A
```

for every `g`.  The top left and right singular subspaces are invariant, and
their orthogonal projectors commute with the corresponding permutation
actions.  GO-T3 therefore supplies the two constant diagonals in GO-T2.  Thus

```text
beta_vec(A) = sqrt(mn) ||A||_op.
```

The proof also gives explicit extremizing vectors: the normalized rows of any
paired top left/right singular bases.  For a square group-orbit matrix this is
`beta_vec(A)=n||A||_op`.

## GO-T5: necessity of balance and a counterexample

For `A=diag(2,1)`, the spectral upper bound is `4`.  The two diagonal terms can
be optimized independently, so `beta_vec(A)=3`.  The top singular projector is
`diag(1,0)`, whose diagonal is not balanced.  Thus group invariance without
transitivity, or a top space without balanced leverage scores, does not force
spectral-bound saturation.

## GO-T6: R/C/H commutant reduction

To classify all invariant extremizers rather than merely exhibit the scalar
one, average a feasible top-space weight over the group.  On each real
isotypic component, the averaged weight lies in the self-adjoint part of the
commutant.  Real Schur theory identifies the division-algebra type as
`R`, `C`, or `H`; with multiplicity `q`, the remaining variable is a positive
semidefinite Hermitian `q x q` matrix over that division algebra.

This gives the intended finite-dimensional R/C/H reduction, but the present
record still lacks a source-verified statement of the real Schur theorem and a
fully written necessity proof for every degenerate top-singular configuration.
Those are kept as separate open claim nodes.

## GO-T7: physical state and measurements

For real unit vectors in `R^r`, choose Hermitian Clifford generators
`Gamma_1,...,Gamma_r` with

```text
Gamma_a Gamma_b + Gamma_b Gamma_a = 2 delta_ab I,
Tr(Gamma_a Gamma_b)/D = delta_ab.
```

Then `Gamma(x)=sum_a x_a Gamma_a` is a Hermitian involution.  On the maximally
entangled state `|Phi_D>`, use Alice observable `Gamma(x_i)` and Bob observable
`Gamma(y_j)^T`.  The identity

```text
<Phi_D| M tensor N^T |Phi_D> = Tr(MN)/D
```

gives correlation `<x_i,y_j>`.  Thus the singular-vector extremizer in GO-T4
has an explicit bipartite state and dichotomic measurements.  A tensor-Pauli
construction works with local dimension at most `2^ceil(r/2)`.

The algebra above is included in the draft, but the exact minimal-dimension
convention and source attribution still require independent review.

## GO-T8: wreath-product corollary and remaining classification

If the natural row and column actions of `G wr S_k` are transitive and a matrix
is equivariant for those actions, GO-T4 applies without enumerating orbit
vectors individually.  In the special tensor case `A_k=A^{tensor k}`, the top
singular value is `||A||_op^k` and paired top singular spaces tensor, so the
canonical extremizer tensors as well.

What remains open is a general orbit-algebra reduction that computes the top
singular block and classifies every extremizer from R/C/H multiplicity data for
arbitrary wreath-product orbit matrices, not just the tensor or already
diagonalized cases.

## GO-T9: evidence boundary

GO-T1 through GO-T5 are complete author-level linear-algebra arguments.  GO-T7
is a standard explicit Clifford realization.  GO-T6 and the final sentence of
GO-T8 are incomplete classification layers.  None has yet passed the protocol's
independent adversarial review, so the corresponding graph nodes are not
labelled `PROVED`.

