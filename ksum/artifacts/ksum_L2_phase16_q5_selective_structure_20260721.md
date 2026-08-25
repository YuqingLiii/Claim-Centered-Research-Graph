# k-Sum L2 phase-16 q=5 selective-kernel structure reconnaissance

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`

Scope: `q=5`, `K=2`, exact finite orbit-feature nullspaces

Tier: **NUMERICAL** only; no asymptotic inference and no DAG completion claim

## Decision

The new exact data supports only a **moving selective equioscillation/cubature ansatz**, not a
bounded-support or fixed-recursion formula.

For every completed `D=6` case `17<=N<=23`, an exact optimum is carried by 11 legal orbits, its
feature columns have rank 10, and its normalized signed kernel is the unique one-dimensional
dependence on that support.  At `D=7`, the two completed vertical jump checks have 17 support
orbits and feature rank 16.  Thus the sparse optimum is always a basic `rank+1` kernel in these
cases, but the support size grows with the actual orbit-feature rank (`8/9` at `D=5`, `11` at
`D=6`, `17` at `D=7`).  There is no evidence for an absolute bounded-support or hidden bounded-rank
law as the cutoff grows.

The full `D=6` block is favorable for the original finite discriminator: correlation recovers from
`0.6566` at `N=17` to `0.7702` at `N=23`, and every returned optimum puts more than `1/4` absolute
mass on `C_t>=9`.  Raising the cutoff by one at the same small sizes is destructive: at `D=7`,
correlation is only `0.3264` and `0.3554` for `N=17,18`, and the unconstrained optimum's mass on
`C_t>=13` is below `1/4` in both cases.

This sharp cutoff sensitivity is finite evidence only.  It neither constructs the desired
`Theta(sqrt N)` family nor obstructs it.

## Exact model and solver paths

The orbit and moment engine is the independently reconstructed phase-14 model.  A legal orbit is
an unordered pair of unordered splits

`H=({r_1,u_1},{r_2,u_2})`, with `r_i<=u_i` and total occupancy `N`.

All phase-12 orbit-feature rows of total degree `<D` are included, with one nonzero scalar omitted
separately from each row.  The label is `+1` iff
`C_t=r_1u_1+r_2u_2>0` and `-1` on the boundary.

Two exact rational solver paths were used:

1. the phase-14 `l1` primal in positive/negative variables, retaining the returned sparse witness
   only after checking true `l1=1` and zero positive/negative overlap;
2. for the larger `D=6` cases, an exact Chebyshev-dual cutting plane which starts from feature
   pivot columns, repeatedly adds the globally most violated orbit constraint, and reconstructs
   an exact complementary-slackness primal witness.

At `(N,D)=(23,6)`, both paths return exactly
`9960784653/12932549372`, the same 11-point support, the same coefficients, and the same tail mass.
This checks value-versus-formula agreement at one endpoint of the new block; it is not an
independent Rule-7 review.

## Two complete adjacent `c=5/4` cutoff blocks

For `D=ceil((5/4)sqrt N)`, `D=5` exactly on `11<=N<=16`, and `D=6` exactly on `17<=N<=23`.
Both complete integer blocks were evaluated.

### Previously sampled `D=5` block, now with exact sparse structure

| `N` | rank/nullity | exact optimum | support | support feature rank | mass on `C_t>=7` |
|---:|:---:|---:|---:|---:|---:|
| 11 | `8/42` | `480/1007` | 9 | 8 | `233/1590` |
| 12 | `8/57` | `8/15` | 9 | 8 | `1234/10875` |
| 13 | `8/69` | `4648/7865` | 8 | 7 | `14503/39325` |
| 14 | `8/88` | `184870/288387` | 9 | 8 | `103717/288387` |
| 15 | `8/104` | `2050/3029` | 8 | 7 | `59602/190827` |
| 16 | `8/128` | `3168/4493` | 9 | 8 | `60355/220157` |

The correlation crosses `2/3` between `N=14` and `N=15`.  The unconstrained optimum's natural
tail mass crosses `1/4` between `N=12` and `N=13`.

### New complete `D=6` block beyond `N=16`

| `N` | orbits | rank/nullity | exact optimum | `>2/3` | support/rank | mass on `C_t>=9` |
|---:|---:|:---:|---:|:---:|:---:|---:|
| 17 | 156 | `10/146` | `564789953/860178993` | no | `11/10` | `4139188631/12042505902` |
| 18 | 185 | `10/175` | `826013/1215389` | yes | `11/10` | `19682357/60769450` |
| 19 | 210 | `10/200` | `10158547112/14514731747` | yes | `11/10` | `34582993925/116117853976` |
| 20 | 246 | `10/236` | `5377395977/7457960852` | yes | `11/10` | `78139624159/253570668968` |
| 21 | 276 | `10/266` | `519765121701/703779880876` | yes | `11/10` | `1212148807553/4222679285256` |
| 22 | 319 | `10/309` | `936185439/1240616764` | yes | `11/10` | `12604500441/47143437032` |
| 23 | 352 | `10/342` | `9960784653/12932549372` | yes | `11/10` | `437818372007/1681231418360` |

The first block point falls below `2/3`, then the remaining six recover above it.  All seven
unconstrained optima already pass the exploratory `1/4` tail-mass gate.  This is the complete
finite sawtooth for this one cutoff block, not a monotonicity or asymptotic claim.

## Vertical cutoff jump at fixed `N`

| `N` | `D` | rank | exact optimum | support/rank | tail threshold | tail mass |
|---:|---:|---:|---:|:---:|---:|---:|
| 17 | 6 | 10 | `564789953/860178993` | `11/10` | 9 | `4139188631/12042505902` |
| 17 | 7 | 16 | `105528169109/323337417317` | `17/16` | 13 | `1295022390503/7113423180974` |
| 18 | 6 | 10 | `826013/1215389` | `11/10` | 9 | `19682357/60769450` |
| 18 | 7 | 16 | `2422133018146681/6815177889114186` | `17/16` | 13 | `545722466877987571/2249008703407681380` |

One additional degree raises the exact feature rank from 10 to 16 and the basic support from 11 to
17.  At both sizes the correlation roughly halves and the natural tail mass falls below `1/4`.
The `D=7` block at its `c=5/4` locations `N=24..31` was not completed by this exact engine; no
claim is made about that block.

## What the supports say

The full support and rational coefficient list for every case is in the JSON logs.  Three patterns
are stable enough to record:

- At `D=6`, every optimum has exactly three NO-boundary support orbits and eight YES orbits.  The
  signed coefficient vector has five positive and six negative entries.
- The selected columns always span the full 10-dimensional feature row space, and deleting the
  one-dimensional kernel leaves a nonsingular basic system.  At `D=7`, the same statement holds
  with dimensions 16 and 17.
- Some geometric atoms recur, such as the extreme boundary orbit
  `{(0,1),(0,N-1)}`, the near-boundary YES orbit `{(0,1),(1,N-2)}`, a balanced split paired with
  `(0,1)`, and a fully active near-balanced orbit.  But the other boundary partitions and active
  splits jump with `N`; the seven-point block does not display a single fixed-offset or fixed-period
  support template.

Any `rank+1` feature kernel admits a cofactor/determinant expression after its support is chosen:
the coefficient at one support column is proportional to the corresponding maximal minor.  The
observed exact weights therefore have a determinant representation in this tautological linear
algebra sense.  They do **not** exhibit the phase-15 product-determinant/OA structure, a separable
coefficient law, or a recurrence that predicts the moving support.

The data also disfavor a low-rank explanation.  On the completed cutoffs the feature ranks are
`8,10,16` for `D=5,6,7`, and the optimal supports track that growth.  A fixed-`D` optimum is sparse
because every finite LP has a basic optimum; this alone gives no bounded support when
`D=Theta(sqrt N)` grows.

## The only analytic ansatz licensed by these data

For each `(N,D)`, seek a moving legal support `S_{N,D}` of exactly `rank(F_{<D})+1` orbit profiles
such that:

1. the feature columns on `S_{N,D}` have a one-dimensional signed nullspace;
2. the cofactor vector has `l1=1`, correlation uniformly above `2/3`, and enough high-`C_t` mass;
3. a dual orbit polynomial equioscillates on `S_{N,D}` and has no larger residual on any other
   legal orbit.

This is a selective discrete cubature/Remez description: it annihilates exactly the actual
orbit-feature rows, not arbitrary assignment-coordinate cylinders.  The finite computations
license this **description of an optimum**, but not a formula for `S_{N,D}` or its cofactors.

If elevated into a distinct analytic route (for example, a continuum-scaled moving-Remez support
with rounded lattice nodes), Rule 8 requires registering that route before any verification.  No
such verification was attempted here.

## Falsification gates for a later registered route

1. Complete the `D=7`, `N=24..31` block with a scalable exact or independently certified LP
   solver.  Failure to recover `>2/3` correlation and `1/4` tail mass anywhere before the next jump
   would weaken the recovery picture.
2. Give one explicit support formula valid across at least three consecutive cutoff blocks.  A
   case table or an LP-selected support is not a formula.
3. Prove the support columns have the stated one-dimensional nullspace and control the cofactor
   signs and `l1` norm uniformly; generic basic-feasible sparsity is insufficient.
4. Produce a dual equioscillation polynomial and prove its residual bound over **all** legal
   integer orbits, not only the selected support or a continuum relaxation.
5. Maintain constant high-`C_t` absolute mass under the same kernel.  The `D=7`, `N=17,18`
   unconstrained optima show that correlation feasibility does not automatically preserve the
   exploratory tail gate.
6. Verify that the construction annihilates only the required orbit tensors and does not silently
   revert to the full coordinate-cylinder annihilation already obstructed in phase 15.

## Reproduction and provenance

Exact commands are archived in
`ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/run_commands.txt`.
The logs contain full orbit supports, exact rational coefficients, ranks, tail masses, orbit
digests, raw-matrix digests, and solver-path metadata.

Key SHA-256 values:

```text
E0DF277E67864D152E705B7CEFAA47BBD794F80CA481308C88F75BBE98532CA7  ksum/tools/ksum_l2p16_q5_selective_structure.py
0627B9B5B14A7C9EBB67588A5706FCF69266109B40C1150AB94C93B0BD69DFF7  ksum/tools/ksum_l2p14_target_scale_sweep.py
D84D8D48D2C666602B58FB6C2ECB8BE2B900B1A39E75371C6AEEBA8C369257E3  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/run_commands.txt
C3857062136C511DA6A96327885C936B06B3CDD6B5F777025168FF531C6D2AE6  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d5_block.json
F65FC37B24648AAE5FEB500F648A7E15FE4BBB29EFB4999824BEE75828A62E86  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n17.json
2425493690FFF0CBCDECD7A6AD6A0B90E148E8A8B9CDCC0B6AF84D31367844FB  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n18.json
5F3695316DAF0F25F975AA0B760DA8B4F12AC3E721D1E9E258B3EEFAA118C7BB  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n19.json
4C6B465D33E56BE7707CE24478C3B6FE914DB8DC9CDE99BD9816572BD16625C0  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n20.json
D10AC319905F6F6DC93017E200FFF313BFB690D6876AF5C6714FAF3D5C558983  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n21.json
085B6B403FF4376D07B28FBD3C03D20B4B78405294F3242F9CC2325D9C047B67  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n22.json
7E466F43FAA1892AA8EB4D826AA43992553CEE5BB5281453E01318132ADD7A41  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n23.json
8CC8F8F3748ED1C72652F8714F9AF0249DAA12957BD8545C71EF30E90682367C  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/d6_n23_primal_crosscheck.json
15DA73F2F93EBD9CE51FD37D770B367A9BDAEAA4908E265546D9BFC862951302  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/jump_n17_d7.json
E7BC8E8BE331245807BA8D57D0752457190EBA5DE05602837E70739ED3058B1E  ksum/artifacts/logs_ksum_L2p16_q5_selective_structure_20260721/jump_n18_d7.json
```

No `PROVED`, `CERTIFIED*`, or `REFUTED` conclusion is claimed.
