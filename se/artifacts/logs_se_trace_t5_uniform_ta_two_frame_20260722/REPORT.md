# Uniform `T-a` normalization audit: two tame physical counterexamples

Date: 2026-07-22  
Scope: source artifact only; no DAG, note, paper, or `ksum` edit

## Verdict

**REFUTED.** The registered raw physical inequality

\[
 T_a\le B_\theta(q)^2T
\]

fails at both independently constructed tame `c=2` packets once the literal
colour multiplicity `m=C(j,a)=20` is restored. The archived final contraction
scripts divided the raw physical value by `m` and therefore incorrectly
reported both gates as passing.

This is not a mechanism-only counterexample. It is an exact correction of the
actual registered long contraction using the stored physical `R_out` and
carrier data.

## 1. Exact normalization chain and source locations

There are two conventions that must not be mixed.

### Raw registered branch

In `se/artifacts/logs_se_trace_t3_20260721/se_trace_t3_report_20260721.md`,
equation (3.2) puts `m=C(j,a)` and states

\[
 S_{h,\gamma}S_{h,\gamma}^*=mK_\gamma.
\]

The same report defines `A_gamma=S_(h,gamma)^*S_(h,gamma)`. The exact hostile
implementation `se/artifacts/logs_se_trace_t3_majorization_20260721/
se_trace_t3_majorization.py`, lines 218--230, horizontally stacks every
physical coloured branch block with no `1/sqrt(m)` factor and sets
`a0=s0.T*s0`. Its actual contraction is `Tr(a0*dmat)` at lines 280 and 311.

The complete non-tame `c=2` implementation independently uses the same raw
typing. In `se/artifacts/logs_se_trace_t5_c2_gate_20260721/
se_trace_t5_c2_gate.py`, lines 279--283, `K[name]` is a horizontal stack of
all 20 physical colour blocks; lines 390--410 compute the actual value from
`product=K[name]@L` with no normalization.

### Common-line coordinates

The common-line report defines the raw fold

\[
 F_L(y_D)_D=\sum_{D\mapsto L}U_Dy_D
\]

in equation (2.2), explicitly saying that `1/sqrt(m)` is optional and must be
absorbed into the branch scalar. Its equations (3.3)--(4.3) define
`a_(gamma,mu)=||v_(gamma,mu)||^2` and

\[
 T_a=\sum_\mu f^\mu a_{0\mu}r_\mu.
\]

For the tame `c=2` packets, `R_out` makes the factor explicit. Section 3 of
`se/artifacts/logs_se_trace_t5_tame_c2_rout_20260721/REPORT.md` states

\[
 a_{\gamma\mu}=20|d_{\gamma\mu}|^2.
\]

The carrier report defines

\[
 \|t_\mu\|^2=\|(FL)^*e_\mu\|^2,
 \qquad r_\mu=\|t_\mu\|^2/20.
\]

Therefore the registered raw block contribution is

\[
 a_{0\mu}r_\mu
 =20|d_{0\mu}|^2r_\mu
 =|d_{0\mu}|^2\|t_\mu\|^2.                 \tag{1}
\]

## 2. The exact bug in both tame gate scripts

In `se/artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/construct_rcol.py`,
`D2["long"]` stores `|d_(0,mu)|^2` (lines 35--39), while lines 625--631 set
`r_mu=t_squared/20` and contract `D2*r_mu`. Thus the script evaluates

\[
 \sum_\mu f^\mu |d_{0\mu}|^2r_\mu={T_a\over20},       \tag{2}
\]

not (1). The `n=19` script mechanically inherits the same convention. Its
JSON likewise stores `a_mass=20*d_squared` but contracts `d_squared*r_mu`.

The mismatch is visible without numerical inference: (1) follows symbol by
symbol from the registered raw definitions, while (2) is the literal code.

## 3. Corrected exact physical values

Joining every stored `f^mu`, `r_mu`, and long `d_squared` row gives the
archived divided values exactly. Multiplying by the missing `m=20` gives:

| tame gate | corrected raw physical `T_a` | cap | exact excess | ratio |
|---:|---:|---:|---:|---:|
| `n=18,j=6,c=2` | `160582822829/85260` | `51396202/35` | `35381674757/85260` | `36224413/28242984` |
| `n=19,j=6,c=2` | `204466088827/71920` | `137582445/64` | `199431265033/287680` | `10611004/8023575` |

Both ratios are strictly greater than one (approximately `1.2826` and
`1.3225`). Every quantity is rational and comes from the persisted exact
tables; no fit, floating reconstruction, or extrapolation is used.

## 4. Why the tempting two-frame proof loses exactly `m`

Let `F~=F/sqrt(m)` and `C=F~L_h`. The reviewed input frame and Pieri rank give

\[
 \|C\|_{op}^2\le B_\theta(q),\qquad
 \operatorname {rank}C\le\dim\mathscr Y.
\]

For the uncoloured synthesis map `E`, the complete fixed-set frame gives

\[
 EE^*=\sum_L\Pi_L=B_\theta(q)I.
\]

Hence `O0=Q0 Pcomp E` satisfies `||O0||op^2<=B`, and

\[
 \|O_0C\|_{HS}^2\le B^2\dim\mathscr Y.                \tag{3}
\]

But `O0 C=S_0L_h/sqrt(m)`. Thus (3) bounds `T_a/m`, not `T_a`:

\[
 T_a\le mB^2\dim\mathscr Y\le {m\over c}B^2T.
\]

At `m=20,c=2` this is far too weak. The exact output frame is sharp in both
tame packets: `max_mu |d_(0,mu)|^2=B`, equal to `341/280` at `n=18` and
`77/64` at `n=19`.

This diagnoses precisely why the otherwise valid effective-rank idea cannot
close raw `T-a`.

## 5. Scope and consequences

- The refutation is of uniform registered physical `T-a`, not of a von
  Neumann surrogate.
- The same normalization defect reaches the claimed uniform `T-b` theorem:
  its chain uses `h_mu=sum_z|d_(z,mu)|^2` and therefore bounds raw `T_b/m`,
  while the registered branch masses are `m|d|^2`. The uniform physical
  `T-b` conclusion must be reopened. This audit does not produce a physical
  `T-b` counterexample: after restoring `m=20`, both tame finite gates still
  pass their tail caps.
- The earlier `c=1` orbital formulas are unaffected when `m=1` on an extreme
  face, but mixed `c=1` computations must retain their raw `m` convention.
- The two tame `c=2` gate verdicts for `T-a` require correction. Their stored
  `R_out`, `R_col`, `q_mu`, `t_mu`, and `r_mu` data remain useful; only the
  final long contraction omitted `m`.

## Reproducibility

The attached script verifies nine dependency manifests, recomputes both
eight-block divided contractions, restores `m=20`, checks the two strict
violations, verifies `max d0^2=B`, and checks the known `j=1` formulas and
exact standard fixed-point frames. Output is exact JSON plus a concise log.

No DAG, notes, handoff, paper, `research/ksum`, or git-history file was
modified. No commit was created.
