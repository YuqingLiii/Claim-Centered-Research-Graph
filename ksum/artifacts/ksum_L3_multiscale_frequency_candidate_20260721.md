# L3 multiscale-frequency-mask: explicit critical-spectrum candidate

Date: 2026-07-21  
Canonical scope: `KSUM.B4b.L3.ALT.multiscale-frequency-mask`  
Status of this memo: proposer-tier construction and hostile upper-bound gate only; **no lower
bound is claimed**  
Method: local corpus only; no web; no DAG-file edits

## 1. Outcome

There is one explicit integer multiscale law that survives the requested
palette-exposure/residual-claw self-test.  Write `n=floor(N/2)`.  Apart from one side-exclusive
reservoir value of multiplicity `Theta(n)`, its decoy spectrum has

```text
h_j = Theta(q/4^j),       M_j = Theta(2^j sqrt(q)),
0 <= j <= Theta(log q),                                  (MF.1)
```

with the constants and roundings frozen in Section 3.  The bottom band has `Theta(q)` labels of
multiplicity `Theta(sqrt(q))`; the higher bands have geometrically fewer labels.  Consequently,

```text
number of non-reservoir decoy labels = Theta(q),
non-reservoir decoy mass             = Theta(q^(3/2)),
total decoy mass                     = Theta(N).          (MF.2)
```

Each side also has `Theta(q)` singleton candidate labels.  NO has disjoint left/right supports.
YES has exactly one common label, occurring once on each side, and no other common label.  The
complete marginal frequency spectrum of each side is therefore identical in YES and NO.

The promise is an exact permutation-invariant restriction of two-list claw.  The standard cyclic
map with modulus `2q+1` gives an arbitrary-target 2-SUM instance of exact length `N` with one input
query per live coordinate.  Section 4 checks this directly.

The important conclusion is narrower than a lower bound:

```text
best audited sample/cutoff + residual-claw scale      = Theta-tilde(sqrt(N)q^(1/4));
quantum distinct-label palette enumeration scale     = O-tilde(sqrt(N)q^(1/4));
neither audited attack is little-oh of the target.    (MF.3)
```

The frequency `sqrt(q)` is forced by optimizing the two attacks against one another.  A seemingly
natural `N`-dependent frequency `sqrt(N)q^(-1/4)` passes the classical sampling gate but is exposed
by quantum distinct-label enumeration in `o(sqrt(N)q^(1/4))` throughout every strictly
subcritical polynomial regime.

This candidate is not a new endpoint donor.  Once its reservoir is removed, the residual has
`B=Theta(q^(3/2))` positions and range `q=Theta(B^(2/3))`: it is exactly a critical hidden-palette
core, with harmless lower-mass frequency bands.  Thus the construction converges structurally to
the already registered pair

```text
KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint
KSUM.B4b.L3.ALT.critical-core-psearch-lift.             (MF.4)
```

It passes the construction/upper-attack gate, but proving the desired lower bound still requires
the unresolved critical-core theorem and a valid lift/composition argument.

## 2. Why the bottom frequency is forced

Before choosing a ladder, consider a bottom band containing

```text
h=Theta(q) side-exclusive decoy labels,
each with multiplicity m,                               (MF.5)
```

plus `r=Theta(q)` singleton candidates.  Ignore the reservoir, which can be learned with
`O(1)` samples and handled by the usual sample-incident claw check in `O(sqrt(n))` queries.

Let

```text
T:=sqrt(n)q^(1/4).                                      (MF.6)
```

All `N`- versus `n`-based targets below differ only by absolute constants.

### 2.1 Residual-claw constraint

If the bottom palette is not exposed, the residual contains `Theta(qm)` positions.  The reviewed
virtual-residual reduction followed by the standard claw child costs

```text
C_res(m)=O-tilde(sqrt(n)(qm)^(1/6)).                    (MF.7)
```

Avoiding `C_res(m)=o(T)` requires

```text
qm = Omega(q^(3/2)),
or equivalently m=Omega(sqrt(q)).                       (MF.8)
```

