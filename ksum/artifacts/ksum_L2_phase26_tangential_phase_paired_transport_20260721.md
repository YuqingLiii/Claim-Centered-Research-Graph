# k-Sum L2 phase-26 analytic/numerical proposer — tangential phase-paired transport

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.tangential-phase-paired-transport`

Scope: one explicit two-atom phase pair, one explicit one-parameter exposed-phase family, the exact
`m=b+O(1)` birth edge, and the associated WKB-normalized right inverse.  No broad support search or
LP is performed.

Tier: proposer derivation plus bounded exact/numerical checks; no independent review and no
completion-tier claim.

## Decision

**Decision B for the explicit minimal construction; the controlling node remains OPEN.**

The canonical two-atom pair cannot cancel even two adjacent birth rows: after exact cancellation
of row `b`, its normalized row-`b+1` defect stays constant for separated transition points and
grows linearly in `D` if one point lies at `m=b+O(1)`.  The exact birth-edge operator is a Pascal
matrix.  Its unique square right inverse has `l1 -> TV` norm at least

```text
2^M-1=exp(Theta(D))                                     (26.1)
```

when `M=Theta(D)` birth rows are corrected.  Consequently an `o(D^{-3})` canonical defect is far
too large: this inverse requires an exponentially small defect merely to keep the correction TV
bounded.

An explicit continuous tangential phase family can pair all leading WKB phases.  However, unique
saddle localization forces its positive and negative densities to agree pointwise if the
WKB-normalized defect is `o(D^{-3})`.  Their signed transition mass, and therefore their possible
constant YES/NO correlation transfer, then also tends to zero.  Keeping constant correlation or
constant unmatched transition mass leaves an `Omega(1)` normalized defect.

This refutes the displayed minimal pair/family, not every possible nonseparable transport in the
node.  A more elaborate support could try to store correlation on phase-subexposed strata; that
distinct escape is only named in Section 10.

## 1. One explicit two-atom exposed-phase pair

On a regular tangential face use the Phase-25 dominant row

```text
K_{h,b}(sigma,m)
 =(m)_b(N sigma-m)_h/(N)_{h+b},                          (26.2)
```

where `h=alpha D+O(1)`, `b=beta D+O(1)`, and `m=lambda D+O(1)` with
`0<beta<lambda`, `alpha+beta<1`.

Choose two legal transition points

```text
x_+=(sigma_+,lambda_+),
x_-=(sigma_-,lambda_-),       lambda_+ != lambda_-.     (26.3)
```

For the exact adjacent-row test below, also choose `alpha_0>max(lambda_+,lambda_-)`, so the reverse
orientation in (25.3) is exactly zero at both points and (26.2) is the full symmetric orbit row up
to its common factor.

For one chosen direction `(alpha_0,beta_0)`, their leading phases can be paired by setting

```text
alpha_0 log(sigma_+/sigma_-)
 +F(lambda_+,beta_0)-F(lambda_-,beta_0)=0,              (26.4)
```

where `F` is the Phase-25 entropy phase.  Exact weights can then cancel the finite row `b_0`:

```text
w_+=1,
w_-=-K_{h,b_0}(x_+)/K_{h,b_0}(x_-).                    (26.5)
```

This is the minimal tangential phase-paired candidate.

## 2. Exact adjacent-row obstruction

The exact factorial recurrence gives

```text
K_{h,b+1}(sigma,m)/K_{h,b}(sigma,m)
 =(m-b)/(N-h-b).                                       (26.6)
```

The denominator is row-dependent but support-independent.  Therefore, after (26.5) cancels row
`b_0`, the absolute row-`b_0+1` residual normalized by the plus atom is exactly

```text
Delta_adj
 =|1-(m_- -b_0)/(m_+ -b_0)|.                           (26.7)
```

Tangential tuning of `sigma_+` and `sigma_-` disappears completely from (26.7).

For the explicit values

```text
alpha_0=0.65,       beta_0=0.15,
lambda_+=0.35,      lambda_-=0.55,
sigma_+=0.5114929978,   sigma_-=0.45,
```

equation (26.4) holds (to the printed precision), while the defect is

```text
Delta_adj=1                                                   (26.8)
```

for every `D` making the displayed quantities integral.  It is not `o(D^{-3})`.

At the exact birth edge, take

```text
m_+=b_0+s,       s=O(1),       m_-=lambda_-D.
```

Then

```text
Delta_adj
 =|1-(lambda_- -beta_0)D/s+O(1)|
 =Theta(D).                                               (26.9)
