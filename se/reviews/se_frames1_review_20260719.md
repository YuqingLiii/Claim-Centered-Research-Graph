# Independent adversarial review of `se_frames1_20260719.md`

Date: 2026-07-19  
Role: independent reviewer under DAG protocol rules 6 and 7  
Object: foundational-layer rebuild R1, `se/artifacts/se_frames1_20260719.md`  
Human-review baseline read first: `se/artifacts/se_human_review_20260719.md`  
Source of the literal BR block: `se/artifacts/references/BR_1310.5185v4_collision.tex:522-553`

## 0. Bottom line

R1 repairs the mathematics of the admissible range, the operator-level
colored-orbit isolation, the honest full-space transport, and the
axial-distance off-by-one. I found no counterexample to those claims. The
literal BR kernel also has the diagonal covariance needed for the full
matching twirl, and the resulting Schur statement is valid on the complete
carrier, including arbitrary LR multiplicity.

Two documentation/type-construction gaps prevent blanket completion:

1. Section 5 never defines the Fourier kernel `widehat b_0`, the matching
   encoding `r_h`, the completion projector, the left output action, or the
   `sigma dot h` reindexing as actual formulas. I reconstructed them from the
   literal BR block and obtained the claimed identities, but R1 itself does
   not meet rule 7(g) at these displays.
2. The maps in (6.5) are described by properties rather than constructed.
   If those properties are assumed, (6.6) is a correct contraction argument
   with no factor `c`; R1 correctly says that identification with the eventual
   physical/output-frame map is still open. Thus (6.5)-(6.6) are not a proved
   physical-map statement.

The required independent `c>=2` matrix gate remains open. My stretch built
the exact `1120 x 1120` subgroup-fixed kill matrices on
`V_(3,2,1) tensor V_(4,2,1) tensor C^2`, but did not build
`P_xi Pi_D P_xi` or `B_h`: the missing object is precisely the LR
subduction/recoupling for non-`H`-normalizing maps. This corroborates R1's
stated obstruction but does not close rule 7(b).

One review-process caveat is material. While extracting the W2 statement, I
also exposed R1's short proof before recording my own W2 derivation. I then
reconstructed W2 from branching and subgroup averages and independently
matrix-tested it, but this W2 portion is chronologically contaminated under
rule 7(c). Therefore this report must not be the sole review cited for a
completion-tier promotion of W2. I record the coincidence rather than hiding
it.

## 1. Definitions and complete type audit

Use the following dimensions throughout:

\[
F=f^\lambda,\quad d=f^\kappa f^\nu,\quad c=c_{\alpha\beta}^\theta,
\quad D_\xi=dc,\quad r=f^\theta,
\]

\[
r_+=f^{\lambda/(q-j-1)},\quad
R=f^{\lambda/(n)},\quad
T=\binom{n-1}{a}\binom{n-1-a}{b}f^\alpha f^\beta,
\]

\[
M={q!f^\alpha f^\beta\over(q-j)!a!b!}.
\]

All dependences on `c` are explicit below.

