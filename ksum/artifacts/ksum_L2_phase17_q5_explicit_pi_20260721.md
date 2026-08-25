# k-Sum L2 phase-17 proposer analysis — an explicit positive q=5 base law

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`  
Tier: proposer proof plus numerical diagnostics; no independent review and no DAG status claim

## Decision

**B — the most canonical explicit Hahn/Dirichlet base law is not the missing witness.**

There is a completely formula-defined, strictly positive legal law: push the symmetric
Dirichlet--multinomial law on the four nonzero q=5 symbol counts to the wreath-product orbit
space, conditioned on both complementary value pairs being occupied.  At `alpha=1` this is just
uniform measure on legal ordered compositions, hence its orbit weight is the orbit size.  It is
not an LP output and does not use `|W_*|`.

For this law the first nonconstant cutoff `D=3` can be analysed exactly.  Its phase-16 projection
residual has limiting correlation

```text
48 / (48 + 90*pi/7 - 192/(7*sqrt(7)))
  = 0.6151883860... < 2/3.                                      (17.1)
```

At the same time, for every threshold `T_N=omega(N)` with `T_N=o(N^2)`, the residual's absolute
mass above `C_t>=T_N` tends

```text
(24 + 90*pi/7 - 192/(7*sqrt(7)))
 / (48 + 90*pi/7 - 192/(7*sqrt(7)))
  = 0.6924058069....                                             (17.2)
```

Thus this law fails because the YES-side projection has too much sign variation, not because it
loses the high-`C_t` tail.

At the actual target cutoffs `D=ceil(sqrt(N))`, direct weighted projections for
`N=8,12,16,20,24,32,40,50,64` all have correlation below `2/3`; it is about `0.33` at `N=64`,
while the `C_t>=N^(3/2)/4` residual mass is about `0.55`.  These target-scale results are
**NUMERICAL diagnostics only**.  Equation (17.1) rigorously rejects the fixed `D=3` residual; it
does not by itself prove monotonicity in `D` or an asymptotic no-go for every
`D=c sqrt(N)`.  Accordingly this memo rejects this explicit base law as the next proof witness,
but does not refute the controlling selective-kernel node.

## 1. Formula-defined positive legal law

Write the four nonzero q=5 counts as

```text
n=(n_1,n_2,n_3,n_4),
n_1+n_2+n_3+n_4=N,
n_1+n_2>=1,  n_3+n_4>=1.                                        (17.3)
```

The two complementary pairs are `(1,2)` and `(3,4)`.  Let `G=S_2 wr S_2` swap within either pair
and swap the two pairs.  For `alpha>0`, put on an orbit `H=G n`

```text
pi_{N,alpha}(H)
  = Z_{N,alpha}^{-1}
    sum_{n' in H} product_{j=1}^4 Gamma(n'_j+alpha)/n'_j!.        (17.4)
