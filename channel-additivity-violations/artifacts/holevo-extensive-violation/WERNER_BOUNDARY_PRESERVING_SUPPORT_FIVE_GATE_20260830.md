# Werner boundary-preserving surgery: an exact support-five threshold example

Date: 2026-08-30

Status: proposer-side Question 3 artifact. No canonical YAML is changed. This note gives the
unique local normal form for surgeries that keep both rooted physical trace permutations fixed,
proves that one actual admissible genus-one Werner skeleton admits no such genus-lowering surgery
on four or fewer darts, and gives an explicit connected support-five surgery to genus zero. Thus
support three and support four are rigorously insufficient in general, while support five is
proved only for this skeleton. The universal bounded-support lemma and the full-size extensive
violation remain **OPEN**.

No web access, external theorem search, or large numerical process is used. The finite obstruction
below is reduced to a displayed table of permutations on four letters.

## 1. Outcome

Let `A B C=rho` be the exact two-boundary constellation from
`WERNER_PERMUTATION_CONSTELLATION_SURGERY_GATE_20260830.md`. Every second triple
`A' B' C'=rho` has the unique form

\[
 A'=A p,\qquad B'=p^{-1}Bq,\qquad C'=q^{-1}C.                 \tag{1}
\]

Consequently the natural dart support of a boundary-preserving surgery is

\[
 S(p,q)=\operatorname{supp}(p)\cup\operatorname{supp}(q).   \tag{2}
\]

If `s=|S(p,q)|`, the recovered row pairing changes on exactly `|supp(p)|` arrows and
the recovered column pairing changes on exactly `|supp(qp^{-1})|` arrows. In particular at most
`2s` tuple-label equality arrows change, and the label-assignment loss is at most `m^(2s)`.

There is an actual `N=4` admissible contraction skeleton, written explicitly in Section 4, with

\[
 \#A+\#B+\#C=14=2(8)-2,                                    \tag{3}
\]

so it is connected of genus one. For this skeleton, every pair `p,q` with
`|S(p,q)|<=4` satisfies

\[
 \#(Ap)+\#(p^{-1}Bq)+\#(q^{-1}C)
 \le \#A+\#B+\#C.                                          \tag{4}
\]

Thus no support-three or support-four boundary-preserving surgery can lower its genus; in fact
such a move cannot increase the Euler cycle sum at all, even if connectedness is discarded.

The lower bound is sharp for this skeleton. With

\[
 p=(0\ 5)(1\ 6),\qquad q=(4\ 6),                            \tag{5}
\]

the support union is `{0,1,4,5,6}`, the new triple remains connected, its cycle sum increases by
two, and its genus is zero. Exactly four row-pairing arrows and five column-pairing arrows change,
so the exact tuple-label loss is at most `m^9`.

This proves a minimum support of five for one physical skeleton. It does **not** prove that every
positive-genus skeleton admits a support-five surgery. The remaining universal gate is therefore
strictly narrowed from `support>=3` to `support>=5`.

## 2. Exact normal form for every boundary-preserving move

Let `X` be the `E=2N` physical dart set. Fix a triple `(A,B,C)` with

\[
 ABC=\rho,                                                   \tag{6}
\]

where the two rooted cycles of `rho` are the forward and reversal trace boundaries. Suppose a
second triple `(A',B',C')` has the same rooted boundary permutation:

\[
 A'B'C'=\rho.                                                \tag{7}
\]

Define

\[
 p=A^{-1}A',\qquad q=(AB)^{-1}A'B'.                          \tag{8}
\]

Then `A'=Ap` and `A'B'=ABq`, whence `B'=p^(-1)Bq`. Comparing (6)--(7) gives
`C'=q^(-1)C`. This proves (1). Conversely every choice of `p,q` in (1) fixes `rho` identically.
The definitions (8) also prove uniqueness.

Thus (1) is not a special ansatz: it is the lossless breakpoint-coordinate description of every
move that preserves both rooted physical boundary cycles pointwise. It is useful to view the
factorization as the three-segment path

\[
 1\longrightarrow A\longrightarrow AB\longrightarrow\rho
\]

