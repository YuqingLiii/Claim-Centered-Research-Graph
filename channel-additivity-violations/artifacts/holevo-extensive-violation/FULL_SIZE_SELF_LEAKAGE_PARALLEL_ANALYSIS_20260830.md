# Full-size self-leakage parallel analysis

Date: 2026-08-30

Status: independent parallel derivation; **the full-size claim remains OPEN**.  This note does not
alter any canonical node or assessment.  It separates the already available finite-dimensional
absolute-unbounded result from the still missing fixed-finite all-copy estimate.

All logarithms are base two.

## Executive conclusion

The tensor-copy leakage identities in `TENSOR_COPY_LEAKAGE_PROOF_20260829.md` are correct.  For a
fixed finite pair, a positive asymptotic defect is exactly a regularized-MOE question.  For the
product-Haar block `L_J` and its conjugate, the required sufficient inequality is

\[
 \gamma_J>2\ell_J,
 \qquad
 \ell_J=S_{\min}(L_J)-\overline S_{\min}(L_J),
\tag{1}
\]

where `gamma_J` may be the actual one-shot pair gap or the smaller product-Bell certificate.
No audited external theorem proves (1), a uniform `O(1)` bound on `ell_J`, or even
`ell_J=o(J)` for one fixed successful finite realization.

There are, however, two rigorous new reductions.

1. Montanaro's Haar-random-subspace theorem cannot be imported: the Stinespring projector of a
   random-unitary block has an exactly maximally mixed partial trace and is tensor decomposable,
   so its distribution is singular with respect to Haar measure on the relevant Grassmannian.
   More strongly, even a fictitious application of the theorem lands in its half-rate regime and
   gives only `bar S_min(L_J) >= (J/2) log m-O(1)`.
2. The deterministic partial-transpose relaxation underlying that theorem has an exact obstruction
   on these blocks:

   \[
      \|P_J^\Gamma\|_\infty\ge m^{-J/2}.
   \tag{2}
   \]

   Hence that relaxation can never certify more than `(J/2) log m` bits per block, whereas the
   construction needs a side rate close to `J log m`.  This rules out a whole proof interface, not
   the true channels.

The sharp next lemma is narrower than uniform `O(1)` leakage.  Let `C_J=L_J^c`, let `q=m^J`, and
let

\[
 A_{J,\eta}=1+(1+\eta)^2\big((1+9/m)^J-1\big).
\tag{3}
\]

For one fixed finite realization already satisfying the one-copy strong-convergence estimate, it
would suffice to prove the **self-only purity multiplicativity**

\[
 \sup_\rho \operatorname{Tr}\!\left[C_J^{\otimes n}(\rho)^2\right]
 \le \left(\frac{A_{J,\eta}}q\right)^n
 \quad\text{for every }n\ge1.
\tag{4}
\]

Equation (4) concerns only physical outputs of repeated copies of the same selected tuple.  It is
strictly weaker in scope than a small completely bounded distortion estimate and need not hold for
`C_J tensor bar(C_J)`.  If (4) holds, then

\[
 \overline S_{\min}(L_J)\ge \log q-\log A_{J,\eta},
\tag{5}
\]

and the product Bell witness gives the regularized pair defect lower bound

\[
 \overline\Delta(L_J,\bar L_J)
 \ge \frac{J\log m}{m}-2\log A_{J,\eta}.
\tag{6}
\]

At `eta=0`, the right side is exactly `J c_m`, where

\[
 c_m=\frac{\log m}{m}-2\log(1+9/m)>0
 \quad(\ln m>18).
\tag{7}
\]

Thus a sufficiently small fixed `eta` makes (6) positive.  Proving (4), or an entropy analogue
with the same exponent, would close the fixed-pair regularized gate and therefore the full-size
question.  No cited result currently supplies (4).

## 1. Quantifiers and dimensions

Fix `m>e^18`.  For every hierarchy depth `J`, the absolute-unbounded proof first fixes `J`, then
chooses `eta`, and only afterward chooses a sufficiently large finite per-leg dimension `D` and a
successful tuple.  The channels are

\[
 \Phi_{j,D}(\rho)=\frac1m\sum_{i=1}^mU_{i,j}\rho U_{i,j}^*,
 \qquad
 L_J=\bigotimes_{j=1}^J\Phi_{j,D}.
\tag{8}
\]

Their dimensions are

| channel | input | output | minimal Stinespring environment (upper bound) |
|---|---:|---:|---:|
| `L_J` | `D^J` | `D^J` | `m^J` |
| complement `C_J=L_J^c` | `D^J` | `m^J` | `D^J` |