```

All omitted Dirichlet--multinomial factors depend only on `N,alpha` and cancel in the
normalisation.  Therefore (17.4) is strictly positive on every legal orbit and is invariant under
all orbit symmetries.  For `alpha=1`, every ordered legal composition has the same mass, so

```text
pi_N(H)=|H|/Z_N,
Z_N = binom(N+3,3)-2(N+1) = (N-1)(N+1)(N+6)/6.                   (17.5)
```

This is the boundary-deleted symmetric Dirichlet--multinomial/Hahn law.  The deletion is exactly
the legal `K=2` condition in the archived finite orbit model; no illegal empty-pair orbit is added.

The NO set consists of choosing one nonzero coordinate from each pair and splitting `N` positively
between them.  Hence it has `4(N-1)` ordered compositions and

```text
delta_N := pi_N(NO)=24/((N+1)(N+6)) = 24/N^2+O(N^-3).            (17.6)
```

## 2. Exact asymptotic projection at `D=3`

For weighted degree `<3`, the actual q=5 orbit-feature span is generated, on the hyperplane
`sum n_j=N`, by

```text
1,
A_N=sum_j (n_j)_2,
B_N=n_1 n_2+n_3 n_4=C_t.                                        (17.7)
```

This follows directly from the phase-16 slot product: the raw patterns are `(0,1),(0,2),(1,1)`
and the injection of two `(0,1)` patterns; after using the fixed total, their rank is three.

Put `x_j=n_j/N`,

```text
A=sum_j x_j^2,  B=x_1x_2+x_3x_4.
```

Uniform legal compositions converge by Riemann sums to `Dirichlet(1,1,1,1)`; deleting the two
pair-empty faces changes neither this interior limit nor the scaled Gram matrix.  Conditional on
NO, the limit is the average of the four line segments joining one vertex of the first pair to one
vertex of the second.  On that boundary law,

```text
E_boundary[1,A,B]=(1,2/3,0).                                    (17.8)
```

Under the interior Dirichlet law the Gram matrix of `(1,A,B)` is

```text
G = [[1,    2/5,   1/10],
     [2/5,  6/35,  4/105],
     [1/10, 4/105, 1/84]],     det(G)=1/55125.                   (17.9)
```

The scaled projection polynomial is consequently

```text
h(x) = (1,A,B) G^{-1} 24(1,2/3,0)^T
     = -60+420A-840B
     = 60[-1+7((x_1-x_2)^2+(x_3-x_4)^2)].                       (17.10)
```

If `p_N` is the `L_2(pi_N)` projection of the NO indicator onto (17.7), finite-dimensional Gram
convergence gives, uniformly on the simplex,

```text
p_N(n)=N^-2 h(n/N)+o(N^-2).                                     (17.11)
```

For the residual `g_N=b-p_N`, orthogonality and `b^2=b` yield

```text
N^2 ||g_N||_2^2 -> 24.                                          (17.12)
```

The NO contribution to `N^2||g_N||_1` tends 24, while the YES contribution tends
`E_Dir |h|`.  It remains only to integrate (17.10).

Let `s=x_1+x_2`, `d_1=x_1-x_2`, and `d_2=x_3-x_4`.  Under the uniform Dirichlet law the joint
density in `(s,d_1,d_2)` is `3/2` on

```text
0<s<1, |d_1|<s, |d_2|<1-s.
```

After integrating out `s`, `(d_1,d_2)` has density
`(3/2)(1-|d_1|-|d_2|)` on the diamond `|d_1|+|d_2|<=1`.  The negative region of
`7(d_1^2+d_2^2)-1` is the full circle of radius `1/sqrt(7)`, which lies inside that diamond.  A
quarter-circle polar integral gives

```text
J := E[(1-7(d_1^2+d_2^2))_+]
   = 3*pi/28 - 8/(35*sqrt(7)),
E[7(d_1^2+d_2^2)-1]=2/5,
E|h| = 60(2/5+2J)
     = 24+90*pi/7-192/(7*sqrt(7))
     = 54.0248800007....                                         (17.13)
```

Combining (17.12)--(17.13) with the exact phase-16 correlation formula proves (17.1).  In
particular `3||g_N||_2^2>||g_N||_1` is false for all sufficiently large `N` at `D=3`.

## 3. High-`C_t` tail at `D=3`

On the interior scale, `C_t=N^2 B`.  If `T_N=o(N^2)`, the set
`0<C_t<T_N` shrinks to the measure-zero set `B=0`; dominated convergence applied to (17.11) shows
that all of the limiting YES-side `|p_N|` mass lies above `T_N`.  If also `T_N=omega(N)`, this is
exactly a legal high-`C_t` threshold of the kind required by the parent node.  The NO residual has
`C_t=0`.  Therefore

```text
Tail_pi(T_N)
 -> E|h|/(24+E|h|)
  = 0.6924058069...,                                             (17.14)
