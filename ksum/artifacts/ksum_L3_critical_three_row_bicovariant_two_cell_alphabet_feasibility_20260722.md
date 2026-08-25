# L3 critical endpoint: three-row bicovariant two-cell alphabet feasibility audit

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-bicovariant-two-cell-alphabet-kernel`

Verdict: **the exact representation gate passes for each registered single two-box alphabet
carrier, but a new carrier-level physical gate fails.**  If

\[
 \nu_+=(q-2,2),\qquad \nu_-=(q-2,1,1),
\]

then both restrictions to either exact NO or YES palette type subgroup contain exactly one copy of

\[
 \operatorname{Std}(H_{L_d})\boxtimes\operatorname{Std}(H_{R_d}),
\]

trivial on every other palette cell.  Coupling this copy to the complete left and right
three-row block-standard occurrence spaces gives `C_r^2` orthonormal common NO/YES channels in
one full type, where

\[
 C_r=\sum_{j=0}^{r-2}p(j).
\]

Thus the proposal is genuinely bicovariant and does not reduce to the previously refuted
`L_d plus R_d` direct sum.

For either fixed single carrier, however, its restriction to the alphabet point stabilizer is
multiplicity-free with two branches.  The exact covariant raw-value effects satisfy

\[
 0\preceq F_{t,z}^{s,T}\preceq \gamma_\pm(q) I,
 \qquad \sum_zF_{t,z}^{s,T}=I,
 \qquad \gamma_\pm(q)\le {1\over2}\quad(q\ge5).
\]

Consequently, for every rectangular, nonnormal, noncommuting coefficient matrix and for **each**
physical side,

\[
 \left\|T_s-\sum_zF_{1,z}^{s,T}T_sF_{0,z}^{s,T}\right\|
 \ge {1\over2}\|T_s\|.
\]

On the legal critical family the top three-row restriction has minimum singular value
`1-o(1)`, so every nonzero multiplier in either registered single carrier has normalized query
ratio at least `1/2-o(1)`.  This is incompatible with the required `O(m^(-1/6))` ratio.

Status discipline: proposer-tier analytic audit only.  The canonical node remains `OPEN` with
`pending-review`.  The conclusion is scoped to a multiplier supported in one fixed
`nu_+` or one fixed `nu_-` full-group block.  A coordinated direct sum across both global
alphabet irreps is not covered, because the two point-stabilizer restrictions share a branch and
could interfere after a query.  That possibility was registered, before calculation, as
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-mixed-two-box-full-type-recoupling-kernel`.

## 1. Ordered scope and exact endpoint groups

The audit opens the gates in the registered order:

1. restrict each two-box alphabet irrep under the exact NO and YES palette type subgroups;
2. construct the common bicovariant occurrence channels;
3. type the literal marked maps, positive effects, polar transports, and equality sandwiches;
4. test whether the new carrier really escapes the old direct-sum mechanism;
5. stop at the first uniform query obstruction, before incidence or numerator work.

Use the exact `p=0,u=1` critical profile

\[
 a=s^2,\qquad d=4s+1,\qquad r=s,\qquad q=4a,
 \qquad n=a(d+1),\qquad N=2n,
 \qquad s\ge4.
\tag{1.1}
\]

The NO palette type subgroup is

\[
 H_0=S_a^{L_1}\times S_a^{R_1}\times S_a^{L_d}\times S_a^{R_d},
\tag{1.2}
\]

and the YES palette type subgroup is

\[
 H_1=S_1^U\times S_1^C\times S_{a-1}^{L_1}\times S_{a-1}^{R_1}
       \times S_a^{L_d}\times S_a^{R_d}.
\tag{1.3}
\]

These are the palette quotients of the exact wreath-product orbit stabilizers.  Their
`L_d` and `R_d` factors have the same size `a` in both answers.  Put

\[
 A_t=\operatorname{Std}(S_a^{L_d}),\qquad
 B_t=\operatorname{Std}(S_a^{R_d}),\qquad D=a-1.
\tag{1.4}
\]

