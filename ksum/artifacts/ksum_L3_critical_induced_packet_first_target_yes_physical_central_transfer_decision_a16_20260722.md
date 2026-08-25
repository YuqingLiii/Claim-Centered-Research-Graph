# First-target YES physical assembly and central-transfer decision at `a=16`

Date: 2026-07-22

Controlling canonical node (not edited by this proposer):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-rectangular-transfer-resolvent-law`

Tier: **exact proposer result, pending fresh independent Rule-7 review**.

The finite scope is

\[
(s,a,d,r,q,n,N)=(4,16,17,4,64,288,576),
\qquad \tau_*=(61,2),
\]

with one fixed raw mark first.  No statement below is an all-`s`, asymptotic, feasibility, query,
numerator, lower-bound, or exponent claim.

## 1. Decision

The gate has a split outcome.

1. **The missing finite YES common-`tau_*` physical assembly is constructible from the reviewed
   inputs, and it passes every exact proposer gate.**  On the active one-side multiplicity space
   of dimension `64`, the YES branch ranks are

   \[
   \operatorname{rank}(C,L,\beta_T,\beta_M,\beta_B)=(4,4,24,14,24).
   \]

   The complete one-side effect has rank `32`; after restoring the untouched four-dimensional
   occurrence factor the ranks multiply by four and the one-side total rank is `128` on the full
   `256`-dimensional YES multiplicity space.  All three heavy-pair commutators have active rank
   `12`.  These are new proposer-tier finite values.
2. **Exact `S_64` covariance proves that a genuinely complete fixed-mark effect determines its
   all-mark central sum by one correlated coset twirl.**  Explicit distinct-mark tables are not
   intrinsically necessary; the stabilizer action and carrier transport are.
3. **The reviewed common child is not the literal fixed-mark effect.**  The three full parents
   have five point children in total: the common `tau_*` and four private children.  The reviewed
   NO/YES point-child tables contain only `tau_*`.  The classification resolution and native
   transfer require every nonzero child.  Therefore the true literal
   `F_(t,z)` and `sum_z F_(1,z) B F_(0,z)` are not determined by the reviewed inputs.
4. Even the common-`tau_*` partial orbit has not been expanded into the full rectangular
   Hilbert--Schmidt matrix.  Its exact definition is available, but its rank, kernel, and spectrum
   require the still-unevaluated `S_64 downarrow S_63` correlated carrier/Wigner kernel.

Thus this artifact licenses the finite YES reduced assembly and an exact insufficiency theorem.
It does **not** license a literal transfer matrix, transfer spectrum, or numerator-active block.

## 2. Reviewed inputs and immutable scope

Only finite inputs with fresh scoped Rule-7 reviews are used:

* the `s=4` occurrence forms/effects;
* the NO and YES `tau_*` alphabet point-child tables;
* the corrected transported NO/YES Pieri scalar table;
* the reviewed NO physical assembly, used as an exact reconstruction check;
* the direct-coset theorem, used only for the native transfer type and the full-YES boundary.

The exact tool pins the hashes of all six data files and all five relevant review artifacts before
reading a value.  In particular, it does not use the unreviewed `s=5` occurrence result.

## 3. Spaces and the unequal-answer boundary

At the common point child,

\[
Y_{0,\tau_*}\cong\mathbb Q^{1+3+6}=\mathbb Q^{10},
\qquad
Y_{1,\tau_*}\cong\mathbb Q^{1+5+10}=\mathbb Q^{16},
\]

and `Z_L`, `Z_R` are each `Q^4`.  After suppressing the common carrier factors, the active
and full multiplicity spaces are

\[
\begin{array}{c|cc}
 & \text{active one side} & \text{both occurrence factors}\\ \hline
\mathrm{NO} & 10\cdot4=40 & 10\cdot4\cdot4=160\\
\mathrm{YES}& 16\cdot4=64 & 16\cdot4\cdot4=256.
\end{array}
\]

Hence the carrier-suppressed rectangular multiplicity space has dimension `256*160=40960`.
This is not the full Hilbert--Schmidt dimension: the actual space also contains the
`S^tau_*` carrier, the three unequal `S_64` parent carriers, and the position carriers.

The finite inputs determine source Grams/effects, not a common basis for every literal marked-row
codomain.  This artifact therefore constructs positive source effects.  That is sufficient input
for the native effect transfer `B -> sum_z F_(1,z) B F_(0,z)`.  It does not reconstruct the
literal row maps or their polar partial isometries, and it makes no claim about the distinct
literal equality sandwich between marked codomains.

For either physical orientation,

\[
j_o:Y_{0,\tau_*}\hookrightarrow Y_{1,\tau_*}
\]

has image dimension ten and complement dimension six.  After both occurrence factors are restored,
the image and unmatched dimensions are `160` and `96`.  The native transfer uses all `256` target
dimensions; it does not pull back through `j_o` and does not pad NO with zeros.

## 4. Exact YES common-child assembly

Work in the reviewed marked-Mackey orthonormal alphabet gauge.  Let

\[
D_U,D_C,D_L,D_R,D_{HL,1},D_{HL,V},D_{HR,1},D_{HR,V}
\]

be the eight coordinate projectors of ranks `1,1,1,1,5,1,5,1`.  They resolve `I_16`.
Let `G` be the reviewed non-normalized occurrence source Gram and

\[
O_{\kappa,\eta}=G^{-1}H_{\kappa,\eta},
\qquad \kappa\in\{T,M,B\},\quad \eta\in\{1,V_{15}\}.
\]

Every product and commutator below uses `O`, never the raw bilinear forms `H`.

The exact status weights are

\[
w_C={1\over288},\qquad w_L=w_R={5\over96},\qquad w_H={17\over18},
\]

and the coevaluation weights are `1/15` and `14/15`.  For a left query,

\[
F_C={1\over288}D_C\otimes I_4,
\qquad
F_L={5\over96}D_L\otimes I_4,
\]

and

\[
F_\beta={17\over18}\sum_{\eta\in\{1,V_{15}\}}
{d_\eta\over15}D_{HL,\eta}\otimes
\sum_{\kappa,\xi}|p^{1,H}_{\beta,\kappa,\xi}|^2O_{\kappa,\eta}.
\tag{4.1}
\]

The right formula replaces `L,HL` by `R,HR`.  The transported YES path inventory in (4.1) is

\[
\begin{array}{c|c|c|c}
\beta&\kappa&\xi&p^2\\ \hline
T&T&T&1\\
T&M&T&1/4929\\
T&M&M&11/862575\\
M&M&M&9273/9275\\
T&B&T&15/76127\\
T&B&B&67/5405017\\
B&B&B&19095/19099.
\end{array}
\]

For every fixed `kappa`, the listed squares sum to one.  The literal no-transport table is not
used.  With `Gamma_64=I_16 tensor G`, every assembled form `Gamma_64 F` is exactly symmetric.

The resulting active ranks and kernels are

| branch | rank | kernel dimension |
|---|---:|---:|
| common `C` | 4 | 60 |
| residual `L` or `R` | 4 | 60 |
| heavy `beta_T` | 24 | 40 |
| heavy `beta_M` | 14 | 50 |
| heavy `beta_B` | 24 | 40 |
| one-side total | 32 | 32 |

All three unordered heavy-pair commutators have active rank `12`; common and residual effects
commute with every heavy effect because their alphabet supports are orthogonal.  Restoring the
untouched occurrence factor multiplies these ranks by four.

At the same raw mark, the only nonzero left/right branch product is common/common:

\[
F_C^LF_C^R={1\over288^2}D_C\otimes I_{Z_L}\otimes I_{Z_R}.
\]

Every other left/right product is zero in both orders.  Hence all same-mark cross-side effects
commute, consistently with the reviewed direct-coset theorem.

## 5. Full unmatched-complement audit

The independent YES review archives exact six-column complements `u_L,u_R` in the marked gauge.
For each orientation and each side, the tool evaluates both

\[
u_o^*F^su_o,
\qquad
(I-u_ou_o^*)F^su_o.
\]

At alphabet level the exact ranks are:

| orientation | queried side | complement diagonal rank | common/unmatched leakage rank |
|---|---|---:|---:|
| `L` | left | 3 | 1 |
| `L` | right | 4 | 2 |
| `R` | left | 4 | 2 |
| `R` | right | 3 | 1 |

Tensoring the active occurrence identity multiplies these ranks by four.  Thus neither orientation
permits deletion of its complement; both the unmatched diagonal and common-to-unmatched leakage
are physically nonzero.  This is also why an orientation pullback cannot stand in for the native
rectangular transfer.

## 6. What fixed-mark covariance actually proves

Let `G=S_64`, let `H=Stab(z_*)` (isomorphic to `S_63`), and let `U_t` be the full alphabet action on the NO/YES
selected sources.  Suppose the **complete** fixed-mark effects

\[
A_t=F^s_{t,z_*}
\]

satisfy `[A_t,U_t(h)]=0` for every `h in H`.  For any coset representative `g_z` with
`g_z z_*=z`, define

\[
F^s_{t,z}=U_t(g_z)A_tU_t(g_z)^*.
\tag{6.1}
\]

If `g'_z=g_zh`, stabilizer invariance makes (6.1) independent of the representative.  Vectorizing
the native transfer gives the exact correlated coset twirl

