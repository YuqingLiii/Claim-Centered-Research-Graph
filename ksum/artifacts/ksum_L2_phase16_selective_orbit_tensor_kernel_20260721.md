# k-Sum L2 phase-16 proposer analysis — selective orbit-tensor projection kernel

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`  
Tier: proposer only; no independent review and no DAG status claim

## Decision

**C — an exact selective coefficient law exists as a weighted orbit-feature projection, but the
choice of weight remains exactly the missing dual-polynomial problem.**  The construction below
annihilates the actual orbit rows `F_gamma` and no larger coordinate-cylinder space.  It gives
closed formulas for zero mass, `l1` normalization, correlation, and high-`C_t` mass.  It also
explains why `q=5` can have growing feature rank even though there are only two complementary value
pairs.

However, the construction is a normal form, not yet an asymptotic witness.  A duality calculation
shows that optimizing its base measure is equivalent to finding the original optimal signed dual.
The present pass therefore does not establish a constant above `2/3`, a uniform annihilation band,
or the two endpoint theorem.  No impossibility for selective kernels is obtained.

## 1. Exact truncated orbit-feature map

Let `Omega_{N,q,K}` be any finite set of legal unordered split histograms, written with an ordered
slot representative

`H=(tau_1,...,tau_m)`, `tau_i=(r_i,u_i)`, `m=(q-1)/2`,

including unused slots `(0,0)`.  For a nonzero source-pair query pattern
`kappa=(alpha,beta)`, define

`a_kappa(tau)=((r)_alpha (u)_beta+(r)_beta (u)_alpha)/2`.

Introduce a formal variable `z_kappa` for every such pattern and the slot-product

```text
P_H(z)=product_{i=1}^m (1+sum_kappa z_kappa a_kappa(tau_i)).       (16.1)
```

Give `z_(alpha,beta)` weighted degree `alpha+beta`.  The coefficient of
`z_{kappa_1}...z_{kappa_rho}` in (16.1), with the usual multiplicity factor when patterns repeat,
is precisely the injection tensor

```text
T_{boldkappa}(H)
 = sum_{iota:[rho]->[m] injective}
     product_{h=1}^rho a_{kappa_h}(tau_{iota(h)}).                 (16.2)
```

The phase-12 orbit row is the nonzero row rescaling

`F_{boldkappa}(H)=T_{boldkappa}(H)/((m)_rho (N)_d)`,

where `d=sum_h |kappa_h|`.  A query involving the fixed symbol gives the zero row.  Hence, for a
cutoff `D`, the actual feature map is exactly

```text
Phi_D(H) = coefficients of P_H having weighted degree <D,         (16.3)
```

with duplicate coordinates removed.  This includes the constant coordinate.  It is important
that (16.3) contains only symmetric injection tensors.  It does **not** contain every function of
a chosen set of assignment coordinates, which is the larger space accidentally annihilated by the
phase-15 determinant/OA law.

Equations (16.1)--(16.3) use the phase-12 formula only in its currently stated odd-`q`, `K<=m`
scope.  The parent node still records missing independent gates for the fully general `K<m` and
`rho>=3` formula; this proposer pass does not promote that input.

## 2. The selective projection coefficient law

Choose a legal support `S subseteq Omega_{N,q,K}` and a strictly positive probability law
`pi=(pi_H)_{H in S}`.  Let `A` be the matrix whose column at `H` is `Phi_D(H)`, after choosing any
row basis.  Put

```text
G = A diag(pi) A^T,                                                (16.4)
b_H = 1[H is NO],
c = G^dagger A diag(pi) b,
g = b-A^T c.                                                       (16.5)
```

Here `G^dagger` is the Moore--Penrose inverse.  All spaces are finite-dimensional:
`A:R^S -> R^R`, `G:R^R -> R^R`, `c in R^R`, and `g in R^S`, where `R=rank A` after row-basis
reduction.  Thus there is no undefined inverse when raw orbit rows are dependent.

If `g` is nonzero, define

```text
Z = sum_H pi_H |g_H|,
W_pi(H)=pi_H g_H/Z.                                                (16.6)
```

Because `A diag(pi) g=0`, (16.6) gives exactly

```text
sum_H W_pi(H) F_gamma(H)=0   for every |gamma|<D,                  (16.7)
sum_H W_pi(H)=0,
sum_H |W_pi(H)|=1.                                                (16.8)
```

The total-mass identity is included in (16.7) because the constant row belongs to `Phi_D`.
Legality is automatic because `pi` is supported only on legal histograms.

This law is genuinely selective.  For an arbitrary coordinate-cylinder function `h` lifted to
the same support,

`<W_pi,h>=<g,h>_pi/Z`,

which need not vanish.  It vanishes automatically only when `h` lies in the actual row span or is
accidentally orthogonal to the residual.  Thus the phase-15 over-annihilation is absent.

## 3. Exact correlation and tail gates

Use label `f=+1` on YES and `f=-1` on NO, so `f=1-2b`.  Since `g` is orthogonal to the row span,
including constants and the projection `A^T c`,

```text
|<W_pi,f>|
 = 2 <g,g>_pi / ||g||_{1,pi}.                                    (16.9)
