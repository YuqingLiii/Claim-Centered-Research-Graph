# Independent review: Werner centered 4096-threshold refinement

Date: 2026-08-30

Reviewer: independent Codex adversarial-review context `/root/q3_threshold_review`.

## Independence and scope

I did not author
`artifacts/WERNER_CENTERED_THRESHOLD_REFINEMENT_20260830.md`, the canonical target node, or any
of its ten load-bearing premise nodes. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full,
read the target artifact and canonical node, inspected every premise claim and its linked
completion review, and independently reconstructed the sector partition and every displayed
`m,N,d,H` power. I also recomputed the integer endpoint with exact rational arithmetic. I did not
use Chrome, webpage ChatGPT, an external source search, a running SU(3) certificate, or another
agent. I made no canonical-node change; this immutable review is my only repository mutation.

This review is limited to the following proposition and route:

- canonical claim `HEXT.same-tuple-werner-centered-bound-4096-threshold`, exact repository hash
  `sha256:4bbc6ff3ff3542426b8baf1b02361c071f7250c63538d1f3bc8cc557bcdd8991`;
- route `unabsorbed-planar-log-moment`, exact implication hash
  `sha256:266332d6f57b98cdc86296b077657794df14568453c0b8baafa92c4e74190877`.

It does not review or imply arbitrary-Hermitian same-tuple strong convergence, the physical
global `n=2` estimate, any all-copy theorem, absolute-unbounded leakage, or the
Hayden--Penington full-size extensive-violation root.

## 1. Executive verdict

**PASS.** The route implication at `266332...` and the exact claim at `4bbc6f...` are eligible for
`PROVED`. All ten listed premises are currently `PROVED`, their exact claims are sufficient, and
the new assembly does not import a stronger hidden statement from any premise.

The threshold improvement is legitimate. The connected planar sector may be bounded directly by

\[
  16m^2N^2\left(\frac{4096}{m}\right)^N,
\]

instead of first absorbing `16N^2` into `32768^N`. After division by `H^N`, the only
unsuppressed nonreturn exponential base is therefore `a=4096/(mH)`. The strict condition
`mH>4096` gives `a<1`; the return base `u=(3m-4)/(m^2H)` is independently less than one for every
`m>=2`; and the positive-genus and disconnected sectors have additional `d^(-2)` handle ratios.
An even logarithmic moment then gives the asserted probability limit.

The uniform integer endpoint is exact: `m=932063` fails and `m=932064` passes at `eta=0`, while
the defining expression is strictly increasing in both `(1+eta)^2` and `m`. The word “uniform”
applies to the sufficient integer threshold over `eta>=0`; the probability limit still fixes
`m,eta` before `d->infinity`.

## 2. Immutable inspected objects

The exact bytes inspected had the following SHA-256 digests:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| threshold-refinement artifact | `59b7d50e1fe85a11166d4d5dd657ce12abb44604fe10874e961967ec32aa8f3c` |
| target canonical YAML | `3e81211a81606b9ee9abcf75f609441028d38f493fbeb3c4491b336537516ffb` |

The repository-normalized target hashes were independently recomputed from the current YAML:

| reviewed statement | exact hash | result |
|---|---|---|
| node claim | `sha256:4bbc6ff3ff3542426b8baf1b02361c071f7250c63538d1f3bc8cc557bcdd8991` | exact match; PASS |
| route implication | `sha256:266332d6f57b98cdc86296b077657794df14568453c0b8baafa92c4e74190877` | exact match; PASS |

The load-bearing premise claims inspected were:

| premise | exact claim hash | level |
|---|---|---|
| `HEXT.werner-centered-reversal-return-bound` | `sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a` | `PROVED` |
| `HEXT.werner-contraction-skeleton-ribbon-injection` | `sha256:288e0f5df3ca6a53915325c487648184b9be0ff950c1e52c5db7689468c730f7` | `PROVED` |
| `HEXT.werner-planar-two-boundary-rooted-map-count` | `sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8` | `PROVED` |
| `HEXT.werner-minimal-catalan-weight` | `sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54` | `PROVED` |
| `HEXT.werner-positive-genus-two-boundary-weighted-count` | `sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6` | `PROVED` |
| `HEXT.werner-admissible-equality-component-genus-bound` | `sha256:443c7023066be044f8795ef5d036a159f652ccb78bb6b51d15d0a95904791651` | `PROVED` |
| `HEXT.werner-two-component-low-genus-return-separation` | `sha256:c523f97093f9490b81572424cc273a25e9224cdbff285506d7a376dc304e9724` | `PROVED` |
| `HEXT.werner-two-component-nonreturn-weighted-count` | `sha256:16edb16e7ddcce4a044c0fe7608bc73bfe530a0fad52e02fc9f1a05fe7488c32` | `PROVED` |
| `HEXT.werner-monotone-weingarten-tail-summability` | `sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4` | `PROVED` |
| `HEXT.werner-constellation-euler-deficit` | `sha256:c1c37d08c4f0cf37cb698b26a03d48cef0dd668686b71ed3a8391fed63c1d62a` | `PROVED` |

The relevant completion findings were also inspected: `WCMF-IR-08` and `WCCIA-01` for the return
atom; `WPCS-IR-01--03` for the constellation injection and Euler power; `WTPR-IR-01--04` for the
planar map count and its `e=4N` application; `WMSC-IR-03` for the Catalan normalization;
`WTBC-IR-01--03` for the positive-genus count; `WECG-IR-01--09` for equality components,
low-genus separation, and the residual two-component mass; and `STDW-IR-05--06` for the exact
monotone-path source and skeletonwise geometric tail. No adverse finding attached to the current
hash of any listed premise.

## 3. Findings

### Finding WCTR-IR-01 — PASS: the partition is exhaustive and nonoverlapping in the required sense

Centering removes exactly the diagonal `v=a` terms. The exact trace expansion is first split into
the union of forward-return and block-reversed-return edge sequences and its complement. The
return atom bounds that union directly and therefore already handles all Weingarten behavior of
those sequences.

For every nonreturn balanced term, the lossless constellation encoding has `c` equal to one or
two because its two fixed physical boundary cycles are unions of topological components. The
complement therefore splits into

```text
c=1,h=0; c=1,h>=1; c=2,h<=1; c=2,h>=2.
```

The `c=2,h<=1` part is empty in the nonreturn complement by the proved low-genus separation. The
remaining three sectors are precisely the three bracketed contributions in the refined master
inequality. The monotone excess is then summed skeletonwise on the nonreturn complement. This
exhausts all nonzero Haar terms; no cancellation is assumed.

**Verdict:** PASS.

### Finding WCTR-IR-02 — PASS: connected planar term and the constant `4096`

The ribbon injection sends a connected Werner skeleton with `E=2N` constellation darts to a map
with `e=2E=4N` ordinary edges and two ordered directed face roots, without a factorial or color
multiplier. The planar map theorem gives

\[
 R_{e,0}^{(2)}\le e^2\binom{2e}{e}.
\]

Using `e=4N`, `binom(2e,e)<=4^e`, and the minimal Catalan weight
`16^N=2^e`, the total planar minimal weight is bounded by

\[
 e^2 4^e 2^e=(4N)^2 8^{4N}=16N^2\,4096^N.
\]

For connected `c=1,h=0`, the equality bound is `kappa<=N+2` and the Euler power is one. After
the `m^(-2N)` moment normalization, the planar nonreturn mass is therefore

\[
 m^{-2N}m^{N+2}\,16N^2 4096^N
 =16m^2N^2\left(\frac{4096}{m}\right)^N.
\]

After division by `H^N`, this is exactly `16m^2N^2a^N`. The polynomial was not lost, and no
`32768` witness hidden inside an aggregate premise was imported.

**Verdict:** PASS.

### Finding WCTR-IR-03 — PASS: connected positive-genus sum and `x_43`

For each `h>=1`, the structural minimal-weight premise gives
`4096^N N^(43h)`, the equality theorem gives `kappa<=N+2+2h`, and the connected Euler theorem
gives `d^(-2h)`. Thus the normalized minimal mass is at most