\[
\boxed{
K_s=\sum_{z=1}^{64}(F^s_{0,z})^T\otimes F^s_{1,z}
=\sum_{gH}W(g)(A_0^T\otimes A_1)W(g)^*,
\quad W(g)=\overline{U_0(g)}\otimes U_1(g).}
\tag{6.2}
\]

Therefore complete fixed-mark data plus the actual transporter action are sufficient in principle.
One must not replace (6.2) by `64(A_0^T tensor A_1)`, and one must not independently average the
NO and YES factors: the same `gH` occurs on both sides.  The exact synthetic coset guard in the
tool verifies representative independence and falsifies both wrong substitutions.

Because every `A_t` is positive self-adjoint, every summand `A_0^T tensor A_1` in the real
deterministic gauge is positive self-adjoint.  Hence both the common-child partial twirl and the
eventual complete transfer are positive self-adjoint on their correctly typed rectangular
Hilbert--Schmidt spaces.  This formula-level property does not determine their rank or kernel.

No distinct-mark **values** are independent unknowns after (6.1).  What remains necessary is the
complete fixed-mark seed and an evaluated representation/Wigner implementation of (6.2).

## 7. Why the common child is not the literal effect

The three reviewed parents have the following exact `S_64 downarrow S_63` branching:

\[
\begin{aligned}
(62,2)&\downarrow (61,2)\oplus(62,1),\\
(61,3)&\downarrow (61,2)\oplus(60,3),\\
(61,2,1)&\downarrow (61,2)\oplus(60,2,1)\oplus(61,1,1).
\end{aligned}
\tag{7.1}
\]