| R1 display | Independently recomputed type | Result |
|---|---|---|
| (1.1) | Equality of groups of order `(n-1)! n!`; its represented operators on `V_lambda` are `F x F`. | Typed. |
| (2.1) | `Hom_H(V_kappa box V_nu,V_lambda)` has dimension `c`; `P_xi V_lambda` and `(V_kappa box V_nu) tensor C^c` both have dimension `D_xi=dc`. | Typed for every `c`. `P_xi` should have been explicitly defined. |
| (4.1) | `Pi_D^lambda: V_lambda -> V_lambda`, size `F x F`; rank `r` for `|D|=j`, rank `r_+` for `|D|=j+1`. | Typed. |
| (4.2) | `Pi_D P_xi` is `F x F` with effective domain dimension `D_xi`; `P_xi Pi_D P_xi` restricts to a `D_xi x D_xi` operator. | Typed for every `c`. |
| (4.3)-(4.4) | Both sides are `F x F`; compression/restriction gives `D_xi x D_xi`. | Typed for every `c`. |
| (5.1) | With co-restrictions understood, `P_xi: V -> C` is `D_xi x F`, `widehat b_h` is `F x F`, `P_comp: V -> O` is `R x F`, hence `B_h` is `R x D_xi` and `G` is `D_xi x D_xi`. | Dimensionally typed. Several constituent maps are not formally defined in R1. |
| (5.2) | `rho_C(pi)` is `D_xi x D_xi`; both sides are `R x D_xi`. | Typed for every `c`. |
| (5.3) | Three `F x F` endomorphisms of `V_lambda`. | Typed. |
| (5.4) | `rho_C(sigma)` is `D_xi x D_xi`, `L_(sigma,h)` is `R x R`; both sides are `R x D_xi`. | Typed, but `L_(sigma,h)` and the reindexing are not defined as formulas. |
| (5.5) | Commutator in `End(C)`, size `D_xi x D_xi`. | Typed for every `c`. |
| (5.6) | After one unitary identification `C ~= (V_kappa box V_nu) tensor C^c`, `I_d tensor M_xi` is `D_xi x D_xi`; the partial trace is `c x c` and requires the factor `1/d`, not `1/c`. | Typed for every `c`; no LR copy is selected. |
| (6.1) | `A_p` and `P_xi^tau` are `F x F`; their ranks are `r` and `D_xi`. | Typed. |
| (6.2) | Three `F x F` identities. On ranges, `A_p: C^r -> C^r` is an isometry and `rho(tau_p): C -> C^tau` is a `D_xi`-dimensional unitary. | Typed for every `c`; this is not a fixed-multiplicity endomorphism. |
| (6.3) | Sum of `(q-j)!` matrices of size `F x F`; right side is `F x F`. | Typed. |
| (6.4) | Scalar basis count `T`; it has no multiplicity factor `c`. | Typed. |
| (6.5) | `J_raw` is `M x T`, `W_h` is `M x M`, `Q` is an `M x M` projection with selected range `F c`, the co-restricted `F_BR` is `F x Fc`, and final `P_xi` is `D_xi x F`; `U_h` is `D_xi x T`. | Dimensionally typed if `Q` is co-restricted and `F_BR` is extended by zero off its range. The maps are not constructed. |
| (6.6) | First two operators are `T x T`; `U_h` has `T` source columns and `D_xi` rows; `||U_h||_HS^2=Tr(U_h^*U_h)<=T`. | Typed. Codomain growth with `c` cannot create a source-column factor. |
| (7.1) | Integer scalar depending on `(q,j,theta,z)`, independent of `(a,b,alpha,beta,c)`. | Typed. |
| (7.2) | Two scalar squared coordinates in a `2 x 2` path block; on multiplicity `c` the block is tensored with `I_c`. | Typed. |
| (7.3) | Integer scalar hook length, independent of `c`. | Typed. |
| (7.4)-(7.5) | `2 x 2` orthogonal matrices; with multiplicity they are `2c x 2c` after tensoring with `I_c`. | Typed. |
| (8.1) | `F=23296`, `d=16*35=560`, `c=2`, `D_xi=1120`; dense ambient size is `23296^2=542703616`. | Arithmetic confirmed. |

### 1.1 Rule 7(g) term resolution

R1 Section 1.1 defines partition, Specht module, dimension, column height,
corner, content, axial distance, pointwise stabilizer, twirl, isotypic
component, multiplicity space, `A`, `B`, the query, and `H`. Definition 2.1
then defines admissibility and the later paragraph defines the tame range.

The following downstream terms do **not** resolve to Section 1.1 or to an
explicit local formula: `P_xi` as a projector; `widehat b_0`; the convention
turning a matching into `r_h`; `P_comp` (only its range/dimension and later
its averaging property are described); `sigma dot h`; `L_(sigma,h)`;
`J_raw`, `W_h`, `Q_(lambda,theta)`, and `F_BR` as concrete maps; and the
normalization convention for the "normalized BR Fourier row." Standard
terms such as LR coefficient, Young branching, seminormal form, Pieri, and
Jucys--Murphy have literature references, but the SE-specific maps just
listed do not. This is harmless for the abstract subgroup arguments, but is
load-bearing for W3 as written and for the physical interpretation of W4's
raw-column map.