\[
 m^{-2N}m^{N+2+2h}4096^N N^{43h}d^{-2h}
 =m^2\left(\frac{4096}{m}\right)^N
  \left(\frac{m^2N^{43}}{d^2}\right)^h.
\]

Summing from `h=1` produces exactly

\[
 m^2\left(\frac{4096}{m}\right)^N\frac{x_{43}}{1-x_{43}}.
\]

The premise's structural `h>=1` statement is universal in `m`; its separate consequence for
`m>e^18` is not used here. Hence the threshold-refinement route is valid for every fixed
`m>=2,eta>=0` satisfying its own displayed condition.

**Verdict:** PASS.

### Finding WCTR-IR-04 — PASS: disconnected starting genus and `x_24`

All two-component terms with total genus `h<=1` are already inside the return union. For `h>=2`,
the exact residual premise gives the minimal-path mass

\[
 \left(\frac{4096}{m}\right)^N m^2N^{24}
 \left(\frac{m^2N^{24}}{d^2}\right)^{h-1}.
\]

Consequently, summing from `h=2` gives

\[
 m^2\left(\frac{4096}{m}\right)^N
 N^{24}\frac{x_{24}}{1-x_{24}}.
\]

The outside `m^2`, the extra `N^24`, and the initial `d^(-2)` suppression are all present. In
particular, no disconnected `d^2` or `d^0` nonreturn term remains unbounded.

**Verdict:** PASS.

### Finding WCTR-IR-05 — PASS: monotone-Weingarten factor

For a fixed skeleton the proved monotone-tail statement bounds all positive total excess by
`theta/(1-theta)` times its minimal-path absolute weight, with

\[
 \theta=\frac{6(2N)^{7/2}}{d^2}.
\]

Adding the minimal path gives exactly the common multiplier `(1-theta)^(-1)`. The premise already
convolves excess allocations across active labels, so no extra composition or factorial factor is
needed. Applying it after restricting to nonreturn skeletons is legitimate because the estimate
is skeletonwise and positive.

Combining Findings WCTR-IR-02--05 gives precisely

\[
 \frac{\mathbb E\operatorname{Tr}(S_U^N)}{H^N}
 \le 2d^2u^N+
 \frac{m^2a^N}{1-\theta}
 \left[16N^2+\frac{x_{43}}{1-x_{43}}
 +N^{24}\frac{x_{24}}{1-x_{24}}\right].
\]

**Verdict:** PASS for the master inequality.

### Finding WCTR-IR-06 — PASS: `a<1`, `u<1`, and logarithmic moment

The route hypothesis is exactly `(mH)^2>4096^2`, so it gives the strict exponential margin
`a=4096/(mH)<1`. For `b=(1+eta)^2>=1`,

\[
 (mH)^2=(18mb+81b^2)(1-m^{-2}).
\]

The denominator of `u` is `m^2H=m(mH)`. At the worst case `eta=0`, exact expansion gives

\[
 m^2(mH)^2-(3m-4)^2
 =18m^3+72m^2+6m-97>0 \qquad(m\ge2).
\]

Thus `0<u<1` for every permitted `m,eta`; the threshold is imposed only by the unsuppressed
planar nonreturn term.

For any fixed permitted `m,eta`, choose
`N(d)=2ceil(gamma log(d)/2)` with `gamma>2/log(1/u)`. Then
`N=gamma log d+O(1)` is even,

```text
d^2 u^N -> 0,       N^2 a^N -> 0,
x_43 -> 0,          x_24 -> 0,          theta -> 0.
```

The remaining positive-genus and disconnected expressions are products of these vanishing
geometric ratios with `a^N` and fixed powers of `N`, so they also tend to zero. The
Collins--Matsumoto tail premise is uniform for every fixed logarithmic coefficient; there is no
upper constraint conflicting with the required lower bound on `gamma`.

**Verdict:** PASS.

### Finding WCTR-IR-07 — PASS: even-moment domination and Markov

