# k-Sum L2 phase-14 target-scale finite sweep

Date: 2026-07-21  
Scope: `q=5`, `K=2`, variable-pair-total orbit family  
Controlling node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Tier: **NUMERICAL** only; no asymptotic inference and no DAG completion claim

## Outcome

The phase-13 finite calculation is independently reproduced.  At `N=8`, the exact rational
moment matrices give

| polynomial cutoff `D` | raw rows | rank | nullity | maximum unit-`l1` sign correlation |
|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | 23 | `1` |
| 8 | 63 | 20 | 4 | `1/32` |
| 9 | 92 | 24 | 0 | `0` (no nonzero annihilator) |

At `D=8`, imposing at least `1/4` absolute mass on `C_t>=4,6,8` again gives exact optimum `1/32`.
The returned decompositions have zero positive/negative overlap; their actual high-tail masses are
respectively `31/32`, `7/8`, and `1/4`.

Thus there is no phase-13 numerical discrepancy.  The earlier orbit-list digest cannot be compared
byte-for-byte because its serialization was not archived; this run's canonical compact-JSON orbit
digest is `9b5f89df588536d0c670da336a4907a1ed029fe4b65da09ed27239d5051f80b5`.

## Independently reconstructed finite model

An orbit is an unordered pair of unordered splits

`H=({r_1,u_1},{r_2,u_2})`, with `r_i<=u_i`, `r_i+u_i>=1`, and
`r_1+u_1+r_2+u_2=N`.

For a source-pair multiplicity pattern `p=(a,b)`, the script uses

`B_p(r,u)=(r)_a(u)_b+(r)_b(u)_a=2 A_{a,b}(r,u)`.

The one-slot and two-slot moment rows are

`B_p(h_1)+B_p(h_2)`

and

`B_p(h_1)B_s(h_2)+B_p(h_2)B_s(h_1)`.

This is the phase-12 orbit-average formula after omitting a nonzero scalar separately from every
row.  Such row rescaling leaves rank, nullspace, and the signed optimization unchanged.  Row
patterns are multisets of at most two unordered `(a,b)` patterns of total degree `<D`; this gives
the preregistered raw row counts `2,63,92` at `D=2,8,9`.

The label is `+1` when `C_t=sum_i r_i u_i>0` and `-1` on the NO boundary.  Every rank and LP result
below was computed over exact SymPy integers/rationals.

## Target-scale sweep

Here `D` is always a **polynomial-degree cutoff**: every moment of degree `<D` is annihilated.
It is not a query count.  If used in the standard polynomial-method conversion, it corresponds to
the query lower-bound scale `D/2`.

Duplicate floor/ceiling choices are listed once.

| `N` | `D` choice | orbits | raw rows | rank | nullity | max correlation |
|---:|:---|---:|---:|---:|---:|---:|
| 6 | `floor sqrtN` | 12 | 2 | 1 | 11 | `1` |
| 6 | `ceil sqrtN` | 12 | 5 | 3 | 9 | `5/6` |
| 6 | `ceil(2sqrtN)` | 12 | 17 | 8 | 4 | `1/8` |
| 7 | `floor sqrtN` | 16 | 2 | 1 | 15 | `1` |
| 7 | `ceil sqrtN` | 16 | 5 | 3 | 13 | `8/9` |
| 7 | `ceil(2sqrtN)` | 16 | 27 | 10 | 6 | `13/69` |
| 8 | `floor sqrtN` | 24 | 2 | 1 | 23 | `1` |
| 8 | `ceil sqrtN` | 24 | 5 | 3 | 21 | `11/12` |
| 8 | `ceil(2sqrtN)` | 24 | 27 | 10 | 14 | `505/1838` |
| 9 | `floor=ceil sqrtN` | 30 | 5 | 3 | 27 | `15/16` |
| 9 | `ceil(2sqrtN)` | 30 | 27 | 10 | 20 | `1107/3352` |
| 10 | `floor sqrtN` | 41 | 5 | 3 | 38 | `19/20` |
| 10 | `ceil sqrtN` | 41 | 9 | 4 | 37 | `13/15` |
| 10 | `ceil(2sqrtN)` | 41 | 43 | 16 | 25 | `961351/10264045` |
| 11 | `floor sqrtN` | 50 | 5 | 3 | 47 | `24/25` |
| 11 | `ceil sqrtN` | 50 | 9 | 4 | 46 | `8/9` |
| 11 | `ceil(2sqrtN)` | 50 | 43 | 16 | 34 | `200848/1657831` |
| 12 | `floor sqrtN` | 65 | 5 | 3 | 62 | `29/30` |
| 12 | `ceil sqrtN` | 65 | 9 | 4 | 61 | `49/54` |
| 12 | `ceil(2sqrtN)` | 65 | 43 | 16 | 49 | `274875/1752668` |

