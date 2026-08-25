# KSUM.B4b Front L — optimal-certificate structure reconnaissance

Date: 2026-07-19  
Status: **NUMERICAL structure evidence; pending-review.**  
Scope: cyclic 2-Sum only. This report makes **no exponent claim from finite instances** (G11).

## Executive verdict

The extracted HLS-dual optimizers are substantially richer than the paper's concrete Belovs--Spalek
(BS) \(\Gamma_L\). Along fixed \(q=3\), one repetition-one Wedderburn sector becomes increasingly
dominant in Frobenius mass (85.27%, 91.66%, 96.57%, 97.88% at \(N=3,4,6,7\)), while its trace
share falls (63.34%, 60.59%, 42.80%, 35.82%): the optimizer has a near-rank-one spine plus a growing
set of diffuse satellite sectors. The natural HLS block is almost entrywise nonnegative; the
negative Frobenius share never exceeds \(3.31\times10^{-5}\) on this grid. Thus the useful
"negative-adversary" structure is not a large negative-entry pattern in this dual Gram
representation.

At \(N=5,q=4\), changing \(t=0\) (\(\tau=2\)) to \(t=1\) (\(\tau=0\)) changes the
commutant from 19 to 23 sectors. The fixed-point-free optimizer is less concentrated in the leading
sector (85.33% versus 93.35% of Frobenius mass) and moves 22.33% of trace into a repetition-two
sector. This is a real symmetry-type change, not a target relabeling.

For the lower-bound chain, BHK preserves the adversary multiplicatively up to a constant and
pSearch itself is tight at \(\Theta(\sqrt m)\); Zhang's ordinary \(q\)-by-\(q\) claw base is
tight at \(\Theta(q^{2/3})\). ABI's disjoint-bucket assembly therefore forces
\[
q^{2/3}\sqrt{N/q}=\sqrt N\,q^{1/6}.
\]
A \(q^{1/4}\) lower-bound chain must change the assembly/outer promise, not sharpen either cited
component theorem in place.

## 1. Reproducibility and numerical scope

New extractor: [ksum/tools/ksum_expL_dual_extract.py](../tools/ksum_expL_dual_extract.py), SHA-256
\(8873e72d24927fbeca8cfec6a7cd46c3137cbecd9e3de78dd6939d499c712321\). It imports the reviewed
L33 solver unchanged (SHA-256
\(940de0ceb9472aa5fa47e33b7fd0bfb604fbb020e4245aec3c6ff2d1e0d76111\)), rebuilds the same SDP,
and saves every optimized multiplicity block plus the reconstructed natural stabilizer block
\(A=M_0\) in compressed NPZ form.

MOSEK was installed, so all six runs used it with primal feasibility, dual feasibility, and relative
gap tolerances set to \(10^{-9}\). The exact commands are in
[COMMANDS.txt](logs_ksum_expL_20260719/COMMANDS.txt); all artifact and script hashes are in
[SHA256SUMS.txt](logs_ksum_expL_20260719/SHA256SUMS.txt), whose SHA-256 is
\(4937d8c11abc4ab9865f46fedea880a5cde9fee2c40d6124d51ad9b1b33ac1c1\).

