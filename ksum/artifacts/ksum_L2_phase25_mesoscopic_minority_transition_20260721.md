# k-Sum L2 phase-25 analytic/numerical proposer — mesoscopic minority transition

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.mesoscopic-minority-occupancy-transition`

Scope: `q=5`, `K=2`, `D=kappa sqrt(N)`, regular tangential faces, and only the
`m=lambda D` minority-occupancy transition kernel and its matching to the fixed-`m` factorial jet
and macroscopic bulk.  No finite support or LP search is performed.

Tier: proposer derivation plus bounded gamma-ratio checks; no independent review and no
completion-tier claim.

## Decision

**Decision C.**  The exact/Stirling transition kernel is explicit, including its activation edge
and its two-slot polarization.  Contrary to the pessimistic possibility left open in Phase 24,
the active transition kernel *does* have a clean overlap with macroscopic bulk when it is written
using the unexpanded major fraction `q=sigma-m/N`.  On the other side it matches the fixed-index
factorial jet through the exact gamma ratio, but scaled minority query directions have an exact
birth threshold and no direct overlap with fixed `m`.

The calculation gives:

- an interior transition phase `F(lambda,beta)`;
- a discrete birth kernel for `m-b=O(1)`;
- a uniform transition-to-bulk limit as `lambda -> infinity` and `m/N -> v`;
- a fixed-index overlap through `(m)_j` and the Stirling triangular jet;
- a scoped obstruction: on a fixed tangential fiber, a shallow transition band cannot carry a
  nonzero annihilator at all, and a transition band separated from NO cannot represent NO with
  bounded total variation.

It does **not** produce a globally coupled, nonseparable support with correlation above `2/3`.
The remaining missing object is a tangentially moving phase-paired measure with a uniformly
bounded exact-correction operator.

## 1. Exact dominant transition row

For one unordered slot write

```text
tau=(m,n-m),       n=N sigma+O(1),
D=kappa sqrt(N)+O(1),
m=lambda D+O(1).                                         (25.1)
```

Let the two query exponents be

```text
h=alpha D+O(1),       ell=beta D+O(1),
alpha>=beta>0,        h+ell<D.                           (25.2)
```

The exact symmetric row is

```text
2A_{h,ell}(m,n-m)
 =(m)_h(n-m)_ell+(m)_ell(n-m)_h.                         (25.3)
```

For `alpha>beta`, the second term is the WKB-dominant orientation.  The first term is exactly zero
when `m<h`, and even when it is active it is smaller by the superexponential factor
`(D/N)^{(alpha-beta)D+O(1)}` away from a phase tie.  If `alpha=beta`, the two terms coincide and
their sum contributes an extra factor two.

Define the exact dominant, row-rescaled kernel

```text
T^N_{alpha,beta}(sigma,lambda)
 :=(N/D)^ell (m)_ell(n-m)_h/(N)_{h+ell}.                 (25.4)
```

All scalings in (25.4) depend only on the row, never on the support point, so they preserve the
annihilating kernel.

## 2. Interior Stirling kernel

For `lambda>beta`, set

```text
F(lambda,beta)
 :=lambda log lambda
   -(lambda-beta)log(lambda-beta)-beta.                  (25.5)
```

Also retain the actual major fraction

```text
q_N=(n-m)/N=sigma-lambda D/N+o(D/N).                    (25.6)
```

Uniformly when `q_N>=delta>0` and `lambda-beta>=epsilon>0`, the exact gamma ratios give

```text
T^N_{alpha,beta}
 =sqrt(lambda/(lambda-beta))
  exp[D F(lambda,beta)] q_N^h
  exp{(kappa^2/2)[(alpha+beta)^2-alpha^2/q_N]}
  (1+O(D^{-1})).                                        (25.7)
```

Here `alpha=h/D`, `beta=ell/D`, and `lambda=m/D` may be taken as their exact sequence values;
doing so absorbs all floor/ceiling offsets.  Formula (25.7) is the requested mesoscopic
falling-factorial/Stirling kernel.

For fixed `lambda`, expanding `q_N^h` around `sigma` recovers the Phase-24 correction:

```text
q_N^h
 =sigma^h exp[-alpha lambda kappa^2/sigma+O(D^{-1})],

T^N_{alpha,beta}
 =sqrt(lambda/(lambda-beta)) exp[D F(lambda,beta)] sigma^h
  exp{(kappa^2/2)[(alpha+beta)^2
                  -(alpha^2+2alpha lambda)/sigma]}
  (1+O(D^{-1})).                                        (25.8)
