# k-Sum L2 weighted-activation OR dual composition: exact row space and dense-slice obstruction

Date: 2026-07-22

Controlling node:
`KSUM.B4b.L2.ALT.weighted-activation-or-dual-composition`

Scope: the registered dense-composition support with exactly `L` positive complementary-pair
totals,

\[
 s_i\ge 2,\qquad \sum_{i=1}^L s_i=N,\qquad
 x_i=y_i(s_i-1),\qquad y_i\in\{0,1\},
\tag{1}
\]

followed by the unordered simultaneous-slot histogram quotient.  The optional upper bound
`s_i<=L+1` from the Phase-30 dense component is allowed but is not used.  This memo does not cover
the balanced positive-split component, whose target-count range can be `Theta(L^2)`.

Tier: exact proposer-tier analytic obstruction.  No numerical exponent inference and no
completion-tier DAG status are claimed.

## Decision

**Scoped kill of the registered dense-slice claim.**  Conditioning on `sum_i s_i=N` and passing
to unordered histograms do not create a loophole for a weighted-activation OR dual composition.
The complete actual weight-filtered row space has an exact injection-sum description given below.
In particular,

\[
 C:=\sum_{i=1}^L x_i
\tag{2}
\]

is a genuine global histogram statistic of actual weight two.  On (1),

\[
 C=0\quad\Longleftrightarrow\quad y=0,
 \qquad
 1\le C\le B:=N-L\quad\text{on every YES point}.
\tag{3}
\]

Let `D=floor(L/2)` and

\[
 n=\left\lfloor\frac{D-1}{2}\right\rfloor.
\tag{4}
\]

The single actual polynomial

\[
 Q_N(C)=
 \frac{T_n\!\left((B+1-2C)/(B-1)\right)}
      {T_n\!\left((B+1)/(B-1)\right)}
\tag{5}
\]

has actual weight `2n<D`, equals one on all NO points, and obeys

\[
 |Q_N(C)|\le
 \eta_N:=\operatorname{sech}\!\left(
 n\operatorname{arcosh}\frac{B+1}{B-1}
 \right)
 \le 2e^{-N^{1/6}/5}
\tag{6}
\]

on every YES point for all sufficiently large `N`, where
`L=floor(N^(2/3))`.

Consequently every signed histogram measure `W` with `||W||_1=1` that annihilates all actual rows
of weight `<D` satisfies

\[
 |\langle W,1-2\mathbf 1_{\rm NO}\rangle|
 \le 2\eta_N
 \le 4e^{-N^{1/6}/5}=o(1).
\tag{7}
\]

This rules out correlation strictly above `2/3`.  A fortiori it rules out the node's stronger
request for pure actual weight at least `(1/2+delta)L` for any fixed `delta>0`.  The conclusion is
formula-independent: it applies to ordinary OR duals, weighted inner/outer block compositions,
and arbitrary signed coefficient laws on the exact dense slice.

## 1. Ordered cover and the histogram quotient

Put

\[
 t_i=s_i-1\ge1,\qquad \sum_i t_i=B=N-L,
 \qquad x_i=y_it_i.
\tag{8}
\]

It is convenient to work first on the ordered cover of the support.  The symmetric group `S_L`
simultaneously permutes `(t_i,y_i)`.  Every actual query row is invariant under this action and
therefore descends to the unordered joint histogram.

Conversely, a signed measure `W` on histograms has a canonical symmetric lift to the ordered
cover: divide the coefficient of an orbit equally among its ordered representatives.  The lift
has the same total mass and `l1` norm, and its pairing with every invariant row is exactly the
histogram pairing.  Thus neither annihilation nor correlation changes under the quotient.  It is
therefore enough, and exact, to characterize invariant rows on the ordered cover.

## 2. Exact filtered injection-sum row space

Give `s_i` actual weight one and `x_i` actual weight two.  For a list

\[
 \tau=((a_1,b_1),\ldots,(a_r,b_r)),
 \qquad a_j,b_j\ge0,
\tag{9}
\]

with no `(0,0)` entry, define the ordered injection orbit sum