| Case (raw log) | Adv± | max equality residual | max diagonal violation | log SHA-256 |
|---|---:|---:|---:|---|
| [(3,3,0)](logs_ksum_expL_20260719/n3_q3_t0.log) | 2.418246386 | \(9.84\times10^{-10}\) | \(-5.29\times10^{-10}\) | \(1fbbd7e2d8e84fb4bb4bd8679f579986e88db092f2a901e25b2670484485bbb8\) |
| [(4,3,0)](logs_ksum_expL_20260719/n4_q3_t0.log) | 2.712159296 | \(9.25\times10^{-10}\) | \(-1.61\times10^{-10}\) | \(d51ba184cc6124bdd4a3ed708dcdaa0e0c7cbfec6e28a8f1ed5866589aa553bf\) |
| [(5,4,0)](logs_ksum_expL_20260719/n5_q4_t0.log) | 3.334236658 | \(7.49\times10^{-11}\) | \(-1.82\times10^{-11}\) | \(952100f64ec7e0ac493d7e601a1983abd9ac6be15857b0faf736efd4d464eab3\) |
| [(5,4,1)](logs_ksum_expL_20260719/n5_q4_t1.log) | 3.312519646 | \(3.83\times10^{-10}\) | \(-3.91\times10^{-10}\) | \(ae519759a9cef0fefe2dee38d21cdbc28667a0737fc1327cd30181efd2971fe0\) |
| [(6,3,0)](logs_ksum_expL_20260719/n6_q3_t0.log) | 3.349771964 | \(7.08\times10^{-10}\) | \(-2.93\times10^{-10}\) | \(a63a39e3fa3960bb24762ac48006ca0815c109b6b670693bf2deb2164eb0b6b4\) |
| [(7,3,0)](logs_ksum_expL_20260719/n7_q3_t0.log) | 3.631736495 | \(4.98\times10^{-10}\) | \(-5.41\times10^{-10}\) | \(b1567cdfdb1881c6b6d5871bef13b911d5c5667107f1434b59e182a773fdda01\) |

These are numerical approximations, not exact algebraic values. The tightened \((5,4,0)\) value is
\(3.13\times10^{-6}\) below the earlier default-MOSEK reviewed decimal; its reconstructed matrix
passes the stronger residual audit above. No inference below depends on those last digits.

## 2. Wedderburn-block profile

Here \(m\) is multiplicity-block dimension, \(d\) is the number of aligned copies (irrep
dimension in the reviewed construction), rank uses eigenvalue threshold \(10^{-8}\), and
\(r_{\rm eff}=\operatorname{tr}(B)^2/\lVert B\rVert_F^2\). The MOSEK interior point leaves
many tiny positive eigenvalues, so threshold rank is descriptive; effective rank and top-eigenvalue
share are the stable concentration diagnostics.

| Case | sectors | rank(A)/dim | leading (m,d) | leading trace | leading Frobenius | eff. rank | top eig./trace |
|---|---:|---:|---:|---:|---:|---:|---:|
| [(3,3,0)](logs_ksum_expL_20260719/n3_q3_t0.json) | 4 | 12/27 | (10,1) | 63.34% | 85.27% | 1.13 | 93.82% |
| [(4,3,0)](logs_ksum_expL_20260719/n4_q3_t0.json) | 6 | 61/81 | (16,1) | 60.59% | 91.66% | 1.14 | 93.68% |
| [(6,3,0)](logs_ksum_expL_20260719/n6_q3_t0.json) | 10 | 691/729 | (33,1) | 42.80% | 96.57% | 1.20 | 91.15% |
| [(7,3,0)](logs_ksum_expL_20260719/n7_q3_t0.json) | 14 | 2133/2187 | (44,1) | 35.82% | 97.88% | 1.17 | 92.33% |
| [(5,4,0), τ=2](logs_ksum_expL_20260719/n5_q4_t0.json) | 19 | 839/1024 | (44,1) | 41.06% | 93.35% | 1.18 | 92.19% |
| [(5,4,1), τ=0](logs_ksum_expL_20260719/n5_q4_t1.json) | 23 | 890/1024 | (22,1) | 39.98% | 85.33% | 1.07 | 96.57% |

The complete per-block spectra (top eight eigenvalues, two ranks, trace/Frobenius shares, and
minimum eigenvalue) are in each linked JSON and the matrices themselves are in the same-name NPZ.

### Movement at fixed q=3

- The leading repetition-one sector remains near rank one in meaningful mass, but its trace share
  drops by 27.52 percentage points from \(N=3\) to \(N=7\). Satellite sectors therefore carry
  more trace even as the leading sector carries almost all Frobenius mass.
