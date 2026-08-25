# Independent review — T6 assembly-weighted joint route

Date: 2026-07-22  
Scope: independent review of `logs_se_trace_t6_joint_20260722/` and
`logs_se_trace_t6_joint_gate_scan_20260722/`; no DAG edit and no commit

## Verdict

**CONFIRMED, with DAG-semantic and provenance caveats.**  The two packets'
raw normalization, exact `n=18/n=19` fractions, 59 certified `c=1` gates,
old-`M_phys` refutation, and no-physical-cross-term conclusion are correct.
They are enough to register a distinct **OPEN** T6 research route.  They do
not prove the uniform route or license any ancestor promotion.

Two qualifications are load-bearing:

1. T6 is an assembly-weighted positive joint route, not a destructive
   cross-term-cancellation route.  All physical branch cross terms are zero.
2. The current TRACE Claim still literally states the now-false separate
   `(T-a)/(T-b)` conjunction.  A propagating `T6 -> TRACE` child edge is
   sound only if TRACE is simultaneously restated as the canonical joint
   trace frontier.  Otherwise T6 belongs under/reformulating GRAM and TRACE
   should be only a non-propagating related node.

## 1. Exact operator and normalization audit

Write

`B_(h,gamma)=P_comp Q_gamma A_h P_xi`

and

`R_h=omega B_(h,0)-sum_z B_(h,z)`.

Since `[P_comp,Q_gamma]=0` and the `Q_gamma` are pairwise orthogonal,

`B_(h,gamma)^* B_(h,gamma')=0` for `gamma != gamma'`.

Therefore

`||R_h||_HS^2 = omega^2 T_a(raw)+T_b(raw) =: J_h`.

Right matching covariance makes the fixed-`h` HS trace equal to its matching
average.  The reviewed twirl has Schur form `I_d tensor M_xi`, so

`J_h=d Tr(M_xi)`, where `d=f^kappa f^nu`.

There is no factor `c` in this trace identity.  In the two tame `c=2`
archives, the stored `d_(gamma,mu)^2` contractions are divided by the colour
fold `m=C(6,3)=20`; the review restores that factor exactly once to obtain
raw `T_a,T_b`.  After this restoration, neither `m` nor `c` appears again.
The original `c=1` sweep already totals all physical colours, so applying an
extra `m` there would double-count.

This resolves the raw-normalization question:

`divided branch data --multiply by m once--> raw T_a,T_b --omega^2 joint--> J --divide by d--> Tr M_xi`.

## 2. Relation among the three targets

Under the rebuilt exact canonical interface

`G_can = r_top/(B_theta(q)^2 omega) M_xi`, `M_xi >= 0`,

the exact necessary-and-sufficient target is

`M_xi <= (15/4) B_theta(q)^2 omega I_c`.                    (P)

The direct scalar trace condition

`J_h <= (15/4) B_theta(q)^2 omega d`                        (CT)

is sufficient because `||M_xi|| <= Tr(M_xi)=J_h/d`; it is not necessary for
`c>1`.

The historical constant-preserving condition

`J_h <= B_theta(q)^2 T [omega^2+1/(delta_min+1)]`            (JT)

is a different sufficient route.  Combined with the already recorded tame
hook arithmetic it reproduces the historical `(F3.47)` envelope, hence the
`15/4` goal.  JT is not equivalent to (P).  Its finite success comes from
the small coefficient `omega^2` and unused tail allowance, not from branch
interference.

The current GRAM node remains `CONJECTURED`.  Thus the canonical coefficient
must be named as a rebuilt input/obligation of T6; the original
`se_gramdirect_20260719.md` formula must not be silently cited as an already
proved theorem.

## 3. Independent exact `c=2` recomputation

The review does not read either T6 JSON.  It loads manifest-verified original
`R_col/R_out` data, rebuilds hook dimensions, `p0`, `omega`, `B`, `T`, and
`d`, and restores raw `m=20` once.

| gate | `omega` | raw `J_h` | `J_h/JT` | `J_h/CT` | old raw `M_phys` / cap |
|---|---:|---:|---:|---:|---:|
| `n=18` | `6173/29667` | `132950061300160/1571846661` | `2556731948080/3452466241653` | `40907711169280/831256340602941` | `314047397248/158949 > 51396202/35` |
| `n=19` | `13465/69223` | `404454069049888/3632863495` | `3660217819456/4953985056825` | `553691131961344/11397981418779375` | `413148057504/139345 > 137582445/64` |

The corresponding trace upper bounds on `G_can/r_top` are exactly

- `51134638961600/277085446867647` at `n=18`;
- `138422782990336/759865427918625` at `n=19`.

Both are below `15/4`.  Old `M_phys` is refuted independently of its tail
details because raw `T_a>B^2T` already, and the explicit weighted sums above
confirm the full failures.

## 4. Independent `59`-gate interval propagation

All source interval endpoints were parsed as exact decimal rationals and
propagated only through positive coefficients.  Results:

| target | pass count | tightest certified upper ratio |
|---|---:|---:|
| old `M_phys <= B^2T` | `59/59` | `0.9000012910879944` |
| JT | `59/59` | `0.3035451078282223` |
| CT | `59/59` | `0.10666666668835943` |

These are finite consistency gates only.  The two exact raw `c=2` failures
supersede any universal old-`M_phys` inference from the `c=1` rows.

## 5. Recommended OPEN node contract

- ID/alias: `SE.denom.Phi.legal.trace.t6` / `T6`
- Kind/role/status: `LEAF` / `proof` / `OPEN`
- Claim: for every admissible strict sector, prove (P) for the reflected
  multiplicity block.  CT or the sharper JT may be recorded as sufficient
  scalar discharge routes for the exact joint trace
  `J_h=omega^2 raw T_a+raw T_b=d Tr(M_xi)`.
- Inputs: FOUND's typed physical branches, reflection, matching covariance
  and Schur form; the rebuilt canonical normalization; raw physical traces
  with colour-fold multiplicity retained.
- Output: `||G_can|| <= (15/4)r_top` uniformly, without an LR multiplicity
  loss.
- Parent: TRACE only after TRACE's Claim is broadened to the canonical joint
  frontier.  If that semantic edit is not made, parent/reformulation should
  be GRAM and TRACE should be `related` only.
- Related: GRAM, FOUND, T5 (reusable raw witnesses), and MPHYS (refuted
  stronger positive target/history).

Do not revive the old positive `M_phys`, normalized per-`mu` `g_mu`, a
branch-index Schur/cross-term rescue, or scalar/rank-one LR-colour shortcuts.

## Reproduction

Run the two commands in `COMMANDS.txt`.  The first rebuilds the independent
JSON/log from manifest-bound pre-T6 sources; the second checks the saved
invariants.
