# k-Sum L2 phase-24 analytic proposer — stratified normal kernel

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.continuation-seeded-block-fekete.continuum-limit-remez-support-flow.stratified-boundary-jet-remez-system`

Scope: only the regular `q=5`, `K=2`, `D=kappa sqrt(N)` NO-face normal layer
`xi=D^2 C_t/N^2=Theta(1)`, its exact falling-factorial/WKB kernel, and necessary matching to the
NO face and bulk.  There is no finite support search and no DAG status adjudication here.

Tier: proposer derivation; no independent review and no completion-tier claim.

## Decision

**Decision C for the controlling node, with a sharp negative subdecision for a scalar-`xi`
ansatz.**  On every regular NO face (`sigma_i` bounded away from zero), the exact normal layer and
all one- and two-slot query kernels can be derived.  The layer is a *discrete falling-factorial
jet*, indexed by the minority occupancies `m_i in Z_{>=0}`, not a measure on `xi` alone.  Its
generating kernel is `(1+t_i)^{m_i}` times an explicit tangential WKB factor.

The NO trace and the coefficientwise bulk-to-normal matching law are also explicit.  They show,
however, that the four-sector template from Phase 23 does not yet close:

1. equal `xi` does not imply equal orbit kernels;
2. the fixed-`m` normal layer has no overlap with query directions having both exponents of order
   `D`;
3. those directions turn on at the additional scale `m=Theta(D)`, where
   `xi=Theta(D)`, between the normal layer and macroscopic bulk.

Thus this memo supplies the requested normal kernel and necessary matching conditions, but not a
solution or obstruction for the full node.  A distinct untested escape forced by the calculation
is named in Section 9 and is not tested here.

## 1. Regular NO-face coordinates

Write the two unordered complementary-pair slots as

```text
tau_i=(r_i,u_i),       s_i=r_i+u_i,       s_1+s_2=N.
```

On a regular NO face, orient each unordered slot so that

```text
m_i=min(r_i,u_i),      n_i=s_i=N sigma_i+O(1),
(r_i,u_i)=(m_i,n_i-m_i),
sigma_i in [delta,1-delta],   sigma_1+sigma_2=1.         (24.1)
```

NO is `m_1=m_2=0`.  If `m_i=O(1)`, then

```text
C_t=sum_i m_i(n_i-m_i)
   =N sum_i sigma_i m_i-O(1),
xi=D^2 C_t/N^2
  =kappa^2 sum_i sigma_i m_i+o(1).                       (24.2)
```

Conversely, on a regular face, bounded `xi` forces every `m_i=O(1)`.  Hence the normal coordinate
does not become continuous: its transverse variables are the integer pair `(m_1,m_2)`.

This statement deliberately excludes degenerating tangential corners `sigma_i -> 0`; Section 8
records why they require a separate scaling.

## 2. Exact one-slot falling-factorial identity

For a slot `tau=(m,n-m)`, the exact symmetric orbit coefficient is

```text
A_{a,j}(m,n-m)
 =((m)_a(n-m)_j+(m)_j(n-m)_a)/2.                        (24.3)
```

If `a>m`, which always holds eventually when `a=alpha D+O(1)`, `alpha>0`, and `m` is fixed,
then

```text
2 A_{a,j}(m,n-m)=(m)_j(n-m)_a.                          (24.4)
```

This is exact, not asymptotic.  In particular, the entire discrete transverse dependence is the
falling factorial `(m)_j`.  It automatically gives the support cutoff

```text
A_{a,j}(m,n-m)=0  when j>m and a>m.                    (24.5)
```

The exponential generating function in the fixed minority index is therefore

```text
sum_{j>=0} 2 A_{a,j}(m,n-m) t^j/(j!(n-m)_a)
  =(1+t)^m,                                              (24.6)
```

again exactly once `a>m`.  Equation (24.6) is the normal falling-factorial kernel before the
tangential WKB limit.

## 3. Tangential WKB factor

Let

```text
D=kappa sqrt(N)+O(1),       a=alpha D+O(1),
n=N sigma+O(1),             m,j=O(1),
alpha>0,                    sigma in [delta,1].          (24.7)
```

Using the common finite-query normalization `(N)_{a+j}`, define

```text
K^{N}_{alpha,j}(sigma,m)
 :=2 N^j A_{a,j}(m,n-m)/(N)_{a+j}.                       (24.8)
