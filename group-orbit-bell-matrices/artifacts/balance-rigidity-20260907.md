# Balance-kernel rigidity and vector-dimension reduction

Date: 2026-09-07. Author-level mathematical argument; independent review pending.
Canonical owner: `GROTHORB.balance-rigidity`, route `balance-kernel`.
The existing load-bearing classification is `GROTHORB.extremizer-classification`,
specifically GOC-T1 through GOC-T4 of
`complete-extremizer-classification-20260829.md`.
The statements below concern real vector dimensions. They do not assert a
minimum complex Hilbert-space dimension or a new Grothendieck ratio.

## BR-1: setup and strictly positive feasible weight

Let nonzero real `A` have size `m by n`, and suppose a finite group acts
transitively on its rows and on its columns by permutation matrices satisfying
`P_g A Q_g^T=A`. Let `sigma=||A||_op>0` have multiplicity `r>=1`, and choose
paired orthonormal top singular bases `U,V` of widths `r`:

```text
U^T U = V^T V = I_r,       A V = sigma U,       A^T U = sigma V.
```

For symmetric `r by r` matrices define the linear map

```text
L(K) = (diag(U K U^T), diag(V K V^T)).
```

The balance spectrahedron and its scalar feasible point are

```text
S(A) = { H>=0 : L(H)=((n/m)1_m,1_n) },
c = n/r > 0,                       H_0 = c I_r.
```

For completeness, equivariance makes `A A^T` commute with `P_g`, and `A^T A`
commute with `Q_g`. Their top spectral projectors `U U^T,V V^T` also commute
with these permutations. Transitivity makes their diagonal entries constant;
their traces are `r`, so the entries are respectively `r/m,r/n`. Hence
`H_0` satisfies both balance equations and is positive definite. Here
"strictly positive" means interior to the positive-semidefinite cone;
it need not be interior to `S(A)` in the whole space `Sym_r`.

The existing equality classification therefore applies to every vector
optimum, since the spectral bound is attained. Its minimum-dimension formula is

```text
d_min(A) = min { rank(H) : H in S(A) }.
```

## BR-2: exact affine description and uniqueness

Subtracting the balance equations of `H_0` from those of an arbitrary `H`
gives the exact identity

```text
S(A) = (H_0 + ker L) intersect { H>=0 }.
```

If `L` is injective, this set is the singleton `{H_0}`. Conversely, suppose
`0 != K in ker L`. If `0<epsilon<c/||K||_op`, then

```text
H_0 + epsilon K > 0,              H_0 - epsilon K > 0.
```

Both matrices have the required balance equations and are distinct. Therefore
the feasible balance weight is unique if and only if `L` is injective, and in
that case it is precisely `(n/r)I_r`.

This conclusion is independent of the paired orthonormal bases: replacing
`U,V` by `U R,V R` for orthogonal `R` replaces the kernel by its orthogonal
congruence image, which preserves its dimension and the ranks of weights.

## BR-3: constructive boundary point for a nonzero kernel

For `K in ker L`, summing either side of its zero-diagonal equation gives

```text
Tr(K) = Tr(V K V^T) = 0.
```

A nonzero real symmetric traceless matrix has both a positive and a negative
eigenvalue. In particular `lambda_min(K)<0`, and `r>=2`. Put

```text
t_* = -c/lambda_min(K) > 0,
H_* = c I_r + t_* K.
```

If `lambda_i` are the eigenvalues of `K`, those of `H_*` are

```text
c (1 - lambda_i/lambda_min(K)).
```

Since `lambda_i>=lambda_min(K)` and `lambda_min(K)<0`, every displayed
eigenvalue is nonnegative, and at least one is zero. Thus `H_*>=0` and
`rank(H_*)<=r-1`. Its balance equations hold because `L(K)=0`, so
`H_* in S(A)`. Also `Tr(H_*)=n>0`, so it is not the zero matrix.