\[
 I_\tau(s,x)=
 \sum_{\iota:[r]\hookrightarrow[L]}
 \prod_{j=1}^r s_{\iota(j)}^{a_j}x_{\iota(j)}^{b_j}.
\tag{10}
\]

Its weight is

\[
 w(\tau)=\sum_j(a_j+2b_j).
\tag{11}
\]

### Lemma 1 (injection basis)

The invariant actual row space of weight `<D`, before or after restriction to (1), is the span of
the restrictions of all `I_tau` with `w(tau)<D`.

**Proof.**  Products of polarized power sums

\[
 p_{(a,b)}=\sum_i s_i^a x_i^b
\tag{12}
\]

expand by the collision partition of their selected indices.  For a list `tau`,

\[
 \prod_{j=1}^r p_{(a_j,b_j)}
 =\sum_{\pi\in\Pi_r} I_{\operatorname{merge}_\pi(\tau)},
\tag{13}
\]

where exponents are added inside every block of the set partition `pi`.  Moebius inversion on the
partition lattice expresses every `I_tau` as a linear combination of such products.  Merging
preserves (11), so this is an equality of filtered spaces, not merely an unfiltered spanning
claim.  The multisymmetric orbit sums span the simultaneous-permutation invariants.  Restricting
to a support or quotienting by its relations takes the image of this same span.  `square`

Substitute (8) into (10).  A local factor becomes

\[
 s^a x^b=
 \begin{cases}
 (t+1)^a,&b=0,\\
 y(t+1)^a t^b,&b>0,
 \end{cases}
\tag{14}
\]

because `y^b=y` for `b>0`.  Define the monomial injection sums

\[
 J_\gamma(t,y)=
 \sum_{\iota:[r]\hookrightarrow[L]}
 \prod_{j=1}^r t_{\iota(j)}^{c_j}y_{\iota(j)}^{\epsilon_j},
\tag{15}
\]

where `epsilon_j in {0,1}`, `c_j>=1`, and assign the filtered cost

\[
 \kappa(c_j,\epsilon_j)=c_j+\epsilon_j.
\tag{16}
\]

We use the convention `J_empty=1`.  A formal unmarked `(c,epsilon)=(0,0)` slot is omitted:
summing its unused injection index only multiplies a shorter injection sum by the appropriate
falling-factorial scalar.  Thus requiring `c_j>=1` loses no row.

### Lemma 2 (marked-composition form)

On (1), the complete actual row space of weight `<D` is exactly the image of

\[
 \operatorname{span}\left\{
 J_\gamma:\ \sum_j(c_j+\epsilon_j)<D
 \right\}
\tag{17}
\]

under the composition relation `sum_i t_i=B`.  Here `epsilon=1` marks an active slot.  In
particular every marked slot costs at least two, and its coefficient contains at least one power
of its positive weight `t_i`.

**Proof.**  Expanding (14), an unmarked term `t^c` has `c<=a` and hence cost `c<=a`.  A marked
term `yt^c` has `b<=c<=a+b`, and therefore

\[
 c+1\le a+b+1\le a+2b.
\tag{18}
\]

This proves containment of every actual row in (17), without increasing filtered weight.
Conversely, `t^c` is obtained triangularly from `(t+1)^c`, while `yt^c` is obtained triangularly
from

\[
 yt(t+1)^{c-1}=s^{c-1}x
\tag{19}
\]

and the lower powers `yt,\ldots,yt^{c-1}`.  Their respective actual costs are `c` and `c+1`.
Tensoring this triangular change of local basis inside injection sums proves the reverse
containment.  Restriction to the exact composition slice takes the image of the equality.
`square`

For clarity, the fundamental composition relation in this injection notation is exact.  If
`gamma` has `r` existing slots, then

\[
 J_{\gamma\cup(1,0)}
 =B J_\gamma-
 \sum_{j=1}^r J_{\gamma:\,c_j\mapsto c_j+1}.
\tag{20}
\]

