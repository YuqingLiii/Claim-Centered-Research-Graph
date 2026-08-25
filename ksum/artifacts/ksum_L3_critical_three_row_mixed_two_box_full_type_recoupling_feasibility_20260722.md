# L3 critical endpoint: mixed two-box full-type recoupling feasibility audit

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-mixed-two-box-full-type-recoupling-kernel`

Verdict: **the two legal unmarked two-box blocks do share the marked alphabet type
`tau=(q-2,1)`, and their deterministic restriction phases differ by a sign between left and right
marks.  Nevertheless the proposed mixed-full-type cancellation has a uniform physical
obstruction.**  The tempting carrier identity

\[
 \alpha_++\alpha_-
 =1-{q-1\over q(q-2)},
 \qquad
 \alpha_+={q-3\over2(q-2)},
 \quad
 \alpha_-={q-1\over2q},
\]

omits the occurrence mass of the selected bicovariant cell tensor in the shared point branch.
For a heavy palette cell of size `a`, those exact masses are

\[
 r_+={q-2\over a(q-3)},
 \qquad
 r_-={q\over a(q-1)},
\]

and therefore

\[
 \boxed{\alpha_+r_+=\alpha_-r_-={1\over2a}.}
\]

The full raw-value effect is a `2 x 2` matrix in the `nu_+,nu_-` index.  Its common off-diagonal
blocks have sign `sigma_L=+1` and `sigma_R=-1`, but all off-diagonal **full-`S_q`** output blocks
vanish after the equality sum over raw labels.  The surviving diagonal equality blocks have norm
only `O(1/a)` of the unmasked coefficient.  On the legal critical family

\[
 a=s^2,\quad d=4s+1,\quad q=4a,\quad r=s,
\]

each physical query retains `1-o(1)` of every nonzero mixed multiplier.  Hence the mixed pair
cannot have query ratio `O(m^(-1/6))`.

Status discipline: proposer-tier analytic audit only.  No `REFUTED`, `CERTIFIED*`, or `PROVED`
status is asserted without a fresh Rule-7 review.  Incidence, numerator, and remainder work is not
opened after the uniform query obstruction.

## 1. Scope, endpoint, and legal unmarked multiplier

Use the exact critical family

\[
 a=s^2,\qquad d=4s+1,\qquad r=s,\qquad q=4a,
 \qquad n=a(d+1),\qquad N=2n,
 \qquad s\ge4.
\tag{1.1}
\]

It satisfies `q^3<=N^2`, `q=Theta(N^(2/3))`, and the stable three-row conditions
`a>=r+1`, `d>=r`, `ad>=2r+1`.

Let

\[
 \nu_+=(q-2,2),\qquad \nu_-=(q-2,1,1),
 \qquad \rho_\epsilon=(\lambda,\lambda,\nu_\epsilon),
\tag{1.2}
\]

where `lambda=(n-r-1,r,1)`.  The previous single-carrier audit constructs deterministic common
NO/YES occurrence isometries

\[
 J_t^\epsilon:E_{t,\epsilon}\hookrightarrow M_t(\rho_\epsilon),
 \qquad \epsilon\in\{+,-\}.
\tag{1.3}
\]

The selected spaces `E_(t,+)` and `E_(t,-)` may have different dimensions in either answer and
need not agree across answers.  Let

\[
 B_+:E_{0,+}\longrightarrow E_{1,+},
 \qquad
 B_-:E_{0,-}\longrightarrow E_{1,-}
\tag{1.4}
\]

be arbitrary rectangular, nonnormal, noncommuting coefficient maps.

The only legal unmarked invariant adversary in this scope is the **sum of two separate full-type
blocks**

\[
 \begin{aligned}
 \Gamma
 =&\ \mathcal J_1^+
   (I_{S^\lambda\boxtimes S^\lambda\boxtimes S^{\nu_+}}\otimes B_+)
   \mathcal J_0^{+*}\\
 &+\mathcal J_1^-
   (I_{S^\lambda\boxtimes S^\lambda\boxtimes S^{\nu_-}}\otimes B_-)
   \mathcal J_0^{-*}.
 \end{aligned}
\tag{1.5}
\]

There is no unmarked map between `nu_+` and `nu_-`; they are inequivalent `S_q` irreps.  Thus

\[
 \|\Gamma\|=\max\{\|B_+\|,\|B_-\|\}.
\tag{1.6}
\]

All possible mixing below is created only by literal raw-value restriction and disappears again
where full alphabet equivariance forces it to.

## 2. Deterministic point restriction and relative phases

### 2.1 Standard-space model

Let

\[
 V=\left\{x\in\mathbb C^q:\sum_ix_i=0\right\}=S^{(q-1,1)}
\]

with its real Euclidean structure.  For a distinguished raw label `z`, put

\[
 u_z=\sqrt{q\over q-1}\left(e_z-{1\over q}\mathbf1\right),
 \qquad
 W_z=u_z^\perp\cap V.
\tag{2.1}
\]

Then `W_z` is the `S_(q-1)` standard type `tau=(q-2,1)`.

For `w in W_z`, define normalized symmetric and alternating tensors

\[
 S_z(w)={u_z\otimes w+w\otimes u_z\over\sqrt2},
 \qquad
 A_z(w)={u_z\otimes w-w\otimes u_z\over\sqrt2}.
\tag{2.2}
\]

Write `u_i` for (2.1) with `z=i`.  The normalized global-standard copy inside
`Sym^2(V)` is

\[
 \mathcal J(w)={q-1\over\sqrt{q(q-2)}}
 \sum_{i=1}^q w_i\,u_i\otimes u_i.
\tag{2.3}
\]

For unit `w in W_z`, direct frame calculation gives

\[
 \langle\mathcal J(w),S_z(w)\rangle
 =-\eta,
 \qquad
 \eta=\sqrt{2\over(q-1)(q-2)}.
\tag{2.4}
\]

Put

\[
 p=\sqrt{1-\eta^2}
 =\sqrt{q(q-3)\over(q-1)(q-2)}.
\tag{2.5}
\]

The deterministic common-branch restriction isometries are

\[
 \boxed{
 I_{+,z}(w)={S_z(w)+\eta\mathcal J(w)\over p}
 :W_z\hookrightarrow S^{\nu_+},
 }
\tag{2.6}
\]

and

\[
 \boxed{
 I_{-,z}(w)=A_z(w):W_z\hookrightarrow S^{\nu_-}.
 }
\tag{2.7}
\]

They realize the exact point branching

\[
 S^{\nu_+}\downarrow S_{q-1}
 =S^{(q-2,1)}\oplus S^{(q-3,2)},
\tag{2.8}
\]

\[
 S^{\nu_-}\downarrow S_{q-1}
 =S^{(q-2,1)}\oplus S^{(q-3,1,1)}.
\tag{2.9}
\]

All phases in (2.6)--(2.7) are fixed by the displayed real formulas, not by matching irrep names.

### 2.2 Restricting the selected cell tensor

Let `H_L,H_R` be the disjoint left- and right-heavy palette cells, each of size `a`.  For
`z in H_L`, the normalized point-fixed vector in `Std(H_L)` is

\[
 v_{L,z}=\sqrt{a\over a-1}
 \left(e_z-{1\over a}\mathbf1_{H_L}\right).
\tag{2.10}
\]

Its overlap with the global point vector is

\[
 c:=\langle u_z,v_{L,z}\rangle
 =\sqrt{q(a-1)\over a(q-1)}.
\tag{2.11}
\]

For unit `y in Std(H_R)`, disjoint support and the zero-sum conditions give

\[
 \left\langle\mathcal J(y),
 {v_{L,z}\otimes y+y\otimes v_{L,z}\over\sqrt2}
 \right\rangle=0.
\tag{2.12}
\]

Therefore the symmetric and alternating cell-tensor embeddings satisfy

\[
 I_{+,z}^*\Phi_+(v_{L,z}\otimes y)={c\over p}y,
 \qquad
 I_{-,z}^*\Phi_-(v_{L,z}\otimes y)=c\,y.
\tag{2.13}
\]

For a right-heavy mark `z in H_R`, the symmetric formula is unchanged, whereas

\[
 \Phi_-(x\otimes v_{R,z})=x\wedge v_{R,z}
 =-v_{R,z}\wedge x.
\]

Thus the exact relative phases are

\[
 \boxed{\sigma_L=+1,\qquad\sigma_R=-1.}
\tag{2.14}
\]

The sign is independent of the answer `t`; canonical cell ordering is used in both NO and YES.
Answer-dependent rephasing of a deterministic occurrence basis only conjugates the formulas below
and does not affect the norm bound.

## 3. The missing occurrence mass

Let

\[
 D=\dim\operatorname{Std}_a=a-1.
\tag{3.1}
\]

The bicovariant invariant uses the normalized double coevaluation.  After a left mark, projecting
the left alphabet standard onto (2.10) selects one vector out of the `D`-dimensional left
coevaluation; the untouched right coevaluation remains normalized.  Equations (2.13) therefore
give the exact shared-branch occurrence masses

\[
 r_+={1\over D}{c^2\over p^2}
 =\boxed{{q-2\over a(q-3)}},
\tag{3.2}
\]

\[
 r_-={1\over D}c^2
 =\boxed{{q\over a(q-1)}}.
\tag{3.3}
\]

The right mark gives the same masses and only changes the cross phase (2.14).

The carrier coefficients attached to the common point type are

\[
 \alpha_+={f^{\nu_+}\over qf^\tau}
 ={q-3\over2(q-2)},
 \qquad
 \alpha_-={f^{\nu_-}\over qf^\tau}
 ={q-1\over2q}.
\tag{3.4}
\]

Their unweighted sum is indeed

\[
 \alpha_++\alpha_-
 =1-{q-1\over q(q-2)}.
\tag{3.5}
\]

But the physical common effect contains the occurrence masses (3.2)--(3.3), and

\[
 \boxed{
 \alpha_+r_+=\alpha_-r_-={1\over2a}.
 }
\tag{3.6}
\]

Thus the two common raw-effect weights add to `1/a`, not to `1-O(1/q)`.

For later use, the private point-branch coefficients are

\[
 \delta_+={q-3\over(q-1)(q-4)},
 \qquad
 \delta_-={q-1\over q(q-3)}.
\tag{3.7}
\]

Both are `O(1/q)` on (1.1).

## 4. Literal maps, top polar sources, and occurrence operators

For answer `t`, side `s`, carrier `epsilon`, and raw value `z`, let

\[
 \ell_{t,z}^{s,\epsilon}:
 (S^\lambda\boxtimes S^\lambda\boxtimes S^{\nu_\epsilon})
 \otimes E_{t,\epsilon}
 \longrightarrow D_{t,z}^sX_t^{(s,\#)}
\tag{4.1}
\]

be the literal normalized refinement followed by raw-value projection.  Its positive effect is
`G_(t,z)^(s,epsilon)=ell^*ell`; no effect is identified with the rectangular map itself.

Select the top position predecessor

\[
 \beta_T=(n-r-2,r,1).
\tag{4.2}
\]

For either full alphabet type, the top heavy restriction on the selected occurrence space has
polar decomposition

\[
 A_{t,T}^{s,\epsilon}=U_{t,T}^{s,\epsilon}H_{t,T}^{s,\epsilon},
 \qquad
 H_{t,T}^{s,\epsilon\,2}\succeq\kappa_T I,
\tag{4.3}
\]

where

\[
 \kappa_T=1-{1\over(d+1)p_T},
\qquad
 p_T={(n-r+1)(n-2r-1)(n-r-1)
 \over n(n-2r)(n-r)}.
\tag{4.4}
\]

Also `H<=I`, and `kappa_T=1-o(1)` on (1.1).

Put

\[
 K_\epsilon^s
 =H_{1,T}^{s,\epsilon}B_\epsilon H_{0,T}^{s,\epsilon}.
\tag{4.5}
\]

Then

\[
 \kappa_T\|B_\epsilon\|
 \le\|K_\epsilon^s\|\le\|B_\epsilon\|.
\tag{4.6}
\]

Let `M_(t,epsilon)^(s,0)` be the unpolarized restriction of the selected invariant to the common
point branch.  Equations (2.13) and the coevaluation normalization give, in deterministic common
marked bases,

\[
 M_{t,+}^{s,0}={c/p\over\sqrt D}\,Q_{t,v}^s,
 \qquad
 M_{t,-}^{s,0}=\sigma_s{c\over\sqrt D}\,Q_{t,v}^s,
\tag{4.7}
\]

where `Q_(t,v)^s` is the formula-defined marked position contraction, with operator norm at most
one.  For arbitrary selected subspaces, (4.7) is compressed by their deterministic inclusions.

After transport to the top polar sources, define

\[
 R_{t,\epsilon}^s:E_{t,\epsilon}\to E_{t,\epsilon}
\]

as the positive common-branch reduced Gram and

\[
 C_t^s:E_{t,-}\to E_{t,+}
\]

as the cross reduced Gram, with the sign `sigma_s` kept outside `C_t^s`.  Formula (4.7) and
(4.3) give

\[
 0\preceq R_{t,+}^s\preceq {r_+\over\kappa_T}I,
 \qquad
 0\preceq R_{t,-}^s\preceq {r_-\over\kappa_T}I,
\tag{4.8}
\]

\[
 \boxed{
 \|C_t^s\|\le{\sqrt{r_+r_-}\over\kappa_T}.
 }
\tag{4.9}
\]

The remaining private-branch reduced Grams are

\[
 S_{t,\epsilon}^s=I-R_{t,\epsilon}^s,
 \qquad 0\preceq S_{t,\epsilon}^s\preceq I.
\tag{4.10}
\]

Equations (4.7)--(4.10) are valid for occurrence multiplicity one, multiplicity greater than one,
unequal selected ranks, and arbitrary compressions of the full `C_r^2` common space.

## 5. Full `2 x 2` raw-value effect

Let

\[
 \Pi_{\epsilon,z}=I_{\epsilon,z}I_{\epsilon,z}^*
\tag{5.1}
\]

be the common point-branch projector in `S^(nu_epsilon)`, let
`Xi_(epsilon,z)=I-Pi_(epsilon,z)` be its private point-branch projector, and put

\[
 X_z=I_{+,z}I_{-,z}^*:S^{\nu_-}\longrightarrow S^{\nu_+}.
\tag{5.2}
\]

After suppressing the unchanged marked position Specht identities, the complete pulled positive
raw-value effect on

\[
 (S^{\nu_+}\otimes E_{t,+})\oplus
 (S^{\nu_-}\otimes E_{t,-})
\]

is

\[
 \boxed{
 F_{t,z}^s=
 \begin{pmatrix}
 \alpha_+\Pi_{+,z}\otimes R_{t,+}^s
 +\delta_+\Xi_{+,z}\otimes S_{t,+}^s
 &
 \sigma_s\sqrt{\alpha_+\alpha_-}\,X_z\otimes C_t^s
 \\
 \sigma_s\sqrt{\alpha_+\alpha_-}\,X_z^*\otimes C_t^{s*}
 &
 \alpha_-\Pi_{-,z}\otimes R_{t,-}^s
 +\delta_-\Xi_{-,z}\otimes S_{t,-}^s
 \end{pmatrix}.
 }
\tag{5.3}
\]

Every block in (5.3) is typed: the diagonal blocks act on their own full-type source, while the
upper-right block maps `S^(nu_-) tensor E_(t,-)` to
`S^(nu_+) tensor E_(t,+)`.  It is a **marked effect**, not an illegal unmarked intertwiner.

The exact Schur sums are

\[
 \sum_z\Pi_{\epsilon,z}={1\over\alpha_\epsilon}I_{\nu_\epsilon},
 \qquad
 \sum_z\Xi_{\epsilon,z}={1\over\delta_\epsilon}I_{\nu_\epsilon},
\tag{5.4}
\]

and

\[
 \boxed{\sum_zX_z=0.}
\tag{5.5}
\]

The last identity holds because its left side is an `S_q` intertwiner from the inequivalent
`nu_-` irrep to `nu_+`.  Hence `sum_zF_(t,z)^s=I` exactly.  Formula (5.3) includes both diagonal
and off-diagonal raw blocks and retains the left/right sign instead of discarding it in a
dimension count.

## 6. Full equality superoperator

On the top polar source, write

\[
 T_s=\operatorname{diag}
 \left(I_{\nu_+}\otimes K_+^s,
       I_{\nu_-}\otimes K_-^s\right).
\tag{6.1}
\]

For one raw value, all four output blocks are

\[
 \begin{aligned}
 [F_{1,z}^sT_sF_{0,z}^s]_{++}
 &=F_{1,z}^{++}T_+F_{0,z}^{++}
   +F_{1,z}^{+-}T_-F_{0,z}^{-+},\\
 [F_{1,z}^sT_sF_{0,z}^s]_{+-}
 &=F_{1,z}^{++}T_+F_{0,z}^{+-}
   +F_{1,z}^{+-}T_-F_{0,z}^{--},\\
 [F_{1,z}^sT_sF_{0,z}^s]_{-+}
 &=F_{1,z}^{-+}T_+F_{0,z}^{++}
   +F_{1,z}^{--}T_-F_{0,z}^{-+},\\
 [F_{1,z}^sT_sF_{0,z}^s]_{--}
 &=F_{1,z}^{-+}T_+F_{0,z}^{+-}
   +F_{1,z}^{--}T_-F_{0,z}^{--}.
 \end{aligned}
\tag{6.2}
\]

Common/private cross terms inside one carrier vanish because `Pi_(epsilon,z) Xi_(epsilon,z)=0`.
After summing over `z`, (5.5) kills both off-diagonal full-type outputs:

\[
 \boxed{
 \left[\sum_zF_{1,z}^sT_sF_{0,z}^s\right]_{+-}
 =\left[\sum_zF_{1,z}^sT_sF_{0,z}^s\right]_{-+}=0.
 }
\tag{6.3}
\]

The two surviving diagonal occurrence operators are exactly

\[
 \boxed{
 \begin{aligned}
 \mathcal E_+^s
 =&\ \alpha_+R_{1,+}^sK_+^sR_{0,+}^s
 +\alpha_-C_1^sK_-^sC_0^{s*}
 +\delta_+S_{1,+}^sK_+^sS_{0,+}^s,\\
 \mathcal E_-^s
 =&\ \alpha_-R_{1,-}^sK_-^sR_{0,-}^s
 +\alpha_+C_1^{s*}K_+^sC_0^s
 +\delta_-S_{1,-}^sK_-^sS_{0,-}^s.
 \end{aligned}
 }
\tag{6.4}
\]

The transfer coefficient is the coefficient of the **input** full type; this follows, for
example, from

\[
 \alpha_+\alpha_-\sum_zX_zX_z^*
 =\alpha_-I_{\nu_+}.
\tag{6.5}
\]

The signs `sigma_s` occur twice in every diagonal transfer term and therefore square to `+1`.
They flip the per-value off-diagonal raw blocks between left and right, but those blocks vanish in
the legal equality sum by (6.3).  Thus there are not two opposite scalar cancellation equations
to solve; the obstruction below is the small common occurrence mass.

Restoring the row and column heavy polar isometries preserves every norm in (6.3)--(6.4).

## 7. Uniform constant-retention obstruction

Let

\[
 M_B=\max\{\|B_+\|,\|B_-\|\}.
\tag{7.1}
\]

Using (4.6), (4.8)--(4.10), and (3.6), the first line of (6.4) obeys

\[
 \begin{aligned}
 \|\mathcal E_+^s\|
 &\le
 \left[
 \delta_+
 +{\alpha_+r_+^2+\alpha_-r_+r_-\over\kappa_T^2}
 \right]M_B\\
 &=\boxed{
 \left[\delta_+ +{r_+\over a\kappa_T^2}\right]M_B.
 }
 \end{aligned}
\tag{7.2}
\]

Similarly,

\[
 \boxed{
 \|\mathcal E_-^s\|
 \le\left[\delta_-+{r_-\over a\kappa_T^2}\right]M_B.
 }
\tag{7.3}
\]

Define

\[
 \varepsilon_a=max\left\{
 \delta_+ +{r_+\over a\kappa_T^2},
 \delta_- +{r_-\over a\kappa_T^2}
 \right\}.
\tag{7.4}
\]

Choose `epsilon_0` with `||B_(epsilon_0)||=M_B`.  Compressing the queried operator to its
`nu_(epsilon_0)` diagonal top branch and using (4.6) gives

\[
 \begin{aligned}
 \|\Gamma\circ\Delta_s\|
 &\ge\|K_{\epsilon_0}^s-\mathcal E_{\epsilon_0}^s\|\\
 &\ge(\kappa_T-\varepsilon_a)M_B.
 \end{aligned}
\tag{7.5}
\]

Together with (1.6), for `s=L` and separately for `s=R`,

\[
 \boxed{
 {\|\Gamma\circ\Delta_s\|\over\|\Gamma\|}
 \ge\kappa_T-\varepsilon_a.
 }
\tag{7.6}
\]

On `q=4a`,

\[
 \delta_+={4a-3\over(4a-1)(4a-4)},
 \qquad
 \delta_-={4a-1\over4a(4a-3)},
\tag{7.7}
\]

and `r_+,r_-=Theta(1/a)`.  Hence

\[
 \varepsilon_a=O(1/a),
 \qquad
 \kappa_T=1-O(1/d),
\tag{7.8}
\]

so along (1.1)

\[
 \boxed{
 {\|\Gamma\circ\Delta_L\|\over\|\Gamma\|},
 {\|\Gamma\circ\Delta_R\|\over\|\Gamma\|}
 \ge1-o(1).
 }
\tag{7.9}
\]

This is incompatible with `O(m^(-1/6))` because `m=d+1->infinity`.

## 8. Decision on the tempting coefficient identity

The identity (3.5) is correct, but it concerns only the dimensions of the two global alphabet
carriers relative to their shared point type.  It does not measure how much of the **selected
cell-covariant invariant** reaches that point type.  The double coevaluation contributes the
missing factor `1/D`, and the explicit restriction amplitudes contribute `c^2/p^2` or `c^2`.
Their products reduce both effective weights exactly to `1/(2a)`.

The symmetric/antisymmetric swap signs are also real and unavoidable: `sigma_L=+1` and
`sigma_R=-1`.  They do not create incompatible surviving diagonal cancellation equations,
because every legal diagonal equality transfer contains the sign twice, while every off-diagonal
full-type output is killed by full-`S_q` Schur orthogonality.  Thus no coefficient choice can
exploit (3.5) on even one side, let alone both sides; the common channel is too small before the
phase question could help.

## 9. Multiplicity, rank, and legality regimes

- `C=1`: choose one occurrence in each carrier.  All maps above become scalars or rectangular
  one-row/one-column maps, and (7.6) is unchanged.
- `C>1`: the exact three-row occurrence dimension is
  `C_r=sum_(j=0)^(r-2)p(j)`, and the full bicovariant space has dimension `C_r^2`.  Equations
  (4.8)--(7.6) are operator inequalities on the complete multiplicity, not trace checks.
- Unequal ranks: `E_(t,+)` and `E_(t,-)` may all have different dimensions.  The cross reduced
  Gram `C_t^s:E_(t,-)->E_(t,+)` is rectangular, and (4.9), (6.4), and (7.2)--(7.6) remain valid.
- Noncommuting coefficients: no simultaneous diagonalization or relation between `B_+` and `B_-`
  is used.
- Critical legality: (1.1) has `q=4a>=64`, so every branching dimension and denominator in this
  audit is positive.  The route is a critical `q=Theta(N^(2/3))` donor candidate, not a claim about
  the separately handled `q=5` or `q=N` project endpoints.

## 10. Exact stopping point

The mixed-full-type raw-query gate fails uniformly before normalized incidence, coefficient
optimization, remainder control, or the outer numerator is opened.  No endpoint exponent changes.

The result is scoped to the complete registered architecture: separate legal unmarked
`nu_+`/`nu_-` multipliers coupled to the selected three-row bicovariant cell tensor, with arbitrary
occurrence matrices and every cross-full-type marked block retained.  It does not claim a no-go
for other alphabet partitions, more than two full types, or a different position parent.

## 11. Gate ledger

| Ordered obligation | Outcome |
|---|---|
| legal unmarked construction | separate diagonal `nu_+` and `nu_-` blocks only, (1.5) |
| deterministic common point isometries | (2.6)--(2.7) |
| left/right relative phase | `sigma_L=+1`, `sigma_R=-1`, (2.14) |
| common occurrence masses | exact `r_+,r_-`, (3.2)--(3.3) |
| tempting coefficient sum | algebraically correct but physically incomplete, (3.5)--(3.6) |
| literal map/effect separation | (4.1), (5.3) |
| `c=1` and `c>1` | both covered by operator identities |
| unequal NO/YES and `+/-` ranks | rectangular maps explicitly typed |
| full raw `2 x 2` effect | all diagonal/off-diagonal blocks in (5.3) |
| all four per-value equality outputs | (6.2) |
| summed off-diagonal full-type outputs | exactly zero by Schur, (6.3) |
| surviving diagonal superoperator | exact formula (6.4) |
| arbitrary noncommuting `B_+,B_-` | uniform bounds (7.2)--(7.6) |
| both physical sides | **DECISIVE SCOPED FAIL**, ratio `1-o(1)`, (7.9) |
| incidence/numerator/remainders | not opened after physical failure |
| completion-tier status | none; fresh Rule-7 review pending |

## 12. Frozen-source ledger

* Single-full-type branching, bicovariant occurrence, point coefficients, and literal-map
  conventions:
  `ksum/artifacts/ksum_L3_critical_three_row_bicovariant_two_cell_alphabet_feasibility_20260722.md`,
  SHA-256 `537973EF787B96B97AA65EC2AAEDB94B7964B31FC6B7F2AB565AA2768104EC79`.
* Independent ordered-pair branching cross-check:
  `ksum/artifacts/ksum_L3_critical_two_box_branching_independent_crosscheck_20260722.md`, SHA-256
  `72185D1BADCC4A1EDC929970D528152233DAEA6D0AACD8ABC65A683A4F26CFBA`.
* Three-row coefficient, deterministic occurrence intertwiners, common NO/YES attachments, and
  top-branch Gram bound:
  `ksum/artifacts/ksum_L3_critical_three_row_block_standard_covariant_feasibility_20260722.md`, SHA-256
  `3FE61B416E5C0C8AB84FEF1940F9BFB9A4513CADCAC9AC40BC611FAECE71B0DD`.

Every new point-isometry, phase, occurrence-mass, raw-effect, equality-superoperator, and norm
statement in this artifact is analytic.  No numerical value fit or dimension-only cancellation
claim supports the verdict.