Numerically, every sampled `floor/ceil sqrtN` cutoff has correlation above `2/3`, while every
sampled `ceil(2sqrtN)` cutoff has correlation below `2/3`.  This is a small-`N`, constant-sensitive
observation only; the jumps in `D` already make the doubled-cutoff sequence visibly nonmonotone.

## Natural high-`C_t` gate

For each target-scale case the exploratory gate was

`sum_{C_t >= ceil(D^2/4)} |W(H)| >= 1/4`.

| `N` | `D` | threshold | gated correlation | finite LP check |
|---:|---:|---:|---:|:---|
| 6 | 2 | 1 | `1` | actual absolute mass |
| 6 | 3 | 3 | `3/4` | actual absolute mass |
| 6 | 5 | 7 | n/a | no orbit reaches threshold |
| 7 | 2 | 1 | `1` | actual absolute mass |
| 7 | 3 | 3 | `9/11` | actual absolute mass |
| 7 | 6 | 9 | `<=39/272` | LP relaxation upper bound; overlap prevents an attaining witness claim |
| 8 | 2 | 1 | `1` | actual absolute mass |
| 8 | 3 | 3 | `6/7` | actual absolute mass |
| 8 | 6 | 9 | `1517/6492` | actual absolute mass |
| 9 | 3 | 3 | `8/9` | actual absolute mass |
| 9 | 6 | 9 | `366/1253` | actual absolute mass |
| 10 | 3 | 3 | `10/11` | actual absolute mass |
| 10 | 4 | 4 | `197/240` | actual absolute mass |
| 10 | 7 | 13 | `16427925/196555832` | actual absolute mass |
| 11 | 3 | 3 | `25/27` | actual absolute mass |
| 11 | 4 | 4 | `21/25` | actual absolute mass |
| 11 | 7 | 13 | `1319287647/11622788986` | actual absolute mass |
| 12 | 3 | 3 | `15/16` | actual absolute mass |
| 12 | 4 | 4 | `325/378` | actual absolute mass |
| 12 | 7 | 13 | `5218070320/33416555403` | actual absolute mass |

Except for the explicitly marked relaxation, “actual absolute mass” means the exact LP returned
`l1=1`, tail `l1>=1/4`, and zero overlap between its positive and negative variables.  This is an
internal witness check, not a completion-tier certification.

The high-tail-gated `floor/ceil sqrtN` samples also remain above `2/3`.  This finite evidence is
consistent with continuing the variable-total direction at the intended `q=5` scale, but it does
not supply an asymptotic coefficient formula or a uniform constant.

## Reproduction command and hashes

```text
python ksum/tools/ksum_l2p14_target_scale_sweep.py --output ksum/artifacts/logs_ksum_L2p14_target_scale_sweep_20260721/results.json
```

SHA-256:

```text
0627B9B5B14A7C9EBB67588A5706FCF69266109B40C1150AB94C93B0BD69DFF7  ksum/tools/ksum_l2p14_target_scale_sweep.py
2948EEF01B74A509FE1A9230560C41C3F2C7DD748DBB2BDC717DF6DD301C6C89  ksum/artifacts/logs_ksum_L2p14_target_scale_sweep_20260721/results.json
211A9D7C528F780BE241238F6E0318262F354A02113DFE4A905560F0F652B763  ksum/artifacts/logs_ksum_L2p14_target_scale_sweep_20260721/run_command.txt
```

## Numerical interpretation and next discriminator

The finite pattern suggests that the constant hidden in a prospective `Theta(sqrt N)` cutoff is
decisive: coefficient `1` survives all sampled instances, while coefficient `2` does not.  This is
only a **CONJECTURED** diagnostic pattern.  A useful next numerical step is to extend `N` and sweep
all intermediate integer cutoffs, especially `D=ceil(c sqrt N)` for several fixed
`1<c<2`, while keeping the exact tail gate.  None of the present data may be extrapolated to an
asymptotic lower bound.
