# k-Sum L2 phase-21 proposer analysis — critical dense-palette `q=N` law

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure`  
Tier: proposer only; no independent review and no DAG status claim

## Decision

**C — the first genuinely critical constant window.**  The explicit mixture law below has all of
the requested structural properties and makes the local positive product palette exactly contain
the full integer interval

```text
{1,2,...,L},       L=floor(N^(2/3)).                         (21.1)
```

It also has a component whose *global* `C_t` support contains every integer from `0` through

```text
T_N=(1/4+o(1))L^2=(1/4+o(1))N^(4/3),                       (21.2)
```

while retaining constant high-tail base mass, random exact total partitions, and a distributed
NO boundary.

The earlier `o(N^(2/3))` activity separators no longer apply.  Separating zero from the dense
local interval has degree `Theta(sqrt(L))=Theta(N^(1/3))`, and composing with a global
`Theta(sqrt(K))` boundary test is now of the target order `Theta(N^(2/3))`, not below it.

There is nevertheless an explicit upper obstruction.  Since powers of `C_t` of degree `r` lie in
the actual orbit span by query degree `2r`, a continuous-interval Chebyshev discriminator gives

```text
c > c_* := (arcosh 3)/2 = 0.8813735870...                  (21.3)
```

asymptotic correlation at most `2/3` for `D=cN^(2/3)` (strictly below `2/3` for every fixed
`c>c_*`, after choosing an approximation error strictly below `1/3`).

For `0<c<c_*`, this pass obtains neither a witness nor a falsifier.  The full orbit span is larger
than the scalar `C_t` polynomials, so failure of this one separator is not evidence that the
projection correlation is above `2/3`.  Conversely, the dense support removes the previous
little-`o` argument, so it is no longer valid to claim failure for every fixed `c>0`.  This is a
real constant-sensitive unresolved window, not Decision A.

## 1. Endpoint parameters

Take sufficiently large odd `N`, put `q=N`, and set

```text
m=(N-1)/2,
L=floor(N^(2/3)),
U=ceil(2N^(1/3)),
M=L-U.                                                       (21.4)
```

All components below use exactly `K=L` positive occupied complementary pair-types, so `K<=m` for
all sufficiently large `N`.  The law is the equal mixture

```text
pi_(N,N)=(1/2)pi_bal+(1/2)pi_dense.                          (21.5)
```

Both components have exact total occupancy `N`; therefore so does the mixture.

## 2. Balanced component with globally gap-free `C_t`

In `pi_bal`, use `U` unit pair-types of total `2`.  For the remaining `M` bulk pairs, put

```text
N_bulk=N-2U,
a=floor(N_bulk/M),
h=N_bulk-Ma,                                                (21.6)

C_bal={s in Z^M:
       s_i=a+delta_i, delta_i in {-2,-1,0,1,2},
       sum_i delta_i=h}.                                    (21.7)
```

Draw `s` uniformly from `C_bal`.  It is nonempty because `0<=h<M`: take `h` deviations `1` and
the rest `0`.  Unit pairs independently choose `(0,2)` or `(1,1)`, each with probability `1/2`.
Conditional on a bulk total `s_i`, independently choose

```text
(0,s_i)                         with probability 1/2,
(r,s_i-r), 1<=r<=floor(s_i/2)  each with probability
                                 1/(2 floor(s_i/2)).         (21.8)
```

Every profile is legal because

```text
2U+sum_i s_i=N.                                              (21.9)
```

The random composition makes the labeled law nonproduct, and all-inactive choices distribute NO
mass over every total histogram arising from `C_bal`.

Fix any one total vector in `C_bal`.  Activating `j` unit pairs gives every target count
`0<=j<=U`.  For a bulk total `s`, its possible one-slot contributions are

```text
X_s={r(s-r):0<=r<=floor(s/2)}.                              (21.10)
```

Consecutive values have gap

```text
x_(r+1)-x_r=s-2r-1<=s-1.                                   (21.11)
```

Here `a=(1+o(1))N^(1/3)` and `U=(2+o(1))N^(1/3)`, so
`U>=max_i(s_i-1)` for all large `N`.  Starting from the full unit interval `[0,U]`, adding one
set `X_s` preserves an integer interval: the translates `[x,x+R]` overlap whenever the current
radius `R>=U` and consecutive `x` differ by at most `U+1`.  Induction over the bulk slots proves

```text
{C_t(H):H in supp(pi_bal) with this total vector}
 ={0,1,...,U+sum_i floor(s_i^2/4)}.                         (21.12)