Minimum output entropy, including every tensor power, is unchanged by passing to the complementary
channel.  The existing proof establishes

\[
 \forall G\;\exists J\;\exists\eta\;\lim_{D\to\infty}
 \Pr[\Delta(L_J,\bar L_J)>G]=1.
\tag{9}
\]

The full-size bootstrap needs a different order:

\[
 \exists J,D,(U_{i,j})\;\forall n\ge1:
 \text{a sufficiently strong side-entropy estimate for }L_J^{\otimes n}.
\tag{10}
\]

If (10) yields any positive regularized defect `delta_J>0`, then tensoring this one fixed block `n`
times gives defect `n delta_J+o(n)`.  The complete input/output/minimal-environment qubit cost is
`Theta(nJ(log D+log m))`.  Since `J,D` are fixed constants at that stage, the ratio is positive.
Thus the uncontrolled function `D(J)` ceases to matter after one successful regularized block is
selected.  This is why self-leakage is a genuine bypass of the tensor-strong-convergence rate gate.
The repository's finite Weyl-flag transfer acts at every tensor exponent, and the balanced
direct-sum pair-to-self step has only constant logarithmic overhead/loss.  Therefore a positive
fixed-pair regularized MOE rate here transfers to the claimed full-size Holevo scaling; those
reductions do not supply the missing estimate (10).

## 2. Exact tensor-copy bookkeeping

For arbitrary finite channels `N,M`, set

\[
 \Delta=S_{\min}(N)+S_{\min}(M)-S_{\min}(N\otimes M),
\]

\[
 \alpha_n=nS_{\min}(N)-S_{\min}(N^{\otimes n}),\qquad
 \beta_n=nS_{\min}(M)-S_{\min}(M^{\otimes n}).
\]

Using the product of `n` minimizing inputs for `N tensor M` gives

\[
 \Delta_n(N,M)\ge n\Delta-\alpha_n-\beta_n.
\tag{11}
\]

After division by `n`, Fekete's lemma gives the exact limit

\[
 \lim_{n\to\infty}\frac{\Delta_n(N,M)}n
 =\overline S_{\min}(N)+\overline S_{\min}(M)
  -\overline S_{\min}(N\otimes M).
\tag{12}
\]

Let `ell_N=S_min(N)-bar S_min(N)`.  Since
`bar S_min(N tensor M)<=S_min(N tensor M)`, one has

\[
 \overline\Delta(N,M)\ge\Delta-\ell_N-\ell_M.
\tag{13}
\]

For `M=bar N`, conjugation preserves all tensor-power output spectra, so `ell_M=ell_N` exactly.
For the selected product-Haar block, the condition is therefore (1), not merely small leakage on
average over newly sampled layers.

There is no hidden implication from the one-shot unbounded result to (1): the copies in
`L_J^tensor n` reuse the same `mJ` sampled unitaries, whereas Bordenave--Collins controls a fixed
number of independently placed tensor legs only after increasing `D`.

## 3. Haar-random-subspace weak multiplicativity does not transfer

### 3.1 The distributions are singular

For one random-unitary layer, use the Stinespring isometry

\[
 Vx=\frac1{\sqrt m}\sum_{i=1}^m U_i x\otimes |i\rangle,
 \qquad P=VV^*.
\tag{14}
\]

Then `P` has rank `D` in `C^D tensor C^m` and satisfies the exact constraint

\[
 \operatorname{Tr}_{\mathbb C^m}P
 =\frac1m\sum_iU_iU_i^*=I_D.
\tag{15}
\]

A Haar-uniform rank-`D` projector in `C^D tensor C^m` satisfies (15) with probability zero: (15)
is a nontrivial system of polynomial equalities, not an almost-sure property of a Haar point on the
Grassmannian.  At depth `J`,

\[
 P_J=P_1\otimes\cdots\otimes P_J,
 \qquad \operatorname{Tr}_{(\mathbb C^m)^{\otimes J}}P_J=I_{D^J},
\tag{16}
\]

and the additional tensor-decomposability constraint makes the mismatch still stronger.  Thus a
probability-one theorem for Haar subspaces says nothing about the product-Haar tuple distribution
without a new comparison theorem.  There is no absolute-continuity shortcut.

### 3.2 Even a fictitious application has the wrong rate

Montanaro's theorem orders the two Stinespring factors as `d_A<=d_B`.  For the whole block,

\[
 d_A=m^J,\qquad d_B=D^J,\qquad r=D^J.
\tag{17}
\]

The channel is necessarily in the first regime because