The exact carrier dimensions are

\[
\begin{array}{c|c}
\text{shape}&f^{\text{shape}}\\ \hline
(61,2)&1890\\
(62,1)&62\\
(60,3)&37758\\
(60,2,1)&75579\\
(61,1,1)&1891.
\end{array}
\]

They resolve the parent dimensions exactly:

\[
1952=1890+62,
\quad39648=1890+37758,
\quad79360=1890+75579+1891.
\tag{7.2}
\]

Thus `tau_*` is a proper marked subspace in every parent.  The literal resolution in the reviewed
classification sums every point child, status, position predecessor, and compatible heavy path.
The common-`tau_*` effect constructed here is one positive component of `F_(t,z_*)`; it is not
`F_(t,z_*)` itself.  Covariance cannot manufacture the four missing private-child seeds because
it only moves a fixed child between conjugate point stabilizers.

### Exact two-completion inference guard

There is an exact information-theoretic guard even after imposing the same central marginal mass.
Inside the parent `nu=(61,2,1)`, keep the reviewed common-child block fixed and consider one
nonzero missing scalar multiplicity line.  Allocate one unit of its missing central marginal to
either private child `chi_A=(60,2,1)` or `chi_B=(61,1,1)`.  The required fixed-mark seed scale is

\[
a_\chi={f^\nu\over64f^\chi},
\]

because summing its 64 conjugates gives

\[
64{f^\chi\over f^\nu}a_\chi I=I.
\]

Both completions are `H`-equivariant and positive, retain the same reviewed common-child block,
and add the same central single-effect marginal.  But if the same completion is used on the NO
and YES scalar lines, its equality-transfer coefficient is

\[
64{f^\chi\over f^\nu}a_\chi^2=a_\chi.
\]

The two exact values are

\[
a_{(60,2,1)}={1240\over75579},
\qquad
a_{(61,1,1)}={40\over61},
\]

which are unequal.  This guard does not claim either artificial allocation is the actual k-Sum
row.  It proves that the reviewed common-child matrices, covariance, positivity, and the same
missing central marginal do not determine the literal equality transfer.  The physical private
rows are precisely the missing information that selects the real completion.

## 8. The unevaluated common-child Wigner interface

Even for the legitimate partial orbit of `tau_*`, reduced `40 x 40` and `64 x 64` matrices do not
contain the full carrier action.  Let

\[
\iota_{\nu,\tau}:S^\tau\hookrightarrow S^\nu
\]

be the deterministic last-letter branching isometry.  A cross-parent carrier block transported
to mark `z` is