```

Define

```text
T_N=max_(s in C_bal) [U+sum_i floor(s_i^2/4)].              (21.13)
```

Because `M=L-o(L)`, `a=(1+o(1))N/L`, and every `s_i=a+O(1)`,

```text
T_N=(1+o(1)) M a^2/4
   =(1/4+o(1)) N^2/L
   =(1/4+o(1)) L^2.                                        (21.14)
```

Choosing a maximizing total vector in (21.12) shows that the union support contains every integer
`C_t=0,...,T_N`.

The high-tail base gate also holds.  Each bulk slot has a fixed positive probability of being
active with `r` between `s_i/4` and `s_i/2`; a Chernoff bound gives

```text
Pr_pi_bal[C_t>=c_0 N^(4/3)] >=1-exp(-c_1L)                 (21.15)
```

for absolute constants `c_0,c_1>0`.  Hence the mixture (21.5) assigns asymptotic mass at least
`1/2` to the required high scale.

## 3. Dense local-palette component

Let

```text
C_dense={s in Z^L:
         2<=s_i<=L+1,
         sum_i s_i=N}.                                      (21.16)
```

This set is nonempty for all sufficiently large `N`: the average `N/L=Theta(N^(1/3))` lies
strictly between the bounds.  Draw an ordered total vector uniformly from `C_dense`.  Conditional
on each total `s_i`, independently choose

```text
(0,s_i)       with probability 1/2,
(1,s_i-1)     with probability 1/2.                         (21.17)
```

Again total occupancy is exactly `N`, the composition law is nonproduct, and the all-inactive NO
boundary is distributed across its total histograms.

For every integer `1<=c<=L`, the set `C_dense` contains a vector with a prescribed coordinate
`s_i=c+1`: the remaining total `N-c-1` lies between the aggregate lower and upper capacities of
the other `L-1` coordinates for all large `N`.  Activating that coordinate gives one-slot product

```text
1*(s_i-1)=c.                                                 (21.18)
```

Thus the union one-slot positive product palette contains the complete interval (21.1), not merely
`Omega(N^(1/3))` scattered values.  Profiles remain highly nonunique at fixed product, activation
count, or `C_t`; the construction is not parametrized by a scalar reservoir.

Both pushforward laws are formula-defined and strictly positive on their stated supports.  For
example, an unordered dense histogram has mass

```text
pi_dense(H)=[L!/product_tau H_tau!]/[|C_dense|2^L],         (21.19)
```

and `pi_bal` has the analogous multinomial factor times the product of the probabilities in
(21.8).  If the component supports overlap, (21.5) simply adds the two displayed positive masses.

## 4. Why the old little-`o` separators stop here

Consider a polynomial `q` with `q(0)=0` and

```text
|q(c)-1|<=epsilon,       c=1,...,L,                         (21.20)
```

for a fixed error `epsilon<1`.  The classical discrete OR approximation bound gives degree
`Theta(sqrt(L))` for constant `epsilon`; in particular, the dense interval rules out the
`O(N^(1/6)log N)` local separator used in phase 20.  Exact interpolation costs degree at least `L`,
since `q-1` has the `L` distinct roots `1,...,L` when `epsilon=0`.

The global boundary contains `K=L` active/inactive coordinates, whose constant-error OR/AND
approximation scale is `Theta(sqrt(L))`.  Therefore the naive local-times-global scale is

```text
Theta(sqrt(L))*Theta(sqrt(L))=Theta(L)=Theta(N^(2/3)).       (21.21)
```

The important conclusion is only order-theoretic: this mechanism no longer produces a separator
of degree `o(N^(2/3))`.  Leading constants and robustness under composition matter.  No claim that
the product of the two separate optimal degrees is itself the optimal orbit-span degree is made.

## 5. Explicit actual-orbit upper obstruction and its constant

The scalar route gives a clean constant without any composition theorem.  Let

```text
b(H)=1[H is NO]=1[C_t(H)=0].                                (21.22)
```

All profiles in the mixture satisfy `0<=C_t<=T_N`: in the balanced component this is the
definition of `T_N`, while in the dense component (21.17) gives
`C_t<=sum_i(s_i-1)=N-L=o(L^2)<T_N` for large `N`.

For any `epsilon in (0,1/3)`, put

```text
alpha_N=arcosh((T_N+1)/(T_N-1)),
r_N(epsilon)=ceil(arcosh(1/epsilon)/alpha_N),
p_(N,epsilon)(x)
 =T_(r_N)( (T_N+1-2x)/(T_N-1) )
  /T_(r_N)( (T_N+1)/(T_N-1) ).                              (21.23)
