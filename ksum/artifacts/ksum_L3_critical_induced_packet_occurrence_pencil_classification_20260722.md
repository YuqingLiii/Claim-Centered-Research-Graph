# L3 critical endpoint: induced-packet occurrence-pencil classification

Date: 2026-07-22  
Canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: proposer-side analytic classification; fresh Rule-7 review is pending.  
Scope: the complete `p=0,u=1,q=4a` induced alphabet packet tensored with both deterministic
three-row block-standard occurrence spaces.  No resolvent, Sylvester equation, incidence norm,
query attenuation, or numerator is tested here.

## 1. Classification verdict

The operator hierarchy and every required index can be typed exactly, but the physical pencils
cannot yet be assigned a uniform commuting or noncommuting verdict.

1. The complete unmarked source is the direct sum of every alphabet full type, every alphabet
   multiplicity, and the full left/right occurrence product.  No multiplicity-one copy is
   selected.
2. Every literal marked row is indexed by the actual queried cell status, an ordered position
   predecessor, an alphabet point predecessor, and every compatible internal heavy path.  All
   unmarked parents sharing one marked child are columns of the same row map; an old full-parent
   tag is not a superselection label.
3. The deterministic coevaluation proves an untouched-factor theorem for **all cross-Grams and
   positive effects** on the complete, uncompressed occurrence source:

   \[
   G^L_{p,p'}=\widehat G^L_{p,p'}\otimes I_{Z_R},\qquad
   G^R_{p,p'}=I_{Z_L}\otimes\widehat G^R_{p,p'}.
   \tag{1.1}
   \]

   It does not, with the currently constructed codomains, prove that the rectangular literal maps
   themselves admit a common tensor factorization.  That stronger statement would require a
   compatible factorization of every marked raw codomain.
4. Left and right effects share the alphabet packet/marked-parent coordinate.  Equation (1.1)
   therefore does not imply that they commute.  Conversely, no physical nonzero commutator has
   been derived for the complete critical family.
5. NO and YES effects act on different spaces.  Their ordinary commutator is undefined.  The
   native cross-answer object is the rectangular equality-transfer superoperator

   \[
   \boxed{
   \mathcal E_s(B)=\sum_zF_{1,z}^s\,B\,F_{0,z}^s,
   \qquad B\in\operatorname{Hom}(\mathbf E_0,\mathbf E_1).}
   \tag{1.2}
   \]

6. Deterministic Young/subduction matrices would decide every finite rank and commutator in
   (1.1)--(1.2).  The currently reviewed inputs do not contain the complete row matrices for all
   position parents, point children, cell statuses, and private branches.  Thus no closed formula
   presently decides commutation uniformly for `s>=4`.

This is a substantive partial classification, not completion of the canonical claim.  The node
must remain **OPEN / pending fresh review**.

## 2. Complete deterministic unmarked source

Put

\[
G=S_q,\qquad q=4a,\qquad W=S_d\wr S_a,\qquad
V_a=S^{(a-1,1)},\qquad D=a-1,
\tag{2.1}
\]

and

\[
\theta_r=(ad-r-1,r,1),\qquad
\lambda=(n-r-1,r,1),\qquad
Z=\operatorname{Hom}_W(V_a,S^{\theta_r}).
\tag{2.2}
\]

Let `C_r=dim Z`.  The reviewed coefficient formula is

\[
C_r=\sum_{j=0}^{r-2}p(j).
\tag{2.3}
\]

Use the deterministic real Young bases and positive-leading-coordinate Gram--Schmidt convention
already fixed by the occurrence construction.  Its basis intertwiners satisfy

\[
T_h^*T_k=\delta_{hk}I_{V_a},\qquad 1\le h,k\le C_r.
\tag{2.4}
\]

For answer `t in {0,1}`, let `H_t` and `tau_t` be the exact alphabet stabilizer and its two-heavy-
standard representation from the complete induced packet.  For every `nu |- q`, define

\[
Y_{t,\nu}
=\operatorname{Hom}_{H_t}
  \bigl(\tau_t,\operatorname{Res}^{S_q}_{H_t}S^\nu\bigr),
\qquad m_{t,\nu}=\dim Y_{t,\nu}.
\tag{2.5}
\]

