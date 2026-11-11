# Qutrit Weyl random-unitary factors reduce to a classical autocorrelation entropy gate

Date: 2026-08-30

Status: proposer-side exact reduction; the final classical inequality is now resolved by the
linked selected-line majorization theorem.  Independent review is pending.

All logarithms are base two.  Let `G=F_3^2`, let `{W_z:z in G}` be a qutrit Weyl system, and let

\[
 \Phi_p(\rho)=\sum_{z\in G}p_zW_z\rho W_z^\dagger
\tag{1}
\]

for a probability distribution `p` on `G`.  This family is bistochastic and automatically gives a
Hilbert--Schmidt-positive Gram channel `Phi_p Phi_p^*`; it therefore starts beyond the orientation
obstructions that killed the `G2` and octonionic support candidates.

## 1. Exact Bell-output entropy

For the normalized maximally entangled input, Weyl covariance and

\[
 (A\otimes\bar B)|\Omega\rangle=(AB^\dagger\otimes I)|\Omega\rangle
\tag{2}
\]

show that the output of `Phi_p tensor bar(Phi_p)` is diagonal in the nine-element Bell basis.  Its
probability distribution is the group autocorrelation

\[
 q_g=(p*\widetilde p)_g=\sum_{z\in G}p_zp_{z-g}.
\tag{3}
\]

Consequently

\[
 S((\Phi_p\otimes\bar\Phi_p)(\Omega_3))=H(p*\widetilde p).
\tag{4}
\]

## 2. Four exact stabilizer side bounds

The four one-dimensional subspaces `L<=G` are the four qutrit stabilizer directions.  Choose a
pure stabilizer state whose phase-space stabilizer is `L`.  Errors in one coset of `L` produce the
same output ray up to phase, while the three cosets produce an orthogonal basis.  The output
spectrum is therefore the quotient distribution

\[
 r_L(c)=\sum_{z\in c}p_z,
 \qquad c\in G/L.
\tag{5}
\]

This gives the exact upper bounds

\[
 S_{\min}(\Phi_p)\le\min_L H(r_L),
 \qquad
 \overline S_{\min}(\Phi_p)\le\min_L H(r_L),
\tag{6}
\]

where the regularized inequality follows by tensoring the same stabilizer input.

Combining (4) and (6) yields

\[
 2\overline S_{\min}(\Phi_p)
 -S((\Phi_p\otimes\bar\Phi_p)(\Omega_3))
 \le
 2\min_LH(r_L)-H(p*\widetilde p).
\tag{7}
\]

Thus the uniform classical inequality

\[
 \boxed{H(p*\widetilde p)\ge2\min_{L\le\mathbb F_3^2}H(p\bmod L)}
\tag{8}
\]

would exclude the entire fixed-qutrit Weyl random-unitary conjugate-Bell route, including its
regularized version.  Conversely, a positive right-hand side in (7) is only a candidate signal:
the stabilizer input need not minimize output entropy.

## 3. Exact Renyi-2 shadow of the Shannon inequality

Before the full Shannon proof was found, its collision-entropy analogue supplied an exact global
shadow.  Write

\[
 H_2(s)=-\log\sum_xs_x^2.
\]

For the autocorrelation `q=p*tilde p`, let

\[
 q_0=\sum_zp_z^2,
 \qquad x_i=q_{g_i}=q_{-g_i}\quad(i=1,\ldots,4),
\tag{9}
\]

where `{+/-g_i}` are the four nonzero projective directions.  Cauchy--Schwarz gives
`0<=x_i<=q_0`, and normalization gives `q_0+2 sum_i x_i=1`.

For the line `L_i={0,+/-g_i}`, the quotient collision probability is

\[
 C_i=\sum_c r_{L_i}(c)^2
 =\Pr[X-Y\in L_i]
 =q_0+2x_i.
\tag{10}
\]

The autocorrelation collision probability is