## 2. W1: admissible sector and stable LR coefficient

**Verdict: CONFIRMED.** The definition is sufficient for all claims actually
made in R1 and covers `c>=2`.

My derivation was as follows. Restrict `V_lambda` first from `S_q` to
`S_(q-1)`. Its children are

\[
\tau_0=(q-j-1,\theta)
\quad\hbox{and}\quad
\tau_z=(q-j,\theta-z).
\]

If `c_(kappa,nu)^(tau_z)>0`, the first-row LR inequality gives

\[
(\tau_z)_1\leq\kappa_1+\nu_1.
\]

Here the left side is `q-j`, while the right side is

\[
(n-1-a)+(n-b)=q-j-1,
\]

which is impossible. Thus only `tau_0` can contain the requested `H` type.

Put `K=n-1-a`, `N=n-b`, and `L=K+N=q-j-1`. In the skew shape
`tau_0/kappa`, the first row has exactly `N` boxes. Since `K>=theta_1`,
these boxes lie strictly to the right of every tail box. The LR word reads
that row first and right-to-left. Row semistandardness makes that segment
weakly decreasing; the lattice condition forces its first symbol, hence all
of it, to be `1`. It consumes all `N` ones in content `(N,beta)`.
Deleting the row and subtracting one from every remaining entry gives an LR
tableau of shape `theta/alpha` and content `beta`.

Conversely, shift an LR tableau of `theta/alpha` and content `beta` up by one
and prefix the `N` ones. There is no column conflict because `K>=theta_1`.
The lattice condition across the junction follows from
`N>=theta_1>=beta_1`; the last inequality follows from nonzero
`c_(alpha,beta)^theta` (equivalently use LR symmetry and `beta subset theta`).
This is a bijection, so

\[
c_{\kappa\nu}^{\tau_0}=c_{\alpha\beta}^{\theta}=c.
\]

This argument counts all LR tableaux, not one chosen copy, so it applies
unchanged at `c=2` and above. R1's proof agrees, although it omits the short
`N>=beta_1` sentence needed to verify the inverse word at the junction; the
inequality is present in Definition 2.1 and the omission is not a theorem
gap.

**Promotion recommendation:** at most **CERTIFIED\***, with caveat
"no independent full `c>=2` module/operator identity gate." The independent
LR enumeration does confirm the first `c=2` coefficient itself.

## 3. W2: operator-level orbit isolation

**Mathematical verdict: CONFIRMED. Review-qualification caveat: this W2
portion fails the chronological anchoring requirement of rule 7(c), as
disclosed in Section 0.**

For a set `D`, write `r=|D intersect A^circ|`, `s=|D intersect B|`, and

\[
L_D=S_{A^\circ\setminus D}\times S_{B\setminus D}.
\]

Then `L_D <= H intersect K_D`. Let `Q_D` be its averaging projector. Group
inclusion gives `Pi_D=Pi_D Q_D`. The isotypic projector is the represented
central idempotent for the `H` type `(kappa,nu)`, so it commutes with `Q_D`.

Independently applying the branching rule to `V_kappa downarrow S_m`, the
multiplicity of the trivial representation is

\[
\dim (V_\kappa)^{S_m}=f^{\kappa/(m)}.
\]

It is nonzero exactly when the row `(m)` fits in `kappa`, i.e.
`m<=kappa_1`. With `m=n-1-r`, this requires `r>=a`. The second factor gives
`s>=b`. Hence `Q_D P_xi=0`, and therefore `Pi_D P_xi=0`, whenever either
inequality fails. This acts on the entire
`V_kappa box V_nu tensor C^c`; the last factor is exactly `I_c`.

For (4.3), a `j`-set containing the query has only `j-1=a+b-1` tail
positions and is killed. A query-free set has `r+s=j=a+b`, and simultaneous
`r>=a`, `s>=b` forces `(r,s)=(a,b)`. For (4.4), the `j` free positions are
all tail positions and the same arithmetic applies. This is a term-by-term
operator kill, not a colored-orbit/full-central-sum substitution.