```

Then

```text
p_(N,epsilon)(0)=1,
|p_(N,epsilon)(x)|<=epsilon for every real x in [1,T_N].    (21.24)
```

The phase-18 collision-partition identity directly places every degree-`r` polynomial in `C_t`
inside the actual orbit-feature span by query degree at most `2r`.  Thus (21.23) belongs to `V_D`
when `2r_N(epsilon)<D`.

Using `alpha_N=2/sqrt(T_N)+o(T_N^(-1/2))` and (21.14),

```text
2r_N(epsilon)/L
 =arcosh(1/epsilon) sqrt(T_N)/L+o(1)
 =(1/2)arcosh(1/epsilon)+o(1).                              (21.25)
```

Let `D=floor(cL)`.  If

```text
c>(1/2)arcosh(3)=0.8813735870...,                           (21.26)
```

choose `epsilon<1/3` sufficiently close to `1/3` that
`(1/2)arcosh(1/epsilon)<c`.  Then (21.23) lies in `V_D` for all sufficiently large `N`.

Let `g=b-Proj_(V_D)^(L_2(pi))b`.  If `g=0`, the normalized phase-16 law is unavailable.  Otherwise
`W_pi=pi g/||g||_(1,pi)` annihilates (21.23), has zero mass and unit `l1`, and satisfies

```text
|<W_pi,1-2b>|
 =2|<W_pi,b-p_(N,epsilon)(C_t)>|
 <=2epsilon<2/3.                                            (21.27)
```

This is an actual projection/correlation bound, not a base-support argument.

## 6. The unresolved constant window

For `c>c_*`, (21.27) sharply falsifies the candidate.  At `c=c_*`, strictness and lower-order
rounding terms are unresolved.  For

```text
0<c<c_*,                                                     (21.28)
```

the explicit scalar separator (21.23) does not fit below the cutoff asymptotically.  The dense
integer intervals in (21.1) and (21.12) also explain why the previous local or scalar Chebyshev
arguments cannot simply be rerun with a little-`o` degree.

This does **not** prove correlation above `2/3` in (21.28).  The actual orbit-feature span contains
many multisymmetric rows beyond polynomials in `C_t`; one of them may still approximate the label
more efficiently.  Nor has the weighted projection residual been diagonalized.  Therefore the
proper verdict is Decision C:

- **falsified** for every fixed `c>c_*`;
- **open** for every fixed `0<c<c_*`;
- **open at the boundary** `c=c_*`.

## 7. Gate ledger

| Gate | Critical mixture law |
|---|---|
| formula-defined positive law | **PASS** |
| exact all-large-odd-`N` legality and rounding | **PASS** |
| `K=Theta(N^(2/3))` | **PASS** |
| nonproduct dependence | **PASS** in both mixture components |
| distributed NO boundary | **PASS** |
| local positive products contain `1,...,Theta(N^(2/3))` | **PASS** |
| global `C_t` support contains `0,...,Theta(N^(4/3))` | **PASS** |
| constant base mass at `C_t=Theta(N^(4/3))` | **PASS** |
| previous `o(N^(2/3))` activity separator | **BLOCKED** by dense palettes |
| actual projection correlation for `c>c_*` | **FAIL**, strictly below `2/3` |
| actual projection correlation for `0<c<c_*` | **OPEN** |
| residual-weighted high-tail mass in the open window | **OPEN** |

## 8. Scoped conclusion

This law reaches the critical regime requested in Phase 21.  It removes both forms of cheap local
activity recovery: neither exact interpolation nor interval Chebyshev approximation is
`o(N^(1/3))`.  The resulting global separator has the same `N^(2/3)` order as the target.

The exact scalar calculation exposes a nontrivial constant window rather than an all-constant
no-go.  Above `c_*=(arcosh3)/2`, the actual orbit span forces correlation below `2/3`; below it,
the present methods genuinely stop.  Establishing Decision A would require direct control of the
weighted projection residual and its high-tail mass in that window.  Establishing Decision B for
the whole family would require a new actual-orbit approximant with a better constant or a
non-scalar mechanism.

No distinct escape route was tested or commissioned in this pass.  No `PROVED`, `CERTIFIED*`,
`NUMERICAL`, or `REFUTED` status is claimed.