### 2.2 Quantum palette-enumeration constraint

Classical coupon sampling is not the strongest palette attack.  Keep a table `D` of already seen
values and Grover-search for an index whose value is not in `D`.  A successful search returns a
new value with probability proportional to its remaining multiplicity.  Repeating this operation
enumerates the heavy palette; Section 6 includes the singleton-distraction accounting.

With `k` bottom-band labels still unseen, the marked mass is at least `km`, so the decoy-discovery
part costs

```text
sum_(k=1)^h O(sqrt(n/(km)))
 =O(sqrt(nh/m))
 =O(sqrt(nq/m)).                                        (MF.9)
```

Avoiding an `o(T)` enumeration therefore requires

```text
sqrt(nq/m)=Omega(sqrt(n)q^(1/4)),
or equivalently m=O(sqrt(q)).                           (MF.10)
```

Together, (MF.8) and (MF.10) force

```text
m=Theta(sqrt(q)).                                       (MF.11)
```

The ordinary sample-exposure time is then

```text
n/m=Theta(n/sqrt(q)) >= Omega(T)                        (MF.12)
```

for `q=O(n^(2/3))`, so sampling imposes no stronger restriction.

For comparison, balancing only (MF.12) against `T` suggests
`m=Theta(sqrt(n)q^(-1/4))`.  Substituting this larger value into (MF.9) gives

```text
C_enum/T
 =Theta(n^(-1/4)q^(3/8))
 =Theta((q/n^(2/3))^(3/8)),                             (MF.13)
```

which tends to zero for every `q=n^kappa`, `0<kappa<2/3`.  That parameter choice is therefore
self-rejected.  Equation (MF.11), not the sample-only balance, is the law used below.

## 3. Exact integer law

Assume

```text
N>=12,       5<=q<=floor(N^(2/3)),       n=floor(N/2).  (MF.14)
```

As in the exact single-scale construction, these inequalities imply `q<n`.  Define

```text
r := max{1,floor(q/8)},
J := floor(log_4 r),
m := max{2,floor(sqrt(q)/16)}.                          (MF.15)
```

For `j=0,...,J-1` (an empty set if `J=0`), put

```text
h_j := floor(r/4^(j+1)),
M_j := 2^j m.                                           (MF.16)
```

Finally set

```text
H := sum_(j=0)^(J-1) h_j,
D := sum_(j=0)^(J-1) h_j M_j,
R := n-r-D.                                             (MF.17)
```

The one-side frequency law is

```text
candidate labels:  r labels of frequency 1;
ladder decoys:     h_j labels of frequency M_j for every j;
reservoir decoy:   1 label of frequency R.              (MF.18)
```

All entries are explicit integers.  The elementary geometric bounds are

```text
H <= sum_(j>=0) r/4^(j+1) =r/3,                         (MF.19)

D <= sum_(j>=0) (r/4^(j+1)) 2^j m
  <rm/2
  <=q/8 + q^(3/2)/256.                                 (MF.20)
```

Because `q<n` and `q^(3/2)<=N<=2n+1`, (MF.20), together with `r<=q/8`, makes `R` a positive
constant fraction of `n`; in particular the law sums exactly to `n` and its total decoy mass
`D+R=n-r` is `Theta(n)`.  For `q` tending to infinity,

```text
h_0=Theta(q),       m=Theta(sqrt(q)),
D=Theta(q^(3/2)),   H=Theta(q).                         (MF.21)
```

The support size on either side is

```text
s=r+H+1 <=4r/3+1 <=q/6+1.                              (MF.22)
```

Hence `2s<=q/3+2<=q` for every `q>=5`: two disjoint copies of the support fit inside `[q]`.

The ladder degenerates legally at small fixed `q`.  In particular, at `q=5`, `r=1` and `J=0`,
so each side consists of one singleton and one reservoir label of multiplicity `n-1`.  No
zero-size required palette is used.

## 4. Exact YES/NO promise and cyclic 2-SUM embedding

