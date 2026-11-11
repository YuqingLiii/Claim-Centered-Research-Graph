# WHGAP P3 R4 independent review (2026-07-29)

Target node: `WHGAP.qpositive-onset`

Reviewed artifact: `artifacts/whgap_p3_qonset_20260729.md`

Role: reviewer

## PRE-ACTION REPORT

- Target node and disk status: `WHGAP.qpositive-onset`, `NUMERICAL` with
  `pending-review:`.
- Independence statement: I did not author the reviewed work and was given no desired
  outcome.
- Highest licensable tier: `PROVED` for a statement fully established by this fresh
  independent review. The protocol permits an independent checker to write that tier, but
  R4 forbids status writes and leaves status application to a separate decision layer.
- Gate: independently adjudicate claims 1-9 and demonstrably execute rule 7a-7g,
  including the pre-reading anchoring freeze.
- Deliverables: this immutable report; reviewer scripts/logs and hashes under
  `artifacts/logs_whgap_p3_review_20260729/`; a dated node `Adversarial reviews`
  append only; both validators at exit 0.
- Conflict: `research/PRETASK_RELOAD_PROMPT.md` names the WindowsApps Python for
  closeout, while the R4 commission and direct user instruction require
  `C:<home>/cpython3119/python.exe` for every Python invocation. The latter,
  task-specific pinned CPython 3.11.9 was used throughout. No other conflict found.

## Overall adjudication

**PASS with MINOR defects; no MAJOR and no GAP.**

The exact rational rank-two G2(b) certificate is valid. Direct reconstruction from the
frozen Kraus family gives the artifact's exact output and environment characteristic
polynomials, proves every displayed output/environment eigenvalue positive, and yields an
outward-rounded bit-entropy interval strictly above the proposed rational lower bound.
Thus `I_c(rho,783/2000)>0` and `783/2000>x_1` are independently established.

The two material defects are not outcome-changing:

1. The artifact's D2 supporting line
   `I_c(pi,3/4)=-1/4` is false. The correct value is
   `log_2(3)-2<0`. The derivative, sign argument, existence, and uniqueness remain correct.
2. The node accurately discloses that the proposer manifest was generated post-hoc, but
   says it has 19 entries; it has 23. All 23 digests match the present files, but a
   post-hoc manifest is only a present-state snapshot and cannot independently establish
   execution-time immutability.

The word "ceiling" is licensed below only as a finite best-found optimizer picture, never
as a proved upper bound on the all-input supremum.

## Anchoring-ban record (7c)

Before opening any proposer script, artifact table, or execution log, I derived D1 and D2
from the frozen Kraus convention and constructed my own root bracket at 120 scalar decimal
digits and 100 `mpmath.iv` decimal digits. The derivation, code, and raw log were then
hash-frozen in
[`ANCHORING_BOUNDARY_SHA256.txt`](logs_whgap_p3_review_20260729/ANCHORING_BOUNDARY_SHA256.txt).

Frozen hashes:

| Object | SHA-256 |
|---|---|
| `anchoring_independent.py` | `b93188439fd97430408dcc7e892944a6b6996d9c9f123746141d9193e7002fde` |
| `anchoring_derivation.md` | `0c0a8d1a87996d70a312be703eb353588683af928d04a081328112d8e7f5d2b6` |
| `anchoring_independent.log` | `633744442e20ec1c6be111774c4fb036e9079c6eb032feb60cafb9c6f1f9108e` |
| anchoring-boundary file itself | `bfbc502b78973fb3f80d9228e70ad5d4261d56346483b5d486ca9895ca58c13f` |

My independent adjacent rational endpoints were

\[
a=\frac{3909102320761813234827218531341}{10^{31}},\qquad
b=\frac{1954551160380906617413609265671}{5\cdot10^{30}},
\qquad b-a=10^{-31},
\]

with

\[
I_c(\pi,a)\subset
[2.2053778267312532193824580769002535\cdot10^{-31},
  2.2053778267312532193824580769002536\cdot10^{-31}]
\]

and

\[
I_c(\pi,b)\subset
[-1.940219516785425435438747068218287\cdot10^{-33},
 -1.940219516785425435438747068218286\cdot10^{-33}].
\]

After crossing the boundary I found that the proposer selected the same adjacent decimal
rationals and printed the same formulas. This numerical/notational coincidence is flagged
explicitly; the pre-reading hashes establish that it was independently obtained.

## Per-claim verdicts

### Claim 1 - D1 closed form: PASS

