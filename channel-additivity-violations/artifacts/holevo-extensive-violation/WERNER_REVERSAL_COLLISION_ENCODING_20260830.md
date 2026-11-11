# Werner reversal moments: exponential free-reduction collision encoding

Date: 2026-08-30

Status: proposer-side analytic artifact for `HEXT.same-tuple-werner-centered-bound`.  No canonical
YAML is changed.  The result below proves the requested exponential count for the fixed-word,
genus-zero/second-order collision support, but it does **not** provide a uniform finite-`d`
Weingarten estimate through `k=Theta(log d)`.  The centered-spectrum claim therefore remains
mathematically unresolved and its canonical node remains `CONJECTURED`.

No numerical computation is used.

## 1. Result

Let

\[
 E_m=\{(v,a)\in[m]^2:v\ne a\},
 \qquad x_{v,a}=g_v^{-1}g_a\in F_m.
\tag{1}
\]

For a block sequence

\[
 \mathbf e=(e_1,\ldots,e_N)\in E_m^N,
\tag{2}
\]

write

\[
 w(\mathbf e)=x_{e_1}\cdots x_{e_N},
 \qquad
 \check w(\mathbf e)=x_{e_N}\cdots x_{e_1},
\tag{3}
\]

and let `cyc(w)` denote the cyclically reduced core, regarded as a cyclic word.  Define

\[
 \mathcal C_{m,N}:=
 \{\mathbf e\in E_m^N:
   \operatorname{cyc}(w(\mathbf e))
   =\operatorname{cyc}(\check w(\mathbf e))
   \text{ up to cyclic rotation}\}.
\tag{4}
\]

The main finite combinatorial statement is

\[
 \boxed{
 |\mathcal C_{m,N}|
 \le (2N+1)81^N m^{N+2}
 \le 243^N m^{N+2}.}
\tag{5}
\]

For the moment order `N=2k`, this is

\[
 |\mathcal C_{m,2k}|
 \le 59049^k m^{2k+2}.
\tag{6}
\]

Thus the reduction-plus-block-reversal collision set has the desired form
`C^k m^{2k+O(1)}` with a universal, explicit, nonoptimized constant.  The proof uses two circular
noncrossing cancellation matchings and one cyclic core matching.  The associated equality graph
has at most `N+2` connected components, so it has at most `m^{N+2}` labelings.  The two
noncrossing matching shapes contribute only exponentially many possibilities.

At fixed `N`, the second-order Haar-unitary cyclic-matching rule then bounds the nonreturn leading
term by

\[
 2N(2N+1)m^2\left(\frac{81}{m}\right)^N.
\tag{7}
\]

For `N=2k`, its base relative to the Werner allowance
`h_W^{2k}~[18(1+eta)^2/m]^k` is

\[
 \frac{81^2}{18(1+\eta)^2m}
 =\frac{364.5}{(1+\eta)^2m},
\tag{8}
\]

apart from a polynomial in `k` and the fixed prefactor `m^2`.  Hence every fixed-order
genus-zero collision family is safely below the target in the project's regime `ln m>18`.

What remains is not another free-reduction word-count problem: it is a **uniform finite-`d`**
bound on positive-genus/remainder Weingarten diagrams with only exponential diagram growth up to
`N=c_m log d`.  Equation (5) does not control those remainders.

## 2. Why cyclic reduction is the correct support

For the centered operator

\[
 S_U=\frac1{m^2}\sum_{e\in E_m}A_e\otimes A_e^*,
 \qquad A_{v,a}=U_v^*U_a,
\tag{9}
\]

the exact even-moment expansion at `N=2k` is

\[
 \operatorname{Tr}(S_U^N)
 =\frac1{m^{2N}}
 \sum_{\mathbf e\in E_m^N}
 \operatorname{Tr}W_U(\mathbf e)\,
 \overline{\operatorname{Tr}\check W_U(\mathbf e)}.
\tag{10}
\]

For fixed nontrivial free-group words `g,h`, second-order freeness of independent Haar unitaries
gives a nonzero `d->infinity` limit of

\[
 \mathbb E[\operatorname{Tr}U_g\,
 \overline{\operatorname{Tr}U_h}]
\tag{11}
\]

