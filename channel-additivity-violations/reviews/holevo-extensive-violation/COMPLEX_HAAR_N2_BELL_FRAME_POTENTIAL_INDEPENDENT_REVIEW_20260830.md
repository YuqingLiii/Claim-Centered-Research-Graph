# Independent adversarial review of the complex-Haar two-copy Bell frame potential

**Date:** 2026-08-30
**Reviewer:** OpenAI Codex review agent
**Target node:** `HEXT.complex-haar-n2-bell-frame-potential`
**Primary proof object:** `COMPLEX_HAAR_N2_BELL_FRAME_POTENTIAL_ANALYSIS_20260830.md`
**Review status:** completed and immutable; any later correction should be a new review object

## Independence and repository discipline

I reviewed this claim in a fresh, separately commissioned context and did not participate in its
derivation. I did not receive private proposer reasoning, did not contact the proposer, and used no
subagent. I reconstructed the frame-potential calculation from the hash-bound disk inputs,
independent Haar-moment contractions, an independent enumeration of set partitions, and fresh
read-only smoke tests.

The canonical YAML, proposer artifact, referenced source analyses, and generated DAG views were
read-only. This report is the only durable file created for this review. I did not stage, commit,
push, regenerate a view, or modify canonical research state.

## Executive verdict

**CHN2-BFP-IR-VERDICT: PASS / PROVED in the stated Bell-input scope.**

For independent Haar unitaries $U_1,\ldots,U_m\in U(d)$, $d\ge2$, the two-copy Bell frame
potential has exact mean

\[
 \mathbb E F
 =m^2+\frac{m^4-m^2}{d^2}
   +\frac{2m(m-1)}{d(d+1)}.
\]

All fifteen exact equality partitions of $(v,a,w,b)$ are present. Their ordered-assignment
counts sum to $m^4$; the two exceptional moments are respectively
$2/[d(d+1)]$ and $2/d^2$; every remaining nondeterministic row has moment $1/d^2$. The stated
normalization, Markov bound, positive-measure inference, and fixed-$m$, fixed-$\eta$,
$d\to\infty$ quantifier order are correct.

The result tests only the maximally entangled input. High-dimensional Bell safety does not control
the supremum over all entangled inputs and does not prove the global $n=2$ target. Conversely,
Bell failure supplies a genuine counterexample input for the tested tuple but is only shown on a
positive-measure set in the low-dimensional direction.

No fatal or repair-requiring mathematical defect was found. Finding CHN2-BFP-IR-09 records one
minor standalone wording issue: the exact node claim does not itself state the intended
$\eta>0$ domain, although that domain is explicit in its parent target and is the domain used by
the artifact. The audited formulas are valid as claimed in that inherited domain.

## 1. Input and exact statement binding

I had already read the complete repository DAG and file protocols in this independent review
context. The exact disk bindings are:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `holevo-extensive-violation/proof-dag/nodes/HEXT.complex-haar-n2-bell-frame-potential.yaml` | `437497a13bed6cf47671e2645cce9c9cdd8c6c8f8dce62fd5901b2ad42b1d5ba` |
| `holevo-extensive-violation/artifacts/COMPLEX_HAAR_N2_BELL_FRAME_POTENTIAL_ANALYSIS_20260830.md` | `96a9aa0c7bc7bb2e1a540835eede00d5b839010ea0a422ffd65985d27d2133da` |

The exact reviewed node claim is:

> For independent Haar unitaries U_1,...,U_m in U(d), d>=2, the two-copy maximally entangled
> frame potential F has exact mean
> E[F]=m^2+(m^4-m^2)/d^2+2m(m-1)/(d(d+1)). Hence, with
> A=1+9(1+eta)^2/m, the Bell-input failure probability is at most
> min(1,delta_(m,d)/(A^2-1))=O(m^3/d^2) for fixed eta, while
> d^2<(m^2-1)/(A^2-1) implies a positive-Haar-measure set of Bell-failing tuples.

Using the repository normalization `sha256(statement.strip())` after CRLF normalization, its
exact claim hash is:

**sha256:7305265855ecacd760896568ce87cb064d824ed5bca7598edf9e70954148579e**

This review becomes stale if the claim or either primary disk input changes.

## 2. Independent check ledger

The following fresh checks were performed without modifying repository inputs:

1. A separately written standard-library enumeration generated all set partitions of the four
   ordered positions $v,a,w,b$. It found exactly 15 partitions, with block-count distribution
   $1,7,6,1$ for one through four blocks.