```

which proves (17.2).  This separates the two phase-16 gates: the tail succeeds, but the residual
inequality fails.

## 4. Target-scale numerical gate

The diagnostic script constructs the actual q=5 feature rows of weighted degree `<D`, pushes
(17.4) to the unordered histogram orbits, performs the phase-16 weighted projection by SVD, and
checks weighted orthogonality.  For `alpha=1`:

| `N` | `D=ceil(sqrt(N))` | correlation | tail mass at `C_t>=N^(3/2)/4` |
|---:|---:|---:|---:|
| 8 | 3 | 0.6196 | 0.3088 |
| 12 | 4 | 0.6176 | 0.2605 |
| 16 | 4 | 0.6313 | 0.3266 |
| 20 | 5 | 0.4140 | 0.3954 |
| 24 | 5 | 0.4327 | 0.4245 |
| 32 | 6 | 0.4397 | 0.4568 |
| 40 | 7 | 0.3148 | 0.5220 |
| 50 | 8 | 0.3231 | 0.5354 |
| 64 | 8 | 0.3306 | 0.5478 |

Every reported weighted orthogonality residual is below `2e-16`.  The sawtooth comes from the
integer cutoff, as in phases 14--15.  Sensitivity runs for `alpha=1/2` and `alpha=2` show the same
overall failure at the sampled target scale, except for the isolated `alpha=1/2,N=16,D=4` value
`0.6814`; hence those runs are not an asymptotic exclusion of the full alpha family.

Provenance:

- driver: `ksum/tools/ksum_l2p17_q5_explicit_pi.py`, SHA-256
  `1ab0d61f4617644720934df59badee291d6171b7b612c3102eb37904f9a3d92d`;
- `alpha=1` JSON: `ksum/artifacts/logs_ksum_L2p17_q5_explicit_pi_alpha1_20260721.json`, SHA-256
  `ec15e5f7cf4f9ee6d15f33fdfb8f33e25f834e248a883aa2875a3026dcdd9885`;
- `alpha=1/2` JSON: `ksum/artifacts/logs_ksum_L2p17_q5_explicit_pi_alpha05_20260721.json`, SHA-256
  `c2839de1747534c00380328bdc9c4dbbaf4cbc52bf67a67e0285f5984892818a`;
- `alpha=2` JSON: `ksum/artifacts/logs_ksum_L2p17_q5_explicit_pi_alpha2_20260721.json`, SHA-256
  `7508a31c8e9a0c7d12308c1a16d2b6109248e1223b04e77121a1b9e03863452f`.

The JSON arithmetic is float64 and therefore numerical evidence, not a certificate.  The analytic
`D=3` calculation is independent of those floating-point values.

## 5. Exact scope and next obligation

### Established in this proposer memo

- (17.4) is a formula-defined, strictly positive law on every legal q=5 orbit.
- For `alpha=1,D=3`, the residual correlation has the strict asymptotic limit (17.1), so the
  phase-16 inequality fails for all sufficiently large `N`.
- For the same residual and every `omega(N)<<T_N<<N^2`, the high-`C_t` mass has the positive limit
  (17.2).
- At sampled `D=ceil(sqrt(N))`, the exact orbit-feature numerical projection fails correlation but
  retains substantial high-tail mass.

### Not established

- No monotonicity of the residual correlation as `D` grows is claimed.
- No asymptotic theorem at `D=c sqrt(N)` is proved for (17.4).
- The one exceptional finite `alpha=1/2` pass is neither extrapolated nor dismissed.
- No impossibility is claimed for other explicit positive legal measures.
- The controlling selective-kernel node remains OPEN and requires independent Rule-7 review before
  any completion-tier status.

The minimum useful continuation inside this node is to alter the base law so that its YES-side
projection has much smaller `L_1/L_2^2` while preserving the tail.  Merely changing a fixed
Dirichlet parameter does not look sufficient from the sensitivity runs, but this is evidence, not
an exclusion theorem.

No genuinely distinct route was generated or tested in this pass; therefore Rule 8 requires no
new node proposal from this memo.