Choose all deterministic normalized alphabet intertwiners

\[
\Phi_{t,\nu,\alpha}:V_a\otimes V_a\longrightarrow S^\nu,
\qquad
\Phi_{t,\nu,\alpha}^*\Phi_{t,\nu,\alpha'}
=\delta_{\alpha\alpha'}I_{V_a\otimes V_a}.
\tag{2.6}
\]

Write `Z_L,Z_R` for two labelled copies of `Z`.  The full selected multiplicity over `nu` is

\[
\mathcal E_{t,\nu}=Y_{t,\nu}\otimes Z_L\otimes Z_R,
\qquad
\dim\mathcal E_{t,\nu}=m_{t,\nu}C_r^2,
\tag{2.7}
\]

and the complete unmarked carrier is

\[
\mathcal K_t
=\bigoplus_{\nu\vdash q}
 \left(S^\lambda_L\otimes S^\lambda_R\otimes S^\nu\right)
 \otimes\mathcal E_{t,\nu}.
\tag{2.8}
\]

For compactness, set

\[
\mathbf E_t:=\mathcal K_t,
\qquad
\mathcal E_t:=\bigoplus_\nu\mathcal E_{t,\nu}.
\tag{2.8a}
\]

Thus `mathbf E_t` retains every carrier factor, while `mathcal E_t` denotes only the multiplicity
coordinates.  A display that suppresses carriers always means the corresponding carrier-identity
extension on `mathbf E_t`.

For orthonormal `f_1,...,f_D` in `V_a`, a deterministic invariant basis vector is

\[
\omega_{t,\nu;\alpha,h,k}
=\frac1D\sum_{i,j=1}^{D}
 \iota_{t,L}(T_hf_i)\otimes
 \iota_{t,R}(T_kf_j)\otimes
 \Phi_{t,\nu,\alpha}(f_i\otimes f_j).
\tag{2.9}
\]

The factor `1/D`, not `1/sqrt(D)`, is forced by the two coevaluations.  Equations (2.4) and
(2.6) give orthonormality for all `(alpha,h,k)`.  Formula (2.9), rather than a later choice of
answer-dependent eigenbasis, is the reference basis used below.

The two physical unmarked orientation embeddings, with the carrier identities displayed, are

\[
\mathbf J_o^{\mathrm{occ}}
=\bigoplus_{\nu}
 I_{S^\lambda_L\otimes S^\lambda_R\otimes S^\nu}
 \otimes j_{o,\nu}\otimes I_{Z_L}\otimes I_{Z_R}:
 \mathbf E_0\longrightarrow\mathbf E_1,
\qquad o\in\{L,R\},
\tag{2.10}
\]

where `j_(o,nu):Y_(0,nu)->Y_(1,nu)` is an isometry.  They are physical embeddings, not two gauges:

\[
(\mathbf J_L^{\mathrm{occ}})^*\mathbf J_R^{\mathrm{occ}}
=K\otimes I_{Z_L}\otimes I_{Z_R},
\tag{2.11}
\]

and `K` is the normalized Johnson swap on each rare-cell fiber.

## 3. Regimes that must not be conflated

The actual critical family is

\[
a=s^2,\qquad d=4s+1,\qquad r=s,\qquad
q=4a,\qquad n=a(d+1),\qquad s\ge4.
\tag{3.1}
\]

Here `C_r>1`, and the complete bicovariant occurrence factor has rank `C_r^2`.  The first values
are `C_4=4`, `C_5=7`, and `C_6=12`; these values are checks of (2.3), not an asymptotic inference.

There are three different rank-one statements in the surrounding project.

* At `r=2`, (2.3) gives `C_r=1`, so the stable bicovariant two-copy construction has an actual
  uncompressed `C_r^2=1` occurrence case when its separate stability conditions (including
  `a>=3`) hold.  It is outside (3.1).
* Inside the critical `C_r^2>1` space one may select a one-dimensional compression.  That is a
  legal algebraic `c=1` formula gate, not a claim that the full critical multiplicity is one.
* The older one-cell construction additionally needed an invariant channel of multiplicity
  `g_r=p(r)+p(r-1)-p(r+1)`.  Its `r=2` value is zero, so that different one-cell realization has no
  physical rank-one endpoint.  This absence does not remove the bicovariant rank-one case above.

Unequal selected ranks `c_0,c_1>1` are allowed by taking subspaces of the full occurrence
multiplicities.  Their multiplier is intrinsically rectangular.  No zero padding is licensed.

At `a=2`, `V_a` is one-dimensional and the induced alphabet/Johnson gate is exact, but the
three-row occurrence stable condition `a>=r+1` fails for every `r>=2`.  Thus `a=2` is an
alphabet-only degeneration check and is physically absent from the three-row critical occurrence
family.  It also does not make the complete `S_8` alphabet packet multiplicity one.

## 4. Complete marked index and actual cell statuses

For a query on side `s`, a marked row is indexed by

\[
b=(s,z,\chi,\beta,\tau,\gamma).
\tag{4.1}
\]

The meanings are:

* `z` is the actual raw palette value, summed over all `q` values;
* `chi` is the queried cell status in the table below;
* `beta nearrow lambda` is the **ordered** predecessor on the queried position side;
* `tau nearrow nu` is the alphabet point predecessor;
* `gamma` is every compatible internal heavy-cell restriction path when `chi=H_s`, and is empty
  for a singleton/residual status.

The actual cell-status inventory is

| answer | left query | right query |
|---|---|---|
| NO | `A` (rare singleton cell), `H_L` | `B` (rare singleton cell), `H_R` |
| YES | `C` (common singleton), `L` (left residual), `H_L` | `C` (common singleton), `R` (right residual), `H_R` |

The unused YES cell `U` is not an input value and therefore is not an actual queried status.
Opposite-side cells are zero for the stated query side.  They must not be inserted to make a
colored or symmetric-looking table.

The three position predecessors are

\[
\begin{aligned}
\beta_T&=(n-r-2,r,1),\\
\beta_M&=(n-r-1,r-1,1),\\
\beta_B&=(n-r-1,r).
\end{aligned}
\tag{4.2}
\]

Every row among (4.2) whose deterministic restriction coefficient is nonzero is retained.  The
reviewed top Gram bound does not license deleting `beta_M` or `beta_B` from the complete pencil.

Likewise, `tau` ranges over every nonzero point child.  A child shared by multiple full parents is
a codiagonal/common branch; a child reached from only one selected parent is a private branch.
Both are physical.  The words `common/private point child`, `singleton/residual cell`, and
`top/other position predecessor` name three different refinements and are never identified.

For fixed `(t,s,chi,beta,tau,gamma)`, the parent-column domain is

\[
\mathcal D^s_{t,b}
=\bigoplus_{\nu:\,\tau\nearrow\nu}
 Y_{t,\nu}\otimes Z_L\otimes Z_R,
\tag{4.3}
\]

with only the parents for which the full deterministic coupling is nonzero.  The direct sum in
(4.3) is essential: after restriction, the marked symmetry sees `tau`, not an orthogonal copy of
the old `nu` label.

The child carrier is ordered:

\[
\begin{cases}
S^\beta_L\otimes S^\lambda_R\otimes S^\tau,&s=L,\\
S^\lambda_L\otimes S^\beta_R\otimes S^\tau,&s=R.
\end{cases}
\tag{4.4}
\]

Thus `(beta,lambda;tau)` and `(lambda,beta;tau)` are distinct physical tags.

## 5. Literal rows, effects, ranks, kernels, and images

Let `Ref_t^s` be the normalized physical refinement and `D_(t,z)^s` the raw-value projector.  On
the full selected carrier the literal map is

\[
\ell_{t,z}^s
=D_{t,z}^s\operatorname{Ref}_t^s\mathcal J_t:
\mathcal K_t\longrightarrow\mathscr R_{t,z}^s.
\tag{5.1}
\]

After decomposing both sides under the marked subgroup, the multiplicity row belonging to (4.1)
is the deterministic matrix

\[
A_{t,z;b}^s:\mathcal D^s_{t,b}\longrightarrow\mathcal N^s_{t,z;b}.
\tag{5.2}
\]

Its entries are, by definition, the matrix coefficients of (5.1) between the vectors (2.9) and
the deterministic marked Young/subduction basis.  This is a constructive exact definition, not
an abstract branching coefficient.  It includes every compatible `nu` as a column and every
marked multiplicity/path as a row.

For rows with the same physical marked codomain define the full cross-Gram pencil

\[
G^s_{t;b,b'}=(A^s_{t,z;b})^*A^s_{t,z;b'},
\tag{5.3}
\]

and for a diagonal member define the positive source effect

\[
Q^s_{t,z;b}=G^s_{t;b,b}=(A^s_{t,z;b})^*A^s_{t,z;b}.
\tag{5.4}
\]

Rows with different physical codomains do not have a cross-Gram until an explicit codomain
embedding is supplied.  Literal rectangular maps never have an ordinary commutator.

For every row, without any rank assumption,

\[
\begin{aligned}
\operatorname{rank}A_{t,z;b}^s
 &=\operatorname{rank}Q_{t,z;b}^s,\\
\ker A_{t,z;b}^s
 &=\ker Q_{t,z;b}^s,\\
\operatorname{im}Q_{t,z;b}^s
 &=(\ker A_{t,z;b}^s)^\perp,\\
\operatorname{im}A_{t,z;b}^s
 &=A_{t,z;b}^s[(\ker A_{t,z;b}^s)^\perp].
\end{aligned}
\tag{5.5}
\]

These identities classify the spaces but do not supply the missing numerical rank.  The latter is
the rank of the deterministic subduction matrix (5.2), which has not yet been evaluated for the
complete row inventory.

Embedding each (5.4) back into the complete source and summing every raw value and every actual
branch gives the normalization resolution

\[
\sum_{z}\sum_{b\in\mathcal B_t^s}
 I_{t,b}Q^s_{t,z;b}I_{t,b}^*=I_{\mathbf E_t}
\tag{5.6}
\]

after the standard carrier normalization factors are included in `A`.  A sum over one chosen
color, one top parent, or only a common point child is not (5.6).

## 6. What factorizes, and what does not

Let `p,p'` collect the alphabet full-type/multiplicity coordinate and every compatible marked
parent/path coordinate.  In the basis `(p,h,k)` of (2.9), the exact contraction of the untouched
coevaluation gives, for every pair of left rows sharing a codomain,

\[
\bigl(G^L_{t;b,b'}\bigr)_{p h k,\,p'h'k'}
=g^L_{t;b,b'}(p,h;p',h')\,\delta_{kk'},
\tag{6.1}
\]

and, for every pair of right rows,

\[
\bigl(G^R_{t;b,b'}\bigr)_{p h k,\,p'h'k'}
=g^R_{t;b,b'}(p,k;p',k')\,\delta_{hh'}.
\tag{6.2}
\]

Equivalently, on the complete uncompressed occurrence product,

\[
G^L=\widehat G^L\otimes I_{Z_R},\qquad
G^R=I_{Z_L}\otimes\widehat G^R,
\tag{6.3}
\]

where the shared packet coordinate is part of each hatted active factor.  For singleton/residual
rows, neither block-standard occurrence is touched, so their Grams further specialize to

\[
G^{\rm singleton/residual}
=\widehat G^{\rm packet,parent}\otimes I_{Z_L}\otimes I_{Z_R}.
\tag{6.4}
\]

Full-type Fourier transformations and marked-parent codiagonal mixing act inside the hatted
packet/active factor, so they preserve the passive identity in (6.3).  An arbitrary entangled
compression `E_t subset Z_L tensor Z_R`, however, need not preserve a visible tensor factor:
`P_E(\widehat G tensor I)P_E` can have no such form.

If `c_R=dim Z_R`, (6.3) and (5.5) give the exact diagonal-effect consequences

\[
\begin{aligned}
\operatorname{rank}Q^L&=c_R\operatorname{rank}\widehat Q^L,\\
\ker Q^L&=(\ker\widehat Q^L)\otimes Z_R,\\
\operatorname{im}Q^L&=(\operatorname{im}\widehat Q^L)\otimes Z_R,
\end{aligned}
\tag{6.5}
\]

and symmetrically on the right.  For (6.4), ranks multiply by `C_r^2`.  The literal row has the
same rank and kernel as its diagonal Gram, but its codomain image has no canonical tensor-product
identification unless one separately constructs
`mathcal N^L=widehat{mathcal N}^L tensor Z_R` or its right analogue.

This is why the proved theorem is a Gram/effect theorem.  Upgrading it to
`A_L=widehat A_L tensor I_R` after the full parent codiagonal would be an unsupported literal-map
claim.

## 7. Exact aggregate cell masses

The complete induced alphabet embedding supplies exact aggregate identities before any parent
pinching.  In the left physical orientation,

\[
\begin{aligned}
J_L^*Q_C(z)J_L&={1\over a}P_A(z),&
J_L^*Q_L(z)J_L&={a-1\over a}P_A(z),\\
J_L^*Q_U(z)J_L&={1\over a}P_B(z),&
J_L^*Q_R(z)J_L&={a-1\over a}P_B(z),
\end{aligned}
\tag{7.1}
\]

with `C,U` exchanged in the right orientation.  Heavy-cell identities have Gram one on the
unchanged heavy fiber.  Tensoring (7.1) by both occurrence identities is exact.

For one physical query side, the complete position/cell mass splits as

\[
\begin{array}{c|c}
\text{branch}&\text{aggregate mass}\\ \hline
\text{NO rare singleton cell}&1/(d+1)\\
\text{YES common singleton}&1/[a(d+1)]\\
\text{YES residual singleton}&(a-1)/[a(d+1)]\\
\text{heavy cell}&d/(d+1).
\end{array}
\tag{7.2}
\]

The entries in (7.2) are full branch/partial-trace normalizations.  They do not say that an
individual `(beta,tau,gamma)` effect is a scalar.  In particular, keeping only the common
singleton loses the non-negligible residual mass.

## 8. Four operator levels and the native rectangular transfer

Four distinct objects occur.

1. **Literal marked row:** `ell_(t,z)^s` in (5.1), or a row `A_(t,z;b)^s` in (5.2).
2. **Positive source effect:**
   `F_(t,z)^s=ell_(t,z)^(s*) ell_(t,z)^s`, or its carrier/branch compression `Q`.
3. **Literal equality sandwich:** for a legal unmarked multiplier
   `B:mathbf E_0->mathbf E_1`,

   \[
   \mathcal L_{s,z}(B)
   =\ell_{1,z}^s(I\otimes B)\ell_{0,z}^{s*}:
   \mathscr R_{0,z}^s\longrightarrow\mathscr R_{1,z}^s.
   \tag{8.1}
   \]

4. **Effect sandwich and summed transfer:**

   \[
   \mathcal S_{s,z}(B)=F_{1,z}^sBF_{0,z}^s,
   \qquad
   \mathcal E_s=\sum_z\mathcal S_{s,z}.
   \tag{8.2}
   \]

The polar transports suppressed when passing from (8.1) to (8.2) must be tracked in any literal
claim; (8.1) and (8.2) are not interchangeable.

Unmarked equivariance requires, with all position carriers included,

\[
B=\bigoplus_{\nu}
 I_{S^\lambda_L\otimes S^\lambda_R\otimes S^\nu}\otimes B_\nu,
\qquad
B_\nu:\mathcal E_{0,\nu}\longrightarrow\mathcal E_{1,\nu}.
\tag{8.3}
\]

There is no unmarked map between inequivalent `nu`.  Individual marked effects may have
cross-parent blocks after restriction to a common `tau`; the full raw-value sum in (8.2) restores
the legal unmarked equivariance.

Expanding (8.2) by status means summing every physically compatible pair
`(b_1,b_0)` with the same raw `z`.  Common and private point branches, singleton and residual
cells, every nonzero position predecessor, and every heavy path remain in this sum.  Compatibility
may make a term zero, but no branch is discarded merely because it is not codiagonal.

The map

\[
\mathcal E_s:
\operatorname{Hom}(\mathbf E_0,\mathbf E_1)
\longrightarrow
\operatorname{Hom}(\mathbf E_0,\mathbf E_1)
\tag{8.4}
\]

is well typed even when the two ranks differ.  With the Hilbert--Schmidt inner product it is
positive self-adjoint:

\[
\langle B,\mathcal E_s(B)\rangle_{HS}
=\sum_z\left\|(F_{1,z}^s)^{1/2}B(F_{0,z}^s)^{1/2}\right\|_{HS}^2\ge0.
\tag{8.5}
\]

Equivalently,

\[
\operatorname{vec}(\mathcal E_s)
=\sum_z(F_{0,z}^s)^T\otimes F_{1,z}^s.
\tag{8.6}
\]

Formula (8.6) is the deterministic representation formula that decides a completed finite pencil.
It does not itself provide the missing physical matrices or an asymptotic commutation theorem.

## 9. Meaningful commutators and embeddings

### 9.1 Same-answer effects

Within one answer, all positive effects transported to the same complete unmarked source have
ordinary commutators.  Write a left effect `X` and a right effect `Y` as

\[
X_{p h k,p'h'k'}=x(p,h;p',h')\delta_{kk'},\qquad
Y_{p h k,p'h'k'}=y(p,k;p',k')\delta_{hh'}.
\tag{9.1}
\]

Then the exact cross-side commutator is

\[
[X,Y]_{p h k,p'h'k'}
=\sum_u\Bigl[
x(p,h;u,h')y(u,k;p',k')
-y(p,k;u,k')x(u,h;p',h')
\Bigr].
\tag{9.2}
\]

The shared packet index `u` is why untouched occurrence factors do not force (9.2) to vanish.
Same-side commutators reduce to the commutator of the corresponding hatted active matrices, tensored
with the passive identity.

A finite Hermitian effect family on one Hilbert space is simultaneously unitarily diagonalizable
if and only if every pairwise commutator vanishes.  This criterion applies to the same-answer
effects and, after an explicit common-source pullback, to a combined NO/YES family.  It does not
apply to literal rectangular rows.

### 9.2 Cross-answer comparison

Because

\[
F_{0,z}^s\in\operatorname{End}(\mathbf E_0),\qquad
F_{1,z}^s\in\operatorname{End}(\mathbf E_1),
\tag{9.3}
\]

the expression `[F_(0,z)^s,F_(1,w)^u]` is undefined.  For a chosen physical orientation `o`, one
may pull YES back to the NO source:

\[
\widetilde F_{1,z}^{s,o}
=(\mathbf J_o^{\mathrm{occ}})^*F_{1,z}^s\mathbf J_o^{\mathrm{occ}}
\in\operatorname{End}(\mathbf E_0).
\tag{9.4}
\]

Only commutators such as `[F_(0,z)^s,tilde F_(1,w)^(u,o)]` are then defined.  The conclusion may
depend on `o`: (2.11) shows that `J_L` and `J_R` are distinct physical embeddings and are not
coordinate gauges.

For genuinely unequal ranks, choose a common Hilbert space `U` and explicit isometries

\[
R_0:U\hookrightarrow\mathbf E_0,\qquad
R_1:U\hookrightarrow\mathbf E_1.
\tag{9.5}
\]

Then `R_t^*F_tR_t` are comparable on `U`.  If `dim E_0<=dim E_1`, (9.4) is the special case
`R_0=I,R_1=mathbf J_o`.  If neither full space embeds in the other in the desired physical way, (9.5)
classifies only the stated common subspace and leaves both unmatched complements outside the
claim.  If the two orientations also use external occurrence embeddings `R_L,R_R`, their
cross-Gram is

\[
K\otimes R_L^*R_R,
\tag{9.6}
\]

not automatically `K tensor I`.

A coherent basis change
`F_t -> U_t^*F_tU_t`, `J -> U_1^*JU_0` conjugates every pulled commutator by `U_0`; its rank and
vanishing are invariant.  Changing `J_L` to `J_R`, or changing the physical common subspace in
(9.5), is not such a gauge transformation.

### 9.3 Transfer superoperators

Both `mathcal E_L` and `mathcal E_R` act on the same rectangular Hilbert--Schmidt space, so their
superoperator commutator is meaningful:

\[
\begin{aligned}
[\mathcal E_L,\mathcal E_R](B)
=\sum_{z,w}\bigl(&F_{1,z}^LF_{1,w}^R B F_{0,w}^RF_{0,z}^L\\
&-F_{1,w}^RF_{1,z}^L B F_{0,z}^LF_{0,w}^R\bigr).
\end{aligned}
\tag{9.7}
\]

Since each transfer is self-adjoint by (8.5), the pair is simultaneously unitarily diagonalizable
on `Hom(E_0,E_1)` exactly when (9.7) vanishes for every `B`.  The current inputs do not decide
(9.7) on the critical family.

## 10. Johnson interaction: one exact noncommutation and its limit

The orientation cross-Gram on one rare-cell fiber is

\[
K|A\rangle={1\over a^2}\sum_{c\in A,\,u\notin A}|A-c+u\rangle.
\tag{10.1}
\]

Let `P_z` project onto subsets containing `z`.  For any `a>=2`, choose `A` containing `z`, set
`c=z`, and choose `u notin A`.  The matrix entry joining `A` to `A-z+u` has magnitude `1/a^2` in

\[
[K,P_z]\ne0.
\tag{10.2}
\]

Thus raw singleton membership is not diagonal in Johnson harmonic degree.  No global basis
labelled only by `(j,h,k)` may be assumed for all raw statuses.

The heavy-cell alphabet projectors do commute with `K`, because (10.1) fixes both heavy cells and
their standard fibers.  This does **not** prove that the full parent-refined heavy occurrence
effects commute: their position restrictions and shared packet recouplings are additional
operators.  Equation (10.2) likewise does not prove uniform noncommutation of the physical heavy
occurrence pencil.  It is an exact warning against a false joint spectral assumption, not a
Sylvester-premise theorem.

## 11. Missing deterministic data and stopping point

To replace the present OPEN verdict by a commuting or noncommuting theorem, one still needs the
complete normalized row matrices (5.2), namely:

1. `S^lambda downarrow S_(n-1)` subduction rows for all three ordered predecessors, not only the
   top aggregate Gram;
2. `S^nu downarrow S_(q-1)` rows for every point child `tau`, with all parents sharing `tau`
   assembled before any diagonalization;
3. every compatible internal heavy restriction path `gamma` and every singleton/residual
   attachment row;
4. the NO/YES and L/R recoupling coefficients between (2.9) and one deterministic marked basis;
5. common/private cross-Grams and all leakage rows needed to verify (5.6).

Once those rows are supplied, (5.5), (9.2), and (9.7) analytically decide ranks, kernels, images,
effect commutation, and transfer commutation at each finite parameter.  A uniform critical-family
conclusion then requires a formula-level recoupling theorem; finite gates cannot establish it.

The classification stops here.  In particular:

* the scalar total-energy resolvent law is not licensed by simultaneous diagonalization;
* the noncommuting Sylvester law is not licensed by a proved physical nonzero commutator;
* the newly registered rectangular-transfer resolvent law is now well typed by (1.2), but no
  coefficient, inverse, attenuation, or numerator statement about it is tested here.

## 12. Exact structural checker

Checker: `ksum/tools/ksum_l3_occurrence_pencil_classification_check.py`  
Checker SHA-256: `6D96E025E3B28E01153CF1813DD859B47F11CDDCD4925F38A3567E7C1AD6A2C9`  
Raw output: `ksum/artifacts/logs_ksum_L3_occurrence_pencil_classification_20260722/run.json`  
Raw-output SHA-256: `8AB84417DB98C52332F13611613F289B656134094D6D4EA1E16BFB3AB65FEF8C`

The checker performs exact symbolic/rational gates only.

* At `a=2,3` it constructs the full Johnson walk, verifies its spectrum, and confirms the nonzero
  commutator (10.2).  These values corroborate the all-`a` entry proof; they do not infer it.
* A labelled synthetic shared-packet example verifies that Gram factorization with untouched
  occurrence factors does not logically force cross-side commutation.  It is not presented as a
  physical counterexample.
* A packet-scalar synthetic example verifies the corresponding sufficient commuting case.
* Exact rational matrices verify rank multiplication, rectangular `F_1BF_0` typing, positivity
  and self-adjointness of its vectorized superoperator, pullback typing, orientation dependence,
  and coherent-gauge rank invariance.
* The status inventory and the separation between formal `c=1`, actual critical `C_r>1`, and the
  alphabet-only `a=2` gate are asserted explicitly.

The checker expressly does not prove a physical occurrence commutator, any uniform
noncommutation, a literal-map codomain tensor theorem, query attenuation, a resolvent/Sylvester
bound, incidence normalization, or a numerator.

## 13. Failure-mode audit

| attack | disposition |
|---|---|
| dropped/extra normalization | `1/D` double coevaluation, normalized refinement, every raw `z`, and complete branch sum are explicit |
| literal/effect confusion | literal rows, Grams/effects, literal equality sandwiches, and effect transfers have separate types |
| multiplicity-one anchoring | all `m_(t,nu)` and all `C_r^2` channels are retained; `a=2` and selected `c=1` are scoped separately |
| answer-dependent basis alignment | deterministic Young/Gram--Schmidt bases are fixed before comparison; coherent gauge invariants are stated |
| private-status deletion | private point children, residual cells, other position parents, and heavy paths are mandatory rows |
| colored sum for a central sum | (5.6) and (8.2) sum all physical raw values and branches |
| false parent superselection | every `nu` sharing one marked child `tau` is a column of the same row map |
| illegal unmarked cross-irrep | (8.3) is block diagonal in `nu`; only marked restriction creates cross-parent blocks |
| unequal-rank padding | native transfer remains rectangular; common comparisons use explicit isometries only |
| finite-value asymptotic inference | finite exact gates are labelled corroboration/inference guards; no critical exponent is inferred |

## 14. Frozen inputs used with scope

* `ksum/artifacts/ksum_L3_critical_three_row_induced_bicovariant_alphabet_packet_first_gate_20260722.md`,
  SHA-256 `047CA5FEB7E4A5D27A687106F87F4BD1F838B68BF4695E79BE18B23EBBA1CC59`:
  complete induced packet, physical orientations, Johnson cross-Gram, and cell masses.
* `ksum/artifacts/ksum_L3_critical_three_row_induced_bicovariant_alphabet_packet_rule7_review_20260722.md`,
  SHA-256 `CF1E853AE7BEBC689963409A03D19BBA96684AF0C4BBAF4ED59155E2F64741F2`:
  fresh scoped validation of those alphabet claims, including all multiplicities and the warning
  that occurrence pencils were not yet typed there.
* `ksum/artifacts/ksum_L3_critical_three_row_block_standard_covariant_feasibility_20260722.md`,
  SHA-256 `3FE61B416E5C0C8AB84FEF1940F9BFB9A4513CADCAC9AC40BC611FAECE71B0DD`,
  and its review, SHA-256
  `6731D07408B5D3117FE59043E151B0412F5081D99D15405D59BEA5C35B68F1AF`:
  deterministic `T_h`, coefficient formula, ordered position parents, and literal/effect typing.
* `ksum/artifacts/ksum_L3_critical_three_row_bicovariant_two_cell_alphabet_rule7_review_20260722.md`,
  SHA-256 `2FE6AE8F38DE6BBFB85C070B2AA1904F17D99228D4D771438141A015789BEB6A`:
  double coevaluation, full `C_r^2` occurrence source, point branches, and rectangular equality
  effect formula.  It does not supply the complete induced-packet row matrices.
* `ksum/artifacts/ksum_L3_critical_three_row_mixed_two_box_full_type_recoupling_rule7_review_20260722.md`,
  SHA-256 `0D6AA6C0AFE42716A9DBC4F0D85D0E2FC9722998432A7C1AA032B445E5F79506`:
  common/private codiagonal typing and unequal-rank rectangular transfer precedent.  Its selected
  two-full-type theorem is not extrapolated to the complete packet.

No downstream artifact is used as evidence for a commutation or feasibility verdict.