only when their cyclically reduced cores have matching primitive cyclic words and matching
powers.  The limiting value counts cyclic matches and is at most the core length.  Thus (4)
contains the entire nonreturn support of the fixed-word leading term.  It intentionally
overcounts it by allowing every cyclic equality, including cases whose primitive powers do not
match.

Identity cores are the return sector.  They were bounded separately in
`WERNER_CENTERED_GROWING_TRACE_METHOD_GATE_20260830.md` by the free-group norm constant
`(3m-4)/m^2~3/m`.  The present artifact concentrates on nonempty cyclic cores, although the
combinatorial bound (5) also includes the empty-core cases.

## 3. Circular cancellation matchings

Each block `e_i=(v_i,a_i)` contributes the two signed letter positions

\[
 V_i=(i,-),\qquad A_i=(i,+),
\tag{12}
\]

carrying labels `v_i` and `a_i`.  There are `2N` positions.  The forward circular reading order is

\[
 V_1,A_1,V_2,A_2,\ldots,V_N,A_N,
\tag{13}
\]

while the block-reversed circular order is

\[
 V_N,A_N,V_{N-1},A_{N-1},\ldots,V_1,A_1.
\tag{14}
\]

The signs alternate in either circular order.

### Lemma 1: noncrossing cyclic-reduction matching

For any assignment of the `2N` labels, cyclic reduction of the forward word can be encoded by a
noncrossing partial matching `P` of the `2N` circular positions such that:

1. every matched pair has opposite signs and equal labels;
2. the unmatched positions, read in the forward circular order, spell the cyclically reduced
   core.

The block-reversed word has an analogous matching `Q`, noncrossing in order (14).

**Proof.**  Repeatedly delete an adjacent inverse pair on the current circle, recording a chord
between the two deleted original positions.  A chord recorded at its deletion bounds a region
whose earlier positions have already been deleted, so two recorded chords cannot cross.  Stop
when there is no adjacent inverse pair.  The surviving cyclic word is cyclically reduced, and the
recorded pairs have the stated sign and label properties.  Apply the same procedure in the
block-reversed order for `Q`.  `square`

The cancellation order need not be unique.  Existence is enough for an upper count.  Each
noncrossing partial matching on `L` labeled circular points has a standard open/close/unmatched
encoding, so the number of its shapes is at most the `L`th Motzkin number and therefore at most
`3^L`.  Consequently

\[
 \#\{P\}\le3^{2N},\qquad
 \#\{Q\}\le3^{2N}.
\tag{15}
\]

Every cancellation removes one negative and one positive position.  Hence if the cyclic core is
nonempty, its unmatched set contains the same number `r` of each sign and alternates in sign.

## 4. The equality graph

Fix matching shapes `P,Q`.  Suppose their two surviving cyclic cores agree after a cyclic
rotation.  Choose one such rotation and let

\[
 \phi:U_P\longrightarrow U_Q
\tag{16}
\]

be the induced bijection from the unmatched positions of `P` to those of `Q`.  It preserves
signed letters, hence it preserves signs and requires equal labels.  There are at most `2N`
possible rotations; if both unmatched sets are empty, there is one empty choice.

Construct a graph `H=H(P,Q,phi)` on the `2N` signed positions:

- add one equality edge for every pair in `P`;
- add one equality edge for every pair in `Q`;
- add an equality edge `p--phi(p)` for every `p in U_P`.

Self-loops are allowed in the last family.  Every edge of `H` is an equality constraint on its two
endpoint labels.  Thus the number of label assignments compatible with a fixed graph is at most

\[
 m^{c(H)},
\tag{17}
\]

where `c(H)` is the number of connected components after self-loops are ignored.  The original
edge conditions `v_i!=a_i` and all inequalities needed to make `P,Q` the actual cancellation
matchings can only decrease this number.

The key point is the following half-dimensional component bound.

### Lemma 2: `c(H)<=N+2`

Every vertex that is matched by `P` is incident to a two-vertex equality edge.  Every vertex
unmatched by `P` is incident to its `phi` edge.  Therefore a singleton component can occur only at
a fixed point `phi(p)=p`; at such a point `p` is unmatched by both `P` and `Q`.

There are at most four fixed points of `phi`: at most two negative positions and at most two
positive positions.

To see this, treat the negative positions first.  Let

\[
 P_-:=\{i:V_i\in U_P\},\qquad
 Q_-:=\{i:V_i\in U_Q\}.
\tag{18}
\]

