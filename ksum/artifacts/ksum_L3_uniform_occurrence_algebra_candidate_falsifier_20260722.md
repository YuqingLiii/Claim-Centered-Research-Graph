# L3 uniform occurrence-algebra candidate: independent exact falsifier

Date: 2026-07-22  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: independent exact falsifier artifact, pending fresh Rule-7 review.  No canonical/shared DAG
file was edited.  This artifact concerns only the occurrence multiplicity space and its six
corner/eta endomorphisms.  It makes no alphabet, Pieri, physical assembly, transfer, feasibility,
query, numerator, exponent, or asymptotic lower-bound inference.

## 1. Verdict

The registered candidate

\[
 C_s\stackrel?=1+\binom{s-1}{2},\qquad
 \mathcal A_s\stackrel?\cong
 \mathbb Q^{s-3}\oplus
 M_{(s^2-5s+10)/2}(\mathbb Q)
\tag{1.1}
\]

is false at the first untested legal member `s=6`.

There are two independent levels of failure.

1. A uniform Jacobi--Trudi/orbit calculation gives the exact formula

   \[
   \boxed{C_s=\sum_{k=0}^{s-2}p(k)},
   \tag{1.2}
   \]

   where `p(k)` is the integer-partition number.  Hence `C_6=12`, not `11`, and
   `C_7=19`, not `16`.
2. A self-contained exact `s=6` James/Jucys--Murphy computation constructs all six
   `12 x 12` rational forms.  Their generated rational algebra is

   \[
   \boxed{\mathcal A_6\cong M_1(\mathbb Q)\oplus M_{11}(\mathbb Q)},
   \tag{1.3}
   \]

   with dimension `122`, not the proposed
   `Q^3 direct-sum M_8(Q)` of dimension `67` on an eleven-dimensional carrier.

The finite algebra calculation is not used to prove (1.2); the formula-level orbit argument is
independent and already kills (1.1).  Conversely, the exact `s=6` matrices show that the failure
is not merely an omitted passive direction: the whole central decomposition and commutator-rank
pattern change.

## 2. Uniform standard-multiplicity calculation

Put

\[
 r=s,\qquad a=s^2,\qquad d=4s+1,\qquad m=ad,
 \qquad\theta=(m-r-1,r,1).
\]

Let

\[
 H=S_d^a,\qquad W=H\rtimes S_a,\qquad
 W_0=H\rtimes S_{a-1},
\]

where `S_(a-1)` fixes block zero, and put `U_theta=(S^theta)^H`.  Since

\[
 \operatorname{Ind}_{S_{a-1}}^{S_a}{\bf1}
 \cong {\bf1}\oplus S^{(a-1,1)},
\]

Frobenius reciprocity gives

\[
 C_s=\dim U_\theta^{S_{a-1}}-\dim U_\theta^{S_a}
 =\dim(S^\theta)^{W_0}-\dim(S^\theta)^W.
\tag{2.1}
\]

### 2.1 Jacobi--Trudi reduction

Expanding the three-row Jacobi--Trudi determinant gives the exact character identity

\[
\begin{aligned}
s_{(m-r-1,r,1)}={}&
h_{m-r-1}h_rh_1-h_{m-r-1}h_{r+1}\\
&-h_{m-r}h_{r-1}h_1+h_{m-r+1}h_{r-1}.
\end{aligned}
\tag{2.2}
\]

Each product of complete symmetric functions is the Frobenius characteristic of the
corresponding Young permutation module.  Taking invariants therefore turns (2.2) into an
alternating sum of exact orbit counts.

No capacity or block-count truncation occurs anywhere in the legal family: every small row has
size at most `r+1=s+1<d=4s+1`, and it can meet at most `r+1<s^2=a` blocks.

### 2.2 Full-block orbits

Write `p(k)` for the number of partitions of `k` and
`P_k=sum_(j=0)^k p(j)`.

For `W`, an orbit on a `k`-set is its block-occupancy partition, so there are `p(k)` orbits.  An
orbit on a disjoint ordered pair `(B,C)` with `|B|=k` and `|C|=1` is determined by the number of
`B`-points in the block containing `C`, followed by a partition of the remainder.  Thus there are

\[
 P_k=\sum_{j=0}^k p(j)
\]

such orbits.  Substitution into (2.2) gives

\[
 \dim(S^\theta)^W
 =P_r-p(r+1)-P_{r-1}+p(r-1)
 =p(r)-p(r+1)+p(r-1).
\tag{2.3}
\]

### 2.3 One distinguished block

For `W_0`, an orbit on a `k`-set is specified by the distinguished-block occupancy and a
partition of the remaining occupancy.  Its count is

\[
 D_k=P_k.
\tag{2.4}
\]

For a pair `(B,C)`, split according to whether `C` lies in block zero.