All other factors of `H_t` will act trivially on the target alphabet component.

The endpoint is legal:

\[
 q^3=64s^6\le 16s^4(2s+1)^2=N^2,
 \qquad q=\Theta(N^{2/3}),
\tag{1.5}
\]

and the three-row stable conditions `a>=r+1`, `d>=r`, `ad>=2r+1` hold.

## 2. Exact type-cell branching

### 2.1 A general palette-product decomposition

Let a palette partition have nonempty cells `Omega_1,...,Omega_h`, and write

\[
 H=\prod_{i=1}^h S_{|\Omega_i|},\qquad
 A_i=\operatorname{Std}(S_{|\Omega_i|}),
\]

with `A_i=0` for a singleton cell.  If `V=S^(q-1,1)` is the global standard representation,
then its restriction is exactly

\[
 V\downarrow_H
 =\mathbf1_H^{\oplus(h-1)}\oplus\bigoplus_i A_i.
\tag{2.1}
\]

The two global two-box representations satisfy

\[
 \operatorname{Sym}^2V
 =\mathbf1\oplus V\oplus S^{(q-2,2)},
 \qquad
 \bigwedge^2V=S^{(q-2,1,1)}.
\tag{2.2}
\]

For two distinct cells `i` and `j`, both the symmetric cross term

\[
 x\otimes y\longmapsto {x\otimes y+y\otimes x\over\sqrt2}
\tag{2.3}
\]

and the alternating cross term

\[
 x\otimes y\longmapsto {x\otimes y-y\otimes x\over\sqrt2}
\tag{2.4}
\]

are isometric copies of `A_i boxtimes A_j`.  This product type occurs once in the corresponding
cross term.  It cannot occur in `1` or in (2.1), because those contain at most one nontrivial cell
factor at a time.  Therefore

\[
 \boxed{
 \dim\operatorname{Hom}_{H}
 \left(A_i\boxtimes A_j,
       S^{(q-2,2)}\downarrow_H\right)=1,
 }
\tag{2.5}
\]

and

\[
 \boxed{
 \dim\operatorname{Hom}_{H}
 \left(A_i\boxtimes A_j,
       S^{(q-2,1,1)}\downarrow_H\right)=1.
 }
\tag{2.6}
\]

Equations (2.1)--(2.4) are also an exact restriction construction, rather than a dimension
guess: expanding `Sym^2` or `wedge^2` of the direct sum in (2.1) gives every type-cell summand.

### 2.2 The common NO/YES tensor

Apply (2.5)--(2.6) to the `L_d,R_d` cells of (1.2) and (1.3).  For
`epsilon in {+,-}`, choose the deterministic positive-leading isometry

\[
 \Psi_t^\epsilon:A_t\boxtimes B_t\hookrightarrow S^{\nu_\epsilon}
\tag{2.7}
\]

obtained from (2.3) or (2.4) after the order-defined cell identifications.  It is trivial on all
other factors of `H_t`.  The branching multiplicity is exactly one for `t=0` and for `t=1`.

This already separates the new carrier from the old one.  The standard alphabet carrier restricts
to `A_t direct-sum B_t`, whose summands are nontrivial on only one cell factor.  The present target
is the irreducible product `A_t boxtimes B_t`, nontrivial on both factors simultaneously.  Even
when dimensions happen to agree, their characters under `S_a^(L_d) x S_a^(R_d)` differ.

An independent formula scout checked the same multiplicity by the ordered-distinct-pair model.  If
`e_(ell r)` denotes the ordered pair basis, its explicit maps are

\[
 \Phi_\pm(x\otimes y)
 ={1\over\sqrt2}\sum_{\ell\in H_L,r\in H_R}
 x_\ell y_r(e_{\ell r}\pm e_{r\ell}).
\tag{2.8}
\]

The zero-sum conditions put `Phi_+` in the symmetric two-box kernel and `Phi_-` in the oriented
two-box kernel.  The scout also averaged the two exact character polynomials against the two cell
standard characters and obtained multiplicity one.  Thus (2.5)--(2.7) are corroborated by an
independent construction, not only by a dimension equality.

