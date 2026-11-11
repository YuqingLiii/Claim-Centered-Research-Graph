# Root classical denominators: sources and normalization

Date: 2026-09-07. Scope: C1--C4 in
`classical-family-registration-20260907.md`. This is a source/normalization
note, not an independent review, node promotion, or novelty finding. Only
this staged artifact was edited. Primary sources were checked online;
external numerical certificates were not rerun.

## L1. Directly checked prior sources

1. [Designolle, Vertesi, Pokutta, *Better bounds on Grothendieck constants
   of finite orders*, arXiv:2409.03739v2](https://arxiv.org/html/2409.03739v2),
   Section II, Eq. (1), defines `SDP_1` as the same bilinear sign maximum
   used here. Section III.2 and Table 1 use unit-vector Gram matrices with
   `m=r(r-1)` for `D_r`, i.e. one representative per antipodal pair.
   They study `P-mu I`, including `mu=2/3`. Table 1 reports shifted ratios
   `4/3, 7/5, 10/7, 13/9, 16/11, 19/13` for `r=3,...,8`; these entries
   have no heuristic asterisk. Section III.2 states the extension to
   `r=6,7,8`. Asterisks mark heuristic classical optima; shifted `E_8`
   is starred.

2. [Fishburn and Reeds, *Bell Inequalities, Grothendieck's Constant, and
   Root Two*, SIAM J. Discrete Math. 7 (1994), 48--56](https://epubs.siam.org/doi/abs/10.1137/S0895480191219350?journalCode=sjdmec),
   publisher abstract: a family of size `k(k-1)` approaches ratio `3/2`,
   and a diagonal change gives the size-20 ratio `10/7`. The full paper
   was inaccessible in this pass: the PDF endpoint redirected to the
   abstract. The more specific attribution of the exact `D_r` base norm
   and optimal shifts for `r=3,4,5` was checked only in item 1, Section
   III.2, and is not presented as a personally checked theorem locator
   in the 1994 original.

3. [Reeds and Sloane, *A finite matrix with Grothendieck ratio greater
   than sqrt(2)*](https://neilsloane.com/doc/ReedsSloane.pdf), author-hosted
   six-page note: pp. 2--3 construct the positive-root `E_8` Gram matrix;
   Eq. (1), p. 3, reduces its classical value to the squared largest
   signed-root sum. Lemma 1, pp. 4--5, proves that a maximizing signed
   sum has the signs of a regular linear functional. Lemma 2, pp. 5--6,
   uses Weyl-chamber transitivity to make the norm chamber independent.
   This is a directly readable primary proof of the root-system
   certificate mechanism, instantiated there for `E_8`. Its adaptation
   to `D_r` is a deduction, not the literal scope of its lemma statements.

4. [Finis, Lapid, Muller, *The spectral side of Arthur's trace formula*
   (2009)](https://www.math.uni-bonn.de/people/mueller/papers/pnas.pdf),
   PDF p. 3, paragraph **Root Zonotope** immediately after Eq. (4):
   `Z_Phi=(1/2) sum_{alpha in Phi_+}[-alpha^vee,alpha^vee]`
   is the convex hull of the Weyl orbit of
   `rho^vee=(1/2) sum_{alpha in Phi_+}alpha^vee`.
   This is an explicitly stated geometric identity, not an imported
   assertion about Bell values or diagonal shifts.

## L2. Exact translation and unshifted value

The following is an algebraic deduction with all normalization factors
shown. Let `U` have rows `e_i-e_j,e_i+e_j`, `i<j`, so `m=r(r-1)`.
After reordering the full root set, `W=[U;-U]`. Define

```text
P = UU^T/2                  (unit-root Gram matrix; literature convention)
C = P/(r-1)                (half-root orthogonal projection)
A = WW^T/[4(r-1)]
  = (1/2) [ C  -C ]
          [-C   C ],        n=2m.
```

For positive roots above, `rho=(r-1,r-2,...,1,0)` and
`||rho||^2=r(r-1)(2r-1)/6`. Roots have squared length 2, so their
coroots equal the roots. Item 4 gives

```text
sum_{alpha in D_r}[-alpha,alpha] = 4 conv(Weyl(D_r) rho).
```

Thus the greatest norm of a signed full-root sum is `4||rho||`.
It is attained by assigning positive roots sign `+1` and their negatives
sign `-1`; the resulting sum is `4rho`. Cauchy--Schwarz reduces the
bilinear PSD-Gram objective to this squared norm (the mechanism in item 3).
Consequently

```text
beta_cl(P) = 2||rho||^2 = r(r-1)(2r-1)/3,
beta_cl(A) = 16||rho||^2/[4(r-1)] = 2r(2r-1)/3.
```

`W^TW=4(r-1)I` makes `A` a projection, and the root vector strategy
attains `beta_q(A)=n`. Hence its ratio is exactly
`3(r-1)/(2r-1)`, the unshifted `D_r` ratios in item 1, Table 1.
The root geometry and this normalization do not support a novelty claim.

## L3. A shift does not commute with antipodal duplication

Write `B=A-lambda I_(2m)`. On antipodally constrained classical signs
`s=(a,-a)`, `t=(b,-b)`, direct block multiplication gives

```text
s^T B t = 2 a^T(C-lambda I_m)b
        = 2/(r-1) a^T(P-(r-1)lambda I_m)b.
```

Therefore the literature parameter is `mu=(r-1)lambda`, and `mu=2/3`
corresponds to `lambda=2/[3(r-1)]`. What follows without further proof is
the LOWER bound

```text
beta_cl(B) >= 2/(r-1) beta_cl(P-(r-1)lambda I_m).
```

The two matrix operations are different. With
`D(X)=(1/2)[X,-X;-X,X]`,

```text
B-D(C-lambda I_m) = -(lambda/2)[I,I;I,I].
```

The right side vanishes on the antipodal subspace but acts on the
symmetric subspace. Thus unrestricted full-root signs cannot simply be
discarded after a shift. Equality of the displayed classical bound is a
separate mathematical question for this family and parameter range.

For a precise description of those extra choices, any Bob sign vector
can be written `t=(z+q,q-z)` with `z_i in {-1,0,1}`, `q_i=0` when
`z_i != 0`, and `q_i in {-1,1}` otherwise. Maximizing Alice's signs then
gives the exact finite identity

```text
beta_cl(B)/2 = max_{z in {-1,0,1}^m} [
    sum_{i:z_i!=0}|(Cz)_i-lambda z_i|
  + sum_{i:z_i=0} max(|(Cz)_i|,lambda) ].
```

This follows from `|x-y|+|x+y|=2max(|x|,|y|)` for `lambda>=0`.
Restricting to `z in {-1,1}^m` recovers the half-root lower bound.
At `lambda=0`, convexity allows an endpoint maximizer and duplication
only rescales the classical and quantum values. That unshifted argument
does not certify removal of the zero coordinates when `lambda>0`.

## L4. What this comparison establishes

The unshifted family and its root-geometric norm method have direct
prior-art counterparts. Uniform diagonal modification is also a prior
construction. Neither the cited geometry nor the finite table proves
the registered whole-interval full-root plateau, and this pass does not
claim an all-`r` shifted formula or new Grothendieck bound. The exact
sign-elimination step is already in item 1, Section III.3, Eq. (9).
A new envelope computation must prove complete coverage and breakpoints.
