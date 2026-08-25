# k-Sum L2 phase-20 proposer — label-aware Fekete/Remez basis exchange

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange`

Scope: deterministic local basis exchange at `q=5`, `K=2`

Tier: proposer plus exact finite gates; no independent review and no completion-tier claim

## Decision

**Decision B — the displayed deterministic label-aware Fekete/Remez exchange is not a uniform
construction.**

The rule is closed and does not query the final correlation LP or the Phase-16 optimal supports.
It starts from a basis selected jointly from balanced NO-boundary and high-`C_t` balanced YES
orbits, forms its first full fundamental circuit, then performs worst-dual-residual exchanges with
an exact objective combining cofactor correlation and global dual fit.

All 21 exact cases in the three consecutive `c=5/4` cutoff blocks were completed:

```text
D=5,  11<=N<=16;
D=6,  17<=N<=23;
D=7,  24<=N<=31.
```

Every final support is legal, has `rank(F_<D)+1` columns, a one-dimensional full cofactor kernel,
zero mass, and exact annihilation of all orbit-feature rows below `D`.  Yet none reaches
correlation `2/3`; the best is only `102/455 approximately 0.2242` at `(N,D)=(13,5)`.  Two `D=5`
cases also fail the `1/4` tail gate.  Every global dual bound fails, with violation ratios ranging
from `12.1` to `6.88e6`.

A wider all-deletion ablation at `(17,6)` is genuinely suggestive: after 12 exact exchanges it
reaches correlation

`159661393/247663793 approximately 0.64467`

and dual ratio `1.17075`, but remains below `2/3`.  The identical wider rule at `(23,6)` stops after
one exchange at correlation `0.0001314` and dual ratio `64568`.  Thus the near-success is isolated,
not a block-stable formula.

This is a scoped failure of the stated initialization, single worst-residual insertion, and
small-cofactor deletion rule.  It does not refute arbitrary label-aware or block-exchange supports.

## 1. Closed initialization

For every legal orbit `H=((r_1,u_1),(r_2,u_2))`, define

```text
s_i = r_i+u_i,
C_t(H)=r_1u_1+r_2u_2,
B(H)=s_1s_2.
```

Split the orbit list into NO and YES lists.  Sort them deterministically as follows:

- NO: decreasing `B(H)`, then increasing `|s_1-s_2|`, then the canonical orbit index;
- YES: decreasing `C_t(H)`, then decreasing `B(H)`, then increasing `|s_1-s_2|`, then index.

Interleave one NO orbit and one YES orbit, beginning with NO.  Scan this order and retain the first
columns which increase the exact orbit-feature rank.  Equivalently, take the pivot columns of the
feature matrix after permuting its columns into this interleaved order.  Stop after `R=rank(F_<D)`
columns.

This is a label-aware Fekete-style unisolvent basis: boundary and balanced interior columns are
chosen jointly, unlike Phase 19's near-boundary lexicographic staircase.  Let `C` be its exact
`R x R` feature matrix.  In the same interleaved order, choose the first nonbasis column `j` for
which every coordinate of `C^{-1}F_j` is nonzero.  The initial support is the resulting full
fundamental circuit of size `R+1`.

No correlation optimum, dual optimum, or previously computed support enters this definition.

## 2. Exact circuit state and dual residual

For a circuit support `S`, compute its unique null vector `w`, orient it so
`<w,f_t>>=0`, and normalize `||w||_1=1`.  Put

```text
c(S) = <w,f_t>,
T(S) = sum_{H in S, C_t(H)>=ceil(D^2/4)} |w(H)|.
```

The support-interpolating dual polynomial `P_S=F^T y_S` is defined by

`f_t(H)-P_S(H)=c(S) sgn(w(H))` for every `H in S`.

Compatibility and uniqueness follow from `Fw=0`, unit `l1`, and rank `R`.  Evaluate it on **every**
legal orbit and set

`M(S)=max_H |f_t(H)-P_S(H)|`.

The closed exchange score is

`Phi(S)=c(S)^2/M(S)`

when `T(S)>=1/4`, and zero otherwise.  This rewards both absolute signed correlation and proximity
to a globally valid equioscillation certificate.  It is not the final LP objective: `P_S` is
interpolated from the current circuit, and no optimization over all measures is performed.

## 3. Deterministic exchange rule

At each step:

1. Let `h_*` be the lexicographically first orbit attaining `M(S)`.
2. Order the current support columns for deletion by:
   same label as `h_*` first, then increasing `|w(H)|`, then orbit index.
3. Examine the first four deletion candidates.  For each, insert `h_*`, discard candidates that
   are not full circuits or have tail mass below `1/4`, and compute the exact new score.
4. Choose the candidate maximizing the lexicographic merit

   `(Phi,c,T,-support_indices)`.

5. Accept only a strict merit increase.  Stop at a strict local optimum, when no tested exchange
   is a tail-feasible full circuit, when the global dual bound passes, or after `2R` exchanges.

The width four, `2R` cap, initialization, objective, tie breakers, and stopping rules are fixed in
advance and apply identically to all 21 main gates.

The wider ablation replaces width four by every support deletion while changing nothing else.  It
was run only at two preregistered-node diagnostic points and is not used to define the main result.

## 4. Exact three-block gates

### Main width-four rule

| block | exact cases | final correlation range | tail gate | dual-ratio range | exchanges |
|:---|---:|---:|:---|---:|:---|
| `D=5`, `N=11..16` | 6 | `0.000401..0.2242` | 4/6 PASS | `12.1..5162` | `0..4` |
| `D=6`, `N=17..23` | 7 | `0.000131..0.000821` | 7/7 PASS | `2187..74468` | `1..2` |
| `D=7`, `N=24..31` | 8 | `2.40e-7..9.20e-6` | 8/8 PASS | `2.85e5..6.88e6` | `0..2` |

No case reaches `2/3`, and no candidate dual polynomial satisfies the global residual bound.

The failed `D=5` tail cases are:

```text
(N,D)=(14,5): T=0.22828...;
(N,D)=(16,5): T=0.20534....
```

Twelve cases stop because none of the four deterministic deletion candidates gives a full-circuit
tail-feasible exchange.  The other nine stop at a strict local score optimum.  No case reaches the
iteration cap or a valid global dual certificate.

The worst residual is no longer always the same balanced orbit as in Phase 19.  It alternates
between balanced interior YES atoms and near-boundary `C_t=1` YES atoms, showing that the
boundary/interior initialization repairs one hole only by exposing another.

### Wider deletion ablation

| case | exchanges | exact correlation | tail mass | dual ratio | stop |
|:---|---:|---:|---:|---:|:---|
| `(17,6)` | 12 | `159661393/247663793` | `1291860471/3467293102` | `1.17075` | strict local optimum |
| `(23,6)` | 1 | `3365/25611596` | `42436503/51223192` | `64567.8` | strict local optimum |

The first case is close enough to show that exact worst-residual exchange can find a meaningful
selective circuit without an LP oracle.  But it still misses both decisive inequalities:
correlation is below `2/3`, and the dual ratio exceeds one.  Its collapse at the other end of the
same cutoff block rules out treating it as a uniform formula.

## 5. Why the rule fails

The rule solves only a one-orbit exchange problem.  The current worst dual residual is inserted,
but preserving a full circuit and high-tail mass can require several coordinated deletions and
insertions.  With one insertion fixed:

- many states have no tail-feasible full-circuit deletion among the label-balanced small-cofactor
  candidates;
- other states improve `Phi` but become strict local optima with a different large residual;
- parity and lattice rounding change which near-boundary or balanced orbit is worst;
- a good exchange path at `N=17` does not persist to `N=23`, even though `D=6` is unchanged.

The score itself is not the missing ingredient: the `(17,6)` wider run makes both correlation and
dual fit nearly viable.  The obstruction is path stability and the locality of single-entry
exchange.  No recurrence or continuation principle chooses the successful path uniformly in `N`.

## 6. Gate ledger

| gate | result |
|:---|:---|
| deterministic closed initialization | PASS |
| jointly selected NO boundary and balanced YES columns | PASS |
| no final-LP or Phase-16-support oracle | PASS |
| three complete consecutive cutoff blocks | PASS: 21/21 completed exactly |
| legal `rank+1` full circuits | PASS in every final state |
| zero mass and all degree-`<D` moments | PASS exactly |
| unit `l1` | PASS exactly |
| tail mass at least `1/4` | FAIL in 2/21 main gates |
| correlation strictly above `2/3` | **FAIL in 21/21** |
| global dual residual bound | **FAIL in 21/21** |
| stable exchange path across one fixed-`D` block | FAIL |
| large-`q` endpoint | NOT TESTED; the `q=5` rule already fails |

## 7. Scoped boundary and untested escape

The proposer-tier boundary is:

> A closed single-worst-residual, single-entry label-aware Fekete exchange can dramatically improve
> an individual selective circuit, but the displayed initialization/deletion rule has no stable
> path across `N`.  It fails constant correlation, global equioscillation, and occasionally the
> tail constraint across three consecutive cutoff blocks.

This does not cover coordinated multi-entry exchanges or a support path continued jointly in
`(N,D)` rather than restarted at every instance.

A **continuation-seeded block-Fekete exchange**, replacing several orbit columns simultaneously
and transporting support between neighboring `N`, is a distinct escape.  Under Rule 8 it must be
registered before any computation or proof.  It is only named here and was not tested.

## 8. Reproduction and provenance

Driver:
`ksum/tools/ksum_l2p20_label_aware_exchange.py`

Commands:
`ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/run_commands.txt`

Main exact logs:

```text
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d5_block.json
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d6_block.json
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d7_block_a.json
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d7_block_b.json
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d7_block_c.json
```

Wider ablation:

```text
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/wide_n17_d6.json
ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/wide_n23_d6.json
```

SHA-256:

```text
124507C3AE26FC1EB9055325D31A39EEB1348C6CA2A62594C07FE58D1AE70B28  ksum/tools/ksum_l2p20_label_aware_exchange.py
A8B5777FF85328C321BA49A7814B400D0C382F3E44480B1BF5B0D5F32B9ACA4C  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/run_commands.txt
EF1E77864E2868156C777FD796F6B0D92096EB390687DAD41743724C964A83E4  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d5_block.json
473B3A1312EA454F3574D8025A05E5492B1C5E1880005750F23D0829BECEC8CA  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d6_block.json
4FEA2A8E55632ECB6800FA6D491FAE856B19266BB4C7D105030BFD3BE1C24265  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d7_block_a.json
6BF6300A06E3CA605B3B39EA0E222C5E6DFD7621DD16634CA4C5BFA36F9FF46D  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d7_block_b.json
19FBF0E7B3DB24410CCCB79272F51D3840BE00D0FB6C2EF825C8A444DB3D7316  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/d7_block_c.json
833A95F4895828518BC38DF745DE188B2DD9CDB12F2F848EFA251B567765E04D  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/wide_n17_d6.json
28719D02C0C7400AB04CEEAC93AE3F82B3F62B6D38E860339F87BDBC9D9E6F63  ksum/artifacts/logs_ksum_L2p20_label_aware_exchange_20260721/wide_n23_d6.json
```

No `PROVED`, `CERTIFIED*`, or `REFUTED` conclusion is claimed.
