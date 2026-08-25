# L3 critical endpoint: sparse delocalized multiblock selector-star audit

Date: 2026-07-22  
Canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.ALT.delocalized-multiblock-occurrence-kernel`  
Verdict: **FAIL for the hidden-selector-star / independently slot-symmetric family typed below;
PARTIAL for the registered node; proposer-tier only**

## 1. Verdict

The smallest explicit sparse-delocalization law can be made invariant and can be inserted into the
exact `C/uC` presentation incidence.  It does not produce the hoped-for `sqrt(r)` load-sharing
gain.

The attempted law adds a hidden `r`-block chart and a branch `h in [r]`.  In branch `h`, the sharp
one-block pSearch operator

\[
 A={J_m-I_m\over m-1}=P-{1\over m-1}Q
\tag{1.1}
\]

is placed on block `h`; the other selected blocks carry a common passive
`B=xP+yQ`.  The selector-star map sends all orthogonal column branches to one uniform row branch.
Before the hidden selector is forgotten, its norm can be `Theta(sqrt(r))`.

Exact incidence compression is decisive.  Because neither the physical input nor the outer UIC
data retains the hidden branch, the normalized incidence maps contract both selector sides with
the uniform vector.  The occurrence operator that survives is

\[
 K_{r,B}={1\over\sqrt r}\sum_{h=1}^r
 A_h\bigotimes_{k\ne h}B_k .
\tag{1.2}
\]

This lies in the complete independently slot-symmetric `P/Q` algebra.  If a physical outer
transition has even one unequal block `j`, then every slot query in `j` contains, as an exact
orthogonal companion-sector block, the sharp one-block mask of a norm-active coefficient pair.
Consequently

\[
 {\|K_{r,B}\|\over
   \max_v\|K_{r,B}\circ\Delta_{j,v}\|}
 \le \sqrt{m-1},
\tag{1.3}
\]

independently of `r`, of `x,y`, and of signs.  In particular, passive `P` does reduce each
individual unequal mask to scale `1/sqrt(m)`, but all `r` branch contributions retain the same
all-`P` direction and add coherently.  The numerator and the changed-coordinate mask both acquire
the same `sqrt(r)` factor.

For passive `I`, the failure is even sharper.  The unit-norm passive term satisfies
`I circ D_v^ne = |v><v|`; the `r-1` allegedly passive branches add coherently in the one genuinely
changed block.  The exact local masked norm is asymptotic to `sqrt(r)`, so the ratio is bounded by
a constant rather than by `sqrt(mr)`.

Full `S_a` invariance does not repair the problem.  Uniformly averaging an `r`-chart over all
injections `[r] -> [a]` merely produces an `S_a`-invariant element of the `2^a`-sector `P/Q`
algebra, and the same one-coordinate cut proves (1.3).  Retaining the chart label so that its
branches remain orthogonal would require a growing outer selector.  That is the separately
registered growing-selector node and is not tested here.

There is also an independent outer-coordinate accounting obstruction.  If one literally merges
`r` old UIC coordinates into one supercoordinate, an optimistic outer numerator is only
`O((a/r)^(2/3))`; even granting the ideal inner ratio `sqrt(rm)`, the product is

\[
 O\!\left((a/r)^{2/3}\sqrt{rm}\right)
 =O\!\left(a^{2/3}\sqrt m\,r^{-1/6}\right),
\tag{1.4}
\]

which is worse than the addressed baseline.  Thus a successful construction must both leave the
independent outer UIC coordinate count at `Theta(a)` and avoid the selector-forgetting cut above.
No formula doing both is supplied by this audit.

The registered node remains **OPEN**.  The FAIL is restricted to hidden selector-star lifts whose
occurrence factors are independently slot-symmetric and whose chart/branch is forgotten by the
existing incidence.  It does not cover crossed slot operators, a noncommutative occurrence
algebra, or an independently registered growing outer selector.

## 2. Exact critical subsequence and the target scale

To make `r=Theta(m^(1/3))` integral while retaining the exact `p=0,u=1` critical orbit, let
`ell>=2` and put

\[
 k=\ell^3,\qquad
 a=k^2=\ell^6,\qquad
 q=4a,\qquad
 d=k,\qquad
 m=k+1=\ell^3+1,
\tag{2.1}
\]

\[
 n=am,\qquad N=2am,\qquad r=\ell.
\tag{2.2}
\]

Then

\[
 p=(n-a)-ad=0,\qquad u=q-4a+1=1,
\tag{2.3}
\]

and

\[
 r=\Theta(m^{1/3}),\qquad
 a=\Theta(m^2),\qquad
 N=\Theta(m^3).
\tag{2.4}
\]

The desired inner ratio is

\[
 \sqrt{mr}=\Theta(m^{2/3}).
\tag{2.5}
\]

There are no long-heavy exclusion variables on this subsequence, so a uniform endpoint law must
already pass here.

## 3. Typed hidden selector and exact incidence

### 3.1 Original presentation spaces

Use the exact addressed-copy notation of the rectangular-incidence memo:

\[
 \mathcal Y_t=\{(e,z):e\in E,\ z\in H_t\},
 \qquad \pi_t:\mathcal Y_t\to X_t.
\tag{3.1}
\]

The NO and YES fibers have sizes

\[
 c_0=C,\qquad c_1=uC,
\tag{3.2}
\]

and the coisometries are

\[
 R_0=C^{-1/2}Q_0,
 \qquad R_1=(uC)^{-1/2}Q_1.
\tag{3.3}
\]

At (2.1)--(2.3), `u=1` and `C=(a!)^2`.

### 3.2 Redundant `r`-chart selector

Fix one side; the other side is treated by an orthogonal direct sum.  Let

\[
 \Omega_{a,r}=\operatorname{Inj}([r],[a]),
 \qquad L=|\Omega_{a,r}|=(a)_r.
\tag{3.4}
\]

An element `s in Omega_(a,r)` is an ordered chart of `r` existing address blocks, and
`h in [r]` is the hidden informative-branch hypothesis.  Add no oracle symbols and define the
redundant presentation spaces

\[
 \widehat{\mathcal Y}_t
 =\mathcal Y_t\times\Omega_{a,r}\times[r],
 \qquad
 \widehat\pi_t(\tilde x,s,h)=\pi_t(\tilde x).
\tag{3.5}
\]

Thus the refined NO and YES fiber sizes are `CLr` and `uCLr`; their ratio is still exactly `u`.
Under the product identification, with uniform unit vectors `omega_Omega` and `omega_r`,

\[
 \widehat R_t
 =R_t\bigl(I\otimes\langle\omega_\Omega|
                \otimes\langle\omega_r|\bigr).
\tag{3.6}
\]

The selector is a pure presentation gauge variable: (3.6), not an unnormalized sum, is forced by
the exact incidence fibers.  For every physical coordinate `i`, the refined version of the exact
query identity remains

\[
 (\widehat R_1\widehat\Gamma\widehat R_0^*)\circ\Delta_i
 =\widehat R_1(\widehat\Gamma\circ\widehat\Delta_i)
  \widehat R_0^*.
\tag{3.7}
\]

### 3.3 Local row and column spaces

For a fixed chart `s`, the selected occurrence row and column spaces are separately typed as

\[
 \mathcal H_{1,s}=\ell_2([m]^r),
 \qquad
 \mathcal H_{0,s}=\ell_2([m]^r),
\tag{3.8}
\]

both of dimension `m^r`.  With the branch selector, the local map has type

\[
 \widehat K_s:
 \mathbb C^r\otimes\mathcal H_{0,s}
 \longrightarrow
 \mathbb C^r\otimes\mathcal H_{1,s},
\tag{3.9}
\]

and both sides of (3.9) have dimension `r m^r`.

Put

\[
 P={J_m\over m},\qquad Q=I_m-P,\qquad
 \rho={1\over m-1},\qquad A=P-\rho Q.
\tag{3.10}
\]

Let `B=xP+yQ` be any real common passive operator.  The selector-star candidate is

\[
 \widehat K_{s,B}
 =\sum_{h=1}^r |\omega_r\rangle\langle h|
 \otimes
 \left(A_h\bigotimes_{k\ne h}B_k\right).
\tag{3.11}
\]

It is covariant under simultaneous permutation of the chart slots and selector basis.  In the
special case `B=I`, its lift norm is `sqrt(r)`: the all-`P` occurrence vector makes the `r`
orthogonal column branches add in the common row branch.

The exact selector contraction in (3.6) gives

\[
 (\langle\omega_r|\otimes I)\widehat K_{s,B}
 (|\omega_r\rangle\otimes I)
 ={1\over\sqrt r}\sum_{h=1}^r
 A_h\bigotimes_{k\ne h}B_k
 =K_{s,B}.
\tag{3.12}
\]

Every tensor factor in (3.12) lies in `span{P,Q}`.  The apparent off-diagonal selector
orthogonality has therefore disappeared before the physical adversary is formed.

### 3.4 Full address invariance

Because no outer datum names a chart, full address invariance requires averaging (3.12) over
`s in Omega_(a,r)`.  For `B=I`, exact counting gives

\[
 {1\over L}\sum_{s\in\Omega_{a,r}}K_{s,I}
 ={\sqrt r\over a}\sum_{j=1}^a A_j,
\tag{3.13}
\]

since a fixed address `j` occurs as `s(h)` in exactly
`r(a-1)_(r-1)=Lr/a` pairs `(s,h)`.  Formula (3.13) is an element of the full `2^a`-sector
`P/Q` algebra.  For general `B`, the injection average is a symmetric polynomial in the commuting
`P/Q` factors and remains in the same algebra.

## 4. General physical-cut lemma

Let an arbitrary independently slot-symmetric operator on `r` blocks be

\[
 K=\sum_{\epsilon\in\{0,1\}^r}
 \kappa_\epsilon E_{\epsilon_1}\otimes\cdots\otimes E_{\epsilon_r},
 \qquad E_0=P,\ E_1=Q.
\tag{4.1}
\]

Its exact unmasked norm is

\[
 \|K\|=\max_\epsilon|\kappa_\epsilon|.
\tag{4.2}
\]

For a physical slot `v` in block `j`, define the exact pSearch masks

\[
 D_v^{\ne}(r,t)={\bf1}[r=v\text{ or }t=v],
\qquad
 D_v^{=}(r,t)={\bf1}[\text{exactly one of }r,t\text{ is }v].
\tag{4.3}
\]

For `C(x,y)=xP+yQ`, write

\[
 \phi_m(x,y)=\|C(x,y)\circ D_v^{\ne}\|,
 \qquad
 \psi_m(x,y)=\|C(x,y)\circ D_v^{=}\|.
\tag{4.4}
\]

The exact formulas from the fixed-two-block audit are

\[
 \phi_m(x,y)
 ={\sqrt{a_m(x,y)^2+4b_m(x,y)^2}+|a_m(x,y)|\over2},
\tag{4.5}
\]

\[
 \psi_m(x,y)=|b_m(x,y)|,
\tag{4.6}
\]

where

\[
 a_m(x,y)={x+(m-1)y\over m},
 \qquad
 b_m(x,y)={(x-y)\sqrt{m-1}\over m}.
\tag{4.7}
\]

Fixing every companion `P/Q` sector gives the exact all-slot identities

\[
 \|K\circ\Delta_{j,v}\|
 =\max_{\epsilon_{-j}}
 \phi_m(\kappa_{0,\epsilon_{-j}},
        \kappa_{1,\epsilon_{-j}})
 \quad\text{if block `j` has unequal outer labels},
\tag{4.8}
\]

\[
 \|K\circ\Delta_{j,v}\|
 =\max_{\epsilon_{-j}}
 \psi_m(\kappa_{0,\epsilon_{-j}},
        \kappa_{1,\epsilon_{-j}})
 \quad\text{if block `j` has equal outer labels}.
\tag{4.9}
\]

The value of `v` is immaterial by slot symmetry.  For `m>=5`, the sharp one-block inequality is

\[
 \phi_m(x,y)\ge{\max(|x|,|y|)\over\sqrt{m-1}}.
\tag{4.10}
\]

Choose a norm-active coefficient in (4.2).  If block `j` is unequal, its companion index appears
in the maximum (4.8), so (4.10) proves

\[
 \boxed{
 \|K\circ\Delta_{j,v}\|
 \ge {\|K\|\over\sqrt{m-1}}.
 }
\tag{4.11}
\]

Equations (4.8)--(4.9) audit **every physical slot** in the selected blocks.  Equation (4.11)
shows that one actual unequal block suffices to destroy any extra `sqrt(r)` ratio for every
operator that incidence compression returns to (4.1).  The location of that block need not be
named in advance inside the local occurrence formula: for each fixed outer transition sector the
actual value pattern supplies at least one such `j`.

This is a transition-block statement, and its use here is deliberately scoped.  It applies to the
typed selector-star lift (3.11), its tensor multiplication by an outer coefficient, and controlled
direct sums in which the displayed transition sector remains an operator block.  It is not a
ceiling for an arbitrary outer-pair-dependent family `K(z_1,z_0)` whose different occurrence
blocks interfere nonfactorizably after incidence.  Such interference is precisely part of the
still-open post-incidence non-`P/Q` overlap, not a consequence claimed by (4.11).

## 5. Explicit passive-operator gates

### 5.1 Passive identity: a constant-ratio coherent cut

For `B=I`, (3.12) is

\[
 K_{r,I}={1\over\sqrt r}\sum_{h=1}^r A_h,
 \qquad \|K_{r,I}\|=\sqrt r.
\tag{5.1}
\]

The norm is attained on the all-`P` sector.  Since `A` has zero diagonal,

\[
 A\circ D_v^{\ne}=A\circ D_v^{=}
 \ \widehat=\
 \begin{pmatrix}0&1/\sqrt{m-1}\\
                 1/\sqrt{m-1}&0\end{pmatrix}
 =:B_v,
\tag{5.2}
\]

in the basis consisting of `e_v` and the uniform vector off `v`.  Also

\[
 I\circ D_v^{\ne}=|v\rangle\langle v|=:E_v,
 \qquad I\circ D_v^{=}=0.
\tag{5.3}
\]

If block `j` is equal, then exactly

\[
 \|K_{r,I}\circ\Delta_{j,v}\|
 ={1\over\sqrt{r(m-1)}}.
\tag{5.4}
\]

If block `j` is unequal, then

\[
 K_{r,I}\circ\Delta_{j,v}
 ={1\over\sqrt r}
 \left(B_v\otimes I
 +E_v\otimes\sum_{h\ne j}A_h\right).
\tag{5.5}
\]

Diagonalize the companion blocks by their number `t` of `Q` sectors.  The second term has
eigenvalues

\[
 \lambda_t=r-1-(1+\rho)t,
 \qquad 0\le t\le r-1,
\tag{5.6}
\]

and `max_t |lambda_t|=r-1`.  Hence the exact unequal-slot norm is

\[
 \|K_{r,I}\circ\Delta_{j,v}\|
 ={\sqrt{(r-1)^2+4/(m-1)}+(r-1)\over2\sqrt r}
 \ge {r-1\over\sqrt r}.
\tag{5.7}
\]

Combining (5.1) and (5.7),

\[
 {\|K_{r,I}\|\over
   \|K_{r,I}\circ\Delta_{j,v}\|}
 \le {r\over r-1}<2.
\tag{5.8}
\]

Thus the hidden-star intuition counted the `h` branches as orthogonal in the numerator but
incorrectly treated the `r-1` passive identity branches as invisible to the actual unequal query.

After full injection averaging, (3.13) has norm `sqrt(r)`.  Replacing `r-1` by `a-1` in the same
calculation gives

\[
 \left\|{\sqrt r\over a}\sum_{h=1}^aA_h
       \circ\Delta_{j,v}\right\|
 ={\sqrt r\over a}
 {\sqrt{(a-1)^2+4/(m-1)}+(a-1)\over2}
 \ge\sqrt r,{a-1\over a}.
\tag{5.9}
\]

The fully invariant law also has ratio less than two.

### 5.2 Passive `P`: small individual masks still add coherently

Set `B=P`.  Then

\[
 K_{r,P}={1\over\sqrt r}\sum_{h=1}^r
 A_h\bigotimes_{k\ne h}P_k,
 \qquad \|K_{r,P}\|=\sqrt r.
\tag{5.10}
\]

Its only nonzero unmasked sectors are all `P`, with coefficient `sqrt(r)`, and the `r` sectors
having one `Q`, each with coefficient `-rho/sqrt(r)`.  In the all-`P` companion sector, a query in
any block `j` restricts to

\[
 {1\over\sqrt r}\bigl(A+(r-1)P\bigr).
\tag{5.11}
\]

For an unequal block, (4.10) applied to (5.11), whose `P` eigenvalue is `sqrt(r)`, gives

\[
 \|K_{r,P}\circ\Delta_{j,v}\|
 \ge {\sqrt r\over\sqrt{m-1}}.
\tag{5.12}
\]

The equal-label restriction is also explicit:

\[
 \|K_{r,P}\circ\Delta_{j,v}\|
 \ge {r+\rho\over\sqrt r}
       {\sqrt{m-1}\over m}
 =\Theta\!\left(\sqrt{r/m}\right).
\tag{5.13}
\]

Thus `P circ D_v^ne=Theta(1/sqrt(m))` is not enough.  The same
`Theta(1/sqrt(m))` piece occurs in `r-1` passive branches on a common all-`P` vector.  Their sum
has size `Theta(sqrt(r/m))`, exactly canceling the numerator's `sqrt(r)` gain.

### 5.3 General passive `xP+yQ` and arbitrary signs

No special choice of the passive eigenvalues cancels the decisive cut.  More generally, allow
branch weights `c_h` and put

\[
 K=\sum_{h=1}^r c_h
 A_h\bigotimes_{k\ne h}B_k,
 \qquad B=xP+yQ.
\tag{5.14}
\]

This is an instance of (4.1), so (4.8)--(4.11) already prove the ratio ceiling.  The attempted
coefficient cancellation can also be seen directly.  Fix any norm-active `P/Q` sector and then
fix all companion sectors to a physical unequal block `j`.  The surviving one-block operator has
two eigenvalues equal to the two coefficients of `K` obtained by putting `P` or `Q` in slot `j`.
One of them has modulus `||K||`.  The sharp inequality (4.10) forces its unequal query mask to be
at least `||K||/sqrt(m-1)`, regardless of cancellations in either the diagonal or off-diagonal
entry of the printed `2 x 2` mask.

This closes the common-passive selector-star family, including `I`, `P`, `A`, arbitrary
`xP+yQ`, arbitrary real branch signs, and their fully invariant injection averages.  It does not
close an operator that leaves the independently slot-symmetric algebra after physical incidence.

## 6. Sparse-transition gate versus selector gain

For a fixed outer YES/NO pair, let `D` be the set of selected blocks whose outer labels differ.
UIC legality guarantees that `D` is nonempty on at least one side; a Hamming-one YES-to-NO edge
can make `|D|=1`.

There are only two possibilities in the selector-star construction.

1. **All hidden branches remain present.**  This is required to obtain a `sqrt(r)` selector norm.
   Then any `j in D` supplies the coherent physical cut (4.11); for passive `I` it supplies the
   stronger constant-ratio cut (5.7).
2. **The outer coefficient gates the selector to the actual changed branch.**  If `D={j}`, only
   the `h=j` branch remains.  Selector compression contributes `1/sqrt(r)` to both numerator and
   masks, so rescaling returns exactly the one-block `sqrt(m-1)` ratio.  Moreover the outer data
   has now named the informative block, contrary to the intended escape condition.

Using `O(1)` rather than exactly one informative transition changes only constants.  It never
creates `r` norm-active branches while keeping each changed-coordinate cut supported on only one
of them within (3.11).  A global norm recovered by coupling different changed-coordinate outer
sectors is outer-selector interference, not the hidden occurrence-selector gain tested here; a
nonfactorizable version belongs outside this scoped family.

## 7. Outer-coordinate accounting

The local target `sqrt(rm)` is not sufficient by itself.  The outer numerator must remain
`Theta(a^(2/3))`.

If disjoint groups of `r` old coordinates are treated as `a/r` independent supercoordinates,
then even optimistically granting a `UIC_(a/r)` numerator and the ideal local inner ratio gives
(1.4).  At `r=m^(1/3)`, the loss is

\[
 r^{-1/6}=m^{-1/18},
\tag{7.1}
\]

so this route is below the already available addressed scale, not at the target endpoint.

To retain `Theta(a)` outer coordinates one must overlap/reuse the old blocks.  In the present
hidden-selector law, full `S_a` averaging is the exact overlap mechanism, and (3.13), (4.11), and
(5.9) show that the same reuse is visible coherently to a physical query.  Keeping the subset or
chart as an unaveraged orthogonal label would instead require the outer transition to carry that
growing selector.  That is outside this node's tested formula and belongs to the already
registered growing-selector/Specht branching node.

Therefore the outer gate for any future candidate is:

\[
 \boxed{\text{prove `Theta(a)` independent outer UIC coordinates survive,}}
\tag{7.2}
\]

while also proving that no physical query inherits the overlap multiplicity.  Merely displaying
a local `sqrt(rm)` norm ratio is insufficient.

## 8. General `u` and `p>0` obligations

The hidden selector is redundant presentation data, so for general

\[
 u=q-4a+1\in\{1,2,3,4\}
\tag{8.1}
\]

it multiplies the original fibers to `CLr` on NO and `uCLr` on YES.  It does not alter the exact
full-orbit normalization `1/(C sqrt(u))`; equation (3.6) simply adds the common uniform-selector
contraction.

When `p>0`, the original common fiber factor is `C=(a!)^2m^(2p)`.  A legal construction must also
type the long-heavy exclusion variables and bound queries at every public/excluded occurrence.
The present candidate does not do so.  This omission cannot rescue it as a uniform endpoint
formula: the infinite legal `p=0,u=1` subsequence already exhibits the exact changed-coordinate
cut.  However the present FAIL must not be extrapolated to a different formula whose occurrence
operator is not the selector-star/PQ family; such a formula would still owe all `p>0` and `u>1`
gates.

## 9. Interface and non-circularity audit

* **No Boolean replacement.**  The operator acts on the existing `pSearch_m` occurrence spaces and
  leaves the actual UIC labels untouched.  It never substitutes a Boolean collision bit.
* **No alphabet growth.**  `Omega_(a,r)` and `[r]` are presentation selectors, not oracle symbols;
  the physical alphabet remains `q`.
* **Exact rectangular type.**  The local row and column spaces are separately typed in (3.8)--
  (3.9), and insertion into the full orbit uses `R_1 ... R_0^*` with the unchanged `1/sqrt(u)`
  imbalance.
* **No recursive donor.**  Equations (3.11)--(3.12) are explicit matrices built from `P,Q,A`; no
  lower bound for another hidden-frequency instance is assumed.
* **Every physical slot.**  Equations (4.8)--(4.9) cover all selected short-block slots; outside a
  local chart an identity factor gives zero on an equal block and its full companion norm on an
  unequal block.  Full injection averaging eliminates the outside-chart distinction and is
  covered by the `2^a`-sector version of (4.8)--(4.11).  The `p=0` subsequence has no public long
  slots.

## 10. Gate ledger

| Obligation | Outcome |
|---|---|
| exact target scale `r=Theta(m^(1/3))` | integer legal subsequence (2.1)--(2.5) |
| local row/codomain | `ell_2([m]^r) -> ell_2([m]^r)` |
| hidden selector type | `C^r tensor H_0 -> C^r tensor H_1` |
| exact refined incidence fibers | `CLr` and `uCLr`; ratio remains `u` |
| selector-star law | explicit (3.11) |
| selector compression | exact PQ operator (3.12) |
| full `S_a` invariance | injection average; explicit identity-passive formula (3.13) |
| unmasked selector gain | `sqrt(r)` for identity/passive-`P` examples |
| every equal/unequal slot mask | exact formulas (4.8)--(4.9) |
| physical changed-coordinate cut | ratio at most `sqrt(m-1)`, equation (4.11) |
| passive `I` | stronger constant ceiling, equations (5.7)--(5.8) |
| passive `P` | mask `Theta(sqrt(r/m))`; only `Theta(sqrt(m))` ratio |
| arbitrary common `xP+yQ` and signs | same `sqrt(m-1)` ceiling |
| local inner target `sqrt(mr)` | **FAIL in declared selector-star/PQ family** |
| outer `a^(2/3)` under disjoint grouping | **FAIL**, loses `r^(2/3)` and net `r^(-1/6)` |
| overlapping non-PQ law preserving `a` coordinates | unconstructed and unrefuted |
| growing outer selector | separate registered node; not tested here |
| `p>0,u>1` | not needed for this p=0 failure; owed by any different candidate |
| numerical evidence | none used |
| completion status | none; independent review absent |

## 11. Scope boundary

The **FAIL** verdict covers precisely:

* the infinite exact `p=0,u=1` critical subsequence (2.1)--(2.3);
* a redundant invariant injection chart and hidden branch forgotten by exact incidence;
* the selector-star map (3.11), including arbitrary real branch weights;
* active `A=(J-I)/(m-1)` and any common independently slot-symmetric passive `xP+yQ`;
* passive `I`, `P`, `A`, and full uniform injection averages;
* sparse outer transitions with one or any fixed positive number of unequal selected blocks;
* every physical short-block query mask in that family;
* disjoint `r`-to-one supercoordinate accounting, even under the optimistic local ratio
  `sqrt(rm)`.

It does **not** cover:

* a compressed occurrence operator outside the independent `P/Q` algebra;
* crossed row-block/column-block slot charts carrying noncommutative cycle data;
* a growing outer selector, full matching, or cycle word (the separate registered successor);
* an overlapping construction that independently proves both `Theta(a)` outer coordinates and no
  overlap multiplicity in every physical mask;
* the full coupled UIC/address-cycle node or the critical endpoint.

## 12. Bottom line

The naive `sqrt(r)` argument counts orthogonal presentation branches before applying the map that
forgets those branches.  Exact incidence turns the smallest hidden-star lift into an ordinary
`P/Q` occurrence operator.  A real unequal block then supplies an exact one-coordinate cut whose
masked norm is at least `1/sqrt(m-1)` times the whole unmasked norm.  Passive `I` makes that cut
constant-ratio; passive `P` makes each term small but lets all terms add on the same all-`P`
direction, returning the ordinary `sqrt(m)` scale.

Keeping the branches orthogonal would require outer data that retains a growing selector.  Merging
blocks instead reduces the outer coordinate count and loses more than the inner `sqrt(r)` can
repay.  Therefore this explicit sparse-delocalized selector-star family does not supply the
missing `m^(1/6)` factor.  The node remains open only for a genuinely different, post-incidence
non-`P/Q` overlapping law that also preserves the full outer `a^(2/3)` numerator.