- Every computed sector is active above \(10^{-8}\). A scalar Hamming-shell description is too
  small even at these sizes.
- The fraction of input diagonal constraints active within \(10^{-7}\) drops
  96.30% → 37.04% → 7.68% → 3.20%. The optimizer increasingly selects a thin set of histogram
  types rather than saturating diagonals uniformly.

### Tau comparison at (5,4)

For \(t=0,\tau=2\), the next three trace sectors after the leader are repetition-three sectors
with 14.26%, 12.99%, and 7.55% trace. For \(t=1,\tau=0\), a repetition-two sector alone carries
22.33% trace and 12.17% Frobenius mass. The fixed-point-free case also activates 23 rather than 19
sectors and has 44.92% rather than 22.66% active input diagonals. Any uniform ansatz must therefore
parameterize \(C(\sigma)\)'s cycle type, not just \(N,q\).

## 3. Orbits, orbitals, and signs

The extractor groups diagonal entries by \(H=S_{N-1}\times C(\sigma)\) input orbits and all
matrix entries by symmetric \(H\)-orbitals. Signatures record the distinguished-coordinate pair
and the joint histogram on the other coordinates.

At fixed \(q=3\), the top diagonal-orbit trace share falls 21.90% → 17.40% → 9.36% → 6.88%.
Its representatives move from small extreme histograms to interior histograms: at \(N=6\) the top
representative is \(x_0=0\), remaining counts \([2,2,1]\); at \(N=7\) it is \(x_0=0\),
counts \([1,3,2]\). At \((5,4,0)\) the top orbit is \(x_0=0,[1,2,1,0]\) (11.26% trace),
whereas at \((5,4,1)\) it is \(x_0=0,[0,2,2,0]\) (13.27%).

For every case except the smallest anchor, all of the six largest individual orbitals are YES--YES.
The whole natural-matrix Frobenius split is:

| Case | NO--NO | one cross block | YES--YES | negative Frobenius share |
|---|---:|---:|---:|---:|
| [(3,3,0)](logs_ksum_expL_20260719/n3_q3_t0.json) | 8.73% | 20.42% | 50.42% | 0 |
| [(4,3,0)](logs_ksum_expL_20260719/n4_q3_t0.json) | 1.88% | 11.67% | 74.78% | \(3.30\times10^{-5}\) |
| [(6,3,0)](logs_ksum_expL_20260719/n6_q3_t0.json) | 0.090% | 2.84% | 94.22% | \(4.39\times10^{-7}\) |
| [(7,3,0)](logs_ksum_expL_20260719/n7_q3_t0.json) | 0.017% | 1.27% | 97.44% | \(3.02\times10^{-7}\) |
| [(5,4,0)](logs_ksum_expL_20260719/n5_q4_t0.json) | 0.573% | 6.92% | 85.58% | 0 |
| [(5,4,1)](logs_ksum_expL_20260719/n5_q4_t1.json) | 1.71% | 11.26% | 75.76% | 0 |

"One cross block" is NO--YES; symmetry gives the same share for YES--NO. The YES--YES dominance is
partly a PSD-completion effect and partly population imbalance. It is structure to model, not an
asymptotic conclusion.

## 4. Comparison with the BS certificate

For each case the extractor faithfully rebuilds the paper's concrete \(\Gamma_L\) using
[ksum_stage0_c_main.py](../tools/ksum_stage0_c_main.py), recomputes
\(\lVert\Gamma_L\rVert/\max_i\lVert\Gamma_L\circ\Delta_i\rVert\), and decomposes the
normalized column Gram \(\Gamma_L^*\Gamma_L\) in the *same* deterministic Wedderburn basis as
\(A\). The Gram reconstructs with relative error at most \(1.46\times10^{-13}\).
This is an exact finite-instance comparison of symmetry-sector support, but it is not an assertion
that a primal adversary matrix and an HLS-dual Gram are the same optimization variable.