* If `C` lies in block zero, the count is `P_k`.
* Otherwise choose the `B`-occupancy of block zero and of the tail block containing `C`, then a
  partition of what remains.  The count is

  \[
  \sum_{j=0}^k(k-j+1)p(j).
  \]

Hence the three-row permutation-orbit count is

\[
 E_k=\sum_{j=0}^k(k-j+2)p(j).
\tag{2.5}
\]

Using (2.2), (2.4), and (2.5),

\[
\begin{aligned}
\dim(S^\theta)^{W_0}
 &=E_r-D_{r+1}-E_{r-1}+D_{r-1}\\
 &=P_{r-1}+p(r)-p(r+1).
\end{aligned}
\tag{2.6}
\]

Subtracting (2.3) from (2.6) proves

\[
 C_s=P_{r-1}-p(r-1)=P_{r-2}
 =\sum_{k=0}^{s-2}p(k).
\tag{2.7}
\]

In particular the correct recurrence is

\[
 C_{s+1}-C_s=p(s-1).
\tag{2.8}
\]

### 2.4 Why two finite points interpolated incorrectly

The candidate count has the exact combinatorial form

\[
 1+\binom{s-1}{2}=1+\sum_{k=1}^{s-2}k.
\tag{2.9}
\]

There are exactly `k` hook partitions of `k`.  Thus (2.9) counts only hook partitions among the
partition-indexed dimensions counted by (2.7).  Every partition of `k<=3` is a hook, which is why
the reviewed values `C_4=4` and `C_5=7` agree accidentally.  The first missing partition is
`(2,2)` at `k=4`, giving

\[
 C_6=1+1+2+3+5=12
\]

rather than `11`.  This dimension argument does not by itself choose a canonical
partition-labelled basis, but it proves that a pairs/hooks-only basis cannot span the full James
quotient from `s=6` onward.

## 3. Independent exact `s=6` construction

The archived implementation is not a parameter substitution into either frozen reducer.  It
imports neither `ksum/tools/ksum_l3_wreath_occurrence_reducer.py` nor
`ksum/tools/ksum_l3_wreath_occurrence_reducer_s5.py`.  It independently implements:

1. compressed multisets of block occupancies rather than a labelled or length-`a` orbit
   catalogue;
2. every James keep and merge map from orbit-size ratios;
3. the full-to-distinguished orbit embedding;
4. a raw rational, non-Gram--Schmidt gauge for the orthogonal complement of **all** full-block
   invariants (three dimensions at `s=6`, not the one-dimensional `s=4,5` special case);
5. marked refinement and the literal relative sum `J_x=sum_(y!=x)(x y)`;
6. corner projectors applied as degree-two polynomials only on the selected source;
7. eta trace identities, Gram raising, exact centralizers, and exact word-algebra certificates.

As a control, the same new code reproduces the frozen finite classifications:

| `s` | `C_s` | six ranks `(T1,TV,M1,MV,B1,BV)` | different-corner commutator rank | blocks | algebra dimension |
|---:|---:|---|---:|---|---:|
| 4 | 4 | `(4,4,2,4,4,4)` | 2 | `1,3` | 10 |
| 5 | 7 | `(7,7,5,7,6,7)` | 2 | `1,1,5` | 27 |

Those crosschecks agree with the reviewed packages but are produced in the new raw rational gauge.

### 3.1 Source and marked dimensions

At

\[
(s,a,d,r,m)=(6,36,25,6,900),\qquad\theta=(893,6,1),
\]

the exact quotient data are:

| quotient | permutation-orbit dimension | James-stack shape/rank | Specht fixed dimension |
|---|---:|---:|---:|
| full `W` | 30 | `60 x 30`, rank 27 | 3 |
| distinguished `W_0` | 105 | `186 x 105`, rank 90 | 15 |

The exact standard multiplicity is therefore `15-3=12`, in agreement with (2.7).  The marked
orbit quotient has dimension `199`.

The corner contents and Lagrange denominators are

| corner | content | projector denominator |
|---|---:|---:|
| `T` | 892 | 793872 |
| `M` | 4 | -5328 |
| `B` | -2 | 5364 |

The relative JM is exactly self-adjoint in the marked orbit Gram.  Its three projected source
images resolve all twelve columns and are pairwise Gram-orthogonal.

### 3.2 Six exact ranks and commutators

All six archived rational forms are exactly PSD.  Their ranks are

| corner | `eta=1` | `eta=V_35` |
|---|---:|---:|
| `T` | 12 | 12 |
| `M` | 8 | 12 |
| `B` | 10 | 12 |

For the Gram-raised endomorphisms `A=G^(-1)H`:

* the three same-corner/different-eta commutators vanish exactly;
* **every one of the twelve different-corner commutators has rank 6**.

Thus the reviewed `s=4,5` different-corner rank-two pattern also fails at `s=6`.

### 3.3 Central blocks and generated algebra

