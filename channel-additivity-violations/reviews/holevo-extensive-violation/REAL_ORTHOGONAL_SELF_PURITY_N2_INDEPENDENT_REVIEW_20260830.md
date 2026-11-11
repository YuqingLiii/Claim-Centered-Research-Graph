# Independent adversarial review of the real/orthogonal two-copy self-purity obstruction

**Date:** 2026-08-30  
**Reviewer:** OpenAI Codex review agent  
**Target node:** HEXT.real-orthogonal-self-purity-n2-obstruction  
**Primary proof object:** PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md, Section 6  
**Review status:** completed and immutable; any later correction should be a new review object

## Independence and repository discipline

I reviewed this claim in a fresh context and did not participate in its original derivation. I did
not receive private proposer reasoning, did not contact the proposer, and used no subagent. I
reconstructed the proof from the hash-bound disk inputs, elementary Stinespring and matrix
arguments, and independent exact calculations.

The canonical YAML, source analysis, and generated DAG views were read-only. This report is the
only durable file created by the review. I did not stage, commit, push, regenerate a view, or modify
canonical research state.

## Executive verdict

**ROSP-N2-IR-VERDICT: PASS / PROVED by independent adversarial review.**

Let

\[
 L(X)=\frac1q\sum_{v=1}^q W_vXW_v^*
\]

have equally weighted unitary words which, after fixed common input/output unitary orientations
and word-dependent scalar phases, are real orthogonal. There is a maximally entangled input to two
uses for which

\[
 \operatorname{Tr}\!\left[C^{\otimes2}(\Omega)^2\right]
 \ge \frac{2}{q^2}-\frac1{q^3}.
\]

The equal-label Bell collision, the remainder rank bound, the purity estimate, and the transfer to
the complementary output are all correct. Consequently

\[
 \mu_2(C\otimes C)\le(A/q)^2
\]

fails whenever \(A^2<2-1/q\). For \(J=1,\eta=0\), where \(q=m\) and
\(A=1+9/q\), this condition holds exactly for every integer \(q\ge23\).

The conclusion is conditional on simultaneous real/orthogonal realizability. It does not apply to
an arbitrary complex tuple and supplies no counterexample to the generic complex product-Haar
existential node. No fatal, repair-requiring, or conclusion-scope defect was found. Finding
ROSP-N2-IR-05 records the precise interpretation of “common orientation” needed by the claim.

## 1. Input and exact statement binding

I had already read the complete repository DAG and file protocols in this independent review
context. The exact disk bindings for this review are:

| object | SHA-256 |
|---|---|
| DAG_PROTOCOL.md | d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095 |
| FILE_PROTOCOL.md | d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595 |
| holevo-extensive-violation/proof-dag/nodes/HEXT.real-orthogonal-self-purity-n2-obstruction.yaml | 9ac57bac13023742c73f98c4a94351d3c416165fc5740e8966a5dac685e1edf5 |
| holevo-extensive-violation/artifacts/PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md | c1395863067b9713eb0b327b70014be4d5121e8ed2cf6a965c7183e983cafd6b |
| Section 6 text alone, from its heading through the line preceding Section 7 | 3bd36764787d31678d06d28cf5789564127a8597535e37b73aa3122b395b4ede |

The exact reviewed node claim is:

> Let L be a finite random-unitary channel with q equally weighted unitary words that are
> simultaneously real orthogonal up to a common orientation and phases, and let C be its
> complement. A maximally entangled input to two repeated uses satisfies
> Tr[C^(tensor 2)(Omega)^2]>=2/q^2-1/q^3. Consequently the proposed bound
> mu_2(C tensor C)<=(A/q)^2 fails whenever A^2<2-1/q; for J=1, eta=0 and A=1+9/q this includes
> every integer q>=23.

Its repository-normalized exact claim hash is:

**sha256:9272414f78a59e474e65b9fe1257dc7d7c9e2b051300631be8cf97f20c9beb62**

