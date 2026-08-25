# k-Sum L2 phase-19 proposer — canonical moving Remez/cubature circuit

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature`

Scope: explicit formula-defined support at `q=5`, `K=2`

Tier: proposer plus exact finite gates; no independent review and no completion-tier claim

## Decision

**Decision B — the canonical formula-defined moving circuit fails correlation and global
equioscillation, despite perfect legality, exact `rank+1` cancellation, and abundant high-`C_t`
mass.**

The tested support is not selected by an LP.  It is the lexicographically first orbit-feature
basis plus the lexicographically first later column whose fundamental circuit uses every basis
column.  This gives one deterministic support formula for every `(N,D)`, an explicit cofactor
kernel, and a uniquely determined candidate dual interpolant.

All 21 cases in three consecutive `c=5/4` cutoff blocks were completed exactly:

```text
D=5,  11<=N<=16;
D=6,  17<=N<=23;
D=7,  24<=N<=31.
```

Every support has exactly `rank(F_<D)+1` legal orbits and a one-dimensional full-support
nullspace.  Every normalized kernel puts more than `1/2` absolute mass on the natural high-`C_t`
tail, and the `D=6,7` tail masses are generally above `0.89`.  Nevertheless, the correlations are
only

```text
D=5:  0.00272 ... 0.00676;
D=6:  0.000752 ... 0.00214;
D=7:  0.00000901 ... 0.0000274.
```

All are far below `2/3`.  Even optimizing the choice of the single extra circuit column while
keeping the same canonical basis cannot raise correlation above `0.0353`, `0.00721`, and
`0.000200` in the three respective blocks.

The candidate dual polynomial equioscillates exactly on its selected circuit, but violates its
required uniform residual bound on an omitted balanced interior orbit in every case.  The maximum
residual/candidate-epsilon ratio ranges from about `288` to more than `8.0 million`.

This kills only the displayed canonical-basis formula and its one-extra-column repairs.  It does
not refute arbitrary moving Remez supports.

## 1. Explicit support formula

Enumerate the legal `q=5`, `K=2` histograms exactly as in phases 14 and 16:

```text
H=((r_1,u_1),(r_2,u_2)),
r_i<=u_i,
(r_1,u_1)<=(r_2,u_2) lexicographically,
r_1+u_1+r_2+u_2=N.
```

Let `F=F_{N,D}` be the exact orbit-feature matrix containing every phase-12 row of degree `<D`,
with rowwise nonzero denominators deleted.  Replace its rows by the lexicographically selected
independent-row basis used in phase 16, and write its rank as `R`.

The support formula is:

1. Let `b_1<...<b_R` be the pivot columns of the exact reduced row-echelon form of `F`.  Equivalently,
   these are the lexicographically first orbit columns forming a basis.
2. Put `C=[F_{b_1}|...|F_{b_R}]`.
3. For every nonbasis orbit `j` in lexicographic order, compute
   `a(j)=C^{-1}F_j`.  Let `j_*` be the first `j` for which every coordinate of `a(j)` is nonzero.
4. Define

   `S_{N,D}={b_1,...,b_R,j_*}`

   and raw coefficients

   `w_raw=(-a_1(j_*),...,-a_R(j_*),1)`.

5. Orient the sign so `<w_raw,f_t>>=0` and divide by `||w_raw||_1`.

This definition uses exact orbit features but no correlation LP, fitted support list, or Phase-16
optimum.  It applies verbatim across all three completed blocks.

## 2. Exact cancellation and cofactor interpretation

By construction,

`C a(j_*)=F_{j_*}`,

so

`sum_{H in S_{N,D}} w_raw(H)F(H)=0`.

Because `C` is nonsingular and every entry of `a(j_*)` is nonzero, the selected `R+1` columns have
rank `R`, their nullspace is one-dimensional, and every support coefficient is nonzero.  Cramer's
rule gives

`a_i(j_*)=det(C_i(j_*))/det(C)`,

where `C_i(j_*)` replaces the `i`th basis column by `F_{j_*}`.  Thus the nullspace signs are exactly

`sgn w_i=-sgn(det(C_i(j_*))/det(C))`, and `sgn w_{j_*}=+1`

before the global orientation.  This is an explicit cofactor formula, but the computed minor signs
alternate along the near-boundary staircase and show no stable closed sign pattern across the
three cutoffs.

The full exact support, coefficients, ranks, and matrix digests for all 21 cases are in the logs.

## 3. Three consecutive cutoff blocks

### Canonical circuit

| cutoff block | cases | feature rank | support | correlation range | tail-mass range |
|:---|---:|---:|---:|---:|---:|
| `D=5`, `N=11..16` | 6 | 8 | 9 | `0.00272..0.00676` | `0.541..0.571` |
| `D=6`, `N=17..23` | 7 | 10 | 11 | `0.000752..0.00214` | `0.976..0.988` |
| `D=7`, `N=24..31` | 8 | 16 | 17 | `0.00000901..0.0000274` | `0.893..0.922` |

The tail threshold is `C_t>=ceil(D^2/4)`.  Every case passes the `1/4` tail gate by a wide margin.
Thus the failure is not caused by illegal or low-target-pair support.

The feature ranks `8,10,16` match the Phase-16 ranks where the ranges overlap.  Every displayed
support has the required `R+1` cardinality and exact full-support circuit.

### Best possible extra column with the canonical basis frozen

For every nonbasis column whose fundamental circuit has full support, the script also computes its
exact normalized correlation.  This is a diagnostic over all one-column repairs, not a proposed
support formula.

| cutoff block | full circuits per case | best correlation range | best repaired tail mass |
|:---|---:|---:|---:|
| `D=5` | `16..65` | `0.0269..0.0353` | `0.544..0.563` |
| `D=6` | `71..201` | `0.00475..0.00721` | `0.974..0.986` |
| `D=7` | `207..496` | `0.000121..0.000199` | `0.898..0.925` |

Therefore choosing the earliest extra column is not the decisive problem.  With the canonical
lexicographic basis frozen, **no** full fundamental circuit among all legal extra columns comes
remotely close to `2/3` on any sampled case.

## 4. Why correlation collapses

The pivot basis is a near-boundary staircase.  Representative supports begin with orbits such as

```text
((0,1),(0,N-1)),
((0,1),(1,N-2)),
((0,1),(2,N-3)),
((0,2),(0,N-2)),
((0,2),(1,N-3)), ...
```

and only later include a few fully active columns.  Cofactor signs alternate along this staircase.
The constant feature row enforces total signed mass zero, so

`<w,f_t>=2 sum_{YES} w=-2 sum_{NO} w`.

Most absolute mass is indeed on high-`C_t` YES atoms, which explains the excellent tail figures.
But the alternating YES coefficients cancel each other almost perfectly, while the signed NO mass
is tiny.  High absolute YES mass and high signed correlation are therefore sharply separated.

This is also why the correlation decays as the feature rank and staircase length grow.  The data
do not license an asymptotic rate, but they decisively falsify a constant lower bound for every
completed instance of this formula.

## 5. Candidate dual equioscillation polynomial

Let `w` be the normalized circuit, `epsilon=<w,f_t>>0`, and `sigma_H=sgn(w(H))` on the support.
The candidate dual coefficient vector `y` is defined by the exact interpolation system

`f_t(H)-(F^T y)(H)=epsilon sigma_H`, for every `H in S_{N,D}`.

Compatibility follows from `Fw=0` and `||w||_1=1`.  The support columns have rank `R`, so `y` is
unique after deleting redundant feature rows.  This is precisely the equioscillation polynomial
which would certify optimality if

`|f_t(H)-(F^T y)(H)|<=epsilon`

held on every legal orbit.

It fails in every one of the 21 exact gates.  The first maximum-violation orbit is always

`((0,1),(floor((N-1)/2),ceil((N-1)/2)))`,

the balanced interior split omitted by the near-boundary pivot basis.  The violation ratios grow
from about `287.9` at `(N,D)=(11,5)` to about `8.04e6` at `(31,7)`.  Hence the formula fails both
the primal correlation gate and the global dual Remez gate, by large independent margins.

## 6. Gate ledger

| gate | result |
|:---|:---|
| formula not defined by LP output | PASS |
| three consecutive cutoff blocks | PASS: all 21 cases completed |
| all support orbits legal | PASS by enumeration |
| support size `rank(F_<D)+1` | PASS in every case |
| one-dimensional full-support nullspace | PASS exactly |
| explicit cofactor coefficients/signs | PASS by Cramer's rule and exact logs; no uniform sign law |
| zero mass and all degree-`<D` moments | PASS exactly |
| unit `l1` | PASS by exact normalization |
| high-`C_t` mass | PASS strongly in every case |
| correlation `>2/3` | **FAIL in every case** |
| candidate dual equioscillation on support | PASS exactly |
| dual residual bound on every legal orbit | **FAIL in every case** |
| changing only the extra circuit column | **FAIL for every legal full circuit tested** |
| `q=N` endpoint | NOT TESTED; the `q=5` formula already fails its decisive gates |

## 7. Scoped hard boundary and untested remainder

The exact finite hard boundary is:

> Lexicographically canonical unisolvent orbit-feature bases produce legal selective circuits with
> excellent high-`C_t` mass, but their cofactor signs nearly cancel the signed YES mass.  No choice
> of one extra column repairs the correlation while that basis is frozen, and the associated dual
> interpolant is maximally violated at a balanced interior orbit.

The remaining moving-Remez node is broader.  It could replace the entire basis by a simultaneous
boundary/interior design rather than append one column to a near-boundary unisolvent set.  The
Phase-16 optimal supports indeed mix boundary and balanced interior atoms, but no formula for that
global selection is known.

A **label-aware Fekete/basis-exchange support** would be a distinct escape if promoted from this
observation into a construction.  Under Rule 8 it must be registered before any proof or numerical
testing.  It is only named here; no such work was started.

## 8. Reproduction and provenance

Driver:
`ksum/tools/ksum_l2p19_canonical_circuit.py`

Exact commands:
`ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/run_commands.txt`

Exact JSON logs:

```text
ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d5_block.json
ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d6_block.json
ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d7_block_a.json
ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d7_block_b.json
```

SHA-256:

```text
CE7F06D4D20FC3CB4D7B19DA2B5C83CAB32CC132F4DA5DE69372DF384CA13527  ksum/tools/ksum_l2p19_canonical_circuit.py
9F973AA18004FEDF63A1BDBA60FE6A67ED12A28E0962A8A0B84B52AAEDB365C8  ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/run_commands.txt
87961C46536C6AFEB89C4186A7543ED4AD8160BC7D865F379E7BCB39A6141D17  ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d5_block.json
A3D91131AF4C0BDA2A966A7F2EF9C4EA2B6C904E9B5CE4E854BC8D9F84F5C8BF  ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d6_block.json
8572DCA7557E4C73AF0FC483E0DB48010B4C6B945170407860F1954AE2F83420  ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d7_block_a.json
BD13856936E4114EB790AC212DAF3E63ECF39C179E99CDB82B54327816C9E867  ksum/artifacts/logs_ksum_L2p19_canonical_circuit_20260721/d7_block_b.json
```

No `PROVED`, `CERTIFIED*`, or `REFUTED` conclusion is claimed.