Types are `Lambda_x: L(C^3)->L(C^3)` and
`Lambda_x^c: L(C^3)->L(C^4)`, with four Kraus operators
`K_a: C^3->C^3`. For `pi=I_3/3`,

\[
\Lambda_x(\pi)
=\frac{1-x}{3}I_3+\frac{x}{2}\left(I_3-\frac13I_3\right)
=\pi.
\]

The antisymmetric matrices obey `Tr(A_mu)=0` and
`Tr(A_mu A_nu^\dagger)=2 delta_mu,nu`; hence the complement's cross
terms vanish and

\[
\Lambda_x^c(\pi)=\operatorname{diag}(1-x,x/3,x/3,x/3).
\]

With `S(rho)=-Tr(rho log_2 rho)` and `0 log_2 0=0`,

\[
I_c(\pi,x)=\log_2 3+(1-x)\log_2(1-x)+x\log_2(x/3).
\]

The independent direct-Kraus audit also checked Kraus completeness at an exact rational
interior point.

### Claim 2 - D2 derivative and monotonicity: MINOR

Independent differentiation gives

\[
\frac{d}{dx}I_c(\pi,x)
=-\log_2(1-x)-\frac1{\ln2}
 \log_2(x/3)+\frac1{\ln2}
=\log_2\frac{x}{3(1-x)}.
\]

It is strictly negative for `0<x<3/4`. The continuous endpoint values
`I_c(pi,0)=log_2 3>0` and
`I_c(pi,3/4)=log_2 3-2<0`, together with strict decrease, prove exactly one
root on `(0,3/4)`. The verdict is MINOR solely because the artifact instead prints the
false equality `I_c(pi,3/4)=-1/4`; its needed sign is still correct.

### Claim 3 - D3 certified root bracket: PASS

The pre-reading calculation used 120-digit scalar arithmetic only to select adjacent
decimal rationals. Each rational was then embedded as
`iv(numerator)/iv(denominator)` and evaluated using outward-rounded `mpmath.iv` log,
arithmetic, and division by the interval `ln(2)` at 100 decimal digits. The strict signs
and width are printed above. The root is

\[
x_1=0.3909102320761813234827218531341991279\ldots.
\]

The artifact's displayed decimal
`0.3909102320761813234827218531342` is correct. It contains 31 fractional
digits; its first 30 fractional digits are the requested 30-digit value.

### Claim 4 - D4 positivity certificates: PASS

An independent interval evaluation checked the entire proposed rational lower bound,
not a rounded display. The lower interval for `I_c-bound` was respectively about
`1.59068e-51`, `6.31318e-51`, and `9.27909e-51` bits at
`x=1/4,1/3,39/100`. Thus all three strict rational lower bounds are valid.

### Claim 5 - lower-bound principle: PASS

The local RK24 PDF was inspected both textually and visually. PDF page 12, Eqs. (66)-(67),
defines `Q_1` as the all-input coherent-information maximum and `Q` by regularization;
PDF page 14, Sec. 5.4 and Eq. (77), explicitly uses `Q_1(Lambda_x)` as a lower bound for
`Q(Lambda_x)`, and Eq. (78) places a restricted ansatz below `Q_1` and `Q`.
The artifact uses only the pointwise implication

\[
Q(\Lambda_x)\ge Q_1(\Lambda_x)=\sup_\rho I_c(\rho,\Lambda_x)
\ge I_c(\rho,\Lambda_x).
\]

Every numerical entropy in the reviewed certificate is in bits. Natural-log formulas are
divided by `ln 2`; no sign or bound relies on an unstated nat/bit conversion.

### Claim 6 - S1 methodology and picture: MINOR

The proposer's qutrit parameterization uses a complex lower-triangular `3x3` factor with
real diagonal: 3 real diagonal plus 3 complex subdiagonal entries, hence 9 real
coordinates with one scale redundancy. Every positive semidefinite qutrit state admits
such a factorization, including singular ranks, so the state space is not silently
restricted to real or full-rank inputs. The P3 commission's phrase "complex
lower-triangular, 17 real parameters" is itself a count mismatch: 17 is the effective
count for an arbitrary complex `3x3` factor after normalization, not for Cholesky
coordinates.

The frozen results contain exactly 200 restarts at each of ten grid points: one `pi`,
40 diagonal-family, 80 random full-rank, and 79 near-pure starts. Non-successful exits are
reported (five total); each table-winning exit is successful, so no failed solver status
was laundered into a maximum.

