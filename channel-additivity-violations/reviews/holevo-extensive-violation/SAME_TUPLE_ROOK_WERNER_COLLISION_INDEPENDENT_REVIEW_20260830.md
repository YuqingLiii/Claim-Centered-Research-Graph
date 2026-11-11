# Independent adversarial review of the positive rook class and Werner reversal-collision count

**Date:** 2026-08-30  
**Reviewer:** OpenAI Codex review agent  
**Reviewed nodes:** `HEXT.same-tuple-positive-rook-support-base-case`,
`HEXT.same-tuple-rook-truncation-positivity-obstruction`, and
`HEXT.werner-reversal-cyclic-collision-count`  
**Re-audited boundary node:** `HEXT.same-tuple-werner-centered-bound`  
**Review status:** completed and immutable; any later correction requires a new review object

## Independence and repository discipline

I performed this audit in a separately commissioned review context. I did not participate in the
proposer derivations or node registration, did not receive private proposer reasoning, did not
contact the proposer, and used no subagent. I independently reconstructed the rook
inclusion--exclusion output, its commuting spectrum, the shared Hilbert--Schmidt budget, the
truncation counterexample, both circular cancellation matchings, the equality graph, the
fixed-point argument, and the final collision count.

The canonical YAML, proposer artifacts, protocols, prior evidence, and earlier reviews were
read-only. This report is the only durable repository file created by the audit. I did not promote
a node, edit a canonical claim, regenerate a view, stage, commit, or push.

## Executive verdict

All three new claims merit `PROVED` at the exact hashes recorded in Section 1:

- the positive rook-support target is an exact conditional theorem on the already uniform one-leg
  event, with no trace restriction;
- the inclusion--exclusion rook truncation is explicitly nonpositive, so the stated positive
  decomposition route is invalid;
- the forward/reversal cyclic-collision set has the claimed universal exponential bound.

The updated frontier of `HEXT.same-tuple-werner-centered-bound` is correct, but that node remains
unresolved at `CONJECTURED`. The collision count closes only the fixed-word planar/annular label
entropy. A trace proof at `N=Theta(log d)` still needs a uniform finite-`d` positive-genus
Weingarten bound with exponential rather than factorial growth.

No mathematical or wording defect was found in the three reviewed claims.

## 1. Immutable inputs and exact claim hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `nodes/HEXT.same-tuple-positive-rook-support-base-case.yaml` | `d56d13b20e8344f59be5d42dcc5b383ca308997b989deb02e15651f5065e439a` |
| `nodes/HEXT.same-tuple-rook-truncation-positivity-obstruction.yaml` | `6be3991b3b0cf9ae64b5b5eff5e977af1538841e126147c8e24c504a7e0d4b46` |
| `nodes/HEXT.werner-reversal-cyclic-collision-count.yaml` | `13476c2384c45658ca2fb5c13e86552ae3898bcebd6637d9f10cffd660685114` |
| updated `nodes/HEXT.same-tuple-werner-centered-bound.yaml` | `1880dbc46aafdbf091d9780fa8c4b005aa073bb1eb77c8dd1b920224d1f103d1` |
| `artifacts/SAME_TUPLE_POSITIVE_ROOK_SUPPORT_20260830.md` | `db6b6e684180f383515a6c511fa2dd6c41395e1dbc57ac699d14e4f43bc25139` |
| `artifacts/WERNER_REVERSAL_COLLISION_ENCODING_20260830.md` | `25bf03d15ce51f6e4e8959f60de37207b59e633bf69a5167d7a07c73cf5cd96f` |
| inherited positive-extension artifact | `57dbc9903072ea99cb6aef499845b19c6ec41c7044e68480614533627a1a3c35` |
| inherited growing-trace artifact | `6f0d52b4d48433c9f16d8ded4440469268b336df3af8f23f4a8b798ac15752ce` |
| preceding independent review | `d0bc4279e0507979f2d3b994bc620f1ec918c1ff6149e40b7515c209d9f5887e` |

The repository-normalized exact claim hashes are:

| node | exact claim hash | recommendation |
|---|---|---|
| `HEXT.same-tuple-positive-rook-support-base-case` | `sha256:cbe076658098ba4cf5732a06f9ae9a0bfeefbc0f433152fb9703fbd86c7e419a` | `PROVED` |
| `HEXT.same-tuple-rook-truncation-positivity-obstruction` | `sha256:496b1e3e4946b9f4244eff9cf371ea22aeaac1ba076e22f279f43c1bee96ed86` | `PROVED` |
| `HEXT.werner-reversal-cyclic-collision-count` | `sha256:913a8467944b1e977aeca2c5f8bc7bb4b1ea3f7f71f7154f50f65035f7907ac3` | `PROVED` |
| `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | unresolved; no promotion |

The hashes are `sha256(claim.strip())` after YAML folding and CRLF normalization. A finding is
stale for promotion if its reviewed claim changes.

## 2. Independent smoke tests

As non-evidentiary checks, I used only the Python standard library.

For `(m,d)=(3,3)` and the identity/shift/Fourier unitary tuple, the direct rook-supported output
agreed with the inclusion--exclusion formula to `1.11e-16`. The three disjoint coefficient sectors
had squared norms summing to `1.000000000000000`; the explicit positive-definite full-rank example
had Hilbert--Schmidt norm one and trace `2.999800019997778>A` for any intended target constant near
one. The uniform-product truncation counterexample had Rayleigh quotient `-1/9` on a chosen unit
vector in `e^perp tensor e^perp`, exactly matching `-1/m^2`.

I also independently enumerated cyclically reduced forward/reversal collisions. For example:

| `(m,N)` | collision sequences | all edge sequences |
|---|---:|---:|
| `(2,4)` | `16` | `16` |
| `(3,2)` | `36` | `36` |
| `(3,3)` | `168` | `216` |
| `(3,4)` | `984` | `1296` |

All were far below the proved universal bound. The exact proof verdicts below do not rely on these
finite tests.

## 3. Findings

### Finding STRC-IR-01 — PASS: exact rook inclusion--exclusion output and commuting spectrum

**Stable source locators:** rook artifact Sections 2--3, equations (5)--(14); rook-support node
claim.  
**Reviewed claim hash:**
`sha256:cbe076658098ba4cf5732a06f9ae9a0bfeefbc0f433152fb9703fbd86c7e419a`.

Let `Delta_1` pinch onto `v=w` and `Delta_2` pinch onto `a=b`. For a coefficient supported on the
union of those two entry sets,

\[
 Y=P+Q-D,
 \quad P=\Delta_1Y,\quad Q=\Delta_2Y,\quad D=\Delta_1\Delta_2Y.
\]

The `Q-D` sector has zero first coefficient partial trace, while `P-D` has zero second partial
trace. Hence, with `R=Tr_1Y`, `L=Tr_2Y`, and `tau=TrY`,

\[
 \mathcal M_U(P)=m^{-1}I\otimes C^*(R),
 \quad
 \mathcal M_U(Q)=m^{-1}C^*(L)\otimes I,
 \quad
 \mathcal M_U(D)=\tau m^{-2}I.
\]

Inclusion--exclusion therefore gives exactly

\[
 \mathcal M_U(Y)
 =m^{-1}I\otimes C^*(R)
  +m^{-1}C^*(L)\otimes I
  -\tau m^{-2}I.
\]

For positive `Y`, both partial traces and their `C^*` images are positive. The two nonscalar terms
act on different physical tensor legs and commute. Since `M_U(Y)>=0`, its operator norm is its
largest eigenvalue, namely

\[
 \|\mathcal M_U(Y)\|_\infty
 =\frac{\lambda_{\max}(C^*(R))+\lambda_{\max}(C^*(L))}{m}
  -\frac\tau{m^2}.
\]

**Verdict:** the output identity, partial-trace convention, subtraction sign, and commuting
spectrum are exact.

### Finding STRC-IR-02 — PASS: shared sector budget and the `sqrt(2A-1)` constant

**Stable source locators:** rook artifact Sections 4--5, equations (15)--(25); rook-support node
claim.  
**Reviewed claim hash:**
`sha256:cbe076658098ba4cf5732a06f9ae9a0bfeefbc0f433152fb9703fbd86c7e419a`.

The three matrices `D`, `P-D`, and `Q-D` have disjoint entry supports. With

\[
 d_0=\|D\|_F^2,\qquad x=\|P-D\|_F,\qquad y=\|Q-D\|_F,
\]

Hilbert--Schmidt normalization gives the single budget

\[
 d_0+x^2+y^2=1.
\]

All trace lies on the `m^2` nonnegative diagonal entries of `D`, so
`tau/m<=sqrt(d_0)`. Summing the `m` row- or column-coherence blocks gives

\[
 \|\operatorname{Off}(R)\|_F\le\sqrt m,x,
 \qquad
 \|\operatorname{Off}(L)\|_F\le\sqrt m,y.
\]

On the uniform one-leg trace-zero event with
`alpha=sqrt((A-1)/m)`, Finding STRC-IR-01 yields

\[
 \|\mathcal M_U(Y)\|_\infty
 \le\frac1m\left(\frac\tau m+\alpha\sqrt m(x+y)\right).
\]

Using the shared budget rather than maximizing the terms separately,

\[
 \frac\tau m+\alpha\sqrt m(x+y)
 \le\sqrt{d_0}+\sqrt{2(A-1)}\sqrt{1-d_0}
 \le\sqrt{2A-1}.
\]

The last inequality is the two-dimensional Cauchy--Schwarz bound and is sharp for the relaxed
budget. Finally `sqrt(2A-1)<=A` because the squared gap is `(A-1)^2`.

**Verdict:** the conditional theorem merits `PROVED`. Positivity, exact rook support, and the
uniform one-leg event are all load-bearing; no `TrY<=A` hypothesis is used.

### Finding STRC-IR-03 — PASS: full-rank, trace-above-`A` scope is genuine

**Stable source locators:** rook artifact Section 6, equations (26)--(29).

For linearly independent Hermitian zero-diagonal `K_1,...,K_m` and nonzero Hermitian
zero-diagonal `H`, the matrix

\[
 S=\sum_vE_{v,v}\otimes K_v+H\otimes I
\]

is Hermitian and rook-supported. If `0<epsilon<||S||_infinity^-1`, then

\[
 Y_\epsilon=(I+\epsilon S)/\|I+\epsilon S\|_F
\]

is positive definite, full rank, Hilbert--Schmidt normalized, and belongs to neither one-leg
diagonal class. Rewriting its numerator as

\[
 \sum_vE_{v,v}\otimes(I+\epsilon K_v)+\epsilon H\otimes I
\]

shows operator-Schmidt rank `m+1`: both displayed factor families are linearly independent.

Since `TrS=0`,

\[
 \operatorname{Tr}Y_\epsilon
 =\frac{m^2}{\sqrt{m^2+\epsilon^2\|S\|_F^2}},
\]

which tends to `m` as `epsilon` tends to zero. Whenever `m>A`, it is therefore greater than `A`
for all sufficiently small positive `epsilon`.

**Verdict:** the theorem genuinely adds full-rank, high-operator-Schmidt-rank positive examples
outside the earlier near-pure trace window.

### Finding STRC-IR-04 — PASS: rook truncation is not a positive map

**Stable source locators:** rook artifact Section 7, equations (30)--(33); rook-truncation node
claim.  
**Reviewed claim hash:**
`sha256:496b1e3e4946b9f4244eff9cf371ea22aeaac1ba076e22f279f43c1bee96ed86`.

Let `e` be the normalized all-ones vector, `J=|e><e|`, and
`Y=|e tensor e><e tensor e|=J tensor J`. Direct pinching gives

\[
 (\Delta_1+\Delta_2-\Delta_1\Delta_2)(Y)
 =J\otimes I/m+I/m\otimes J-I\otimes I/m^2.
\]

Both `J` terms vanish on `e^perp tensor e^perp`, leaving the eigenvalue `-1/m^2`. Thus the
inclusion--exclusion union of the two commuting positive pinchings is not positive.

**Verdict:** the exact counterexample merits `PROVED`. It rules out declaring the rook truncation
positive; it does not rule out every joint structured decomposition or the general positive
target.

### Finding STRC-IR-05 — PASS: both circular cancellation matchings are valid and exponentially enumerable

**Stable source locators:** reversal-collision artifact Sections 2--3, equations (9)--(15);
collision-count node claim.  
**Reviewed claim hash:**
`sha256:913a8467944b1e977aeca2c5f8bc7bb4b1ea3f7f71f7154f50f65035f7907ac3`.

Each edge block contributes alternating negative/positive signed positions. Repeatedly deleting
an adjacent inverse pair on the forward circle records a chord between opposite signs with equal
labels. A chord can only enclose positions already deleted, so the recorded partial matching is
noncrossing. The survivors, in circular order, are exactly a cyclically reduced core. The same
construction in block-reversed circular order gives an independent noncrossing partial matching.

Deleting an inverse pair preserves alternation of the surviving circle. Hence each nonempty core
has equal numbers of unmatched negative and positive positions. A noncrossing partial matching on
`2N` labeled circular positions has an open/close/unmatched encoding and at most `3^(2N)` shapes.
Thus the two cancellation matchings contribute at most `3^(4N)=81^N` shape pairs.

**Verdict:** the two matching encodings are complete for an upper count; nonuniqueness merely
causes harmless overcounting.

### Finding STRC-IR-06 — PASS: fixed points and the component bound `c(H)<=N+2`

**Stable source locators:** reversal-collision artifact Section 4, equations (16)--(23);
collision-count node claim.  
**Reviewed claim hash:**
`sha256:913a8467944b1e977aeca2c5f8bc7bb4b1ea3f7f71f7154f50f65035f7907ac3`.

Fix the two matching shapes and a cyclic, sign-preserving identification `phi` of their unmatched
cores. The equality graph contains all matching edges and all `p--phi(p)` edges. Every matched
vertex lies on a two-vertex edge; every unmatched vertex lies on a `phi` edge. Therefore a
singleton component can only be a fixed point `phi(p)=p`.

For negative unmatched positions, list the forward indices increasingly as
`p_0<...<p_(r-1)` and the reverse-core indices increasingly as `q_0<...<q_(r-1)`. Reversal plus a
cyclic offset has rank form

\[
 \phi(p_j)=q_{s-j\pmod r}.
\]

At a fixed physical position `i`, the increasing ranks satisfy
`alpha(i)+beta(i)=s mod r`. Along the intersection, both ranks strictly increase, so their sum is
strictly increasing in `[0,2r-2]`. One residue class modulo `r` occurs at most twice. Hence there
are at most two fixed negative positions; the same argument gives at most two fixed positive
positions.

With at most four singleton components and every other component containing at least two of the
`2N` vertices,

\[
 c(H)\le f+(2N-f)/2=N+f/2\le N+2.
\]

**Verdict:** the fixed-point argument, treatment of self-loops, and component budget are correct.

### Finding STRC-IR-07 — PASS: final exponential count and fixed-order consequence

**Stable source locators:** reversal-collision artifact Sections 5--7, equations (24)--(29);
collision-count node claim.  
**Reviewed claim hash:**
`sha256:913a8467944b1e977aeca2c5f8bc7bb4b1ea3f7f71f7154f50f65035f7907ac3`.

For fixed matching shapes and core rotation, every graph component carries at most one free label,
so Finding STRC-IR-06 gives at most `m^(N+2)` assignments. Original inequalities `v_i!=a_i`,
sign compatibility, and realizability constraints can only reduce this number. There are at most
`2N` nonempty core rotations and one empty-core choice. Therefore

\[
 |\mathcal C_{m,N}|
 \le(2N+1)3^{2N}3^{2N}m^{N+2}
 =(2N+1)81^Nm^{N+2}.
\]

For `N>=1`, `2N+1<=3^N`, giving `243^N m^(N+2)`. The `N=0` empty-sequence case also satisfies
the displayed bound directly.

At fixed `N`, second-order Haar asymptotics may be applied termwise after the finite grouping.
The nonreturn leading covariance is at most the core length `2N`, yielding the artifact's
fixed-order bound

\[
 2N(2N+1)m^2(81/m)^N.
\]

At `N=2k`, its moment base has a strict large-`m` margin relative to the Werner threshold. This is
a fixed-order consequence only.

**Verdict:** the collision-count node merits `PROVED` at exact claim hash
`sha256:913a8467944b1e977aeca2c5f8bc7bb4b1ea3f7f71f7154f50f65035f7907ac3`.

### Finding STRC-IR-08 — UNRESOLVED: positive-genus control is still missing

**Stable source locators:** reversal-collision artifact Sections 8--10, especially equation (30);
updated centered-bound evidence, caveats, event, and `growing-centered-reversal-moment` frontier.  
**Reviewed centered claim hash:**
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

The deterministic count controls the free-reduction label entropy of the planar/annular cyclic
support. It does not give a finite-`d` error estimate uniform when `N=c_m log d`. The unresolved
terms are repeated-label positive-genus Weingarten diagrams. A sufficient next theorem must
separate the already counted annular term and bound the total genus-`g` remainder by
`d^(-2g)` times only exponential growth in `N`; the usual factorial absolute permutation count is
not enough.

The centered-bound node links the collision count as non-load-bearing progress and explicitly
retains this positive-genus task in its frontier. Its fixed-`m`, fixed-`eta`, `d->infinity`
quantifier and `CONJECTURED` level remain correct.

**Verdict:** no promotion of `HEXT.same-tuple-werner-centered-bound` is justified.

## 4. Promotion recommendations

The following findings provide exact review bindings:

- positive rook-support base case: Findings STRC-IR-01 and STRC-IR-02, reviewed hash
  `sha256:cbe076658098ba4cf5732a06f9ae9a0bfeefbc0f433152fb9703fbd86c7e419a`;
- rook-truncation positivity obstruction: Finding STRC-IR-04, reviewed hash
  `sha256:496b1e3e4946b9f4244eff9cf371ea22aeaac1ba076e22f279f43c1bee96ed86`;
- reversal cyclic-collision count: Findings STRC-IR-05 through STRC-IR-07, reviewed hash
  `sha256:913a8467944b1e977aeca2c5f8bc7bb4b1ea3f7f71f7154f50f65035f7907ac3`.

Do not promote `HEXT.same-tuple-werner-centered-bound`; Finding STRC-IR-08 rebinds its unresolved
claim hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

I make no canonical level change in this review.

## 5. Limitations

This review does not prove a logarithmic-degree finite-`d` Weingarten expansion, a uniform
positive-genus bound, the centered high-probability spectrum claim, or the general same-tuple
strong-norm lemma. The rook theorem does not extend to coefficients with double-off-diagonal
entries or to a neighborhood of rook support. The finite enumeration is a smoke test, not support
for the universal combinatorial proof.