This review becomes stale if that claim or either primary disk input changes.

## 2. Findings

### Finding ROSP-N2-IR-01 — PASS: equal Kraus labels collide on a Bell input

**Stable source locators:** Section 6, equations (36)–(37), artifact lines 419–436; node claim
lines 5–9.

First suppose every \(W_v=O_v\) is real orthogonal. For the normalized maximally entangled vector
\(|\Omega\rangle=d^{-1/2}\sum_i|i,i\rangle\),

\[
 (O_v\otimes O_v)|\Omega\rangle
 =d^{-1/2}\operatorname{vec}(O_vO_v^T)
 =|\Omega\rangle.
\]

The channel \(L\otimes L\) has \(q^2\) equally weighted Kraus pairs
\((W_v,W_a)\), each of weight \(1/q^2\). The \(q\) diagonal pairs \(v=a\) therefore contribute the
same pure projector with total coefficient \(q/q^2=1/q\). No distinctness or linear independence
of the unitary words is required.

**Verdict:** the collision coefficient \(1/q\) and its quantifiers are exact.

### Finding ROSP-N2-IR-02 — PASS: the positive remainder has the stated trace and rank

**Stable source locators:** Section 6, equations (37)–(38), artifact lines 429–443.

After extracting the \(q\) diagonal Kraus pairs,

\[
 (L\otimes L)(\Omega)=\frac1qP+R,
 \qquad P=|\Omega\rangle\langle\Omega|,
\]

where \(R\) is a sum of the remaining \(q^2-q\) positive rank-one output projectors, each with
weight \(1/q^2\). Hence

\[
 R\succeq0,\qquad
 \operatorname{Tr}R=\frac{q^2-q}{q^2}=1-\frac1q,
 \qquad
 \operatorname{rank}R\le q^2-q.
\]

The bound remains true if some off-diagonal Kraus pairs also produce the same ray or if other
linear dependencies occur; those events only reduce the rank. For the threshold application
\(q\ge23\), \(R\) has positive trace, so the rank denominator is nonzero.

**Verdict:** the rank estimate is complete and does not assume genericity.

### Finding ROSP-N2-IR-03 — PASS: the purity lower bound is exact

**Stable source locators:** Section 6, equation (39), artifact lines 445–454.

Expanding the square gives

\[
 \operatorname{Tr}\left[\left(\frac1qP+R\right)^2\right]
 =\frac1{q^2}+\frac2q\operatorname{Tr}(PR)+\operatorname{Tr}(R^2).
\]

Because \(P,R\succeq0\), the cross term is nonnegative. If \(r=\operatorname{rank}R\), the
Cauchy–Schwarz inequality on the nonzero eigenvalues of \(R\) gives

\[
 \operatorname{Tr}(R^2)\ge\frac{(\operatorname{Tr}R)^2}{r}
 \ge\frac{(1-1/q)^2}{q^2-q}
 =\frac1{q^2}-\frac1{q^3}.
\]

Therefore

\[
 \operatorname{Tr}[(L\otimes L)(\Omega)^2]
 \ge\frac2{q^2}-\frac1{q^3}.
\]

Dropping the cross term is safe even when \(P\) lies partly in the support of \(R\). The direction
of the rank substitution is also correct: a smaller actual rank makes the lower bound stronger.

**Verdict:** no missing cross term or reversed rank inequality.

### Finding ROSP-N2-IR-04 — PASS: complementary outputs have the same nonzero spectrum

**Stable source locators:** Section 6, artifact lines 456–457; Section 1, equations (12a)–(12b),
artifact lines 135–155.

Use the Stinespring isometry

\[
 V=\frac1{\sqrt q}\sum_v |v\rangle_E\otimes W_v
\]