For every pure input, the Stinespring output is a pure vector on `C^3 tensor C^4`.
Its two reduced density matrices have identical nonzero spectra, so `I_c=0` exactly.
The independent gate tested three random pure states at both `x=1/4` and `x=49/100`;
all entropy and padded-spectrum residuals were below `9e-16`.

An independent arbitrary-complex-factor optimizer used 21, 22, and 21 restarts at
`x=0.385,0.3915,0.42`, with all exits successful. It reproduced respectively:

- maximally mixed: `0.0132549871199561` bits;
- rank-two-scale positive: `2.97983231867e-7` bits;
- pure floor: `8.78e-14` numerical residual, while exact pure samples gave zero to
  floating error.

The MINOR is terminology/quantifier scope: "ceiling" is not an upper-bound certificate.
It means only the best value found by the finite full-space parameterized search.

### Claim 7 - S2 Hessian threshold: PASS

The traceless Hermitian tangent space decomposes under the frozen `O(3)` action into
real-symmetric traceless dimension 5 and imaginary-antisymmetric dimension 3 sectors.
For a representative `Delta` in each sector with `Tr(Delta^2)=1`, I independently
formed the channel and complement perturbations and applied the entropy divided
difference. This gives exactly

\[
C_{\rm sym}(x)=-\frac{3(x-1)(9x-4)}{4\ln2}
\]

and

\[
C_{\rm asym}(x)=
-\frac{3(x-1)
(4x^2+8x\ln x-8x\ln(3-3x)-19x+12)}
{4(4x-3)\ln2}.
\]

The environment equal-eigenvalue block has squared norm `x^2/4` in both sectors;
the cross-block squared norm is zero in the symmetric sector and `x(1-x)` in the
antisymmetric sector. High-precision direct second differences agreed with the formulas
within `2.2e-21`.

At `x=2/5<x_H`, both sector coefficients are negative. At
`x=21/50>x_H`, the antisymmetric coefficient is positive, while the symmetric one
remains negative. Independent interval evaluation verifies the proposer's width
`10^-31` bracket for

\[
x_H=0.4162325706014828112675191458355\ldots
\]

and proves its left endpoint is strictly above the upper endpoint for `x_1`.
The transformed uniqueness argument is also correct:
`F''(r)=-8(r^2-r+3)/r^2<0` and `F'(15/4)<0`, so `F` decreases for
`r>=15/4`; because `r=3(1-x)/x` decreases in `x`, there is at most one
crossing on `(0,4/9)`, and the interval signs supply existence.

### Claim 8 - S3 two-letter probe: PASS

For two uses the channel acts on `L(C^9)` with 16 Kraus operators of shape `9x9`;
the chosen complement acts on `L(C^16)`. The full factor has 9 real diagonal and
36 complex subdiagonal entries, hence 81 real coordinates with scale redundancy and
full density-matrix coverage.

At each of `x=0.42,0.46,0.49`, the record contains 40 diagonal-simplex starts,
50 correlated directions, and 50 completed full-parameter restarts. The total elapsed
time is `757.2970000000059` seconds against a 1200-second cap. Each displayed family
winner reports a successful solver exit. The comparison baseline is twice the S1
best at the same `x`.

An independent loop-based two-letter construction verified, at all three points,
`I_c(rho tensor sigma)=I_c(rho)+I_c(sigma)` for random product inputs to residual
below `9e-16`, and verified the exact pure-state floor numerically to the same scale.
No S3 value exceeded `2.1e-13` bits, far below the pre-registered `1e-7` follow-up
threshold. "Null" therefore means only no threshold-exceeding candidate in these frozen
families, restarts, points, and time cap; it is not a proof that `Q_1(Lambda_x^tensor 2)`
is nonpositive.

### Claim 9 - G2 interpretation and licensing: PASS

G2(b) is the correct pre-registered branch because the exact rational witness has
strictly positive coherent information at `x=783/2000`, and exact rational comparison
puts that point above the certified upper endpoint for `x_1`. This establishes a point
and, by continuity, some open neighborhood of that point. It neither locates the far
edge of that neighborhood nor determines the exact onset boundary.

**Licensing statement 1 (exact package):** this review does open the completion gate for
"the D1 closed form, D2 monotonicity/uniqueness lemma with the corrected value
`I_c(pi,3/4)=log_2 3-2`, the width-`10^-31` bracket for `x_1`, the D4
certificates, and therefore `Q(Lambda_x)>0` for every `x in (0,x_1)`; additionally,
the exact G2(b) witness at `x=783/2000`", at tier **PROVED**, with scope "the frozen
qutrit channel and complement, bit entropy, single-letter LSD lower bound, the certified
root interval above, the three rational D4 points, and the one exact rank-two witness
point (plus existence, but not endpoints, of a continuity neighborhood); not the exact
small-`x` onset boundary or the whole strip to `1/2`."