\[
 r=D^J\ge D^J/m^J=d_B/d_A;
\tag{18}
\]

the second regime would require `m^J<=1`.  The von-Neumann consequence is only

\[
 \overline S_{\min}(L_J)
 \ge \frac12(\log d_A+\log d_B-\log r)-C
 =\frac J2\log m-C.
\tag{19}
\]

Since pure outputs of `L_J` have rank at most `m^J`, `S_min(L_J)<=J log m`; (19) permits an
absolute self-loss as large as `(J/2)log m+C`.  The certified one-shot gap is only `Jc_m`, with
`c_m<=log(m)/m`.  Hence (19) is parametrically too weak by a factor of order `m`, even before the
distribution and theorem-hypothesis failures are considered.

The theorem also assumes

\[
 m^J\ge2(J\log_2D)^{3/2}.
\tag{20}
\]

The fixed-depth strong-convergence proof gives no upper bound on the chosen `D(J)`, so (20) is not
automatically licensed for the selected block.

### 3.3 Exact obstruction inside the partial-transpose method

Montanaro's deterministic interface is

\[
 \|N^{\otimes n}\|_{1\to\infty}
 =h_{\rm SEP}(P^{\otimes n})
 \le\|(P^{\otimes n})^\Gamma\|_\infty
 =\|P^\Gamma\|_\infty^n.
\tag{21}
\]

Thus

\[
 \overline S_{\min}(N)\ge-\log\|P^\Gamma\|_\infty.
\tag{22}
\]

For the product block, partial transpose preserves Hilbert--Schmidt norm and `P_J` is a rank
`D^J` projector on a space of dimension `(Dm)^J`.  Therefore

\[
 \|P_J^\Gamma\|_2=\sqrt{D^J},
 \qquad
 \|P_J^\Gamma\|_\infty
 \ge\frac{\|P_J^\Gamma\|_2}{\sqrt{(Dm)^J}}
 =m^{-J/2}.
\tag{23}
\]

Equations (22)--(23) prove that the numerical lower bound furnished by this relaxation can never
exceed `(J/2)log m`.  This is independent of randomness and of any tail estimate.  Consequently,
sharpening only the random-matrix estimate for `||P^Gamma||` cannot produce `O(1)` or `o(J)`
self-leakage for these high-side-entropy blocks; a different tensor-stable functional is required.

## 4. Other external interfaces

### 4.1 Bordenave--Collins and Magee--de la Salle

Bordenave--Collins Theorem 9.2 has the order `for every fixed tensor depth, D->infinity`.  Its
quantitative Lemma 9.3 forces `D` to grow with depth in the present certificate.  It does not give
one finite tuple controlled for every self-copy number.

Magee--de la Salle allow representation degree at most `D^A` while `D->infinity`.  For each fixed
`D` that window is finite.  Moreover their representation is diagonal in one free-group word,
whereas a complementary output of `Phi^tensor n` contains independently indexed factors

\[
 (U_{i_1}^*U_{j_1})\otimes\cdots\otimes(U_{i_n}^*U_{j_n}).
\tag{24}
\]

Neither result supplies the `exists D, for every n` order.

### 4.2 Fukuda--Nechita multiplicative additivity-rate bounds

These bounds do apply to every tensor power of a fixed finite channel.  But every individual lower
bound is generated by a tensor-multiplicative functional.  Applying that same functional to
`L_J tensor bar(L_J)` lower-bounds every matched joint output by the sum of the two side bounds.
It therefore makes the proposed Bell-defect coefficient nonpositive identically.  This is an exact
proof-method obstruction: such a common multiplicative bound cannot distinguish safe self-tensors
from the deliberately bad conjugate cross-tensor.

### 4.3 Special strong-additivity results

King's strong additivity theorem for unital qubit channels and the exact antisymmetric-state
results are genuinely all-copy, but their hypotheses do not include the present channels:
`C_J` has output dimension `m^J` and a product-random-unitary Stinespring support.  No reduction to
a unital qubit, depolarizing, entanglement-breaking, or antisymmetric channel is available.

### 4.4 Targeted literature boundary

The audited post-2024 papers do not change this status.  Kalantar--Shobeiri remain in the
infinite-dimensional commuting-operator model.  The targeted primary-source search also located
Collins--Parraud's concentration estimates for Haar-random subspaces, but those estimates concern
one-shot random-subspace output bodies, not all tensor powers of one fixed product-random-unitary
block.  This is a scoped search result, not a claim that no relevant theorem could exist under a
different terminology.

## 5. Entanglement cost has the wrong direction for self-leakage