`S_U=R_U-I_(d^2)/m` is Hermitian. For even `N`, every eigenvalue satisfies
`|lambda|^N=lambda^N`, hence

\[
 \|S_U\|_\infty^N\le\operatorname{Tr}(S_U^N).
\]

The sectorwise absolute estimates upper-bound the expectation of the right-hand side. Markov's
inequality therefore yields

\[
 \Pr\{\|S_U\|_\infty>H\}
 \le\frac{\mathbb E\operatorname{Tr}(S_U^N)}{H^N}\longrightarrow0.
\]

No concentration inequality, limiting spectral law, or cancellation claim is needed.

**Verdict:** PASS.

### Finding WCTR-IR-08 — PASS: exact endpoint `932063/932064`

For fixed `m`, the threshold expression is strictly increasing in
`b=(1+eta)^2>=1`, so its minimum occurs at `eta=0` and equals

\[
 q(m)=(18m+81)(1-m^{-2})
 =18m+81-18/m-81/m^2.
\]

Moreover

\[
 q'(m)=18+18/m^2+162/m^3>0
\]

for `m>0`. Independent exact integer arithmetic gives

\[
 q(932063)-4096^2
 =\frac{-868758213184}{868741435969}<0,
\]

and

\[
 q(932064)-4096^2
 =\frac{14768619324399}{868743300096}>0.
\]

The second fraction reduces by a factor of nine, but the artifact's unreduced form is exact.
Therefore `932064` is the smallest integer for which this proof's strict condition holds for
every `eta>=0`.

Solving the same quadratic in `b` also gives the stated sufficient condition for smaller `m`,

\[
 (1+eta)^2>
 \frac{-m+\sqrt{m^2+4096^2/(1-m^{-2})}}{9}.
\]

**Verdict:** PASS.

### Finding WCTR-IR-09 — PASS with strict quantifier and scope boundary

The exact theorem quantifies over every integer `m>=2` and every fixed `eta>=0` satisfying the
strict parameter inequality, and only then takes `d->infinity`. The corollary `m>=932064` removes
the need to check the inequality for each `eta`, but it does not assert a probability convergence
uniform in a varying `eta(d)`.

The proof controls only `R_U-I_(d^2)/m` for the centered real-Werner coefficient sector at one
two-leg reuse of a fixed Haar tuple. It does not establish arbitrary-Hermitian same-tuple strong
convergence, the physical global `n=2` estimate, any all-copy result, absolute-unbounded leakage,
or the Hayden--Penington full-size root. The old broader centered node remains distinct.

**Verdict:** PASS only at the reviewed scoped claim and route hashes.

## 4. Promotion recommendation

The integrator may:

1. link this review at Findings `WCTR-IR-01--WCTR-IR-09` to route implication hash
   `sha256:266332d6f57b98cdc86296b077657794df14568453c0b8baafa92c4e74190877`;
2. promote that route from `CONJECTURED` to `PROVED`;
3. link this review at the same findings to exact claim hash
   `sha256:4bbc6ff3ff3542426b8baf1b02361c071f7250c63538d1f3bc8cc557bcdd8991`;
4. promote only `HEXT.same-tuple-werner-centered-bound-4096-threshold` to `PROVED`, remove its
   discharged review frontier, and append the corresponding route and node level-change events;
5. preserve the strict scope caveat and all historical negative or superseded routes; and
6. regenerate generated views and run structural, evidence-closure, scope, and contract checks.

No broader Question 3 node is licensed to change level from this review.

## 5. Limitations

This is an absolute-moment upper bound and does not identify the true optimal threshold. The
condition `mH>4096` is sharp only relative to the present uncancelled planar upper bound: when
`mH<=4096`, the available term `16m^2N^2a^N` cannot vanish for any required
`N(d)->infinity`. A smaller threshold would require a better planar exponential base, a
reviewed cancellation theorem, or a different moment argument.

This review uses the ten existing `PROVED` premise claims and checks that their exact public
interfaces suffice for the new assembly; it does not re-prove the Collins--Matsumoto external
theorems, the Akemann--Ostrand norm identity, or the complete rooted-map deletion code from first
principles.