Indeed, after fixing the existing injection, the sum of `t_i` over unused indices is `B` minus
the selected `t_i`.  Equation (20) shows precisely what conditioning does: it removes a new
unmarked linear factor.  It does not invalidate the filtered description (17).  Any further
finite-support dependencies can only identify elements of this image; they cannot remove the
specific legal row (5).

## 3. What an ordinary outer OR dual does to the full mixed space

The row characterization gives an exact answer for the simplest proposed architecture.  Let
`mu(t)` be any symmetric positive probability law on the exact composition slice and let
`psi(y)` be a symmetric signed Boolean measure.  Consider the factorized ordered law

\[
 \widetilde W(t,y)=\mu(t)\psi(y).
\tag{21}
\]

If `psi` has zero moments against every Boolean monomial of degree at most `k`, then (21)
annihilates every actual mixed row with at most `k` marked slots, including rows with arbitrary
allowed unmarked `t` payloads.  This follows term by term in (15): the `t` and `y` expectations
factor, and the marked `y` moment vanishes.  Since each marked slot costs at least two, Boolean
pure degree `k+1` is sufficient to annihilate the complete actual row space below weight
`2(k+1)`.

This also gives necessity inside the factorized class.  For `r` marked slots of minimal cost,

\[
 J_r=\sum_{\iota:[r]\hookrightarrow[L]}
 \prod_{j=1}^r y_{\iota(j)}t_{\iota(j)},
\tag{22}
\]

and symmetry gives

\[
 \langle\widetilde W,J_r\rangle
 =(L)_r\,\mathbb E_\mu[t_1\cdots t_r]\,
 \mathbb E_\psi[y_1\cdots y_r].
\tag{23}
\]

The middle factor is strictly positive.  Hence full actual purity through weight `2r` forces the
corresponding Boolean moment to vanish.

Thus an ordinary outer OR dual does genuinely annihilate the full mixed row space; it does not
fail merely because `s`-payload rows were forgotten.  Its problem is quantitative.  Purity above
`L/2` forces Boolean purity above `L/4`, while the anchored Chebyshev polynomial in
`H=sum_i y_i` bounds its zero-test correlation by

\[
 2\operatorname{sech}\!\left(
 \left\lfloor\frac{L}{4}\right\rfloor
 \operatorname{arcosh}\frac{L+1}{L-1}
 \right)
 =e^{-\Omega(\sqrt L)}.
\tag{24}
\]

A standard OR dual of only `Theta(sqrt(L))` Boolean pure degree can retain constant correlation,
but (17) then supplies only `Theta(sqrt(L))` actual weight, not a linear fraction of `L`.

Weighted inner blocks were intended to multiply these two scales.  The next section shows that no
such composition can evade the actual scalar row (5) on the legal dense slice.

## 4. Universal scalar obstruction on the dense composition slice

On (8),

\[
 C=\sum_i y_it_i.
\tag{25}
\]

All `t_i` are positive integers.  Therefore `C=0` exactly at the zero activation, and every YES
point has integer `C>=1`.  Also

\[
 C\le\sum_i t_i=B=N-L.
\tag{26}
\]

The affine map

\[
 z(C)=\frac{B+1-2C}{B-1}
\tag{27}
\]

sends `[1,B]` to `[1,-1]`, while

\[
 z(0)=\frac{B+1}{B-1}>1.
\tag{28}
\]

Consequently (5) has `Q_N(0)=1` and, since `|T_n(z)|<=1` for `z in [-1,1]`, satisfies the first
bound in (6).  It is a polynomial of degree `n` in `C=p_(0,1)`, so its actual weight is at most
`2n<D`, including the strict cutoff and all floors.

The Chebyshev exponent has the exact form

\[
 \operatorname{arcosh}\frac{B+1}{B-1}
 =2\operatorname{artanh}\frac1{\sqrt B}
 \ge\frac2{\sqrt B}.
\tag{29}
\]

For all sufficiently large `L`, (4) gives `n>=L/5`.  Since `B<=N` and
`L=floor(N^(2/3))>=N^(2/3)/2` for all sufficiently large `N`,

\[
 n\operatorname{arcosh}\frac{B+1}{B-1}
 \ge \frac{2L}{5\sqrt N}
 \ge \frac15N^{1/6}.
\tag{30}
\]