This is a direct endpoint construction; it does not require an optimization
algorithm or an assertion that a numerical solver found an extreme point.

## BR-4: vector-dimension conclusion

The equality classification writes all optimal strategies as

```text
Y = V T,        X = sqrt(m/n) U T,        H = T T^T in S(A).
```

If `L` is injective, `H=H_0` has rank `r`. Since
`rank(T T^T)=rank(T)<=d` for `T` of width `d`, every optimal strategy in
`R^d` satisfies `d>=r`. Factoring `H_0` in width `r` also attains this bound,
so `d_min(A)=r`.

If `L` is not injective, factor the `H_*` constructed in BR-3 in width
`rank(H_*)`. This gives an optimal strategy in dimension at most `r-1`.
It is an upper bound on the minimum dimension, not necessarily the minimum:
different kernel directions or other feasible weights may reduce rank further.

The conclusion is about every optimal strategy, not only a group-invariant
one. Averaging over the group is unnecessary and could erase the rank
reduction by replacing a singular feasible weight with `H_0`.

## BR-5: exact injective example with `r=2`

Take `m=n=3` and `A=I_3-J_3/3`, with `J_3` the all-ones matrix. Simultaneous
permutation of rows and columns by `S_3` preserves `A`, so both actions are
transitive. The matrix is the orthogonal projection onto `1_3^perp`; its
top singular value is one with multiplicity two. Paired bases are `U=V` with
rows

```text
( 1/sqrt(2),  1/sqrt(6)),
(-1/sqrt(2),  1/sqrt(6)),
( 0,        -2/sqrt(6)).
```

Write `K=[[a,b],[b,c']]`. The third diagonal entry of `U K U^T` is
`(2/3)c'`. If all three diagonal entries vanish, first `c'=0`; subtracting
the first two entries gives `2b/sqrt(3)=0`; either remaining equation gives
`a/2=0`. Thus `L` is injective. The unique weight is `(3/2)I_2`, the vector
optimum is `3`, and its minimum real vector dimension is exactly `2`.

For exact rational checking one can use the unnormalized rows
`R=((1,1),(-1,1),(0,-2))`. With `C=diag(sqrt(2),sqrt(6))`, `U=R C^-1`.
The invertible congruence `B=C^-1 K C^-1` preserves kernel dimension, and
`diag(R B R^T)` has coefficient matrix

```text
[ 1   2   1 ]
[ 1  -2   1 ]
[ 0   0   4 ]
```

in coordinates `(B_11,B_12,B_22)`. Its determinant is `-16`, hence its
rank is three. This check uses no floating-point singular-value threshold.

## BR-6: exact noninjective example with `r=3`

Take `A=I_3`, `U=V=I_3`, and the same simultaneous transitive `S_3` action.
Now `r=3`, `H_0=I_3`, and `L(K)=(diag(K),diag(K))` has kernel dimension
three. In particular

```text
K = [0 1 0; 1 0 0; 0 0 0],
H_* = I_3 + K = [1 1 0; 1 1 0; 0 0 1]
```

is the BR-3 boundary construction because `lambda_min(K)=-1`. Its
eigenvalues are `2,1,0`, so it is a rank-two feasible weight. A still smaller
weight is `J_3=1_3 1_3^T`, of rank one. Taking all three Alice vectors and all
three Bob vectors equal to the scalar `1` attains the vector optimum `3`.
Thus `d_min(I_3)=1`, illustrating that BR-3 need not find minimum rank.

## BR-7: evidence boundary

BR-1 through BR-6 give an author-level proof of the registered criterion and
two representative exact examples. The checker
`grothendieck-group-orbit/tools/check_balance_rigidity.py` records exact
rational checks of these examples. Finite checks are supporting evidence for
the examples; the universal theorem rests on BR-1 through BR-4. No canonical
node assessment is changed by this artifact. Independent review must cover
both the implication here and every load-bearing classification input before
any unconditional `PROVED` promotion.
