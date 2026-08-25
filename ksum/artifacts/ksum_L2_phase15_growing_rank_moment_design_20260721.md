# k-Sum L2 phase-15 proposer audit — growing-rank determinant/OA moment designs

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.growing-rank-moment-design`  
Tier: proposer only; no independent review  
Scope: faithful determinant and orthogonal-array designs defined below; no DAG status change

## Decision

**B — the natural growing-rank determinant/OA coefficient law overkills the moment space.** It
does avoid the phase-14 active-count collapse: its profiles contain genuinely different split
types, and its coefficients depend on a full assignment/permutation. It also gives an exact
all-low-moment cancellation identity. However, the same identity annihilates *every* low-order
coordinate-cylinder function. Since the NO label is an AND of the local boundary indicators, a
standard degree-`O(sqrt L)` polynomial for AND then forces normalized correlation below `2/3` once
the cancellation strength exceeds `O(sqrt L)`.

For the unweighted sign determinant the loss is explicit:

`corr = 2 |det Z|/L! <= 2 L^(L/2)/L!`.

At `q=5`, only `L<=2` assignment coordinates exist and the nonzero determinant measure cancels
only constants, not the required `Theta(sqrt N)` band. At large `q`, a faithful injective orbit
encoding also requires `N=Omega(L^2)`, hence `L=O(sqrt N)` before the correlation obstruction is
even applied. The capped target is `Theta(N^(2/3))`.

This is a scoped failure of determinant/OA cancellation through full coordinate marginals, not a
failure of an arbitrary coefficient law orthogonal only to the actual orbit-moment row space.

## 1. Exact cross-injection tensor system

Let `m=(q-1)/2` be the number of nonfixed complementary value-pair types. Represent a histogram by
an ordered slot list `tau_1,...,tau_m`, where `tau_i=(r_i,u_i)` and unused slots are `(0,0)`. For a
query pattern `kappa=(alpha,beta)`, put

`v_kappa(tau)=A_{alpha,beta}(r,u)=((r)_alpha(u)_beta+(r)_beta(u)_alpha)/2`.

For `boldkappa=(kappa_1,...,kappa_rho)`, define the injection tensor

```text
T_boldkappa(H)
  = sum_{iota:[rho]->[m] injective}
      product_{h=1}^rho v_{kappa_h}(tau_{iota(h)}).       (15.1)
```

If `d=sum_h(alpha_h+beta_h)`, the phase-12 orbit row is

`F_boldkappa(H)=T_boldkappa(H)/((m)_rho (N)_d)`.           (15.2)

The coefficient obligation is therefore

`sum_H W(H) T_boldkappa(H)=0` whenever `d<D`.              (15.3)

Equation (15.1) includes the pure-side rows as well as the cross rows. If every
`alpha_h,beta_h>=1`, all terms vanish on the NO boundary, as in phase 14. The general `K<m` and
`rho>=3` form of (15.2) has not yet passed the independent finite gates noted on the parent node;
it is used here only as a proposer identity.

## 2. Faithful growing-rank assignment family

Choose `L<=K` variable occupied pair slots and `L` positive totals `s_1,...,s_L`. For every row
template `i` and total-column `j`, choose a legal unordered split

`tau_{ij}=(r_{ij},s_j-r_{ij})`, `0<=r_{ij}<=s_j/2`.

The profile indexed by `pi in S_L` is

`H_pi={tau_{i,pi(i)}:1<=i<=L} union H_fix`,                (15.4)

where `H_fix` consists of `K-L` fixed unsplit occupied pairs and

`sum_j s_j + occupancy(H_fix)=N`.

Thus every permutation is automatically legal and has exactly the same total occupancy. The cell
array is chosen so that the resulting histograms are distinct and the selected cells contain a
growing number of genuinely different split types. This injectivity is the **faithful** condition;
it prevents opposite permutation signs from being silently collapsed before `l1` normalization.

Let `M` be an `L x L` scalar matrix of rank `r<L` and define

`mu(pi)=sgn(pi) product_i M_{i,pi(i)}`.                     (15.5)

The raw mass is `sum_pi mu(pi)=det M=0`. Its exact `l1` norm under the faithful condition is

`sum_pi |mu(pi)|=per(|M|)`.                                (15.6)

## 3. Complementary-minor annihilation identity

Let a function `g(pi)` depend only on the assignments of a row set `I`, `|I|=rho`. Expanding the
sum over the selected columns `J` gives

```text
sum_pi mu(pi) g(pi)
  = sum_{J:|J|=rho} sum_{sigma:I->J bijective}
      sgn(sigma;I,J) g(sigma)
      product_{i in I} M_{i,sigma(i)} det M[bar I,bar J].  (15.7)
