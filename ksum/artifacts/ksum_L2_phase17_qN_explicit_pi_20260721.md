# k-Sum L2 phase-17 proposer analysis — an explicit nonproduct `q=N` base law

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`  
Tier: proposer only; no independent review and no DAG status claim

## Decision

**B — a concrete nonproduct, positive, legal `q=N` law with the correct base-measure high-`C_t`
scale is sharply falsified.**  A globally coupled beta-binomial activation law on legal
variable-total histograms has constant base mass at `C_t=Theta(N^(4/3))`.  Nevertheless, on its
support the NO indicator is the point mass at a single scalar activation count.  The actual orbit
row span already contains every polynomial of degree `r` in that count at query degree `2r`.
An explicit Chebyshev polynomial of degree `O(sqrt(K))` then approximates NO to error `1/4`.

Consequently, at every cutoff `D=Theta(N^(2/3))`, the phase-16 projection residual is either zero
or its normalized correlation is at most `1/2`, strictly below `2/3`.  Thus nonproduct dependence,
variable totals, and abundant high-`C_t` support do not suffice if the support remains a
one-parameter activation family.

This is a scoped falsification of the family below, not an impossibility theorem for arbitrary
formula-defined nonproduct measures on the full histogram simplex.

## 1. Exact endpoint family and rounding

Take odd `N` and hence `q=N`, with

```text
m=(N-1)/2,
L=floor(N^(2/3)),
s=floor(N/(3L)).                                             (17.1)
```

For all sufficiently large odd `N`, `s>=1` and `L+1<=m`.  Use `L` switch pair-types and one
reservoir pair-type.  For each integer `0<=a<=L`, define the unordered split histogram `H_a` by

```text
a copies of          (s,s),
L-a copies of        (0,s),
one reservoir copy   (0,R_a),
R_a=N-Ls-as.                                                (17.2)
```

The reservoir may coincide as a split *state* with `(0,s)` for an exceptional `a`; it is still a
separate complementary value-pair type, and the histogram simply records the resulting
multiplicity.  This causes no ambiguity because `C_t(H_a)=as^2` distinguishes the profiles.

All legality and rounding gates are exact:

```text
a(2s)+(L-a)s+R_a=N,
R_a >= N-2Ls >= N/3 >0,
number of occupied pair-types = L+1 <= m.                    (17.3)
```

Every reservoir and inactive switch pair is unsplit.  Hence

```text
H_a is NO iff a=0,
C_t(H_a)=a s^2.                                              (17.4)
```

The support is genuinely variable-total: the reservoir total `R_a=N-Ls-as` changes with `a`.
The switch and reservoir construction also avoids any divisibility assumption on `N`.

## 2. A positive nonproduct law with the right base tail

Put the strictly positive law

```text
pi_{N,N}(H_a)=1/(L+1),             0<=a<=L.                  (17.5)
```

It has a formula-defined nonproduct realization.  Draw `Theta` uniformly from `[0,1]`, then,
conditional on `Theta`, activate the `L` labeled switches independently with probability
`Theta`, and finally push forward to the unordered histogram (17.2).  The beta integral gives

```text
Pr[A=a]=binom(L,a) integral_0^1 theta^a(1-theta)^(L-a)dtheta
       =1/(L+1).                                             (17.6)