\[
 C_q=\sum_gq_g^2=q_0^2+2\sum_i x_i^2.
\tag{11}
\]

A direct calculation now gives

\[
 \sum_{i=1}^4C_i^2-4C_q
 =4\sum_{i=1}^4x_i(q_0-x_i)\ge0.
\tag{12}
\]

Hence `max_i C_i^2>=C_q`, which is exactly

\[
 \boxed{H_2(p*\widetilde p)\ge2\min_LH_2(p\bmod L).}
\tag{13}
\]

This is a genuine global theorem on the full simplex, but it does not imply (8): Shannon entropy
dominates collision entropy on both sides, and the required comparison between the two minima has
the wrong direction for a direct substitution.

## 4. The stronger selected-line majorization theorem

The numerical data suggested a sharper statement that implies (8) immediately.  For each line
direction `L`, let `r_L` be the three parallel-line masses, and choose a direction `L_*` for which
`max_c r_L(c)` is largest over all four directions.  The candidate theorem is

\[
 \boxed{p*\widetilde p\ \prec\ r_{L_*}\otimes r_{L_*}.}
\tag{14}
\]

Here `prec` denotes vector majorization after sorting all nine entries.  If (14) holds, every
Schur-concave entropy gives

\[
 H(p*\widetilde p)\ge H(r_{L_*}\otimes r_{L_*})=2H(r_{L_*}),
\tag{15}
\]

which is stronger than (8).  It also explains why scans over many Renyi indices show the same
sign.

The original reproduction script checked all eight nontrivial cumulative-sum inequalities in
(14), and no counterexample appeared in the seeded sample.  The exact proof now proceeds through
odd cumulative indices: complete certificates establish `k=1,3,5,7`, while paired
autocorrelation values and sorted product entries interpolate `k=2,4,6,8`.

The exact affine-plane maximal theorem first proves

\[
 \max_g(p*\widetilde p)_g=(p*\widetilde p)_0=\sum_xp_x^2\le M^2,
\tag{16}
\]

where `M=max_c r_{L_*}(c)`.  Since `M^2` is the largest entry of
`r_{L_*} tensor r_{L_*}`, equation (16) is precisely majorization at cumulative index one.  A
second exact 18,564-active-set parametric certificate proves the cumulative `k=3` inequality.
Two complete eight-dimensional KKT-face enumerations prove a stronger `k=5` inequality and the
`k=7` inequality.  Because the eight nonzero autocorrelation entries occur in equal pairs, every
even cumulative sum of `q` is the average of its neighboring odd sums; sortedness makes the
corresponding product cumulative sum at least that average.  Thus all even indices follow and
(14) holds.  The full proof and terminal counts are in
`F3_WEYL_SELECTED_LINE_MAJORIZATION_THEOREM_20260830.md`.

## 5. Historical numerical screen and exact boundary

A seeded 200,000-sample Dirichlet scan over the eight-dimensional probability simplex found no
positive value of the right-hand side of (7).  The point-mass distributions and the uniform
distribution have exact value zero.  Earlier channel-level sampling with general and stabilizer
pure inputs likewise found no positive Bell defect.

These observations did **not** prove (8); they only selected the successful route.  The subsequent
exact majorization theorem does prove (8), so the qutrit Weyl conjugate-Bell family is closed.  The
active search must move to non-Weyl qutrit Gram channels or non-Bell joint inputs.

Reproduction:

```text
python3 holevo-extensive-violation/tools/screen_qutrit_weyl_bell_gate.py \
  --samples 200000 --seed 20260830
```

## Scope

- Equation (7) is an exact proposer-side reduction awaiting independent review.
- Equation (13) is an exact proposer-side global collision-entropy theorem.
- Equation (14) is an exact proposer-side computer-assisted theorem awaiting independent review.
- The sample is route-selection evidence only.
- The reduction covers qutrit Weyl random-unitary factors and their product Bell witness, not all
  qutrit Gram channels or non-Bell joint inputs.
- The full-size extensive question remains open.
