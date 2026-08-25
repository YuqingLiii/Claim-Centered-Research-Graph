# k-Sum L2 phase-21 proposer — continuation-seeded block-Fekete exchange

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.continuation-seeded-block-fekete`

Scope: deterministic continuation and bounded width-two exchange at `q=5`, `K=2`

Tier: proposer plus exact finite gates; no independent review and no completion-tier claim

## Decision

**Decision B — continuation produces a real, stable, high-tail circuit path, but the displayed
bounded block exchange remains uniformly subcritical.**

The construction is closed and never reads the current instance's correlation LP optimum or
support.  At the first `N` of each fixed-`D` block it uses the formula-defined Phase-20 interleaved
NO/YES seed.  At every later `N`, it transports the entire previous circuit by same-label nearest
matching in normalized occupancy coordinates, repairs rank only if necessary, and performs at most
two coordinated exchanges involving at most the two worst global dual-residual orbits.

The continuation mechanism succeeds at its narrow purpose:

- every one of the 18 neighboring-`N` transports retains all `R+1` prior support atoms after exact
  rank repair;
- every final support is a legal `rank+1` circuit with exact low-moment cancellation;
- all 21 final kernels pass the `1/4` high-`C_t` mass gate;
- the `D=5` continuation stabilizes at correlations around `0.26..0.39` after its first point;
- the `D=6` continuation recovers from its poor start and stabilizes around `0.19..0.27`.

But it does not approach the required certificate:

- correlation is below `2/3` in all 21 cases;
- the global dual bound fails in all 21 cases;
- `D=7` remains extremely small, rising smoothly only from `4.35e-6` to `1.46e-4`;
- no case terminates with a valid dual certificate.

Thus the path instability of restarted Phase-20 exchange was real and is repaired, but stability
alone selects a stable **suboptimal** branch.  Increasing exchange width or iteration depth until
the exact optimum is found would cease to be a formula and become an algorithmic restatement of
solving the finite LP; this phase explicitly does not make that move.

## 1. Closed block-start seeds

For each fixed `D` block, the first values are

```text
(D,N_0)=(5,11),(6,17),(7,24).
```

At `N_0`, use exactly the Phase-20 seed:

1. Sort NO orbits by decreasing product of their two occupied totals, then total-balance gap and
   canonical index.
2. Sort YES orbits by decreasing `C_t`, then decreasing total product, total-balance gap, and index.
3. Interleave the two lists, beginning with NO.
4. Take the pivot columns of the orbit-feature matrix in this order and append the first later
   column producing a full fundamental circuit.

This seed is formula-defined and uses no finite optimum.

## 2. Deterministic transport from `N` to `N+1`

Let the final circuit at `N` be

`S_N={H_1,...,H_{R+1}}`

with normalized cofactor weights `w_N(H)`.  Sort its atoms by decreasing `|w_N(H)|`, breaking ties
by the canonical orbit index.

For a canonical orbit

`H=((r_1,u_1),(r_2,u_2))`,

write its flattened normalized occupancy vector as

`x_N(H)=(r_1,u_1,r_2,u_2)/N`.

For each old atom in the stated order, choose an unused legal orbit `H'` at `N+1` with the **same
YES/NO label**, minimizing the exact lexicographic key

```text
( ||x_N(H)-x_{N+1}(H')||_1,
  |C_t(H)/N^2-C_t(H')/(N+1)^2|,
  current canonical orbit index ).
```

This gives a deterministic injective transport of the support.  It uses only the previous circuit
and the current legal orbit list, not the current optimal support.

### Exact rank repair

If the transported `R+1` columns are not a full circuit, order the current columns with transported
ones first and the closed Phase-20 interleaved order second.  Take the pivot basis in that order and
append the first remaining column whose fundamental circuit has no zero coefficient.

In the completed experiment the repair never discarded a transported atom:

```text
D=5: all 9/9 transported atoms retained at N=12..16;
D=6: all 11/11 retained at N=18..23;
D=7: all 17/17 retained at N=25..31.
```

So the measured paths are genuine nearest-neighbor continuations, not repeated restarts hidden
inside the repair step.

## 3. Bounded coordinated exchange

For a circuit `S`, define its normalized kernel `w`, correlation `c(S)`, tail mass `T(S)`,
support-interpolating dual polynomial `P_S`, and global residual

`M(S)=max_H |f_t(H)-P_S(H)|`

exactly as in Phase 20.  The merit remains

`Phi(S)=c(S)^2/M(S)`

when `T(S)>=1/4`, and zero otherwise.

At each current `N`, perform at most **two** exchange steps.  In one step:

1. Order all legal orbits by decreasing exact dual residual, breaking ties by orbit index.
2. Test two entering blocks: the first outside-support worst orbit alone, and the first two
   outside-support worst orbits together.
3. Form a deletion pool consisting of four support atoms, ordered by label compatibility with the
   entering block, then increasing `|w(H)|`, then index.
4. For a singleton entry test all four singleton deletions.  For a two-orbit entry test all six
   pairs from the fixed four-atom pool.
5. Discard noncircuits and candidates with tail mass below `1/4`; choose the exact lexicographic
   maximum of `(Phi,c,T,-support indices)` and accept only a strict improvement.

Thus at most ten neighboring supports are examined per step and at most twenty per `N`.  Width,
pool, depth, objective, and tie breakers are independent of `N`, the orbit count, and the hidden LP
optimum.

## 4. Why this is not an LP restatement

The algorithm does evaluate the current support's dual residual on all legal orbits; that is the
mandatory global certificate gate.  It does **not** optimize over arbitrary measures or supports.
Its search neighborhood is permanently bounded:

```text
entry width <=2,
deletion pool =4,
exchange steps per N <=2,
candidate supports per N <=20.
```

The transport performs nearest matching and unisolvent rank repair only.  Neither step scores
candidate supports by the final correlation LP.

Allowing block width, deletion pool, or exchange depth to grow until the best circuit is found
would amount to a combinatorial solver for the finite LP support.  Since the fixed bounded rule
fails the decisive gates, this memo records Decision B instead of silently expanding the search.

## 5. Three complete continuation paths

| fixed-`D` block | final correlation range | post-start stable range | tail range | dual-ratio range |
|:---|---:|---:|---:|---:|
| `D=5`, `N=11..16` | `0.135..0.390` | `0.261..0.390` | `0.253..0.565` | `6.10..36.2` |
| `D=6`, `N=17..23` | `0.00723..0.269` | `0.194..0.269` | `0.402..0.620` | `11.3..701` |
| `D=7`, `N=24..31` | `4.35e-6..1.46e-4` | same scale | `0.622..0.962` | `2.04e4..2.85e5` |

Every block is complete.  Exact pointwise results are archived in the JSON logs.

### `D=5`

The transported seed improves from `0.1358` at `N=12` to `0.3092,0.3483,0.3897,0.4149` before
the bounded exchanges.  Final correlations are

```text
N=11: 959/7106              approximately 0.1350
N=12: 77664/297647          approximately 0.2609
N=13: 207683/671733         approximately 0.3092
N=14: 116096/322931         approximately 0.3595
N=15: 1709379/4386560       approximately 0.3897
N=16: 924800/2417067        approximately 0.3826
```

This is a coherent finite path, but it remains separated from `2/3`, and its dual ratios stay at
least `6.10`.

### `D=6`

The block start is poor (`0.00723` after two exchanges), but continuation carries a much better
branch from `N=18` onward:

```text
0.1942, 0.2280, 0.2402, 0.2510, 0.2606, 0.2691.
```

The path is stable and all tails exceed `0.53` after `N=18`, yet the global residual remains
between roughly 11 and 25 times the candidate epsilon after recovery.

### `D=7`

Transport retains all 17 support atoms at every step and tail mass rises from `0.622` to `0.962`.
Correlation also increases monotonically through the transported path, but only from

`1/229923 approximately 4.35e-6`

to

`1968261384/13495073001767 approximately 1.46e-4`.

This is stable continuation of the wrong branch, not evidence of eventual constant correlation.

## 6. Stop ledger and exact gates

Four cases use the full fixed two-step budget: `N=11,12,17,18`.  The other 17 stop at a bounded
block local optimum.  No case stops because the global dual bound passes.

| gate | result |
|:---|:---|
| start seeds defined without LP | PASS |
| deterministic same-label `N -> N+1` transport | PASS |
| injective full-support transport | PASS in all 18 transitions |
| bounded width-two coordinated exchange | PASS by construction |
| no current optimal support/LP oracle | PASS |
| all three fixed-`D` blocks complete | PASS: 21 exact cases |
| legal `rank+1` circuits | PASS in every case |
| zero mass and all degree-`<D` moments | PASS exactly |
| unit `l1` | PASS exactly |
| tail mass at least `1/4` | PASS in 21/21 |
| correlation strictly above `2/3` | **FAIL in 21/21** |
| global dual residual bound | **FAIL in 21/21** |
| large-`q` endpoint | NOT TESTED; the `q=5` rule already fails |

## 7. Scoped boundary and untested escape

The proposer-tier boundary is:

> Same-label normalized-occupancy continuation can transport an exact selective circuit without
> rank loss and can stabilize correlation and high-tail mass across a fixed cutoff block.  A fixed
> width-two, two-step block exchange nevertheless follows a uniformly subcritical branch and does
> not control the global dual residual.

This does not refute a genuinely analytic support flow.  It does rule out treating an increasingly
wide/deep finite support search as the missing formula: once the search parameters grow toward the
whole orbit set, the route is simply solving the LP by another name.

A **continuum-limit Remez support flow**, in which limiting support locations and cofactor weights
satisfy explicit differential/algebraic equations before lattice rounding, is a distinct escape.
Under Rule 8 it must be registered before any calculation or proof.  It is only named here and was
not tested.

## 8. Reproduction and provenance

Driver:
`ksum/tools/ksum_l2p21_continuation_block_exchange.py`

Commands:
`ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/run_commands.txt`

Exact logs:

```text
ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/d5_block.json
ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/d6_block.json
ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/d7_block.json
```

SHA-256:

```text
DDC6B263B28D95A3ADC819264BE99D99A868AC1CF9BA07C9190E911AD293E6F9  ksum/tools/ksum_l2p21_continuation_block_exchange.py
7F84BDFF9A2AC37B241C28291FCF82CE47EF9DEBD3F5F65E39437B86F1C17E11  ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/run_commands.txt
78B23A5AA6DF7490B65C17D9D903A76C1ADEE1D0459A205D7E3CA55468562D0E  ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/d5_block.json
33B70419C06CEAFA48A56A2B4AA770B2C2C2A8D65FF45764DB6A36BD5AD640DE  ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/d6_block.json
2654829ECC53BA414DCF02C5EEDD2F81530E838AB723F40D9838B399367F0AEE  ksum/artifacts/logs_ksum_L2p21_continuation_block_exchange_20260721/d7_block.json
```

No `PROVED`, `CERTIFIED*`, or `REFUTED` conclusion is claimed.
