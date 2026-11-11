# A transitive projection family with prescribed optimal vector dimension

Date: 2026-09-07. Author-level proof; independent review pending.
Canonical owner: `GROTHORB.root-frame-dimension`, route `root-frame-rigidity`.
Load-bearing nodes: `GROTHORB.balance-rigidity` and
`GROTHORB.transitive-optimum`. The former is developed in
`balance-rigidity-20260907.md`, with its classification dependency explicit.
No novelty or optimality of the number of settings is asserted.

## RF-1: exact family and tightness

Fix an integer `r>=3`. Let `Omega` consist of all vectors

```text
epsilon e_i + delta e_j,       1<=i<j<=r,       epsilon,delta in {-1,+1}.
```

There are `n=4 binom(r,2)=2r(r-1)` distinct vectors. Define the real
`n by r` matrix `W` whose rows are their transposes, and set

```text
A = W W^T / [4(r-1)],        U=V=W/[2 sqrt(r-1)].
```

For a fixed pair `i<j`, summing the four row outer products cancels their
off-diagonal entries and yields `4 e_i e_i^T+4 e_j e_j^T`. Each coordinate
belongs to `r-1` pairs. Consequently

```text
W^T W = 4(r-1) I_r,           U^T U=I_r,           A=U U^T.
```

Thus `A` is a nonzero real symmetric orthogonal projection of rank `r`.
Its top singular value is one, with multiplicity exactly `r`, and `U=V`
are paired top singular bases. The entries of `A` are rational because
`W` has integer entries.

## RF-2: ordinary permutation transitivity

Let `G` be the finite group of signed coordinate permutations on `R^r`.
It permutes the set `Omega` transitively: a coordinate permutation maps
one two-element support to another, and independent coordinate sign changes
then select either sign on that support.

Index rows and columns of `A` by `Omega`, and let `P_g` be the ordinary
permutation matrix defined by `P_g e_w=e_(g w)` on `R^Omega`. The label `w`
denotes an element of `Omega`, whereas `e_w` is its coordinate vector in
the `n`-dimensional label space. Directly,

```text
(P_g W)_w = (g^-1 w)^T = w^T g,       P_g W=W g.
```

Here `g` is orthogonal, so

```text
P_g A P_g^T = W g g^T W^T/[4(r-1)] = A.
```

This is an ordinary transitive permutation action on both matrix axes.
Although signed coordinate permutations construct the action on the roots,
the matrices `P_g` themselves have only zero and positive-one entries.

## RF-3: injectivity of the balance map

Let `K in Sym_r` satisfy `diag(U K U^T)=0`. Multiplication by the positive
normalization factor shows `w^T K w=0` for every `w in Omega`. For every
pair `i<j`, the two roots `e_i+e_j` and `e_i-e_j` therefore give

```text
K_ii + K_jj + 2 K_ij = 0,
K_ii + K_jj - 2 K_ij = 0.
```

Subtracting gives `K_ij=0`; adding gives `K_ii+K_jj=0`. For any index `i`,
choose two other distinct indices `j,k`, possible because `r>=3`. Then

```text
2 K_ii = (K_ii+K_jj) + (K_ii+K_kk) - (K_jj+K_kk) = 0.
```

Every diagonal entry is zero as well, so `K=0`. The first component of the
paired balance map is already injective, hence the full map is injective.
Equivalently, the root outer products span `Sym_r` under the trace pairing.

The hypothesis `r>=3` is used at this exact step. When `r=2`, the nonzero
matrix `diag(1,-1)` has zero quadratic form on all four roots; that case is
outside the registered family and no rigidity conclusion for it is used.

## RF-4: optimum, unique balance weight, and minimum dimension

By RF-1 and RF-2, the transitive spectral optimum is `n ||A||_op=n`.
It can also be exhibited without invoking a black-box optimization routine:

```text
X=Y=W/sqrt(2).
```

Every row is a unit vector, `A Y=Y`, and
`<X,A Y>_F=||Y||_F^2=n`, attaining the universal spectral upper bound `n`.

RF-3 and the balance-kernel rigidity criterion give the unique feasible
balance weight

```text
H_0=(n/r)I_r=2(r-1)I_r.
```

Its rank is `r`. The full extremizer classification, as used in the rigidity
criterion, shows that every optimal real vector strategy needs dimension at
least `r`. The displayed strategy has dimension `r`; therefore

```text
d_min(A)=r.
```

Uniqueness here means uniqueness of the balance weight, or equivalently of
the row-vector Gram data up to ambient orthogonal equivalence. It does not
mean uniqueness of concrete coordinates, nor minimum complex quantum
Hilbert-space dimension.

## RF-5: finite checks and status boundary

The companion exact rational checker verifies `r=3,4,5`: respectively
`n=12,24,40`. It checks root counts, tight-frame identities, projection and
rank identities, generating permutation actions and transitivity, the full
rank of the quadratic-form coefficient map, and an exact rational Gram
matrix realizing objective `n`. These finite checks do not prove the
universal family; RF-1 through RF-4 supply the author-level proof.

Checker: `grothendieck-group-orbit/tools/check_balance_rigidity.py`.
Run record: `balance-rigidity-exact-check-20260907.txt`.
The proof was written after registration of `GROTHORB.root-frame-dimension`.
No canonical node assessment was changed by this artifact. Independent
review and attachment of scoped evidence remain required before a
completion-level assessment.
