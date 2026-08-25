# L3 critical endpoint: three-row block-standard covariant feasibility audit

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-block-standard-covariant-occurrence-kernel`

Verdict: **the proposed three-row shape passes the exact coefficient, growing occurrence,
distinguished-block covariance, and common NO/YES legality gates.  In the closed stable range
`a>=r+1`, `d>=r`, `ad>=2r+1`,**

\[
 \boxed{
 [s_{(ad-r-1,r,1)}],s_{(a-1,1)}[h_d]
 =S_{r-2}:=\sum_{j=0}^{r-2}p(j),
 }
\]

with `S_t=0` for `t<0`.  On the legal critical family this supplies a deterministic growing
complete Hom-space in one common full group type.  Nevertheless, coupling that Hom-space to one
`L_d` alphabet cell leaves the right physical query on a disjoint cell.  On the three-row top
predecessor the position Gram is `1-o(1)`, while the exact opposite-cell positive raw effect is

\[
 P_z^{\rm opp}={q-1\over q(q-2)}(I-L_z).
\]

The occurrence index is exactly an identity factor in this right marked branch, not merely so on
average.  Consequently every nonzero occurrence multiplier has right off-equality query ratio
`1-o(1)`, incompatible with the required `O(m^(-1/6))` ratio.

Status discipline: proposer-tier analytic audit only.  This is a scoped failure of the complete
single-cell realization.  It does not give a completion-tier refutation of every joint alphabet,
multi-sector, or multi-full-type coupling of the growing three-row Hom-space.  The canonical node
therefore remains `OPEN` with `pending-review`.

## 1. Ordered decision and scope

The audit opens gates in the requested order.

1. Compute an all-large coefficient in `s_(a-1,1)[h_d]`, without extrapolating from finite
   plethysm tables.
2. Construct the complete occurrence space and its distinguished-block covariance.
3. Put the same deterministic channels in the exact NO and YES modules on an infinite legal
   critical family.
4. Type full raw restrictions, positive pulled effects, polar factors, and the NO/YES equality
   sandwiches on both physical sides.
5. Stop at the first physical norm obstruction, before outer incidence or numerator work.

The first three gates pass.  The fourth exposes a decisive opposite-side obstruction.  The
selected-side raw law is recorded in its exact operator-valued form, but no estimate of its
unknown recoupling operators is needed after the opposite side already fails.

## 2. Exact three-row block-standard coefficient

Let

\[
 \theta_r=(ad-r-1,r,1)\vdash ad,
 \qquad p(j)=\#\{\text{partitions of }j\},
 \qquad p(j)=0\ (j<0).
\tag{2.1}
\]

### 2.1 Pieri derivation in the clean interior

Put `A=a-1`.  The plethystic Jacobi--Trudi identity is

\[
 s_{(a-1,1)}[h_d]=h_A[h_d]h_d-h_a[h_d].
\tag{2.2}
\]

Suppose first that `a>=r+2` and `d>=r+1`.  A partition `mu` of `Ad` satisfies that
`theta_r/mu` is a horizontal `d`-strip exactly when

\[
 \mu=\mu_{j,0}=(Ad-j,j)
 \quad\text{or}\quad
 \mu=\mu_{j,1}=(Ad-j-1,j,1),
 \qquad 1\le j\le r.
\tag{2.3}
\]

Indeed horizontal-strip interlacing gives
`theta_1>=mu_1>=theta_2>=mu_2>=theta_3>=mu_3>=0`; hence
`mu_3` is zero or one and `1<=mu_2<=r`.  Size then forces (2.3), and the interior inequalities
make every listed shape legal.

For these near-top shapes, the exact stable coefficients in `h_M[h_d]` are

\[
 c_j:=[s_{(Md-j,j)}]h_M[h_d]=p(j)-p(j-1),
\tag{2.4}
\]

and

\[
 g_j:=[s_{(Md-j-1,j,1)}]h_M[h_d]
 =p(j)+p(j-1)-p(j+1).
\tag{2.5}
\]

Formula (2.4) is the difference of adjacent weight multiplicities in
`Sym^M(Sym^d C^2)`.  Formula (2.5) follows by taking the degree-one third-coordinate component of
`Sym^M(Sym^d(C^2 plus C))`, applying GL2 Pieri, and subtracting the two possible two-row parents.
Both are analytic rectangle formulas; no finite character table is used.

Pieri in (2.2) and (2.3) now gives

\[
 \begin{aligned}
 C_r
 &:=[s_{\theta_r}]s_{(a-1,1)}[h_d]\\
 &=\sum_{j=1}^{r}(c_j+g_j)-g_r\\
 &=p(r)-1+\sum_{j=1}^{r-1}
   \bigl(p(j)+p(j-1)-p(j+1)\bigr)\\
 &=\boxed{\sum_{j=0}^{r-2}p(j)}.
 \end{aligned}
\tag{2.6}
\]

Thus `C_1=0`, `C_2=1`, and `C_r>=r-1` for every `r>=2` in the stable range.

### 2.2 GL3 weight check and the closed stable boundary

The two boundary cases `a=r+1` and `d=r` require checking rectangle truncations rather than
silently invoking the clean-interior formulas.

Let `P_(M,D)(Y,Z)` count multisets of at most `M` nonzero tail vectors `(u,v)`, each satisfying
`u+v<=D`, with total `(Y,Z)`.  This is the `(MD-Y-Z,Y,Z)` weight multiplicity in `h_M[h_D]`.
Let `W(Y,Z)` be the corresponding weight multiplicity in the difference (2.2).  In the
unrestricted tail range, direct vector-partition counting gives

\[
 W(Y,0)=S_{Y-1},
 \qquad
 W(Y,1)=\sum_{j=0}^{Y}S_j.
\tag{2.7}
\]

For example, at `Z=0` the distinguished `h_d` monomial contributes
`sum_(u=0)^Y p(Y-u)=S_Y`, followed by subtraction of `p(Y)`.  At `Z=1`, separating whether the
distinguished monomial carries the unique unit of third-coordinate degree gives the second
identity.

GL3 Weyl alternation extracts the target coefficient as

\[
 C_r=W(r,1)-W(r+1,0)-W(r-1,1)+W(r-1,0).
\tag{2.8}
\]

Substitution of (2.7) again gives `C_r=S_(r-2)`.

It remains exact on the closed range

\[
 \boxed{a\ge r+1,qquad d\ge r,qquad ad\ge2r+1.}
\tag{2.9}
\]

To see the boundary cancellation, put `k=r+1`.  Every Weyl term in (2.8) except the two top terms
`(r,1)` and `(r+1,0)` has total tail weight at most `k-1` and is already stable.  For any
`Y+Z=k`, the unique cardinality truncation at `M=k-1` is the multiset containing `Y` copies of
`(1,0)` and `Z` copies of `(0,1)`.  The unique degree truncation at `D=k-1` is the singleton
`(Y,Z)`.  In the product `h_(a-1)[h_d]h_d`, these cause respectively one and two missing terms
(three when both boundaries occur); after subtracting `h_a[h_d]`, the net errors are respectively
one, one, and two.  Crucially, the error depends only on `k`, not on the split `(Y,Z)`.  The two
top terms in (2.8) have opposite signs, so their boundary errors cancel exactly.

No extension outside (2.9) is asserted.  Two analytic counterexamples prevent an unconditional
extrapolation:

* if `d=1`, then `s_(a-1,1)[h_1]=s_(a-1,1)`, so every genuine three-row target is absent although
  `S_(r-2)>0` for `r>=2`;
* if `a=2`, then `s_(1,1)[h_d]=exterior^2(Sym^d)` has only two-row constituents, by the
  multiplicity-free two-row decomposition of `Sym^d tensor Sym^d` and its swap parity.

### 2.3 Infinite legal critical family

For integers `s>=4`, choose

\[
 a=s^2,qquad d=4s+1,qquad r=s,qquad q=4a,qquad
 n=a(d+1),qquad N=2n.
\tag{2.10}
\]

This is the exact `p=0,u=1` critical family.  It satisfies

\[
 q^3=64s^6\le16s^4(2s+1)^2=N^2,
\tag{2.11}
\]

so `q<=N^(2/3)` and `q=Theta(N^(2/3))`.  The stable hypotheses (2.9) hold, and

\[
 C_s=S_{s-2}\ge s-1\longrightarrow\infty.
\tag{2.12}
\]

This growth follows from the exact coefficient formula; no numerical fit is used to infer an
exponent.

## 3. Deterministic complete covariant occurrence space

Let

\[
 W=S_d\wr S_a=S_d^a\rtimes S_a,
 \qquad V_a=S^{(a-1,1)},
 \qquad D=\dim V_a=a-1,
\tag{3.1}
\]

where `V_a` is inflated from the quotient `W -> S_a`.  Frobenius reciprocity identifies

\[
 Z_r^{\rm cov}
 :=\operatorname{Hom}_W(V_a,S^{\theta_r}),
 \qquad
 \dim Z_r^{\rm cov}=C_r=S_{r-2}.
\tag{3.2}
\]

This is a genuine distinguished-block covariant occurrence space: its induced characteristic is
`s_(a-1,1)[h_d]`, rather than the invariant characteristic `h_a[h_d]`.

A deterministic basis needs no optimization.  Fix real Young orthogonal bases, solve

\[
 \rho_{\theta_r}(w)T=T\rho_{V_a}(w)
\tag{3.3}
\]

for a standard generating set of `W`, vectorize solutions lexicographically, keep the first
independent solutions, and apply positive-leading-coordinate Gram--Schmidt for

\[
 \langle T,S\rangle={1\over D}\operatorname{Tr}(T^*S).
\tag{3.4}
\]

Write the result as `T_1,...,T_C`.  Schur's lemma and (3.4) give the operator identity

\[
 \boxed{T_h^*T_k=\delta_{hk}I_{V_a}.}
\tag{3.5}
\]

On the other position side use one wreath-invariant vector.  The exact invariant multiplicity is

\[
 g_r:=\dim(S^{\theta_r})^W
 =p(r)+p(r-1)-p(r+1)>0
 \qquad(r\ge4).
\tag{3.6}
\]

Apply the exact Reynolds projector, lexicographic column selection, and positive-leading
Gram--Schmidt to choose a deterministic unit vector `e_1` in this invariant space.

## 4. Exact common NO/YES embedding

Put

\[
 \lambda=(n-r-1,r,1)\vdash n,
 \qquad
 \zeta=(n-r-2,r,1)\vdash n-1.
\tag{4.1}
\]

The singleton attachments are coefficient-one horizontal-strip paths:

\[
 c^{\lambda}_{\theta_r,(a)}=1,
 \qquad
 c^{\zeta}_{\theta_r,(a-1)}=1,
 \qquad
 c^{\lambda}_{\zeta,(1)}=1.
\tag{4.2}
\]

Choose the positive-leading Young-basis Pieri isometries and denote them by
`Iota_(t,L)` and `Iota_(t,R)` for answer `t in {0,1}`.

Use the global alphabet carrier

\[
 V_q=S^{(q-1,1)}
 =\{x\in\mathbb C^q:\sum_zx_z=0\}.
\tag{4.3}
\]

For each answer, let `H^L_t` be the size-`a` left-heavy palette cell and let

\[
 V_{t,L}=\{x:\operatorname{supp}x\subseteq H^L_t,
                   \ \sum_{z\in H^L_t}x_z=0\}\cong V_a.
\tag{4.4}
\]

Fix the order-defined isometry `phi_t^L:V_a->V_(t,L)`.  If `f_1,...,f_D` is the fixed real
orthonormal basis of `V_a`, define, for every `1<=h<=C`,

\[
 j_t^L(h)={1\over\sqrt D}\sum_{i=1}^{D}
 \Iota_{t,L}(T_hf_i)\otimes
 \Iota_{t,R}(e_1)\otimes
 \phi_t^L(f_i).
\tag{4.5}
\]

Internal block permutations act through the intertwiner equation (3.3), the left block quotient
`S_a` acts diagonally on the first and third factors, the right wreath group fixes `e_1`, and all
singleton and other palette-cell groups act trivially.  Hence

\[
 j_t^L(h)\in M_t(\rho),
 \qquad
 \rho=(\lambda,\lambda,(q-1,1)).
\tag{4.6}
\]

Equation (3.5) makes these vectors orthonormal.  Therefore

\[
 J_t^L:\mathbb C^C\hookrightarrow M_t(\rho),
 \qquad J_t^Le_h=j_t^L(h),
\tag{4.7}
\]

is a deterministic isometry for both NO and YES, using the complete covariant occurrence space.
For arbitrary

\[
 B:E_0\to E_1,
 \qquad E_t=\mathbb C^C,
\tag{4.8}
\]

the selected full Fourier multiplier can be written

\[
 \Gamma_B=\mathcal J_1
 \left(I_{S^\lambda\boxtimes S^\lambda\boxtimes V_q}\otimes B\right)
 \mathcal J_0^*,
 \qquad \|\Gamma_B\|=\|B\|.
\tag{4.9}
\]

Thus coefficient growth has been converted into an actual common physical multiplicity, not a
presentation ancilla.

## 5. Three-row top heavy branch

The common parent `lambda` has three removable corners.  Select the top predecessor

\[
 \beta_T=(n-r-2,r,1).
\tag{5.1}
\]

The exact hook/down ratio is

\[
 \boxed{
 p_T={f^{\beta_T}\over f^\lambda}
 ={(n-r+1)(n-2r-1)(n-r-1)
   \over n(n-2r)(n-r)}.}
\tag{5.2}
\]

For physical side `s in {L,R}` and answer `t`, let

\[
 A_{t,T}^s:E_t\longrightarrow N_{t,T}^s,
 \qquad
 Q_{t,T}^s=A_{t,T}^{s*}A_{t,T}^s.
\tag{5.3}
\]

The exact heavy-coordinate fraction and Young restriction give

\[
 \sum_{\beta\nearrow\lambda}p_\beta Q_{t,\beta}^s
 ={d\over d+1}I_{E_t},
 \qquad 0\preceq Q_{t,\beta}^s\preceq I.
\tag{5.4}
\]

Bounding the two other terms by the identity yields

\[
 \boxed{
 Q_{t,T}^s\succeq\kappa_T I,
 \qquad
 \kappa_T=1-{1\over(d+1)p_T}.}
\tag{5.5}
\]

Write the polar decomposition as

\[
 A_{t,T}^s=U_{t,T}^sH_{t,T}^s,
 \qquad
 H_{t,T}^s\succeq\sqrt{\kappa_T}I.
\tag{5.6}
\]

On (2.10), `p_T=1-o(1)` and `kappa_T=1-o(1)`.  Therefore, for every rectangular, singular,
nonnormal, sign-changing, or noncommuting `B`,

\[
 \|H_{1,T}^sBH_{0,T}^s\|\ge\kappa_T\|B\|.
\tag{5.7}
\]

## 6. Raw restrictions, positive effects, and both equality sandwiches

This section separates three operator levels.  Conflating them would reproduce the type failure
found in an earlier candidate audit.

### 6.1 Full literal map and top pulled effect

Let `X_t` be the unmarked orbit model, `X_t^(s,#)` its exact marked-coordinate refinement,
`Ref_t^s:X_t->X_t^(s,#)` the normalized refinement isometry, and `D_(t,z)^s` the disjoint
projection onto raw marked value `z`.  Thus `sum_zD_(t,z)^s=I`.

On the selected full isotypic source

\[
 K_t=(S^\lambda\boxtimes S^\lambda\boxtimes V_q)\otimes E_t,
 \qquad
 \dim K_t=(f^\lambda)^2(q-1)C,
\tag{6.1}
\]

the **full literal restriction** is

\[
 \ell_{t,z}^s
 :=D_{t,z}^sRef_t^s\mathcal J_t:
 K_t\longrightarrow D_{t,z}^sX_t^{(s,\#)}.
\tag{6.2}
\]

Its positive effect and polar decomposition are

\[
 G_{t,z}^s=\ell_{t,z}^{s*}\ell_{t,z}^s,
 \qquad
 \ell_{t,z}^s=V_{t,z}^s(G_{t,z}^s)^{1/2}.
\tag{6.3}
\]

The NO and YES polar isometries `V_(0,z)^s` and `V_(1,z)^s` are not assumed equal.

After selecting `beta_T` and moving to the heavy polar source, put

\[
 \mathcal C_L=S^{\beta_T}\boxtimes S^\lambda\boxtimes V_q,
 \qquad
 \mathcal C_R=S^\lambda\boxtimes S^{\beta_T}\boxtimes V_q,
\tag{6.4}
\]

both of dimension `f^(beta_T)f^lambda(q-1)`.  Let `F_(t,z)^(s,T)` be the positive effect pulled to
`C_s tensor E_t`; it satisfies `F>=0` and `sum_zF=I`.  With

\[
 K_s=H_{1,T}^sBH_{0,T}^s,
 \qquad
 T_s^{\rm pol}=I_{\mathcal C_s}\otimes K_s,
\tag{6.5}
\]

the exact top-branch equality compression has the typed form

\[
 (I\otimes U_{1,T}^s)
 \left[\sum_zF_{1,z}^{(s,T)}T_s^{\rm pol}F_{0,z}^{(s,T)}\right]
 (I\otimes U_{0,T}^s)^*.
\tag{6.6}
\]

The factors `F` in (6.6) arise from compressing the row and column sides of the physical operator.
They are not the literal maps (6.2), and (6.6) uses neither square roots nor equality of the polar
isometries in (6.3).

### 6.2 Selected left side: exact operator-valued law

The selected-cell side must not be replaced by a bare alphabet frame.  Let
`eta_(t,h)^L in C_L` be the normalized top-marked invariant vector associated with occurrence
channel `h`.  The exact marked-group Fourier average gives the block effect

\[
 [Q_{t,z}^L]_{hk}
 =c_L\,\mathbb E_{g\in S_{n-1}\times S_n\times S_q}
 \left[
  \mathbf1[\pi_g\ell_{t,L}=z]\,
  \rho_{\mathcal C_L}(g)
  |\eta_{t,h}^L\rangle\langle\eta_{t,k}^L|
  \rho_{\mathcal C_L}(g)^*
 \right],
\tag{6.7}
\]

where `c_L=dim C_L`; equivalently sum (6.7) against `|h><k|` to obtain an operator on
`C_L tensor E_t`.  It is positive and `sum_zQ_(t,z)^L=I` by Schur orthogonality.

The point stabilizer restricts

\[
 V_q\downarrow S_{q-1}=\mathbf1\oplus S^{(q-2,1)}
\tag{6.8}
\]

with inequivalent summands.  Consequently there are formula-defined, possibly noncommuting and
answer-dependent operators

\[
 R_t,S_t\succeq0,
 \qquad R_t+S_t=I_{E_t},
\tag{6.9}
\]

such that, after suppressing unchanged Specht identities,

\[
 \boxed{
 Q_{t,z}^L=xL_z\otimes R_t+y(I-L_z)\otimes S_t,
 \quad
 x={q-1\over q},
 \quad
 y={q-1\over q(q-2)}.}
\tag{6.10}
\]

Here

\[
 u_z=\sqrt{q\over q-1}\left(e_z-{1\over q}\mathbf1\right),
 \qquad L_z=|u_z\rangle\langle u_z|.
\tag{6.11}
\]

Normalization follows exactly from

\[
 \sum_zL_z={q\over q-1}I,
 \qquad
 \sum_z(I-L_z)={q(q-2)\over q-1}I.
\tag{6.12}
\]

The selected-side equality sandwich is therefore

\[
 \boxed{
 \sum_zQ_{1,z}^L(I_{V_q}\otimes K_L)Q_{0,z}^L
 =I_{V_q}\otimes
 \left(xR_1K_LR_0+yS_1K_LS_0\right).}
\tag{6.13}
\]

The cross terms vanish because `L_z(I-L_z)=0`.  Formula (6.13) is the exact operator-valued
recoupling law.  Nothing here licenses setting `R_t` or `S_t` to a scalar, and no favorable norm
estimate is claimed.

### 6.3 Opposite right side: occurrence identity and decisive retained branch

For a right-heavy mark, the left covariant position carrier is untouched.  Equation (3.5) gives
the exact reduced operator

\[
 \boxed{
 \operatorname{Tr}_{S^\lambda_L}
 |j_t^L(h)\rangle\langle j_t^L(k)|
 =\delta_{hk}
  |\Iota_{t,R}(e_1)\rangle\langle\Iota_{t,R}(e_1)|
  \otimes{P_{t,L}\over D},}
\tag{6.14}
\]

where `P_(t,L)` projects onto `V_(t,L)`.  Thus the full growing occurrence index is exactly an
identity factor in this marked branch.  This is a consequence of the actual covariant tensors,
not a dimension or reduced-density guess.

The reference right-heavy label `ell_(t,R)` is outside `H_t^L`.  Averaging (6.14) over its point
stabilizer gives

\[
 \begin{aligned}
 P_{t,z}^{\rm opp}
 &={q-1\over q}{1\over(q-1)!}
   \sum_{h\in\operatorname{Stab}(\ell_{t,R})}
   \rho_{V_q}(\kappa_zh){P_{t,L}\over D}
   \rho_{V_q}(\kappa_zh)^*\\
 &=\boxed{y(I-L_z)},
 \qquad y={q-1\over q(q-2)}.
 \end{aligned}
\tag{6.15}
\]

The result is independent of the answer after canonical cell identification.  It satisfies

\[
 \sum_zP_{t,z}^{\rm opp}=I_{V_q},
 \qquad
 \sum_z(P_{t,z}^{\rm opp})^2=yI_{V_q}.
\tag{6.16}
\]

On the top polar source the pulled effect is

\[
 F_{t,z}^{(R,T)}
 =I_{S^\lambda\boxtimes S^{\beta_T}}
  \otimes P_z^{\rm opp}\otimes I_{E_t}.
\tag{6.17}
\]

The corresponding branch **compressed overlap** has the suppressed-carrier form

\[
 C_{t,z}^{(R,T)}=P_z^{\rm opp}\otimes A_{t,T}^R.
\tag{6.18}
\]

It is essential that (6.18) is not called the full literal raw map (6.2).  Its role is to produce
the double compression in (6.6).  Equations (6.16)--(6.18) give, for arbitrary `B`,

\[
 \begin{aligned}
 \sum_zF_{1,z}^{(R,T)}T_R^{\rm pol}F_{0,z}^{(R,T)}
 &=yT_R^{\rm pol},\\
 T_R^{\rm pol}-
 \sum_zF_{1,z}^{(R,T)}T_R^{\rm pol}F_{0,z}^{(R,T)}
 &=(1-y)T_R^{\rm pol}.
 \end{aligned}
\tag{6.19}
\]

Restoring the heavy polar isometries does not change the norm.  Combining (5.7) and (6.19),

\[
 \boxed{
 {\|\Gamma_B\circ\Delta_R\|\over\|\Gamma_B\|}
 \ge(1-y)\kappa_T
 =1-o(1).}
\tag{6.20}
\]

This holds uniformly for every nonzero occurrence matrix `B`.  Since `m=d+1->infinity`, (6.20)
is incompatible with `O(m^(-1/6))`.

## 7. Exact stopping point and relation to earlier sectors

The complete single `L_d`-cell construction is therefore obstructed, regardless of how favorable
the unresolved selected-side operators `R_t,S_t` in (6.10) might be.  Exchanging left and right
gives the mirror statement for every single `R_d`-cell construction.

Mechanistically, this is the shape-independent extension of the previously reviewed one-cell
obstruction: changing the two-row position parent to a three-row parent changes the occurrence
dimension and down ratio, but the disjoint physical side still sees an identity occurrence factor
and the same `y(I-L_z)` effect.  It is not literally covered by that review, whose licensed scope
fixed a two-row parent, so the present three-row result remains proposer-tier pending its own
Rule-7 review.

This artifact does not construct or audit an `L_d plus R_d` direct sum.  It therefore does not
silently import the separately DEAD two-row two-cell theorem to a new position parent.  Any
genuinely non-block-diagonal multi-sector or multi-full-type continuation lies outside this scoped
single-cell result and would need an already registered live node or a new Rule-8 node before
calculation.

The physical failure occurs before normalized incidence, coefficient norm, remainder control, or
the outer `a^(2/3)` numerator is opened.

## 8. Gate ledger

| Ordered gate | Outcome |
|---|---|
| exact three-row coefficient | **PASS:** `S_(r-2)`, (2.6) |
| closed stable range | **PASS:** `a>=r+1,d>=r,ad>=2r+1`, with boundary errors cancelled, (2.9) |
| outside-range hygiene | `d=1` and `a=2` give analytic non-extension examples |
| legal critical growth | **PASS:** `C_s>=s-1`, (2.10)--(2.12) |
| complete covariant occurrence | **PASS:** deterministic `Hom_W(V_a,S^theta)` basis, (3.2)--(3.5) |
| common NO/YES type | **PASS:** coefficient-one attachments and same `rho`, (4.1)--(4.9) |
| three-row top branch | `Q_(t,T)^s>=kappa_T I`, `kappa_T=1-o(1)`, (5.2)--(5.7) |
| full literal map versus effect | **TYPED:** (6.2)--(6.6); no polar-isometry equality assumed |
| selected-side law | exact noncommuting normal form (6.10)--(6.13); no scalar substitution |
| opposite-side occurrence action | exact identity on all `C=S_(r-2)` channels, (6.14) |
| opposite-side raw effect | exact `y(I-L_z)`, (6.15)--(6.17) |
| right equality sandwich | exact `yT_R`, (6.19) |
| simultaneous query target | **DECISIVE SCOPED FAIL:** right ratio `1-o(1)` for every `B`, (6.20) |
| outer incidence/numerator | not opened after physical failure |
| completion status | none; fresh independent Rule-7 review pending |

## 9. Frozen-source ledger

* Exact hidden-frequency histograms, stabilizers, and legal parameter range:
  `ksum/artifacts/ksum_L3_hidden_frequency_promise_20260721.md`, SHA-256
  `558E0B6D8F9F65072B4F5E6E360967092D3B9BF0C3F5A2495124A678DBF8ACEB`.
* Exact position-incidence orbit classification and marked-coordinate groups:
  `ksum/artifacts/ksum_L3_critical_full_position_incidence_orbit_classification_20260722.md`, SHA-256
  `A22D513B66D50635E76C6A2707AC3FC5EE657676FFEEA0C0B68B9EE6EDC2A088`.
* Trivial-block three-row coefficient, invariant occurrence, singleton attachments, and top
  down-ratio derivation:
  `ksum/artifacts/ksum_L3_critical_nonscaled_plethystic_many_corner_candidate_audit_20260722.md`,
  SHA-256 `1F63B8E2D652EF3E423AB2EB19A299E90D6B74EFE2FEE3702C09C7A3E3E0F624`.
* Reviewed two-row single-cell Hom normalization and disjoint-cell Fourier frame:
  `ksum/artifacts/ksum_L3_critical_covariant_block_standard_occurrence_mixing_audit_20260722.md`,
  SHA-256 `62387C00A63C1D54DE7947E17446EC2B5EF714C27A794B3E800CDCD46570A515`, and
  `ksum/artifacts/ksum_L3_critical_covariant_block_standard_occurrence_mixing_rule7_review_20260722.md`,
  SHA-256 `3A29313A8CBBD01038D670CF67A71F835CCAC96FC61A3A0E854064EEFF6CB1DF`.
* Scoped two-row two-cell theorem, cited only to delimit what is **not** imported here:
  `ksum/artifacts/ksum_L3_critical_two_cell_covariant_cross_sector_mixing_audit_20260722.md`, SHA-256
  `73488FF77EDDA7E2497B31D7EA5F0E6EB1307D4A49C364D733BDE17FCEEF790C`, and its Rule-7 review,
  SHA-256 `4110A19C34E9C09E237D1FBB72E756887B0DB5F516C5908E61DE5682E7F9DC9B`.

All new coefficient, boundary-stability, occurrence, common-embedding, operator-valued selected
law, and three-row opposite-query statements in this memo are analytic.  No finite plethysm table
or numerical exponent inference is used.