## 3. Complete bicovariant common occurrence

Set

\[
 W=S_d\wr S_a,\qquad V_a=S^{(a-1,1)},
\]

and

\[
 \theta_r=(ad-r-1,r,1),\qquad
 \lambda=(n-r-1,r,1).
\tag{3.1}
\]

The exact block-standard occurrence space on either physical side is

\[
 Z_r^{\rm cov}=\operatorname{Hom}_W(V_a,S^{\theta_r}),
 \qquad
 C:=\dim Z_r^{\rm cov}=C_r=\sum_{j=0}^{r-2}p(j).
\tag{3.2}
\]

Choose its deterministic orthonormal intertwiners

\[
 T_1,\ldots,T_C:V_a\longrightarrow S^{\theta_r},
 \qquad T_h^*T_k=\delta_{hk}I_{V_a}.
\tag{3.3}
\]

Let `f_1,...,f_D` be the fixed real orthonormal basis of `V_a`.  The coefficient-one NO/YES
attachments are

\[
 c^\lambda_{\theta_r,(a)}=1,
 \qquad
 c^\zeta_{\theta_r,(a-1)}=1,
 \qquad
 c^\lambda_{\zeta,(1)}=1,
 \qquad
 \zeta=(n-r-2,r,1).
\tag{3.4}
\]

Write their deterministic Pieri isometries as `Iota_(t,L)` and `Iota_(t,R)`.

For `1<=h,k<=C`, define

\[
 \begin{aligned}
 j_t^\epsilon(h,k)
 ={1\over D}\sum_{i,j=1}^{D}
 &\Iota_{t,L}(T_hf_i)\otimes
  \Iota_{t,R}(T_kf_j)\\
 &\otimes\Psi_t^\epsilon(f_i\otimes f_j).
 \end{aligned}
\tag{3.5}
\]

The two diagonal coevaluations in (3.5) couple the left and right block-permutation standards to
the two alphabet cell standards.  Internal `S_d` fibers are handled by (3.3); the two block
quotients act diagonally; every remaining type-cell and singleton factor acts trivially.  Hence

\[
 j_t^\epsilon(h,k)\in M_t(\rho_\epsilon),
 \qquad
 \rho_\epsilon=(\lambda,\lambda,\nu_\epsilon).
\tag{3.6}
\]

Equations (2.7) and (3.3) give the operator-level orthogonality identity

\[
 \langle j_t^\epsilon(h,k),j_t^\epsilon(h',k')\rangle
 =\delta_{hh'}\delta_{kk'}.
\tag{3.7}
\]

Thus both answers contain the deterministic common isometry

\[
 J_t^\epsilon:\mathbb C^C\otimes\mathbb C^C
 \hookrightarrow M_t(\rho_\epsilon).
\tag{3.8}
\]

This covers both multiplicity regimes.  At `r=2`, `C=1`; already at `r=3`, `C=2`; and on
(1.1), `r=s>=4` and `C>1` grows without bound.  Every identity above is an operator identity on
the full `C^2` occurrence space, not a trace check at `C=1`.

For unequal selected ranks, take arbitrary subspaces

\[
 E_t\subseteq\mathbb C^C\otimes\mathbb C^C,
 \qquad c_t=\dim E_t,
\tag{3.9}
\]

with no requirement that `c_0=c_1`, restrict (3.8), and let

\[
 B:E_0\longrightarrow E_1
\tag{3.10}
\]

be arbitrary.  The unmarked fixed-type multiplier is

\[
 \Gamma_B=\mathcal J_1
 \left(I_{S^\lambda\boxtimes S^\lambda\boxtimes S^{\nu_\epsilon}}\otimes B\right)
 \mathcal J_0^*,
 \qquad \|\Gamma_B\|=\|B\|.
\tag{3.11}
\]

No normality, commutativity, square-rank, sign, or tensor-product hypothesis is imposed on `B`.

## 4. Literal marked maps and the top branch