There are two different Stinespring states in play, and neither currently lower-bounds the desired
side rate.

First, let `S=Ran(V)` be the Stinespring subspace of an arbitrary channel `N`, let `d` be its input
dimension, and set `tau=P_S/d`.  Every pure-state decomposition of `tau^tensor n` consists of
vectors in `S^tensor n`.  Hence

\[
 E_F(\tau^{\otimes n})\ge
 \min_{|\psi\rangle\in S^{\otimes n}}E(\psi)
 =S_{\min}(N^{\otimes n}),
\tag{25}
\]

and therefore

\[
 E_C(\tau)\ge\overline S_{\min}(N).
\tag{26}
\]

Thus `E_C(tau)` is an upper bound on the regularized minimum output entropy, not the missing lower
bound.  A large entanglement cost does not imply small self-leakage unless an additional symmetry
proves equality in (25) asymptotically.  No such symmetry is known for a fixed sampled tuple.

Second, for the Gram channel `Theta=(k/d)Phi Phi^*`, the repository proves

\[
 2\overline S_{\min}(\Phi)-S(Z)
 \le2E_C(\sigma_{BE})-S(E)_\sigma.
\tag{27}
\]

This is a necessary state-level screen for a positive Bell rate.  It again upper-bounds the desired
surplus.  Passing `E_C>S(E)/2` cannot prove a global all-input entropy lower bound; failing it can
only rule out a candidate.  The flower, qutrit-antisymmetric, Pauli, `G_2`, and octonionic analyses
illustrate precisely this one-way use.  None supplies an `O(1)` or `o(J)` self-loss estimate for
`L_J`.

## 6. The next lemma: physical self-purity, not complete distortion

The one-copy proof already supplies, for a successful block,

\[
 \sup_\rho\operatorname{Tr}[C_J(\rho)^2]
 \le\frac{A_{J,\eta}}q.
\tag{28}
\]

The missing lemma is exactly the self-tensor extension (4).  Its consequence is immediate:
von Neumann entropy dominates Renyi-2 entropy, complements have the same pure-input spectra, and
so

\[
 S_{\min}(L_J^{\otimes n})
 =S_{\min}(C_J^{\otimes n})
 \ge n(\log q-\log A_{J,\eta}).
\tag{29}
\]

For one layer, merging the equal Kraus labels on a Bell input gives entropy at most
`2 log m-(log m)/m`.  The product of the `J` Bell inputs therefore has entropy

\[
 b_J\le J\left(2\log m-\frac{\log m}{m}\right).
\tag{30}
\]

Using the product of this Bell input at every outer copy gives
`bar S_min(L_J tensor bar L_J)<=b_J`.  Equations (29)--(30) prove (6).

It is helpful to express the same cancellation as leakage bookkeeping.  Put

\[
 d_J=\log q-S_{\min}(L_J)\ge0.
\tag{31}
\]

Equation (29) implies

\[
 \ell_J\le\log A_{J,\eta}-d_J,
\tag{32}
\]

while (30) implies the one-shot Bell gap

\[
 \gamma_J=2S_{\min}(L_J)-b_J
 \ge\frac{J\log m}{m}-2d_J.
\tag{33}
\]

Subtracting twice (32) from (33) cancels the unknown one-shot deficit `d_J` and again gives (6).
Therefore the next lemma need not prove `ell_J=O(1)`; it may allow a linear loss
`log A=Theta(J/m)` provided it is the same one-sided purity exponent already present in the
one-shot construction.

The fixed-unitary cb-distortion counterexample does not refute (4).  Its bad coefficients are
arbitrary matrix-level coefficients and are physically realized by the conjugate Bell mechanism;
they have not been realized as centered outputs of `C_J^tensor n` on density operators.  The
self-only qualifier in (4) is load-bearing.

## 7. A concrete physical-range formulation

For possible proof attempts, define

\[
 R_{J,n}=q^n\sup_\rho
 \left\|C_J^{\otimes n}(\rho)-\frac{I_{q^n}}{q^n}\right\|_2^2.
\tag{34}
\]

Because every diagonal Kraus label has probability `q^{-n}`,

\[
 q^n\sup_\rho\operatorname{Tr}[C_J^{\otimes n}(\rho)^2]
 =1+R_{J,n}.
\tag{35}
\]

Thus (4) is equivalent to

\[
 1+R_{J,n}\le A_{J,\eta}^n\quad\text{for every }n.
\tag{36}
\]