```

Thus the birth edge worsens, rather than repairs, a two-point phase pair.

The WKB version says the same thing.  Since

```text
partial_beta F(lambda,beta)=log(lambda-beta),           (26.10)
```

two distinct `lambda` values that are phase-paired at `beta_0` acquire a constant relative
amplitude change when `b` increases by one.  Matching both the phase and its first `beta`
derivative forces `lambda_+=lambda_-`; then (26.4) also forces `sigma_+=sigma_-`, so the pair is
orbit-identical and carries no useful transport.

## 3. Exact birth operator and right inverse

After dividing the birth row by `b!`, its transverse coefficient is exactly

```text
P_{b,m}=(m)_b/b!=binom(m,b),       m>=b.                (26.11)
```

Restrict first to rows and transition occupancies `b,m=1,...,M`.  The square operator `P_M` is
upper triangular with unit diagonal.  Its inverse is explicit:

```text
(P_M^{-1})_{m,b}
 =(-1)^(b-m) binom(b,m),       b>=m.                    (26.12)
```

Indeed,

```text
sum_{k=m}^b (-1)^(k-m) binom(k,m)binom(b,k)
 =1_{b=m}.                                               (26.13)
```

For a defect concentrated in the last birth row `b=M`, the correction coefficients are

```text
x_m=(-1)^(M-m)binom(M,m),       m=1,...,M.              (26.14)
```

Their total variation is

```text
sum_{m=1}^M |x_m|=2^M-1.                                (26.15)
```

Hence

```text
||P_M^{-1}||_{l1 -> l1} >=2^M-1.                        (26.16)
```

On a fixed tangential fiber, the remaining factor `(N sigma-m)_h` is a nonzero column scaling;
after the Phase-25 WKB normalization it is bounded above and below on a phase-tie window.  Such
bounded diagonal scalings do not remove the exponential lower bound (26.16).

This identifies the requested right inverse and its norm.  It is the opposite of uniform.

## 4. Consequence for an `o(D^{-3})` canonical defect

Let `M=cD+O(1)` for some `c>0`, as required to correct a positive fraction of the minority query
degrees.  If a WKB-normalized canonical construction has birth residual `r_D`, the Pascal
correction can obey `||P_M^{-1}r_D||_1=o(1)` uniformly in its direction only if

```text
||r_D||_1=o(2^{-cD}).                                   (26.17)
```

The weaker target

```text
||r_D||_1=o(D^{-3})                                     (26.18)
```

does not control the correction: the worst-case upper scale is

```text
(2^{cD}-1)o(D^{-3}),                                    (26.19)
```

which diverges exponentially.  This is a norm statement, not an extrapolation from condition
numbers.

One could evade (26.17) only if the canonical residual were proven to lie in a special stable
subspace of the Pascal inverse.  The minimal pair fails this possibility explicitly because its
defect already occupies adjacent birth rows with sizes (26.8)-(26.9).

## 5. An explicit exposed tangential family

The two-point failure motivates a moving family.  Choose

```text
sigma(lambda)=sigma_0 exp(-c lambda),
sigma_0=0.8,       c=1,
lambda in [0.25,0.75].                                 (26.20)
```

The other slot carries total `1-sigma(lambda)`, so this is a legal regular tangential path for
large `N`.  Its one-slot WKB phase is

```text
S_{alpha,beta}(lambda)
 =alpha[log sigma_0-c lambda]+F(lambda,beta).           (26.21)
```

The exposed point satisfies

```text
partial_lambda S
 =-alpha c+log(lambda/(lambda-beta))=0,

lambda_*(alpha,beta)
 =beta/(1-exp(-alpha c)).                               (26.22)
```

Moreover,

```text
partial_lambda^2 S(lambda_*)
 =-beta/[lambda_*(lambda_*-beta)]<0,                    (26.23)
```

so every direction whose `lambda_*` lies in the interval has a unique nondegenerate exposed
saddle.  For example,

```text
alpha=0.5, beta=0.15:
lambda_*=0.3812241124,
sigma(lambda_*)=0.5464198385,
S''(lambda_*)=-1.7016795361.                            (26.24)
```

This is an explicit minimal phase-foliating family, not an existence ansatz.

## 6. Density pairing on the exposed family

Place positive and negative WKB densities `rho_+(lambda)` and `rho_-(lambda)` on the same path.
After including the Phase-25 order-one amplitude `A_{alpha,beta}(lambda)`, Laplace's method gives

```text
I_+-I_-
 =e^{D S(lambda_*)} sqrt(2 pi/(D|S''(lambda_*)|))
  A_{alpha,beta}(lambda_*)
  [rho_+(lambda_*)-rho_-(lambda_*)]
  (1+O(D^{-1})).                                        (26.25)
```

Define the canonical WKB-normalized defect by

```text
delta_D(alpha,beta)
 :=e^{-D S(lambda_*)}sqrt(D)[I_+-I_-].                  (26.26)