```

Uniformly on compact `alpha,sigma` ranges with `sigma>0`, expansion of the two gamma ratios gives

```text
K^{N}_{alpha,j}(sigma,m)
 =(m)_j sigma^a
   exp[-(alpha^2 kappa^2/2)(1/sigma-1)]
   (1+O(N^{-1/2})).                                     (24.9)
```

The fixed `m` first enters the exponential at order `a m/N=O(N^{-1/2})`; at leading order it
enters only through `(m)_j`.  It is convenient to name

```text
H_alpha(sigma)
 :=sigma^a exp[-(alpha^2 kappa^2/2)(1/sigma-1)].         (24.10)
```

The exact-factorial / WKB normal generating kernel is then

```text
K_alpha(sigma,m;t)
 :=sum_{j>=0} K_{alpha,j}(sigma,m)t^j/j!
 =H_alpha(sigma)(1+t)^m.                                (24.11)
```

Because `sigma^a` is exponentially selective when `a=Theta(D)`, a pointwise tangential limit is
taken on an exposed WKB face by dividing every row by `sigma_*^a`; this legal row rescaling does
not change the annihilating kernel.  Formula (24.9), rather than a prematurely chosen
`sigma_*`, is the invariant statement.

### Checkable logarithmic form

Before discarding lower order terms, (24.9) follows from

```text
log[N^j(n-m)_a/(N)_{a+j}]
 =a log sigma
  -a m/(N sigma)
  -a(a-1)/(2N sigma)
  +(a+j)(a+j-1)/(2N)
  +O(N^{-1/2}).                                         (24.12)
```

For fixed `m,j`, subtracting the right side of (24.12) from the exact log gamma-ratio must tend
to zero at rate `O(N^{-1/2})`.  This is a direct numerical falsification gate requiring no support
optimization.

## 4. One- and two-slot normal kernels

For a `rho=1` injection row, use the raw convention

```text
F^{(1)}_{a,j}(H)=sum_{i=1}^2 A_{a,j}(tau_i).
```

After multiplication by the harmless nonzero row scalar `2N^j/(N)_{a+j}`, its regular-face
normal kernel is

```text
K^{(1)}_{alpha,j}(H)
 =sum_{i=1}^2 (m_i)_j H_alpha(sigma_i).                  (24.13)
```

Equivalently,

```text
K^{(1)}_alpha(H;t)
 =sum_i H_alpha(sigma_i)(1+t)^{m_i}.                     (24.14)
```

For a `rho=2` row assign `(a,j)` to one slot and `(c,l)` to the other, where

```text
a=alpha D+O(1),   c=gamma D+O(1),
j,l=O(1),         alpha+gamma<1.                       (24.15)
```

With the exact injection symmetrization and row scaling `4N^{j+l}/(N)_{a+j+c+l}`, the kernel is

```text
K^{(2)}_{alpha,j;gamma,l}(H)
 =exp{(kappa^2/2)[(alpha+gamma)^2
                  -alpha^2/sigma_1-gamma^2/sigma_2]}
    (m_1)_j(m_2)_l sigma_1^a sigma_2^c

  +exp{(kappa^2/2)[(alpha+gamma)^2
                  -alpha^2/sigma_2-gamma^2/sigma_1]}
    (m_2)_j(m_1)_l sigma_2^a sigma_1^c,                 (24.16)
```

up to relative `O(N^{-1/2})`.  Overall constants depend on the orbit-row convention and are
irrelevant; the two summands, factorial indices, and WKB exponents do not.

The corresponding generating kernel is obtained by replacing

```text
(m_1)_j(m_2)_l  by  (1+t_1)^{m_1}(1+t_2)^{m_2}          (24.17)
```

coefficientwise in `t_1,t_2`, followed by the displayed slot symmetrization.

Equations (24.13)-(24.17) cover every regular-face query direction in which each occupied slot
has one index of order `D` and its minority index remains fixed.  Purely fixed-degree rows are
their `alpha=gamma=0` algebraic limit and should be handled without WKB normalization.

## 5. Matching to the NO face

The NO face is the trace `m_1=m_2=0`.  Since

```text
(0)_0=1,             (0)_j=0 for j>0,                  (24.18)
```

the exact trace laws are:

```text
K^{(1)}_{alpha,0}|_{NO}=sum_i H_alpha(sigma_i),
K^{(1)}_{alpha,j}|_{NO}=0                     (j>0),    (24.19)
```

and a two-slot kernel survives on NO only if `j=l=0`.

Let `nu_0` be the signed functional on the NO trace and let `nu_m` denote the normal-layer
functional on integer `(m_1,m_2) != (0,0)`.  Necessary leading equations are therefore

```text
<nu_0,K_{alpha,0}>+<nu_m,K_{alpha,0}>
  +[bulk coefficient at normal order 0]=0,              (24.20)

