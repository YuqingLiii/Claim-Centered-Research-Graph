# Fixed-dimension conjugate-collision obstruction for iid Haar layers

Date: 2026-08-30

Status: proposer-side proof; independent review pending.

All logarithms are base two.

## Purpose

The finite-dimensional unbounded-gap construction uses a product

\[
 L_J=\Phi_{U^{(1)}}\otimes\cdots\otimes\Phi_{U^{(J)}},
 \qquad R_J=\overline{L_J},
\]

where every `U^(j)=(U_1^(j),...,U_m^(j))` is an independent Haar tuple in `U(D)^m` and

\[
 \Phi_U(\rho)=\frac1m\sum_{i=1}^m U_i\rho U_i^*.
\]

A tempting full-size route is to fix one sufficiently large `D` once and let `J` grow.  This note
shows that the iid conjugation-invariant ensemble itself obstructs that plan: almost every long
sample contains an asymptotically perfect matching of layers to approximate conjugates.  Bell
inputs on those within-side pairs force a side entropy rate strictly below the Collins--Youn rate
needed by the construction when `m>e^18`.

This is stronger than merely observing that the available strong-convergence theorem is proved
only for fixed `J`: for the iid fixed-`D` model, the desired side bound is actually false at large
`J`.

## 1. Universal matched-pair Bell bound

For any tuple `U in U(D)^m`, let `bar U` be the entrywise conjugate tuple.  On the normalized Bell
state `Omega_D`, the `m` matched Kraus terms all give the same vector because

\[
 (U_i\otimes\overline{U_i})\Omega_D=\Omega_D.
\]

Merging those identical ensemble labels gives one weight `1/m` and `m^2-m` remaining weights
`1/m^2`.  Therefore

\[
 S_{\min}(\Phi_U\otimes\Phi_{\bar U})\le h_m,
 \qquad
 h_m:=2\log m-\frac{\log m}{m}.
\tag{1}
\]

This bound is deterministic and independent of `D` and `U`.

## 2. Stability under an approximate conjugate

Equip `U(D)^m` with

\[
 d(U,V)=\max_i\|U_i-V_i\|_\infty.
\]

If `d(V,bar U)<=epsilon`, the convexity of the diamond norm and the usual unitary-channel bound
give

\[
 \|\Phi_V-\Phi_{\bar U}\|_\diamond\le 2\epsilon.
\tag{2}
\]

Consequently the outputs of `Phi_U tensor Phi_V` and `Phi_U tensor Phi_barU` on `Omega_D` have
trace distance at most `epsilon`.  The sharp entropy-continuity bound then yields, for
`0<=epsilon<=1-1/D^2`,

\[
 S_{\min}(\Phi_U\otimes\Phi_V)
 \le h_m+\eta_D(\epsilon),
\quad
 \eta_D(\epsilon):=\epsilon\log(D^2-1)+h_2(\epsilon).
\tag{3}
\]

For fixed `D`, `eta_D(epsilon)->0` with `epsilon->0`.

## 3. Almost-perfect conjugate matching in a long iid sample

Let `mu` be product Haar measure on the compact space `X=U(D)^m`, and let
`c(U)=bar U`.  The measure is invariant under `c`.

Fix `epsilon>0`.  Choose a finite Borel partition of `X` into cells of diameter at most
`epsilon`, refining it if necessary so that conjugation permutes the cells and every boundary has
`mu`-measure zero.  For iid samples `U^(1),U^(2),...`, the strong law applied to the finitely many
cell indicators gives

\[
 \frac{N_C(J)}J\longrightarrow\mu(C)=\mu(c(C))
\]

simultaneously for every cell.  Pair samples in `C` with samples in `c(C)`; in a self-conjugate
cell, pair samples internally.  The total unmatched count is `o(J)`.  Each matched pair `(a,b)`
satisfies

\[
 d(U^{(b)},\overline{U^{(a)}})\le\epsilon.
\tag{4}
\]

Thus, almost surely, for every fixed `epsilon` all but `o(J)` layers can be partitioned into
approximate-conjugate pairs.

## 4. Consequence for the one-side minimum output entropy

Use a Bell input across each paired pair of layer inputs, and an arbitrary pure input on every
unmatched layer.  Entropy is additive across this product of pair blocks.  Equation (3) bounds each
paired output by `h_m+eta_D(epsilon)`.  Any unmatched random-unitary layer has an output that is a
mixture of `m` pure states and hence entropy at most `log m`.  Therefore, almost surely,

\[
 \limsup_{J\to\infty}\frac1J S_{\min}(L_J)
 \le\frac12\bigl(h_m+\eta_D(\epsilon)\bigr).
\]

Apply the construction to a fixed countable sequence `epsilon_n->0` and intersect the resulting
probability-one events.  Letting `n->infinity` then gives

\[
 \boxed{
 \limsup_{J\to\infty}\frac1J S_{\min}(L_J)
 \le \frac{h_m}{2}
 =\log m-\frac{\log m}{2m}.}
\tag{5}
\]

The same conclusion holds for `R_J=bar L_J`.

## 5. Conflict with the side rate required by the unbounded-gap proof

The Collins--Youn/Bordenave--Collins construction seeks the lower rate

\[
 s_m:=\log m-\log(1+9/m).
\tag{6}
\]

If `ln m>18`, then

\[
 \log(1+9/m)<\frac{9}{m\ln2}<\frac{\log m}{2m},
\]

and hence

\[
 s_m>\frac{h_m}{2}.
\tag{7}
\]

Equations (5)--(7) show that, for every fixed finite `D`, the target global side lower bound fails
almost surely for sufficiently long iid Haar layer products.  A high-probability realization of
that particular construction must therefore let `D=D(J)` escape every fixed bound as `J` grows.

Since the gap certified by the current fixed-`m` Collins--Youn/Bell calculation is only `O(J)`,
while the input cost is `J log D(J)`, that certificate no longer gives a positive asymptotic gap
divided by the full input logarithmic cost once `D(J)->infinity`.  This is not an upper bound on
every possible witness for the same channels.

## 6. Scope and escape routes

The conclusion is model-specific.

- It applies to iid layers drawn from a conjugation-invariant distribution such as product Haar.
- It does not rule out a deliberately oriented distribution supported away from its conjugate,
  though compactness then forces repeated/near-repeated layers and returns the problem to
  fixed-channel self-leakage.
- It does not rule out a different witness whose gain per layer grows with `log D`.
- It does not prove that every deterministic fixed-`D` sequence has low side entropy.
- It does not prove the Hayden--Penington extensive branch impossible.

The viable escape must therefore change at least one of: the iid conjugation-invariant layer
ensemble, the constant-per-layer Bell collision mechanism, or the fixed-channel leakage problem.

## External input

The entropy-continuity step uses Audenaert's sharp Fannes inequality, Theorem 1 of
`holevo-extensive-violation/artifacts/primary-sources/audenaert-0610146.pdf`.  The probabilistic
matching uses only the strong law of large numbers for the finitely many cells of each fixed
partition.