This removes arbitrary coefficient matrices entirely.  A proof may use positivity, unit trace,
the fixed diagonal, or consistency under partial traces of genuine outputs.  Those constraints are
absent from the cb obstruction and from scalar strong convergence.  Equation (36) is the cleanest
next finite lemma to test.

## 8. Interface audit table

| Imported result/interface | Quantifiers actually supplied | Applies to selected block? | Enough for full-size? |
|---|---|---|---|
| Collins--Youn free-group bound | all copy depths in an infinite commuting/free model | only after finite-depth approximation | no finite fixed tuple |
| Bordenave--Collins tensor strong convergence | fixed `m,J`, then `D->infinity` | yes for one prescribed depth | no; wrong order for regularization |
| Bordenave--Collins quantitative rate | finite depth with `D` growing at least with depth | yes as a certificate | no; full cost is subextensive |
| Montanaro Haar-subspace weak multiplicativity | one Haar support, then all powers | no; singular ensemble mismatch | even fictitiously only half-rate |
| Montanaro/PPT deterministic relaxation | every fixed support, all powers | yes | no by (23) |
| Fukuda--Nechita additive rates | every fixed channel, all powers | yes | no; same functional kills Bell coefficient |
| Magee--de la Salle growing representations | degree `<=D^A` as `D->infinity` | not the full coefficient system | no fixed `D`, all `n` conclusion |
| Entanglement cost of a support/Gram state | regularized state quantity | yes as an upper screen | wrong inequality direction for side lower bound |
| Proposed physical-purity lemma (4)/(36) | one fixed tuple, every self-copy | precisely the needed scope | yes, by (6) |

## 9. Failure ledger and status boundary

- **Uniform `O(1)` leakage from Montanaro:** fails twice--the support distribution is not Haar,
  and the theorem's rate permits `Theta(J log m)` leakage.
- **Repair by sharpening only `||P^Gamma||`:** impossible within that relaxation because of the
  exact Hilbert--Schmidt floor (23).
- **Use a common tensor-multiplicative entropy bound:** cannot certify the conjugate Bell gap,
  because it also lower-bounds the matched joint witness.
- **Use entanglement cost as a side lower bound:** inequality direction is reversed; high cost is
  necessary at the Gram-state level but not sufficient.
- **Exchange finite-depth convergence with all-copy control:** invalid quantifier swap.
- **Promote arbitrary cb control to physical outputs:** the known obstruction rules out the broad
  route but does not decide the restricted physical set in (34).

The strongest conclusion of this note is therefore a strict narrowing, not closure:

\[
 \boxed{\text{Full-size extensive violation remains OPEN.}}
\]

The absolute-unbounded finite-dimensional result remains a distinct proposer-side theorem.  To
close the full-size route it is enough to prove (36) (or the corresponding von-Neumann entropy
bound) for one fixed successful block; no uniform theorem over all finite unitary tuples is needed.

## Primary sources and local interfaces

1. Ashley Montanaro, *Weak Multiplicativity for Random Quantum Channels*, arXiv:1112.5271,
   especially Proposition 4, Observation 5, Theorems 8--9, and the von-Neumann consequence on
   PDF pp. 5--7.  Local file:
   `holevo-extensive-violation/artifacts/primary-sources/montanaro-1112.5271.pdf`.
2. Benoit Collins and Sang-Gyun Youn, *Additivity Violation of the Regularized Minimum Output
   Entropy*, arXiv:1907.07856v2, Theorem 3.3.
3. Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries
   and permutations*, arXiv:2304.05714v2, Lemma 9.3 and Theorem 9.2.
4. Motohisa Fukuda and Ion Nechita, *Additivity rates and PPT property for random quantum
   channels*, arXiv:1411.6881, Lemma 4.2 and Proposition 4.4.
5. Benoit Collins and Felix Parraud, *Concentration estimates for random subspaces of a tensor
   product, and application to Quantum Information Theory*, arXiv:2012.00159.  Its scope is
   one-shot Haar-subspace concentration, not (10).
6. Repository derivations:
   `FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`,
   `UNBOUNDED_GAP_ADVERSARIAL_AUDIT_20260830.md`,
   `TENSOR_STRONG_CONVERGENCE_RATE_GATE_20260829.md`,
   `FINITE_UNITARY_CB_DISTORTION_OBSTRUCTION_20260829.md`,
   `FINITE_REGULARIZED_MOE_LITERATURE_GATE_20260830.md`,
   `ADDITIVE_BOUND_AMPLIFICATION_NO_GO_20260829.md`, and
   `GRAM_CHANNEL_ENTANGLEMENT_COST_GATE_20260830.md`.