<nu_m,K_{alpha,j}>
  +[bulk coefficient at normal order j]=0     (j>0),    (24.21)
```

with identical two-slot equations.  The label correlation occurs precisely because `nu_0` is NO
and every nonzero `m` is YES, while the `j=0` kernel does not distinguish them at leading order.
The higher factorial jets are the constraints that can destroy or preserve that boundary
collision.

There is no scalar-`xi` reduction.  For example, at `sigma_1=sigma_2=1/2`, the normal states

```text
(m_1,m_2)=(2,0)  and  (1,1)
```

have the same `xi/kappa^2=1`, but their two-slot `(j,l)=(1,1)` factors are respectively `0` and
`1`, and their one-slot `j=2` factors are respectively `2` and `0`.  Hence any kernel written only
as a function of `xi` identifies orbit rows that are exactly different.

## 6. Coefficientwise bulk-to-normal matching

For a macroscopic split slot write `(r,u)=(Nv,Nq)` with `q>v>0`, `q+v=sigma`.  For fixed `j`
and `a=alpha D+O(1)`, the same exact row has the dominant branch

```text
2A_{a,j}(Nv,Nq)/(N)_{a+j}
 =v^j q^a
   exp[-(alpha^2 kappa^2/2)(1/q-1)](1+o(1)),            (24.22)
```

away from the phase tie `q=v`.  Under the normal substitution `v=m/N`, the monomial factor
`N^j v^j=m^j` must be replaced by the exact lattice factor `(m)_j`.  The change of basis is the
triangular Stirling transform

```text
(m)_j=sum_{h=0}^j s(j,h)m^h,
m^h=sum_{j=0}^h S(h,j)(m)_j.                            (24.23)
```

Thus normal matching is coefficientwise in the falling-factorial jet, not pointwise in `xi`.

More explicitly, consider first a direct three-way ansatz and let
`Phi^N_{a,j}=2A_{a,j}/(N)_{a+j}`.  Decompose an exact signed functional into bulk, regular normal,
and NO parts.  Suppose the bulk functional admits an expansion in `N^{-1/2}` after its tangential
WKB phase is removed:

```text
<nu_bulk^N,Phi^N_{a,j}>
 =sum_{h>=0} N^{-h/2} B_{alpha,j}^{[h]}.              (24.24)
```

Since the regular normal contribution to the unrescaled row is `N^{-j}` times (24.13), exact
annihilation forces the necessary hierarchy

```text
B_{alpha,j}^{[h]}=0                  for 0<=h<2j,

B_{alpha,j}^{[2j]}
 +<nu_m,K^{(1)}_{alpha,j}>
 +1_{j=0}<nu_0,K^{(1)}_{alpha,0}>=0.             (24.25)
```

Here the `h=0` equation is included in the first line when `j>0`; for `j=0` it is the second
line.  WKB corrections and the Stirling transform make (24.25) triangular across lower jet
indices, but do not change the requirement that the bulk cancel through order `N^{-j+1/2}` before
the `j`th normal factorial moment can enter.  The same statement applies to (24.16), with normal
order `N^{-(j+l)}`.

Equation (24.25) is the precise necessary matching law promised by the formal Phase-23 equation:
the normal functional is a boundary defect coefficient of a very high-order bulk cancellation.
It is not an independently normalizable measure that can be glued to an arbitrary bulk solution.

## 7. Why direct normal-to-bulk matching does not close

The regular normal formula assumes `m=O(1)`.  A query direction with both indices scaled,

```text
a=alpha D+O(1),       b=beta D+O(1),       alpha,beta>0,
```

has, after assuming without loss of generality that `alpha>=beta`,

```text
A_{a,b}(m,n-m)=0                                      (24.26)
```

identically for all sufficiently large `N` at fixed `m`.  Such rows are also zero on NO.  They
first become nonzero when `m>=b`, hence at the transition scale

```text
m=lambda D,             lambda>=beta,
C_t=Theta(ND),
xi=Theta(D).                                               (24.27)
```

At `m=lambda D`, Stirling gives the new minority factor

```text
log (lambda D)_{beta D}
 =beta D log D
  +D[lambda log lambda
     -(lambda-beta)log(lambda-beta)-beta]
  +(1/2)log[lambda/(lambda-beta)]+o(1),                  (24.28)
