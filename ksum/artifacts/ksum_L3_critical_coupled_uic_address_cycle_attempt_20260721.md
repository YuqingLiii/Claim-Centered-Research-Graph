# L3 critical endpoint: coupled UIC/address-cycle incidence audit and pointed-hook ceiling

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel`  
Status of this memo: **PARTIAL** for the registered coupled family; **FAIL** for the minimal
pointed-hook/cycle-touching law below; proposer-tier only; no DAG/status edit

## 1. Verdict

This pass obtains two exact results and one scoped obstruction.

1. The incidence maps from addressed `UIC o pSearch` copies to the full YES and NO orbits are now
   type-correct.  If `u=q-4a+1 in {1,2,3,4}`, a NO input has `C` addressed presentations while a
   YES input has `uC`.  The extra factor on the YES side is the choice of which one of its `u`
   unused labels is the unused member of the outer `UIC` alphabet.  This is exactly what reconciles
   the outer-orbit ratio `a^2` with the full-orbit ratio `a^2/u`.
2. Normalized incidence compression commutes exactly with every physical query mask.  In
   particular, the full rectangular matrix has entries with normalization `1/(C sqrt(u))`; using
   the same normalization on both answer classes is ill-typed.
3. The smallest genuinely nonseparable law was tested analytically.  It lets the outer
   YES-to-NO transition choose one endpoint of the unique outer collision and uses the standard
   hook `[a-1,1]` matrix coefficient to ask whether the relative address cycle fixes that selected
   endpoint.  Its address kernel depends on the outer transition, so it is not
   `Gamma_UIC tensor K(address)`.  Nevertheless, a one-point-marked block retains at least an
   `(a-1)/a` fraction of its unmarked hook norm.  With the standard inner `pSearch_m` blocks, the
   entire family has the ceiling

   \[
   O\!\left(a^{2/3}\sqrt m\right)=O(N^{11/18})
   \tag{1.1}
   \]

   on an infinite exact critical subsequence.  It therefore supplies no part of the missing
   `m^(1/6)` factor.

The obstruction covers the pointed single-hook/character law, including one- or two-endpoint
versions and operator-valued outer coefficients.  It does **not** cover higher Specht sectors,
weights depending on the full length of the selected alternating cycle, or laws which alter the
occurrence-level inner operators jointly across several address cycles.  The full coupled node and
the critical endpoint remain open.

## 2. Frozen notation and the two orbit ratios

Each side of the target input has length `n`, and `N=2n`.  Put

\[
 a=\lfloor q/4\rfloor,\qquad
 d=\left\lfloor{n-a\over a}\right\rfloor,\qquad
 p=(n-a)-ad,\qquad
 m=d+1,
\tag{2.1}
\]

and

\[
 u:=q-4a+1\in\{1,2,3,4\}.
\tag{2.2}
\]

Let `X_0` and `X_1` be the exact full NO and YES orbits from the critical hidden-frequency
promise.  The stabilizer calculation in the orbit-intertwiner memo gives

\[
 {|X_1|\over |X_0|}={a^2\over u}.
\tag{2.3}
\]

Let `U_0,U_1` be the two answer classes of the outer `UIC_a` problem on two injective lists of
length `a` over an alphabet of size `2a`.  Direct counting gives

\[
 |U_0|=(2a)!,
\tag{2.4}
\]

because a NO pair is an ordering of a partition of all `2a` labels, and

\[
 |U_1|
 =a^2(2a)(2a-1)(2a-2)!
 =a^2(2a)!.
\tag{2.5}
\]

For (2.5), choose the two collision positions, the common label, the one unused label, and then
biject the remaining `2a-2` labels to the remaining positions.  Thus

\[
 {|U_1|\over|U_0|}=a^2.
\tag{2.6}
\]

Let `H_t` be the exact addressed source class

\[
 H_t=U_t\circ(\mathrm{pSearch}_m)^{2a},
\tag{2.7}
\]

including the fixed public coordinates for the `p` long heavy labels on each side.  Each fixed
outer input has `m^(2a)` choices for the locations of its non-star symbols, and the public
coordinates add no choices.  Consequently

\[
 {|H_1|\over|H_0|}=a^2.
\tag{2.8}
\]

Equations (2.3) and (2.8) are different.  The rectangular incidence maps must account for that
difference.

## 3. Exact addressed-copy incidence maps

### 3.1 Presentation sets and fiber sizes

Take the orbit, under

\[
 G=S_n^{(L)}\times S_n^{(R)}\times S_q,
\tag{3.1}
\]

of one fixed legal embedding of (2.7) into the full critical promise.  Quotient only by
automorphisms that act identically on both answer classes.  Denote the resulting finite multiset
of source copies by `E`.  Define

\[
 \mathcal Y_t:=\{(e,z):e\in E,\ z\in H_t\},
 \qquad
 \pi_t(e,z):=e(z)\in X_t.
\tag{3.2}
\]

The action of `G` is transitive on `X_t`, so every fiber of `pi_t` has the same size; call it
`c_t`.  Counting (3.2) in two ways gives

\[
 |E||H_t|=c_t|X_t|.
\tag{3.3}
\]

Using (2.3) and (2.8),

\[
 {c_1\over c_0}
 ={|H_1|/|H_0|\over |X_1|/|X_0|}
 ={a^2\over a^2/u}=u.
\tag{3.4}
\]

Write

\[
 c_0=C,\qquad c_1=uC.
\tag{3.5}
\]

There is a concrete reduced-address convention in which the common factor is

\[
 C=(a!)^2m^{2p}.
\tag{3.6}
\]

Indeed, on each side one chooses a bijection from the `a` singleton labels to the `a` private
heavy labels, and one excluded public occurrence for each of the `p` long heavy labels.  A YES
input has in addition `u` choices for the unused member of the outer `2a`-label pool.  Retaining
block orderings, palette orderings, or internal occurrence orderings multiplies both `C` and `uC`
by the same factor, so (3.4) and all normalized maps below are convention-independent.

### 3.2 Raw and normalized incidence operators

Let `Q_t` be the raw incidence matrix

\[
 (Q_t)_{x,(e,z)}={\bf1}[\pi_t(e,z)=x].
\tag{3.7}
\]

Its exact type and norm are

\[
 Q_0:\ell_2(\mathcal Y_0)\longrightarrow\ell_2(X_0),
 \quad \|Q_0\|=\sqrt C,
\tag{3.8}
\]

\[
 Q_1:\ell_2(\mathcal Y_1)\longrightarrow\ell_2(X_1),
 \quad \|Q_1\|=\sqrt{uC}.
\tag{3.9}
\]

Define the coisometries

\[
 R_0=C^{-1/2}Q_0,
 \qquad
 R_1=(uC)^{-1/2}Q_1.
\tag{3.10}
\]

Then

\[
 R_tR_t^*=I_{\ell_2(X_t)},
\tag{3.11}
\]

while `R_t^*R_t` is the orthogonal projection onto vectors constant on every presentation fiber.
The dimensions are

\[
 R_0\in\mathbb R^{|X_0|\times C|X_0|},
 \qquad
 R_1\in\mathbb R^{|X_1|\times uC|X_1|}.
\tag{3.12}
\]

For a lifted rectangular kernel

\[
 \widetilde\Gamma:\ell_2(\mathcal Y_0)\longrightarrow
                    \ell_2(\mathcal Y_1),
\tag{3.13}
\]

the corresponding full-orbit matrix is

\[
 \Gamma=R_1\widetilde\Gamma R_0^*:
 \ell_2(X_0)\longrightarrow\ell_2(X_1).
\tag{3.14}
\]

Entrywise, (3.14) is

\[
 \Gamma[x,y]
 ={1\over C\sqrt u}
 \sum_{\substack{\tilde x\in\pi_1^{-1}(x)\\
                  \tilde y\in\pi_0^{-1}(y)}}
 \widetilde\Gamma[\tilde x,\tilde y].
\tag{3.15}
\]

The factor `sqrt(u)` in (3.15) is forced.  Omitting it makes the YES incidence map have norm
`sqrt(u)` rather than one.

### 3.3 Exact query-mask identity

For a physical coordinate `i`, define on the presentation spaces

\[
 \widetilde\Delta_i[\tilde x,\tilde y]
 :={\bf1}[\pi_1(\tilde x)_i\ne\pi_0(\tilde y)_i].
\tag{3.16}
\]

Because (3.16) is constant on every pair of fibers, (3.15) gives the exact identity

\[
 \boxed{
 (R_1\widetilde\Gamma R_0^*)\circ\Delta_i
 =R_1(\widetilde\Gamma\circ\widetilde\Delta_i)R_0^*.
 }
\tag{3.17}
\]

This is the correct rectangular version of the marked one-point extension.  It also shows why a
square address kernel on one input fiber is not by itself an adversary: it supplies neither the
map (3.13) nor the image-dependent mask (3.16).

## 4. The exact critical subsequence used for the coefficient test

A uniform endpoint law must work on every legal integer remainder, so it is enough to test it on
an infinite `p=0,u=1` subsequence.  For every integer `k>=2`, take

\[
 a=k^2,\qquad q=4k^2,\qquad d=k,\qquad m=k+1,
 \qquad n=a(d+1)=k^2(k+1).
\tag{4.1}
\]

Then

\[
 p=(n-a)-ad=0,
 \qquad u=q-4a+1=1,
\tag{4.2}
\]

and

\[
 a=\Theta(N^{2/3}),\qquad
 m=\Theta(N^{1/3}),\qquad
 N=2am.
\tag{4.3}
\]

There are no long-exclusion variables on this subsequence.  The reduced address fiber is

\[
 \Omega=S_a^{(L)}\times S_a^{(R)},
 \qquad |\Omega|=(a!)^2.
\tag{4.4}
\]

Thus a failure of a matching-hook law here cannot be repaired uniformly by weights on long-heavy
exclusion flags.

## 5. The minimal genuinely coupled pointed-hook law

### 5.1 The hook coefficient

Let

\[
 V=\left\{z\in\mathbb C^a:\sum_{r=1}^a z_r=0\right\},
 \qquad \dim V=a-1,
\tag{5.1}
\]

with the standard permutation action `rho` of `S_a`.  For `j in [a]`, put

\[
 v_j=\sqrt{a\over a-1}
 \left(e_j-{1\over a}{\bf1}\right).
\tag{5.2}
\]

Then `||v_j||=1` and

\[
 \langle v_j,v_\ell\rangle=
 \begin{cases}
 1,&j=\ell,\\
 -1/(a-1),&j\ne\ell.
 \end{cases}
\tag{5.3}
\]

For two address copies `sigma,tau in S_a`, define

\[
 C_j(\sigma,\tau)
 :=\left\langle v_j,
   \rho(\sigma^{-1}\tau)v_j\right\rangle.
\tag{5.4}
\]

It equals `1` if the relative address permutation fixes `j`, and `-1/(a-1)` otherwise.  Hence it
is the smallest pointed alternating-cycle statistic: it distinguishes whether the cycle touching
the selected point has length one or length greater than one.  Unlike a central character, the
selected point may depend on the outer YES-to-NO transition.

### 5.2 The outer collision-transition selector

For an outer YES input `z_1`, let `(c_L,c_R)` be the two coordinates carrying its unique shared
label.  For every outer NO input `z_0`, at least one of these two coordinates changes value;
otherwise `z_0` would retain the same cross-list equality.  Define the transition selector

\[
 s(z_1,z_0)=
 \begin{cases}
 (L,c_L),&z_{1,L}(c_L)\ne z_{0,L}(c_L),\\
 (R,c_R),&\text{otherwise}.
 \end{cases}
\tag{5.5}
\]

The priority between the two sides is immaterial; (5.5) is equivariant under independent
coordinate permutations within each side, and its selected coordinate always lies in the outer
query-difference set.

Let `Gamma_out` be any outer `UIC_a` adversary coefficient matrix.  Split it into the two disjoint
transition sectors selected by (5.5).  On the sector `s(z_1,z_0)=(L,j)`, multiply its coefficient
by `C_j(sigma_L,tau_L)`; on the right sector use `C_j(sigma_R,tau_R)`.  The occurrence-level blocks
remain the exact BHK composition blocks `J_m` for unequal outer symbols and `mI_m` for equal outer
symbols.

Equivalently, before the incidence compression (3.14), the coefficient is

\[
 \widetilde\Gamma_{\rm hook}
 [ (z_1,\sigma),(z_0,\tau)]
 =\Gamma_{\rm comp}[z_1,z_0]\,
 C_{s(z_1,z_0)}(\sigma,\tau),
\tag{5.6}
\]

where `sigma=(sigma_L,sigma_R)`, `tau=(tau_L,tau_R)`, and the last factor uses the side and point
chosen in (5.5).  Formula (5.6) is genuinely nonseparable: two outer transitions selecting
different collision endpoints use different, nonproportional address matrices.  It cannot be
written as `Gamma_UIC tensor K(address)`.

A still more naive covariant law would use
`<v_c,rho(sigma^-1 tau)v_b>` when the transition itself transports `b` to `c`.  That coefficient
is identically one by equivariance and therefore collapses back to the separable addressed
witness.  The centered fixed-versus-moved coefficient (5.4) is the first nonconstant hook law.

## 6. Exact hook norm and its marked block

Let `G_a=S_a` and `D=a-1`.  Schur orthogonality for the irreducible hook representation gives

\[
 \|C_j\|={|G_a|\over D}={a!\over a-1}.
\tag{6.1}
\]

More explicitly, convolution by a matrix coefficient has one hook Fourier block equal to
`(|G_a|/D)|v_j><v_j|` and all other irreducible blocks zero.  Normalize it by

\[
 \overline C_j:={D\over |G_a|}C_j,
 \qquad \|\overline C_j\|=1.
\tag{6.2}
\]

Now mark the selected address point `j`.  Its stabilizer is

\[
 H_j=\operatorname{Stab}_{S_a}(j)\cong S_{a-1},
 \qquad |H_j|=(a-1)!.
\tag{6.3}
\]

The vector `v_j` is fixed by `H_j`; equivalently,

\[
 [a-1,1]\downarrow S_{a-1}
 =[a-1]\oplus[a-2,1],
\tag{6.4}
\]

and `v_j` spans the trivial summand.  The aligned `H_j x H_j` marked submatrix of `C_j` is the
all-ones matrix: every relative permutation fixes `j`.  It has norm `|H_j|`.  Therefore the
one-point-marked operator system contains a block of norm at least

\[
 {D\over|G_a|}|H_j|
 ={(a-1)(a-1)!\over a!}
 ={a-1\over a}.
\tag{6.5}
\]

Comparing (6.2) and (6.5), the exact address-layer advantage is bounded by

\[
 {\|\overline C_j\|
  \over\|\overline C_j^{\,\bullet}\|}
 \le {a\over a-1}<2.
\tag{6.6}
\]

This calculation is not a finite-spectrum inference.  It is the exact hook Fourier transform and
the exact point-stabilizer branch for every `a>=2`.

If both endpoints of the unique pair are given hook factors, the unmarked address norm is the
product of the two norms.  A query on one side leaves the other factor unchanged and invokes
(6.5) on the queried side, so the same bound (6.6) applies.  Direct sums of the left- and
right-selected sectors in (5.5) are orthogonal hook sectors under
`S_a^(L) x S_a^(R)` and do not create cross-sector cancellation.

The normalized rectangular incidence maps do not change this comparison.  If the hook component
is orthogonal to the fiber-constant ranges of `R_0^*` or `R_1^*`, its compressed numerator is zero.
If the outer hook coupling makes it survive, Schur orthogonality pairs the outer and address hooks
to the trivial full-orbit sector.  After a selected point is marked, (6.4) pairs the same outer
block with the trivial `H_j` summand, and (6.5) is retained.  The common incidence scalar, and the
`1/sqrt(u)` factor in (3.15), occur on both sides of the norm comparison.  Thus the candidate has
only the two possibilities: vanish under compression, or obey the constant ceiling (6.6).

## 7. Restoring the outer and inner operator factors

Let `B` denote the outer operator-valued block left after the exact hook Fourier transform.  The
hook label is only an ancilla attached to an outer `UIC` input.  Such an operator-valued adversary
cannot have a larger asymptotic ratio than ordinary `UIC_a`: duplicate each outer input by the
finite hook-ancilla index and let every query ignore that index.  The duplicated partial function
has exactly the same query complexity as `UIC_a`.  General-adversary optimality and the standard
`O(a^(2/3))` claw algorithm therefore give

\[
 {\|B\|\over\max_{r\in[2a]}\|B\circ\Delta_r\|}
 =O(a^{2/3}).
\tag{7.1}
\]

This argument allows arbitrary matrices on the hook multiplicity space; it is not limited to a
scalar outer coefficient.

For the exact BHK `pSearch_m` blocks, every unmasked inner block has norm `m`.  If physical query
`i` lies in the source block corresponding to a differing outer coordinate, the relevant masked
block has norm `sqrt(m-1)`.  Hence the unmarked and selected one-point-marked factors are

\[
 m^{2a}
 \quad\text{and}\quad
 \sqrt{m-1}\,m^{2a-1},
\tag{7.2}
\]

respectively.  The following makes the incidence step in the resulting ceiling explicit.

To make the incidence step explicit, fix a numerator-maximizing surviving hook block after
(3.14), and call its common normalized incidence scalar `s>=0`.  If `s=0`, this candidate has zero
numerator.  Otherwise the hook Fourier calculation and its aligned marked branch give, for the
outer block `B` carried by that sector,

\[
 \|\Gamma_{\rm hook}\|
 \le s\,\|B\|m^{2a},
 \qquad
 \max_i\|\Gamma_{\rm hook}\circ\Delta_i\|
 \ge s\,{a-1\over a}
       \max_r\|B\circ\Delta_r\|
       \sqrt{m-1}\,m^{2a-1}.
\tag{7.3}
\]

The same `s` occurs because (3.17) uses the same two normalized incidence maps; the selected
outer coordinate differs by construction (5.5), and the `H_j x H_j` branch in (6.5) is contained
in that one-point extension.  Thus no lower bound on an arbitrary compressed lift is being
assumed here: (7.3) is the explicit surviving/vanishing dichotomy for the pointed-hook sector.
Combining (6.6), (7.1), and (7.2) now gives

\[
 {\|\Gamma_{\rm hook}\|
  \over\max_i\|\Gamma_{\rm hook}\circ\Delta_i\|}
 \le
 O\!\left(
 {a\over a-1}
 {m\over\sqrt{m-1}}
 a^{2/3}
 \right)
 =O(a^{2/3}\sqrt m).
\tag{7.4}
\]

If the query-masked norms are normalized to at most one, (7.4) says

\[
 \|\Gamma_{\rm hook}\|=O(a^{2/3}\sqrt m).
\tag{7.5}
\]

On the exact subsequence (4.1),

\[
 a^{2/3}\sqrt m=\Theta(N^{11/18}),
\qquad
 a^{2/3}m^{2/3}=\Theta(N^{2/3}).
\tag{7.6}
\]

Thus the pointed hook returns precisely the addressed exponent and misses the target by
`m^(1/6)=N^(1/18)`.

## 8. What the type audit rules out

The calculation identifies three distinct mistakes that a future formula must avoid.

1. **Equal fiber normalizations.**  The YES and NO presentation fibers differ by `u`; the exact
   full-orbit entry is (3.15), not an average with denominator `C` on both sides.
2. **An untyped relative cycle.**  A cycle type between a YES presentation and a NO presentation is
   not canonical until the source-copy transition identifies their block indices.  Formula (5.5)
   supplies such an identification.  Writing only `theta(alpha,beta)` without the transition data
   does not define a scalar on the rectangular domain (3.13).
3. **Covariant transport mistaken for interference.**  If the outer transition transports the
   selected hook vector exactly, its matrix coefficient is one.  The first nonconstant centered
   alternative is (5.4), but its point-stabilizer branch has almost the full unmarked norm by
   (6.5).  It creates no growing marked/unmarked separation.

## 9. Coverage boundary

The **FAIL** verdict applies to the following declared subfamily:

* the exact critical promise on the infinite legal `p=0,u=1` sequence (4.1);
* one or both standard-hook `[a-1,1]` factors on the left/right relative address permutations;
* diagonal hook matrix coefficients, the pointed fixed-versus-moved character, and finite direct
  sums over collision-transition sectors;
* arbitrary operator-valued outer `UIC` coefficients;
* the standard occurrence-level BHK blocks `J_m` and `mI_m`.

It does **not** establish a ceiling for:

* higher Specht sectors, especially diagrams whose depth grows with `a` or `m`;
* a weight depending on the entire length or colored word of the alternating cycle containing the
  selected unique-pair edge, rather than only its hook/fixed-point component;
* a coefficient that changes the occurrence-level inner matrices jointly on several blocks, so
  that (7.2) is no longer the BHK tensor block;
* full colored double-coset data involving cross-input position-incidence graphs beyond the
  relative matching permutation.

These are untested variants inside the already registered coupled family, not conclusions of this
memo and not newly commissioned routes.

## 10. Gate ledger

| Obligation | Outcome |
|---|---|
| exact addressed-copy domains/codomains | closed by (3.2), (3.12), and (3.13) |
| orbit-size imbalance | `c_1/c_0=u`; exact normalization `1/(C sqrt(u))` |
| exact compression/query identity | closed by (3.17) |
| genuinely nonseparable coefficient | explicit pointed hook (5.5)--(5.6) |
| exact unmarked hook norm | `a!/(a-1)` by Schur orthogonality |
| exact marked hook branch | at least `(a-1)/a` after unit normalization |
| extra `m^(1/6)` | **FAIL for the pointed-hook family** |
| best ratio in tested family | `O(a^(2/3) sqrt(m))=O(N^(11/18))` |
| higher-character/full-cycle coupled law | untested |
| full endpoint `Omega(N^(2/3))` adversary | not obtained and not refuted |
| numerical spectra | none used |
| DAG/status edit | none |

## 11. Source ledger

* Exact orbit sizes, stabilizers, double-coset types, marked query system, and BHK block norms:
  `ksum/artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md`.
* Exact frozen promise, addressed `UIC o pSearch` restriction, and the
  `Omega(a^(2/3)sqrt(m))` baseline:
  `ksum/artifacts/ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md`.
* Standalone square address-kernel typing and its constant marked/unmarked ceiling:
  `ksum/artifacts/ksum_L3_critical_signed_cycle_weight_attempt_20260721.md`.

## 12. Bottom line

The rectangular lift is now well typed: the source-copy fibers are `C` on NO and `uC` on YES,
and normalized incidence compression commutes exactly with physical query masks.  This removes the
previous ambiguity about orbit-size imbalance and shows precisely where any coupled coefficient
must live.

The first genuinely nonseparable coefficient does not work.  Coupling the outer unique-collision
transition to the standard address hook changes the formula, but not the exponent.  The selected
hook vector becomes a trivial vector for the one-point stabilizer, leaving an aligned marked block
of relative norm `(a-1)/a`; after the tight outer `UIC` ratio and the inner `pSearch` mask are
restored, the construction is capped at `N^(11/18)`.

Any successful continuation within this node must therefore use information beyond a single
pointed hook: a growing higher-character/cycle-length sector or a coefficient that couples several
address cycles to the occurrence-level inner blocks.  This memo supplies no evidence that such a
law exists.
