# Independent hostile review — KSUM.B4b.L2 corrected repair

Date: 2026-07-19  
Reviewer: fresh independent completing reviewer; authored none of the target work; no wanted verdict  
Network: not used  
Commits: none  
Scope: the corrected-threshold exact LP rerun, cap-compatible P4 statement, P2 re-grade,
preregistration record, and synchronized route summaries

## Pre-action reload

Before reviewing or changing status I reloaded from disk the research-structure protocol, the
proof-DAG protocol including completion rule 6, the KSUM node index, KSUM.B4b.L2 and parent
KSUM.B4b, the prior hostile review and defects D1--D4, the repair addendum, both repair drivers, and
the complete repair-log directory. I also checked the current KSUM whole-DAG view, prover prompt,
B4/B4a/root nodes, the paper's exact B4a and middle-gap quantifiers, its cycle-type discussion, and
the local Tani source's standard 0/1 approximate-degree convention. No network or git commit was
used.

Fresh review code, importing neither repair script nor repair output:

- [ksum/tools/ksum_l2rr_exact_review.py](../tools/ksum_l2rr_exact_review.py)
- [exact rational output](logs_ksum_L2rr_20260719/exact_review.log)
- [pre-status-action provenance audit](logs_ksum_L2rr_20260719/provenance_review.log)
- [review SHA-256 manifest](logs_ksum_L2rr_20260719/SHA256SUMS.txt)

## Ruling

**OPEN — independent repair review completed; finite corrected LP table proved, but the registered
P4 obligation still has a quantifier-scope defect.**

D1 and D3 are discharged. The cap arithmetic that repairs D4 is correct at every stated point, and
the finite exact table is proved by this completed independent rerun. However, the addendum calls
an all-`q`, all-target lemma the exact route obligation. The paper's actual middle-gap problem only
needs odd `q`, where all targets have the same involution cycle type. For even `q`, the addendum
also demands both `tau=0` and `tau=2` target classes with uniform constants; C7 does not identify
those two classes. This is a stronger open problem, not the route-minimal lemma, and the addendum
does not label it as an optional strengthening. The route is repairable and is not refuted.

## D3 — corrected direct-error predicate

Let `F` be `-1` on NO inputs and `+1` on YES inputs. If a `T`-query algorithm has error `e`, its
acceptance probability `A` has degree at most `2T`, and its expected-sign polynomial
`p=2A-1` satisfies

\[
  \deg p\le 2T,\qquad \lVert p-F\rVert_\infty\le 2e.
\]

At `e=1/3`, the uniform error is `2/3`. If a unit-`l1` witness `mu` annihilates every polynomial of
degree below `d`, then for any such `p`,

\[
  |\langle\mu,F\rangle|
  =|\langle\mu,F-p\rangle|
  \le \lVert\mu\rVert_1\lVert F-p\rVert_\infty
  \le 2/3.
\]

Thus only correlation **strictly greater than `2/3`** excludes the approximant. Equality gives no
contradiction and does not certify. This is the sign-rescaled version of the paper/Tani standard
0/1 convention, where the acceptance polynomial itself approximates the Boolean output to error
`1/3`.

The repair solver uses exact `optimum > 2/3`, and its verifier independently asserts the same strict
comparison. The fresh reviewer script separately found four equality bands — single degrees 1 and
2 at `(3,3,0)` and `(4,3,0)` — and counted none of them.

### Independent exact table

| Point | Basis | Exact optima by degree | Certified degree (`>2/3`) |
|---|---|---|---:|
| `(3,3,0)` | single | `2/3, 2/3, 1/9` | 0 |
|  | joint | `1, 1, 1/2` | 2 |
| `(4,3,0)` | single | `2/3, 2/3, 1/6, 1/6` | 0 |
|  | joint | `1, 1, 5/9, 3/8` | 2 |
| `(5,4,1)` | single | `1, 1, 11/21, 25/63, 1/11` | 2 |
|  | joint | `1, 1, 5/7, 3/5, 1/11` | 3 |

All 24 independently reconstructed witnesses have exact `l1=1`, exact correlation equal to the
reported rational optimum, and zero exact rational residual in every falling-factorial moment row.
Therefore the corrected finite certified-degree claims `(0,2)`, `(0,2)`, and `(2,3)` are **PROVED
as finite LP claims by this review**. This proves no asymptotic degree or exponent statement.

**D3 verdict: DISCHARGED.**

## D4 — cap repair and quantifiers

Put

\[
  L_\eta(N,q)=\min\{\sqrt N\,q^\eta,N^{2/3}\},
  \qquad \eta\in(1/6,1/4].
\]

For every `3<=q<=N`:

- `L_eta(N,q) <= N^(2/3)`, so it never exceeds the range-independent Johnson walk cap.
- Since `eta<=1/4`, `L_eta(N,q) <= sqrt(N) q^eta <= sqrt(N) q^(1/4)`, so it lies below B4a's
  `N^(1/2+epsilon) q^(1/4)` upper bound even before using the `N^epsilon` slack.

The crossover is exactly

\[
  \sqrt N q^\eta\le N^{2/3}
  \iff q^\eta\le N^{1/6}
  \iff q\le N^{1/(6\eta)}.
\]