**Licensing statement 2 (numerical package):** this review does open the completion gate
for "the numerical single-letter ceiling picture above `x_1` and the two-letter null",
at tier **CERTIFIED\***, with scope "the best-found S1 values from 200 restarts at each
of the ten frozen grid points, independently spot-checked at `0.385`, `0.3915`, and
`0.42`, and the S3 bounded null from the three frozen points, listed families, restart
counts, `1e-7` threshold, and 757.297-second run; 'ceiling' is not an upper bound on the
all-input supremum and 'null' is not a theorem for all two-letter inputs."

These licenses do not license the entire node claim "determine the onset" as PROVED.
The onset boundary remains open.

## Exact G2(b) certificate audit

At `x=783/2000`, `epsilon=1/100000`, the proposed input is a `3x3` Hermitian,
trace-one, positive semidefinite matrix of rank two. Its nonzero principal-block
determinant is exactly `99999/10000000000`, and its spectrum is
`(0,1/100000,99999/100000)`.

Direct characteristic-polynomial checks against the frozen Kraus construction match
the artifact's three output and four environment eigenvalues exactly. Both spectral
lists sum to one. For the potentially delicate environment eigenvalue

\[
\frac{3217}{8000}-\frac{\sqrt{6467990044705822}}{200000000},
\]

the exact difference of squares is

\[
\left(\frac{3217}{8000}\right)^2
-\frac{6467990044705822}{200000000^2}
=\frac{95290147089}{20000000000000000}>0,
\]

so it is strictly positive without decimal inference.

At 100 interval decimal digits, with rational singleton embeddings and an outward-rounded
interval square root,

\[
I_c\in
[0.00000028999308754209583665821303434210409412835388031921374063357\ldots,
 0.00000028999308754209583665821303434210409412835388031921374063358\ldots]
\quad\text{bits}.
\]

Subtracting the proposed exact rational bound inside interval arithmetic gives a lower
endpoint `5.8213034342104094e-26` bits, strictly positive. Every entropy term uses
`-p ln(p)/ln(2)`. This checks exact spectra, positivity, normalization, directed
rounding, and log-base discipline separately.

## Mandatory checklist execution

### 7a - type audit

- Single use: input/output matrices are `3x3`; the complement is `4x4`; each of four
  Kraus matrices is `3x3`.
- Two uses: input/output matrices are `9x9`; the complement is `16x16`; each of 16
  product Kraus matrices is `9x9`.
- The displayed `rho_epsilon` is a qutrit density matrix. Both factor maps produce
  positive semidefinite trace-one matrices whenever the factor is nonzero; their
  zero-factor fallbacks are defined.
- The S1 9-real Cholesky coordinates and S3 81-real Cholesky coordinates cover all
  ranks; they are not real-state restrictions.
- Entropies use base 2 and the sign `S=-Tr rho log_2 rho`.
- "Certified interval" here means an outward-rounded `mpmath.iv` enclosure of the
  exact rational/radical expression, with strict sign determined from the whole
  enclosure. A rounded scalar display is never used as the certificate.

### 7b - regime-complete gates

Independent `I_c(pi,x)` gates:

| Regime point | Independent interval/sign |
|---|---|
| `1/4` | `0.37744375108173427... > 0` |
| `39/100` | `0.0020275769348180569... > 0` |
| one `10^-31` step below the bracket | lower endpoint `4.43015e-31 > 0` |
| one `10^-31` step above the bracket | upper endpoint `-2.24418e-31 < 0` |
| `49/100` | `-0.191380566385020267... < 0` |

The three random pure states at two `x` values, the above-`x_1` optimizer floor at
`x=0.42`, D4 below the crossing, three S1 optimizer characters, the two Hessian sides,
and the two-letter product/pure gates all passed.

Untested regimes are listed separately below.

### 7c - anchoring ban

Executed and hash-frozen before proposer evidence, as recorded in the dedicated section
and boundary file above.

### 7d - no frozen-input immunity

Every displayed `(0,1/2)` formula used by P3 was re-opened. No P1/P2-reviewed
large-`x` fact was used to validate D1-D4, S1, S2, or the G2(b) witness. The separately
reviewed zero-capacity context on `[1/2,1]` is used only to describe what remains open.

### 7e - standing failure modes

- Normalization: Kraus completeness, all trace-one identities, both exact spectral sums,
  and the witness's exact positivity were checked.
