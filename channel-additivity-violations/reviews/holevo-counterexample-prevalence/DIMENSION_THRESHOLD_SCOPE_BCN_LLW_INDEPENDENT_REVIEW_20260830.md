# Independent review: the BCN 183 and LLW 182 output-dimension thresholds

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review` (Q2 source-review
assignment).

## Independence declaration and scope

I did not author `HCPREV.dimension-threshold-scope` or
`artifacts/PRIMARY_SOURCE_AUDIT_20260829.md`. I read `DAG_PROTOCOL.md` and
`FILE_PROTOCOL.md` in full. This review compares the exact canonical claim directly against the
two local primary PDFs; it does not rely on the audit's prose as a substitute for the papers.

The review checks, separately for BCN and LLW:

1. the random ensemble and input/output/environment or rank scaling;
2. the free parameter and its allowed range;
3. the correlated conjugate-channel partner and maximally entangled/Bell input;
4. the probability and limit quantifiers;
5. whether the reported integer comes from analytic proof, numerical optimization, or both; and
6. whether the paper excludes arbitrary channels or arbitrary joint inputs below that integer.

This review is confined to minimum-output von Neumann entropy (`p=1`). It does not transfer either
threshold to one-shot Holevo quantity, classical capacity, Q1, Q3, or WHGAP.

## Executive verdict

**PASS for the exact scoped claim at
`sha256:2d14346b2131fe7a261882d51d53a25bbbb81018ed98ed0ff9fddbc321e9580c`.**

The local primary sources are sufficient to establish the claim's negative boundary: neither
`182` nor `183` is a global minimum output dimension over all finite-dimensional channels.
They are detection thresholds for two different random constructions evaluated with a
product-conjugate Bell-state witness.

There is one important terminology correction. BCN's limiting entropy difference `D(k,t)` has an
explicit analytic expression, and Theorem 6.3 states the `k >= 183` result, but the paper says that
the finite-range step locating the first negative value at `k=183` uses a numerical study. Thus
`183` should not be advertised as a wholly analytic certified threshold. LLW's Proposition 5.3 is
analytic only at the sufficiently-large-`k` level; the exact displayed number `182` is explicitly a
high-precision numerical optimization of its fixed-`k` criterion.

The present canonical node remains `CONJECTURED` under the assignment. Before a later proposer
promotes it, the two imported source statements should be made machine-visible in a node-level
`assumptions` block, as required for route-free source-dependent nodes by `DAG_PROTOCOL.md`
Sections 2 and 6. This is a dossier repair, not a source insufficiency or mathematical objection to
the exact claim.

## Immutable inputs and exact statement hash

The exact bytes inspected were:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `HCPREV.dimension-threshold-scope.yaml` | `19e609a1f83b0bd2241eaab50a1af58cf0a5cb807153a0a78edd5d1e0c40ca97` |
| `PRIMARY_SOURCE_AUDIT_20260829.md` | `6435d74e4da92db4e0e97c490cf6ec937b0c937420aebb0ecb9c474d51a3b246` |
| BCN, arXiv:1305.1567v3 PDF | `5dd55c810f5bb3b244c6abd234600befd302f35ffd9d5610fa1303d22920b810` |
| LLW, arXiv:2607.15210v1 PDF | `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0` |

The exact reviewed claim is:

> The reported dimensions 182 and 183 are thresholds for particular random ensembles, parameter
> choices, Bell witnesses and numerical/analytic criteria; they are not established global minimum
> output dimensions for p=1 additivity violation among all finite-dimensional channels.

After newline normalization and trimming, its digest is
`sha256:2d14346b2131fe7a261882d51d53a25bbbb81018ed98ed0ff9fddbc321e9580c`.

## Finding HCP-DT-IR-01 -- PASS: BCN model and probability quantifiers

BCN Section 5.1, PDF p. 17, defines the random-Stinespring ensemble by a Haar isometry

```text
W : C^d -> C^k tensor C^n,
Phi(X) = (id tensor Tr)(W X W*) .
```

Here `k` is output dimension and `n` is environment dimension. Section 5.2, PDF p. 18, takes
Haar-random image subspaces of dimension `d_n` with `d_n ~ t k n`. Theorem 5.2 fixes `k` and `t`
and sends `n -> infinity`, so the channel input dimension also grows as `d_n ~ tkn`.

Section 6.2, PDF p. 19, chooses the correlated partner `bar(Phi_n)` and evaluates
`Phi_n tensor bar(Phi_n)` on the maximally entangled input of dimension `d_n`. The overbar is
visually present in the PDF even where plain-text extraction drops it. Theorem 6.3, PDF p. 20,
states:

- for every fixed output dimension `k >= 183`, there exist values of `t` such that almost all
  channels in this asymptotic ensemble violate minimum-output von Neumann entropy additivity as
  `n -> infinity`;
- for `k < 183` in the same regime, the displayed Bell-output entropy is almost surely larger than
  twice the single-channel minimum, so this particular Bell input does not exhibit violation.

The theorem does not supply a finite fixed-`n` probability formula or an environment threshold.
BCN PDF p. 22 expressly says its techniques provide no information about the size of `n`.

**Verdict:** PASS. The number `183` is inseparable from this ensemble, scaling, `t`, conjugate
partner, Bell input, and asymptotic probability statement.

## Finding HCP-DT-IR-02 -- PASS with wording correction: BCN's `183` uses numerical study

BCN defines the almost-sure limiting Bell comparison

```text
D(k,t) = H(gamma*_t) - 2 H(x*_t),
```

for which the paper says an analytic expression is available. But the proof of Theorem 6.3 then
says a numerical study of `D(k,t)` gives positivity for all `k < 183` and all `t in (0,1)`, with
the first negative value at approximately `k=183`, `t=0.11`. Its fixed-`t=1/2` analysis yields
violations iff `k >= 276`, and a further numerical study over `k=183,...,276` supplies the remaining
range.

Therefore the strongest accurate description is: **a theorem-level BCN result based on exact
asymptotic formulas plus a finite-range numerical study**. Calling the `183` localization itself a
purely analytic criterion would overstate the source.

BCN PDF p. 22 also explicitly denies the global inference: for `k < 183`, some other input to the
product channel might give a better upper bound. Thus even within the same conjugate-channel model,
failure of the Bell test is not a proof of additivity; a fortiori it is not a proof about all
finite-dimensional channels.

**Verdict:** PASS for the canonical phrase “numerical/analytic criteria,” with the above mandatory
precision whenever `183` is described separately.

## Finding HCP-DT-IR-03 -- PASS: LLW model, criterion, and probability quantifiers

LLW Section 1.1, PDF pp. 3--4, fixes `k >= 2` and `t in (k^-2,1)`, draws a Haar projection `P_n`
of rank `d_n` on `C^n tensor C^k` with `d_n/(nk) -> t`, and locally normalizes `P_n` to a
trace-preserving Choi matrix `J_n`. This is a different ensemble from BCN's Haar-Stinespring
subspace channel.

LLW Proposition 5.1, PDF p. 13, fixes `k,t,p`. If the exact strict Bell comparison

```text
S_p(lambda^Bell_{k,t}) < 2 min_{sigma in K_{k,t}} S_p(sigma)
```

holds, then almost surely the pair `Phi_n, bar(Phi_n)` violates minimum-output `p`-Renyi entropy
additivity for every sufficiently large `n`. Complex conjugation is the correlated partner and the
joint upper bound comes from the maximally entangled/Bell input analyzed in Section 4.

The quantifier is an almost-sure eventual statement for a random sequence in this locally
normalized Haar-projection model. It is not a uniform law over all channels and is not a claim that
every finite `n` succeeds.

**Verdict:** PASS.

## Finding HCP-DT-IR-04 -- PASS: LLW's analytic theorem and numerical `182` are distinct

LLW Lemma 5.2 and Proposition 5.3, PDF p. 14, prove analytically that for every `p > 3/4` there
exist `t` and `k_0` such that the strict Bell criterion holds for all `k >= k_0`. This includes
`p=1`, but it does not identify `k_0=182`.

The same page separately defines `k_high(p)` to be the smallest `k` detected by the present
ensemble and Bell-state witness. It then says explicitly that this is not a universal threshold
over all quantum channels and reports, from high-precision numerical optimization,
`k_high(1)=182`.

Thus `182` is a numerical optimization result inside LLW's exact limiting criterion, while the
analytic proposition is a sufficiently-large-dimension existence theorem. The two statements must
not be merged into “an analytic proof that 182 is minimal.”

**Verdict:** PASS.

## Finding HCP-DT-IR-05 -- PASS: comparison and global-minimum boundary

The two numbers arise from different random models and different limiting output bodies. LLW itself,
PDF pp. 5 and 14, describes the local normalization as changing the finite-`k` geometry and says its
criterion detects `182`, compared with BCN's random-Stinespring/Bell criterion at `183`.

Consequently:

- `182 < 183` is a one-step improvement in a named Bell-witness detection threshold;
- it is not a comparison of two exhaustive searches over the same ambient set;
- neither paper excludes non-Bell inputs, unrelated channel pairs, or another channel construction
  below the reported integer; and
- neither paper establishes the globally least output dimension for a `p=1` counterexample.

The canonical constraint says exactly this and no more.

**Verdict:** PASS.

## Finding HCP-DT-IR-06 -- PASS: no Holevo or explicit-witness overreach

Both reviewed threshold statements concern minimum-output von Neumann entropy. They do not preserve
the same model, same pair, same dimensions, same witness, or same probability after any universal
equivalence argument to Holevo additivity. They also do not print a deterministic finite sample
with a global optimization certificate.

**Verdict:** PASS. The review supplies no same-model Holevo threshold and no deterministic global
minimum witness.

## Finding HCP-DT-IR-07 -- protocol gate before any later promotion

The exact claim has sufficient primary-source support and passes adversarial review. The canonical
node is nevertheless a route-free source-dependent record with no `assumptions` block. Before a
later completion-level promotion, a proposer should register at least the following established
inputs, without changing the claim:

1. **BCN threshold statement.** In the Haar-Stinespring model with fixed output `k`, environment
   `n -> infinity`, input `d_n ~ tkn`, conjugate partner and Bell input, Theorem 6.3 and its proof
   give the `183` model/witness threshold using the exact limiting entropy expression and numerical
   finite-range study, and do not exclude other inputs below `183`. Source: BCN PDF pp. 17--22,
   especially Theorem 6.3 and the final scope remark.
2. **LLW threshold statement.** In the locally normalized Haar-projection model with fixed
   `k,t,p`, rank ratio `d_n/(nk) -> t`, conjugate partner and Bell input, Proposition 5.1 gives
   almost-sure eventual violation under the strict criterion; Proposition 5.3 gives only analytic
   sufficiently-large-`k` existence; the separately defined numerical optimization reports
   `k_high(1)=182` and explicitly is not universal. Source: LLW PDF pp. 3--5 and 13--14.

After those exact assumptions and this hash-bound review are linked, the node can be considered by
the proposer for `PROVED`. This reviewer does not change the canonical level.

## Limitations

This review does not establish a global lower-dimensional exclusion, a finite environment bound,
an exact rational/algebraic certificate for either numerical threshold, a deterministic printable
channel, a same-channel Holevo counterexample, or a new date-bounded literature survey beyond the
two frozen local PDFs.