```

valid for `lambda>beta`.  Formula (24.28) is neither the fixed-`m` factorial jet nor the
macroscopic bulk WKB formula with `v=Theta(1)`.  It is a genuinely intermediate kernel.

Consequently there is no common overlap region in which the full scaled query family is described
both by (24.11) and by the ordinary bulk kernel.  The fixed-`j` subfamily can be coefficientwise
matched by (24.25), but the `b=Theta(D)` subfamily requires at least the transition (24.27)-(24.28).
This is the exact point where the four-sector shorthand `NO / xi=O(1) / bulk / corner` is
under-resolved.

## 8. Tangential corner warning

Bounded `xi` does not force fixed minority occupancy when a slot total degenerates.  For example,

```text
s_1=Theta(sqrt N),       r_1,u_1=Theta(sqrt N)
```

has `r_1u_1=Theta(N)` and hence `xi=Theta(1)`, even though both occupancies diverge.  The other slot
can carry the macroscopic filler.  This state lies in the same scalar normal coordinate as (24.1)
but has a different falling-factorial asymptotic.  It is a tangential-corner sector, not part of
the regular-face kernel derived here.

Therefore the formulas in this memo are uniform only for `sigma_i>=delta`; this restriction is a
mathematical type condition, not an omitted endpoint estimate.

## 9. Named but untested escape

The calculation generates one distinct escape:

> **mesoscopic minority-occupancy transition hierarchy** — augment the stratified Remez system by
> kernels indexed by `m/D -> lambda` (and, if forced, by intermediate powers of `D`), then match
> their Stirling large-deviation phases to the fixed-`m` factorial jets and macroscopic bulk.

This route is only named.  No construction, finite search, or feasibility test for it was performed
here.  Under DAG Rule 8 it must receive a canonical node before any such work is commissioned.

## 10. Falsification and completion gates

The following are direct, bounded checks for this memo's formulas:

1. **Exact factorial identity:** evaluate both sides of (24.4) for arbitrary integers
   `a>m`, `0<=j<=m+2`, `n>m`; equality must be exact.
2. **One-slot WKB:** at fixed `kappa,alpha,sigma,m,j`, the log residual in (24.12) must be
   `O(N^{-1/2})` along admissible integer sequences.
3. **Two-slot WKB:** after removing the two exponents in (24.16), both injection summands must have
   relative error `O(N^{-1/2})` away from tangential phase ties.
4. **NO trace:** all `j>0` one-slot kernels and all two-slot kernels with `j+l>0` must vanish exactly
   at `m_1=m_2=0`.
5. **Non-scalar normal coordinate:** the `(2,0)` versus `(1,1)` example in Section 5 must give the
   stated unequal factorial rows at equal `xi`.
6. **Transition birth:** for `b=beta D`, exact rows must be zero when `m<b` and nonzero when
   `m>=b` subject to the major occupancy constraints; (24.28) must match the gamma ratio.

Passing these gates would validate the displayed kernel formulas, not establish a dual witness,
correlation above `2/3`, high-`C_t` residual tail, or lattice realization.

## 11. Scoped conclusion

The regular-face normal kernel is now explicit:

```text
tangential WKB factor  x  discrete factorial jet
H_alpha(sigma)         x  (1+t)^m.                       (24.29)
```

NO is its `m=0` trace.  Bulk matching requires cancellation through the order at which the
factorial boundary defect appears, as stated in (24.25).  This derivation rules out treating
`xi` as a sufficient one-dimensional normal coordinate and exposes the missing
`m=Theta(D)` transition kernel for the full degree-`D` query family.

Accordingly the controlling node remains open at proposer tier.  No `PROVED`, `CERTIFIED*`,
`NUMERICAL`, or `REFUTED` status is claimed.