Both have cardinality `r`.  In the forward core, their block indices occur in increasing cyclic
order; in the block-reversed core, the indices in `Q_-` occur in decreasing cyclic order.  After
choosing linear cuts and absorbing the cyclic rotation into an offset `s`, write

\[
 P_-=(p_0<\cdots<p_{r-1}),\qquad
 Q_-=(q_0<\cdots<q_{r-1}).
\tag{19}
\]

Then the restriction of `phi` has the rank form

\[
 \phi(p_j)=q_{\,s-j\pmod r}.
\tag{20}
\]

If a physical position `i` is fixed, and its increasing ranks in `P_-` and `Q_-` are `alpha(i)`
and `beta(i)`, then

\[
 \alpha(i)+\beta(i)\equiv s\pmod r.
\tag{21}
\]

As `i` increases through `P_- intersect Q_-`, both ranks strictly increase.  Their sum is
strictly increasing and lies between `0` and `2r-2`.  It can therefore assume at most two values
in one residue class modulo `r`.  Hence there are at most two fixed negative positions.  The same
argument applied to

\[
 P_+:=\{i:A_i\in U_P\},\qquad
 Q_+:=\{i:A_i\in U_Q\}
\tag{22}
\]

gives at most two fixed positive positions.

Let `f<=4` be the total number of fixed points.  All other components contain at least two
vertices.  Since `H` has `2N` vertices,

\[
 c(H)\le f+\frac{2N-f}{2}
 =N+\frac f2\le N+2.
\tag{23}
\]

This proves Lemma 2.  `square`

## 5. Proof of the exponential count

Every sequence in `mathcal C_{m,N}` admits:

1. a forward circular noncrossing matching `P`;
2. a block-reversed circular noncrossing matching `Q`;
3. one of at most `2N` cyclic identifications `phi` of the two cores; and
4. a label assignment compatible with `H(P,Q,phi)`.

Equations (15), (17), and (23) therefore give

\[
 |\mathcal C_{m,N}|
 \le (2N+1)\,3^{2N}\,3^{2N}\,m^{N+2}
 =(2N+1)81^Nm^{N+2}.
\tag{24}
\]

Since `2N+1<=3^N` for `N>=1`, (24) proves (5).  The count is deliberately loose: it ignores
opposite-sign compatibility, the internal inequalities `v_i!=a_i`, consistency conditions that
make a proposed noncrossing matching realizable by adjacent cancellations, and primitive-power
matching.  Every omission enlarges the counted set, so none compromises the upper bound.

## 6. Sharper no-cancellation subclass

There is a useful check with a much smaller constant.  Suppose both full signed words (13)--(14)
are already cyclically reduced, so no letter is deleted.  If their cyclic words agree, sign
preservation forces the rotation to move whole blocks.  For one of the `N` block shifts `s`,

\[
 e_i=e_{s-i\pmod N}\qquad(1\le i\le N).
\tag{25}
\]

This is a reflection of the cyclic block indices.  For even `N`, a reflection has at most
`N/2+1` orbits.  Therefore the number of no-cancellation collision sequences is at most

\[
 N|E_m|^{N/2+1}
 =N[m(m-1)]^{N/2+1}.
\tag{26}
\]

For `N=2k`, after the moment normalization `m^{-4k}`, even the worst termwise trace bound `d^2`
gives

\[
 2k\,d^2[m(m-1)]^{k+1}m^{-4k}
 =2k\,d^2m(m-1)
   \left(\frac{m-1}{m^3}\right)^k.
\tag{27}
\]

This has base `Theta(m^{-2})^k`, far below the Werner base `Theta(m^{-1})^k`.  Hence literal or
cyclic block palindromes were never the dangerous genus-zero family; the only nontrivial work was
to show that nested reductions do not restore `m^{4k}` free labels.  Lemma 2 proves that they do
not: they leave at most `2k+2` free label components.

## 7. Fixed-order Haar consequence

For fixed `N`, group the exact expectation (10) by its two reduced free-group words.  On the
nonreturn support, the limiting second-order covariance is at most `2N`, because there are at most
`2N` cyclic matches.  Therefore (5) yields