At `eta=1/4`, this is `q=N^(2/3)`. For every `eta>1/6` the crossover lies below `N`, and the
minimum supplies the Johnson plateau above it. The addendum's more elaborate above-crossover
comparison with B4a is also correct.

The order `exists eta,c0,delta,N0; forall N,q,t; exists mu_(N,q,t)` is the right order for one
fixed exponent improvement and uniform constants. The issue is the domain of the universal
quantifiers:

- The paper's registered problem `prob:k2-gap` is for odd `q` in the middle regime. C7/translation
  makes every target equivalent there (`tau=1`).
- For cyclic even `q`, even targets have `tau=2` and odd targets have `tau=0`. C7 preserves a fixed
  cycle type; it does not identify these two types.
- The addendum nevertheless requires every `3<=q<=N` and every target with the same constants, and
  the node calls this the exact obligation. That includes both even-`q` types, a result strictly
  stronger than needed to close the registered odd-`q` gap.

Required repair: register the route-minimal statement for odd `q` and all targets (or the desired
single even-`q` cycle type), or explicitly label the all-`q`, all-target statement as an optional
strengthening while retaining a separately stated minimal obligation. If the stronger version is
intended, its uniformity across `tau=0,1,2` must be named rather than attributed implicitly to C7.

**D4 verdict: cap contradiction DISCHARGED; full registered-lemma repair NOT DISCHARGED because of
new defect D7 below.**

## D1 and D2 — P2 bookkeeping

Every current repair summary inspected — the node, addendum, parent, whole-DAG view, and prover
prompt — treats P2 as only the 25--27 percentage-point shell deficit. References to full 100%
joint-orbital capture call it automatic, tautological, or a construction check. The immutable
phase-1 report still contains its historical projection table, but already says full capture is
expected from commutant membership and identifies the shell loss as the discriminator; the review
and addendum explicitly supersede any earlier gloss.

The repair does not claim a one-input discriminator, optimizer uniqueness, a complete
Belovs--Spalek shell-algebra separation, or asymptotic expressiveness.

**D1 verdict: DISCHARGED.**  
**D2 verdict: prior disposition correctly preserved; no new discriminator was supplied or claimed.**

## Preregistration integrity

All eleven hashes in the repair `SHA256SUMS.txt` matched before the reviewer status edit. Relevant
UTC filesystem times are:

| File | Created | Last written |
|---|---|---|
| `predictions.txt` | 19:16:59.583 | 19:16:59.585 |
| corrected solver | 19:18:53.120 | 19:18:53.121 |
| corrected verifier | 19:18:56.044 | 19:18:56.046 |
| exact results | 19:19:47.409 | 19:19:47.409 |
| verifier log | 19:19:54.141 | 19:19:54.204 |

The first executor transcript ended on a sandbox-helper failure before any repository read or write.
The successful transcript records the predictions patch before either solver patch, then records the
solver invocation. The preregistration hash in the later manifest matches the current file and its
transcript content. The manifest itself was created after the run, so manifest line order alone is
not proof of chronology; the timestamps and transcript ordering supply that evidence. I found no
sign of post-hoc editing. This cannot prove the stronger unknowable claim that nobody had seen the
previous reviewed spectrum — indeed the predictions openly use that spectrum.

## New defect

| ID | Severity | Defect | Effect / required repair |
|---|---|---|---|
| D7 | MODERATE | The registered “exact” P4 obligation universally quantifies all even-`q` targets, hence both `tau=0` and `tau=2`, although the paper route to be closed only needs odd `q`; C7 does not bridge the even cycle types. | Scope the canonical route lemma to odd `q`/all targets, or state the all-cycle-type version as an optional strengthening and name its additional uniformity burden. |

## Additional hostile attacks

- **Threshold convention: PASS.** The expected-sign rescaling exactly matches the standard 0/1
  acceptance-polynomial convention; strictness is necessary, not stylistic.
- **G11: PASS.** The addendum, node, parent, whole-DAG view, and prompt consistently state that
  degrees 2 and 3 at `N<=5` are finite machinery/separation evidence only. No exponent fit is made.
- **Status/caveat before review: accurate.** `CONJECTURED · pending-review` correctly described the
  proposer-authored repair. Because D7 remains, this review returns the node to `OPEN · independent
  repair review completed`; it does not clear the route at CONJECTURED.
- **No over-kill.** The cap-compatible formula is algebraically viable and the finite joint gains
  are exact. D7 is a scope repair, not a counterexample to the joint-histogram approach.

## Status action

KSUM.B4b.L2 is set to **OPEN — independent repair review completed; D7 quantifier-scope repair
required**. The finite corrected LP table is proved as a finite claim inside this review. The
asymptotic witness lemma remains open and unproved. KSUM.B4b, KSUM.B4, and the root remain OPEN.

## What I did not check

- I did not construct the asymptotic pair-lattice kernel, prove conditioning preserves moments, or
  prove uniform norm/correlation bounds for any cycle type.
- I did not rerun the expensive optimizer extraction, prove optimizer uniqueness, or create a
  one-input/held-out P2 discriminator.
- I did not test additional `(N,q,t)` points or involution cycle types.
- I did not independently re-prove the Johnson walk or B4a algorithm; I checked their reviewed
  on-disk quantified statements and the cap algebra used here.
- I did not exhaust all Belovs--Spalek shell algebras.
- I did not use the network.