```

The support-dependent WKB phase after removal of row-only normalizations is

```text
S_{alpha,beta}(sigma,lambda)
 =alpha log sigma+F(lambda,beta).                        (25.9)
```

The order-one amplitude in (25.8) is essential on phase-tie sets.

## 3. Exact activation and the birth layer

The transition is not analytic across `lambda=beta`.  Exactly,

```text
(m)_ell=0                 for m<ell,                    (25.10)
```

so the dominant orientation is absent.  At the edge write

```text
m=ell+s,       s in Z_{>=0} fixed.                    (25.11)
```

Then

```text
(ell+s)_ell=Gamma(ell+s+1)/Gamma(s+1),                  (25.12)
```

and Stirling gives the discrete birth kernel

```text
(ell+s)_ell
 =sqrt(2 pi ell) (ell/e)^ell ell^s/s!
  (1+O(ell^{-1})).                                      (25.13)
```

Equivalently, the interior phase reaches

```text
F(beta,beta)=beta log beta-beta,                        (25.14)
```

but its amplitude `sqrt(lambda/(lambda-beta))` is invalid there and must be replaced by

```text
sqrt(2 pi beta D) (beta D)^s/s!.                        (25.15)
```

Thus a unit increase in `m` at activation multiplies the leading birth amplitude by about
`beta D/(s+1)`.  This is the precise degree-jump/birth law missing from the ordinary normal
kernel.

## 4. Two-slot transition kernel

For a `rho=2` injection row, assign high/low pairs `(h_i,ell_i)` to the two slots, with

```text
h_i=alpha_i D+O(1),       ell_i=beta_i D+O(1),
lambda_i=m_i/D>beta_i,
sum_i(alpha_i+beta_i)<1.                                (25.16)
```

Let `q_i=(n_i-m_i)/N` and `d=sum_i(h_i+ell_i)`.  After the common row scaling
`(N/D)^{ell_1+ell_2}`, one injection assignment has kernel

```text
T^{(2)}
 =prod_i sqrt(lambda_i/(lambda_i-beta_i))
  exp[D sum_i F(lambda_i,beta_i)]
  prod_i q_i^{h_i}
  exp{(kappa^2/2)[(sum_i(alpha_i+beta_i))^2
                  -sum_i alpha_i^2/q_i]}
  (1+O(D^{-1})).                                        (25.17)
```

The actual orbit row is the sum of (25.17) and the term obtained by exchanging the two query
assignments between the slots.  If a high/low pair ties, its coincident orientations contribute
the corresponding factor two.  If `lambda_i=beta_i+O(D^{-1})`, replace the affected square-root
amplitude by the birth factor (25.15).

This gives the full regular-face polarization of the transition kernel.  Tangential corners
`sigma_i -> 0` remain outside its stated type.

## 5. Matching to the fixed-`m` factorial jet

There are two different query limits and they must not be conflated.

### 5.1 Fixed minority query index

For `ell=j=O(1)`, the exact identity from Phase 24 remains valid for every `m<h`:

```text
2A_{h,j}(m,n-m)=(m)_j(n-m)_h.                           (25.18)
```

As `m -> infinity`,

```text
(m)_j
 =m^j exp[-j(j-1)/(2m)+O(m^{-2})].                     (25.19)
```

Thus the fixed-`m` factorial jet and the mesoscopic regime overlap directly for every fixed `j`:
the same exact coefficient `(m)_j` is used, and (25.19) is the overlap expansion.  In generating
form, `(1+t)^m` becomes `exp[m log(1+t)]`; it must not be replaced by `exp(mt)` before the
`j(j-1)/(2m)` correction is accounted for.

### 5.2 Scaled minority query index

For `ell=beta D`, `beta>0`, every fixed-`m` row is exactly zero by (25.10).  There is no overlap
limit at fixed positive `beta`: the row is born only at `m=ell+O(1)`.  Matching is therefore a
source law, not equality of two smooth asymptotic expansions:

```text
fixed-m sector:       zero,
birth sector:         (25.13)-(25.15),
interior transition:  (25.7).                           (25.20)
```

The exact gamma ratio (25.12) is the common object connecting the last two lines.

## 6. Matching to macroscopic bulk

Formula (25.7) was deliberately written with the unexpanded `q_N`.  Let

```text
m=Nv,       q=sigma-v,       v,q>=delta>0.
```

Then

```text
lambda=m/D=Nv/D -> infinity.                            (25.21)
```

For large `lambda`,

```text
F(lambda,beta)
 =beta log lambda-beta^2/(2lambda)
  -beta^3/(6lambda^2)+O(lambda^{-3}),                   (25.22)
