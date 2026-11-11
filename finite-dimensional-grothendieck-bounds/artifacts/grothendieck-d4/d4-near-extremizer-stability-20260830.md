# Exact near-extremizer audit for the (W_9) closure term

**Status.**  Exact finite theorem plus exact no-go for a natural coarse
stability ansatz.  This note does **not** prove the global classical upper
bound.  It isolates the precise (W_9) threshold that would close the
remaining (217+83) benchmark and proves that the closest nontrivial
one-coordinate shell already falls below it.

The independent replay entry point is

```
grothendieck-d4/tools/h4_near_extremizer_stability_checker.py
```

It imports the preceding exact CG checker, reconstructs the projectors from
the frozen integer matrix, verifies all 1360 polarized coefficients over the
biquadratic field, and then performs the new exact comparisons below.  No
floating-point eigenvector is used in a decisive assertion.

## 1. Setup and the exact closure threshold

Use the notation of the rank-one CG report.  For complementary ternary
(p,q), let

\[
 e=Ep,\qquad f=Fq,\qquad
 \alpha=\lVert e\rVert^2,\qquad \beta=\lVert f\rVert^2,
\]

and let (w_9) be the nine-dimensional CG-block weight of
(e\otimes f).  Put

\[
 r=\frac{w_9}{\alpha\beta},\qquad
 c(r)=c_*+\kappa r,
\]

where

\[
 c_*=\frac{3\gamma_1+\gamma_2}{4},\qquad
 \kappa=\gamma_2+\gamma_3-2\gamma_1>0.
\]

The exact rank-one identity gives

\[
 \lVert e\circ f\rVert^2=c(r)\alpha\beta.
\]

At the split (s=217,t=83), the (q)-branch of the block-weighted leakage
penalty, using the already registered rational spectral-gap bounds, is

\[
 \Pi(r)=G\frac{15c(r)}{1+15c(r)},\qquad
 G=83\left(
 \frac{11691401709341221}{2}
 -\frac{56846466952431285}{34}
 \right).                                                \tag{1.1}
\]

Let

\[
 T=7114830222845879                                      \tag{1.2}
\]

be the strict lower endpoint of the ten-block correction target.  Since
(Pi) is strictly increasing, its exact critical ratio is

\[
 r_{\rm crit}
 =\frac{T/[15(G-T)]-c_*}{\kappa}.                        \tag{1.3}
\]

The checker proves by exact algebraic-number sign tests that

\[
 \boxed{\quad
 \frac{628}{10^6}<r_{\rm crit}<\frac{629}{10^6}.
 \quad}                                                  \tag{1.4}
\]

The decimal annotation is

\[
 r_{\rm crit}\simeq0.000628629382810043788.
\]

Thus (1.3), rather than the previously used rough (1/6000), is the exact
quantitative gate for the last fraction of the (217+83) correction.

## 2. The archived witness really clears the target

For the frozen equality witness, the exact CG evaluation gives

\[
 \frac1{1500}<r_{\rm arch}<\frac1{1480},
 \qquad
 r_{\rm arch}\simeq0.000673063509034500980.              \tag{2.1}
\]

The new exact comparison is

\[
 \boxed{\Pi(r_{\rm arch})>T}.                            \tag{2.2}
\]

Numerically, only as an annotation,
(Pi(r_{\rm arch})-T\) is about (3.06\times10^{12}).  Hence the
degree-twelve/nonradial CG statistic (w_9) is quantitatively large enough
on the archived witness to beat the requested
(7{,}114{,}830{,}222{,}845{,}879) threshold.  What remains unproved is the
stability implication forcing comparable (w_9) on every putative
competitor at or above the classical target.

## 3. Exact closest-shell theorem

Write the frozen signs as (x=p+q,y=p-q).  Flip the sign of one nonzero
coordinate of (p), leaving its support and (q) fixed.  The checker
enumerates all 300 admissible one-coordinate support-sign flips of (p) or
(q) using the exact integer matrix.