for \(L\). Then \(V\otimes V\) is a Stinespring isometry for \(L\otimes L\), and tracing the two
system outputs gives \(C\otimes C\), up to an irrelevant ordering of the two environment factors.
For a pure two-copy input, \((V\otimes V)|\Omega\rangle\) is a pure bipartite state across system
output versus environment output. Its two reduced density matrices have identical nonzero
eigenvalues. In particular their purities agree:

\[
 \operatorname{Tr}[(C\otimes C)(\Omega)^2]
 =\operatorname{Tr}[(L\otimes L)(\Omega)^2].
\]

This remains true for a nonminimal Kraus-label complement; an isometric enlargement only appends
zero eigenvalues.

**Verdict:** the lower bound transfers exactly to the complement used in the node.

### Finding ROSP-N2-IR-05 — PASS WITH EXPLICIT INTERPRETATION: common orientation and phases

**Stable source locators:** node claim lines 6–8; Section 6, artifact lines 473–475.

The common-orientation extension is valid under the natural precise meaning

\[
 W_v=e^{i\theta_v}UO_vV
\]

for fixed unitaries \(U,V\), word-dependent phases, and real orthogonal \(O_v\). Use the rotated
maximally entangled input

\[
 |\Omega_V\rangle=(V^*\otimes V^*)|\Omega\rangle.
\]

For every equal label,

\[
 (W_v\otimes W_v)|\Omega_V\rangle
 =e^{2i\theta_v}(U\otimes U)(O_v\otimes O_v)|\Omega\rangle
 =e^{2i\theta_v}(U\otimes U)|\Omega\rangle.
\]

All these vectors define the same pure ray. The phases disappear from their projectors, and the
fixed left orientation only rotates the common output ray. The rest of Findings ROSP-N2-IR-02
through ROSP-N2-IR-04 is unchanged.

This argument does not cover word-dependent left or right orientations. The node says “common
orientation,” so no broader quantifier is required. The symbol \(\Omega\) in the claim should be
read as the suitable maximally entangled input, not necessarily the standard Bell vector in the
unoriented basis.

**Verdict:** the orientation extension is correct and does not weaken the claimed lower bound.

### Finding ROSP-N2-IR-06 — PASS: threshold comparison and \(q\ge23\) arithmetic

**Stable source locators:** Section 6, equations (40)–(41), artifact lines 459–473; node claim
lines 9–11.

The exhibited input shows

\[
 \mu_2(C\otimes C)\ge\frac{2}{q^2}-\frac1{q^3}.
\]

It strictly violates the proposed upper bound \((A/q)^2\) whenever

\[
 \frac{2}{q^2}-\frac1{q^3}>\frac{A^2}{q^2}
 \quad\Longleftrightarrow\quad
 A^2<2-\frac1q.
\]

For \(J=1,\eta=0\), the definitions give \(q=m\) and \(A=1+9/m=1+9/q\). Substitution yields

\[
 \left(1+\frac9q\right)^2<2-\frac1q
 \quad\Longleftrightarrow\quad
 q^2-19q-81>0.
\]

The positive real root is

\[
 \frac{19+\sqrt{685}}2,
\]

which lies strictly between 22 and 23. Equivalently the polynomial equals \(-15\) at 22 and \(11\)
at 23, and it is increasing for every \(q\ge23\). Thus the integer threshold is exactly
\(q\ge23\), not merely a loose sufficient threshold.

**Verdict:** all strict inequalities, substitutions, and integer arithmetic are correct.

### Finding ROSP-N2-IR-07 — PASS: the obstruction does not extend to generic complex Haar tuples

**Stable source locators:** Section 6, artifact lines 477–480; Section 7, equations (42)–(43) and
artifact lines 482–506; node caveats lines 14–19; parent open node caveat lines 21–24.

For a general complex word,

\[
 (W_v\otimes W_v)|\Omega\rangle
 =d^{-1/2}\operatorname{vec}(W_vW_v^T),
\]