\[
P_{\tau,z}^{\nu'\leftarrow\nu}
=\rho_{\nu'}(g_z)\iota_{\nu',\tau}\iota_{\nu,\tau}^*
 \rho_\nu(g_z)^*.
\tag{8.1}
\]

The vectorized target/source contraction needs the correlated four-parent kernel

\[
\boxed{
\Omega_{\tau}
=\sum_z
\left(P_{0,\tau,z}^{\nu'_0\leftarrow\nu_0}\right)^T
\otimes
P_{1,\tau,z}^{\nu'_1\leftarrow\nu_1}.}
\tag{8.2}
\]

The parent shapes determine (8.2) uniquely up to coherent gauge, but no reviewed artifact evaluates
it.  Fixed-mark reduced effects alone therefore do not give the full-Hilbert--Schmidt matrix,
rank, kernel, or spectrum.  Scalar trace identities such as
`sum_z P_(tau,z)^nu=(64 f^tau/f^nu)I` do not determine the four-parent kernel (8.2).

## 9. Minimal next exact reducer

The smallest route to the literal finite transfer is:

1. At the same fixed mark, construct the NO and YES reduced point-child tables for the four
   private shapes in (7.1), retaining every parent multiplicity, actual status, all three position
   predecessors, every compatible heavy path, and the unequal-cell normalization.
2. Assemble those tables with the already reviewed occurrence and corrected transported Pieri
   factors.  Verify the complete fixed-mark resolution before any central averaging.
3. In sparse Young-seminormal form, construct
   `rho_nu((z,64)) iota_(nu,tau)` for all three parents, all five children, and `z=1,...,64`.
4. Contract the **same-`z`** target/source blocks into (8.2).  Do not substitute a colored
   representative and do not multiply independent target/source twirls.
5. Tensor the carrier kernels with the reduced effects, retaining all `16` YES columns.  Only
   then compute the exact rectangular transfer rank, kernel, joint spectrum, or numerator-active
   blocks.

Explicitly enumerating unrelated distinct-mark row values is unnecessary if step 3 proves the
transport identity.  Cross-orientation data are also unnecessary for the native transfer; they
are needed only for a separately stated pullback problem.

## 10. Failure guards

| failure mode | exact disposition |
|---|---|
| omit YES unmatched complement | both orientation complements have nonzero diagonal action and leakage; `96` full multiplicity dimensions are retained |
| wrong unequal-cell scaling | the hash-pinned YES review's independent checker gives exact skew rank `8` for the old scaling |
| replace central sum by one colored representative | exact coset guard falsifies `64(A_0^T tensor A_1)` |
| take independent NO/YES twirls | exact coset guard distinguishes them from the correlated same-coset sum |
| multiply raw forms | wrong active raw-form commutator rank is `10`, while the typed `G^{-1}H` effect rank is `8` |
| orientation pullback as native transfer | it reduces `256` target multiplicity dimensions to `160` and drops `96` unmatched dimensions |
| call common `tau_*` the literal effect | exact branching (7.1)--(7.2) exhibits four missing private children |
| infer a spectrum from finite factors | no carrier kernel (8.2), transfer rank, kernel, or spectrum is reported |

## 11. Reproduction and immutable evidence

Tool:
`ksum/tools/ksum_l3_first_target_yes_physical_central_gate.py`, SHA-256
`0179A097C3C99A4190D1466919625903C49831C7C182FD46172C03685A583725`.

Exact JSON:
`ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_gate_20260722/run.json`, SHA-256
`C6EF5ED201E1570AF86D8F7867CF27D1EBA48B117688F6B4052681931E143D0F`.

Concise log:
`ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_gate_20260722/run.log`, SHA-256
`8B1A6C295A58DC557C4438C54E896C98214873C7A78BCE451E8CF2A7D076F5B1`.

PowerShell reproduction commands:

```powershell
python ksum/tools/ksum_l3_first_target_yes_physical_central_gate.py --output-json ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_gate_20260722/run.json --output-log ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_gate_20260722/run.log
python ksum/tools/ksum_l3_first_target_yes_physical_central_gate.py --verify-json ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_gate_20260722/run.json
```

The first command prints `ALL_EXACT_YES_PHYSICAL_CENTRAL_DECISION_GATES_PASS`; the second prints
`ARCHIVED_YES_PHYSICAL_CENTRAL_DECISION_VERIFIED`.

## 12. Exact license and stopping point

Licensed at proposer tier, pending fresh review:

* the finite common-`tau_*` YES physical reduced assembly and its exact ranks/commutators;
* retention and nontrivial action of the entire YES unmatched complement;
* the exact correlated fixed-mark covariance identity;
* the five-child inventory and proof that common `tau_*` is not the literal effect;
* the exact two-completion insufficiency guard and the minimal next reducer.

Withheld:

* all private-child physical row values;
* the evaluated carrier/Wigner kernel;
* the literal native central transfer, its rank, kernel, or spectrum;
* any joint spectrum or numerator-active block;
* any resolvent/taper feasibility, query attenuation, coefficient norm, numerator, lower bound,
  or exponent conclusion.
