# L3 critical endpoint: full Young-rank balanced-harmonic feasibility audit

Date: 2026-07-22
Canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.full-young-rank-balanced-harmonic-kernel`
Status discipline: proposer-tier exact feasibility audit; **no `PROVED`, `REFUTED`, or
`CERTIFIED*` claim**

## 1. Exact decision

The first gate fails.  A scalar harmonic of the Young down-incidence matrix is not a physical
one-coordinate kernel for this promise.

On the stable `p=0,u=1` endpoint, the proposed one-side module is

\[
 \mathcal M_{a,d}
 =\operatorname {Ind}_{S_a\times(S_d\wr S_a)}^{S_n}{\bf1},
 \qquad
 \operatorname {ch}\mathcal M_{a,d}=h_a h_a[h_d],
 \tag{1.1}
\]

but with an essential qualification: (1.1) is the **unlabeled, or alphabet-trivial, position
module**.  It is not the position orbit with the raw singleton and heavy labels held fixed.  The
raw fixed-label module is larger and has characteristic `h_1^a h_d^a`.

After one coordinate is fixed, the literal restriction of (1.1) is

\[
 \mathcal M_{a,d}\!\downarrow S_{n-1}
 \cong \mathcal M^{\rm sing}_{a,d}\oplus\mathcal M^{\rm heavy}_{a,d},
 \tag{1.2}
\]

where

\[
 \operatorname {ch}\mathcal M^{\rm sing}_{a,d}
 =h_{a-1}h_a[h_d],
 \qquad
 \operatorname {ch}\mathcal M^{\rm heavy}_{a,d}
 =h_a h_{d-1}h_{a-1}[h_d].
 \tag{1.3}
\]

At an `S_(n-1)` type `beta`, the parent-origin multiplicity is the orthogonal direct sum

\[
 \mathcal R_\beta
 =\bigoplus_{\lambda:\,\beta\nearrow\lambda}
   \mathcal B_{\beta\lambda}\otimes Z_\lambda,
 \qquad
 \dim\mathcal B_{\beta\lambda}=1,
 \tag{1.4}
\]

not one scalar copy indexed only by `beta`.  Here
`Z_lambda=(S^lambda)^(S_a x (S_d wr S_a))`.  The literal restriction of a full-group multiplier is
parent diagonal on (1.4).  It never applies the codiagonal which sends the different parent copies
to the same scalar.

Consequently the normalized scalar Young map

\[
 \mathscr D_n e_\lambda
 =\sum_{\beta\nearrow\lambda}
   \sqrt{f^\beta/f^\lambda}\,e_\beta
 \tag{1.5}
\]

is an aggregate obtained only after forgetting the spaces `Z_lambda` and summing the mutually
orthogonal summands in (1.4).  A vector in `ker \mathscr D_n` need not have even a small literal
restriction.  In the natural direct-sum norm its parent branches do not cancel at all.

There is a stronger physical no-go for the exact sector represented by (1.1).  Let `P_t` be the
projection of the exact answer space onto the trivial alphabet irrep `nu=(q)`.  For every left or
right physical coordinate `i`, every operator `Gamma=P_1 Gamma P_0` satisfies

\[
 \boxed{
 P_1(\Gamma\circ\Delta_i)P_0
   =\left(1-{1\over q}\right)\Gamma,
 \qquad
 \|\Gamma\circ\Delta_i\|
   \ge\left(1-{1\over q}\right)\|\Gamma\|.
 }
 \tag{1.6}
\]

At the endpoint `q=4a=4(m-1)^2`, the retained ratio is `1-O(m^(-2))`, whereas the desired
selector ratio is `O(m^(-1/6))`.  Equation (1.6) holds for arbitrary multiplicity matrices and
arbitrary parent support, not merely for a scalar cyclic family.

Thus a full-rank scalar Young harmonic is a spurious query mechanism.  A viable continuation
would need an additional, explicitly physical coupling: nontrivial raw-label/alphabet covariance
and status recoupling whose literal maps send several orthogonal parent occurrences into a common
marked channel.  The resulting same-label channel must then be evaluated on both answers and both
physical sides.  Merely writing a scalar incidence kernel, or tensoring it with an independent
payload, cannot provide the missing factor.

## 2. Frozen endpoint and what is being represented

Work on the infinite legal subsequence

\[
 a=k^2,\qquad d=k,\qquad m=d+1,\qquad
 n=a(d+1),\qquad q=4a,
 \tag{2.1}
\]

with integer `k>=2`.  Hence `p=0` and `u=1`.  On either physical side an input has `a` values of
frequency one and `a` values of frequency `d`; the remaining labels do not occur on that side.

Put

\[
 W_{r,d}=S_d\wr S_r=(S_d)^r\rtimes S_r.
 \tag{2.2}
\]

There are two different position modules which must not be conflated.

### 2.1 Raw labels held fixed

Fix named singleton labels `s_1,...,s_a` and named heavy labels `h_1,...,h_a`.  The `S_n` orbit of
strings having the prescribed multiplicities has stabilizer `(S_d)^a`: singleton coordinates are
fixed individually and only occurrences of the same named heavy value may be permuted.  Therefore

\[
 \mathcal M^{\rm raw}_{a,d}
 =\operatorname {Ind}_{(S_d)^a}^{S_n}{\bf1},
 \qquad
 \operatorname {ch}\mathcal M^{\rm raw}_{a,d}=h_1^a h_d^a.
 \tag{2.3}
\]

For a fixed coordinate, its singleton part has `a` raw-label orbits and its heavy part has `a`
raw-label orbits.  Accordingly

\[
 h_1^\perp(h_1^a h_d^a)
 =a h_1^{a-1}h_d^a
  +a h_1^a h_{d-1}h_d^{a-1}.
 \tag{2.4}
\]

Those raw-label copies are exactly the information needed by the equality test.  They disappear
from (1.1).

### 2.2 Unlabeled/alphabet-trivial position module

Let `Omega_(a,d)` consist of pairs `(A,Pi)` where `A subseteq [n]`, `|A|=a`, and `Pi` is a set
partition of `A^c` into `a` unlabeled blocks of size `d`.  The points of `A` are the singleton
positions; the blocks of `Pi` are the heavy occurrence fibers.  The stabilizer of a reference
pair is

\[
 H_{a,d}=S_a\times W_{a,d}.
 \tag{2.5}
\]

Thus

\[
 \mathbb C[\Omega_{a,d}]
 \cong\operatorname {Ind}_{H_{a,d}}^{S_n}{\bf1}.
 \tag{2.6}
\]

Equivalently, first take the Foulkes module

\[
 \mathcal F_{a,d}
 =\operatorname {Ind}_{W_{a,d}}^{S_{ad}}{\bf1},
 \qquad \operatorname {ch}\mathcal F_{a,d}=h_a[h_d],
 \tag{2.7}
\]

and then induce it with the trivial module on the `a` singleton positions.  Transitivity of
induction gives

\[
 \mathcal M_{a,d}
 =\operatorname {Ind}_{S_a\times S_{ad}}^{S_n}
   ({\bf1}\boxtimes\mathcal F_{a,d}),
 \qquad
 \operatorname {ch}\mathcal M_{a,d}=h_a h_a[h_d].
 \tag{2.8}
\]

This proves (1.1).  It also states its exact scope: `mathcal M_(a,d)` is obtained after averaging
the independent singleton-label and heavy-label permutations.  In the full promise this is the
one-side position content of the trivial `S_q` carrier, not the raw named-label carrier.

Its dimension is

\[
 \dim\mathcal M_{a,d}
 ={n!\over a!(d!)^a a!}.
 \tag{2.9}
\]

## 3. Exact singleton- and heavy-marked modules

Fix `i in [n]`.  The basis `Omega_(a,d)` splits into two invariant `S_(n-1)` orbits.

* If `i in A`, removing the marked singleton leaves `a-1` unlabeled singleton positions and
  `a` unlabeled heavy `d`-blocks.  Its stabilizer is

  \[
   H_{\rm sing}=S_{a-1}\times W_{a,d}.
   \tag{3.1}
  \]

* If `i notin A`, the heavy block containing `i` becomes one distinguished block of size `d-1`;
  the other `a-1` heavy blocks still have size `d` and remain unlabeled.  Its stabilizer is

  \[
   H_{\rm heavy}
   =S_a\times S_{d-1}\times W_{a-1,d}.
   \tag{3.2}
  \]

Therefore

\[
 \mathcal M^{\rm sing}_{a,d}
 =\operatorname {Ind}_{H_{\rm sing}}^{S_{n-1}}{\bf1},
 \qquad
 \mathcal M^{\rm heavy}_{a,d}
 =\operatorname {Ind}_{H_{\rm heavy}}^{S_{n-1}}{\bf1},
 \tag{3.3}
\]

and their characteristics are exactly (1.3).  Their dimensions are

\[
 \dim\mathcal M^{\rm sing}_{a,d}
 ={(n-1)!\over (a-1)!(d!)^a a!}
 ={a\over n}\dim\mathcal M_{a,d},
 \tag{3.4}
\]

\[
 \dim\mathcal M^{\rm heavy}_{a,d}
 ={(n-1)!\over a!(d-1)!(d!)^{a-1}(a-1)!}
 ={ad\over n}\dim\mathcal M_{a,d}.
 \tag{3.5}
\]

Since `a+ad=n`, the two dimensions sum to (2.9).  On Frobenius characteristics the literal
restriction identity is

\[
 \begin{aligned}
 h_1^\perp\bigl(h_a h_a[h_d]\bigr)
 &=h_{a-1}h_a[h_d]
   +h_a\,h_1^\perp\bigl(h_a[h_d]\bigr)\\
 &=h_{a-1}h_a[h_d]
   +h_a h_{d-1}h_{a-1}[h_d].
 \end{aligned}
 \tag{3.6}
\]

The plethystic derivative in the last line is the pointed-block identity
`h_1^\perp h_a[h_d]=h_(d-1)h_(a-1)[h_d]`.  Thus both the orbit calculation and the exact character
calculation give

\[
 \boxed{
 \mathcal M_{a,d}\!\downarrow S_{n-1}
 =\mathcal M^{\rm sing}_{a,d}\oplus
  \mathcal M^{\rm heavy}_{a,d}.
 }
 \tag{3.7}
\]

There is no omitted coefficient `a`: the heavy block containing the marked point is distinguished
by the mark, while the other `a-1` blocks remain an unordered family.

## 4. Every multiplicity space in the restriction

For partitions `alpha,theta,lambda` of compatible sizes, define the Littlewood--Richardson
intertwiner space

\[
 \mathcal L^\lambda_{\alpha,\theta}
 =\operatorname {Hom}_{S_{|\alpha|}\times S_{|\theta|}}
 \left(S^\alpha\boxtimes S^\theta,
       S^\lambda\!\downarrow
       (S_{|\alpha|}\times S_{|\theta|})\right).
 \tag{4.1}
\]

It has dimension `c^lambda_(alpha,theta)`.  Define the heavy Foulkes multiplicity

\[
 F^{a,d}_\theta=(S^\theta)^{W_{a,d}},
 \qquad \theta\vdash ad.
 \tag{4.2}
\]

The parent occurrence space of `S^lambda` in (2.8) is

\[
 Z_\lambda=(S^\lambda)^{H_{a,d}}
 \cong
 \bigoplus_{\theta\vdash ad}
 \mathcal L^\lambda_{(a),\theta}\otimes F^{a,d}_\theta.
 \tag{4.3}
\]

No multiplicity-one assumption is made in (4.3).

For `beta vdash n-1`, the singleton-status occurrence space is

\[
 Z^{\rm sing}_\beta=(S^\beta)^{H_{\rm sing}}
 \cong
 \bigoplus_{\theta\vdash ad}
 \mathcal L^\beta_{(a-1),\theta}\otimes F^{a,d}_\theta.
 \tag{4.4}
\]

For the heavy status first put

\[
 Y^{a,d}_\xi
 =(S^\xi)^{S_{d-1}\times W_{a-1,d}},
 \qquad \xi\vdash ad-1.
 \tag{4.5}
\]

If desired, every occurrence in (4.5) is exposed by

\[
 Y^{a,d}_\xi
 \cong
 \bigoplus_{\gamma\vdash d(a-1)}
 \mathcal L^\xi_{(d-1),\gamma}\otimes F^{a-1,d}_\gamma.
 \tag{4.6}
\]

Then

\[
 Z^{\rm heavy}_\beta=(S^\beta)^{H_{\rm heavy}}
 \cong
 \bigoplus_{\xi\vdash ad-1}
 \mathcal L^\beta_{(a),\xi}\otimes Y^{a,d}_\xi.
 \tag{4.7}
\]

Finally define the one-box branching line

\[
 \mathcal B_{\beta\lambda}
 =\operatorname {Hom}_{S_{n-1}}
   (S^\beta,S^\lambda\!\downarrow S_{n-1}).
 \tag{4.8}
\]

It is one-dimensional when `beta nearrow lambda` and zero otherwise.  Regrouping the literal
restriction of the parent decomposition gives

\[
 \mathcal M_{a,d}\!\downarrow S_{n-1}
 \cong
 \bigoplus_{\beta\vdash n-1}S^\beta\otimes\mathcal R_\beta,
 \qquad
 \mathcal R_\beta
 =\bigoplus_{\lambda:\beta\nearrow\lambda}
   \mathcal B_{\beta\lambda}\otimes Z_\lambda.
 \tag{4.9}
\]

The status decomposition (3.7) gives a second decomposition of the same module,

\[
 \mathcal M_{a,d}\!\downarrow S_{n-1}
 \cong
 \bigoplus_{\beta\vdash n-1}S^\beta\otimes
 (Z^{\rm sing}_\beta\oplus Z^{\rm heavy}_\beta).
 \tag{4.10}
\]

Hence for every `beta` there is a unitary recoupling

\[
 U_\beta:\mathcal R_\beta
 \longrightarrow Z^{\rm sing}_\beta\oplus Z^{\rm heavy}_\beta.
 \tag{4.11}
\]

In particular,

\[
 \sum_{\lambda:\beta\nearrow\lambda}\dim Z_\lambda
 =\dim Z^{\rm sing}_\beta+\dim Z^{\rm heavy}_\beta.
 \tag{4.12}
\]

Equation (4.12) is a multiplicity identity, not permission to identify the summands on its left.

## 5. Restriction maps, status rows, polar lifts, and effects

The different maps used in a physical query have different types.

1. Choose isometric Young branching maps

   \[
    j_{\beta\lambda}:S^\beta\longrightarrow
    S^\lambda\!\downarrow S_{n-1}
    \qquad(\beta\nearrow\lambda).
    \tag{5.1}
   \]

   Their direct sum, tensored with `I_(Z_lambda)`, is the **literal restriction isometry**.  It
   lands in the orthogonal parent-origin space (4.9).

2. Let `P_sing,P_heavy` denote the coordinate-status projections in (3.7).  On the `beta`
   multiplicity define the status row maps

   \[
    A_{\sigma,\beta}=P_\sigma U_\beta:
    \mathcal R_\beta\longrightarrow Z^\sigma_\beta,
    \qquad \sigma\in\{{\rm sing},{\rm heavy}\}.
    \tag{5.2}
   \]

   These are coisometries, not positive operators.  Their positive effects on the parent-origin
   space are

   \[
    E_{\sigma,\beta}=A_{\sigma,\beta}^*A_{\sigma,\beta},
    \qquad
    E_{{\rm sing},\beta}+E_{{\rm heavy},\beta}=I_{\mathcal R_\beta}.
    \tag{5.3}
   \]

3. If `J:E->\mathcal R_\beta` selects a proposed occurrence subspace, the literal status map is

   \[
    L_{\sigma,\beta}=A_{\sigma,\beta}J:E\longrightarrow Z^\sigma_\beta.
    \tag{5.4}
   \]

   Its polar decomposition and its positive compression are

   \[
    L_{\sigma,\beta}=V_{\sigma,\beta}Q_{\sigma,\beta}^{1/2},
    \qquad
    Q_{\sigma,\beta}=L_{\sigma,\beta}^*L_{\sigma,\beta}
    =J^*E_{\sigma,\beta}J.
    \tag{5.5}
   \]

   `V_(sigma,beta)` is a partial isometry (a polar lift); `Q_(sigma,beta)` is a positive effect.
   Replacing the former by the latter, or calling the latter a restriction map, changes the
   physical channel.

4. If a full-group invariant multiplier has parent blocks

   \[
    B_\lambda:Z_{0,\lambda}\longrightarrow Z_{1,\lambda},
    \tag{5.6}
   \]

   then its literal unmasked `beta` block is

   \[
    B^{\rm res}_\beta
    =\bigoplus_{\lambda:\beta\nearrow\lambda}
      I_{\mathcal B_{\beta\lambda}}\otimes B_\lambda:
      \mathcal R_{0,\beta}\longrightarrow\mathcal R_{1,\beta}.
    \tag{5.7}
   \]

   A status-to-status block is

   \[
    A_{1,\sigma_1,\beta}
    B^{\rm res}_\beta
    A_{0,\sigma_0,\beta}^*.
    \tag{5.8}
   \]

   Parent mixing can occur in (5.8), but only through the displayed, physically derived
   recouplings.  It is not supplied by Young incidence.

These distinctions also explain why a partial-trace weight, a branch overlap, and a polar lift
cannot be interchanged.  A physical Schur query uses the literal maps on both answer sides; its
selected compression uses the corresponding positive effects.

## 6. Why the scalar Young harmonic is spurious

The scalar map (1.5) has domain `C^(Y_n)` and codomain `C^(Y_(n-1))`.  It knows only partition
labels and carrier dimensions.  It has no factor `Z_lambda`, no parent-origin direct sum, and no
answer index.

The correctly parent-tagged scalar shadow of literal restriction is

\[
 \mathscr R_n e_\lambda
 =\bigoplus_{\beta\nearrow\lambda}
   \sqrt{f^\beta/f^\lambda}\,e_{\beta,\lambda},
 \qquad
 \mathscr R_n:\mathbb C^{\mathcal Y_n}\longrightarrow
 \bigoplus_{\beta\vdash n-1}
 \mathbb C^{\{\lambda:\beta\nearrow\lambda\}}.
 \tag{6.0a}
\]

The vectors `e_(beta,lambda)` with different parent tags are orthogonal.  Young branching gives

\[
 \mathscr R_n^*\mathscr R_n=I,
 \qquad \sigma_{\min}(\mathscr R_n)=1.
 \tag{6.0b}
\]

If `Sigma_beta` is the unprovided codiagonal which sends every `e_(beta,lambda)` to `e_beta`, then

\[
 \mathscr D_n=\Sigma\mathscr R_n.
 \tag{6.0c}
\]

Thus the possible kernel is created entirely by `Sigma`, not by restriction.  Tensoring the
parent-tagged target with the occurrence spaces `Z_lambda` only makes the orthogonal-copy issue
more explicit.

For a support `S subseteq Y_n`, choose one unit occurrence vector in every nonzero `Z_lambda`.
On a fixed lower shape `beta`, the normalized branch vector has the literal form

\[
 r_\beta(c)
 =\bigoplus_{\substack{\lambda\in S\<machine-local-path-redacted>
   \sqrt{f^\beta/f^\lambda}\,c_\lambda e_{\beta\lambda}
 \in
 \bigoplus_{\substack{\lambda\in S\<machine-local-path-redacted>
 \mathcal B_{\beta\lambda}\otimes Z_\lambda.
 \tag{6.1}
\]

The scalar Young row is instead

\[
 (\mathscr D_nc)_\beta
 =\sum_{\substack{\lambda\in S\<machine-local-path-redacted>
  \sqrt{f^\beta/f^\lambda}\,c_\lambda.
 \tag{6.2}
\]

Thus (6.2) is obtained from (6.1) by an additional codiagonal functional which maps all vectors
`e_(beta lambda)` to the same scalar.  Literal restriction contains no such functional.  In fact

\[
 \|r_\beta(c)\|^2
 =\sum_{\substack{\lambda\in S\<machine-local-path-redacted>
  {f^\beta\over f^\lambda}|c_\lambda|^2,
 \tag{6.3}
\]

with no cross terms.  Therefore `(mathscr D_n c)_beta=0` can coexist with a nonzero, even large,
literal restricted vector.

The operator statement is sharper.  Put scalar or common-auxiliary blocks `B_lambda=c_lambda B`
on the selected occurrences.  Then (5.7) gives

\[
 \|B^{\rm res}_\beta\|
 =\max_{\lambda:\beta\nearrow\lambda}|c_\lambda|\,\|B\|,
 \tag{6.4}
\]

not the absolute value of (6.2).  Regrouping all `beta` types is unitary, so literal restriction
preserves the norm of the full operator exactly.  Boundary shapes do not help: every nonzero
parent has at least one removable corner, and its copy remains present at every such child.

For the two physical position factors and a full-group type
`rho=(lambda,mu,nu)`, write

\[
 M_t(\rho)=(S^\lambda\boxtimes S^\mu\boxtimes S^\nu)^{K_t}.
 \tag{6.5}
\]

For a left mark, an `H_L=S_(n-1)^L x S_n^R x S_q` type
`tau=(beta,mu,nu)` has multiplicity

\[
 N_t^L(\tau)
 =\bigoplus_{\lambda:\beta\nearrow\lambda}
   \mathcal B_{\beta\lambda}\otimes M_t(\lambda,\mu,\nu).
 \tag{6.6}
\]

The unmasked block of
`Gamma=\bigoplus_\rho I_(S^\rho)\otimes B_\rho` on (6.6) is

\[
 \bigoplus_{\lambda:\beta\nearrow\lambda}
 B_{(\lambda,\mu,\nu)}.
 \tag{6.7}
\]

For a right mark, with `tau=(lambda,gamma,nu)`, it is similarly

\[
 N_t^R(\tau)
 =\bigoplus_{\mu:\gamma\nearrow\mu}
   \mathcal B_{\gamma\mu}\otimes M_t(\lambda,\mu,\nu),
 \qquad
 \bigoplus_{\mu:\gamma\nearrow\mu}B_{(\lambda,\mu,\nu)}.
 \tag{6.8}
\]

Equations (6.6)--(6.8) hold for both `t=0,1`.  They are the exact reason a left or right scalar
Young harmonic does not cancel the restricted parent blocks.

## 7. Exact NO/YES position modules and common channels

The one-side NO projection onto the trivial alphabet carrier is exactly `mathcal M_(a,d)`.  On
the YES orbit, the singleton carrying the unique common raw label is distinguished from the other
`a-1` singleton positions.  Its one-side position module is therefore

\[
 \widetilde{\mathcal M}_{a,d}
 =\operatorname {Ind}_{S_1\times S_{a-1}\times W_{a,d}}^{S_n}{\bf1},
 \qquad
 \operatorname {ch}\widetilde{\mathcal M}_{a,d}
 =h_1h_{a-1}h_a[h_d].
 \tag{7.1}
\]

Its exact fixed-coordinate statuses are:

\[
 \begin{array}{c|c|c}
 \text{YES status}&\text{stabilizer in }S_{n-1}&\text{character}\\ \hline
 <machine-local-path-redacted> is the common singleton}
   &S_{a-1}\times W_{a,d}&h_{a-1}h_a[h_d]\\
 X:\ i\text{ is an exclusive singleton}
   &S_1\times S_{a-2}\times W_{a,d}&h_1h_{a-2}h_a[h_d]\\
 H:\ i\text{ is heavy}
   &S_1\times S_{a-1}\times S_{d-1}\times W_{a-1,d}
   &h_1h_{a-1}h_{d-1}h_{a-1}[h_d].
 \end{array}
 \tag{7.2}
\]

Their dimension fractions are respectively `1/n`, `(a-1)/n`, and `ad/n`; they sum to one.  In
character form,

\[
 h_1^\perp(h_1h_{a-1}h_a[h_d])
 =h_{a-1}h_a[h_d]
  +h_1h_{a-2}h_a[h_d]
  +h_1h_{a-1}h_{d-1}h_{a-1}[h_d].
 \tag{7.3}
\]

The apparent difference between NO and YES does not remove common occurrence channels.  Let
`widetilde Omega_(a,d)` consist of triples `(A,Pi,c)` with `(A,Pi) in Omega_(a,d)` and `c in A`
the distinguished common-singleton position.  The normalized forgetful pullback

\[
 J:\mathbb C[\Omega_{a,d}]
 \longrightarrow\mathbb C[\widetilde\Omega_{a,d}],
 \qquad
 J|A,\Pi\rangle
 ={1\over\sqrt a}\sum_{c\in A}|A,\Pi,c\rangle
 \tag{7.4}
\]

is an `S_n`-equivariant isometry.  It obeys

\[
 (P_C+P_X)J=JP_{\rm sing},
 \qquad P_HJ=JP_{\rm heavy}.
 \tag{7.5}
\]

If

\[
 \widetilde Z_\lambda
 =(S^\lambda)^{S_1\times S_{a-1}\times W_{a,d}},
 \tag{7.6}
\]

then (7.4) gives a formula-defined isometry
`j_\lambda:Z_\lambda -> \widetilde Z_\lambda` for every
parent occurrence.

Taking `S_q` invariants of the exact two-sided answer modules gives

\[
 V_0^{(q)}\cong\mathcal M_{a,d}^{(L)}\boxtimes\mathcal M_{a,d}^{(R)},
 \qquad
 V_1^{(q)}\cong
 \widetilde{\mathcal M}_{a,d}^{(L)}
 \boxtimes\widetilde{\mathcal M}_{a,d}^{(R)}.
 \tag{7.7}
\]

Consequently

\[
 M_0(\lambda,\mu,(q))\cong Z_\lambda\otimes Z_\mu,
 \qquad
 M_1(\lambda,\mu,(q))\cong
 \widetilde Z_\lambda\otimes\widetilde Z_\mu,
 \tag{7.8}
\]

and `j_\lambda\otimes j_\mu` is an exact common NO/YES occurrence channel.  Thus absence of common
parents is not the obstruction.  The obstruction is that their lower parent-origin copies remain
orthogonal and the raw equality channel is scalar on this alphabet sector.

The formulas are left/right symmetric.  The common label correlates the two distinguished YES
singletons at the raw-label level, but after projection to `nu=(q)` it creates no additional
alphabet carrier; (7.7)--(7.8) are exact.

## 8. The actual raw-label query channel

Let `V_t=C[X_t]` be the exact answer Hilbert spaces.  For side `s in {L,R}`, coordinate `i`, and
raw value `z in [q]`, let

\[
 D^s_{t,z}|x_t\rangle
 =\mathbf1[x_{t,s}(i)=z]|x_t\rangle.
 \tag{8.1}
\]

Each `D^s_(t,z)` is a positive orthogonal projection, and `sum_z D^s_(t,z)=I_(V_t)`.  The equality
pinching and the physical off-equality channel on rectangular operators are

\[
 \Phi_i^s(T)=\sum_{z=1}^qD^s_{1,z}TD^s_{0,z},
 \qquad
 \mathcal Q_i^s(T)=T\circ\Delta_i^s=T-\Phi_i^s(T),
 \tag{8.2}
\]

with type

\[
 \Phi_i^s,\mathcal Q_i^s:
 \operatorname {Hom}(V_0,V_1)\longrightarrow
 \operatorname {Hom}(V_0,V_1).
 \tag{8.3}
\]

This is neither a restriction functor nor a positive effect on one answer space.

For a selected channel `J_t:E_t->V_t` and `B:E_0->E_1`, define the literal raw maps, their
effects, and their polar decompositions by

\[
 L^s_{t,z}=D^s_{t,z}J_t:E_t\longrightarrow D^s_{t,z}V_t,
 \qquad
 F^s_{t,z}=L^{s*}_{t,z}L^s_{t,z}=J_t^*D^s_{t,z}J_t,
 \tag{8.4}
\]

\[
 L^s_{t,z}=U^s_{t,z}(F^s_{t,z})^{1/2}.
 \tag{8.5}
\]

Here `L` is a literal raw-label restriction, `U` is its polar partial isometry, and `F` is a
positive contraction on `E_t`.  The literal equality summand has type

\[
 L^s_{1,z}B L^{s*}_{0,z}:
 D^s_{0,z}V_0\longrightarrow D^s_{1,z}V_1,
 \tag{8.6}
\]

after the evident zero extensions.  Compressing the full channel back to the selected spaces
gives the exact identity

\[
 J_1^*\mathcal Q_i^s(J_1BJ_0^*)J_0
 =B-\sum_zF^s_{1,z}BF^s_{0,z}.
 \tag{8.7}
\]

Formula (8.7), not (1.5), is the same-raw-label equality-subtracted query channel.  In particular,
the polar lifts in (8.5) control the full raw ranges, while the effects in (8.7) control only the
displayed compression.  Neither can be inferred from a Young branching dimension.

If one refines all symmetries, fixing `z` replaces `S_q` by `S_(q-1)`.  For a left query and
`kappa=(beta,mu,gamma)` with `gamma vdash q-1`, the raw-refined parent-origin multiplicity is

\[
 \widehat N_t^L(\kappa)
 =\bigoplus_{\substack{\lambda:\beta\nearrow\lambda\\
                       \nu:\gamma\nearrow\nu}}
   \mathcal B_{\beta\lambda}\otimes
   \mathcal B_{\gamma\nu}\otimes
   M_t(\lambda,\mu,\nu).
 \tag{8.8}
\]

For a right query one replaces the first branching line by
`mathcal B_(eta,mu)` and keeps `lambda` fixed.  The projectors (8.1) act on the multiplicity spaces
(8.8); distinct full-group parents remain separate inputs until these exact raw/status effects
are applied.  Any claimed parent cancellation must therefore exhibit the matrices induced by
(8.1) on (8.8) for `t=0,1` and for both sides.

## 9. Sharp physical no-go on the alphabet-trivial sector

Let `P_t` be the orthogonal projection onto the `S_q`-trivial isotypic component of `V_t`.  The
family `D^s_(t,z)` is covariant under alphabet permutations, while `S_q` acts trivially on
`P_tV_t`.  Therefore all `q` compressed effects are equal.  Since they sum to `P_t`,

\[
 \boxed{
 P_tD^s_{t,z}P_t={1\over q}P_t
 \qquad(t=0,1;\ s=L,R;\ z\in[q]).
 }
 \tag{9.1}
\]

Now let `Gamma:V_0->V_1` satisfy `Gamma=P_1Gamma P_0`; it may contain arbitrary position parents,
arbitrary occurrence multiplicities, and arbitrary matrices between them.  Using (8.2) and (9.1),

\[
 \begin{aligned}
 P_1\Phi_i^s(\Gamma)P_0
 &=\sum_z(P_1D^s_{1,z}P_1)\Gamma
           (P_0D^s_{0,z}P_0)\\
 &=q\left({1\over q}\right)^2\Gamma
 ={1\over q}\Gamma.
 \end{aligned}
 \tag{9.2}
\]

Subtracting from `Gamma` proves (1.6).  Because the norm of a compression is at most the norm of
the full operator,

\[
 \|\mathcal Q_i^s(\Gamma)\|
 \ge\left(1-{1\over q}\right)\|\Gamma\|.
 \tag{9.3}
\]

This is simultaneous in the following sense: the same formula holds separately for every left
coordinate and every right coordinate, on both answer spaces.  It is also completely bounded:
tensoring every displayed map with an identity on a common auxiliary space leaves (9.1)--(9.3)
unchanged.

For a scalar two-sided parent table `c_(lambda,mu)` or common-auxiliary table
`B_(lambda,mu)=c_(lambda,mu)B`, full-group inequivalence gives

\[
 \|\Gamma\|=\max_{\lambda,\mu}\|B_{\lambda\mu}\|.
 \tag{9.4}
\]

The left restriction is the direct sum over `lambda` in (6.7), the right restriction is the
direct sum over `mu` in (6.8), and (9.3) then keeps `1-1/q` of (9.4) for either physical query.
No cyclic coefficient law, coefficient dynamic range, endpoint taper, or operator-valued sign can
alter this bound.

## 10. Incidence, boundaries, and an outer payload

### 10.1 Normalized incidence

The isometry (7.4), and its left/right tensor product, is the normalized pullback along the
constant-size forgetful fibers.  It preserves full-group parent orthogonality.  Moreover, the
physical mask is defined after forgetting by the same raw coordinate value, so normalized
incidence commutes with (8.2) on coefficients constant on those fibers.  Thus neither occurrence
averaging nor the full position-incidence completion inserts the missing codiagonal in (6.2).

The full pair-incidence orbit contains additional transportation data, but using coefficients
which depend on that data is a different, pair-dependent physical coupling.  It is not a scalar
Young-rank harmonic and is outside this node's first mechanism gate.

### 10.2 Boundary and coefficient norms

The no-go is not a boundary-localization statement.  It applies to every parent support and every
coefficient matrix.  If `max_(lambda,mu)||B_(lambda,mu)||=1`, a maximal parent remains as an
orthogonal summand after either literal restriction, and (9.3) gives queried norm at least
`1-1/q`.  Normalizing in `ell_1`, `ell_2`, maximum coefficient, Hilbert--Schmidt norm, or operator
norm cannot turn the scalar cancellation into a physical one; the relevant adversary norm is
(9.4).

### 10.3 Outer tensoring

If an outer payload is a genuine common auxiliary map `B:E_0->E_1` on which the position
restriction and raw-label projections act as the identity, then every map above amplifies by
`I_E`.  Equations (6.4) and (9.3) are unchanged.  Such a tensor factor can preserve an existing
outer numerator, but the Young selector contributes no additional denominator attenuation.

An outer construction which itself uses the same alphabet is **not** an independent tensor factor:
the diagonal `S_q` action couples it to the position carrier.  A nontrivial alphabet payload may
escape (9.1), but then the exact joint maps (8.4)--(8.8) must be derived.  One cannot multiply an
outer query ratio by a scalar Young singular value.  This is an open obligation, not a new
strategy asserted here.

## 11. Minimum extra coupling required

The sharp escape condition from this audit is algebraic.

1. **Restore raw-label covariance.**  Use a nontrivial alphabet constituent `nu`, or an explicitly
   pair-dependent occurrence carrier, for which the effects `F^s_(t,z)` in (8.4) are not all
   scalar on the selected channel.  Remaining in `nu=(q)` is ruled out by (9.3).
2. **Realize a physical codiagonal.**  For some marked type, at least two distinct full-group
   parent occurrences in (6.6) or (8.8) must have literal status/raw maps with overlapping ranges.
   Their formula-defined matrices, not just their dimensions, must implement the desired
   cancellation.  Orthogonal ranges reproduce (6.3)--(6.4).
3. **Pass equality deletion.**  The same coefficient matrices must make
   `B-sum_z F_(1,z) B F_(0,z)` small, including the polar-lifted full raw blocks, rather than only
   make an unweighted or dimension-normalized Young sum vanish.
4. **Do this on both sides.**  The left parent sums over `lambda`; the right parent sums over
   `mu`.  Both complete marked systems must have `O(m^(-1/6))` ratio, with no retained status.
5. **Preserve exact common channels and incidence.**  The proposed occurrences must exist in both
   `M_0(lambda,mu,nu)` and `M_1(lambda,mu,nu)`, and the same block must survive normalized
   full-orbit incidence and carry the outer numerator.

These conditions are necessary, not a construction.  Pursuing a new alphabet or pair-incidence
carrier belongs to its already registered controlling node; this audit does not silently branch
into one.

## 12. Gate ledger

| Gate | Exact outcome |
|---|---|
| frozen regime | integer `k>=2`, `p=0,u=1`, (2.1) |
| asserted one-side module | **correct only for unlabeled/alphabet-trivial quotient**, (2.8) |
| raw fixed-label module | `Ind_{(S_d)^a}^{S_n} 1`, (2.3) |
| singleton-marked module | `Ind_{S_(a-1) x W_(a,d)}^{S_(n-1)} 1`, (3.1)--(3.4) |
| heavy-marked module | `Ind_{S_a x S_(d-1) x W_(a-1,d)}^{S_(n-1)} 1`, (3.2)--(3.5) |
| literal status decomposition | exact direct sum, (3.7) |
| every occurrence multiplicity | formulas (4.2)--(4.9) |
| parent-origin marked space | orthogonal direct sum (4.9), (6.6), (6.8) |
| scalar Young incidence | aggregate codiagonal, not restriction, (6.1)--(6.4) |
| NO/YES common channels | exact normalized embedding, (7.4)--(7.8) |
| YES marked statuses | common/exclusive/heavy modules, (7.2)--(7.3) |
| literal raw maps / polar lifts / effects | separately typed in (8.4)--(8.7) |
| actual same-label query | `T-sum_z D_(1,z)TD_(0,z)`, (8.2) |
| trivial-alphabet equality compression | exactly `1/q`, (9.1)--(9.2) |
| both left/right physical query ratios | at least `1-1/q=1-O(m^-2)` |
| desired `O(m^-1/6)` selector ratio | **proposer-tier scoped FAIL** |
| coefficient/operator normalization | no effect; direct-sum norm (9.4) |
| boundary leakage | irrelevant to this no-go; every parent remains orthogonal |
| normalized incidence | preserves the common submodule and physical mask |
| independent outer auxiliary tensor | no Young gain; bound amplifies unchanged |
| nontrivial shared-alphabet outer coupling | outside scope; exact maps remain owed |
| completion-tier status | none; canonical node remains `OPEN`, pending review |

## 13. Source ledger and scope

This derivation was carried out from the exact endpoint definitions and standard induction,
branching, and Frobenius-characteristic identities.  The following local artifacts were read for
the stated load-bearing interfaces and scope boundaries:

* `ksum/artifacts/ksum_L3_hidden_frequency_promise_20260721.md`, SHA-256
  `558E0B6D8F9F65072B4F5E6E360967092D3B9BF0C3F5A2495124A678DBF8ACEB`: exact histogram and
  endpoint parameters;
* `ksum/artifacts/ksum_L3_critical_shared_branch_young_lattice_patch_audit_20260722.md`, corrected
  SHA-256 `C51B096B611FEA2978C1D208A6FF5194EE6E9607AE0006B65BB3E21473AD30A1`, and its Rule-7 review
  SHA-256 `6B180CBEC384119CABECE7E189A043B63EE1B1A190042DF6E2D367BC9E117E43`: scalar Young-map
  normalization and the explicit warning that physical recoupling was missing;
* `ksum/artifacts/ksum_L3_critical_same_parent_occurrence_multiplicity_audit_20260722.md`, SHA-256
  `A45D83E18E9BCB6E924AABEFCC2F4D6EE06DDF3C038A7FD523D9245429C54199`: typed occurrence spaces,
  marked effects, and the trivial-alphabet equality calculation on a selected family;
* `ksum/artifacts/ksum_L3_critical_full_position_incidence_orbit_classification_20260722.md`, corrected
  SHA-256 `A22D513B66D50635E76C6A2707AC3FC5EE657676FFEEA0C0B68B9EE6EDC2A088`, and
  `ksum/artifacts/ksum_L3_critical_full_position_mask_obstruction_audit_20260722.md`, SHA-256
  `19521DEB54082A37553F6D98075F33DD2095FE6307DBACDEA0121D18927AA315`: exact occurrence
  incidence, parent-origin marked typing, and raw off-equality rule;
* `ksum/artifacts/ksum_L3_critical_macroscopic_two_row_parent_chain_audit_20260722.md`, SHA-256
  `DAF241FA26542F12A989DE519833691FE64C4CA47F50F147F93982FF1990BC9A`, and its Rule-7 review
  SHA-256 `1AF2D6A5B2C0AEE0E4A8C7E1F92A80B167685FD1B64DFD2CA8228267F1DBBC09`: exact separation of
  Young restriction weights, physical status recoupling, polar lifts/effects, and common-auxiliary
  scope.

The result is intentionally scoped.  It rules out using a scalar full-rank Young harmonic as the
missing selector and proves the stronger physical bound (9.3) for the entire alphabet-trivial
sector.  It does not rule out nontrivial alphabet covariance, genuinely pair-dependent
full-position coefficients, or some other occurrence carrier whose exact raw maps implement the
missing coupling.  Those are separate, already registered obligations.

## 14. Bottom line

The full Young lattice can have scalar cycles and scalar down-kernels, and balanced constituents
can occur in the Foulkes-position module.  Neither fact supplies a query algorithm or adversary
block.  Literal restriction remembers which full-group parent produced every lower copy.  The
scalar incidence matrix forgets that label and then adds the copies; its cancellation is therefore
not physical.

On precisely the alphabet-trivial quotient where `ch M=h_a h_a[h_d]` is the right one-side
description, the raw-label calculation is decisive: equality pinching is `1/q` on every selected
block, so off-equality retains `1-1/q` on the left and on the right.  A cyclic coefficient law
cannot supply any positive power of `m`, and an independent outer tensor cannot change that
conclusion.  The canonical existential node must remain `OPEN` because a nontrivial
raw-label/occurrence coupling lies outside this scoped no-go and has not been constructed here.