Use two length-`n` lists `x,y in [q]^n` with the marginal spectrum (MF.18).

```text
NO:  every label in supp(x) is distinct from every label in supp(y).

YES: one singleton label z_* occurs once in x and once in y;
     every other singleton, ladder, and reservoir label is side-exclusive.   (MF.23)
```

All assignments of the displayed multiplicities to positions and all common relabelings of
`[q]` are allowed.  Each answer class is consequently one orbit of
`S_n x S_n x S_q`.  The promise exposes no palette, position block, frequency tag, or address.

Both answer classes have exactly the same complete one-side frequency multiset (MF.18).  NO has
empty support intersection.  YES has support intersection `{z_*}` and exactly one equal
cross-position pair.  Thus ordinary two-list claw is exactly the promise bit.

For an arbitrary target `t`, let

```text
Q:=2q+1,
2c=t in Z_Q,                                            (MF.24)
```

where `c` is unique because `Q` is odd.  Map

```text
x_i -> c+x_i,       y_j -> c-y_j.                       (MF.25)
```

Two left values hit `t` only if `x_i+x_j=0 mod Q`, impossible because the integer sum lies in
`[2,2q]`.  The same argument handles two right values.  A cross pair hits `t` exactly when
`x_i-y_j=0 mod Q`; its integer difference lies in `[-(q-1),q-1]`, so this is equivalent to
`x_i=y_j`.

If `N` is odd, append the one public value `c`.  It is distinct from every live value and cannot
form a target pair with one live value; there is no second padding coordinate.  Therefore (MF.25)
is an exact arbitrary-target cyclic 2-SUM embedding of length `N`, modulus `2q+1=O(q)`, and one
value-oracle query per live coordinate (at most two in the coherent XOR convention).

## 5. Optimized random-sampling/cutoff attack

First take a constant number of random samples on each side.  With constant probability these
contain the reservoir label because `R=Theta(n)`.  As in the single-scale attack, batch-check
whether any sampled label occurs on the opposite side in `O(sqrt(n))` queries.  If the check is
negative, delete every same-side occurrence of the sampled labels.  Repetition gives any fixed
bounded error.  It is then enough to analyze the ladder residual.

After `ell` further uniform samples, a frequency-`M` label is unseen with probability

```text
p_M(ell)=binom(n-M,ell)/binom(n,ell)
        =exp(-Theta(ell M/n))                           (MF.26)
```

in the ranges used below.  The residual mass scale is therefore

```text
b(ell)=r+sum_j h_j M_j exp(-Theta(ell M_j/n)).          (MF.27)
```

The sample/delete/virtual-residual-claw template has cost

```text
A(ell)=O(sqrt(n)+ell)
      +O-tilde(sqrt(n)b(ell)^(1/6)).                    (MF.28)
```

For growing `q`, the lowest band alone has

```text
B_0=h_0M_0=Theta(q^(3/2)),
tau=n/M_0=Theta(n/sqrt(q)).                             (MF.29)
```

All higher bands have no more mass and are easier to expose.  Put `ell=x tau`.  Up to absolute
constants,

```text
b(x tau)=q+Theta(q^(3/2) exp(-Theta(x))).               (MF.30)
```

Normalize (MF.28) by `T` and define

```text
sigma:=(n^(2/3)/q)^(3/4).
```

Then

```text
A(x tau)/T
 =Theta(sigma x)
  +Theta-tilde((q^(-1/2)+exp(-Theta(x)))^(1/6))
  +O(q^(-1/4)).                                        (MF.31)
```

Throughout `q<=N^(2/3)=Theta(n^(2/3))`, `sigma=Omega(1)`.  Consequently:

```text
x=o(1):       a (1-o(1)) fraction of B_0 survives, so the child is Theta(T);
x=Theta(1):   setup is Omega(T), whether or not the residual shrinks;
x->infinity:  setup is omega(T).                        (MF.32)
```