```

and the combination appearing before (25.7) satisfies

```text
(D/N)^ell exp[D F(lambda,beta)]
 sqrt(lambda/(lambda-beta))
 =v^ell exp[-beta^2 kappa^2/(2v)](1+O(D^{-1})).         (25.23)
```

Undoing the transition row scaling therefore yields

```text
2A_{h,ell}(Nv,Nq)/(N)_{h+ell}
 =v^ell q^h
  exp{(kappa^2/2)[(alpha+beta)^2
                  -beta^2/v-alpha^2/q]}
  (1+O(D^{-1})),                                        (25.24)
```

which is exactly the macroscopic two-sided falling-factorial WKB kernel on its dominant
orientation.  Hence transition-to-bulk matching is not an additional conjectural law: (25.7)
and (25.24) are two limits of the same gamma-ratio formula.

There is also a genuine overlap wedge with

```text
1 << lambda << D,       m/N -> 0,                       (25.25)
```

provided the unexpanded `q_N` is retained.  Expanding `q_N` too early destroys this overlap and
creates the false appearance of a missing sector.

## 7. Bounded-TV matching conditions

Let a proposed signed functional be decomposed into NO, fixed-normal, transition, and bulk
pieces, with total variation bounded independently of `N`.  The transition calculation yields
the following necessary conditions.

### 7.1 Tropical phase matching

For every active scaled query direction `(alpha,beta)`, bounded total variation cannot cancel an
exponential phase gap.  Therefore

```text
max_{positive support} S_{alpha,beta}
 =max_{negative support} S_{alpha,beta},                (25.26)
