# Werner centered moment: final conditional Markov assembly

Date: 2026-08-30

Status: proposer-side conditional assembly for Question 3. No canonical YAML is changed. This note
treats `WERNER_EQUALITY_COMPONENT_GENUS_GATE_20260830.md` only as a `CONJECTURED` input and does
not promote any conclusion. The centered spectral statement and the full-size extensive-violation
theorem remain **OPEN**.

No browser, certificate run, or large computation is used.

## 1. Outcome

Fix an integer `m>e^18` and fixed `eta>=0`, before sending `d` to infinity. Let

\[
 R_U={1\over m^2}\sum_{v,a=1}^m
 U_v^*U_a\otimes U_a^*U_v,
 \qquad
 S_U=R_U-I/m,
\tag{1}
\]

and put

\[
 A=1+{9(1+\eta)^2\over m},
 \qquad
 H=h_W(m,\eta)
 :=\sqrt{(A^2-1)(1-m^{-2})}.
\tag{2}
\]

This note derives one explicit conditional moment inequality. Define

\[
\begin{aligned}
 u&:={3m-4\over m^2H},\\
 a&:={4096\over mH},\\
 x_{43}&:={m^2N^{43}\over d^2},\\
 x_{24}&:={m^2N^{24}\over d^2},\\
 \theta&:={6(2N)^{7/2}\over d^2}.
\end{aligned}
\tag{3}
\]

Subject only to the three proposer-side inputs isolated in Section 3, every even `N` for which
`theta,x_43,x_24<1` satisfies

\[
\boxed{
 {\mathbb E\operatorname{Tr}(S_U^N)\over H^N}
 \le
 2d^2u^N
 +{m^2a^N\over1-\theta}
 \left[
   2^{17}N^4
   +{x_{43}\over1-x_{43}}
   +N^{24}{x_{24}\over1-x_{24}}
 \right].}
\tag{4}
\]

Choose any fixed

\[
 \gamma>{2\over\log(1/u)}
\tag{5}
\]

and the even moment order

\[
 N(d):=2\left\lceil{\gamma\log d\over2}\right\rceil.
\tag{6}
\]

Then `N(d)=gamma log d+O(1)`, every bracketed handle parameter in (4) tends to zero, and the
right-hand side of (4) tends to zero. Since `S_U` is Hermitian and `N(d)` is even,

\[
 \|S_U\|_\infty^N\le\operatorname{Tr}(S_U^N).
\]

Markov therefore gives

\[
 \Pr\{\|R_U-I/m\|_\infty>H\}\longrightarrow0.
\tag{7}
\]

Thus there is no further asymptotic-constant or Markov obstruction after the three candidate
inputs are independently proved. At present, however, those inputs are not all reviewed, so (7)
is a conditional route and not a completed centered theorem.

## 2. Reviewed bindings and current statuses

The exact centered/reversal expansion and return estimate are in
`WERNER_CENTERED_GROWING_TRACE_METHOD_GATE_20260830.md`, SHA-256

`6f0d52b4d48433c9f16d8ded4440469268b336df3af8f23f4a8b798ac15752ce`.

They were independently accepted in Finding STPW-IR-05 of
`SAME_TUPLE_POSITIVE_WERNER_TRACE_INDEPENDENT_REVIEW_20260830.md`.

The exact spectral reduction to threshold (2) is `PROVED` at exact claim hash

`sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67`.

The exact constellation Euler/Weingarten dimension power is `PROVED` at exact claim hash

`sha256:c1c37d08c4f0cf37cb698b26a03d48cef0dd668686b71ed3a8391fed63c1d62a`.

The connected positive-genus structural weighted count

\[
 S^{(c=1)}_{N,h}\le4096^N N^{43h},\qquad h\ge1,
\tag{8}
\]

is `PROVED` at exact claim hash

`sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6`.

The skeletonwise monotone-Weingarten excess tail is `PROVED` at exact claim hash

`sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4`.

The candidate equality and disconnected-sector input is
`WERNER_EQUALITY_COMPONENT_GENUS_GATE_20260830.md`, SHA-256

`1aac1c071b61dc3809a3bcf28339263508e301062eba8980e8b287a64ef92be7`.

It is used here only conditionally. The current centered node remains exact claim hash