```

Every complementary minor in (15.7) has size `L-rho`. It is zero when `L-rho>rank(M)=r`.
Consequently the signed assignment law annihilates every cylinder depending on fewer than

`D_0=L-r`                                                   (15.8)

rows.

Each summand of (15.1) involving the determinant-controlled slots depends on at most `rho<=d`
rows; fixed fillers contribute only scalar factors. Therefore (15.7) proves (15.3) for every orbit
row of query degree `d<D_0`, including mixed and pure-side rows. This is an exact full-band
identity, not a reduction to `C_t`, collision count, or the number of active pairs.

## 4. Exact correlation formula

Let

`Z_{ij}=1[tau_{ij} is NO]=1[r_{ij}=0]`.                    (15.9)

A profile `H_pi` is NO exactly when `product_i Z_{i,pi(i)}=1`. Hence its signed NO mass is

`sum_{pi:NO} mu(pi)=det(M circ Z)`,                         (15.10)

where `circ` is entrywise product. With labels `+1` on YES and `-1` on NO and `det M=0`, the
normalized correlation is exactly

`corr(mu)=2|det(M circ Z)|/per(|M|)`.                       (15.11)

For the simplest full alternant `M=all-ones`, `rank(M)=1` and `D_0=L-1`. Equation (15.11) becomes

`corr=2|det Z|/L! <= 2 L^(L/2)/L!`,                        (15.12)

by Hadamard's inequality. This decays as
`exp(-0.5 L log L+O(L))`, even if `Z` is chosen to maximize its determinant.

## 5. The OA/low-rank hard boundary, without active-count collapse

The loss is not peculiar to equal weights. From (15.7), the normalized signed law is orthogonal to
all cylinder functions involving fewer than `D_0` row coordinates. On a selected permutation set,
write `z_i(pi)=Z_{i,pi(i)}`. The NO indicator is

`NO(pi)=AND_{i=1}^L z_i(pi)`.                               (15.13)

A constant-error polynomial for AND on `L` Boolean variables has degree `O(sqrt L)`. Expanding it
into multilinear monomials gives a sum of cylinder functions, each depending on only
`O(sqrt L)` rows. If `D_0` is larger than the approximant degree, (15.7), zero mass, and unit `l1`
give

`|corr(mu)| <= ||f_t-P||_infinity`,                         (15.14)

which can be made below `2/3` by a fixed margin.

Exactly the same argument applies to any faithful signed orthogonal array whose marginals vanish
on all sets of at most `t` row coordinates: constant correlation requires

`t=O(sqrt L)`.                                              (15.15)

This is not an active-count argument. The local split types and their moment vectors may all be
different, and `mu` need not be symmetric under rows. The failure comes from annihilating the much
larger cylinder space rather than only the orbit tensors actually required by (15.3).

## 6. Legality and injectivity cost

For fixed total `s_j`, column `j` has at most `floor(s_j/2)+1` unordered split states. A faithful
map `pi -> H_pi` of all `L!` permutations therefore requires the counting condition

`product_j (floor(s_j/2)+1) >= L!`.                         (15.16)

Since `sum_j s_j<=N`, AM-GM gives

`(N/(2L)+1)^L >= L!`,                                      (15.17)

and hence `N=Omega(L^2)` and `L=O(sqrt N)`. Requiring distinct totals and a cellwise-decodable row
label gives the same bound directly. Thus the faithful determinant's raw exact band
`D_0<=L` is already only `O(sqrt N)`. At the capped endpoint the required band is
`Theta(N^(2/3))`.

## 7. Endpoint and crossover checks

### `q=5`

Here `m=K=2`, so an assignment determinant has `L<=2`. A nonzero singular `2 x 2` weight matrix has
rank at least one, hence `D_0=L-r<=1`: it cancels total mass but no nonconstant query row. A choice
of `Z` with one NO permutation and one YES permutation can give correlation one and legal profiles
with `C_t=Theta(N^2)`, but it still cannot supply the required `Theta(sqrt N)` annihilation band.
Therefore this determinant mechanism has no valid `q=5` specialization.

### Large `q`

One may take `L=Theta(sqrt N)`, distinct totals `s_j=Theta(sqrt N)`, diagonal NO cells, and
off-diagonal split cells with products `Theta(N)`. This is legal and faithful after fixing small
constant factors. A uniformly random permutation has at most `L/2` diagonal fixed points with
probability at least `1-2/L`, so a constant (indeed tending-to-one) fraction of the absolute mass
lies at

`C_t=Theta(LN)=Theta(N^(3/2))`,

well above the required `Theta(N^(4/3))` tail. High-`C_t` mass is therefore compatible with the
support. Nevertheless, (15.12) destroys correlation for the full alternant, while (15.14)-(15.17)
cap every faithful low-rank/OA variant at `O(sqrt N)` rather than `Theta(N^(2/3))`.

### Uncapped and crossover regimes

With `K<=m`, always `L<=K`. In the uncapped range the target is
`D_*=sqrt(N) q^eta`, whereas a faithful determinant has `D_0<=min{K,O(sqrt N)}` and a
constant-correlation OA has effective strength only `O(sqrt L)`. Neither reaches `D_*` for the
required odd `q>=5`. At the crossover and capped range, the gap increases to
`Theta(N^(2/3))` versus `O(sqrt N)`.

## 8. Gate ledger

| Gate | Result for faithful determinant/OA designs |
|---|---|
| genuinely different split types | PASS by the cell array in (15.4) |
| exact total occupancy and odd-`q` pair budget | PASS when `L<=K<=m` and the displayed totals sum to `N` |
| zero total mass | PASS because `rank(M)<L` gives `det M=0` |
| unit `l1` | PASS after division by `per(|M|)` in the faithful nonzero case |
| all orbit moments below `D_0` | PASS exactly by complementary minors (15.7) |
| no active-count collapse | PASS; the coefficient and profiles depend on the full permutation |
| correlation above `2/3` | FAIL for growing cancellation strength by (15.12) or (15.14) |
| `q=5` band | FAIL: `D_0<=1` |
| capped/crossover band | FAIL: faithful legality gives `D_0=O(sqrt N)`; OA correlation is no better |
| constant high-`C_t` absolute mass | compatible; an explicit legal scaling is given above |
| all `N,q` endpoints with one formula | FAIL |

## 9. Hard boundary and Rule-8 escape

The proposer-tier hard boundary is:

> Any faithful determinant or orthogonal-array construction whose moment cancellation comes from
> vanishing all low-order assignment-coordinate marginals either has an explicit determinant
> correlation loss or is defeated by the `O(sqrt L)` approximant to the local-boundary AND.
> Faithful orbit encoding additionally forces `L=O(sqrt N)`. This remains true even with genuinely
> different split types and without any active-count reduction.

The untested escape is to annihilate only the actual span of the tensors (15.1), while deliberately
*not* annihilating arbitrary coordinate cylinders. It would need growing occupancy-feature rank
even when `K=2`, so that the `q=5` target-scale finite feasibility can be represented, and then a
coupling across growing `K` that preserves correlation. This is a genuinely different mechanism;
no analysis of it was started here. Suggested node id, to be registered before any commission:

`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`.

No `PROVED`, `CERTIFIED*`, or `REFUTED` conclusion is claimed.