Finally, the all-`D` sum in (4.3) is `S_q`-central. Each summand has rank
`f^theta`, so its scalar is

\[
B_\theta(q)={\binom qj f^\theta\over f^\lambda}.
\]

The pinned sum is `S_(q-1)`-central; on the unique child `tau_0` its scalar
is

\[
{\binom{q-1}{j}f^\theta\over f^{\tau_0}}.
\]

These traces are consequences of the operator identity, not replacements
for it. R1's proof uses the same `L_D,Q_D` notation and the same branching
criterion; because I saw that block before recording this derivation, that
notational coincidence is anchoring-contaminated.

**Promotion recommendation:** leave **CONJECTURED/pending-review** until a
clean rule-7(c) reviewer repeats this portion. Even then rule 7(b) caps it at
**CERTIFIED\*** with caveat "actual `c>=2` compressed `Pi_D` matrix gate
untested."

## 4. W3: the matching twirl

**Verdict: GAP as a claim in R1; the reconstructed literal-BR covariance is
CONFIRMED.** The gap is definitional/bookkeeping under rule 7(g), not a
counterexample.

### 4.1 Independent literal-kernel derivation

From BR's `Z_(j+1)` block, after removing a common scalar, define for
`g in S_q`

\[
b_j(g)=(q\mathbf1[g(1)=1]-1)
e_j\!\left(qx_2(g)-2,\ldots,qx_n(g)-2\right),
\]

where

\[
x_i(g)=\mathbf1[g(i)=i]+\mathbf1[g(\bar i)=i].
\]

This follows directly from BR:548-550: the queried
`Pi_1 tensor e_0^*` factor supplies `q h_1-1`, every unqueried `Psi_1`
supplies `q(h_i^A+h_i^B)-2`, and the fixed-weight sum is the elementary
symmetric polynomial. This derivation uses the literal kernel, not R1's
printed covariance formula.

Let `d_sigma` simultaneously permute `i` and `bar i` for `i=2,...,n` and
fix the queried pair. Conjugation by `d_sigma` merely permutes the variables
`x_i` and fixes the query factor, so

\[
b_j(d_\sigma^{-1}gd_\sigma)=b_j(g).
\]

For `widehat b_0=sum_g b_j(g)rho_lambda(g)`, change variables
`g'=d_sigma g d_sigma^{-1}` to obtain