### Theorem 3.1 (proved exactly)

Among all such nontrivial one-coordinate flips with positive Bell loss, the
smallest loss is

\[
 g=2353967343413440.                                     \tag{3.1}
\]

It is attained by the six (H_4)-equivalent (p)-coordinates

\[
 \{46,56,85,99,131,148\}                                 \tag{3.2}
\]

in zero-based indexing.  Moreover

\[
 884g<C<885g,
 \qquad C=2081044153087351400.                           \tag{3.3}
\]

Consequently every one of these six neighbors has objective

\[
 B=C-g>\frac{883}{884}C.                                 \tag{3.4}
\]

For the representative flip at coordinate 85, the exact CG computation
proves

\[
 \boxed{\quad
 \frac{561}{10^6}<r_{85}<\frac{562}{10^6}<r_{\rm crit}.
 \quad}                                                  \tag{3.5}
\]

Its numerical annotation is

\[
 r_{85}\simeq0.000561976981776912121.
\]

Finally, the checker proves the decisive reverse comparison

\[
 \boxed{\Pi(r_{85})<T}.                                  \tag{3.6}
\]

The deficit (T-\Pi(r_{85})) is approximately
(4.59\times10^{12}).

### Theorem 3.2 (proved exactly)

The complete two-coordinate support-sign shell consists of

\[
 \binom{300}{2}=44850
\]

pairs.  Exact quadratic update formulas show that every one of these pairs
also has objective strictly below (C).  The smallest two-coordinate loss
is

\[
 g_2=3299723804685584,                                   \tag{3.7}
\]

attained by the three (p)-pairs

\[
 (46,148),\qquad(56,131),\qquad(85,99).                  \tag{3.8}
\]

Thus the archived witness is an exact strict local maximizer through
Hamming radius two inside the fixed complementary-support cell.  This is an
objective theorem only; no claim about the (W_9) values of the full
two-coordinate shell is made here.

## 4. Exact no-go and what it does not say

The following natural coarse stability statement is false:

> If a complementary (217+83) pair has Bell objective exceeding
> ((883/884)C), then (w_9/(\alpha\beta)\ge r_{\rm crit}).

Indeed, the coordinate-85 neighbor satisfies the premise by (3.4) and
violates the conclusion by (3.5).  This is stronger than a random numerical
counterexample: it is the nearest positive-loss shell among all single
support-sign flips, and all comparisons are exact.

This no-go does **not** refute the sharper statement needed for the global
proof,

\[
 p^TAp-q^TAq\ge C
 \quad\Longrightarrow\quad
 \frac{w_9}{\alpha\beta}\ge r_{\rm crit},                \tag{4.1}
\]

nor does it prove (4.1).  It shows that a proof of (4.1) cannot come from a
wide, objective-only continuity basin around the archived witness.  The
barrier is encountered at the very first discrete shell.

## 5. Minimal remaining gate

For the (217+83) cell, a sufficient publishable lemma is the exact
implication (4.1), with (r_{\rm crit}) given by (1.3).  The present work
reduces its quantitative burden to a narrow separation:

\[
 r_{85}<0.000562
 <r_{\rm crit}<0.000629
 <r_{\rm arch}.                                          \tag{5.1}
\]

The next statistic must distinguish the target superlevel set from the
first one-flip shell.  Two concrete routes remain:

1. evaluate a second independent degree-twelve nonradial (H_4) invariant
   on the six-point shell and derive an exact two-statistic SOS inequality;
2. decompose the Bell deficit and (W_9) change on each signed (H_4) orbit
   of two-coordinate flips, then seek a sharp discrete tangent inequality
   valid only on the superlevel set (B\ge C).

Any proposed affine inequality involving only (C-B) and (r) must first
pass the exact shell datum

\[
 (C-B,r)=(2353967343413440, r_{85}),                    \tag{5.2}
\]

as well as the archived point ((0,r_{\rm arch})).  This is now the smallest
replayable obstruction for the near-extremizer route.