in the transposition Cayley graph. The local permutations `p,q` move the two breakpoints to
`Ap,ABq` while leaving both endpoints fixed.

### 2.1 Genus and connectedness

Write

\[
 \Delta(p,q)=
 [\#(Ap)-\#A]+[\#(p^{-1}Bq)-\#B]+[\#(q^{-1}C)-\#C].         \tag{9}
\]

For a connected constellation, the exact Euler identity is

\[
 \#A+\#B+\#C=2E-2h.                                         \tag{10}
\]

Therefore a move (1) which remains connected lowers genus by exactly one if and only if
`Delta(p,q)=2`. The connectedness clause cannot be omitted: if the number of components rises
from one to two, an Euler increase of two may be absorbed by the component count without reducing
genus.

The obstruction in Section 5 is stronger than needed: it proves `Delta(p,q)<=0`, before any
connectedness test.

## 3. Exact pairing-arrow and label losses

Let `J` be the fixed physical row matching. The exact inverse constellation formulas are

\[
 \sigma=A^{-1}J,\qquad \tau=C^{-1}A^{-1}J=C^{-1}\sigma.      \tag{11}
\]

For (1),

\[
 \sigma'=p^{-1}\sigma,
 \qquad
 \tau'=C^{-1}q p^{-1}\sigma
       =C^{-1}q p^{-1}C\,\tau.                              \tag{12}
\]

Left multiplication by a permutation `r` changes exactly those arrows whose old image belongs to
`supp(r)`. Hence

\[
 \#\{x:\sigma'(x)\ne\sigma(x)\}=|\operatorname{supp}(p)|,
\]

and, because conjugation preserves support size,

\[
 \#\{x:\tau'(x)\ne\tau(x)\}=|\operatorname{supp}(qp^{-1})|.
                                                                  \tag{13}
\]

Both support sets in (13) lie in `S(p,q)`, so the total number of changed pairing arrows is at
most `2s`.

Recall that the tuple-label equality graph has the undirected edges

\[
 \{x,\sigma(x)\},\qquad \{x,\tau(x)\}.                       \tag{14}
\]

Replacing `L` such arrows can increase the number of equality components by at most `L`: delete
the `L` old edges first and then add the new ones. Thus a structural surgery with support `s` costs
at most

\[
 m^{L},\qquad L\le 2s,                                       \tag{15}
\]

in the label-assignment bound. The intermediate triple need not itself respect the original
coloring; (15) is precisely the defect accounting required when it does not.

## 4. An actual admissible genus-one skeleton

Set `N=4`, `E=8`, and identify

\[
 V_i=i,\qquad A_i=4+i\qquad(0\le i<4).                       \tag{16}
\]

Take the physical two-label coloring

\[
 \lambda(V_i)=1,\qquad \lambda(A_i)=2.                       \tag{17}
\]

The required inequality `lambda(V_i)!=lambda(A_i)` holds. Choose the row and column Haar
pairings

\[
 \sigma=(0\ 3\ 2\ 1)(4\ 5\ 6\ 7),
 \qquad
 \tau=(0\ 3\ 2\ 1)(4\ 7\ 6\ 5).                           \tag{18}
\]

Both preserve the coloring (17), so this is an actual nonzero balanced Werner contraction, not an
abstract uncolored constellation.

Using `A=J sigma^(-1)`, `B=sigma K tau sigma^(-1)`, and `C=sigma tau^(-1)` gives

\[
\begin{aligned}
 A&=(0\ 5)(1\ 6)(2\ 7)(3\ 4),\\
 B&=(0\ 4)(1\ 5)(2\ 6)(3\ 7),\\
 C&=(4\ 6)(5\ 7),
\end{aligned}                                                 \tag{19}
\]

with omitted points fixed. Direct multiplication gives

\[
 ABC=(0\ 3\ 2\ 1)(4\ 7\ 6\ 5)=\rho.                       \tag{20}
\]

The group generated by `A,B` is already transitive: alternating the two matchings produces the
eight-cycle

\[
 0\mathrel{-_B}4\mathrel{-_A}3\mathrel{-_B}7
 \mathrel{-_A}2\mathrel{-_B}6\mathrel{-_A}1
 \mathrel{-_B}5\mathrel{-_A}0.                               \tag{21}
\]

Finally,

\[
 \#A=4,\qquad\#B=4,\qquad\#C=6.                              \tag{22}
\]

Equations (10) and (22) show that the connected genus is exactly one.

## 5. Exact obstruction for every support of size at most four

The proof of (4) uses a finite first-return reduction, so no permutations on more than four
letters need to be enumerated.

### Lemma 1: first-return cycle formula

Let `P` be a permutation of a finite set `X`, let `S` be nonempty, and let `r_(P,S)` be the
first-return permutation on `S`: `r_(P,S)(x)` is the first point of `S` met after iterating `P`
from `x`. If `u` is supported in `S`, then

\[
 \#(Pu)-\#P=\#(r_{P,S}u)-\#r_{P,S}.                          \tag{23}
\]

Indeed, cycles of `P` disjoint from `S` are unchanged. Every remaining `P`-cycle is cut into
directed segments between successive visits to `S`; multiplication by `u` reconnects those
segments according to `r_(P,S)u`. The cycles of the reconnected segments are therefore exactly
the cycles of `r_(P,S)u`.

Since `XY` and `YX` are conjugate, `#(XY)=#(YX)`. Applying (23) three times to (9) gives, whenever
`p,q` are supported in `S`,

\[
\begin{aligned}
 \Delta(p,q)
 ={}&[\#(r_{A,S}p)-\#r_{A,S}]\\
 &+[\#(r_{B,S}q p^{-1})-\#r_{B,S}]\\
 &+[\#(r_{C,S}q^{-1})-\#r_{C,S}].                            \tag{24}
\end{aligned}
\]

Thus for `|S|=4`, (24) is an exact calculation entirely inside `S_4`.

### Lemma 2: the four-dart cycle sum never increases

For the triple (19), if `p,q` are supported on a common set of at most four darts, then
`Delta(p,q)<=0`.

**Proof.** Enlarge the common support to a four-set `S` if necessary. The simultaneous rotation

\[
 g=(0\ 1\ 2\ 3)(4\ 5\ 6\ 7)                                 \tag{25}
\]

commutes with each of `A,B,C`. Its action has the following twenty orbits on the seventy
four-subsets. For every representative `S`, the table gives the exact number of the `24^2=576`
ordered pairs `(p,q) in Sym(S)^2` producing each value of (24). A blank entry is zero.

| `S` | orbit size | `Delta=0` | `-2` | `-4` | `-6` | `-8` |
|---|---:|---:|---:|---:|---:|---:|
| `0123` | 1 | 1 | 18 | 123 | 344 | 90 |
| `0124` | 4 | 3 | 50 | 267 | 240 | 16 |
| `0125` | 4 | 12 | 147 | 318 | 99 |  |
| `0126` | 4 | 12 | 147 | 318 | 99 |  |
| `0127` | 4 | 3 | 50 | 267 | 240 | 16 |
| `0145` | 4 | 55 | 270 | 231 | 20 |  |
| `0146` | 4 | 55 | 270 | 231 | 20 |  |
| `0147` | 4 | 3 | 50 | 267 | 240 | 16 |
| `0156` | 4 | 55 | 270 | 231 | 20 |  |
| `0157` | 4 | 55 | 270 | 231 | 20 |  |
| `0167` | 4 | 3 | 50 | 267 | 240 | 16 |
| `0245` | 4 | 12 | 147 | 318 | 99 |  |
| `0246` | 2 | 55 | 270 | 231 | 20 |  |
| `0247` | 4 | 9 | 156 | 309 | 102 |  |
| `0257` | 2 | 55 | 270 | 231 | 20 |  |
| `0456` | 4 | 55 | 270 | 231 | 20 |  |
| `0457` | 4 | 55 | 270 | 231 | 20 |  |
| `0467` | 4 | 12 | 147 | 318 | 99 |  |
| `0567` | 4 | 12 | 147 | 318 | 99 |  |
| `4567` | 1 | 9 | 156 | 309 | 102 |  |

The orbit sizes sum to `70`, and every row count sums to `576`. For audit, the table is obtained
directly from (24). For example, for `S=0123` all three first-return permutations are the identity;
for `S=0145` they are respectively `(0 5)`, `(0 4)(1 5)`, and the identity; and for `S=0246`
they are respectively the identity, `(0 4)(2 6)`, and `(4 6)`. Substitution in (24) over the
twenty-four permutations of each displayed four-set gives the recorded rows. The remaining
rows are the same elementary four-letter multiplication.

No row contains a positive value. This proves the lemma. `square`

By (10), a connected one-handle reduction requires `Delta=2`. Lemma 2 rules this out even without
requiring the output to be connected. Since the starting triple comes from the admissible
pairings (18), it is a physical counterexample to every proposed universal one-step theorem with
support at most four.

## 6. A connected support-five reduction of the same skeleton

Now take (5):

\[
 p=(0\ 5)(1\ 6),\qquad q=(4\ 6),
 \qquad S(p,q)=\{0,1,4,5,6\}.                                \tag{26}
\]

Equation (1) gives

\[
\begin{aligned}
 A'&=(2\ 7)(3\ 4),\\
 B'&=(0\ 4\ 2\ 1)(3\ 7)(5\ 6),\\
 C'&=(5\ 7),
\end{aligned}                                                 \tag{27}
\]

again with omitted points fixed. Hence

\[
 (\#A'-\#A,\#B'-\#B,\#C'-\#C)=(2,-1,1),                    \tag{28}
\]

and `Delta(p,q)=2`.

The new triple is transitive. The `B'` cycle `(0 4 2 1)` reaches `0,1,2,4`; `A'` reaches `3,7`
from `2,4`; `C'` reaches `5` from `7`; and the `B'` pair `(5 6)` reaches `6`. Thus all eight
darts lie in one orbit. Equations (10) and (28) prove that its genus is zero, while (1) proves
`A'B'C'=rho` exactly. Both rooted physical boundaries are therefore preserved pointwise.

The pairing cost is also exact. Here

\[
 |\operatorname{supp}(p)|=4,
 \qquad qp^{-1}=(0\ 5)(1\ 4\ 6),
 \qquad |\operatorname{supp}(qp^{-1})|=5.                    \tag{29}
\]

Therefore (13)--(15) give exactly nine changed pairing arrows and label loss at most

\[
 m^9.                                                         \tag{30}
\]

The leading Möbius/Catalan coefficient has no loss in this example: `C=(4 6)(5 7)` and
`C'=(5 7)` both have coefficient magnitude one.

Combining Lemma 2 with (26)--(30), the minimum boundary-preserving surgery support for this
particular physical genus-one skeleton is exactly five.

## 7. Quantitative interface if support five were universal

The preceding example does not establish universality, but it fixes all dimension and label costs
of the next possible theorem.

For `E=2N`, the number of ordered local pairs `(p,q)` with support union at most five is bounded by

\[
 \sum_{j=0}^{5}\binom Ej(j!)^2
 \le E^5\sum_{j=0}^{5}j!
 =154E^5.                                                      \tag{31}
\]

A universal support-five surgery would therefore cost at most `m^10` in labels and
`154E^5` in reverse histories per handle.

Unlike the earlier `A--B` transposition subclass, a general move may change `C` and hence its
leading unitary-Weingarten Möbius coefficient

\[
 P_0(C)=\prod_{\gamma\in\operatorname{Cyc}(C)}
          \operatorname{Cat}_{|\gamma|-1}.                   \tag{32}
\]

This is still only a polynomial per local handle. The elementary bounds

\[
 \frac{4^r}{2(r+1)^2}\le\operatorname{Cat}_r\le4^r           \tag{33}
\]

show that joining or splitting two cycles of total length at most `E` by one transposition changes
`P_0` by a ratio of at most `16E^4` in either direction. A permutation on five darts has
transposition length at most four, so

\[
 \max\left\{\frac{P_0(q^{-1}C)}{P_0(C)},
             \frac{P_0(C)}{P_0(q^{-1}C)}\right\}
 \le (16E^4)^4=2^{16}E^{16}.                                 \tag{34}
\]

Consequently a universal connected support-five reduction, together with a controlled planar
endpoint, would have the conservative per-handle factor

\[
 \frac{154\,2^{16}\,m^{10}E^{21}}{d^2}.                     \tag{35}
\]

For every fixed `m` this is `o_m(1)` uniformly when `E=2N<=2c_m log d`. Thus support five is fully
compatible with the desired logarithmic growing-moment regime; the obstacle is existence, not
dimension or label entropy. The already separated monotone-Weingarten excess tail would still
need to be included in the final assembly.

More generally, any universal fixed support `s` gives at most `2s` changed equality arrows and a
polynomial-in-`N` structural and Catalan cost. The finite-d `d^(-2)` Euler gain per handle absorbs
all such fixed-support losses at `N=O_m(log d)`.

## 8. Exact remaining OPEN gate

The strongest unproved statement justified by the present analysis is:

> **Support-at-least-five physical-boundary surgery (OPEN).** There exist universal constants
> `s>=5` and `a` such that every connected positive-genus constellation arising from an admissible
> Werner contraction can be taken to a connected constellation of genus one less by at most `a`
> moves of the normal form (1), each with `|S(p,q)|<=s`. The total number of changed recovered
> pairing arrows per handle is bounded by a universal constant.

If every individual move lowers genus, one may take `a=1`. Allowing a bounded number of neutral
preparatory moves could be useful, but their cycle, connectedness, arrow-defect, and Catalan costs
must all be counted. An ordinary topological trisection does not prove this statement because it
need not fix `rho` pointwise or lift to bounded changes in (12).

The `N=4` skeleton (18)--(22) proves that any theorem with `s<=4` is false. The explicit move
(26) proves only that `s=5` is attainable on this minimum obstruction. No family requiring support
growing with `N` is known here, and no universal support-five construction is claimed.

## 9. Quantifiers, scope, and failure boundaries

- Equations (1), (8), and (12)--(15) are finite identities for every `N,d` and every pair of
  constellation triples with the same rooted `rho`.
- Lemma 2 concerns the single actual admissible `N=4` skeleton (18). It quantifies over every
  `p,q` whose union support has size at most four; it does not sample moves.
- The table in Section 5 is a complete finite classification modulo the exact order-four
  automorphism (25). It proves absence of any positive cycle-sum move, so no hidden connectedness
  assumption is used in the obstruction.
- Section 6 proves a one-handle support-five reduction only for the displayed skeleton.
- Equations (31)--(35) are conditional cost accounting for a hypothetical universal support-five
  theorem. They do not establish that theorem or the planar endpoint count.
- No full minimal-skeleton mass bound, high-probability norm bound, or counterexample to the Werner
  centered target is proved.
- The already established absolute-unbounded extensive violation is separate. The full-size
  extensive Question 3 and `HEXT.same-tuple-werner-centered-bound` remain OPEN.

## 10. Candidate atomic DAG updates (not applied)

No canonical YAML is edited. Suggested proposer-side claims, all requiring independent audit before
any promotion, are:

1. `HEXT.werner-boundary-surgery-normal-form`
   - claim: equations (1), (8), and (12)--(15) uniquely parameterize every fixed-`rho` surgery and
     give exact pairing-arrow and label-defect costs;
   - candidate verdict: `CONJECTURED` pending review of the finite permutation derivation.
2. `HEXT.werner-support-four-surgery-obstruction`
   - claim: the physical `N=4` skeleton (18)--(22) admits no genus-lowering fixed-`rho` surgery on
     at most four darts;
   - candidate verdict: `CONJECTURED` pending independent audit of Lemmas 1--2 and the twenty-row
     `S_4` table. This refutes only universal `s<=4` routes, not the main bounded-support claim.
3. `HEXT.werner-support-five-genus-one-base-case`
   - claim: equations (26)--(30) give a connected support-five reduction of that skeleton with
     exactly nine pairing-arrow changes and at most `m^9` label loss;
   - candidate verdict: `CONJECTURED` pending independent audit.
4. `HEXT.werner-boundary-preserving-genus-reduction`
   - keep `OPEN`; replace the live support range `support>=3` by `support>=5`, and link this artifact
     as proposer-side evidence only.
5. `HEXT.same-tuple-werner-centered-bound`
   - keep `OPEN`; the universal surgery or a sharp weighted-constellation count is still missing.