\[
\rho(d_\sigma)\widehat b_0\rho(d_\sigma)^{-1}
=\sum_{g'}b_j(d_\sigma^{-1}g'd_\sigma)\rho(g')
=\widehat b_0.
\]

Thus (5.3) is correct for the literal BR kernel. A global Fourier or BR
normalization factor cancels from this identity.

### 4.2 Right and diagonal covariance bookkeeping

With `widehat b_h=widehat b_0 rho(r_h^{-1})` and
`r_(h dot pi)^(-1)=r_h^(-1)pi`, direct multiplication gives

\[
B_h\rho_C(\pi)=B_{h\cdot\pi};
\]

the only projector moved is `P_xi`, which commutes with `H`. This is (5.2).

For the `A^circ` action, define the reindexed matching `h'` by

\[
r_{h'}^{-1}=\bar\sigma^{-1}r_h^{-1}.
\]

Since `sigma=d_sigma bar_sigma^(-1)` and the `A` and `B` permutations
commute,

\[
B_h\rho_C(\sigma)
=\rho(d_\sigma)|_{\mathcal O}\,B_{h'}.
\]

Here `P_comp` is the `S_B` averaging projector: `d_sigma` normalizes that
subgroup, so it preserves `O`, and its restriction
`L_sigma=rho(d_sigma)|_O` is unitary. Consequently
`L_sigma^*L_sigma=I_O`, it cancels on taking `B_h^*B_h`, and the matching
sum reindexes. Together with right covariance this proves (5.5).

On the full carrier

\[
\mathcal C\cong (V_\kappa\boxtimes V_\nu)\otimes\mathbb C^c,
\]

the first tensor factor is irreducible for `H`. Therefore its commutant is
exactly `I_d tensor End(C^c)`, giving (5.6) and the normalized partial trace
`M_xi=(1/d)Tr_d G`. This does not choose an LR copy and is valid for
`c>=2`.

R1 does not write the formula for `b_j`, the definition of `h'`, or the
formula for `L`; it only says "for a reindexed matching" and "restriction of
an alphabet permutation." Those omissions are precisely the missing
bookkeeping the human review requested. My reconstruction closes the
mathematics for the stated literal interpretation, but rule 7(g) prevents
calling R1's own display fully defined.

**Promotion recommendation:** **CONJECTURED**, not a completion tier, until
the SE-specific maps/reindexing are defined in R1 or an explicitly cited
definition. After that repair, at most **CERTIFIED\*** with caveat
"`c>=2` matching-block matrix gate untested."

## 5. W4: transport and raw-column contraction

### 5.1 (6.1)-(6.3)

**Verdict: CONFIRMED.** From `A_p=rho(tau_p)Pi_D` and unitarity,

\[
A_p^*A_p=\Pi_D.
\]

Conjugating the pointwise stabilizer of `D` by `tau_p` gives the pointwise
stabilizer of `K`, hence

\[
A_pA_p^*=\rho(\tau_p)\Pi_D\rho(\tau_p)^*=\Pi_K.
\]

The carrier equation is the definition of the conjugate projector:

\[
P_\xi^{\tau_p}\rho(\tau_p)=\rho(\tau_p)P_\xi.
\]

Thus `A_p` is an isometry between two `f^theta`-dimensional fixed-set ranges,
while `rho(tau_p)` maps the `D_xi=dc` carrier to the honest conjugate
carrier. Nothing here is an endomorphism of a fixed multiplicity space.

Every extension of `p` is uniquely `tau_p s` with `s in K_D`; there are
`(q-j)!` of them. Averaging gives (6.3) with exactly that factor.

R1 also characterizes the old formula correctly. Its synthesis frames had
`f^theta` columns, whereas the proposed middle operator
`rho_theta(sigma_p) tensor L_p` acted on `f^theta c` dimensions when `c>1`.
Moreover a general `tau_p` transports the `H`-isotypic component to a
`tau_p H tau_p^(-1)`-isotypic component; it does not define an endomorphism
of one fixed LR multiplicity space.

**Promotion recommendation:** at most **CERTIFIED\***, caveat "no actual
`c>=2` non-normalizing transport matrix gate."

### 5.2 (6.4)-(6.6)

**Verdict: GAP as a physical-map claim; CONFIRMED as a conditional abstract
contraction.** The induced dimension is

\[
M=[S_q:S_{q-j}\times S_a\times S_b]f^\alpha f^\beta
={q!f^\alpha f^\beta\over(q-j)!a!b!}.
\]

The retained source count is

\[
T=\binom{n-1}{a}\binom{n-1-a}{b}f^\alpha f^\beta.
\]

If `J_raw` is an isometry, `W_h` a unitary, `Q` and `P_xi` orthogonal
projections, and `F_BR` a norm-one Fourier row, then their composition is a
contraction. Hence

\[
U_h^*U_h\preceq I_T,
\qquad
\|U_h\|_{HS}^2=\operatorname{Tr}(U_h^*U_h)\le T.
\]

The trace is over source columns. Increasing the codomain from `d` to `dc`
cannot multiply their number, so no factor `c` appears.

However, R1 supplies no actual formulas for these four induced-module maps
and no proof that its abstract normalized Fourier row is the later physical
BR/output-frame map. R1 itself acknowledges this immediately after (6.6).
Thus (6.6) is safe algebra once the maps exist with the asserted norms, but
it does not discharge the missing physical identification or human item 3.

**Promotion recommendation:** remain **CONJECTURED**.

## 6. W5: contents, axial distance, hooks, and the split conclusion

**Verdict: CONFIRMED for the Young/Pieri scalar statements.** R1 correctly
does not claim the deferred frame-operator identity.

Let `L=q-j`. The long-row endpoint is `u_L=(1,L)` with content `L-1`.
A corner of `theta` in column `t` lies in row `theta'_t`; in `lambda` its
coordinate is `u_t=(theta'_t+1,t)`, so its content is
`t-theta'_t-1`. Therefore

\[
|c(u_L)-c(u_t)|=L-t+\theta'_t=\delta_z,
\]

not `delta_z+1`.

For an independent construction of (7.4)-(7.5), I used the standard
representation of `S_(L+1)` on the sum-zero subspace of `R^(L+1)`. In the
two-dimensional `S_(L-1)`-fixed branching space, take the normalized vectors

\[
v_{(L)}={ (1,\ldots,1,-L)\over\sqrt{L(L+1)}},
\quad
v_{(L-1,1)}={ (1,\ldots,1,-(L-1),0)\over\sqrt{L(L-1)}}.
\]

The transposition exchanging the last two coordinates has matrix, in that
ordered basis,

\[
\begin{pmatrix}
-1/L&\sqrt{1-1/L^2}\\
\sqrt{1-1/L^2}&1/L
\end{pmatrix}.
\]

At `L=5` and `L=7` this gives exactly R1's (7.4) and (7.5), including
`(2/5,3/5)` and `(3/7,4/7)` for the squared `+1` coordinates. This uses an
actual coordinate representation, not R1's printed seminormal formula.
The general Young-orthogonal calculation with axial distance `delta_z`
gives

\[
{\delta_z-1\over2\delta_z},\qquad
{\delta_z+1\over2\delta_z}.
\]

The hook at `(1,t)` is instead

\[
(L-t)+(\lambda'_t-1)+1=L-t+\theta'_t+1=\delta_z+1.
\]

The relative Pieri/Jucys factor attached to a strip box `u` is
`L-c(u)`. Hence the intended conditioning ratio is

\[
{L-c(u_L)\over L-c(u_t)}={1\over\delta_z+1}.
\]

Thus the Young coefficients change, while the separate reciprocal-hook
Pieri scalar does not. This only checks the scalar used later. R1 expressly
says that constructing `E_(out,z)` and proving its frame Gram remains human
item 3; it does not claim that operator identity here.

**Promotion recommendation:** **CERTIFIED\*** for the stated scalar/path
claims. The `c>=2` action is analytically `path block tensor I_c`, but there
is no general cross-stack output-frame gate and no frame identity is included
in this recommendation.

## 7. W6 gates and arithmetic

The new scripts do not import or call R1's gate script.

| Gate | Regime covered | Result | Formula or independent construction? |
|---|---|---|---|
| T2 free, pinned, and each wrong orbit | `(n,q,j)=(3,6,1)`, both `c=1` sectors | Exact rational residuals all zero. | Independent: point-permutation representation, subgroup averages, and explicit strict projectors. It does not insert (4.2)-(4.4). |
| T3 diagonal covariance, right covariance, full `H` commutators | `(3,6,1)`, both `c=1` sectors | Exact residuals all zero. | Independent: derived literal BR weights, all `6!=720` permutations, all `3!=6` matchings, and an independently averaged completion projector. |
| T4 partial isometry, final projector, coset sum | `q=6,j=1`, representative `c=1` transport | Coset count `120`; all four exact residuals zero. | Independent permutation action and coset enumeration; (6.2) was not inserted. |
| T5 | `q=6,8,j=1` | Exact matrices and squared coordinates agree. | Independent standard-representation coordinate construction, not the printed content formula. |
| LR search | Every `j<=8`, all partitions and splits | First and only first-degree hit is `j=6`, `theta=(3,2,1)`, `alpha=beta=(2,1)`, `c=2`. | Independent LR-tableau backtracking with semistandard and lattice-word checks. |
| Hook/admissibility arithmetic | `(n,q,j)=(7,14,6)` | `f^lambda=23296`, `f^kappa=16`, `f^nu=35`, carrier `1120`, induced `M=240240`; all Definition 2.1 inequalities hold. | Independent hook products and direct inequalities. |

This is a representative subset of R1's nine `c=1` sectors, not a rerun of
all nine. It corroborates both values and formulas because the objects were
constructed independently.

## 8. W7 budget-boxed `c=2` stretch

**Result: partial construction; the required matrix gate remains UNTESTED.**

At `(7,14,6)`, `a=b=3`, `alpha=beta=(2,1)`, I generated the actual Young
branching bases of `V_(3,2,1)` and `V_(4,2,1)`. The fixed-space projectors
for the boundary wrong-color subgroups are:

\[
Q_A(S_4)=0_{16\times16},\qquad
Q_B(S_5)=0_{35\times35}.
\]

For comparison the allowed boundary ranks are
`rank Q_A(S_3)=2` and `rank Q_B(S_4)=2`. Tensoring the forbidden factors
with the other Specht factor and `I_2` produced exact structural matrices

\[
Q_A(S_4)\otimes I_{35}\otimes I_2=0_{1120\times1120},
\]

\[
I_{16}\otimes Q_B(S_5)\otimes I_2=0_{1120\times1120}.
\]

All free and pinned wrong color counts reduce to one of these zero factors.
This independently tests the full-multiplicity fixed-vector mechanism in
Lemma 4.1 and explicitly includes both LR directions.

It is not the requested matrix gate for `P_xi Pi_D P_xi`: constructing
`Pi_D` on this carrier requires how a non-`H` permutation recouples the two
LR copies. Nor does it construct `B_h` for T3. The induced-module alternative
has dimension `240240`; extracting and transporting the two `lambda` copies
still requires the same subduction data. A double-coset trace would only be
an aggregate unless converted to the complete multiplicity matrix. Therefore
R1's obstruction is adjudicated as accurate, with the refinement that the
`L_D` kill factor itself is cheaply matrix-testable while the nonnormalizing
compressed operator is not presently constructed.

A failed stretch is not a gap in R1, which already labels the regime
untested.

## 9. Per-claim verdicts and promotion advice

| Claim | Verdict | Promotion recommendation |
|---|---|---|
| W1 admissibility and Theorem 2.2 | **CONFIRMED** | At most **CERTIFIED\***: no independent full `c>=2` module/operator identity gate. |
| W2 Lemma 4.1 and Theorem 4.2 | **CONFIRMED mathematically** | Keep **CONJECTURED/pending-review** because this review's W2 sequence was rule-7(c) contaminated. A future clean review is still capped at **CERTIFIED\*** until the actual `c>=2` compressed matrix gate exists. |
| W3 matching twirl and full-carrier Schur step | **GAP in R1; reconstructed claim confirmed** | **CONJECTURED** until the SE-specific kernel, matching reindex, completion, and output unitary are defined. Then at most **CERTIFIED\*** with `c>=2` matrix gate named untested. |
| W4 (6.1)-(6.3) transport | **CONFIRMED** | At most **CERTIFIED\***: `c>=2` nonnormalizing transport matrix gate untested. |
| W4 (6.5)-(6.6) raw-column map | **GAP as physical claim; conditional contraction confirmed** | **CONJECTURED** until the maps and their identification with the actual BR/output object are constructed. |
| W5 axial/Young/Pieri split | **CONFIRMED** | **CERTIFIED\*** for the stated path/scalar claim only; output-frame identity remains explicitly outside scope. |
| W6 finite evidence | **CONFIRMED for the independently covered regimes** | Evidence only; it does not lift T2/T3/T4 above the `c>=2` cap. |
| W7 stretch | **UNTESTED regime remains; obstruction confirmed** | No promotion effect. |

No claim is refuted. R1 substantially discharges human items 1, 2, 4, 6,
and 8 at the analytic level. Human item 5 is mathematically recoverable and
independently corroborated but not self-contained in R1. The raw-column
paragraph does not discharge human item 3 and correctly says so.

## 10. Reproducibility

Commands used:

```powershell
& '<machine-local-path-redacted>' -u `
  'se/artifacts/logs_se_frames1rev_20260719/independent_gates.py'

& '<machine-local-path-redacted>' -u `
  'se/artifacts/logs_se_frames1rev_20260719/c2_stretch.py'
```

Outputs are in `se/artifacts/logs_se_frames1rev_20260719/`. SHA-256 values are
recorded in `se/artifacts/logs_se_frames1rev_20260719/SHA256SUMS.txt`.

No DAG, node, index, paper, or R1 source file was edited.