2. Assigning $(m)_r$ ordered distinct labels to every $r$-block partition gave

   \[
   (m)_1+7(m)_2+6(m)_3+(m)_4=m^4.
   \]

   The identity and the consolidated background count were checked mechanically for
   $m=1,\ldots,8$, in addition to the symbolic derivation below.
3. The $p=2$ Weingarten contraction was independently evaluated with exact rational arithmetic
   for $d=2,\ldots,10$, producing
   $\mathbb E|\operatorname{Tr}(RR^T)|^2=2d/(d+1)$ and
   $\mathbb E|\operatorname{Tr}(\overline R R)|^2=2$ in every case.
4. As a diagnostic separate from the proof, standard-library complex-Gaussian Gram--Schmidt Haar
   sampling reproduced the full mean at
   $(m,d)=(2,2),(2,3),(3,2),(3,3)$. The four deviations from the exact formula were respectively
   $-0.93,-0.50,0.70,-1.68$ estimated standard errors.

The universal verdict rests on the exact arguments below, not on the finite smoke tests.

## 3. Findings

### Finding CHN2-BFP-IR-01 — PASS: Bell frame and purity normalization

**Stable source locators:** artifact equations (1)–(3), lines 13–38; node claim lines 6–8.

For normalized

\[
 |\Omega_d\rangle=d^{-1/2}\sum_i|i,i\rangle,
\]

the vectorization identity gives

\[
 (U_v\otimes U_a)|\Omega_d\rangle
 =d^{-1/2}\operatorname{vec}(U_vU_a^T)=|\phi_{v,a}\rangle.
\]

Thus

\[
 \langle\phi_{v,a}|\phi_{w,b}\rangle
 =\frac1d\operatorname{Tr}[(U_vU_a^T)^*(U_wU_b^T)].
\]

The output of $L\otimes L$ is the equal mixture of the $m^2$ projectors
$|\phi_{v,a}\rangle\langle\phi_{v,a}|$, each with weight $m^{-2}$. Squaring this mixture gives
$P_{\rm Bell}=F/m^4$, with no omitted factor of $d$ or $m$.

For the pure Bell input, a Stinespring dilation of $L\otimes L$ is globally pure across physical
and complementary outputs. Therefore the two reduced outputs have the same nonzero spectrum and
the same purity. This justifies using the same $F/m^4$ for $C\otimes C$.

**Verdict:** normalization and complementary-spectrum transfer are exact.

### Finding CHN2-BFP-IR-02 — PASS: the fifteen partitions are exhaustive

**Stable source locators:** artifact Section 3, table lines 143–165.

The exact equality patterns of four ordered labels are precisely the set partitions of four
positions. Independent enumeration gives:

| number of blocks | exact patterns | count |
|---:|---|---:|
| 1 | `vawb` | 1 |
| 2 | `vaw|b`, `vab|w`, `va|wb`, `vwb|a`, `vw|ab`, `vb|aw`, `v|awb` | 7 |
| 3 | `va|w|b`, `vw|a|b`, `v|aw|b`, `vb|a|w`, `v|ab|w`, `v|a|wb` | 6 |
| 4 | `v|a|w|b` | 1 |

Every one appears once in the artifact table. A partition with $r$ blocks has exactly $(m)_r$
ordered assignments of distinct labels, including the correct zero value when $r>m$. Hence the
table covers

\[
 (m)_1+7(m)_2+6(m)_3+(m)_4=m^4
\]

ordered quadruples, with neither omissions nor overlaps.

**Verdict:** the classification and total count are complete for every positive integer $m$.

### Finding CHN2-BFP-IR-03 — PASS: every background row has moment \(1/d^2\)

**Stable source locators:** artifact equation (11), lines 102–120; Section 3, lines 166–182.

The unnormalized overlap can be written as

\[
 dX=\operatorname{Tr}(\overline U_a U_v^*U_wU_b^T).
\]

Every nondeterministic partition other than `va|wb` and `vb|aw` has at least one singleton label.
Condition on all other unitary labels. The unique occurrence of the singleton is one of
$U,U^*,\overline U,U^T$, each Haar distributed. Cyclically positioning that factor in the trace
and multiplying it on either side by the remaining fixed unitary product leaves a Haar unitary
$R$. Thus conditionally $dX$ has the distribution of $\operatorname{Tr}R$, and

\[
 \mathbb E|dX|^2=\mathbb E|\operatorname{Tr}R|^2=1.
\]