For answer `t`, side `s in {L,R}`, and raw label `z`, let

\[
 \ell_{t,z}^s:
 (S^\lambda\boxtimes S^\lambda\boxtimes S^{\nu_\epsilon})\otimes E_t
 \longrightarrow D_{t,z}^sX_t^{(s,\#)}
\tag{4.1}
\]

be the literal normalized refinement followed by the raw-value projection.  Its positive effect
and polar decomposition are

\[
 G_{t,z}^s=\ell_{t,z}^{s*}\ell_{t,z}^s,
 \qquad
 \ell_{t,z}^s=V_{t,z}^s(G_{t,z}^s)^{1/2}.
\tag{4.2}
\]

The row and column polar isometries are not identified.

Select the top predecessor

\[
 \beta_T=(n-r-2,r,1).
\tag{4.3}
\]

The marked representation carrier is

\[
 \mathcal C_L^epsilon
 =S^{\beta_T}\boxtimes S^\lambda\boxtimes S^{\nu_\epsilon},
 \qquad
 \mathcal C_R^epsilon
 =S^\lambda\boxtimes S^{\beta_T}\boxtimes S^{\nu_\epsilon}.
\tag{4.4}
\]

Its dimension is `f^(beta_T) f^lambda f^(nu_epsilon)`.  The heavy restriction map on the selected
multiplicity has polar decomposition

\[
 A_{t,T}^s=U_{t,T}^sH_{t,T}^s:E_t\longrightarrow N_{t,T}^s,
\tag{4.5}
\]

and the exact down-ratio argument gives

\[
 H_{t,T}^{s,2}\succeq\kappa_T I_{E_t},
 \qquad
 \kappa_T=1-{1\over(d+1)p_T},
\tag{4.6}
\]

where

\[
 p_T={f^{\beta_T}\over f^\lambda}
 ={(n-r+1)(n-2r-1)(n-r-1)
   \over n(n-2r)(n-r)}.
\tag{4.7}
\]

On (1.1), `kappa_T=1-o(1)`.  For the rectangular matrix (3.10), put

\[
 K_s=H_{1,T}^sBH_{0,T}^s:E_0\longrightarrow E_1,
 \qquad
 T_s=I_{\mathcal C_s^\epsilon}\otimes K_s.
\tag{4.8}
\]

Then

\[
 \|T_s\|=\|K_s\|\ge\kappa_T\|B\|.
\tag{4.9}
\]

Let `F_(t,z)^(s,T)` denote the positive raw-value effect after pulling (4.2) to the top polar
source `C_s^epsilon tensor E_t`.  It obeys

\[
 F_{t,z}^{(s,T)}\succeq0,
 \qquad \sum_zF_{t,z}^{(s,T)}=I.
\tag{4.10}
\]

The exact top-branch same-value compression is

\[
 (I\otimes U_{1,T}^s)
 \left[\sum_zF_{1,z}^{(s,T)}T_sF_{0,z}^{(s,T)}\right]
 (I\otimes U_{0,T}^s)^*.
\tag{4.11}
\]

Thus (4.1), (4.2), and (4.10) are three distinct levels: literal rectangular maps, their positive
effects, and the polar-source effects.  The calculation below uses (4.10)--(4.11), not an
untyped substitution of an effect for a literal map.

## 5. Exact point-stabilizer branching and the effect cap

### 5.1 A general multiplicity-free covariant POVM formula

Fix a reference raw label.  Let `P=S_(q-1)` be its alphabet point stabilizer.  Suppose

\[
 S^\nu\downarrow_P=\bigoplus_{j=1}^J S^{\tau_j}
\tag{5.1}
\]

is multiplicity-free, and let `Pi_(j,z)` be the translate to label `z` of the orthogonal projector
onto `S^(tau_j)` at the reference point.  For fixed `z`,

\[
 \Pi_{j,z}\Pi_{k,z}=\delta_{jk}\Pi_{j,z},
 \qquad \sum_j\Pi_{j,z}=I_{S^\nu}.
\tag{5.2}
\]

The reference effect in (4.10) commutes with the marked position groups and with `P`.  Schur's
lemma, covariance, and `sum_z F_(t,z)=I` therefore give the exact normal form

\[
 \boxed{
 F_{t,z}^{(s,T)}
 =\sum_{j=1}^J\gamma_j\Pi_{j,z}\otimes R_{t,j}^s,
 \qquad
 \gamma_j={f^\nu\over q f^{\tau_j}},
 }
\tag{5.3}
\]

where

\[
 R_{t,j}^s\succeq0,
 \qquad \sum_jR_{t,j}^s=I_{E_t}.
\tag{5.4}
\]

Indeed Schur averaging gives

\[
 \sum_z\Pi_{j,z}={qf^{\tau_j}\over f^\nu}I_{S^\nu},
\tag{5.5}
\]

which fixes every coefficient in (5.3).  The operators `R_(t,j)^s` may be noncommuting,
answer-dependent, side-dependent, and different-dimensional for `t=0,1`.  No scalarization or
identification is used.

By (5.2)--(5.4), with `gamma=max_j gamma_j`,

\[
 \boxed{0\preceq F_{t,z}^{(s,T)}\preceq\gamma I.}
\tag{5.6}
\]

### 5.2 The symmetric two-box carrier

For `q>=5`, ordinary branching gives

\[
 S^{(q-2,2)}\downarrow S_{q-1}
 =S^{(q-2,1)}\oplus S^{(q-3,2)}.
\tag{5.7}
\]

The dimensions and coefficients in (5.3) are

\[
 \begin{array}{c|c|c}
 \tau&f^\tau&\gamma_\tau\\ \hline
 (q-2,1)&q-2&{q-3\over2(q-2)}\\[2mm]
 (q-3,2)&{(q-1)(q-4)\over2}
   &{q-3\over(q-1)(q-4)}.
 \end{array}
\tag{5.8}
\]

Here `f^(q-2,2)=q(q-3)/2`.  Hence

\[
 \gamma_+(5)={1\over2},
 \qquad
 \gamma_+(q)={q-3\over2(q-2)}<{1\over2}\quad(q\ge6).
\tag{5.9}
\]

### 5.3 The alternating two-box carrier

For `q>=5`,

\[
 S^{(q-2,1,1)}\downarrow S_{q-1}
 =S^{(q-2,1)}\oplus S^{(q-3,1,1)}.
\tag{5.10}
\]

The dimensions and coefficients are

\[
 \begin{array}{c|c|c}
 \tau&f^\tau&\gamma_\tau\\ \hline
 (q-2,1)&q-2&{q-1\over2q}\\[2mm]
 (q-3,1,1)&{(q-2)(q-3)\over2}
   &{q-1\over q(q-3)}.
 \end{array}
\tag{5.11}
\]

Here `f^(q-2,1,1)=(q-1)(q-2)/2`, and therefore

\[
 \gamma_-(q)={q-1\over2q}<{1\over2}\qquad(q\ge5).
\tag{5.12}
\]

Combining (5.6), (5.9), and (5.12), every raw-value effect for either registered single carrier,
on either answer and either physical side, satisfies

\[
 \boxed{0\preceq F_{t,z}^{(s,T)}\preceq {1\over2}I.}
\tag{5.13}
\]

This statement is independent of the unknown recoupling operators (5.4).

## 6. Uniform physical obstruction

From (4.10) and (5.13),

\[
 \sum_z(F_{t,z}^{(s,T)})^2
 \preceq {1\over2}\sum_zF_{t,z}^{(s,T)}
 ={1\over2}I.
\tag{6.1}
\]

The operator Cauchy--Schwarz/Haagerup inequality, valid for rectangular `T_s`, gives

\[
 \begin{aligned}
 \left\|\sum_zF_{1,z}^{(s,T)}T_sF_{0,z}^{(s,T)}\right\|
 &\le
 \left\|\sum_z(F_{1,z}^{(s,T)})^2\right\|^{1/2}
 \|T_s\|
 \left\|\sum_z(F_{0,z}^{(s,T)})^2\right\|^{1/2}\\
 &\le {1\over2}\|T_s\|.
 \end{aligned}
\tag{6.2}
\]

Therefore

\[
 \boxed{
 \left\|T_s-\sum_zF_{1,z}^{(s,T)}T_sF_{0,z}^{(s,T)}\right\|
 \ge {1\over2}\|T_s\|.
 }
\tag{6.3}
\]

Restoring the row and column polar isometries in (4.11) preserves the norm.  Combining (4.9) and
(6.3), for `s=L` and separately for `s=R`, yields

\[
 \boxed{
 {\|\Gamma_B\circ\Delta_s\|\over\|\Gamma_B\|}
 \ge {\kappa_T\over2}
 ={1\over2}-o(1).
 }
\tag{6.4}
\]

This holds for `C=1`, for every `C>1`, for unequal `c_0,c_1`, and for every nonzero rectangular
`B:E_0->E_1`.  It is an operator-value obstruction, not a trace or average statement.  In
particular it rules out the required `O(m^(-1/6))` query ratio in either fixed registered
two-box carrier.

## 7. Why this is not the old direct-sum no-go

The old alphabet standard carrier contained orthogonal one-cell sectors `A_t` and `B_t`.  A left
query preserved the right-selected sector and a right query preserved the left-selected sector,
so a `2 x 2` sector matrix could not hide all of its blocks.

Here there is one shared cell tensor `A_t boxtimes B_t`.  A left mark leaves the right occurrence
index as an identity factor and a right mark leaves the left occurrence index as an identity
factor, but neither operation projects onto an `L` versus `R` sector: there is no such direct-sum
decomposition.  Both queries act on the same `C x C` occurrence tensor through the same global
alphabet irrep.  Thus the registered architectural escape genuinely succeeds.

More explicitly, fixing a left-heavy label restricts the left cell standard as

\[
 \operatorname{Std}_a\downarrow S_{a-1}
 =\mathbf1\oplus\operatorname{Std}_{a-1}.
\tag{7.1}
\]

Hence the selected tensor contains

\[
 \operatorname{Std}_{a-1}\boxtimes\operatorname{Std}_a
\tag{7.2}
\]

of dimension `(a-2)(a-1)` for every `a>=3`.  It remains nontrivial on both palette cells after
the mark.  At `a=2` this local branch vanishes, although the unmarked tensor is still not the old
direct sum.  The legal critical family has `a=s^2>=16`, so the physical obstruction (6.4) is not
caused by this small-cell degeneration.

The failure is different and stronger at the single-irrep level.  Every point effect in a two-box
irrep is spread over at least two point-stabilizer branches, and its largest covariant coefficient
is at most `1/2`.  Equations (5.13)--(6.4) then prevent the equality sandwich from approximating
the unmasked block.

## 8. Endpoint and parameter hygiene

### 8.1 The critical family

The construction is legal and growing on (1.1).  It is specifically a donor candidate at
`q=Theta(N^(2/3))`, not a uniform construction for every alphabet size.

### 8.2 The `q=5` endpoint

The exact critical type profile (1.2)--(1.3) has `q=4a`, so it does not exist at `q=5`.  The
nearest occupancy choice has `a=1`, for which
`Std(S_a)=0` and the bicovariant tensor (1.4) is absent.  Abstractly, the two point-branching caps
(5.9) and (5.12) remain valid at `q=5`, but there is no nonzero three-row bicovariant occurrence
to attach.  This route therefore supplies nothing at the small-alphabet endpoint; that endpoint
is handled by a different DAG branch.

### 8.3 The `q=N` endpoint

Within the exact profile `q=4a` and `N=2a(d+1)`, imposing `q=N` forces `d=1`.  The stable
three-row family requires `d>=r`, while nonzero/growing bicovariant occurrence needs `r>=2`.
Hence the three-row carrier is absent at `q=N` as well.  Again, this is an endpoint-specific
critical donor route, not the project's already separate large-alphabet construction.

### 8.4 Small and large occurrence ranks

The `C=1` branch (`r=2`) and all `C>1` branches are covered by the same identities
(3.3), (3.7), and (5.3)--(6.4).  No claim is inferred from a numerical `C=1` gate.  The legal
critical family lies in `C>1` and has `C->infinity`.

## 9. Exact stopping point and noncoverage

The physical query gate fails before normalized incidence, coefficient norm optimization,
remainder control, or the outer numerator is opened.  No exponent improvement follows.

The following possibility is deliberately not adjudicated here.  The restrictions of
`nu_+` and `nu_-` to `S_(q-1)` share `tau=(q-2,1)`.  Although distinct global `S_q` blocks are
orthogonal before a query, their marked restrictions may interfere in that shared branch.  A
coordinated multiplier supported on the direct sum of both global alphabet irreps is therefore
not covered by the compression-to-one-full-type argument (6.4).  It is a distinct multi-full-type
candidate now recorded at
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-mixed-two-box-full-type-recoupling-kernel`;
no recoupling or cancellation calculation for it is performed here.

## 10. Gate ledger

| Ordered obligation | Outcome |
|---|---|
| exact NO/YES palette subgroups | (1.2)--(1.3) |
| symmetric cell-tensor branching | **PASS**, multiplicity one, (2.5) |
| alternating cell-tensor branching | **PASS**, multiplicity one, (2.6) |
| common NO/YES full type | **PASS**, `rho_epsilon=(lambda,lambda,nu_epsilon)`, (3.5)--(3.8) |
| common occurrence rank | **PASS**, `C_r^2`, including `C=1` and `C>1` |
| unequal selected ranks | typed by (3.9)--(3.11) |
| literal map/effect/polar separation | typed by (4.1)--(4.11) |
| exact point branching for `nu_+` | (5.7)--(5.9) |
| exact point branching for `nu_-` | (5.10)--(5.12) |
| arbitrary recoupling operators | retained in (5.3)--(5.4), not scalarized |
| raw-effect spectral cap | `F_(t,z)<=I/2`, (5.13) |
| equality sandwich | at most half the unmasked norm, (6.2) |
| both physical queries | **DECISIVE SCOPED FAIL**, at least `1/2-o(1)`, (6.4) |
| reduction to dead `L/R` direct sum | **NO**; Section 7 gives a distinct obstruction |
| `q=5` legality | target cell tensor absent in the exact critical profile |
| `q=N` legality | forces `d=1`; three-row occurrence absent |
| mixed `nu_+ direct-sum nu_-` multiplier | outside scope; separate Rule-8 registration required |
| incidence/numerator/remainders | not opened after the physical failure |
| completion-tier status | none; independent Rule-7 review pending |

## 11. Frozen-source ledger

* Exact critical type cells and full wreath-product stabilizers:
  `ksum/artifacts/ksum_L3_critical_full_position_incidence_orbit_classification_20260722.md`, SHA-256
  `A22D513B66D50635E76C6A2707AC3FC5EE657676FFEEA0C0B68B9EE6EDC2A088`.
* Independent ordered-pair and character cross-check of the two exact type-cell multiplicities,
  including the marked genuine two-cell branch:
  `ksum/artifacts/ksum_L3_critical_two_box_branching_independent_crosscheck_20260722.md`, SHA-256
  `72185D1BADCC4A1EDC929970D528152233DAEA6D0AACD8ABC65A683A4F26CFBA`.
* Exact three-row coefficient, deterministic block-standard intertwiners, singleton attachments,
  top down-ratio, and literal-map conventions:
  `ksum/artifacts/ksum_L3_critical_three_row_block_standard_covariant_feasibility_20260722.md`, SHA-256
  `3FE61B416E5C0C8AB84FEF1940F9BFB9A4513CADCAC9AC40BC611FAECE71B0DD`.

All new two-box branching, common bicovariant embedding, point-stabilizer coefficient, effect-cap,
and norm-obstruction statements in this memo are analytic.  No finite character table, fitted
exponent, or numerical value check supports the verdict.
