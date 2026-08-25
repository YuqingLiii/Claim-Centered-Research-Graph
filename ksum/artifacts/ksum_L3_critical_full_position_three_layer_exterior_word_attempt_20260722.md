# L3 critical endpoint: centered full-position exterior word and off-equality fiber audit

Date: 2026-07-22
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.full-position-incidence-three-layer-word-kernel`
Verdict: **PASS for a genuine third full-position relation; FAIL for the fixed-centered
contingency exterior/minor carrier and for the first explicit three-relation rectangular word;
proposer-tier only**
Status discipline: the canonical node remains **OPEN**; no completion status is licensed; no
numerical exponent inference is used

## 1. Verdict

On the exact `p=0,u=1` critical subsequence, the heavy--heavy physical-position contingency is a
legal third relation.  It is not determined by the repaired singleton matching, the private-heavy
matching, or their two repair endpoints: swapping two heavy occurrences changes the contingency
while leaving all of those data fixed.

The most immediate growing carrier does not survive the required structural gate.  If `Z` is the
fixed double-centered, normalized heavy--heavy contingency, then

\[
 Z=F_1^*F_0
 \tag{1.1}
\]

for input-wise isometries `F_t` into the common physical-position space.  Consequently

\[
 \bigwedge^r Z=(\bigwedge^rF_1)^*(\bigwedge^rF_0),
 \tag{1.2}
\]

and every minor or fixed linear combination of minors is a fixed-middle tensor feature.  The
exterior degree `r=Theta(m^(1/3))` is not a pair-dependent middle law.

The first word which visibly uses all three relations also collapses.  Let `A` be the centered
repaired-singleton matching, `B` the centered heavy-label matching, `D=A-B`, and define the
rectangular word

\[
 T=ZD^*Z:U_0\longrightarrow U_1.
 \tag{1.3}
\]

Although `T` is nonlinear in the pair data and has variable singular spectrum, an exact
tensorization gives input-wise isometries `S_t` and one fixed signature `J` such that

\[
 \boxed{T=2h\,S_1^*JS_0,\qquad h=2(a-1).}
 \tag{1.4}
\]

Exterior functoriality then leaves every `wedge^r T` in the same fixed-middle family.  Thus this
first explicit three-relation word does **not** pass the node's nonfactorization gate.

There is also no hidden blockwise `sqrt(r)` physical-mask dilution.  Normalize
`W_r=wedge^r(T/2)`.  Its fiber norm is at most one and is exactly one on a legal family with `r`
disjoint active transpositions.  For every off-equality one-coordinate status

* heavy/heavy with different raw labels;
* heavy/singleton;
* singleton/heavy; and
* singleton/singleton with different raw labels,

on either the left or right physical side, there is a legal pair in the same family for which

\[
 \|W_r\|=\|W_r\,\widetilde\Delta_i\|=1.
 \tag{1.5}
\]

Here the mask is the actual scalar Schur mask on the presentation pair, so (1.5) identifies an
off-equality retained block, not merely a branch of the full one-point extension.  This kills any
claim that the exterior word has a uniform `1/sqrt(r)` attenuation at each physical query.

Equation (1.5) is deliberately a **fiberwise** statement.  It does not prove a norm ceiling for
an arbitrary signed sum of full orbitals, because different presentation-pair blocks may interfere
after normalized incidence.  A genuinely pair-dependent, noncommutative parent-mixing
coefficient could still exploit such interference.  No such coefficient is constructed here, so
the full-position node remains OPEN.

## 2. Exact legal subsequence and dimensions

Let `ell>=2` and set

\[
 k=\ell^3,\qquad a=k^2=\ell^6,\qquad d=k=\ell^3,
 \qquad m=d+1,\qquad q=4a,
 \tag{2.1}
\]

\[
 n=am,\qquad N=2n,\qquad r=\ell.
 \tag{2.2}
\]

Then

\[
 p=(n-a)-ad=0,\qquad u=q-4a+1=1,
 \tag{2.3}
\]

and

\[
 r=\Theta(m^{1/3}),\qquad a=\Theta(m^2),\qquad
 2r+4\le a.
 \tag{2.4}
\]

There are no long-heavy exclusion variables.  A uniform critical construction must work on this
infinite legal sequence.

For `t in {0,1}` and `sigma in {L,R}`, let

\[
 I_\sigma=[n]_\sigma,
 \qquad P_{t,\sigma}=[a]_{t,\sigma}
 \tag{2.5}
\]

be respectively the physical-position set and the addressed private-heavy block set.  Put

\[
 P_t=P_{t,L}\sqcup P_{t,R},\qquad
 U_{t,\sigma}=\mathbf1^\perp\subset\mathbb R^{P_{t,\sigma}},
 \qquad U_t=U_{t,L}\oplus U_{t,R}.
 \tag{2.6}
\]

Thus

\[
 \dim U_t=h=2(a-1),
 \qquad
 \dim\bigwedge^rU_t={h\choose r}.
 \tag{2.7}
\]

The two sides are kept separate in (2.6); no `r`-to-one supercoordinate grouping is made.

## 3. The minimal heavy--heavy full-position relation

For completeness, the full side-`sigma` physical relation is the label contingency

\[
 C_\sigma(v,w)
 =|\{i\in I_\sigma:
       \widetilde x_{1,\sigma}(i)=v,
       \widetilde x_{0,\sigma}(i)=w\}|,
 \tag{3.0}
\]

with YES-label rows, NO-label columns, and one edge for every physical position.  The pair
`(C_L,C_R)`, modulo the simultaneous type-preserving palette gauge, is the complete full-position
relation classified in the preceding orbit memo.  The construction below takes its smallest
growing regular subrelation: the private-heavy/private-heavy block on each separately typed side.

For a presentation `\widetilde x_t`, let

\[
 H_{t,\sigma}(u)
 =\{i\in I_\sigma:\widetilde x_{t,\sigma}(i)
          \text{ is the private-heavy label addressed by }u\}.
 \tag{3.1}
\]

At `p=0`,

\[
 |H_{t,\sigma}(u)|=d
 \tag{3.2}
\]

and the `a` sets in (3.1) are disjoint.  They leave exactly the `a` singleton positions on that
side.  Define the raw heavy--heavy contingency

\[
 M_\sigma(\widetilde x_1,\widetilde x_0)[u,v]
 =|H_{1,\sigma}(u)\cap H_{0,\sigma}(v)|,
 \tag{3.3}
\]

with exact type

\[
 M_\sigma:\mathbb R^{P_{0,\sigma}}
       \longrightarrow\mathbb R^{P_{1,\sigma}}.
 \tag{3.4}
\]

Let

\[
 E_{t,\sigma}:\mathbb R^{P_{t,\sigma}}\longrightarrow
               \mathbb R^{I_\sigma},
 \qquad
 E_{t,\sigma}|u\rangle
 ={1\over\sqrt d}\mathbf1_{H_{t,\sigma}(u)}.
 \tag{3.5}
\]

The disjointness and (3.2) give

\[
 E_{t,\sigma}^*E_{t,\sigma}=I_a,
 \qquad
 {1\over d}M_\sigma=E_{1,\sigma}^*E_{0,\sigma}.
 \tag{3.6}
\]

Write `Q_(t,sigma)=I-J/a` and restrict to `U_(t,sigma)`.  The normalized centered relation is

\[
 Z_\sigma
 ={1\over d}Q_{1,\sigma}M_\sigma Q_{0,\sigma}
 =F_{1,\sigma}^*F_{0,\sigma}:
 U_{0,\sigma}\longrightarrow U_{1,\sigma},
 \tag{3.7}
\]

where `F_(t,sigma)=E_(t,sigma)|_(U_(t,sigma))` is an isometry.  Put

\[
 Z=Z_L\oplus Z_R=F_1^*F_0:U_0\longrightarrow U_1.
 \tag{3.8}
\]

### 3.1 Exact covariance

An address-gauge reindexing

\[
 g_t=g_{t,L}\oplus g_{t,R}
 \in S_a^{(L)}\times S_a^{(R)}
 \tag{3.9}
\]

precomposes `F_t` by `g_t^*`.  Therefore

\[
 Z\longmapsto g_1Zg_0^*.
 \tag{3.10}
\]

A common physical coordinate permutation acts on the left of both occurrence embeddings and
cancels in `F_1^*F_0`.  A common alphabet relabeling only reindexes the addressed fibers.  Hence
(3.3) is a legal full-orbit relation and (3.10) is its complete presentation-gauge covariance.

### 3.2 It is not old two-matching data

Fix both repaired singleton and private-heavy matchings, every repair endpoint, every singleton
position, and the entire right side.  On the left, choose two heavy blocks `u!=v`.  Start with

\[
 H_{1,L}(u)=H_{0,L}(u),\qquad
 H_{1,L}(v)=H_{0,L}(v).
 \tag{3.11}
\]

Swapping one YES heavy occurrence of `u` with one YES heavy occurrence of `v` preserves all input
histograms and all address-label matchings, but changes the selected contingency block from

\[
 \begin{pmatrix}d&0\\0&d\end{pmatrix}
 \quad\hbox{to}\quad
 \begin{pmatrix}d-1&1\\1&d-1\end{pmatrix}.
 \tag{3.12}
\]

Thus `M_L`, and hence the pair `(M_L,M_R)`, cannot be reconstructed from the two matchings plus
their two endpoints.  The third relation passes the data-independence gate.

## 4. Exterior minors fail the structural carrier gate

For every `0<=s<=h`, exterior functoriality applied to (3.8) gives

\[
 \boxed{
 \bigwedge^s Z
 =(\bigwedge^sF_1)^*(\bigwedge^sF_0):
 \bigwedge^sU_0\longrightarrow\bigwedge^sU_1.
 }
 \tag{4.1}
\]

Every `s by s` minor is a matrix entry of (4.1), by Cauchy--Binet.  A fixed linear combination of
minors inserts only a fixed middle matrix on the ambient exterior-position carrier.  Tensoring
independent left and right minors gives the tensor product of two factorizations (4.1).

Consequently all of the following remain fixed-middle carriers:

* raw heavy--heavy minors;
* the fixed double-centered minors (3.7);
* exterior characters, determinants, and fixed sums of minors;
* tensor products or fixed direct sums of their left/right copies.

The fact that `M_sigma` is genuine new pair data does not turn its fixed-centered exterior power
into a pair-dependent middle law.  This is an exact structural FAIL before any exponent can be
credited.

## 5. First explicit three-relation rectangular word

Let `mathcal A` be the common repaired singleton palette and
`mathcal B=mathcal B_L disjoint-union mathcal B_R` the common private-heavy palette.  The input-wise
address maps restricted to the centered side spaces are isometries

\[
 L_t:U_t\longrightarrow\mathbb R^{\mathcal A},
 \qquad
 B_t:U_t\longrightarrow\mathbb R^{\mathcal B}.
 \tag{5.1}
\]

Their centered cross-input matchings are

\[
 A=L_1^*L_0:U_0\longrightarrow U_1,
 \qquad
 B=B_1^*B_0:U_0\longrightarrow U_1.
 \tag{5.2}
\]

The repaired singleton map may cross the two physical sides; this causes no type problem because
`L_t` embeds the already centered direct sum `U_t` into the common `2a`-label palette.  The heavy
map is side respecting.  Put

\[
 D=A-B:U_0\longrightarrow U_1.
 \tag{5.3}
\]

Under (3.9),

\[
 A,B,D\longmapsto g_1(A,B,D)g_0^*.
 \tag{5.4}
\]

The shortest rectangular word with two full-position edges and one matching-difference return is

\[
 \boxed{
 T=ZD^*Z:U_0\longrightarrow U_1.
 }
 \tag{5.5}
\]

It uses the repaired singleton matching, the heavy matching, and the full physical-position
contingency.  Its covariance follows without an omitted middle gauge:

\[
 T\longmapsto g_1Tg_0^*.
 \tag{5.6}
\]

It is not recoverable from `A,B` because changing (3.12) changes `Z` while holding `A,B` fixed.
The remaining question is whether the *operator law* (5.5), rather than merely its input data, is
outside fixed-middle transport.

## 6. Exact tensorization of the apparent nonlinear word

Work over the real spaces above; the unitary version only adds conjugate carriers.  Fix compatible
orthonormal block bases `(e_(t,j))_(j=1)^h` of `U_t`.  For `C_t=L_t` or `C_t=B_t`, let

\[
 \mathcal F_C=
 \mathbb R^{I_L\sqcup I_R}\otimes
 \mathbb R^{\mathcal C}\otimes
 \mathbb R^{I_L\sqcup I_R}.
 \tag{6.1}
\]

The row and column feature maps have deliberately opposite first/third orientations:

\[
 \mathcal R_{1,C}y
 =\sum_{j=1}^h
   F_1y\otimes C_1e_{1,j}\otimes F_1e_{1,j},
 \qquad
 \mathcal R_{1,C}:U_1\longrightarrow\mathcal F_C,
 \tag{6.2a}
\]

\[
 \mathcal R_{0,C}x
 =\sum_{j=1}^h
   F_0e_{0,j}\otimes C_0e_{0,j}\otimes F_0x,
 \qquad
 \mathcal R_{0,C}:U_0\longrightarrow\mathcal F_C.
 \tag{6.2b}
\]

Here `mathcal C=mathcal A` in the singleton term and `mathcal C=mathcal B` in the heavy term.
Since `F_t` and `C_t` are isometries,

\[
 \mathcal R_{t,C}^*\mathcal R_{t,C}=hI_{U_t}.
 \tag{6.3}
\]

Expanding one matrix coefficient of (6.2) gives the exact contraction

\[
 \mathcal R_{1,C}^*\mathcal R_{0,C}
 =Z(C_0^*C_1)Z.
 \tag{6.4}
\]

The right side is `ZA^*Z` for `C=L` and `ZB^*Z` for `C=B`.  Define

\[
 S_t={1\over\sqrt{2h}}
 (\mathcal R_{t,L}\oplus\mathcal R_{t,B}),
 \qquad
 J=I_{\mathcal F_L}\oplus(-I_{\mathcal F_B}).
 \tag{6.5}
\]

Then `S_t` is an isometry into the fixed direct-sum tensor carrier and

\[
 \boxed{
 S_1^*JS_0={1\over2h}(ZA^*Z-ZB^*Z)
 ={1\over2h}T.
 }
 \tag{6.6}
\]

This is stronger than observing that the singular values of `T` vary.  The apparently nonlinear
three-relation word is an input-wise isometric compression of one fixed signature.  Moreover,

\[
 \bigwedge^sT
 =(\bigwedge^sS_1)^*
   \bigwedge^s(2hJ)
  (\bigwedge^sS_0),
 \tag{6.7}
\]

so growing exterior degree does not escape.  Formula (6.6) is the structural kill for (5.5).

## 7. Exact unmasked fiber norm

Since `F_t,L_t,B_t` are isometries,

\[
 \|Z\|\le1,
 \qquad \|A\|\le1,
 \qquad \|B\|\le1,
 \qquad \|D\|\le2.
 \tag{7.1}
\]

Therefore

\[
 \left\|{T\over2}\right\|\le1,
 \qquad
 W_r:=\bigwedge^r(T/2),
 \qquad
 \|W_r\|\le1.
 \tag{7.2}
\]

The bound is sharp on the legal subsequence.  Choose `2r` ordinary heavy blocks, disjoint from
the two repair endpoints and from four spectator blocks.  Make the YES and NO heavy-position
partitions identical on those `2r` blocks, so `Z` is the identity on their centered span.  Let
the heavy matching `B` be the identity there and let

\[
 A=BR,
 \qquad
 R=(1\ 2)(3\ 4)\cdots(2r-1\ 2r)
 \tag{7.3}
\]

on the active blocks.  The repaired singleton matching can realize (7.3) away from its two defect
endpoints.  On the `r` orthonormal antisymmetric vectors

\[
 f_j={e_{2j-1}-e_{2j}\over\sqrt2},
 \tag{7.4}
\]

one has

\[
 Zf_j=f_j,
 \qquad Df_j=-2Bf_j,
 \qquad \left|{T\over2}f_j\right|=|f_j|.
 \tag{7.5}
\]

Thus the wedge `f_1 wedge ... wedge f_r` is a unit singular vector and

\[
 \boxed{\|W_r\|=1.}
 \tag{7.6}
\]

This is an exact finite-parameter identity for every `ell>=2`, not a fitted exponent.

## 8. Physical one-coordinate mask ledger

For a physical coordinate `i` on side `sigma`, define the lifted scalar mask

\[
 \widetilde\Delta_i(\widetilde x_1,\widetilde x_0)
 =\mathbf1[\widetilde x_{1,\sigma}(i)
            \ne\widetilde x_{0,\sigma}(i)].
 \tag{8.1}
\]

It multiplies the entire operator block `W_r(tilde x_1,tilde x_0)`.  At `p=0`, the complete
value-status table is

| YES role at `i` | NO role at `i` | raw labels | `widetilde Delta_i` |
|---|---|---|---:|
| heavy | heavy | equal | 0 |
| heavy | heavy | different | 1 |
| heavy | singleton | necessarily different | 1 |
| singleton | heavy | necessarily different | 1 |
| singleton | singleton | equal | 0 |
| singleton | singleton | different | 1 |

The table is identical on `L` and `R`.  There are no public/excluded long occurrences on this
subsequence.

Keep the active `2r` blocks of Section 7 away from the queried spectator block(s).

1. **Heavy/heavy, different labels.**  Keep the heavy-position partitions aligned.  On two
   spectator blocks let `A` and `B` share the same transposition, so `D` has no additional active
   direction there, while the raw heavy labels at the same physical position are different.
2. **Singleton/singleton, different labels.**  Keep the heavy-position partitions aligned and use
   the same spectator transposition in the repaired singleton and heavy matchings.  At a common
   singleton position the two singleton values are different, while the active word is unchanged.
3. **Heavy/singleton.**  Inside one inactive block, interchange which of two physical positions is
   the singleton in the NO presentation while keeping it heavy in the YES presentation.  All
   active heavy fibers and all matrices on the span of (7.4) remain unchanged.
4. **Singleton/heavy.**  Reverse the preceding interchange.

All four modifications are legal histogram-preserving position permutations.  They do not touch
the unique YES collision endpoints, and they can be performed on either physical side.  In every
case (7.5)--(7.6) remain exact and the queried values differ.  Hence the actual off-equality Schur
block satisfies

\[
 \boxed{
 \|W_r(\widetilde x_1,\widetilde x_0)\|
 =\|\widetilde\Delta_i(\widetilde x_1,\widetilde x_0)
        W_r(\widetilde x_1,\widetilde x_0)\|=1.
 }
 \tag{8.2}
\]

For the two equal-label rows of the table, the physical Schur mask is zero by definition.  Thus
the exact worst off-equality **fiber** attenuation of this exterior word is one, not
`1/sqrt(r)`.

Equation (8.2) rules out a proof which tries to bound every masked coefficient block by
`O(1/sqrt(r))` times its unmasked block.  It does not compare the norm of the full unmarked signed
orbital sum to the norm of its full masked sum.  A global cancellation law in the noncommutative
one-point orbital system is outside this audit.

## 9. `C/uC` incidence and outer-coordinate accounting

Let

\[
 \pi_t:\mathcal Y_t\longrightarrow X_t
 \tag{9.1}
\]

be the exact addressed-presentation maps.  Their fibers have sizes

\[
 c_0=C,\qquad c_1=uC,
 \tag{9.2}
\]

and the normalized coisometries are

\[
 R_0=C^{-1/2}Q_0,
 \qquad R_1=(uC)^{-1/2}Q_1.
 \tag{9.3}
\]

On (2.1)--(2.3),

\[
 u=1,\qquad C=(a!)^2,
 \tag{9.4}
\]

so a scalar presentation-pair coefficient descends with exact entry factor `1/C`.  In general the
factor is `1/(C sqrt(u))`.

The gauge orbit of the contingency (3.3), every gauge-invariant closed contraction of (5.5), and
the physical mask (8.1) are constant on the corresponding pair of presentation fibers once the
underlying physical inputs are fixed.  Thus for every gauge-invariant scalar contraction `f` of
the word and every correctly typed lifted kernel `widetilde Gamma`,

\[
 R_1(\widetilde\Gamma\circ f)R_0^*
 =(R_1\widetilde\Gamma R_0^*)\circ f,
 \tag{9.5}
\]

\[
 (R_1\widetilde\Gamma R_0^*)\circ\Delta_i
 =R_1(\widetilde\Gamma\circ\widetilde\Delta_i)R_0^*.
 \tag{9.6}
\]

No equal-fiber normalization is used.  The operator-valued `T` itself is gauge covariant rather
than scalar invariant; to obtain a full-orbit scalar adversary it must be contracted with a
covariant outer carrier or by a gauge-invariant closed word.  Formula (6.6) shows that every fixed
tensor contraction of the displayed exterior construction remains fixed-middle.  Retaining the
exterior fiber as a query-invisible free ancilla would not be a new lower bound and is not
credited here.

The full relation retains all `a` block coordinates on both sides and performs no grouping, so it
does not incur the earlier `a -> a/r` supercoordinate loss.  This passes only the combinatorial
coordinate-count gate.  No calculation here proves that an outer `UIC_a` numerator survives the
gauge contraction (9.5); therefore no `a^(2/3)` numerator is claimed.

## 10. Scope boundary

The scoped **FAIL** covers:

* the infinite exact `p=0,u=1` subsequence (2.1)--(2.3);
* raw or fixed double-centered heavy--heavy `L/R` contingencies;
* every exterior power, minor, determinant, or fixed linear combination of those minors;
* their fixed direct sums and tensor products across the two physical sides;
* the explicit three-relation rectangular word `T=Z(A-B)^*Z`;
* every exterior power of that word;
* the hoped-for blockwise `sqrt(r)` attenuation at `r=Theta(m^(1/3))`;
* all six heavy/singleton and equality/off-equality one-coordinate statuses on both sides;
* exact normalized incidence factors `C/uC` for scalar contractions;
* non-circularity: all displayed maps are explicit occurrence, label, and exterior operators and
  embed no copy of the critical donor.

It does **not** cover:

* an arbitrary signed coefficient in the full position-incidence orbital basis;
* a genuinely non-simultaneously-diagonalizable parent-mixing block after one physical mark;
* a pair-dependent nonlinear recentering or normalization not generated by fixed tensor
  contractions of (3.3), (5.1), and (5.5);
* a proof that the outer `a^(2/3)` numerator survives exact incidence;
* the `p>0,u>1` remainder/exclusion statuses required by any different uniform formula;
* the whole canonical node or the critical endpoint.

No new successor ansatz is tested in this memo.  The only remaining escape named here is the
already recorded noncommutative parent-mixing condition inside the registered full-position node.

## 11. Gate ledger

| Obligation | Outcome |
|---|---|
| exact endpoint | infinite `p=0,u=1` subsequence, (2.1)--(2.4) |
| row/codomain heavy-block fibers | `P_(0,sigma)` and `P_(1,sigma)`, both size `a` |
| physical position fibers | `I_sigma`, size `n`; heavy fibers size `d` |
| genuine third relation | PASS by the fixed-old-data swap (3.11)--(3.12) |
| full orbit covariance | exact gauge law (3.10) |
| centered contingency carrier | fixed-middle Gram, (4.1) |
| first three-relation rectangular word | explicit `T=Z(A-B)^*Z`, (5.5) |
| structural nonfactorization | **FAIL**, exact tensorization (6.6) |
| exterior degree | `r=Theta(m^(1/3))`, dimension `binom(2a-2,r)` |
| exact unmasked fiber norm | at most one and attained, (7.2)--(7.6) |
| left/right `HH`, `HS`, `SH`, `SS` masks | complete status table; every off-equality type retains norm one |
| hoped-for blockwise `sqrt(r)` dilution | **FAIL**, (8.2) |
| incidence fiber sizes | `C,uC`; exact factor `1/(C sqrt(u))` |
| outer coordinate count | all `Theta(a)` blocks retained; no grouping |
| outer `a^(2/3)` numerator | unproved |
| recursive critical donor | absent |
| numerical exponent inference | none |
| completion status | none; independent review absent |

## 12. Sources and bottom line

Frozen inputs used here:

* `ksum/artifacts/ksum_L3_critical_full_position_incidence_orbit_classification_20260722.md` for the
  complete transportation-orbit parameter and exact incidence pull-through, corrected SHA-256
  `A22D513B66D50635E76C6A2707AC3FC5EE657676FFEEA0C0B68B9EE6EDC2A088`;
* `ksum/artifacts/ksum_L3_critical_full_position_mask_obstruction_audit_20260722.md` for the exact
  one-query Fourier typing and the fixed-centered exterior branching ceiling, SHA-256
  `19521DEB54082A37553F6D98075F33DD2095FE6307DBACDEA0121D18927AA315`;
* `ksum/artifacts/ksum_L3_critical_coupled_uic_address_cycle_attempt_20260721.md`, corrected SHA-256
  `A380DCA5527DD229B18C747E3EDC6EFC414094CE1357631F4AF8BEE4A461EC32`, for the `C/uC`
  rectangular normalization;
* `ksum/artifacts/ksum_L3_critical_cycle_word_factorization_audit_20260722.md`, SHA-256
  `25B023FE5E0A3E2665D393C98B5F70B9DB0571F16C769AB24B89D7B85F721535`, for the old
  two-matching boundary;
* `ksum/artifacts/ksum_L3_critical_lr_multiplicity_mixing_audit_20260722.md`, SHA-256
  `06E4FB71D02D96460A0917B2B882BA3CC30B7821D9C35ED2FB6D6461F09E3503`, for the fixed-middle
  partial-trace comparison;
* `ksum/artifacts/ksum_L3_critical_sparse_delocalized_multiblock_attempt_20260722.md`, SHA-256
  `511356C36D03A320365A252DDB89923990BB6630A52F5FE23F29D747D22C9D7A`, for the independent
  `P/Q` one-coordinate cut and outer-coordinate accounting.

The physical-position contingency is real new pair data, so the third relation itself exists.
But the obvious growing carriers built from fixed centering, minors, exterior powers, and the
first cubic three-relation word all tensorize to input-wise fixed-middle features.  Their apparent
`r`-dimensional freedom is not a new post-incidence selector.

Moreover, every actual off-equality role has a legal norm-one retained fiber, so no blockwise
`sqrt(r)` mask dilution is present.  The remaining live problem is not to choose a larger minor;
it is to find a genuinely pair-dependent signed law whose **global off-equality one-point Fourier
blocks** cancel in a growing noncommutative parent system while the same block preserves the outer
`a^(2/3)` numerator.  This memo does not supply that law.