`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

## 3. Exact conditional inputs not yet all independently proved

The assembly uses the following three inputs and no stronger all-genus theorem.

### Input P — local planar tree--cotree repair

For connected topological genus zero,

\[
 \boxed{
 S^{(c=1)}_{N,0}le2^{17}N^4\,4096^N.}
\tag{P}
\]

Here `S` is the sum of the minimal Catalan weights `P_0(C)` over all connected structural triples
`ABC=rho`. Section 6 gives a self-contained derivation from the already reviewed tree--cotree
injection. This is a smaller repair than the false exact planar coefficient in
`WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md`: it keeps a polynomial prefactor
instead of forcing a pure `D^N` statement for every small `N`.

Input P is new proposer-side and requires independent review.

### Input E — equality components versus genus

For every admissible skeleton with `c in {1,2}` topological components and total genus `h`,

\[
 \kappa(\sigma,\tau)
 \le N-2c+q_N+2+2h-|\mathsf C|,
 \qquad q_N\in\{1,2\}.
\tag{E}
\]

The only consequences used in (4) are

\[
 \kappa\le N+2+2h\quad(c=1),
 \qquad
 \kappa\le N+2h\quad(c=2).
\tag{9}
\]

Input E is the author's own `CONJECTURED` proposer-side lemma and must not be treated as reviewed.

### Input D — two-component separation and residual count

For `c=2`:

1. every skeleton with total genus `h<=1` has at least one return boundary word; and
2. for the residual nonreturn sector, necessarily `h>=2` and

\[
 S^{(c=2)}_{N,h}\le4096^N N^{24h}.
\tag{D}
\]

Input D is also proposer-side. Its low-genus disk-return deletion and its two-unicellular-map
tree--cotree count both require independent review.

If only P and E are reviewed but D is not, the two-component `h>=2` nonreturn sector remains an
unclosed interface. Equality control by itself does not count those structural skeletons.

## 4. Exact centered trace expansion

Let

\[
 E_m=\{(v,a):v\ne a\},\qquad A_{v,a}=U_v^*U_a.
\]

Centering removes the `v=a` terms exactly:

\[
 S_U={1\over m^2}\sum_{e\in E_m}A_e\otimes A_e^*.
\tag{10}
\]

For every integer `N`, direct multiplication gives

\[
 \operatorname{Tr}(S_U^N)
 ={1\over m^{2N}}
 \sum_{\mathbf e\in E_m^N}
 \operatorname{Tr}W_U(\mathbf e)\,
 \overline{\operatorname{Tr}\check W_U(\mathbf e)},
\tag{11}
\]

where

\[
 W_U(\mathbf e)=A_{e_1}\cdots A_{e_N},
 \qquad
 \check W_U(\mathbf e)=A_{e_N}\cdots A_{e_1}.
\tag{12}
\]

Equation (11), not a modulus square, is the load-bearing signed expansion. The proof below takes
absolute values only after separating the safe return sequences and expanding each remaining Haar
expectation into exact contraction skeletons.

For one global row/column skeleton `(sigma,tau)`, let `kappa` be the number of tuple-label equality
components, let `c` be the number of topological constellation components, let `h` be total genus,
and let `g` be monotone-Weingarten excess. The exact constellation interface and Euler identity
give the absolute term scale

\[
 m^{-2N}\,m^\kappa\,P_g(\mathsf C)\,
 d^{,2c-2h-2-2g}.
\tag{13}
\]

There is no identification of `c` with `kappa`. The factor `m^kappa` counts compatible physical
slot labelings; the edge inequalities `v_i!=a_i` only reduce that number. The factor
`d^(2c-2h-2)` is topological, and `d^(-2g)` is monotone excess.

The `PROVED` tail theorem packages all allocations of excess among generator labels. With
`theta` from (3), the `g=0` minimal mass of every fixed skeleton receives a total multiplier at
most

\[
 1+\sum_{g\ge1}\theta^g={1\over1-\theta}.
\tag{14}
\]

No factorial or extra label-block convolution factor is added in (14).

## 5. First partition: returns before Weingarten expansion

Let `w(e)` and `check w(e)` be the forward and block-reversed free-group words. Partition the
sequence sum (11) into

\[
 \mathcal R=\{w=1\text{ or }\check w=1\},
 \qquad
 \mathcal N=\mathcal R^c.
\tag{15}
\]

The independently reviewed return estimate applies before any skeleton or genus expansion:

\[
 |M_{\rm ret}|
 \le2d^2\left({3m-4\over m^2}\right)^N.
\tag{16}
\]

It therefore covers return sequences with every possible `c,h,g` at once. The factor two is the
union bound for forward and reverse returns; an overlap only makes it loose. Return sequences are
removed before the remaining structural classification, so no claim that every two-component
diagram is a product term is needed.

The nonreturn sum `mathcal N` is expanded exactly into skeletons. Restricting to nonreturn labelings
can only decrease each all-label structural upper bound below.

## 6. The planar nonreturn sector is real, and the minimal repair

Connected planar nonreturn skeletons cannot be discarded by centering or by (16). A smallest
example has `N=2`, `sigma=tau=id`, and four distinct labels

\[
 (v_0,a_0,v_1,a_1)=(1,2,3,4).
\tag{17}
\]

Then `A=J,B=K,C=id`, the constellation is connected with genus zero, and `kappa=4=N+2`. The words

\[
 g_1^{-1}g_2g_3^{-1}g_4,
 \qquad
 g_3^{-1}g_4g_1^{-1}g_2
\tag{18}
\]

are both reduced and nontrivial. Thus a correct final assembly needs an actual planar bound.

The exact planar enumeration formula used in the earlier weighted-count artifact was independently
shown false. It is unnecessary here. The reviewed deterministic tree--cotree code has, for a
connected genus-`h` map with two faces and `e` ordinary edges, `2h+1` cotree edges and the ordinary
upper bound

\[
 R_{e,h}^{(2)}
 \le4^e(4e)^2(32e^2)^{2h+1}.
\tag{19}
\]

The encoder and decoder in (19) remain valid at `h=0`: there is exactly one cotree edge and its
deletion leaves a plane tree. Set `e=4N` and multiply by the already-`PROVED` per-skeleton Catalan
bound `P_0(C)<=2^e`. One obtains

\[
\begin{aligned}
 S^{(c=1)}_{N,0}
 &\le8^e(4e)^2(32e^2)\\
 &=4096^N\,512(4N)^4\\
 &=2^{17}N^4\,4096^N,
\end{aligned}
\tag{20}
\]

which is Input P.

The polynomial `2^17N^4` is harmless at logarithmic moment order and should not be charged to a
nonexistent first handle. For `N>=11` it may also be absorbed into `32768^N`, but no such pure
exponential repackaging is needed for (4).

The `PROVED` cyclic-reversal sequence count does not by itself replace (20). It controls the signed
`g=0` annular support, but the monotone theorem bounds `g>=1` skeletonwise relative to the
**absolute** minimal mass. Without an absolute planar estimate such as (20), a cancellation in the
leading annular coefficient does not control its positive excess tail. This is a real interface,
not merely a status-label issue.

## 7. Sector-by-sector absolute masses

Write `M_(c,h,g)` for the nonreturn absolute contribution after moment normalization
`m^(-2N)`. Under Inputs P, E, and D, the following bounds hold.

| sector | minimal `g=0` absolute mass | excess `g>=1` |
|---|---:|---:|
| returns, all `c,h` | bounded together by (16), before skeleton expansion | already included in (16) |
| `c=1,h=0`, nonreturn | `m^2 (4096/m)^N 2^17 N^4` | multiply minimal mass by at most `theta/(1-theta)` |
| `c=1,h>=1`, nonreturn | `m^2 (4096/m)^N (m^2 N^43/d^2)^h` | multiply minimal mass by at most `theta/(1-theta)` |
| `c=2,h<=1`, nonreturn | zero by Input D | zero, because the edge sequence was already placed in the return set |
| `c=2,h>=2`, nonreturn | `(4096/m)^N m^(2h) N^(24h) d^(2-2h)` | multiply minimal mass by at most `theta/(1-theta)` |

For example, the connected positive-genus row follows exactly from

\[
 m^{-2N}\,m^{N+2+2h}\,
 4096^NN^{43h}d^{-2h}
 =m^2\left({4096\over m}\right)^N
 \left({m^2N^{43}\over d^2}\right)^h.
\tag{21}
\]

The last row uses the correct disconnected Euler power:

\[
 m^{-2N}\,m^{N+2h}\,4096^NN^{24h}d^{2-2h}
 =\left({4096\over m}\right)^N
 m^{2h}N^{24h}d^{2-2h}.
\tag{22}
\]

In particular, the enhanced factors `d^2` at `c=2,h=0` and `d^0` at `c=2,h=1` never appear in
the nonreturn table: Input D places those edge sequences in (16). The first residual disconnected
nonreturn genus is `h=2`, with dimension suppression `d^(-2)`.

## 8. Summing `g` and `h`

Sum (21) over `h>=1`, sum (22) over `h>=2`, and apply (14). When the quantities in (3) are below
one,

\[
\begin{aligned}
 |M_{c=1,h\ge1}|
 &\le {m^2(4096/m)^N\over1-\theta}
       {x_{43}\over1-x_{43}},\\
 |M_{c=2,h\ge2}|
 &\le {m^2(4096/m)^N\over1-\theta}
       N^{24}{x_{24}\over1-x_{24}},\\
 |M_{c=1,h=0}|
 &\le {m^2(4096/m)^N\over1-\theta}
       2^{17}N^4.
\end{aligned}
\tag{23}
\]

Adding (16) proves the unnormalized moment bound underlying (4). This summation extends the finite
genus ranges to infinity only to enlarge a positive geometric sum.

## 9. Exact threshold constants and even moment choice

From (2),

\[
 (mH)^2
 =\left[18m(1+\eta)^2+81(1+\eta)^4\right](1-m^{-2}).
\tag{24}
\]

For `m>=2,eta>=0`, this is strictly greater than `18m`. Hence, in the project regime,

\[
 4096<32768<\sqrt{18m}<mH,
\tag{25}
\]

so `0<a<1`. Also `0<u<1` for `m>e^18`.

With `N(d)` from (6),

\[
 2d^2u^{N(d)}
 =\exp\left\{
 [2-\gamma\log(1/u)]\log d+O(1)
 \right\}\longrightarrow0
\tag{26}
\]

by (5). Meanwhile

\[
 a^{N(d)}N(d)^4\longrightarrow0,
 \qquad
 x_{43},x_{24},\theta\longrightarrow0.
\tag{27}
\]

There is no competing upper restriction on the fixed coefficient `gamma`: for every fixed
`gamma`, logarithmic `N(d)` makes all three ratios in (27) vanish. The phrase
`N<=c_m log d` in the monotone-tail statement is satisfied after taking any fixed
`c_m>gamma`.

Finally, because `N(d)` is even,

\[
 0\le\|S_U\|_\infty^{N(d)}
 \le\operatorname{Tr}(S_U^{N(d)}).
\tag{28}
\]

Equations (4), (26)--(28), and Markov yield the conditional probability conclusion (7) with the
**exact** Werner radius, not merely its `sqrt(18/m)` asymptotic.

## 10. Hidden-interface audit

### 10.1 Interfaces that are already closed

1. **Centering and normalization.** Equation (10) supplies exactly `m^(-2N)` and restricts to
   `v_i!=a_i`; no further diagonal subtraction is present.
2. **Reversal rather than a square.** Equation (11) retains the correct signed order. No
   modulus-square majorant is used.
3. **Dimension exponent.** The `PROVED` Euler node supplies `d^(2c-2h-2)` and the monotone
   expansion supplies `d^(-2g)`.
4. **Generator-label convolution.** The `PROVED` monotone theorem already sums allocations of
   excess among labels; no hidden factorial is inserted.
5. **Moment to operator norm.** Evenness of (6) makes (28) exact; the matrix dimension contributes
   only through the explicit `d^2` return bound.
6. **Target constant.** Inequality (25) gives strict room at `4096`; no asymptotic replacement of
   `H` is needed.

### 10.2 Interfaces still awaiting independent proof

1. **Input P:** extend the reviewed tree--cotree formula to its literal `h=0` specialization and
   approve (20). This is the smallest planar repair needed by the moment route.
2. **Input E:** independently review the admissibility/length proof of the equality bound. It is
   load-bearing in every nonreturn row.
3. **Input D:** independently review both the disk-return implication for `c=2,h<=1` and the
   residual two-unicellular-map count. Equality review alone does not imply D.

After P, E, and D pass at stable exact statements, equations (10)--(28) form a complete
independently reviewable conditional route. No additional probabilistic concentration theorem,
uniform second-order-freeness remainder, genus-lowering surgery, or unknown choice of
`N=Theta(log d)` remains.

The only additional work would be protocol assembly: register an atomic route whose implication
is (4), bind the exact premise hashes, and obtain an independent review of this final algebra.
That is evidence closure, not a new mathematical interface.

## 11. Minimal candidate atomic claims (not applied)

All candidate nodes below should remain at most `CONJECTURED` until independent review.

### `HEXT.werner-planar-two-boundary-polynomial-weighted-count`

> For every `N>=1`, the total minimal Catalan weight of connected planar triples `ABC=rho` is at
> most `2^17 N^4 4096^N`.

Suggested premises: `HEXT.werner-contraction-skeleton-ribbon-injection` and
`HEXT.werner-minimal-catalan-weight`. Its proof is (19)--(20), not the false refined planar-map
coefficient.

### `HEXT.werner-centered-moment-conditional-assembly`

> Assuming the planar weighted count above, the exact equality-component bound (E), and the
> two-component separation/count (D), every even `N` with the ratios in (3) below one satisfies
> the master moment inequality (4). Consequently the even choice (6) proves the centered
> high-probability Werner radius for fixed `m>e^18` and fixed `eta>=0`.

Suggested proved premises: the exact reversal trace/return result, exact ribbon injection and
Euler deficit, positive-genus weighted count, minimal Catalan weight, monotone tail, and exact
Werner spectral reduction. The route must list E and D as load-bearing candidate premises rather
than burying them in evidence prose.

## 12. Final status

This note identifies no hidden analytic obstruction after Inputs P, E, and D. It does not assert
that those inputs have passed review. In particular:

- the author's equality artifact remains only `CONJECTURED` input;
- the local planar and disconnected-sector claims need independent review;
- `HEXT.same-tuple-werner-centered-bound` remains unresolved; and
- the full-size extensive-violation theorem remains **OPEN**.