- Dimensions/types: audited above.
- Log base: every natural-log entropy/Hessian expression carries `/ln 2`.
- Undefined terms: `floor` means the exactly achievable pure-state value zero;
  `restart` means one local solve from one recorded start; `ceiling` means finite
  best-found scan only; `null` means no value above the registered threshold in the
  frozen finite probe; `certified` means a strict outward-rounded enclosure.
- Partial-for-full substitution: both factor parameterizations cover all density matrices;
  no diagonal or real restriction is used for the full searches.
- Values versus broken derivation: the false `-1/4` line was caught even though all
  numerical root values pass.
- Sign/orientation: proposer objectives minimize `-I_c` and report positive `I_c`;
  independent direct evaluations agree.
- Solver status: failed exits remain counted; every winning S1/S3 record is successful.
- Rounding: exact rational/radical objects are separated from floating optimizer output;
  the G2(b) rational lower bound was checked by interval subtraction.

### 7f - value versus formula decoupling

Verification came from
[`independent_math_audit.py`](logs_whgap_p3_review_20260729/independent_math_audit.py),
[`independent_optimizer.py`](logs_whgap_p3_review_20260729/independent_optimizer.py),
and
[`independent_two_letter_gate.py`](logs_whgap_p3_review_20260729/independent_two_letter_gate.py).
They directly reconstruct the Kraus channel, characteristic polynomials, entropy
intervals, Hessian perturbations, and independent optimizer coordinates. This verifies
the mathematical objects and formulas.

Reproduction is separate: isolated redirected reruns of the proposer calibration,
Hessian, and interval-candidate scripts produced JSON files byte-for-byte identical to
the frozen proposer JSON hashes. The full 2,000-restart S1 and 757-second S3 runs were
not repeated; their claims are supported by code/log inspection plus the independent
spot and structural gates, and remain numerical in scope.

### 7g - quantifier hygiene

- Exact region: for every `x in (0,x_1)`, the single fixed input `pi` has
  `I_c(pi,x)>0`, so there exists an input and `Q(Lambda_x)>0`.
- G2(b): at the single exact point `783/2000`, the displayed rank-two input has
  `I_c>0`; continuity gives some neighborhood, not a certified endpoint for it.
- "Sup over all inputs" is the mathematical `Q_1`; the optimizer tables do not prove
  that supremum.
- "Floor" is exactly zero because every pure input has `I_c=0`.
- "Ceiling picture" and "null" have only the finite numerical scopes stated above.
- "Onset" is not determined by this work. The exact boundary, all unscanned `x`, and
  general higher-blocklength behavior remain open.

## Proposer-manifest bookkeeping audit

[`audit_proposer_manifest.log`](logs_whgap_p3_review_20260729/audit_proposer_manifest.log)
checks all 23 lines of the post-hoc `SHA256SUMS.txt`; every current digest matches. The
node note's count of 19 is incorrect. Because the manifest was created after execution,
it proves only that the files now on disk match that post-hoc snapshot. It does not,
without an execution-time digest, prove that no file changed between the original run
and manifest creation. This is a closeout/provenance MINOR, not a mathematical failure:
the exact core JSON was reproduced byte-for-byte in isolation and the load-bearing
certificate was independently reconstructed.

## Untested regimes

- Any blocklength `n>=3`.
- Exhaustive global optimization over all two-letter inputs; S3 is a finite local search.
- Two-letter ansatz families outside the registered diagonal, one-direction correlated,
  and random full-factor searches.
- A proof of the global single-letter supremum at any scanned point; optimizer maxima are
  best-found values.
- Continuum values of `x` not covered by the analytic maximally mixed region or the one
  exact rank-two witness.
- The endpoints of the rank-two witness's continuity neighborhood and the exact onset
  boundary in `(x_1,1/2)`.
- `x` outside `(0,1/2)` as P3 subject matter; the cited large-`x` campaign results were
  not re-reviewed here.
- RK24's entire optimizer implementation and every literature numerical datum; only the
  cited definition/lower-bound scope and the relevant reported picture were inspected.

## Reproduction and retained logs

All Python invocations used
`C:<home>/cpython3119/python.exe` (CPython 3.11.9). The stable review log
directory contains:

- pre-reading anchor derivation, script, log, and boundary hashes;
- independent math, optimizer, two-letter, and manifest-audit scripts/logs;
- isolated redirected proposer reruns and byte-hash comparison;
- retained failed checker/reproduction attempts, each superseded by a passing log;
- validator logs and final `SHA256SUMS.txt`.

No node status was written by this review.