The exact common-commutant system has `144` unknowns, rank `142`, and nullity `2`.  The commutant
is commutative.  A rational Gram-self-adjoint separator has two distinct rational linear factors
with multiplicities `1` and `11`; therefore both central projectors and both central subspaces are
defined over `Q`.  No non-split field-extension obstruction occurs at this finite target.

The bicommutant has exact rational dimension `122`.  Independently, reduction modulo the good
prime `1000000007` finds `122` linearly independent words in the two natural generators.  Modular
independence is a characteristic-zero lower bound, while containment in the rational bicommutant
is an upper bound, so

\[
 \dim_\mathbb Q\mathcal A_6=122=1^2+11^2.
\]

Because the rational central block ranks are `1` and `11`, attaining the full block-diagonal
maximum proves (1.3).  In particular, at `s=6` there is one rational invariant line, not the three
claimed by (1.1), and the complementary rational block is irreducible for the generated algebra.

## 4. Exact `s=7` source check

A cheap separate James-quotient run checks the next legal member without attempting the expensive
nineteen-dimensional six-operator algebra:

\[
(s,a,d,m,\theta)=(7,49,29,1421,(1413,7,1)).
\]

The full and distinguished permutation-orbit dimensions are `45` and `165`; their exact James
kernel dimensions are `4` and `23`.  Hence

\[
 C_7=23-4=19=\sum_{k=0}^{5}p(k),
\]

whereas the registered candidate gives `16`.  The source Gram has exact rank `19`.  No `s=7`
six-matrix, commutant, or algebra conclusion is claimed.

## 5. Hostile obstruction audit

* **Extra invariant directions:** yes.  The candidate misses non-hook partition directions,
  beginning with `(2,2)` at `s=6`.
* **Claimed trivial-line count:** false at `s=6`.  The actual rational central ranks are `1,11`,
  rather than `1,1,1,8`.
* **Reducibility of the claimed big block:** the claimed eight-dimensional block is not a block
  of the actual twelve-dimensional object.  The actual eleven-dimensional complement is full
  `M_11(Q)` in this finite target.
* **Non-split/field-extension block:** not present at `s=6`; the exact commutant separator splits
  into rational linear factors.
* **Exceptional corner denominators:** none in the legal family.  The three differences are
  `m-2s`, `m-s`, and `s`, all nonzero for `m=s^2(4s+1)` and `s>=4`.
* **James quotient dimension formula:** the two-point quadratic guess fails.  The exact uniform
  quotient formula is the partition-prefix sum (2.7).
* **Finite-to-uniform guard:** (2.7) is proved uniformly by character/orbit identities.  The
  algebra classification (1.3) is asserted only at `s=6`; no algebra sequence is inferred from
  `s=4,5,6`.

## 6. Reproduction

Exact `s=4`, `s=5`, and `s=6` runs:

```powershell
python ksum/artifacts/ksum_L3_uniform_occurrence_algebra_s6_falsifier_20260722.py `
  --s 6 `
  --json ksum/artifacts/logs_ksum_L3_uniform_occurrence_algebra_s6_falsifier_20260722/s6_exact.json `
  --log ksum/artifacts/logs_ksum_L3_uniform_occurrence_algebra_s6_falsifier_20260722/s6_exact.log
```

Replace `--s 6` and the two output basenames by `s4_crosscheck` or `s5_crosscheck` for the frozen
finite controls.

Exact `s=7` source-only check:

```powershell
python ksum/artifacts/ksum_L3_uniform_occurrence_algebra_s7_source_check_20260722.py `
  --json ksum/artifacts/logs_ksum_L3_uniform_occurrence_algebra_s6_falsifier_20260722/s7_source_exact.json `
  --log ksum/artifacts/logs_ksum_L3_uniform_occurrence_algebra_s6_falsifier_20260722/s7_source_exact.log
```

The `s=6` log begins `ALL_EXACT_S6_FALSIFIER_GATES_PASS`; the `s=7` log begins
`ALL_EXACT_S7_SOURCE_GATES_PASS`.  The JSON contains the complete six rational forms, Gram,
James-map ranks, PSD certificates, all fifteen commutator ranks, commutant/bicommutant ranks,
rational separator factorization, and the modular word certificate.

## 7. Immutable evidence hashes

The companion manifest
`ksum/artifacts/ksum_L3_uniform_occurrence_algebra_candidate_falsifier_20260722.sha256`
contains the SHA-256 of every script and output listed below and is verified separately after the
report is frozen.

## 8. Stopping point

The registered joint candidate has an exact formula-level counterexample and a stronger exact
finite algebra counterexample.  The strongest replacement theorem established here is only the
uniform multiplicity formula (2.7).  No replacement all-`s` formula for the central blocks or
generated occurrence algebra is proved.  The sequence

\[
M_1\oplus M_3,\quad
M_1\oplus M_1\oplus M_5,\quad
M_1\oplus M_{11}
\]

is explicitly not interpolated.  Completion-tier DAG action requires a fresh independent Rule-7
review of this artifact and its exact outputs.