which depends on \(v\) unless the tuple has the simultaneous real/orthogonal structure of Finding
ROSP-N2-IR-05. Unitarity alone gives \(W_v\otimes\overline{W_v}\) invariance, not
\(W_v\otimes W_v\) invariance. The two repeated channel uses in this node use the latter.

Therefore the deterministic weight-\(1/q\) collision is absent from the proof for a generic
complex tuple. In the relevant nontrivial dimensions, simultaneous realifiability by fixed common
orientations is a lower-dimensional constraint and an independently Haar-sampled complex tuple is
almost surely outside it. More importantly, Section 6 proves only the conditional implication
“simultaneously real/orthogonal implies failure”; it proves neither universal failure nor
positive-probability failure for the complex product-Haar ensemble.

The parent node HEXT.product-haar-physical-self-purity-multiplicativity correctly treats this
obstruction as non-load-bearing boundary evidence and remains open for generic complex-Haar
entangled inputs and for all copy numbers.

**Verdict:** the node and artifact use the correct restricted quantifier. No inference to generic
complex Haar is licensed by this review.

## 3. Independent exact checks

I performed a separate exact signed-permutation test, not present in the proposer artifact. For
several real orthogonal tuples in dimension three, I formed every two-copy pure Kraus output,
computed the frame-potential purity with rational arithmetic, and independently row-reduced the
off-diagonal-output span. The results were:

| \(q\) | exact output purity | theorem lower bound | off-diagonal span rank bound |
|---:|---:|---:|---:|
| 2 | \(3/8\) | \(3/8\) | \(2\le2\) |
| 3 | \(1/3\) | \(5/27\) | \(2\le6\) |
| 4 | \(211/1152\) | \(7/64\) | \(7\le12\) |
| 5 | \(11/75\) | \(9/125\) | \(8\le20\) |
| 6 | \(11/81\) | \(11/216\) | \(9\le30\) |

These finite examples are diagnostics only; the universal verdict comes from Findings
ROSP-N2-IR-01 through ROSP-N2-IR-06. The independent arithmetic check also reproduced
\(22^2-19\cdot22-81=-15\) and \(23^2-19\cdot23-81=11\).

## 4. Node adjudication and scope

| object | verdict | boundary |
|---|---|---|
| HEXT.real-orthogonal-self-purity-n2-obstruction claim | PASS / PROVED | exact reviewed hash above; applies only to simultaneous real/orthogonal tuples |
| Direct Section 6 argument | PASS / PROVED | Findings ROSP-N2-IR-01 through ROSP-N2-IR-07 |
| HEXT.product-haar-physical-self-purity-multiplicativity | not adjudicated as proved | remains OPEN; the reviewed node is non-load-bearing boundary evidence only |

This report licenses completion-level review support for the exact target claim at
**sha256:9272414f78a59e474e65b9fe1257dc7d7c9e2b051300631be8cf97f20c9beb62**,
with Finding ROSP-N2-IR-VERDICT or the more specific findings above as stable locators. It does not
modify the node. Any canonical application must link the applicable finding and exact claim hash,
append the proper review event, refresh generated views, and run the repository validators.

## 5. Severity and limitations

| category | result |
|---|---|
| fatal issue | none |
| mathematical repair required | none |
| wording/scope repair required | none; Finding ROSP-N2-IR-05 fixes the precise reading of “common orientation” |
| passed load-bearing findings | ROSP-N2-IR-01 through ROSP-N2-IR-07 |

Limitations:

1. This is an exact algebraic/model review with rational diagnostics, not a proof-assistant
   formalization.
2. The conclusion concerns \(n=2\) only. It does not classify \(n\ge3\).
3. The result excludes the simultaneously real/orthogonal replacement ensemble. It neither proves
   nor refutes the repeated-use purity bound for a generic complex product-Haar realization.
4. The “almost surely outside” statement is understood in the relevant nontrivial complex Haar
   setting. It is not used as a premise for the obstruction itself.