```

Before pushforward the switches are not independent:

```text
Cov(X_i,X_j)=E[Theta^2]-E[Theta]^2=1/3-1/4=1/12.             (17.7)
```

They are coupled further by the deterministic reservoir total.  Thus (17.5) is not a disguised
independent-slot product measure.

It also has the desired high-target scale at the level of the positive base law.  For all large
`N`, `s=Theta(N/L)=Theta(N^(1/3))`; more explicitly, once `N/(3L)>=4`,

```text
N/(4L) <= s <= N/(3L).                                      (17.8)
```

Therefore every `a` in `[ceil(L/3),floor(2L/3)]` has

```text
C_t(H_a)=a s^2=Theta(N^2/L)=Theta(N^(4/3)),                  (17.9)
```

and (17.5) assigns this interval asymptotic mass `1/3`.  This is base-measure mass; the
residual-weighted tail required by phase 16 is a separate gate and is not inferred from (17.9).

## 3. The actual orbit rows recover activation polynomials

For `j` distinct nonfixed complementary source-pair types, query one variable from each side of
each type.  This has multilinear query degree `2j` and pattern
`kappa_1=...=kappa_j=(1,1)`.  On a target split `(r,u)`, its one-slot factor is

```text
A_{1,1}(r,u)=ru.                                             (17.10)
```

On `H_a`, exactly `a` target slots have nonzero factor, each equal to `s^2`; inactive switches and
the reservoir contribute zero.  Directly summing injective target assignments gives the exact
orbit row

```text
F_j(H_a)=(a)_j s^(2j) / ((m)_j (N)_(2j)).                   (17.11)
```

The denominator is nonzero in the range used below.  Thus, whenever `2j<D`, the actual degree-`<D`
orbit-feature span contains `(a)_j`, equivalently `binom(a,j)`.  Together with the constant row,
it contains every univariate polynomial in `a` of degree at most `r` provided

```text
2r<D.                                                        (17.12)
```

This conclusion uses only the repeated `(1,1)` rows and can be checked directly from the orbit
average; no claim about the still-unreviewed general phase-12 tensor formula is needed.

## 4. Explicit Chebyshev discriminator

Let `b(a)=1[a=0]`.  For `L>=2`, set

```text
y_L(a)=(L+1-2a)/(L-1),
alpha_L=arcosh((L+1)/(L-1)),
r_L=ceil(arcosh(4)/alpha_L),
p_L(a)=T_(r_L)(y_L(a))/T_(r_L)(y_L(0)),                    (17.13)
```

where `T_r` is the Chebyshev polynomial of the first kind.  Then `p_L(0)=1`.  For every real
`a in [1,L]`, `y_L(a) in [-1,1]`, so `|T_(r_L)(y_L(a))|<=1`, while

```text
T_(r_L)(y_L(0))=cosh(r_L alpha_L)>=4.                       (17.14)
```

Consequently

```text
max_{0<=a<=L} |b(a)-p_L(a)| <= 1/4.                         (17.15)
```

Also `alpha_L=Theta(L^(-1/2))`, hence `r_L=O(sqrt(L))`.  For example, for `L>=5`, the elementary
bound `cosh x<=1+x^2` on `0<=x<=1` gives
`alpha_L>=sqrt(2/(L-1))`, which already yields the required upper bound on `r_L`.

Since `L=Theta(N^(2/3))`, every cutoff satisfying `D>=cL` for a fixed `c>0` obeys
`2r_L<D` for all sufficiently large `N`.  Equations (17.11)--(17.12) therefore place `p_L` in the
*actual* orbit-feature span at every target cutoff `D=Theta(N^(2/3))`.

## 5. Sharp failure of the phase-16 projection residual

Let `g=b-Proj_{V_D}^{L_2(pi)} b` be the phase-16 residual for (17.5).  If `g=0`, the normalized
signed law is undefined and the candidate fails immediately.  Otherwise let

```text
W_pi(H_a)=pi(H_a)g(a)/||g||_(1,pi).                         (17.16)
```

It has zero mass and annihilates `V_D`, hence also `p_L`.  With label `f=1-2b`, unit `l1`, and
(17.15),

```text
|<W_pi,f>|
 =2|<W_pi,b>|
 =2|<W_pi,b-p_L>|
 <=2||b-p_L||_infinity
 <=1/2 <2/3.                                                (17.17)
```

Using the exact phase-16 identity, the same statement is

```text
2||g||_(2,pi)^2 / ||g||_(1,pi) <= 1/2,                     (17.18)
```

so in particular `3||g||_(2,pi)^2>||g||_(1,pi)` is impossible.  This is an analytic bound on the
projection residual, independent of any numerical LP and even independent of the particular
positive weights on this support.

The residual-weighted high-`C_t` gate need not be decided: the required correlation gate already
fails by a fixed margin.  Notice the separation of issues.  The positive law itself is nonproduct
and has constant mass at the correct tail scale, but the support encodes the label as the
one-dimensional statistic `b=1[C_t=0]=1[a=0]`.  Selective projection cannot undo that collapse.

## 6. Gate ledger

| Gate | Family (17.1)--(17.6) |
|---|---|
| formula-defined positive `pi_{N,N}` | **PASS** on its stated support |
| nonproduct dependence | **PASS** by (17.6)--(17.7) |
| exact odd-`q` legality and rounding | **PASS** by (17.1)--(17.3) |
| occupied-pair budget `K=Theta(N^(2/3))` | **PASS**, with `K=L+1` |
| base mass at `C_t=Theta(N^(4/3))` | **PASS** by (17.8)--(17.9) |
| actual degree-`<D` orbit span identified | **PASS** for the rows needed in (17.11) |
| genuinely nonseparable support geometry | **FAIL**: the label is a scalar activation predicate |
| correlation strictly above `2/3` | **FAIL**: at most `1/2` by (17.17) |
| residual-weighted high-`C_t` mass | not needed after correlation failure |
| target band `D=Theta(N^(2/3))` | **FAIL** for every fixed positive linear cutoff constant |

## 7. Scoped conclusion

This family was a serious endpoint candidate in three respects: it is exactly legal without a
divisibility subsequence, its positive law is explicitly nonproduct, and it places constant mass
at `C_t=Theta(N^(4/3))`.  It nevertheless fails for a more basic reason.  Whenever all active
switches contribute the same target-pair count and all remaining occupancy is absorbed by an
unsplit reservoir, the repeated `(1,1)` orbit rows recover low-degree polynomials in the activation
count.  A target cutoff linear in `K` then vastly exceeds the `O(sqrt(K))` degree needed to
approximate the boundary predicate.

The selective-orbit-tensor node therefore remains open.  Any successful `q=N` base measure must
prevent the NO label from becoming a low-degree-approximable function of one activation coordinate
even after the exact orbit rows are restricted to its support.

No distinct escape route was analyzed or commissioned in this pass.  No `PROVED`, `CERTIFIED*`,
`NUMERICAL`, or `REFUTED` status is claimed.