```

Therefore the required strict correlation gate is the explicit scalar inequality

```text
3 <g,g>_pi > ||g||_{1,pi}.                                       (16.10)
```

If `pi` is a probability law, Cauchy--Schwarz gives the useful sufficient condition
`||g||_{2,pi}>1/3`.  It is only sufficient; (16.10) is exact.

For any tail threshold `T`, the absolute mass of (16.6) on high-target-pair-count orbits is

```text
Tail_pi(T)
 = (sum_{H:C_t(H)>=T} pi_H |g_H|)/||g||_{1,pi}.                   (16.11)
```

Thus constant high-`C_t` mass is neither lost nor obtained by projection automatically.  It is a
second explicit requirement on `pi` and its projection residual.

## 4. Why this normal form is not yet a construction

Let `V_D` be the actual row span and consider the standard primal problem of uniformly
approximating `f` by `p in V_D`.  Suppose `W_*` is an optimal unit-`l1` dual and `p_*` is a matching
optimal primal, with error `epsilon`.  Complementary slackness gives, on the support of `W_*`,

```text
f(H)-p_*(H)=epsilon sign(W_*(H)).                                 (16.12)
```

Set `pi_H=|W_*(H)|`.  Since `W_*` annihilates `V_D`, the right side of (16.12) is orthogonal to
`V_D` in `L_2(pi)`.  Consequently `p_*` is precisely the weighted orthogonal projection of `f`,
and (16.5)--(16.6), applied equivalently to `b=(1-f)/2`, reconstructs `W_*` up to sign.

Hence the family (16.4)--(16.6) is universal: with a suitable `pi` it contains every optimal dual.
But this also exposes the hard boundary.  Saying "choose `pi` to satisfy (16.10)" is equivalent to
saying "find the desired dual polynomial."  Progress requires a **uniform, formula-defined**
`pi_{N,q}` for which the Gram projection and the two inequalities (16.10)--(16.11) can be bounded
without first solving the finite LP.

Several tempting two-layer choices fail before that point.  If the chosen support makes the NO
indicator an affine function of `C_t` (for example, one constant-`C_t` YES layer and one
`C_t=0` boundary layer), then `b` already lies in `V_D` once the degree-two row is present.  In that
case `g=0`.  More generally, any base law supported where `b` is a low-degree function of active
pair count, occupied complementary-pair count, collision count, or another existing orbit row
recreates exactly the forbidden low-statistic collapse.

## 5. Endpoint audit

### `q=5`

Here `m=K=2`, but the feature rank is not bounded by two.  The number of slots is fixed while the
query multiplicities `(alpha,beta)` in (16.1) grow with `D`; their falling-factorial polynomials
produce new functions of the two split states.  The exact finite ranks already archived are, for
example, `1,3,4,8,10,16` at cutoffs `D=2,3,4,5,6,7` in the relevant small-`N` ranges.  Thus (16.5)
has a genuinely growing projection space even at the small alphabet endpoint.

For every fixed `N,D`, (16.4)--(16.6) is a legal exact coefficient formula.  The phase-14 and
phase-15 exact LP sweeps show that *some* selective signed laws have correlation above `2/3` at all
sampled `D=floor/ceil(sqrt N)` cases through `N=12`, including the natural tail gate; they do not
provide a formula-defined sequence `pi_N`.  The intermediate-constant sweep also shows sharp
integer-cutoff oscillations.  Therefore:

- legality, zero mass, `l1`, and exact moment annihilation: **PASS conditionally on any chosen
  positive legal `pi` with `g!=0`**;
- a uniform `D=c sqrt(N)` band with correlation `>2/3`: **OPEN**;
- non-negligible mass at `C_t=omega(N)` (or the sharper chosen tail scale): **OPEN uniformly**, though
  finite target-scale instances pass;
- avoidance of a one-dimensional statistic: **not automatic** and must be proved for the eventual
  `pi_N`; two-layer laws can fail by `g=0`.

### `q=N`

Take `K=Theta(N^(2/3))` in the variable-total simplex.  The legal support contains balanced split
histograms with `C_t=Theta(N^(4/3))` and the full distributed NO boundary.  Equations
(16.1)--(16.8) remain well defined at the desired cutoff `D=Theta(N^(2/3))` and, unlike the faithful
assignment determinant, impose no `L=O(sqrt N)` injectivity cost: the columns are histograms
themselves, not a required injective encoding of all permutations.

This removes the phase-15 structural cap but proves no correlation.  A base measure concentrated
on one NO layer and one balanced YES layer is killed by the degree-two `C_t` row, while a product
activation law risks reducing the residual to the active-count OR dual.  No formula-defined
nonproduct `pi_{N,N}` is presently known for which (16.10) holds and (16.11) places constant mass at
`C_t=Theta(N^(4/3))`.  Thus the `q=N` correlation, high-tail, and uniform-band gates are **OPEN**.

## 6. Gate ledger

| Gate | Selective projection law |
|---|---|
| actual `F_gamma` rows only | **PASS** by (16.1)--(16.7) |
| arbitrary low-order cylinders retained | **PASS as a capability**; they are not automatically annihilated |
| legal orbits | **PASS** when `pi` has legal support |
| zero total mass | **PASS** because the constant row is projected out |
| unit `l1` | **PASS** by (16.6) when `g!=0` |
| exact degree-`<D` annihilation | **PASS** in the stated phase-12 formula scope |
| genuinely nonseparable coefficient law | **CONDITIONAL** on an explicit nonproduct choice of `pi` |
| correlation strictly above `2/3` | **OPEN**; equivalent to (16.10) |
| constant high-`C_t` mass | **OPEN**; equivalent to a lower bound in (16.11) |
| `q=5`, `D=Theta(sqrt N)` | finite evidence only; no uniform `pi_N` |
| `q=N`, `D=Theta(N^(2/3))` | legal formal construction, but correlation/tail bounds absent |
| one formula for all odd `q` | **OPEN** |

## 7. Next minimum obligation

The next proposer must give a formula-defined family of positive legal measures `pi_{N,q}` (not an
LP output and not `|W_*|`) and prove, for one constant `c>0` across the endpoint regimes,

```text
D >= c min{sqrt(N) q^eta, N^(2/3)},
3 <g,g>_pi > ||g||_{1,pi},
sum_{C_t>=T_{N,q}} pi_H |g_H| >= c ||g||_{1,pi},                  (16.13)
```

with `T_{N,5}=omega(N)` and `T_{N,N}=Theta(N^(4/3))` (or the exact project threshold adopted by
the parent node), while showing that `b` is not a low-degree function of any prohibited scalar
statistic on the support.  Analytically diagonalizing the finite Gram matrix (16.4) is useful only
insofar as it proves these three inequalities; merely naming an orthogonal-polynomial basis does
not discharge them.

No distinct Rule-8 escape was analyzed in this pass.  No `PROVED`, `CERTIFIED*`, `NUMERICAL`, or
`REFUTED` status is claimed.