Consequently every such row has $\mathbb E|X|^2=1/d^2$. This argument remains valid for all
four `3+1` patterns, so it does not accidentally treat two frame vectors as independent when a
unitary label is repeated three times.

**Verdict:** all background moments are correct; no higher-order contraction is needed.

### Finding CHN2-BFP-IR-04 — PASS: the `va|wb` exceptional moment

**Stable source locators:** artifact Section 4.1, equations (14)–(15), lines 205–226.

For $v=a\ne w=b$, put $R=U_v^*U_w$, which is Haar by invariance. Cyclicity of trace gives

\[
 dX_{v,v;w,w}=\operatorname{Tr}(RR^T).
\]

For a Haar $R$, the $p=2$ unitary Weingarten values are

\[
 \operatorname{Wg}(e)=\frac1{d^2-1},\qquad
 \operatorname{Wg}((12))=-\frac1{d(d^2-1)}.
\]

Expanding $\operatorname{Tr}(RR^T)=\sum_{i,j}R_{ij}R_{ij}$ leaves

\[
 \mathbb E|\operatorname{Tr}(RR^T)|^2
 =2d^2\bigl(\operatorname{Wg}(e)+\operatorname{Wg}((12))\bigr)
 =\frac{2d}{d+1}.
\]

Dividing by $d^2$ yields $2/[d(d+1)]$, valid for every $d\ge2$.

**Verdict:** the complex-symmetric exceptional moment is exact.

### Finding CHN2-BFP-IR-05 — PASS: the `vb|aw` exceptional moment

**Stable source locators:** artifact Section 4.2, equations (16)–(17), lines 228–247.

For $v=b\ne a=w$, again set $R=U_v^*U_a$. Then

\[
 dX_{v,a;a,v}=\operatorname{Tr}(\overline R R)
 =\sum_{i,j}\overline{R_{ij}}R_{ji}.
\]

The four $p=2$ contractions have total

\[
 2d^2\operatorname{Wg}(e)+2d\operatorname{Wg}((12))=2.
\]

Therefore $\mathbb E|X|^2=2/d^2$. This is a factor-two enhancement of the background moment,
not a dimension-independent collision.

**Verdict:** the transpose-exchange exceptional moment is exact.

### Finding CHN2-BFP-IR-06 — PASS: class counts and exact mean

**Stable source locators:** artifact Section 3, lines 166–199; equations (4)–(6), lines 41–65.

The deterministic condition $v=w,a=b$ contains `vawb` and `vw|ab`, hence

\[
 m+m(m-1)=m^2
\]

unit terms. Each exceptional family has $m(m-1)$ members. The remaining background count is

\[
 m^4-m^2-2m(m-1)=m^4-3m^2+2m.
\]

Thus

\[
\begin{aligned}
 \mathbb EF
 &=m^2+\frac{2m(m-1)}{d(d+1)}
   +\frac{2m(m-1)}{d^2}
   +\frac{m^4-3m^2+2m}{d^2}\\
 &=m^2+\frac{m^4-m^2}{d^2}
   +\frac{2m(m-1)}{d(d+1)}.
\end{aligned}
\]

After division by $m^4$, defining

\[
 \delta_{m,d}=\frac{m^2-1}{d^2}
 +\frac{2(m-1)}{m d(d+1)}
\]

indeed gives $\mathbb EP_{\rm Bell}=(1+\delta_{m,d})/m^2$.

**Verdict:** total counting, algebraic simplification, and normalization all agree.

### Finding CHN2-BFP-IR-07 — PASS: Markov bound and \(O(m^3/d^2)\) estimate

**Stable source locators:** artifact equation (8), lines 68–94; equations (18)–(19), lines
249–275; node claim lines 8–10.

There are $m^2$ diagonal Gram terms equal to one and all other terms are nonnegative, so
$Y=F-m^2\ge0$. Moreover

\[
 \mathbb EY=m^2\delta_{m,d}.
\]

With $c=(1+\eta)^2$ and $A=1+9c/m>1$ in the intended $\eta>0$ domain, Bell failure is
$Y>(A^2-1)m^2$. Markov's inequality therefore gives

\[
 \Pr\{F>A^2m^2\}
 \le \min\left\{1,\frac{\delta_{m,d}}{A^2-1}\right\}.
\]

The second displayed estimate follows from

\[
 \delta_{m,d}\le\frac{m^2+1}{d^2},\qquad
 A^2-1=\frac{18c}{m}+\frac{81c^2}{m^2}\ge\frac{18c}{m}.
\]

Hence

