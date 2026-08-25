# L3 critical endpoint: induced bicovariant alphabet-packet first gate

Date: 2026-07-22  
Canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-induced-bicovariant-alphabet-packet-kernel`

Tier: analytic proposer audit only; fresh Rule-7 review is pending.  
Scope: the exact `p=0`, `u=1`, `q=4a` critical palette quotient, every integer `a>=2`.

## 1. Decision

The first two gates have a clean but limited answer.

1. **Complete common packet: PASS.** The exact NO module embeds isometrically into the exact YES
   module, including every multiplicity of every common `S_q` full type. This is a physical
   subgroup-induced embedding, not merely a coefficientwise symmetric-function inequality.
2. **Packet width and multiplicity: PASS.** The common NO packet has at least `2a-1` distinct full
   types and contains a full type with multiplicity at least `a-1`.
3. **First marked mass/parent-tag gate: PASS.** Literal marked-cell restriction of the complete
   coset embedding has total common mass one. A distinguished singleton branch has squared mass
   `1/a`, but its residual companion has squared mass `(a-1)/a`; retaining only the former caused
   the earlier fixed-two-box loss. Full-type parent labels are not physical superselection tags
   after restriction to `S_(q-1)`.
4. **Scalar orientation novelty: FAIL.** The two physical embeddings `J_L,J_R` have
   `J_L^*J_R` equal to the normalized Bernoulli--Laplace swap walk on `J(2a,a)`. They are exactly
   the normalized immediate collision-split orbitals already audited at the critical endpoint.
   Thus `J_L+J_R`, `J_L-J_R`, or any coefficient depending only on the Johnson harmonic degree is
   the old addressed Johnson/UIC mechanism in complete Fourier coordinates. It does not supply a
   new endpoint exponent.

The broad induced-packet node therefore remains **OPEN / pending-review**. No full coefficient
optimization, incidence normalization, remainder estimate, or outer numerator is attempted here.
Three genuinely nonseparable packet-harmonic/occurrence continuations were registered under Rule 8
but not tested.

## 2. Exact subgroup-induced modules

Let

\[
 G=S_q,qquad q=4a,qquad V_a=S^{(a-1,1)},qquad D=\dim V_a=a-1.
 \tag{2.1}
\]

For a NO palette assignment, write the ordered cells as

\[
 (A,B,H_L,H_R),qquad |A|=|B|=|H_L|=|H_R|=a.
 \tag{2.2}
\]

The first two cells are the left/right rare-singleton palettes and the last two are the heavy
palettes. Define

\[
 H_0=S_A\times S_B\times S_{H_L}\times S_{H_R}\cong S_a^4,
 \qquad
 \tau_0=\mathbf 1\boxtimes\mathbf 1\boxtimes V_a\boxtimes V_a,
 \tag{2.3}
\]

and

\[
 M_0=\operatorname{Ind}_{H_0}^{G}\tau_0.
 \tag{2.4}
\]

For a YES palette assignment, write

\[
 (U,C,L,R,H_L,H_R),qquad |U|=|C|=1,quad |L|=|R|=a-1,quad
 |H_L|=|H_R|=a,
 \tag{2.5}
\]

where `C` is the common singleton label and `U` is the unused label. Let

\[
 H_1=S_U\times S_C\times S_L\times S_R\times S_{H_L}\times S_{H_R},
 \qquad
 \tau_1=\mathbf1^{\boxtimes4}\boxtimes V_a\boxtimes V_a,
 \tag{2.6}
\]

and

\[
 M_1=\operatorname{Ind}_{H_1}^{G}\tau_1.
 \tag{2.7}
\]

These definitions type the heavy-cell tensor explicitly. Their dimensions are

\[
 \dim M_0={ (4a)!\over(a!)^4}(a-1)^2,
 \qquad
 \dim M_1=a^2\dim M_0.
 \tag{2.8}
\]

There are two physical inclusions of `H_1` into `H_0`:

\[
 \begin{array}{lll}
 \iota_L:& A=L\sqcup C,& B=R\sqcup U,\\
 \iota_R:& A=L\sqcup U,& B=R\sqcup C.
 \end{array}
 \tag{2.9}
\]

Both have index `[H_0:H_1]=a^2`. The orientation is extra physical data; the character identity
below does not choose between them.

## 3. Character identity versus physical embedding

Write `s=s_(a-1,1)` and `h=h_a`. Frobenius characteristics give

\[
 \operatorname{ch}M_0=s^2h^2=:F_0,
 \qquad
 \operatorname{ch}M_1=h_1^2h_{a-1}^2s^2=:F_1.
 \tag{3.1}
\]

Pieri gives the exact identity

\[
 h_1h_{a-1}=s_{(a)}+s_{(a-1,1)}=h+s.
 \tag{3.2}
\]

Consequently

\[
 \boxed{F_1=F_0+2hs^3+s^4.}
 \tag{3.3}
\]

Equation (3.3) is coefficientwise Schur-positive, but positivity alone would not specify a
physical isometry. Here induction in stages does. For either inclusion (2.9),

\[
 \operatorname{Ind}_{S_{a-1}\times S_1}^{S_a}\mathbf1
 \cong \mathbf1\oplus V_a.
 \tag{3.4}
\]

Therefore

\[
 \begin{aligned}
 M_1\cong{}&M_0\\
 &\oplus\operatorname{Ind}_{S_a^4}^{G}
    (V_a\boxtimes\mathbf1\boxtimes V_a\boxtimes V_a)\\
 &\oplus\operatorname{Ind}_{S_a^4}^{G}
    (\mathbf1\boxtimes V_a\boxtimes V_a\boxtimes V_a)\\
 &\oplus\operatorname{Ind}_{S_a^4}^{G}
    (V_a\boxtimes V_a\boxtimes V_a\boxtimes V_a).
 \end{aligned}
 \tag{3.5}
\]

This is an orthogonal decomposition of actual unitary `G`-modules.

In a cell/coset basis, let `x=(A,B,H_L,H_R;v_L,v_R)` be a coarse NO vector. The two normalized
pullbacks are

\[
 \begin{aligned}
 J_Lx&={1\over a}\sum_{c\in A}\sum_{u\in B}
  (U=u,C=c,L=A\setminus\{c\},R=B\setminus\{u\},H_L,H_R;v_L,v_R),\\
 J_Rx&={1\over a}\sum_{u\in A}\sum_{c\in B}
  (U=u,C=c,L=A\setminus\{u\},R=B\setminus\{c\},H_L,H_R;v_L,v_R).
 \end{aligned}
 \tag{3.6}
\]

Each sum has `a^2` orthogonal terms, and its coarsening is unique. Hence

\[
 J_L^*J_L=J_R^*J_R=I_{M_0}.
 \tag{3.7}
\]

If

\[
 M_t\cong\bigoplus_{\nu\vdash4a}S^\nu\otimes Z_{t,\nu},
 \qquad m_{t,\nu}=\dim Z_{t,\nu},
 \tag{3.8}
\]

then equivariance and (3.7) give

\[
 J_o=\bigoplus_{\nu\vdash4a}I_{S^\nu}\otimes j_{o,\nu},
 \qquad
 j_{o,\nu}:Z_{0,\nu}\hookrightarrow Z_{1,\nu}
 \text{ is an isometry}.
 \tag{3.9}
\]

Thus `m_(0,nu)<=m_(1,nu)` and every copy on the NO side embeds. The unused orthogonal complement
in `Z_(1,nu)` accounts for the unequal YES multiplicity. Equation (3.9), not (3.3) alone, is the
physical all-multiplicity statement.

## 4. Analytic packet width and growing multiplicity

Pieri gives

\[
 h_a^2=\sum_{j=0}^{a}s_{(2a-j,j)}.
 \tag{4.1}
\]

For each `0<=k<=a-2`, the LR product `s_(a-1,1)^2` contains

\[
 \theta_k=(2a-2-k,k+2)
 \tag{4.2}
\]

with coefficient one. One explicit LR tableau fills the newly added first-row boxes with `1`,
fills the newly added second-row boxes with `1` except for a final `2`, and is unique with the
required content and lattice word.

For every pair `(j,k)`, the Cartan component of
`s_(2a-j,j)s_(2a-2-k,k+2)` is

\[
 \nu_{j+k}=(4a-j-k-2,j+k+2)
 \tag{4.3}
\]

with coefficient one. Hence `F_0` contains the distinct types

\[
 \nu_r=(4a-r-2,r+2),qquad 0\le r\le2a-2,
 \tag{4.4}
\]

so the packet width is at least `2a-1`. At `r=a-1`, the pairs

\[
 (j,k)=(1,a-2),(2,a-3),\ldots,(a-1,0)
 \tag{4.5}
\]

give

\[
 [s_{(3a-1,a+1)}]F_0\ge a-1.
 \tag{4.6}
\]

This is an analytic all-`a` lower bound. At `a=2` it certifies width three and multiplicity one;
for `a>=3` it certifies a nontrivial, growing multiplicity. No finite character table is used to
infer either assertion.

## 5. Exact orientation cross-Gram

Take a fine state in the support of `J_Lx`, chosen by `c in A,u in B`. It lies in the support of
`J_Ry` for exactly the coarse state

\[
 y=(A\setminus\{c\})\cup\{u\},
   (B\setminus\{u\})\cup\{c\},H_L,H_R.
 \tag{5.1}
\]

Every coincident fine state contributes `(1/a)(1/a)=1/a^2`. Therefore

\[
 \boxed{
 K:=J_L^*J_R,qquad
 K|A,B,H_L,H_R;v_L,v_R\rangle
 ={1\over a^2}\sum_{c\in A,u\in B}
 |A-c+u,B-u+c,H_L,H_R;v_L,v_R\rangle.}
 \tag{5.2}
\]

The operator fixes the ordered heavy cells, their standard vectors, and the union `A union B`.
On each remaining fiber it is the normalized adjacency of the Johnson graph `J(2a,a)`. It is real,
self-adjoint, stochastic, and `G`-equivariant.

The Johnson adjacency eigenvalue at harmonic degree `j` is

\[
 (a-j)^2-j=a^2-j(2a-j+1).
 \tag{5.3}
\]

Thus

\[
 \boxed{\lambda_j(K)=1-{j(2a-j+1)\over a^2},qquad0\le j\le a.}
 \tag{5.4}
\]

Within a fixed Johnson fiber its multiplicity is

\[
 d_j={2a\choose j}-{2a\choose j-1},
 \tag{5.5}
\]

where the second binomial is zero at `j=0`. Globally it is repeated

\[
 { (4a)!\over(2a)!(a!)^2}(a-1)^2
 \tag{5.6}
\]

times, accounting exactly for the heavy-cell choices and heavy standard fibers.

Because `K=K^*`,

\[
 (J_L\pm J_R)^*(J_L\pm J_R)=2(I\pm K).
 \tag{5.7}
\]

Consequences needed for the gate are:

\[
 \begin{array}{c|c|c}
 &J_L+J_R&J_L-J_R\\ \hline
 j=0&\text{squared singular value }4&0\\
 \text{operator norm}&2&\sqrt{2+2/a}\\
 \text{smallest nonzero singular value}&\sqrt{2(1-1/a)}&2/\sqrt a
 \end{array}
 \tag{5.8}
\]

For the contrast, the smallest nonzero value occurs at `j=1`, while its norm occurs at `j=a`.
In particular, the contrast is nonzero but kills the constant orientation sector exactly. At
`a=2`, the spectrum is `{1,0,-1/2}`, so every formula remains legal at the smallest allowed value.

## 6. Literal marked-cell mass and parent tags

Fix a palette point `z`. Let `P_X(z)` denote the NO projector onto coarse states with
`z in X`, `X in {A,B,H_L,H_R}`, and let `Q_Y(z)` denote the corresponding YES projector for
`Y in {U,C,L,R,H_L,H_R}`. Formula (3.6) gives the operator identities

\[
 \begin{aligned}
 Q_{H_L}(z)J_o&=J_oP_{H_L}(z),&
 Q_{H_R}(z)J_o&=J_oP_{H_R}(z),\\
 (Q_L(z)+Q_C(z))J_L&=J_LP_A(z),&
 (Q_R(z)+Q_U(z))J_L&=J_LP_B(z),\\
 (Q_L(z)+Q_U(z))J_R&=J_RP_A(z),&
 (Q_R(z)+Q_C(z))J_R&=J_RP_B(z).
 \end{aligned}
 \tag{6.1}
\]

The individual fine branches have exact Grams

\[
 \begin{aligned}
 J_L^*Q_C(z)J_L&={1\over a}P_A(z),&
 J_L^*Q_L(z)J_L&={a-1\over a}P_A(z),\\
 J_L^*Q_U(z)J_L&={1\over a}P_B(z),&
 J_L^*Q_R(z)J_L&={a-1\over a}P_B(z),
 \end{aligned}
 \tag{6.2}
\]

with `C` and `U` exchanged for `J_R`. The heavy identities have Gram one. Thus a selected
singleton branch has squared mass `1/a`, but the complementary residual branch carries
`(a-1)/a`; their physical direct sum has mass one. The full packet therefore repairs the
`O(1/a)` mass loss of a fixed two-box truncation at this first alphabet gate.

Each marked space is an actual `S_(q-1)` module. In an unmarked Fourier basis, `J_o` is legal and
block diagonal as in (3.9). The projectors in (6.1), however, commute only with `S_(q-1)`. They
have cross-parent blocks whenever two different `S_q` parents restrict to the same marked child.
Those blocks are required to reconstruct (6.1). Carrying the old parent name as an additional
orthogonal tag after physical restriction would erase real matrix entries and is not the literal
query map.

This gate is stable under a common occurrence tensor. If `R:C^(c_0)->C^(c_1)` is an explicitly
chosen isometry, then every identity above holds with `J_o` replaced by `J_o tensor R`. It covers
`c=1` and every `c>1`; for unequal occurrence ranks it uses only the stated common rank and makes
no claim about an unmatched complement. The selected three-row construction has equal common rank
on the two answers. Its prior review found that its formal coefficient-one point `C_r=1` is not a
physical two-sided case because the opposite invariant multiplicity `g_2` vanishes; the actual
critical family begins in the `C_r>1` regime. That caveat does not affect the alphabet identities.

## 7. Exact comparison with earlier mechanisms

### 7.1 Immediate collision-split / addressed UIC baseline

At `u=1`, let `A_L,A_R` be the two immediate collision-split orbital matrices in the exact
critical orbit: replace the common singleton on the left or right by the unique unused label. In
the row-YES/column-NO convention, each orientation has row degree one and column degree `a^2`.
Consequently

\[
 J_L={A_L\over a},qquad J_R={A_R\over a}
 \tag{7.1}
\]

up to the harmless swap of the orientation names. This is equality of the physical coset
relations, not merely equality of spectra.

For a fixed left singleton coordinate, only one orientation survives the off-equality query mask;
the masked orbital has row degree one and column degree `a`. Hence

\[
 \|J_{\rm changed}\circ\Delta_i\|={1\over\sqrt a},
 \qquad
 \|J_{\rm unchanged}\circ\Delta_i\|=0,
 \tag{7.2}
\]

with the roles exchanged for a right query. The earlier exact two-orbital audit already allowed
arbitrary signed scalar coefficients and proved the resulting adversary value is at most
`2sqrt(a)`. Equations (5.2)--(5.8) are its full Johnson/Fourier resolution; they do not define a
new outer law.

The addressed lower bound uses the stronger outer `UIC_a` adversary and independent
`pSearch_m` blocks, giving `a^(2/3)sqrt(m)=N^(11/18)` at the critical endpoint. Tensoring a scalar
function of `K` with a passive three-row occurrence matrix does not change that query map. A new
critical gain can only come from coefficients depending nonseparably on the packet harmonic and
the physical occurrence restrictions.

### 7.2 The `q=5` two-orientation shared-NO cascade

There is one structural analogy: two oriented refinements share a coarse NO object, and their
contrast kills a constant/shared component. The mechanisms are nevertheless not the same.

* The `q=5` construction is a signed histogram measure on reflected slot totals `s` and `N-s`.
  Its barycentric law annihilates low-degree moments and moves constant `l1` mass to a high-`C_t`
  YES tail.
* The present construction is a rectangular `q=4a` coset intertwiner. Its cross-Gram is a Johnson
  swap walk on two rare palette cells, and it has no moment or high-`C_t` conclusion.

Therefore the induced packet is **not** a Fourier presentation of the proved `q=5` dual. It **is**
the complete Fourier presentation of the already audited L3 immediate collision-split/Johnson-UIC
orientation baseline. No `q=5` correlation or endpoint result transfers.

## 8. Rule-8 nonseparable continuations

Let `E_j` be the exact spectral projector of `K` for (5.4), let
`mu_j=1-lambda_j`, and let `h,k` index deterministic common three-row occurrence bases. A passive
law has `B_j=b_jB` and is already covered by Section 7. Before any further calculation, three
genuinely nonseparable formula classes were recorded and mapped to their canonical nodes.

1. **Matrix-valued Young holonomy.** On an actual common point-branching diamond in packet sector
   `j`, with deterministic occurrence transports `U_(e,j)`, use

   \[
    H_j=U_{(e_4,j)}U_{(e_3,j)}-U_{(e_2,j)}U_{(e_1,j)},
    \qquad b_{j,h,k}=\langle e_h,H_je_k\rangle,
    \qquad \Gamma=\sum_j E_j\otimes H_j.
    \tag{8.1}
   \]

   The commutator/difference of the two path transports is not a scalar orientation coefficient.
   This is exactly the architecture in
   `KSUM...ALT.induced-packet-young-holonomy-law`.
2. **Joint parent-content kernel.** After the literal left/right occurrence pencils define exact
   spectral parameters `ell_h,r_k`, test the Cauchy/Sylvester prototype

   \[
    b_{j,h,k}={1\over\epsilon+\mu_j+\ell_h+r_k}.
    \tag{8.2}
   \]

   With at least two active occurrence eigenvalues this has tensor rank greater than one in
   `j,h,k`; it is not `b_jB_(h,k)`. This maps to
   `KSUM...ALT.induced-packet-joint-parent-content-kernel` and is the most directly calculable next
   candidate because `mu_j` is now explicit. The exact pencils and admissible `epsilon` remain
   undefined until that node is commissioned.
3. **Divergence-free plaquette flow.** Put a matrix face weight `Phi_f(h,k)` on actual common
   packet/occurrence plaquettes and assign each oriented edge

   \[
    b_{e,h,k}=\sum_{f\supset e}\operatorname{sgn}(e,f)\Phi_f(h,k).
    \tag{8.3}
   \]

   The boundary-of-boundary identity makes the scalar graph divergence vanish, while matrix face
   weights can keep a nonzero circulation jointly in packet degree and `(h,k)`. This is the
   architecture in `KSUM...ALT.induced-packet-plaquette-flow-law`.

These are registrations, not feasibility results. In particular, no actual diamond, occurrence
pencil, holonomy, or nonzero physical circulation is asserted here. At `c=1`, every occurrence
matrix is scalar, so genuine three-index nonseparability must disappear or come from a different
parent-pair degree of freedom; the formal `c=1` gate must be reported separately rather than hidden.

## 9. Gate ledger and stopping point

| obligation | outcome |
|---|---|
| exact NO/YES induced modules | PASS, (2.3)--(2.7) |
| `h_1h_(a-1)=h_a+s_(a-1,1)` | PASS, Pieri (3.2) |
| coefficient identity | PASS, `F_1=F_0+2hs^3+s^4` |
| physical all-multiplicity embedding | PASS, (3.5)--(3.9) |
| unequal NO/YES multiplicities | PASS, rectangular isometries `j_(o,nu)` |
| analytic packet width | PASS, at least `2a-1` |
| analytic growing multiplicity | PASS, at least `a-1` in one type |
| exact `J_L^*J_R` | PASS, normalized `J(2a,a)` swap walk |
| exact spectrum | PASS, (5.4)--(5.6) |
| `a=2` and all `a>=2` | PASS for the alphabet gate |
| literal complete marked mass | PASS, total one; split `1/a` and `(a-1)/a` |
| orthogonal-parent-tag obstruction | FAILS as an obstruction; physical marked spaces overlap |
| `c=1` / `c>1` typing | tensor identities cover both; actual selected three-row `c=1` absent |
| scalar `J_L+/-J_R` novelty | FAIL; exact old collision-split/Johnson-UIC law |
| comparison with `q=5` shared-NO | analogous cancellation, different operator and no transfer |
| nonseparable `j x (h,k)` candidate registration | PASS under Rule 8; three nodes mapped |
| full nonseparable coefficient optimization | NOT OPENED |
| incidence, remainders, numerator, exponent | NOT OPENED |
| fresh independent Rule-7 review | PENDING |

The ordered stopping rule is satisfied: the common packet and marked-mass gates were resolved, the
scalar law collapsed to an existing baseline, three distinct nonseparable successors were recorded
before testing, and no next-gate calculation was begun.

## 10. Sources and provenance boundary

This audit reuses the exact critical-promise notation and the already archived two-orbital degree
calculation from:

* `ksum/artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md`;
* `ksum/artifacts/ksum_L3_critical_three_row_mixed_two_box_full_type_recoupling_feasibility_20260722.md`,
  SHA-256 `DAE5740C9FEA503F9AC92CA5412276E2FC9EF6287647D778EC0CEB63CFB70EE5`;
* `ksum/artifacts/ksum_L3_critical_three_row_block_standard_covariant_feasibility_20260722.md`,
  SHA-256 `3FE61B416E5C0C8AB84FEF1940F9BFB9A4513CADCAC9AC40BC611FAECE71B0DD`;
* `ksum/artifacts/ksum_L3_critical_three_row_bicovariant_two_cell_alphabet_rule7_review_20260722.md`,
  SHA-256 `2FE6AE8F38DE6BBFB85C070B2AA1904F17D99228D4D771438141A015789BEB6A`.

The subgroup decomposition, explicit pullbacks, cross-Gram, Johnson spectrum, marked-projector
identities, and packet-width bounds in this report are analytic. No finite character table,
numerical spectrum, or exponent fit is used. All new claims remain proposer-tier until a fresh
Rule-7 review.
