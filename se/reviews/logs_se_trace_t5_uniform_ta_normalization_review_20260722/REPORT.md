# Independent review: physical colour normalization in T-a/T-b

Date: 2026-07-22  
Node family: `SE.denom.Phi.legal.trace`

## Verdict

**CONFIRMED WITH A MATERIAL SCOPE CORRECTION.**  The two tame `c=2`
physical T-a counterexamples in `uniform_ta_two_frame` are correct, and the
uniform effective-rank argument loses the raw colour factor
`m=C(j,a)`.  However, this defect does **not** invalidate the `c=1`
four-overlap/target-local certificates: their `pair_count` already sums all
physical coloured targets, and the same factor occurs in `T` in the cap.
Multiplying those stored ratios by `m` again would double-count colour.

## 1. Raw definition and where `m` belongs

The original T3 definition states, with `m=C(j,a)`,

`S_gamma S_gamma^* = m K_gamma`

and gives nonzero `A_gamma=S_gamma^*S_gamma` eigenvalues `m k_(gamma,mu)`.
The original raw majorization implementation horizontally stacks every
physical coloured branch without a `1/sqrt(m)` normalization.

For a `c=1` orbital calculation, let

`N=C(n-1,j)`, `M=N C(j,a)`.

The raw trace is `M` times a fixed-colour row sum.  The physical cap is
`B_theta(2n)^2 T`, where `T=M f^alpha f^beta`.  Thus `M` cancels in the
ratio.  The target-local routine implements exactly the remaining fixed-row
formula: its four-overlap `pair_count` sums to `M`.

### Minimal sealed j5 reproduction

For `theta311_a1_alpha1_beta31` at `n=15`:

| quantity | exact value |
|---|---:|
| stored ratio | `127304/207207` |
| `m=C(5,1)` | `5` |
| `N=C(14,5)` | `2002` |
| `M=N m=sum(pair_count)` | `10010` |
| `T=M f^alpha f^beta` | `30030` |
| `B_theta(30)` | `28/23` |
| raw cap | `23543520/529` |
| raw trace from `M B^2 fixed_row_sum` | `998063360/36501` |
| raw trace / raw cap | `127304/207207` |
| cap minus raw trace | `626439520/36501` |

The tempting extra multiplication gives `636520/207207`, but it counts the
same `m=5` twice.

This conclusion has an independent full-state check.  The earlier T2 source
explicitly enumerates all coloured states, reconstructs the raw trace as
`M * fixed_row_sum`, and agrees exactly with `family_ratio` at all five
`j=2,n=4` rows:

`4/15, 19/45, 3/7, 8/21, 1/3`.

Therefore the sealed theta32/theta311 and related `c=1` certificates are not
invalidated by this particular normalization issue.

## 2. The actual c2 contraction bug

The compressed tame gates use `r_mu=||t_mu||^2/20`.  Their R-out tables store
both `d_squared=|d|^2` and `a_mass=20|d|^2`, but the final scripts contract
`d_squared*r_mu`.  The registered raw definition requires
`a_mass*r_mu`.  There is no orbital `M`/cap cancellation at this final
compressed contraction.

Joining the original R-out and R-col tables independently gives:

| gate | corrected raw T-a | T-a cap | ratio | corrected raw T-b | T-b cap | ratio |
|---:|---:|---:|---:|---:|---:|---:|
| `n=18` | `160582822829/85260` | `51396202/35` | `36224413/28242984 > 1` | `67576575391/22252860` | `51396202/1015` | `5198198107/86677717896 < 1` |
| `n=19` | `204466088827/71920` | `137582445/64` | `10611004/8023575 > 1` | `8391760923/2229520` | `137582445/1984` | `17565172/323617525 < 1` |

Thus physical T-a fails at both exact tame gates.  Physical T-b still passes
these two finite gates, but the claimed uniform T-b proof bounds the divided
quantity and must be reopened.

## 3. Proof-state consequences

- **T5:** its uniform physical T-a claim is refuted.  The uniform physical
  T-b proof is reopened; the two corrected finite T-b gates are not
  counterexamples.
- **T2:** its exact `c=1` full-state/orbital identities and finite gates
  survive.  Its proposed all-parameter route to physical T-a cannot prove a
  false universal statement because of the two `c=2` counterexamples.
- **TRACE:** the registered universal T-a inequality is false, so TRACE
  cannot remain supported by T2/T5 as presently formulated.
- **Root lower-bound theorem:** the theorem itself is not directly refuted
  by failure of this sufficient trace inequality.  Its current TRACE/T2
  proof chain is unsupported; absent another route, the proof status should
  be treated as open rather than inherited as conjectured through T2.

The theta41 run was stopped before interpolation: PID 45136 is gone, with
84/96 raw samples through complete `m=23`, zero symbolic kernels, and zero
family certificates.  No prior artifact, DAG, note, paper, `research/ksum`
file, or git history was modified.
