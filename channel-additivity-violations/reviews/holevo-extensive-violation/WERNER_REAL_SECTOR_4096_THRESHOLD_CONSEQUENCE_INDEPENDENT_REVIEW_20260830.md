# Independent review: real-Werner consequence under the centered 4096 threshold

Date: 2026-08-30

Reviewer: independent Codex adversarial-review context `/root/q3_real_4096_review`.

## Independence and scope

I did not author the target node, either load-bearing premise, or
`artifacts/WERNER_REAL_SECTOR_4096_THRESHOLD_CONSEQUENCE_20260830.md`. I read
`DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full, inspected the current target and premise nodes,
the target artifact, the two premise artifacts, and the independent completion findings bound to
the premise claims. I independently redid the two-dimensional coefficient optimization, the event
identification, the probability-quantifier transfer, and the integer-endpoint check. I used no
subagent and made no canonical-node change. This immutable review report is my only repository
mutation.

The review is limited to:

- claim `HEXT.same-tuple-real-werner-sector-4096-threshold`, exact hash
  `sha256:73ea83e47b97862ffccdd54b1bcee83c261b4b655dae73001b535d536a94bd28`;
- route `centered-4096-event-plus-spectral-equivalence`, exact implication hash
  `sha256:e68b489d9db13b26ced14ea980a11894835480bb7e0defe13812480f899fbd78`.

It does not review or imply an arbitrary-Hermitian coefficient estimate, a physical global `n=2`
optimization, any all-copy statement, absolute-unbounded leakage, or Hayden--Penington full-size
extensive violation.

## 1. Executive verdict

**PASS.** The exact route implication at `e68b489d...` and the exact node claim at
`73ea83e4...` are eligible for `PROVED`, in that order. Both listed premises are currently
`PROVED` at the hashes inspected below. Their public statements suffice without a hidden
assumption.

For every fixed unitary tuple, the centered spectral event from the first premise is exactly the
simultaneous real-Werner coefficient event in the target, by the deterministic equivalence in the
second premise. The two event sets are therefore equal for every output dimension `d`; this is not
a one-way implication or an asymptotic comparison. The first premise's fixed-`m`, fixed-`eta`,
then-`d->infinity` probability limit and its exact eta-uniform integer corollary transfer verbatim.

## 2. Immutable inspected objects and exact hashes

The exact bytes inspected had the following SHA-256 digests:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| target canonical YAML | `0de7371c6be4eb7046f5701202f84f76e540862cfd7617837326162a1b6427ff` |
| target consequence artifact | `707e8f3b6374255df23a1aab8bb7fe1272c977b9a9a8ea3261d77224294e98c2` |
| centered-threshold premise YAML | `1a4cab48a5e84b3aa8abb76b8594b856a2fac9046e4680a54673aa772ce8d8aa` |
| spectral-reduction premise YAML | `40521efd59f271785b2b09b31e13c649380866020dff4e079e2d6c8b15225a70` |
| centered-threshold premise artifact | `59b7d50e1fe85a11166d4d5dd657ce12abb44604fe10874e961967ec32aa8f3c` |
| spectral-reduction premise artifact | `5a9dc94ec0f02f76065f87134244dcde4781486d112d194dbcbc8ec73de9f056` |
| centered-threshold independent review | `77682919603cb08e7df1f8b535c6b613d3b2ded76bff977116f9d525b9ef2026` |
| spectral-reduction independent review | `6c2651600430e3455a963def1c0884a29e6a935e777c4ac5bd6657e1e81df088` |

The repository-normalized hashes are `sha256(statement.strip())` after YAML folding and CRLF
normalization. I recomputed:

| reviewed statement | exact hash | result |
|---|---|---|
| target claim | `sha256:73ea83e47b97862ffccdd54b1bcee83c261b4b655dae73001b535d536a94bd28` | exact match; PASS |
| target route implication | `sha256:e68b489d9db13b26ced14ea980a11894835480bb7e0defe13812480f899fbd78` | exact match; PASS |

The two load-bearing premise interfaces are:

| premise | exact claim hash | current level | relevant completion finding |
|---|---|---|---|
| `HEXT.same-tuple-werner-centered-bound-4096-threshold` | `sha256:4bbc6ff3ff3542426b8baf1b02361c071f7250c63538d1f3bc8cc557bcdd8991` | `PROVED` | `WCTR-IR-01--WCTR-IR-09` |
| `HEXT.same-tuple-werner-spectral-reduction` | `sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67` | `PROVED` | `STGW-IR-06` |

No adverse finding is attached to either current premise hash.

## 3. Findings

### Finding WRS4096-IR-01 — PASS: identity dimensions, normalization, and Hilbert--Schmidt norm

The coefficient identity `I_(m^2)` and flip `F_m` act on
`C^m tensor C^m`; the output identity `I_(d^2)` and `R_U` act on
`C^d tensor C^d`. In the established same-tuple convention,

\[
 M_U(I_{m^2})=I_{d^2},\qquad M_U(F_m)=R_U,
\]

so for real `Y=alpha I_(m^2)+beta F_m`,

\[
 M_U(Y)=\alpha I_{d^2}+\beta R_U.
\]

The norm `||Y||_2` is the coefficient Hilbert--Schmidt norm. Since
`Tr(I_(m^2)F_m)=m`, its exact quadratic form is

\[
 \|Y\|_2^2=m^2(\alpha^2+\beta^2)+2m\alpha\beta.
\]

For `m>=2`, the Gram matrix is positive definite. Its inverse gives, for each real eigenvalue
`lambda` of `R_U`,

\[
 \sup_{(\alpha,\beta)\ne(0,0)}
 \frac{|\alpha+\beta\lambda|^2}{\|Y\|_2^2}
 =\frac{1+\lambda^2-2\lambda/m}{m^2-1}.
\]

Thus comparison with the exact target `(A/m)^2` is equivalent to

\[
 (\lambda-1/m)^2\le (A^2-1)(1-m^{-2}).
\]

Taking the maximum over the finite spectrum gives precisely

\[
 \|R_U-I_{d^2}/m\|_\infty
 \le \sqrt{(A^2-1)(1-m^{-2})}.
\]

There is no missing factor of `m`, no interchange of the coefficient and output identities, and
no replacement of the Hilbert--Schmidt norm by an operator norm.

**Verdict:** PASS.

### Finding WRS4096-IR-02 — PASS: exact equality of events

Let

\[
 E_d=\{\|R_U-I_{d^2}/m\|_\infty\le H\},\qquad
 H=\sqrt{(A^2-1)(1-m^{-2})},
\]

and let `W_d` be the target event that the `(A/m)||Y||_2` inequality holds simultaneously for
every real `Y=alpha I_(m^2)+beta F_m`. Finding WRS4096-IR-01 proves, for every fixed unitary
tuple and every `d`,

\[
 E_d\Longleftrightarrow W_d.
\]

Consequently `E_d=W_d` as subsets of the tuple sample space and
`Pr(E_d)=Pr(W_d)` for every `d`. The uncountable phrase “for every real `alpha,beta`” causes no
measurability gap because it has already been reduced exactly to the continuous spectral-norm
condition defining `E_d`.

**Verdict:** PASS. The route correctly uses an equivalence, not a one-sided transfer.

### Finding WRS4096-IR-03 — PASS: probability and parameter quantifiers

The first premise states, for every integer `m>=2` and every **fixed** `eta>=0` satisfying

\[
 [18m(1+\eta)^2+81(1+\eta)^4](1-m^{-2})>4096^2,
\]

that

\[
 \Pr\{\|R_U-I_{d^2}/m\|_\infty>H\}\to0
 \quad(d\to\infty).
\]

Because `E_d=W_d`, its complement form is exactly `Pr(W_d)->1`. The order is: choose fixed
`m` and fixed `eta`, then take `d->infinity`; neither premise supplies convergence uniform in
`m=m(d)` or `eta=eta(d)`, and the target does not claim it.

The parameter expression is `(mH)^2`, since

\[
 A^2-1=\frac{18(1+\eta)^2}{m}+\frac{81(1+\eta)^4}{m^2}.
\]

At `eta=0`, the expression is

\[
 q(m)=(18m+81)(1-m^{-2}),
\]

which is strictly increasing for `m>0`. Exact arithmetic gives

\[
 q(932063)-4096^2=
 -\frac{868758213184}{868741435969}<0,
\]

and

\[
 q(932064)-4096^2=
 \frac{1640957702711}{96527033344}>0.
\]

The expression is increasing in `(1+eta)^2`, so `m>=932064` is the exact eta-uniform integer
corollary of this sufficient condition. The target correctly says “every fixed `eta>=0`.”

**Verdict:** PASS.

### Finding WRS4096-IR-04 — PASS: route assembly and promotion scope

The route has exactly the two load-bearing unresolved-at-registration premises it needs:

1. the proved high-probability centered event under the 4096 threshold; and
2. the proved deterministic real-Werner spectral equivalence.

The first supplies the probability limit, while the second identifies the target event without
loss. No third assumption is hidden. Therefore the exact route implication at `e68b489d...`
proves the exact target claim at `73ea83e4...` once the already-`PROVED` premise levels are used.

**Verdict:** PASS.

### Finding WRS4096-IR-05 — PASS: strict non-propagation boundary

The simultaneous quantifier ranges only over the real two-dimensional space

\[
 \operatorname{span}_{\mathbb R}\{I_{m^2},F_m\}.
\]

It does not range over arbitrary Hermitian matrices, arbitrary complex coefficients outside this
real span, or all physical two-copy inputs. It is one scoped two-leg same-tuple estimate and has no
logical implication by itself for all-copy behavior, absolute-unbounded leakage, or full-size
extensive violation. The target node and artifact state all of these exclusions explicitly.

**Verdict:** PASS only for the hash-bound scoped target and route. No broader node is licensed to
change level.

## 4. Promotion recommendation

The integrator may perform the following ordered canonical update:

1. link Findings `WRS4096-IR-01--WRS4096-IR-05` to route implication hash
   `sha256:e68b489d9db13b26ced14ea980a11894835480bb7e0defe13812480f899fbd78`;
2. promote route `centered-4096-event-plus-spectral-equivalence` from `CONJECTURED` to `PROVED`;
3. link the same findings to claim hash
   `sha256:73ea83e47b97862ffccdd54b1bcee83c261b4b655dae73001b535d536a94bd28`;
4. promote only `HEXT.same-tuple-real-werner-sector-4096-threshold` from `CONJECTURED` to `PROVED`,
   remove its discharged independent-review frontier, and append separate route and node
   level-change events; and
5. regenerate derived views and run structural, evidence-closure, three-question-scope, and
   contract checks.

Do not change the level of any arbitrary-Hermitian, physical, all-copy, absolute-unbounded, or
full-size node on the basis of this review.

## 5. Limitations

This is a consequence review, not a new proof of the ten-premise centered moment theorem. It
verified that the two current `PROVED` premise interfaces, at their reviewed hashes, assemble into
the exact new claim. The number `932064` is the smallest eta-uniform integer for the present
sufficient condition, not a claim about the optimal true threshold. The review gives no estimate
outside the real Werner coefficient span and no conclusion when the strict 4096 condition fails.