```

with `S` from (25.9), including the slot-polarized analog for (25.17).  On each phase-tie set,
the signed leading amplitudes from (25.7), (25.15), and (25.17) must sum to zero.  Subsequent WKB
coefficients must cancel until the fixed-normal order is reached.

### 7.2 Activation matching

NO and every fixed-`m` state contribute exactly zero to a row with `ell=beta D>m`.  Consequently
the transition-plus-bulk functional must self-annihilate every positive-`beta` query family:

```text
<nu_transition+nu_bulk,T_{alpha,beta}>=0,
0<beta, alpha+beta<1.                                  (25.27)
```

Only the `beta=0` and fixed-`j` families can transfer signed mass between NO/fixed-normal and the
outer sectors.  Equations (25.26)-(25.27) are the missing compatibility condition between the
two sides of the birth edge.

### 7.3 A checkable sufficient correction condition

Let `A_N` be the exact orbit-moment operator restricted to the chosen transition and bulk support,
with row weights obtained by removing the WKB phases above.  Suppose an approximate matched
functional `tilde nu_N` satisfies the label/tail inequalities with a fixed margin and has residual
`r_N=A_N tilde nu_N`.  A sufficient condition for exact bounded-TV lifting is the existence of
right inverses `R_N` on the residual subspace such that

```text
A_N R_N r_N=r_N,
||R_N r_N||_TV=o(1),
sup_N ||tilde nu_N||_TV<infinity.                        (25.28)
```

Then

```text
nu_N=tilde nu_N-R_Nr_N                                  (25.29)
```

is exactly annihilating, has uniformly bounded TV, and preserves every strict correlation and
tail margin for large `N`.  Formula (25.28) is useful rather than tautological because the WKB
normalization in (25.7) identifies the weighted row norm in which a uniform inverse must be
proved.  No such inverse is constructed here.

## 8. Scoped obstructions

### 8.1 Fixed tangential fiber, shallow transition

Fix `sigma`, fix the other slot identically, and let only one minority occupancy vary over

```text
0<=m<=M,       M<=Lambda D,       Lambda<1/2.            (25.30)
```

Choose an integer `h` with

```text
M<h<D-M,                                                   (25.31)
```

which is possible precisely because `Lambda<1/2`.  After the fixed other-slot contribution is
removed using the zero-mass row, every `j=0,...,M` row in (25.18) is `(m)_j` times the nonzero
column factor `(n-m)_h`.  The square matrix

```text
[(m)_j]_{0<=j,m<=M}                                      (25.32)
```

is triangular with nonzero diagonal `m!`; multiplying its columns by `(n-m)_h` preserves
invertibility.  Exact annihilation of these rows forces the aggregate signed weight at every `m`
to be zero.  Hence no nonzero annihilator, bounded-TV or otherwise, can live on a single shallow
tangential fiber.

This does not obstruct the full node: it proves that tangential motion and/or coupling between
the two slots is mandatory.

### 8.2 A gap from NO causes TV blow-up on one fiber

Still on one tangential fiber, suppose a weight `-1` at `m=0` is represented by YES weights
supported only on `m in [lambda_0D,Lambda D]`, with `lambda_0>0`, while matching all polynomials
of degree `cD`.  A Chebyshev polynomial rescaled from that interval to take value one at zero has
supremum exponentially small on the YES interval.  The moment representation inequality then
forces

```text
sum |w_m| >= exp(c' D)                                  (25.33)
```

for a constant `c'=c'(c,lambda_0,Lambda)>0`.

Thus direct NO-to-transition matching across a positive `m/D` gap is incompatible with bounded
TV on one fiber.  Fixed-normal atoms or nonseparable tangential/slot coupling are not optional.

These are scoped obstructions only; neither applies to a support moving jointly in
`(sigma_1,sigma_2,m_1,m_2)`.

## 9. Bounded numerical checks

The gamma-ratio formulas were checked without any support search at

```text
D=100,200,400,800,       N=D^2,       kappa=1.
```

Command:

```text
python ksum/tools/ksum_l2p25_transition_kernel_check.py
```

Driver SHA-256:

```text
72f99e9b87b9886236d781b58f7ff628dbef3ca6f159850422d51930a09c3c87
```

Raw log:
`ksum/artifacts/logs_ksum_L2p25_transition_kernel_20260721/run.json`

Observed log errors from `D=100` to `800` were:

```text
interior transition:  6.64e-5 -> 1.22e-5,
bulk overlap:          9.50e-3 -> 1.18e-3,
birth edge s=2:        1.49e-1 -> 1.92e-2,
fixed-j overlap:       1.12e-3 -> 1.71e-5.              (25.34)
```

The bulk and birth errors are asymptotically proportional to `D^{-1}` in the displayed range;
the fixed-`j` remainder is proportional to `m^{-2}`.  These runs validate values computed from
the displayed formulas, not the existence of a matched signed measure.

## 10. New escape generated by this calculation

One distinct escape is generated and only named here:

> **tangential phase-paired transport with uniform WKB right inverse** — construct a genuinely
> nonseparable signed transport in `(sigma_1,sigma_2,m_1,m_2)` satisfying the tropical phase ties
> (25.26), birth self-cancellation (25.27), and the exact-correction bound (25.28).

No construction or test of this route was performed.  Under DAG Rule 8 it requires a canonical
node before any work is commissioned.

## 11. Gate ledger

| obligation | result |
|:---|:---|
| exact `m=lambda D` row | PASS analytically: (25.3)-(25.4) |
| interior Stirling kernel | PASS at proposer tier: (25.7)-(25.8) |
| activation/birth law | PASS at proposer tier: (25.10)-(25.15) |
| two-slot polarization | PASS at proposer tier: (25.17) |
| fixed-index overlap | PASS: exact coefficient plus (25.19) |
| scaled-index overlap with fixed `m` | EXACTLY ABSENT; replaced by birth law |
| macroscopic bulk overlap | PASS: (25.22)-(25.25) |
| bounded-TV necessary conditions | PASS at proposer tier: (25.26)-(25.27) |
| bounded-TV sufficient criterion | FORMULATED, uniform right inverse missing |
| fixed-fiber obstruction | PASS at proposer tier: (25.30)-(25.33) |
| global nonseparable support | OPEN |
| correlation `>2/3` and constant high tail | OPEN |
| finite legal lifting | OPEN |

## 12. Scoped conclusion

The mesoscopic kernel is not itself the obstruction.  Its gamma-ratio form smoothly reaches the
macroscopic bulk and exactly resolves the activation edge.  The obstruction is geometric: any
bounded-TV solution must combine tangential motion, two-slot coupling, phase pairing, and a
uniform exact-correction mechanism.  Fiberwise or scalar-normal constructions cannot do this.

Accordingly the controlling node remains open with Decision C and bounded numerical evidence.
No `PROVED`, `CERTIFIED*`, or `REFUTED` claim is made; independent review remains owed before any
completion-tier status.
