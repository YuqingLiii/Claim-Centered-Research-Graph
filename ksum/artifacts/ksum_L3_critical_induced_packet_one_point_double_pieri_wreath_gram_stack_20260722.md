# L3 induced packet: one-point double-Pieri/wreath Gram-stack specification

Date: 2026-07-22
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: read-only proposer-side derivation and implementation specification.  No fresh Rule-7
review of this artifact has been performed.  It asserts no physical commuting/noncommuting
verdict, query attenuation, coefficient construction, numerator, or exponent.

## 1. Decision

The missing all-parent marked data have a deterministic and gauge-invariant formulation.  One
does **not** need to choose phases for the literal marked codomain in order to decide same-source
effect commutators.  The required object is a one-point double-Pieri/wreath **Gram stack**.

The current local inputs suffice to define that stack uniquely, including every parent, point
child, cell status, position child, heavy path, and YES unmatched column.  They do not contain its
evaluated matrices.  In particular, the reviewed aggregate masses, top-branch lower bound, and
Johnson cross-Gram do not determine the three reduced recoupling tables below.  Therefore the
physical same-source commutators are well typed but their values are still unknown.

The smallest useful next computation is an exact reduced construction of the NO left-heavy and
right-heavy Gram stacks on one all-parent point-child closure, followed by an exact commutator.
A nonzero finite commutator would be finite evidence only; a zero finite commutator would close
only that tested sector.  Neither outcome would be a uniform theorem on the target family.

## 2. Unmarked source and deterministic Young branching

Put

\[
 D=a-1,
 \qquad V_a=S^{(a-1,1)},
 \qquad W=S_d\wr S_a,
 \qquad
 Z=\operatorname{Hom}_W(V_a,S^\theta),
 \tag{2.1}
\]

where

\[
 \theta=(ad-r-1,r,1),
 \qquad
 \lambda=(n-r-1,r,1),
 \qquad n=a(d+1).
 \tag{2.2}
\]

For answer `t` and alphabet parent `nu`, let

\[
 Y_{t,\nu}
 =\operatorname{Hom}_{H_t}
 \bigl(V_a\boxtimes V_a,\operatorname{Res}_{H_t}^{S_q}S^\nu\bigr).
 \tag{2.3}
\]

Fix the already specified deterministic real intertwiners

\[
 T_h:V_a\longrightarrow S^\theta,
 \qquad
 \Phi_{t,\nu,\alpha}:V_a\otimes V_a\longrightarrow S^\nu,
 \tag{2.4}
\]

normalized by