\[
 \limsup_{d\to\infty}
 \left|
 \frac1{m^{2N}}
 \sum_{\substack{\mathbf e:\ 
   \operatorname{cyc}(w)\ne1,\ 
   \operatorname{cyc}(\check w)\ne1}}
 \mathbb E\left[
  \operatorname{Tr}W_U(\mathbf e)
  \overline{\operatorname{Tr}\check W_U(\mathbf e)}
 \right]
 \right|
 \le
 2N(2N+1)m^2\left(\frac{81}{m}\right)^N.
\tag{28}
\]

The expression is written as a limsup at fixed `N`; finite summation permits termwise use of the
fixed-word theorem.  Equation (28) does not assert any uniformity as `N` grows with `d`.

At `N=2k`, comparison with (4)--(5) gives

\[
 \frac{\text{right side of (28)}}{h_W^{2k}}
 \le4k(4k+1)m^2
 \left(\frac{81^2}{18(1+\eta)^2m}\right)^k(1+o_m(1)).
\tag{29}
\]

Thus the full fixed-order annular/cyclic collision contribution has a strict constant margin in
the intended large-`m` regime.  This is stronger than checking only literal palindromes or only
return paths.

## 8. What remains at growing order

The count (5) solves the free-reduction label entropy requested by the centered reversal-moment
route.  It does not solve the uniform Haar integration problem.  At `N=c_m log d`, the missing
inputs are:

1. a finite-`d` expansion separating the annular/cyclic term controlled by (5) from positive-genus
   terms;
2. a bound `C_0^N d^{-2g}` for the total absolute weight of genus `g` diagrams, with `C_0`
   independent of `N`; and
3. control of words in which one generator occurs `Theta(N)` times without using the factorial
   absolute permutation bound `(CN)^{CN}`.

The exact unresolved family is therefore repeated-label **positive-genus Weingarten diagrams**.
The planar/free-reduction collision family itself now has the exponential bound (5).  A successful
next step could use a nonbacktracking Weingarten expansion or a transfer operator on paired stack
states; its state count must be exponential in `N`, not factorial.

A sufficient uniform extension would be: for some fixed `C_g,C_*` and all
`N<=c_m log d`,

\[
 \left|
 \mathbb E\operatorname{Tr}(S_U^N)-
 \mathcal A_{m,N}^{(0)}(d)
 \right|
 \le d^2\sum_{g\ge1}d^{-2g}
       \left(\frac{C_*}{m}\right)^N C_g^N,
\tag{30}
\]

where `mathcal A^{(0)}` is the return plus annular contribution already controlled by the free
norm estimate and (28).  Equation (30) is a proposed interface, not a theorem here.

## 9. Quantifier and scope audit

- Equation (5) is a finite, deterministic combinatorial bound for every `m,N`.
- Equation (28) uses second-order Haar asymptotics only after fixing `m,N` and then taking
  `d->infinity`.
- Equations (5) and (28) do not imply a high-probability norm bound, because a trace proof needs
  `N=Theta(log d)` and a uniform finite-`d` remainder.
- No deterministic bad tuple or rare-event argument is used.  This artifact gives no generic Haar
  counterexample.
- The absolute-unbounded extensive-violation result is already established elsewhere.  This note
  concerns only the still-open full-size same-tuple Werner gate.

## 10. Proposed atomic DAG updates (not applied)

All proposed statuses remain at most `CONJECTURED`; no canonical YAML is edited.

1. Create or record a lemma-level evidence item
   `HEXT.werner-reversal-cyclic-collision-count`: equation (5) gives a universal exponential
   upper bound on the fixed-word reduction-plus-reversal collision set.
2. Link that evidence to the frontier of `HEXT.same-tuple-werner-centered-bound`, narrowing the
   remaining growing-moment task to uniform positive-genus Weingarten control.
3. Replace any proposed frontier phrased as “count all cyclic collision words” by the smaller task
   in Section 8; the free label-entropy part is handled by (5), subject to independent review.
4. Do not promote the centered-spectrum node: neither (5) nor the fixed-order consequence (28)
   supplies the required `N=c_m log d` quantifier.

## 11. Reference interface

The only external probabilistic input used for (28) is the fixed-word cyclic matching rule from
J. A. Mingo, P. Sniady, and R. Speicher, *Second Order Freeness and Fluctuations of Random
Matrices II: Unitary Random Matrices*, arXiv:math/0405258.  Its use is explicitly limited to
fixed `N`.  The combinatorial bound (5) is independent of that theorem.