Using `sech(u)<=2e^{-u}` proves the second bound in (6).

Now let `W` be any signed measure on the histogram support with

\[
 \|W\|_1=1,
 \qquad
 \langle W,F\rangle=0
 \quad\text{for every actual row of weight }<D.
\tag{31}
\]

Constants are included in (31), so `sum W=0`.  Since `Q_N` is also included,

\[
 0=\langle W,Q_N\rangle
 =W({\rm NO})+\sum_{H\in{\rm YES}}W(H)Q_N(C(H)).
\tag{32}
\]

Equations (6) and (32) imply

\[
 |W({\rm NO})|
 \le \eta_N\sum_{H\in{\rm YES}}|W(H)|
 \le\eta_N.
\tag{33}
\]

For either sign convention of the zero-test label, zero mass gives

\[
 |\langle W,1-2\mathbf1_{\rm NO}\rangle|
 =2|W({\rm NO})|.
\tag{34}
\]

Combining (33)-(34) proves (7).

## 5. Consequence for dual block composition

The obstruction does not depend on how a candidate is assembled.  Suppose a discrete inner/outer
composition claims all of the following on (1):

1. it descends to legal unordered histograms;
2. its coefficient `l1` norm is finite and can be normalized to one;
3. its pure actual weight is at least `(1/2+delta)L` for fixed `delta>0`; and
4. its zero-test correlation is bounded below by a positive constant.

For large `L`, item 3 forces annihilation of (5), whose weight is `<L/2`.  Items 1-2 then place the
candidate under (32)-(34), and its correlation is `o(1)`, contradicting item 4.  Therefore at
least one claimed composition property must fail.  Exact conditioning cannot rescue it: (26),
which is caused by that conditioning, is the reason the separator is inexpensive.

This also pinpoints the distinction from the Phase-30 balanced component.  There a positive split
can have `x_i=Theta(s_i^2)`, and the complete support reaches `C=Theta(L^2)`.  With degree only
`Theta(L)`, the same anchored separator from the first positive scalar level does not have a
vanishing error.  The present theorem deliberately makes no claim about that different support.

## 6. Gate ledger

| obligation | result |
|:---|:---|
| exact full mixed row space after `x_i=y_i(s_i-1)` | **PASS**, Lemmas 1-2 |
| exact composition relation | **PASS**, (20) |
| unordered histogram quotient | **PASS**, symmetric lift preserves all pairings and `l1` |
| ordinary factorized OR dual annihilates mixed payload rows | **PASS**, if its Boolean moments vanish |
| ordinary OR dual attains linear actual purity with constant correlation | **FAIL**, (24) |
| weighted/block-composed dual attains purity `>L/2` and correlation `>2/3` | **FAIL on the entire dense slice**, (5)-(7) |
| exact strict actual weight cutoff | **PASS**, `weight(Q_N)=2n<D` |
| formula dependence or LP-selected coefficients | **IRRELEVANT** to the obstruction |
| balanced positive-split support | **OUT OF SCOPE** |
| every possible near-zero law | **NOT CLAIMED** |

## 7. Scoped conclusion

The smallest exact reduction is enough to decide the registered dense-composition architecture.
After conditioning and histogram quotient, marked mixed rows are precisely weighted activation
injection sums, with one extra unit of actual cost per active mark.  A factorized Boolean OR dual
therefore handles the complete mixed span, but linear actual purity forces linear Boolean purity
and destroys correlation.

Allowing `s`-dependent inner duals does not repair the tradeoff.  The exact composition identity
`sum_i(s_i-1)=N-L` makes the global target count lie in `[1,N-L]` on YES.  A legal actual
Chebyshev row below the `L/2` cutoff then approximates the zero-test uniformly with error
`exp(-Omega(N^(1/6)))`.  Duality in the elementary form (32) forces the same upper bound on every
normalized signed witness's correlation.

Thus the node's dense-slice claim has an analytic proposer-tier obstruction and should receive a
fresh Rule-7 review before any completion-tier DAG adjudication.  No successor architecture is
proposed in this memo.