\[
 \Pr\{F>A^2m^2\}
 \le\min\left\{1,\frac{m(m^2+1)}{18c\,d^2}\right\}
 =O_\eta(m^3/d^2).
\]

No variance or concentration premise is being smuggled into this one-sided result.

**Verdict:** the probability inequality and asymptotic upper bound are correct.

### Finding CHN2-BFP-IR-08 — PASS: low-dimensional positive measure and fixed-\(m\) quantifiers

**Stable source locators:** artifact equations (21)–(23), lines 284–315; Section 6, lines
317–333; node claim lines 10–11 and caveats lines 25–30.

If

\[
 d^2<\frac{m^2-1}{A^2-1},
\]

then the first summand of $\delta_{m,d}$ already exceeds $A^2-1$. Consequently

\[
 \mathbb EF=m^2(1+\delta_{m,d})>A^2m^2.
\]

If the event $F>A^2m^2$ had Haar measure zero, the reverse inequality would hold almost surely
and hence also in expectation, a contradiction. Thus the failure set has positive Haar measure.
When $A<m$, the bound $F\le m^4$ further gives exactly

\[
 \Pr\{F>A^2m^2\}
 \ge\frac{\delta_{m,d}-(A^2-1)}{m^2-A^2}>0.
\]

This is an existence statement, not a high-probability lower bound.

For the opposite direction, the limit is taken only after fixing both $m$ and $\eta$. Then the
Markov upper bound tends to zero as $d\to\infty$. If the separately established one-copy event
also has probability tending to one in that same fixed-$m$ limit, a union bound gives positive
probability of their intersection; independence of the events is neither used nor claimed. The
argument supplies no conclusion when $m=m(d)$ grows without an additional rate condition.

**Verdict:** the mean-threshold inference and quantifier order are correct.

### Finding CHN2-BFP-IR-09 — PASS IN BELL SCOPE; minor standalone wording issue

**Stable source locators:** artifact status lines 5–7, lines 97–98, and Section 6 lines 324–333;
node caveats lines 25–30; parent target
`HEXT.product-haar-physical-self-purity-multiplicativity` claim lines 5–10.

The passing event controls only the single input $\Omega_d$. It does not upper-bound

\[
 \sup_\rho\operatorname{Tr}[(C\otimes C)(\rho)^2]
\]

over entangled inputs, prove the global $n=2$ physical Gram inequality, or say anything about
$n\ge3$ and the all-copy target. The artifact and node caveats state all of these restrictions
correctly. A Bell failure, on the other hand, is sufficient to refute the corresponding universal
two-copy bound for that tuple because it exhibits an explicit failing physical input.

One low-severity self-containment issue remains. The exact node claim introduces $\eta$ but does
not quantify it. Its parent target explicitly assumes $\eta>0$, and Section 1 imports $A$ from
that target, so the intended domain is unambiguous in repository context. Taken as an isolated
sentence, however, the node's ratio is undefined at $\eta=-1$, where $A=1$. A future canonical
wording patch should say “for $\eta>0$” (or otherwise explicitly require $A>1$). No canonical
file was changed in this review.

**Severity:** wording/self-containment only; no mathematical repair is needed in the inherited
$\eta>0$ scope.

## 4. Limitations of this review

1. The unitary Weingarten formula is an external theorem assumed by the node. I independently
   checked every contraction actually needed after the singleton-label reduction, but did not
   re-prove Haar integration theory from first principles.
2. This review proves the exact first moment and its Markov consequence. It does not compute the
   variance, a concentration rate, or the actual low-dimensional failure probability.
3. The audit is confined to the Bell input for one-layer complex product-Haar tuples. It does not
   optimize over all physical inputs, control higher tensor powers, or prove regularized entropy
   consequences.
4. The result is ensemble-level. Passing with high Haar probability does not certify any named
   finite tuple until one is selected and separately verified as required by downstream claims.

## 5. Final disposition

The exact node claim bound to
**sha256:7305265855ecacd760896568ce87cb064d824ed5bca7598edf9e70954148579e**
passes independent adversarial mathematical review in its repository-inherited $\eta>0$,
Bell-input scope. Findings CHN2-BFP-IR-01 through CHN2-BFP-IR-08 certify the normalization,
complete partition enumeration, exceptional moments, counting, exact expectation, Markov bound,
positive-measure inference, and fixed-$m$ limit. Finding CHN2-BFP-IR-09 preserves the Bell-only
boundary and records the sole minor wording issue. No canonical YAML or proposer artifact was
modified.