```

Because `(alpha,beta) -> lambda_*` covers the interior of the path, the uniform requirement

```text
sup_{alpha,beta}|delta_D(alpha,beta)|=o(D^{-3})         (26.27)
```

forces

```text
rho_+(lambda)-rho_-(lambda)=o(D^{-3})                  (26.28)
```

uniformly on every compact exposed subinterval.  Therefore the signed transition mass on that
subinterval is also `o(D^{-3})`.

The family can achieve exponentially small quadrature defect by taking the two densities equal,
but then its signed mass is zero.  Conversely, a constant signed mass difference—needed to
balance a constant NO mass and retain constant label correlation—creates an `Omega(1)` normalized
defect for at least one exposed query direction.

All points on (26.20) have `m=Theta(D)` and

```text
C_t=Theta(ND)=omega(N),                                (26.29)
```

so constant unsigned mass there would satisfy the desired high-tail condition.  The failure is
not tail location: exact phase pairing removes the signed mass needed for correlation.

## 7. Correlation and constant-row accounting

Every transition and bulk point in this construction is YES.  Let `M_tr` be their total signed
mass and let `M_0` be signed mass on NO.  Constant-row annihilation requires

```text
M_tr+M_0=0.                                             (26.30)
```

With labels `+1` on transition and `-1` on NO, the unnormalized label correlation is

```text
Corr_signed=M_tr-M_0=2M_tr.                             (26.31)
```

Thus constant normalized correlation requires `M_tr=Theta(1)`.  But (26.28) gives
`M_tr=o(D^{-3})` for the exposed family whenever the canonical defect meets (26.27).  Adding a
constant NO mass would then violate (26.30).

The canonical family therefore cannot simultaneously have:

```text
canonical defect=o(D^{-3}),
bounded correction TV,
constant correlation,
constant high-tail signed mass.                         (26.32)
```

It can retain constant *unsigned* tail mass only by pairing equal positive and negative YES
density, which contributes no correlation.

## 8. Two-slot rows do not repair the minimal family

The obstruction already occurs in the one-slot row subspace, which is part of the full orbit
feature span.  Adding two-slot rows can only add annihilation constraints.  In particular:

- the adjacent recurrence (26.6) remains an exact one-slot constraint;
- the Pascal inverse is a principal transverse block of the full moment operator;
- two-slot polarization cannot change the fact that unique exposed saddles read off the local
  signed density in (26.25).

Therefore the failure of this explicit pair/family is not an artifact of omitting the `rho=2`
rows.  A successful construction would need a signed component invisible to the exposed
one-slot phases while still interacting with the low-index and two-slot equations.

## 9. Bounded checks

Command:

```text
python ksum/tools/ksum_l2p26_phase_pair_right_inverse_check.py
```

Driver SHA-256:

```text
27fb0fc6ce7d06590d5773791acb32a601f5882963f6e9562c7b1c7b9ae0fb5f
```

Raw log:
`ksum/artifacts/logs_ksum_L2p26_phase_pair_20260721/run.json`

The bounded run checked:

```text
D=100,200,400,800:
  separated two-atom adjacent defect =1 at every D;
  birth-edge s=2 defect             =19,39,79,159;

M=4,8,12,16,20:
  Pascal inverse lower bound        =15,255,4095,65535,1048575.   (26.33)
```

It also evaluated the exposed saddle (26.24).  These are independent exact-ratio/value checks of
the displayed construction.  They do not test a broader support family.

## 10. New escape generated and not tested

The failure identifies one distinct escape:

> **phase-subexposed correlation reservoir** — place constant signed YES mass on strata that are
> never maximizers of any positive-`beta` WKB phase, cancel the exposed transition/bulk phases
> separately, and couple the reservoir to NO only through fixed-index and two-slot rows.

This route is only named.  It was not constructed, searched, or tested.  Under DAG Rule 8 it must
receive a canonical node before any work is commissioned.

## 11. Gate ledger

| obligation | result |
|:---|:---|
| explicit minimal phase pair | CONSTRUCTED: (26.3)-(26.5) |
| adjacent birth rows | FAIL exactly: (26.7)-(26.9) |
| exact birth right inverse | DERIVED: Pascal inverse (26.12) |
| uniform inverse norm | FAIL: at least `2^M-1` |
| explicit exposed family | CONSTRUCTED: (26.20)-(26.24) |
| uniform phase pairing | forces local density equality |
| canonical defect `o(D^-3)` | incompatible with constant signed mass on this family |
| constant correlation | FAIL for this family |
| constant unsigned high tail | possible but correlation-neutral |
| full nonseparable node | NOT ADJUDICATED |

## 12. Scoped conclusion

The minimal tangential phase-paired strategy fails twice: locally, adjacent birth rows have an
exact nonvanishing defect; globally, the birth right inverse is exponentially ill-conditioned.
The smooth exposed-family version can make its defect tiny only by matching positive and negative
density pointwise, which removes the signed transition mass needed for constant correlation.

This is Decision B for the explicit construction and a scoped obstruction to any method relying
on a uniform Pascal-block inverse.  It is not a global refutation of the controlling node.  The
node remains open, and no `PROVED`, `CERTIFIED*`, or `REFUTED` claim is made.