The optimum of this entire cutoff continuum is therefore `Theta-tilde(T)`, achieved already by
removing only the reservoir and running the residual child.  Equivalently, a cutoff above `m`
leaves the `Theta(q^(3/2))` bottom band, while a cutoff through `m` costs
`Omega(n/m)=Omega(T)` before coupon-collection logarithms.

At fixed `q` the ladder may be empty, but deleting the reservoir leaves `Theta(1)` singleton
positions and costs `Theta(sqrt(n))=Theta(T)` through virtual residual access.  Thus no fixed or
polynomial regime is silently omitted from (MF.32).

## 6. Quantum distinct-label palette exposure

The sample cutoff is not enough for a hostile audit, because quantum search can enumerate new
values faster than classical coupon collection.  The following explicit attack was included in
the parameter optimization.

Maintain the set `D_seen` of discovered values.  Grover/BBHT-search the list for an index `i`
satisfying

```text
input[i] notin D_seen.                                  (MF.33)
```

This predicate uses one input query plus a table lookup.  Query the returned position and add its
value to `D_seen`.  Conditional on success, the new value is sampled proportionally to its
remaining frequency.

There are `H+1=Theta(q)` decoy labels, and every non-reservoir decoy has frequency at least
`m=Theta(sqrt(q))`.  If `k` decoys remain, their positions alone give marked mass at least `km`.
Thus the decoy-discovery work is

```text
O(sum_(k=1)^H sqrt(n/(km)))
 =O(sqrt(nH/m))
 =O(T).                                                 (MF.34)
```

This `T` scale is not only slack from the displayed upper summation for this particular
one-new-value-per-search procedure.  After the reservoir is removed, the entire marked
non-reservoir mass is `O(q^(3/2))`.  Each iteration returns at most one new label and has ordinary
search cost `Omega(sqrt(n/q^(3/2)))`; learning `Theta(q)` decoy labels therefore costs

```text
Omega(q sqrt(n/q^(3/2)))=Omega(T).                      (MF.34a)
```

Hence this explicit sequential enumeration attack is `Theta-tilde(T)`.  Equation (MF.34a) is only
a lower bound for that specified procedure, not for arbitrary quantum palette algorithms.

Singletons can appear before the last decoy and cannot simply be ignored.  A size-biased random
ordering is equivalently an exponential race with rate equal to each label's frequency.  With
probability `1-delta`, every decoy appears before time

```text
O(log(H/delta)/m),                                      (MF.35)
```

and only

```text
O((r/m) log(H/delta))                                  (MF.36)
```

singleton labels appear by then.  Charging each such distraction the worst remaining-decoy
search cost `O(sqrt(n/m))` gives

```text
O-tilde(sqrt(nH/m)+(r/m)sqrt(n/m))
 =O-tilde(sqrt(n)q^(1/4))
 =O-tilde(T).                                           (MF.37)
```

Operationally, after removing the reservoir, run (MF.33) for
`H+O((r/m)log(H/delta))` distinct-value discoveries.  The algorithm need not identify which
discoveries are decoys: (MF.35)--(MF.36) imply that this fixed stopping count contains all `H`
ladder labels with probability at least `1-delta`.

After the enumeration, one batch cross-list membership search detects any sampled occurrence of
the unique claw in `O(sqrt(n))`.  On a negative result it is safe to delete all discovered labels;
with high probability only `O(q)` singleton positions survive.  Their compressed claw cost is

```text
O-tilde(sqrt(n)q^(1/6))=o(T)                            (MF.38)
```

for growing `q` and is `Theta(sqrt(n))` for fixed `q`.  The total attack (MF.37)--(MF.38) matches
the target up to logarithms; it does not beat it.

Partial enumeration has no hidden subtarget optimum in the same accounting.  Removing an
`alpha` fraction of the `Theta(q)` bottom labels costs on the scale

```text
T(1-sqrt(1-alpha)),                                     (MF.39)
```

while the remaining-band child costs

```text
T(1-alpha)^(1/6).                                      (MF.40)
```

