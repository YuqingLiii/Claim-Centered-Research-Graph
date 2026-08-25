# Independent definition-level review: T5 raw colour normalization

Date: 2026-07-22  
Scope: review artifact only; no DAG, notes, paper, `ksum`, or git-history edit

## Verdict

**CONFIRMED_REFUTATION.** The registered physical operators use the raw
horizontal sum over the `m=C(j,a)` colours.  They are not divided by
`sqrt(m)`.  Both tame `c=2` final contraction scripts instead combined
`|d_(gamma,mu)|^2` with `r_mu=||t_mu||^2/m`; this evaluates the registered
physical trace divided by `m`.

Restoring the missing `m=20` produces two exact, strictly tame physical
counterexamples to (T-a).  The same error reaches the claimed uniform (T-b)
proof, although the two corrected finite (T-b) gates themselves still pass.

## 1. Definition audit

The conclusion is fixed before reading any prior verdict:

- T3 equation (3.2) states `S_(h,gamma) S_(h,gamma)^* = m K_gamma`, with
  `m=C(j,a)`.  Thus `S` is the raw coloured synthesis map.
- The common-line report defines `F` by summing all coloured fibres.  Its
  `1/sqrt(m)` factor is explicitly optional and may be used only if the inverse
  factor is absorbed into the branch scalar.  Its physical branch mass is
  `a_(gamma,mu)=||v_(gamma,mu)||^2`.
- The tame `R_out` witness stores both quantities and verifies exactly
  `a_(gamma,mu)=m|d_(gamma,mu)|^2`.
- The canonical T5 node asks for the *physical actual pairings*, so silently
  replacing `S` by `S/sqrt(m)` changes the registered obligation.

The independent non-tame `c=2` matrix witness gives a direct convention gate.
For every long/tail branch, the saved physical matrix `K_gamma` is the
horizontal stack of 20 colour blocks and

`||K_gamma L||_HS^2 / ||(K_gamma/sqrt(20))L||_HS^2 = 20`.

Its raw long value is `58443/1024`, exactly the previously direct physical
value.  This check uses the archived matrices, not a prior scalar verdict.

## 2. Exact reconstruction from the archived witnesses

For each tame gate the review reads the exact archived `d^2` and `q_mu`
numerator/denominator arrays.  It independently recomputes `f^mu` by the hook
formula and then uses

`||t_mu||^2 = C(n-1,j) f^theta q_mu/f^mu`,

`r_mu=||t_mu||^2/m`, and

`a_(gamma,mu)=m|d_(gamma,mu)|^2`.

Therefore the raw block contribution has two independently identical forms:

`f^mu a_(gamma,mu) r_mu = f^mu |d_(gamma,mu)|^2 ||t_mu||^2`.

The review does not take either archived final `T_a` value as an arithmetic
input.  It recovers the old divided value only as a diagnostic equality.

| gate | corrected raw physical `T_a` | cap | exact excess | cap ratio |
|---:|---:|---:|---:|---:|
| `n=18,j=6,a=b=3,c=2` | `160582822829/85260` | `51396202/35` | `35381674757/85260` | `36224413/28242984 > 1` |
| `n=19,j=6,a=b=3,c=2` | `204466088827/71920` | `137582445/64` | `199431265033/287680` | `10611004/8023575 > 1` |

Hence both earlier tame `c=2` (T-a) PASS verdicts are wrong.  This is an
actual failure of the registered physical inequality, not a failure of a
surrogate estimate.

## 3. T-b consequence

The common-line tail formula has the same branch mass
`a_(z,mu)=m|d_(z,mu)|^2`.  Writing
`h_mu=sum_z |d_(z,mu)|^2`, the raw trace is

`T_b(raw)=m sum_mu f^mu r_mu h_mu`.

The carrier/effective-rank theorem correctly bounds
`R_h=sum_mu f^mu r_mu=||(F/sqrt(m))L_h||_HS^2`, and the output frame correctly
bounds `h_mu`.  Their combination therefore bounds `T_b(raw)/m`, not
`T_b(raw)`.  The advertised uniform physical (T-b) closure is invalid and
must be reopened.