| Case | BS certified | fraction of optimum | sector trace TV distance |
|---|---:|---:|---:|
| [(3,3,0)](logs_ksum_expL_20260719/n3_q3_t0.json) | 1.446858 | 59.83% | 0.142 |
| [(4,3,0)](logs_ksum_expL_20260719/n4_q3_t0.json) | 1.551514 | 57.21% | 0.290 |
| [(6,3,0)](logs_ksum_expL_20260719/n6_q3_t0.json) | 1.925769 | 57.49% | 0.417 |
| [(7,3,0)](logs_ksum_expL_20260719/n7_q3_t0.json) | 2.100933 | 57.85% | 0.506 |
| [(5,4,0)](logs_ksum_expL_20260719/n5_q4_t0.json) | 1.689705 | 50.68% | 0.354 |
| [(5,4,1)](logs_ksum_expL_20260719/n5_q4_t1.json) | 1.691757 | 51.07% | 0.478 |

Where is the missing weight?

1. **A dominant sector with the wrong internal direction.** At \((4,3,0)\), the true leading
   sector has 60.59% of trace versus 32.13% for the BS column Gram, and their within-block
   Frobenius cosine is only 0.0886. At \((7,3,0)\), the corresponding figures are 35.82% versus
   18.94%, cosine 0.00864.
2. **Satellite sectors absent from the concrete BS Gram.** At \((4,3,0)\), two true sectors carry
   0.5837% trace while their BS norms are below \(5\times10^{-29}\). A top absent sector carries
   6.28% trace at \((6,3,0)\), and a top absent sector carries 8.16% at \((7,3,0)\).
3. **Fine joint-histogram orbitals and PSD completion.** The true dual uses many distinct
   \(C(\sigma)\)-joint-histogram orbitals and large YES--YES completion mass. The paper ansatz
   assigns one scalar \(\alpha_m\) per Hamming shell before legality restriction; it cannot tune
   these orbitals or the tau-dependent satellite redistribution independently.

The TV distance grows monotonically on the computed \(q=3\) sequence, but G11 forbids reading an
exponent from four points.

## 5. Where the 1/6 chain loses

On-disk dependencies: [ABI package](../ksum/literature/ambainis-balodis-iraids-2021-small-range-claw/README.md),
[ABI lower DAG](../ksum/literature/ambainis-balodis-iraids-2021-small-range-claw/proof-dag/lower-root.md),
[Zhang page](../ksum/literature/zhang-2005-promised-distributed-search/README.md),
[BHK page](../ksum/literature/brassard-et-al-2019-merkle-psearch/README.md), and ABI's
[local source lines 289--330](references/abi_2103.16390_src/claw.tex).

| Link | Precisely preserved | Exponent contribution | What a 1/4-strength link would require |
|---|---|---|---|
| Zhang base | Bounded-error query complexity of ordinary two-list \(\mathrm{Claw}_{q,q}\) | \(\Theta(q^{2/3})\) | With the same bucket packing, an outer lower bound \(q^{3/4}\). This cannot be ordinary claw: Zhang's theorem is tight, including an upper bound. |
| BHK pSearch composition | \(\mathrm{Adv}^{\pm}(F\circ\mathrm{pSearch}_m)\ge(2/\pi)\mathrm{Adv}^{\pm}(F)\mathrm{Adv}^{\pm}(\mathrm{pSearch}_m)\) | \(\Theta(\sqrt m)\); only a constant \(2/\pi\) is lost | With Zhang unchanged, an extra \(q^{1/12}\) beyond \(\sqrt m\). Independent pSearch cannot supply it because its own query complexity is \(\Theta(\sqrt m)\). |
| ABI assembly | A query-free encoding of \(\mathrm{Claw}_{q,q}\circ\mathrm{pSearch}_{\lfloor N/q\rfloor}\) into small-range claw, using two distinct padding values and range \(q+2\) | Sets \(m=\lfloor N/q\rfloor\), hence exactly \(\sqrt N q^{1/6}\) | Replace the disjoint independent buckets/ordinary outer claw by a correlated or stronger promised outer object that still embeds with \(O(1)\) query overhead, range \(O(q)\), and no spurious claws. |

