# L3 critical endpoint: coupled multiblock occurrence-inner audit

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel`  
Status of this memo: **FAIL** for the independently slot-symmetric fixed two-block inner family;
**PARTIAL** for growing-block delocalization; proposer-tier only

## 1. Verdict

The smallest genuinely joint occurrence-level operator can be typed and diagonalized exactly, but
it does not improve the inner exponent.

On the infinite legal `p=0,u=1` critical subsequence, take the two `pSearch_m` blocks at the left
and right endpoints of the outer YES input's unique collision.  Their occurrence spaces are both
`ell_2([m]^2)`.  Under independent internal slot permutations, every real two-block operator has four
orthogonal `P/Q` sectors.  For every physical slot query, its masked norm is an exact one-block
expression on each companion sector.  Since at least one collision endpoint changes in every
YES-to-NO outer transition, the sharp inequality is

\[
 {\|K\|\over \max_i\|K\circ\Delta_i\|}
 \le \sqrt{m-1}
 \qquad(m\ge5).
 \tag{1.1}
\]

The sharp one-block direction is

\[
 A={J_m-I_m\over m-1}=P-{1\over m-1}Q.
 \tag{1.2}
\]

There is even an explicit operator-Schmidt-rank-two candidate

\[
 K_{\rm joint}=A\otimes A+{1\over m-1}Q\otimes Q
 \tag{1.3}
\]

with

\[
 \|K_{\rm joint}\|=1,
 \qquad
 \|K_{\rm joint}\circ\Delta_i\|={1\over\sqrt{m-1}}
 \tag{1.4}
\]

for every physical slot in either selected block, whether the companion outer symbols are equal
or unequal.  Thus (1.3) is genuinely nonseparable as an operator formula but its joint sector is
spectrally inert: the `P tensor P`/BHK component already fixes both numerator and largest mask.

Consequently a fixed two-block replacement of the standard BHK occurrence tensor still supplies
only `Theta(sqrt(m))`, not `m^(2/3)`.  This FAIL is exact for the declared slot-symmetric,
incidence-closed/aligned family.  It does not cover a coefficient whose norm-active outer
transition is genuinely delocalized over a growing number of address blocks after full incidence
compression.

For the simplest orthogonal load-balancing mechanism over `r` candidate blocks, the most it can
add to the one-block ratio is `sqrt(r)`.  Merely becoming scale-eligible therefore requires

\[
 \sqrt m\sqrt r\ge m^{2/3}
 \quad\Longrightarrow\quad
 r\ge m^{1/3}.
 \tag{1.5}
\]

Equation (1.5) is a **necessary scale in that mechanism, not a no-go theorem**.  If exactly one
informative transition is hidden among `r` blocks, Grover search over the `rm` occurrence slots
costs `Theta(sqrt(rm))`; at `r=m^(1/3)` this is exactly `m^(2/3)`.  Hence this pass neither proves
nor refutes the growing-`r` boundary case.

Finally, replacing that missing law by another hidden-frequency critical donor is circular only
under a specific parameterization: an `r`-block, block-size-`m`, alphabet-`Theta(r)` hidden-
frequency instance has length `Theta(rm)`, and its critical relation forces `r=Theta(m^2)`.  Since
the present endpoint has `a=Theta(m^2)`, that proposed inner donor is the original critical core
up to constants.  This circularity statement does not apply to every possible delocalized
coefficient law.

## 2. Exact scope and typed domain

Work on the exact subsequence already used by the pointed-hook audit:

\[
 a=k^2,\qquad q=4k^2,\qquad d=k,\qquad m=k+1,
 \qquad n=am,
 \tag{2.1}
\]

so `p=0`, `u=1`, and `N=2am`.  There are no long-block public exclusions in this test.

Fix an outer pair `(z_1,z_0) in U_1 x U_0`.  The YES input `z_1` has a unique common label at one
left outer coordinate `b_L` and one right outer coordinate `b_R`.  Put

\[
 \delta_s={\bf1}[z_{1,s}(b_s)\ne z_{0,s}(b_s)],
 \qquad s\in\{L,R\}.
 \tag{2.2}
\]

Because `z_0` is a NO input,

\[
 \delta_L+\delta_R\ge1.
 \tag{2.3}
\]

In one addressed source copy, the variable occurrence of each block lies in `[m]`.  The two
selected row and column spaces are therefore

\[
 \mathcal H_1^{(2)}
 =\ell_2([m]_{r_L}\times[m]_{r_R}),
 \qquad
 \mathcal H_0^{(2)}
 =\ell_2([m]_{t_L}\times[m]_{t_R}),
 \tag{2.4}
\]

both of dimension `m^2`.  A local occurrence operator is a rectangular map

\[
 K:\mathcal H_0^{(2)}\longrightarrow\mathcal H_1^{(2)}.
 \tag{2.5}
\]

The dimensions happen to agree, but the row and column bases remain typed by different answer
classes.  Formula (2.5) is inserted into the already typed presentation lift

\[
 \widetilde\Gamma:\ell_2(\mathcal Y_0)\longrightarrow\ell_2(\mathcal Y_1),
 \qquad
 \Gamma=R_1\widetilde\Gamma R_0^*,
 \tag{2.6}
\]

where on this subsequence both incidence fiber sizes are `C`.  For general `u`, the same insertion
uses the previously proved entry factor `1/(C sqrt(u))`; nothing below changes that normalization.

This memo audits the incidence-closed/aligned occurrence chart: the two chosen addressed blocks
use the same physical slot chart on the row and column sides.  Full crossed charts produced by a
nontrivial relative address cycle are outside the FAIL scope; they belong to the still-open
growing/full-address coupling.

## 3. The complete slot-symmetric two-block algebra

Let

\[
 |\mathbf u\rangle={1\over\sqrt m}(1,\ldots,1),
 \qquad
 P=|\mathbf u\rangle\langle\mathbf u|={J_m\over m},
 \qquad
 Q=I_m-P.
 \tag{3.1}
\]

Write `E_0=P,E_1=Q`.  Requiring invariance under independent simultaneous reorderings of the row
and column slots in each selected block gives the whole commutant

\[
 K_\kappa
 =\sum_{\alpha,\beta\in\{0,1\}}
   \kappa_{\alpha\beta}E_\alpha\otimes E_\beta,
 \qquad \kappa_{\alpha\beta}\in\mathbb R.
 \tag{3.2}
\]

The four terms in (3.2) have mutually orthogonal row and column supports.  Hence the exact
unmasked norm is

\[
 \boxed{\|K_\kappa\|=\max_{\alpha,\beta}|\kappa_{\alpha\beta}|.}
 \tag{3.3}
\]

Thus different `P/Q` sectors form an operator direct sum.  A rank-two coefficient matrix
`kappa` is algebraically nonseparable, but its unmasked norm is still attained in one separable
sector; there is no numerator interference among the four sectors.

## 4. Exact physical query masks

Fix a physical slot `v` in one selected block.  If the two outer labels in that block differ, its
`pSearch` query mask on `[m] x [m]` is

\[
 D_v^{\ne}(r,t)
 ={\mathbf 1}[r=v\ \text{or}\ t=v].
 \tag{4.1}
\]

If the outer labels agree, it is

\[
 D_v^{=}(r,t)
 ={\mathbf 1}[\text{exactly one of }r,t\text{ equals }v].
 \tag{4.2}
\]

For a real one-block invariant operator

\[
 B(x,y)=xP+yQ,
 \tag{4.3}
\]

put `s=sqrt(m-1)`.  In the orthonormal basis consisting of `e_v` and the uniform vector on
`[m]\{v}`, the nonzero block of the unequal-label mask is exactly

\[
 B(x,y)\circ D_v^{\ne}
 \ \widehat=\
 \begin{pmatrix}
  a_m(x,y)&b_m(x,y)\\
  b_m(x,y)&0
 \end{pmatrix},
 \tag{4.4}
\]

where

\[
 a_m(x,y)={x+(m-1)y\over m},
 \qquad
 b_m(x,y)={(x-y)\sqrt{m-1}\over m}.
 \tag{4.5}
\]

Therefore

\[
 \phi_m(x,y)
 :=\|B(x,y)\circ D_v^{\ne}\|
 ={\sqrt{a_m(x,y)^2+4b_m(x,y)^2}+|a_m(x,y)|\over2}.
 \tag{4.6}
\]

For equal outer labels, the diagonal entry is removed and

\[
 \psi_m(x,y)
 :=\|B(x,y)\circ D_v^{=}\|
 =|b_m(x,y)|.
 \tag{4.7}
\]

The physical slot `v` is immaterial by permutation symmetry.  Applying (4.6)--(4.7) to (3.2)
gives every selected-block mask exactly.  For a left query,

\[
 \|K_\kappa\circ\Delta_{L,v}\|
 =
 \begin{cases}
 \displaystyle\max_{\beta}
   \phi_m(\kappa_{0\beta},\kappa_{1\beta}),&\delta_L=1,\\[2mm]
 \displaystyle\max_{\beta}
   \psi_m(\kappa_{0\beta},\kappa_{1\beta}),&\delta_L=0,
 \end{cases}
 \tag{4.8}
\]

and for a right query,

\[
 \|K_\kappa\circ\Delta_{R,v}\|
 =
 \begin{cases}
 \displaystyle\max_{\alpha}
   \phi_m(\kappa_{\alpha0},\kappa_{\alpha1}),&\delta_R=1,\\[2mm]
 \displaystyle\max_{\alpha}
   \psi_m(\kappa_{\alpha0},\kappa_{\alpha1}),&\delta_R=0.
 \end{cases}
 \tag{4.9}
\]

Equations (4.8)--(4.9) are direct sums over the untouched companion `P/Q` sector, not triangle-
inequality bounds.

## 5. Sharp one-block ceiling and the active rank-one direction

For `m>=5`, direct minimization of (4.6) gives

\[
 \boxed{
 \phi_m(x,y)
 \ge {\max(|x|,|y|)\over\sqrt{m-1}}.
 }
 \tag{5.1}
\]

For real `(x,y) != (0,0)`, equality holds precisely on the ray

\[
 (x,y)=\lambda\left(1,-{1\over m-1}\right).
 \tag{5.2}
\]

Here is a short exact check.  By homogeneity normalize `max(|x|,|y|)=1`.  On the edges
`|x|=1`, global sign reduces to `x=1`; differentiating (4.6) on the two sides of
`a_m(1,y)=0` shows that for `m>=5` the unique minimum occurs at
`y=-1/(m-1)`.  It has `a_m=0`, `|b_m|=1/sqrt(m-1)`.  On the two edges
`|y|=1`, direct differentiation gives its minimum at
`x=(2m-3)/(4m-3)`, with value

\[
 {4(m-1)\over4m-3}>{1\over\sqrt{m-1}},
 \tag{5.3}
\]

so those edges cannot attain (5.1).

Normalize (3.2) by `||K_kappa||=1`.  Some coefficient has modulus one.  If, say, the left
collision endpoint changes, the column containing that coefficient and (5.1) imply

\[
 \|K_\kappa\circ\Delta_{L,v}\|
 \ge {1\over\sqrt{m-1}}.
 \tag{5.4}
\]

The same reasoning applies on the right.  Since (2.3) guarantees at least one unequal endpoint,
(3.3), (4.8)--(4.9), and (5.4) prove (1.1).

The equality structure explains why this algebra cannot hide a useful joint effect.  Every
norm-active column controlled by an unequal left query must be proportional to

\[
 u=\left(1,-{1\over m-1}\right)^T,
 \tag{5.5}
\]

and every norm-active row controlled by an unequal right query must be proportional to `u^T`.
If both columns and rows are norm-active, the only simultaneous completion is

\[
 \kappa=\lambda uu^T,
 \tag{5.6}
\]

which has coefficient rank one and gives the separable operator `lambda A tensor A`.  A rank-two
completion can share the same overall ratio only by putting its extra coefficients strictly below
the already norm-active sector.  Such a completion neither raises (3.3) nor lowers the mask in
(5.4); it is spectrally inert rather than a joint gain.

## 6. An explicit genuinely joint two-block formula

Put

\[
 \rho={1\over m-1},
 \qquad
 A=P-\rho Q={J_m-I_m\over m-1},
 \tag{6.1}
\]

and define

\[
 K_{\rm joint}=A\otimes A+\rho Q\otimes Q.
 \tag{6.2}
\]

Its exact entry formula on the typed domain (2.4) is

\[
 K_{\rm joint}[(r_L,r_R),(t_L,t_R)]
 =A[r_L,t_L]A[r_R,t_R]
  +\rho Q[r_L,t_L]Q[r_R,t_R].
 \tag{6.3}
\]

In the ordered sectors `(P tensor P,P tensor Q,Q tensor P,Q tensor Q)`, its eigenvalues are

\[
 1,\quad-\rho,\quad-\rho,\quad\rho^2+\rho.
 \tag{6.4}
\]

Thus for `m>=3`,

\[
 \|K_{\rm joint}\|=1.
 \tag{6.5}
\]

Its `2 x 2` coefficient matrix is

\[
 \kappa_{\rm joint}
 =\begin{pmatrix}
  1&-\rho\\
  -\rho&\rho^2+\rho
 \end{pmatrix},
 \qquad
 \det\kappa_{\rm joint}=\rho\ne0.
 \tag{6.6}
\]

Hence (6.2) has operator Schmidt rank two and is genuinely nonseparable.

For the first column `(1,-rho)`, both (4.6) and (4.7) equal

\[
 {1\over\sqrt{m-1}}.
 \tag{6.7}
\]

For the second column `(-rho,rho^2+rho)`, equations (4.5)--(4.7) give

\[
 a_m={1\over m},
 \qquad
 |b_m|={2m-1\over m(m-1)^{3/2}},
 \tag{6.8}
\]

and therefore

\[
 \phi_m(-\rho,\rho^2+\rho)
 ={1+\sqrt{1+4(2m-1)^2/(m-1)^3}\over2m},
 \tag{6.9}
\]

\[
 \psi_m(-\rho,\rho^2+\rho)
 ={2m-1\over m(m-1)^{3/2}}.
 \tag{6.10}
\]

For `m>=5`, both (6.9) and (6.10) are at most `1/sqrt(m-1)`.  The matrix is symmetric, so the
same calculation applies to its rows.  Combining (4.8)--(4.9) gives the promised exact result

\[
 \boxed{
 \|K_{\rm joint}\circ\Delta_{L,v}\|
 =\|K_{\rm joint}\circ\Delta_{R,v}\|
 ={1\over\sqrt{m-1}}
 }
 \tag{6.11}
\]

for every slot `v`, independently of whether the unselected endpoint has equal or unequal outer
labels.  The rank-two term changes neither side of the adversary ratio.

To make a full aligned addressed coefficient, multiply (6.3) by the outer UIC coefficient on the
transition `(z_1,z_0)`, use (6.2) on its two collision-endpoint blocks, use `A` on every other
unequal-output block, and use `I_m` on every other equal-output block.  All unmarked occurrence
factors have norm one.  A query in any unequal ordinary block or either selected block has norm
`1/sqrt(m-1)`; a query in an ordinary equal block has norm zero.  Fixed remainder coordinates are
absent on (2.1).  Thus every physical occurrence mask in this declared aligned construction has
been covered.

## 7. Algorithmic ceiling and non-circularity of the fixed two-block test

The exact algebraic ceiling agrees with a black-box upper bound.  Once the outer transition names
one changed collision-endpoint block, Grover search recovers that block's unique non-star label in
`O(sqrt(m))` queries.  Equivalently, any adversary supported only on the fixed two-block occurrence
promise is bounded by `O(sqrt(m))` by general-adversary optimality.  Coupling finitely many
additional named blocks cannot change this upper bound.

At the full addressed level, the source function is still

\[
 \mathrm{UIC}_a\circ(\mathrm{pSearch}_m)^{2a},
 \tag{7.1}
\]

which has the standard `O(a^(2/3)sqrt(m))` algorithm.  Therefore an occurrence law confined to
one addressed copy cannot exceed the already proved `N^(11/18)` scale.  The possible escape has
always been interference between many hidden address presentations after (2.6), not a more clever
matrix on two named source blocks.

The test (6.2) is not circular: it invokes no lower bound for the critical endpoint, changes no
promise, and adds no oracle symbols.  It is a direct formula on two existing occurrence spaces.

## 8. What growing `r` would have to accomplish

There are two qualitatively different regimes.

### 8.1 A changed block remains named

If the outer transition or the coefficient formula still identifies a particular changed block
`b`, then querying that block by Grover costs `O(sqrt(m))`, irrespective of how many passive blocks
are coupled to it.  In the independently slot-symmetric `r`-block algebra this is also visible
directly: the algebra is the `2^r`-sector direct sum

\[
 \sum_{\epsilon\in\{0,1\}^r}
 \kappa_\epsilon E_{\epsilon_1}\otimes\cdots\otimes E_{\epsilon_r},
 \tag{8.1}
\]

and a query in the named unequal block applies the sharp one-block bound (5.1) on every fixed
companion sector.  No growing `r` helps in this regime.

### 8.2 The changed address is genuinely delocalized

To escape (8.1), the norm-active transition must be hidden among `r` candidate address blocks so
that no fixed physical query sees every active sector.  In the simplest orthogonal load-balancing
model, `r` branches can reduce a one-coordinate load by at most `sqrt(r)` by Cauchy--Schwarz.
Starting from the one-block ratio `Theta(sqrt(m))`, this yields at most

\[
 O(\sqrt{rm}).
 \tag{8.2}
\]

Therefore this particular mechanism cannot even reach `m^(2/3)` unless

\[
 r=\Omega(m^{1/3}).
 \tag{8.3}
\]

This is only a necessary scaling law for orthogonal branch delocalization.  It is not a ceiling on
arbitrary full-orbit coefficients.

At `r=m^(1/3)`, two cases separate sharply.

* If all `r` blocks contain independently informative differences, Grover search over their `rm`
  slots has `r` marks and still costs only `Theta(sqrt(m))`; there is no gain.
* If only `O(1)` transition is informative and its address is hidden among the `r` blocks, Grover
  search costs `Theta(sqrt(rm))=Theta(m^(2/3))`.  This meets, rather than beats, the desired lower
  scale.  The present audit does not rule this sparse delocalized case out.

A successful continuation must therefore provide an invariant formula that simultaneously makes
the informative transition sparse, prevents the outer data from naming its block, survives the
rectangular incidence compression, and controls every crossed physical-role mask and every long-
exclusion status.  No such formula is constructed here.

## 9. Exact boundary of the circular-inner objection

Suppose one attempts to declare the growing-`r` gadget itself to be another hidden-frequency
critical instance with

\[
 B_{\rm in}=\Theta(rm),
 \qquad
 q_{\rm in}=\Theta(r).
 \tag{9.1}
\]

The critical relation `q_in=Theta(B_in^(2/3))` then says

\[
 r=\Theta((rm)^{2/3})
 \quad\Longleftrightarrow\quad
 r=\Theta(m^2).
 \tag{9.2}
\]

At the current endpoint,

\[
 N=\Theta(am),
 \qquad a=\Theta(N^{2/3}),
 \qquad m=\Theta(N^{1/3}),
 \tag{9.3}
\]

so `a=Theta(m^2)`.  Equations (9.2)--(9.3) make the proposed inner critical donor the original
`a`-block critical problem up to constants.  Assuming its `Omega(B_in^(2/3))` adversary would be
the desired endpoint lemma itself, hence circular.

This objection depends on both assumptions in (9.1): alphabet proportional to the number of
blocks and another hidden-frequency critical donor.  It does **not** refute a direct
`r=m^(1/3)` signed/delocalized coefficient law, a different alphabet scaling, or a noncritical
inner coherent configuration.

## 10. Range, interface, and known-upper-bound audit

* **Legality and range.**  Formula (6.3) changes only adversary coefficients.  It introduces no
  input symbol, does not alter the frozen histograms, and keeps the alphabet at `q`.
* **Rectangular interface.**  The local row and column spaces are separately typed in (2.4), and
  their insertion uses the existing `R_1 ... R_0^*` incidence map.  No square address matrix is
  silently substituted for the full YES-to-NO operator.
* **Value interface.**  The construction does not replace `pSearch` by a Boolean Collision
  gadget; the outer UIC coordinates still receive their actual labels.  A literal Boolean
  ED/Collision inner would fail that interface.
* **Fixed-block upper bound.**  A named differing block is solvable in `O(sqrt(m))`, matching
  (1.1).  The whole addressed source is solvable in `O(a^(2/3)sqrt(m))`.
* **Sparse growing-`r` upper bound.**  `O(sqrt(rm))` becomes exactly `m^(2/3)` at
  `r=m^(1/3)`; it is not a subtarget algorithm and hence does not kill that case.
* **Critical-donor circularity.**  It applies only under (9.1), where (9.2) forces
  `r=Theta(m^2)=Theta(a)`.

## 11. Gate ledger

| Obligation | Outcome |
|---|---|
| exact two-block row/codomain | `ell_2([m]^2) -> ell_2([m]^2)`, equation (2.4) |
| complete independently slot-symmetric algebra | four `P/Q` sectors, equation (3.2) |
| exact unmasked norm | `max |kappa_ab|`, equation (3.3) |
| every selected physical slot mask | exact formulas (4.8)--(4.9) |
| sharp unequal-block ceiling | `sqrt(m-1)`, equation (5.1) |
| equality structure | active BHK ray; fully active completion rank one |
| explicit genuinely joint candidate | operator Schmidt rank two, equations (6.2)--(6.6) |
| its unmarked and all selected mask norms | `1` and `1/sqrt(m-1)`, equations (6.5), (6.11) |
| inner gain `m^(2/3)` from fixed two blocks | **FAIL** |
| named changed block with growing companions | **FAIL**, Grover `O(sqrt(m))` |
| orthogonal delocalization necessary scale | `r=Omega(m^(1/3))`; necessary only |
| sparse delocalized `r=m^(1/3)` law | **OPEN / not constructed / not refuted** |
| hidden-frequency inner donor | circular only when (9.1) forces `r=Theta(m^2)` |
| range or label interface violation | none for (6.2); Boolean replacement would fail |
| numerics | none used as evidence |

## 12. Scope boundary and bottom line

The FAIL verdict covers:

* a fixed number of named occurrence blocks, in particular the two outer collision endpoints;
* independent internal slot-permutation invariance;
* the aligned/incidence-closed addressed chart;
* arbitrary real coefficients in the complete four-sector algebra (3.2);
* the explicit genuinely nonseparable formula (6.2);
* any growing number of passive companions while one changed block remains named.

It does not cover:

* a norm-active transition genuinely delocalized over `r=Omega(m^(1/3))` address blocks;
* crossed row-block/column-block physical-role masks from nontrivial relative address cycles;
* growing Specht multiplicity sectors or full colored cycle-word coefficients;
* the long-heavy exclusion statuses when `p>0`;
* the full registered coupled node.

The minimal two-block experiment is decisive within its scope.  A nonseparable occurrence formula
exists and is perfectly legal, but the `P/Q` decomposition exposes it as a direct sum whose active
direction is still the sharp one-block pSearch adversary.  Fixed-block jointness changes the
formula, not the exponent.

The only remaining occurrence-level escape identified here is genuinely growing, sparse address
delocalization.  The first scale at which orthogonal load balancing could possibly supply the
missing `m^(1/6)` is `r=m^(1/3)`.  That boundary is neither proved nor refuted by this memo and must
not be confused with the circular `r=m^2` hidden-frequency-inner proposal.