This is not yet a (T-b) counterexample.  Direct exact reconstruction gives:

| gate | corrected raw physical `T_b` | cap | result |
|---:|---:|---:|---:|
| `n=18` | `67576575391/22252860` | `51396202/1015` | PASS |
| `n=19` | `8391760923/2229520` | `137582445/1984` | PASS |

## 4. Existing j=1 through j=5 T-a certificates

The review traced the actual source formulas, not their labels:

- `j=1`: `m=1`, so raw and normalized conventions coincide.
- mixed `j=2`: the exact physical sum explicitly multiplies by
  `M=(n-1)(n-2)=C(n-1,2)C(2,1)`.
- `j=3`: the orbital engine uses
  `M=C(n-1,3)C(3,a)` and `T_a=M*fixed_sum`; the killer value agrees with the
  direct raw T3 matrix value.
- `j=4`: scalar engines use `M=C(n-1,4)C(4,a)`; matrix packets use the same
  raw `M` in `T` or cancel the same raw orbit factor in the ratio, and regress
  to the raw scalar/orbital gates.
- `j=5`: scalar engines use `C(n-1,5)C(5,a)` explicitly.  Matrix/local-DP
  certificates evaluate the fixed-state orbital sum divided by
  `f^alpha f^beta`; this is exactly the ratio after the same raw colour-state
  factor is cancelled from physical `T_a` and its cap.  Their j4 regression
  checks the convention.

Because a second audit disputed this point, the review also performed a full
coloured enumeration at `n=15,j=5,a=2`.  For a fixed coloured source there
are exactly

`C(14,5) C(5,2) = 2002*10 = 20020`

coloured targets, not 2002 uncoloured targets.  The code's `pair_count`
formula agrees with the exhaustive enumeration in all 40 four-overlap types
and sums to 20020.  Two mixed local-DP families were then checked term by
term from their stored signed orbitals:

| packet/family | full coloured-sum ratio | archived ratio | result |
|---|---:|---:|---:|
| theta `(3,2)`, `a=2,alpha=(1,1),beta=(2,1)` | `67173/104650` | `67173/104650` | exact |
| theta `(3,1,1)`, same split | `267437/417312` | `267437/417312` | exact |

For the raw trace, the outer source orbit contributes the same
`M=C(14,5)C(5,2)` that appears in
`T=M f^alpha f^beta`; it cancels once in the ratio.  Multiplying either ratio
again by `C(5,2)=10` double-counts the colour factor already present in both
`pair_count` and `T`.  The theta32 and theta311 scripts both call this same
audited `family_ratio` engine.  Therefore the contrary “all 50 mixed
certificates need an extra m” interpretation is rejected by exhaustive
counting, not by convention.

Thus no missing-`m` defect was found in the archived `c=1`, `j<=5` orbital
certificates.  Their inequality verdicts remain valid.  What fails is the
two tame `c=2` final reduced contraction and any later argument identifying a
raw physical trace with a normalized-fold Hilbert--Schmidt norm.

## 5. Route and root adjudication

- **T-a:** `CONFIRMED_REFUTATION`.  Uniform registered physical (T-a) is
  false.  T5's required target is therefore refuted, not merely blocked.
- **T-b:** no finite counterexample here, but the all-parameter proof is
  invalid by exactly one factor `m`; the sub-obligation must be reopened.
- **T2:** its claimed endpoint is the same uniform physical (T-a).  The exact
  four-overlap formula may remain correct, but it cannot prove a false target;
  T2 cannot remain the conjectured route keeping TRACE alive.
- **Original SE/root:** not refuted by these witnesses.  (T-a)/(T-b) are a
  sufficient decomposition used by this trace route, not an equivalence to
  the original SE lower-bound claim.  Other routes or a joint/cancellation
  estimate could still succeed, so only the current proof-route status must
  fall.

No DAG, note, handoff, paper, `research/ksum`, or git-history file was changed.
No commit was made.