**Verdict:** algebraically the \(q^{1/6}\) comes from Zhang's \(2/3\) minus the \(1/2\)
cost of splitting \(N\) positions into \(q\) pSearch buckets. There is no theorem-proof slack at
(a) or (b): both factors are tight for the exact component functions. The actionable loss is (c),
ABI's assembly architecture. A successful replacement must preserve query simulation and the
\(O(q)\) output alphabet while producing a genuinely global extra \(q^{1/12}\); merely
strengthening the BHK constant or re-proving Zhang cannot change the exponent.

## 6. Ranked candidate lower-bound routes

| Rank | Route | Concrete first lemma | L33 evidence | Kill criterion | Difficulty |
|---:|---|---|---|---|---|
| 1 | Symmetry-resolved direct negative-adversary family | Derive a closed-form family in the \(S_{N-1}\times C(\sigma)\) Wedderburn algebra with one near-rank-one repetition-one spine plus tau-indexed satellite PSD blocks, and prove the adversary constraints/norm ratio symbolically. | Consistent: stable leading-spine shape, every sector active, growing BS sector mismatch. Not evidence for an exponent. | Kill if the sector labels cannot be aligned across consecutive \(N\), or a fitted family fails feasibility/PSD or loses a constant fraction of optimum on the first held-out \((N,q,t)\). | Very high, but most directly informed by L33. |
| 2 | Multisymmetric joint-histogram dual polynomial | Build a moment functional on the distinguished pair plus joint \(C(\sigma)\)-histogram variables; first prove pure high degree and correlation for a finite-band kernel that distinguishes complementary-pair occupancy rather than Hamming weight alone. | Consistent: dominant orbitals are fine joint histograms; tau changes sector content; scalar Hamming shells are insufficient. | Kill if symmetrization collapses the candidate to the BS Hamming-shell algebra, or exact moment checks fail already at the six certificate points/next held-out point. | Very high; may expose a smaller analytic state space than route 1. |
| 3 | Correlated composition replacing ABI's disjoint pSearch assembly | Define a promised outer/range-coupled gadget and prove a query-free embedding into \(N\)-by-\(N\), range-\(O(q)\) claw together with \(\mathrm{Adv}^{\pm}\ge\Omega(\sqrt N q^{1/4})\). The first sublemma is exact completeness/soundness with no padding-induced false claw. | Weakly consistent: true optimizers use sectors and joint orbitals missing from the independent-shell BS profile. L33 does not test composition. | Kill if the gadget factors back into independent pSearch (then the tight \(1/6\) cap returns), needs superconstant query simulation, increases range beyond \(O(q)\), or admits a small-range upper algorithm below the target. | Extreme; current chain analysis says a genuinely new assembly is mandatory. |

These are candidates only. Their canonical DAG nodes remain OPEN and pending independent review.

## 7. Limitations / what was not checked

- Optimizer uniqueness was not proved. MOSEK returns a high-accuracy interior-point representative
  of the optimal face; tiny eigenvalues and threshold ranks can move within that face.
- No exact rational/algebraic certificate or interval enclosure was produced.
- No primal optimal adversary matrix was recovered from KKT dual multipliers. The BS comparison is
  the concrete \(\Gamma_L^*\Gamma_L\) sector diagnostic described above.
- No instances beyond the six commissioned points, no \(k\ge3\), no non-cyclic groups, and no
  held-out prediction test were run.
- The BHK primary paper is represented on disk by the verified literature page; no local primary
  source file was present. Zhang's result was read from its verified page, while ABI's composition
  arithmetic was checked against the local primary LaTeX.
- No network was used, no git commit was made, and no completion-tier status was assigned.
