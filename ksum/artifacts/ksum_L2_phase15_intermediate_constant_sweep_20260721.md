# k-Sum L2 phase-15 intermediate-constant finite sweep

Date: 2026-07-21  
Scope: `q=5`, `K=2`, variable-pair-total orbit family  
Controlling node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Tier: **NUMERICAL** only; no asymptotic inference and no DAG completion claim

## Outcome

The exact rational phase-14 engine was extended to

`D=ceil(c sqrt(N))`, for `c in {5/4,3/2,7/4}` and every `6<=N<=16`.

All 33 requested `(c,N)` cases completed.  Coincident degree cutoffs were computed once, leaving 29
unique exact moment-rank/LP instances.  The maximum completed size is `N=16` (136 legal orbits);
there are no omitted requested cases.  Total measured run time was 170.007344 seconds.

Here `D` is a polynomial-degree cutoff: all moment rows have degree `<D`.  It is not a query count;
the usual polynomial-method query lower-bound scale would be `D/2`.

The high-tail column uses the same exploratory gate as phase 14:

`sum_{C_t >= ceil(D^2/4)} |W(H)| >= 1/4`.

Except where explicitly noted, the exact LP decomposition has actual `l1=1`, the required actual
tail mass, and zero positive/negative overlap.

## Results for `c=5/4`

| `N` | `D` | rank/nullity | correlation | gated correlation |
|---:|---:|:---:|---:|---:|
| 6 | 4 | 4/8 | `2/3` | `2/3` |
| 7 | 4 | 4/12 | `3/4` | `18/25` |
| 8 | 4 | 4/20 | `13/16` | `109/142` |
| 9 | 4 | 4/26 | `37/44` | `73/92` |
| 10 | 4 | 4/37 | `13/15` | `197/240` |
| 11 | 5 | 8/42 | `480/1007` | `24204/51949` |
| 12 | 5 | 8/57 | `8/15` | `8/15` |
| 13 | 5 | 8/69 | `4648/7865` | `4648/7865` |
| 14 | 5 | 8/88 | `184870/288387` | `184870/288387` |
| 15 | 5 | 8/104 | `2050/3029` | `2050/3029` |
| 16 | 5 | 8/128 | `3168/4493` | `3168/4493` |

The strict `>2/3` test is met at `N=7..10,15,16`, is exactly equal at `N=6`, and is below at
`N=11..14`.  The gated values have the same classification.

## Results for `c=3/2`

| `N` | `D` | rank/nullity | correlation | gated correlation |
|---:|---:|:---:|---:|---:|
| 6 | 4 | 4/8 | `2/3` | `2/3` |
| 7 | 4 | 4/12 | `3/4` | `18/25` |
| 8 | 5 | 8/16 | `2275/7698` | `287/1125` |
| 9 | 5 | 8/22 | `99/271` | `19467/56171` |
| 10 | 5 | 8/33 | `84/197` | `47106/115633` |
| 11 | 5 | 8/42 | `480/1007` | `24204/51949` |
| 12 | 6 | 10/55 | `485128/1004503` | `485128/1004503` |
| 13 | 6 | 10/67 | `4612584/8778823` | `4612584/8778823` |
| 14 | 6 | 10/86 | `116905/206113` | `116905/206113` |
| 15 | 6 | 10/102 | `303416420/505566459` | `303416420/505566459` |
| 16 | 6 | 10/126 | `3290093/5213637` | `3290093/5213637` |

The strict `>2/3` test is met only at `N=7`, is exactly equal at `N=6`, and is below for `N=8..16`.
The gated values have the same classification.

## Results for `c=7/4`

| `N` | `D` | rank/nullity | correlation | gated correlation |
|---:|---:|:---:|---:|---:|
| 6 | 5 | 8/4 | `1/8` | n/a: no orbit has `C_t>=7` |
| 7 | 5 | 8/8 | `1/5` | `57/334` |
| 8 | 5 | 8/16 | `2275/7698` | `287/1125` |
| 9 | 6 | 10/20 | `1107/3352` | `366/1253` |
| 10 | 6 | 10/31 | `63/163` | `163/438` |
| 11 | 6 | 10/40 | `129596/299021` | `70014/162133` |
| 12 | 7 | 16/49 | `274875/1752668` | `5218070320/33416555403` |
| 13 | 7 | 16/61 | `5889826850/29848675473` | `376631366750/1909147296661` |
| 14 | 7 | 16/80 | `128712863686/548813812183` | `109785647519050/468119368797847` |
| 15 | 7 | 16/96 | `62251198407/234209188402` | `62251198407/234209188402` |
| 16 | 7 | 16/120 | `43286547681/145443144476` | `931330457216523/3136417119828004` |

Every sampled ungated and feasible gated value is below `2/3`.

## Numerical interpretation

The samples show a strong integer-cutoff sawtooth.  Within a block where `D` stays fixed, the
correlation often rises with `N`; when `ceil(c sqrt(N))` increments, it can fall sharply.  For
example, the `c=5/4` sequence drops from `13/15` at `(N,D)=(10,4)` to `480/1007` at `(11,5)`, then
recovers above `2/3` by `N=15`.  Therefore neither a monotone finite trend nor a critical
asymptotic constant can be read from these data.

As a **CONJECTURED numerical diagnostic**, coefficient `7/4` looks too demanding on this range,
coefficient `3/2` is also below threshold after `N=7`, and coefficient `5/4` remains unresolved due
to cutoff oscillations.  This is not an asymptotic obstruction or construction.

A next finite discriminator could either extend the constant-`D` blocks far enough to observe
their full recovery before the next jump, or sample larger `N` selectively around the jump points.
An asymptotic result still requires a uniform coefficient formula and analytic moment identities.

## Reproduction command and hashes

```text
python ksum/tools/ksum_l2p15_intermediate_constant_sweep.py --min-n 6 --max-n 16 --output ksum/artifacts/logs_ksum_L2p15_intermediate_constant_sweep_20260721/results.json
```

SHA-256 before creation of this report:

```text
964F975952B71BA6FFCD44BBEE44E20094C2DDAA762AD3824889E6D38491A988  ksum/tools/ksum_l2p15_intermediate_constant_sweep.py
C1FC6532EF642199EE3E966E4340D71716C95DB8D72BADBBB2304EB235F384F7  ksum/artifacts/logs_ksum_L2p15_intermediate_constant_sweep_20260721/results.json
6F774183B757D7070C9527B401D4F0F23AFF37012C5C6A8DC3028E72F26009EA  ksum/artifacts/logs_ksum_L2p15_intermediate_constant_sweep_20260721/run_command.txt
```