\[
 T_h^*T_{h'}=\delta_{hh'}I_{V_a},
 \qquad
 \Phi_{t,\nu,\alpha}^*\Phi_{t,\nu,\alpha'}
 =\delta_{\alpha\alpha'}I_{V_a\otimes V_a}.
 \tag{2.5}
\]

The unmarked multiplicity embedding is

\[
 \Omega_{t,\nu}:Y_{t,\nu}\otimes Z_L\otimes Z_R
 \longrightarrow
 S^\lambda_L\otimes S^\lambda_R\otimes S^\nu,
 \tag{2.6}
\]

whose reference vectors are

\[
 \omega_{t,\nu;\alpha,h,k}
 =\frac1D\sum_{i,j=1}^{D}
 \iota_{t,L}(T_hf_i)\otimes
 \iota_{t,R}(T_kf_j)\otimes
 \Phi_{t,\nu,\alpha}(f_i\otimes f_j).
 \tag{2.7}
\]

Use the real Young--Yamanouchi branching coisometry

\[
 b_{\rho\to\sigma}:S^\rho\longrightarrow S^\sigma,
 \tag{2.8}
\]

defined in the last-letter gauge by deleting the box containing `|rho|` when the remaining shape
is `sigma`, and returning zero otherwise.  For a raw label `z`, choose once and for all the
lexicographically first permutation `g_z` carrying the reference alphabet letter to `z` and put

\[
 b_{\nu\to\tau}^{(z)}
 =b_{\nu\to\tau}\rho_\nu(g_z).
 \tag{2.9}
\]

For a status whose reference letter lies in a different physical cell, the corresponding fixed
cell transport is included in `g_z`.  This is physical alignment data, not a rephasing of the
marked codomain.

## 3. Gauge-invariant all-parent Gram stack

Fix answer `t`, side `s`, actual cell status `chi`, ordered position child `beta`, and alphabet
point child `tau`.  Let `K^#_(t,s,chi)` be the stabilizer of the reference marked input.  In the
marked carrier

\[
 \mathcal V^L_{\beta,\tau}
 =S^\beta_L\otimes S^\lambda_R\otimes S^\tau,
 \qquad
 \mathcal V^R_{\beta,\tau}
 =S^\lambda_L\otimes S^\beta_R\otimes S^\tau,
 \tag{3.1}
\]

let

\[
 P^#_{t,s,\chi;\beta,\tau}
 ={1\over |K^#_{t,s,\chi}|}
 \sum_{g\in K^#_{t,s,\chi}}\rho_{\beta,\tau}^{s}(g)
 \tag{3.2}
\]

be its Reynolds projector.  In a nonorthonormal exact seminormal gauge, (3.2) is understood with
the invariant Young Gram; it is the same unitary projector after orthonormalization.

Let `B_(beta,tau,z)^s` apply `b_(lambda->beta)` on the queried position carrier,
`b_(nu->tau)^(z)` on the alphabet carrier, and the identity on the other position carrier.  Its
domain has all parent columns

\[
 \mathcal D_{t,\tau}
 =\bigoplus_{\nu:\,\tau\nearrow\nu}
 Y_{t,\nu}\otimes Z_L\otimes Z_R,
 \tag{3.3}
\]

omitting a parent only after its exact multiplicity or coupling has been shown to be zero.

The complete basis-independent Gram stack is

\[
 \boxed{
 \mathscr G^{\,t,s,\chi}_{\beta,\tau}(z)
 =w_{t,s,\chi}\,
 \Omega_t^*
 (B_{\beta,\tau,z}^{s})^*
 P^#_{t,s,\chi;\beta,\tau}
 B_{\beta,\tau,z}^{s}
 \Omega_t .}
 \tag{3.4}
\]

If `U^#` is any orthonormal marked invariant basis, the associated literal row is

\[
 A^{t,s,\chi}_{\beta,\tau}(z)
 =\sqrt{w_{t,s,\chi}}\,(U^#)^*B^s_{\beta,\tau,z}\Omega_t,
 \tag{3.5}
\]

and (3.4) is exactly `A^*A`.  Changing `U^#` changes the literal row on the left but does not
change (3.4).  More generally, the cross-Gram of two path rows with a common physical codomain is

\[
 \sqrt{w_bw_{b'}}\,
 \Omega_t^*B_b^*P^#_{b,b'}B_{b'}\Omega_t.
 \tag{3.6}
\]

Rows in different physical child carriers have no cross-Gram without a stated codomain
embedding.  No commutator of literal rectangular rows is defined.

## 4. Complete status and position-path inventory

The only nonempty queried cell statuses are

| answer | left query | right query |
|---|---|---|
| NO | rare `A`, heavy `H_L` | rare `B`, heavy `H_R` |
| YES | common `C`, residual `L`, heavy `H_L` | common `C`, residual `R`, heavy `H_R` |

The YES unused cell `U` is not a queried status.  Opposite-side cells are zero and are not added
for symmetry.

The exact branch masses are

\[
\begin{array}{c|c}
\text{status}&w_{t,s,\chi}\\ \hline
\text{NO rare }A/B&1/(d+1)\\
\text{YES common }C&1/[a(d+1)]\\
\text{YES residual }L/R&(a-1)/[a(d+1)]\\
\text{heavy }H_L/H_R&d/(d+1).
\end{array}
\tag{4.1}
\]

Write the three removable children as

\[
\begin{aligned}
 \beta_T&=(n-r-2,r,1),&
 \kappa_T&=(ad-r-2,r,1),\\
 \beta_M&=(n-r-1,r-1,1),&
 \kappa_M&=(ad-r-1,r-1,1),\\
 \beta_B&=(n-r-1,r),&
 \kappa_B&=(ad-r-1,r).
\end{aligned}
\tag{4.2}
\]

Horizontal-strip interlacing gives the following complete candidate path inventory in the stable
range.  A candidate is retained only when its exact deterministic recoupling coefficient is
nonzero.

1. NO rare `A/B`: only `beta_T`.
2. YES common `C`: only `beta_T`.
3. YES residual `L/R`: only `beta_T`, through the unique intermediate
   `(n-r-3,r,1)` obtained by attaching the remaining `a-2` residual points before the common
   singleton.
4. NO heavy:
   - `beta_T` receives `kappa_T,kappa_M,kappa_B`;
   - `beta_M` receives only `kappa_M`;
   - `beta_B` receives only `kappa_B`.
5. YES heavy: after attaching the `a-1` residual points, write the three possible intermediates
   below `beta_T` as

   \[
   \xi_T=(n-r-3,r,1),\qquad
   \xi_M=(n-r-2,r-1,1),\qquad
   \xi_B=(n-r-2,r).
   \tag{4.3}
   \]

   Then:
   - `beta_T` has the five paths
     `(kappa_T,xi_T)`, `(kappa_M,xi_T)`, `(kappa_M,xi_M)`,
     `(kappa_B,xi_T)`, `(kappa_B,xi_B)`;
   - `beta_M` has only `(kappa_M,xi_M)`;
   - `beta_B` has only `(kappa_B,xi_B)`.

Thus `top` versus `other`, singleton versus residual, and common versus private alphabet child are
three independent refinements.  None may substitute for another.

## 5. Deterministic Pieri recoupling scalars

Let `iota_(mu,l)^rho:S^mu -> S^rho` denote the positive-leading normalized Pieri isometry for a
horizontal `l`-strip.  The NO unmarked position map is

\[
 I_0=\iota_{\theta,a}^{\lambda},
 \tag{5.1}
\]

whereas the YES map is the ordered two-step attachment

\[
 I_1=\iota_{\zeta,1}^{\lambda}\iota_{\theta,a-1}^{\zeta},
 \qquad \zeta=\beta_T.
 \tag{5.2}
\]

The required position coefficients are defined without an ambiguous phase by the intertwiner
identities

\[
 (\iota_{\theta,a-1}^{\beta})^*
 b_{\lambda\to\beta}I_0
 =p^{0,\mathrm{rare}}_\beta I_{S^\theta},
 \tag{5.3}
\]

\[
 (\iota_{\kappa,a}^{\beta})^*
 b_{\lambda\to\beta}I_0
 =p^{0,H}_{\beta,\kappa}\,b_{\theta\to\kappa},
 \tag{5.4}
\]

and, for the YES residual/heavy paths,

\[
 (\iota_{\theta,a-2}^{\xi})^*
 (\iota_{\xi,1}^{\beta})^*
 b_{\lambda\to\beta}I_1
 =p^{1,\mathrm{res}}_{\beta,\xi} I_{S^\theta},
 \tag{5.5}
\]

\[
 (\iota_{\kappa,a-1}^{\xi})^*
 (\iota_{\xi,1}^{\beta})^*
 b_{\lambda\to\beta}I_1
 =p^{1,H}_{\beta,\kappa,\xi}\,b_{\theta\to\kappa}.
 \tag{5.6}
\]

Removing the YES common singleton gives `beta=beta_T` in the fixed positive-leading gauge.  The
scalars (5.3)--(5.6), including any signs, are part of the required exact table.  Aggregate down
ratios do not determine them individually.

## 6. Reduced occurrence and alphabet tables

Under the marked heavy-label stabilizer,

\[
 V_a\downarrow S_{a-1}=\mathbf1\oplus V_{a-1}.
 \tag{6.1}
\]

Let `eta` range over these two irreducibles, let `d_eta=dim eta`, and choose the canonical
positive-leading isometry `i_eta:eta -> V_a`.  The normalized coevaluation decomposes with the
exact factor

\[
 {1\over\sqrt D}\sum_{i=1}^D f_i\otimes f_i
 \longmapsto
 \sqrt{d_\eta\over D}
 {1\over\sqrt{d_\eta}}
 \sum_{u=1}^{d_\eta}e_u\otimes e_u.
 \tag{6.2}
\]

This factor must not be dropped.

### 6.1 Wreath occurrence restriction

Define the gauge-invariant occurrence Gram

\[
 \boxed{
 \mathsf O_{\kappa,\eta}[h,h']
 ={1\over d_\eta}
 \operatorname{Tr}
 \left[
  (b_{\theta\to\kappa}T_hi_\eta)^*
  (b_{\theta\to\kappa}T_{h'}i_\eta)
 \right].}
 \tag{6.3}
\]

Equivalently, if `U_(kappa,eta,gamma)` is any orthonormal marked-wreath intertwiner basis and

\[
 b_{\theta\to\kappa}T_hi_\eta
 =\sum_\gamma o_{\kappa,\eta,\gamma;h}
 U_{\kappa,\eta,\gamma},
 \tag{6.4}
\]

then

\[
 \mathsf O_{\kappa,\eta}[h,h']
 =\sum_\gamma
 \overline{o_{\kappa,\eta,\gamma;h}}
 o_{\kappa,\eta,\gamma;h'}.
 \tag{6.5}
\]

Thus the marked path basis cancels.  On the first target instance each (6.3) is only a `4 x 4`
matrix.

### 6.2 Alphabet point-child table

For a left-heavy mark put

\[
 Y^{t,L}_{\tau,\eta;\nu,\alpha}
 =b_{\nu\to\tau}^{(z)}
 \Phi_{t,\nu,\alpha}(i_\eta\otimes I_{V_a})
 :\eta\otimes V_a\longrightarrow S^\tau,
 \tag{6.6}
\]

and define

\[
 \boxed{
 \mathsf C^{t,L}_{\tau,\eta}
 [ (\nu,\alpha),(\nu',\alpha')]
 ={1\over d_\eta D}
 \operatorname{Tr}
 \left[
  (Y^{t,L}_{\tau,\eta;\nu,\alpha})^*
  Y^{t,L}_{\tau,\eta;\nu',\alpha'}
 \right].}
 \tag{6.7}
\]

For a right-heavy mark replace `i_eta tensor I` by `I tensor i_eta`.  For rare, common, or
residual marks both heavy standards are untouched, and the table is

\[
 \boxed{
 \mathsf C^{t,\chi}_{\tau}
 [ (\nu,\alpha),(\nu',\alpha')]
 ={1\over D^2}
 \operatorname{Tr}
 \left[
  (b_{\nu\to\tau}^{(z)}\Phi_{t,\nu,\alpha})^*
  b_{\nu'\to\tau}^{(z)}\Phi_{t,\nu',\alpha'}
 \right].}
 \tag{6.8}
\]

Equations (6.7)--(6.8) contain all parents sharing `tau` as rows and columns.  An off-diagonal
`nu,nu'` entry is a physical marked-parent codiagonal coefficient.  A point child is private only
when its exact active parent set has size one.

### 6.3 Assembly

For a left-heavy branch, on the active packet/left-occurrence factor,

\[
 \boxed{
 \widehat{\mathscr G}^{\,t,L,H}_{\beta,\tau}
 =w_H\sum_{\kappa,\xi,\eta}
 {d_\eta\over D}
 |p^{t,H}_{\beta,\kappa,\xi}|^2
 \left(
  \mathsf C^{t,L}_{\tau,\eta}
  \otimes
  \mathsf O_{\kappa,\eta}
 \right).}
 \tag{6.9}
\]

The sum is over the legal path inventory in Section 4; `xi` is absent on the NO side.  Restoring
the untouched factor gives

\[
 \mathscr G^{\,t,L,H}_{\beta,\tau}
 =\widehat{\mathscr G}^{\,t,L,H}_{\beta,\tau}
 \otimes I_{Z_R}.
 \tag{6.10}
\]

The right formula is the same with `Z_L` untouched and the active occurrence table on `Z_R`.
For rare/common/residual rows,

\[
 \boxed{
 \mathscr G^{\,t,s,\chi}_{\beta,\tau}
 =w_\chi\sum_\xi |p^{t,\chi}_{\beta,\xi}|^2
 \mathsf C^{t,\chi}_{\tau}
 \otimes I_{Z_L}\otimes I_{Z_R}.}
 \tag{6.11}
\]

These formulas prove the untouched-factor Gram theorem while retaining the shared packet factor.
They do not imply that a left Gram commutes with a right Gram.

## 7. YES common image and unmatched leakage

For each physical orientation `o in {L,R}` the induced packet supplies

\[
 j_{o,\nu}:Y_{0,\nu}\hookrightarrow Y_{1,\nu}.
 \tag{7.1}
\]

Let

\[
 P_{o,\nu}=j_{o,\nu}j_{o,\nu}^*,
 \qquad
 Y_{1,\nu}=j_{o,\nu}Y_{0,\nu}\oplus U_{o,\nu},
 \tag{7.2}
\]

where `U_(o,nu)` is the positive-leading orthogonal complement.  Every YES Gram in this
decomposition has the full block form

\[
 \boxed{
 Q_1^{s,o}=
 \begin{pmatrix}
  j_o^*Q_1^sj_o & j_o^*Q_1^su_o\\
  u_o^*Q_1^sj_o & u_o^*Q_1^su_o
 \end{pmatrix}.}
 \tag{7.3}
\]

The off-diagonal block is physical common-to-unmatched leakage.  Aggregate marked masses determine
some sums of the upper-left block; they determine neither the leakage block nor the unmatched
diagonal block.  The unmatched complement is orientation dependent: a vector unmatched to `J_L`
need not be unmatched to `J_R`, since `J_L^*J_R=K` is the nontrivial Johnson walk.  Therefore no
orientation-free zero-padding or unmatched superselection is allowed.

## 8. Meaningful commutators and the current stopping point

Embed every branch Gram (3.4) back into the complete answer source and sum the desired physical
branches.  For one answer `t`, the effects

\[
 Q^L_{t,z},\ Q^R_{t,w}\in\operatorname{End}(\mathbf E_t)
 \tag{8.1}
\]

have a well-defined commutator.  Using packet/occurrence coordinates, (6.9)--(6.10) reduce its
entries to

\[
 [X,Y]_{phk,p'h'k'}
 =\sum_u\left[
  x(p,h;u,h')y(u,k;p',k')
  -y(p,k;u,k')x(u,h;p',h')
 \right].
 \tag{8.2}
\]

The shared packet index `u` is the possible source of noncommutation.  Existing aggregate inputs
do not evaluate (8.2), because they do not supply (5.3)--(5.6), (6.3), and (6.7)--(6.8) in one
deterministic gauge.

Cross-answer ordinary commutators remain undefined:

\[
 F_{0,z}^s\in\operatorname{End}(\mathbf E_0),
 \qquad
 F_{1,z}^s\in\operatorname{End}(\mathbf E_1).
 \tag{8.3}
\]

Their native comparison is the rectangular transfer

\[
 \mathcal E_s(B)=\sum_zF_{1,z}^sBF_{0,z}^s,
 \qquad B\in\operatorname{Hom}(\mathbf E_0,\mathbf E_1).
 \tag{8.4}
\]

Alternatively, one may state an explicit physical pullback `J_o^*F_1J_o`, with the conclusion
scoped to that orientation and common subspace.

No expression in this artifact proves a nonzero physical commutator.  Conversely, no current
identity proves simultaneous diagonalization.

## 9. Finite regimes and the corrected first target instance

The small exact regimes must be separated from the currently selected target family.

1. `(a,d,r)=(3,6,2)` satisfies the stable and endpoint-inequality arithmetic and has `C_r=1`.
   It can check typing and packet-only recoupling but cannot test genuinely matrix-valued
   occurrence dependence.  It is not a member of the selected `s>=4` target family.
2. `(a,d,r)=(4,7,3)` has `C_r=2` and occurrence product rank four.  It can be a smaller exact
   implementation gate, but it is likewise not a member of the selected target family.
3. The selected target family is

   \[
   a=s^2,\qquad d=4s+1,\qquad r=s,\qquad
   q=4a,\qquad n=a(d+1),\qquad N=2n,
   \qquad s\ge4.
   \tag{9.1}
   \]

   Its first member is exactly

   \[
   \boxed{
   (s,a,d,r,q,n,N,C_r)=(4,16,17,4,64,288,576,4).}
   \tag{9.2}
   \]

   In particular, `N=576`; the value `256` is an arithmetic error and is not used here.

For (9.2),

\[
 \theta=(267,4,1),\qquad
 \lambda=(283,4,1),
 \tag{9.3}
\]

and exact hook division gives

\[
 f^\theta=46{,}937{,}442{,}816,
 \qquad
 f^\lambda=62{,}660{,}742{,}144.
 \tag{9.4}
\]

Thus a dense Young carrier is impossible.  The reduced output is nevertheless small: every
occurrence table (6.3) is `4 x 4` and the final Gram acts only on alphabet multiplicity times the
`4 x 4` occurrence product.

A minimal low-tail alphabet codiagonal can start from

\[
 \tau_*=(61,2).
 \tag{9.5}
\]

It has the certified packet parents `(62,2)` and `(61,3)`.  Its complete one-box parent closure is

\[
 \{(62,2),(61,3),(61,2,1)\},
 \tag{9.6}
\]

with a parent included exactly when `m_(t,nu)>0`.  No multiplicity line inside an included parent
may be selected away.  The Specht dimensions of `(62,2)`, `(61,3)`, `(61,2,1)`, and `(61,2)` are
respectively `1952`, `39648`, `79360`, and `1890`, so sparse alphabet branching is far smaller
than the position ambient carriers.

### Unreviewed planning counts

A scratch exact-integer Pieri-path recurrence was used only to assess implementation size:

\[
 D_0(\varnothing)=1,
 \qquad
 D_k(\mu)=
 \sum_{\rho:\,\mu/\rho\text{ horizontal }d\text{-strip}}
 D_{k-1}(\rho).
 \tag{9.7}
\]

It returned the planning values

\[
 [s_{(267,4,1)}]h_{17}^{16}=34272
 \tag{9.8}
\]

and, for the three marked position children in the order `kappa_T,kappa_M,kappa_B`,

\[
 [s_\kappa]h_{16}h_{17}^{15}
 =34272,\ 7140,\ 3060.
 \tag{9.9}
\]

No standalone script, raw log, or independent review was archived for (9.8)--(9.9).  They are
**unreviewed planning values only** and may not support a status change, a proof claim, or a
resource certificate.  They must be regenerated by an archived exact checker before being cited
as evidence.

## 10. Local-code reuse audit

The repository contains useful components, but no existing script directly constructs the stack
in Sections 3--6.

1. `tools/mdh_engine.py`, SHA-256
   `E01516DC93D995B0FB7B940C102D3F29F9C590F3A888BF07A0D5511613B3F760`, supplies an exact
   `Fraction` Young seminormal gauge and invariant Gram.  Its `YSN` constructor enumerates every
   standard tableau, so it cannot be applied directly to (9.3).
2. `tools/mdh_standard_query_tensor.py`, SHA-256
   `F31127DFCA1A6E2D651DE21599FFE086335BC501EA01D326BF0F3503F2B7C3C0`, contains a useful exact
   parent-to-child branching/Gram pattern, including parent-off-diagonal rectangles.  It is tied
   to the SE coset and does not implement the present wreath product.
3. `ksum/artifacts/logs_se_trace_t5_c2_embedding_20260721/se_trace_t5_c2_embedding.py`, SHA-256
   `41B858EE1D54B96383167206B2C18BA342FE47285AE754D6BBF1DCE7144F9DD3`, contains reusable
   skew-tableau enumeration, one/two-sparse generator plans, permutation transport, JM seed
   propagation, and implicit matvec structure.  It is shape-specific and primarily floating
   point.
4. `ksum/artifacts/logs_se_trace_t5_c2_gate_review_20260721/audit_t5_c2_gate_review.py`, SHA-256
   `68F72FBBA458351B0724B8D276BC2D9846A20C20F7790BE190B1E11F87275071`, independently rebuilds
   sparse generator plans and transport checks, but does not supply a generic wreath reducer.
5. `ksum/artifacts/logs_se_trace_t5_tame_c2_gate_20260721/tame_c2_reduced_audit.py`, SHA-256
   `CBA7C9A411AA4698D6AF35584940AB76481767853C076392AAE965A6C6BB68B2`, supplies a compact
   skew-tableau/Pieri feasibility implementation.  It is hard-coded to the SE target and does not
   construct `Hom_(S_d wr S_a)(V_a,S^theta)` or its one-point restriction.

The sparse combinatorial algorithms can be ported.  The stored numerical arrays and hard-coded
subgroup data cannot be reused as physical k-Sum recoupling coefficients.

## 11. Smallest module that must be added for the next calculation

The minimal missing implementation is an exact reduced Pieri-path/wreath reducer with the
following operations.

1. Build the ordered horizontal-strip-chain carrier

   \[
   U_\theta=(S^\theta)^{S_d^a}
   \tag{11.1}
   \]

   without constructing `S^theta`.
2. On that path basis, construct the adjacent `d`-block swap operators.  These give the physical
   `S_a` action and allow extraction of the `V_a` isotypic multiplicity `C_r`.
3. Mark one distinguished block, replace `d` by `d-1`, and construct the branching to every
   `kappa` and both

   \[
   \eta\in\{\mathbf1,V_{a-1}\}.
   \tag{11.2}
   \]

   The only persisted mathematical output needed from this stage is the exact collection of
   small matrices `O_(kappa,eta)` in (6.3), plus identity-level residuals and normalization sums.
4. Use the exact low-tail alphabet branching pattern to build the all-parent matrices
   `C_(tau,eta)` in (6.7)--(6.8).
5. Compute the Pieri scalars (5.3)--(5.6), assemble (6.9)--(6.11), and verify the full status
   resolution before testing commutators.

The safest arithmetic port combines the sparse skew-tableau and permutation-plan structures from
the T5 code with the rational/nonorthogonal exact Young Gram used by `mdh_engine.py`.  Reusing the
floating-point arrays alone would not decide whether a displayed commutator is exactly zero.

## 12. Concrete first target calculation

For the actual first target (9.2), perform the following calculation inside the existing
occurrence-pencil classification node.

1. Use answer `t=0`, so no YES unmatched issue enters the first same-source witness.
2. Use the point child `tau_*=(61,2)` and its complete active parent closure (9.6), retaining every
   alphabet multiplicity.
3. Compute all left-heavy and right-heavy path rows for `beta_T`, including all three `kappa`
   branches and both local `eta` branches.  Do not keep only a favorable path.
4. Assemble

   \[
   Q_L(z)=\mathscr G^{0,L,H_L}_{\beta_T,\tau_*}(z),
   \qquad
   Q_R(w)=\mathscr G^{0,R,H_R}_{\beta_T,\tau_*}(w).
   \tag{12.1}
   \]

5. Check separately the two alphabet-pair orbits `z=w` and `z!=w`, and compute exactly

   \[
   [Q_L(z),Q_R(w)].
   \tag{12.2}
   \]

6. If (12.2) is nonzero, archive its exact entry or exact rank as a **finite first-target
   witness only**.  It does not prove noncommutation for every `s>=4` and does not by itself
   activate a uniform Sylvester construction.
7. If (12.2) vanishes, record only that this `beta_T,tau_*` sector commutes at `s=4`; next add
   `beta_M,beta_B`, another point-child closure, and then the YES common/unmatched blocks.  Do not
   infer global or uniform commutation.

After a finite nonzero witness, the actual theorem obligation is a formula-level all-`s`
recoupling identity or determinant/minor that remains nonzero on a growing common source.  Finite
matrices cannot establish that quantifier.

## 13. Stopping point

This artifact supplies:

* a deterministic all-parent literal-row construction;
* the gauge-invariant Gram-stack replacement that avoids marked-codomain phases;
* the complete status and position-path inventory;
* common/private point-child typing;
* the YES unmatched leakage blocks;
* exact reduced formulas identifying the missing occurrence, alphabet, and Pieri tables;
* a corrected first-target parameter and size audit;
* a local-code reuse decision and one concrete next calculation.

It does **not** supply any evaluated physical Gram stack, any physical nonzero or zero commutator,
any simultaneous-diagonalization theorem, or any query/adversary conclusion.  The controlling
node must therefore remain OPEN unless and until separately archived calculations and the
required independent review justify a different status.