Their sum stays a positive constant times `T` for every `0<=alpha<=1`.  This is an optimization
of this explicit enumeration-plus-child strategy, not a query lower bound against all possible
algorithms.

## 7. Endpoint and cap sweep

Let

```text
L(N,q):=min{sqrt(N)q^(1/4),N^(2/3)}.                   (MF.41)
```

The frozen construction is used through the crossover `q=Theta(N^(2/3))`; above it the standard
walk supplies the cap.

### `q=5`

Each side has one singleton and one side-exclusive reservoir value.  Four support labels fit in
the five-value claw alphabet.  The promise remains nonempty, the cyclic modulus is `11`, and the
audited residual access cost is `Theta(sqrt(N))=Theta(L(N,5))`.

### `q=N^kappa`, `0<kappa<2/3`

The bottom band has

```text
Theta(N^kappa) labels,
m=Theta(N^(kappa/2)) copies per label,
B_0=Theta(N^(3kappa/2)) positions.                      (MF.42)
```

The reservoir has `Theta(N)` positions.  After its removal, residual compression followed by the
critical claw child costs

```text
sqrt(N/B_0) B_0^(2/3)
 =sqrt(N)q^(1/4).                                      (MF.43)
```

The sample cutoff costs at least this much, and quantum palette enumeration matches it by
(MF.37).  None is little-oh of (MF.43).

### `q=floor(N^(2/3))`

Here

```text
m=Theta(N^(1/3)),       B_0=Theta(N),
T=Theta(N^(2/3)).                                      (MF.44)
```

The law becomes the critical rare/heavy hidden-palette profile up to fixed constants and the
extra lower-mass ladder bands.  Both audited attacks meet, but do not beat, the standard
`N^(2/3)` cap.

## 8. Structural diagnosis and remaining obligation

The construction gates pass:

| obligation | result |
|:---|:---|
| explicit integer `{(h_j,M_j)}` | **PASS**, (MF.15)--(MF.18) |
| `O(q)` side-exclusive decoy labels | **PASS**, (MF.19), (MF.22) |
| total decoy mass `Theta(N)` | **PASS**, reservoir in (MF.17)--(MF.20) |
| identical per-side YES/NO spectra | **PASS**, (MF.23) |
| exactly one shared-label bit | **PASS**, unique shared singleton in (MF.23) |
| legal fixed endpoint `q=5` | **PASS**, Sections 3 and 7 |
| legal through `q=N^(2/3)` | **PASS**, (MF.20), (MF.44) |
| exact range-`O(q)` cyclic 2-SUM embedding | **PASS**, (MF.24)--(MF.25) |
| optimized random sampling/cutoff self-test | **SURVIVES**, `Theta-tilde(T)` |
| quantum distinct-label exposure self-test | **SURVIVES**, `O-tilde(T)`, not little-oh |
| lower bound | **NOT ATTEMPTED / OPEN** |

The multiscale ladder does not itself create a new hardness mechanism.  Its bottom band already
contains `Theta(q^(3/2))` positions, and every higher band contributes only a geometrically smaller
mass.  Deleting the reservoir exposes a critical range-`q` claw core.  Therefore a future proof
must do both of the following, neither of which is supplied here:

1. prove `Omega(B^(2/3))=Omega(q)` for the exact hidden-palette critical core with
   `B=Theta(q^(3/2))`; and
2. justify the `sqrt(N/B)` lift for this promise without a forbidden public address or a loss in
   alphabet/range.

These are precisely the obligations already visible in the registered critical-endpoint and
critical-core-pSearch-lift nodes.  The present law is useful because it realizes their scaling as
one exact permutation-invariant frequency orbit and shows that palette exposure does not
automatically destroy it.  It does not discharge either obligation and licenses no status above
OPEN.

## 9. Generated ideas outside the controlling node

None.  The sample-only `m=Theta(sqrt(n)q^(-1/4))` choice was a rejected parameter point inside the
same multiscale family, not a separate mechanism.  The surviving `m=Theta(sqrt(q))` law converges
to the already registered critical-core/lift route, so no unregistered successor was tested.
