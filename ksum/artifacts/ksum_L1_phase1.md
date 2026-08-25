# KSUM.B4b.L1 phase 1 — three-class polar-completion ansatz

Date: 2026-07-19  
Status: **P2 KILL RECORDED; OPEN and pending independent review under DAG rule 6.**  
Scope: cyclic 2-Sum HLS dual only. All fits below are finite-instance structure evidence, never exponent proofs (G11).

## Decision

The tested closed-form family is exactly feasible and positive semidefinite, but it does not model the
true optimum closely. Even after giving each known point its own globally optimized balance weights
(an oracle-best fit strictly more permissive than one shared smooth profile), capture is at most
62.83% and is below 60% at five of six points. It decreases to 38.90% along the q=3 sequence.

This meets the commissioned P2 kill criterion. P3 and P4 were not entered: no held-out values were
pre-registered, neither held-out L33 solve was run, and no next-lemma claim was registered.

## 1. Explicit family

Let X=(Z_q)^N, let f be cyclic 2-Sum with target t, and split X into
Y=f^{-1}(1) and Z=f^{-1}(0). Let d(x,x') be Hamming distance. Define the fixed YES--NO orbit kernel

[
C_{yz}=rac{1}{d(y,z)},qquad yin Y, zin Z.
]

The denominator never vanishes on Y times Z. It is an explicit orbit coefficient: it depends only
on the S_N-invariant joint histogram, and it is also invariant under the alphabet centralizer
C(sigma), sigma(a)=t-a.

Take a singular decomposition grouped by exact equal-singular-value clusters,

[
C=sum_{alpha} C_alpha,qquad
C_alpha=U_alphaSigma_alpha V_alpha^{mathsf T}.
]

The three fixed classes, independent of N and q, are

[
egin{aligned}
mathcal I_{
m sp}&={	ext{largest singular cluster}},\
mathcal I_{2}&={alpha: 	au=0, operatorname{rank}C_alpha=2},\
mathcal I_{
m sat}&={	ext{all remaining clusters}}.
end{aligned}
]

The numerical implementation uses relative cluster tolerance 10^{-8}. On every tested point the
largest cluster is simple, hence it is a literal rank-one spine. For c in
{sp,2,sat}, put

[
C_c=sum_{alphainmathcal I_c}C_alpha,quad
R_c=sum_{alphainmathcal I_c}U_alphaSigma_alpha U_alpha^{mathsf T},quad
S_c=sum_{alphainmathcal I_c}V_alphaSigma_alpha V_alpha^{mathsf T}.
]

Thus the individual same-label orbit coefficients are explicitly

[
(R_c)_{yy'}=sum_{alphainmathcal I_c}sum_j
 sigma_{alpha j}u_{alpha j}(y)u_{alpha j}(y'),qquad
(S_c)_{zz'}=sum_{alphainmathcal I_c}sum_j
 sigma_{alpha j}v_{alpha j}(z)v_{alpha j}(z').
]

For theta=(theta_sp,theta_2,theta_sat) in R_{>0}^3, omit the empty tau0 class and define

[
Gamma(N,q,t;	heta)=
egin{pmatrix}
 sum_c	heta_cR_c & C\
 C^{mathsf T} & sum_c	heta_c^{-1}S_c
end{pmatrix}_{Ysqcup Z}.
	ag{1}
]

This is a three-parameter family (two active parameters when tau is nonzero).

### Exact PSD and commutant membership

For each class,

[
egin{pmatrix}	heta_cR_c&C_c\C_c^{mathsf T}&	heta_c^{-1}S_cend{pmatrix}
=
egin{pmatrix}sqrt{	heta_c}U_c\	heta_c^{-1/2}V_cend{pmatrix}
Sigma_c
egin{pmatrix}sqrt{	heta_c}U_c\	heta_c^{-1/2}V_cend{pmatrix}^{mathsf T}
succeq0.
]

Summing gives (1), so Gamma is PSD for every positive theta. Because C intertwines the
S_N times C(sigma) actions on Y and Z, its singular spectral projectors and their matrix square
roots commute with those actions. Hence Gamma lies in that commutant.

### Exact HLS equalities and objective

Let s_i swap coordinates 0 and i. Position permutations preserve labels and Hamming distance.
For every y in Y and z in Z,

[
sum_{i:y_i
e z_i}Gamma_{s_i y,s_i z}
=sum_{i:y_i
e z_i}rac1{d(y,z)}=1.
]

The implementation reports zero floating residual for these identities because it evaluates
d times (1/d) directly. Full S_N invariance also makes every transported diagonal equal, so the
dual objective bound is

[
T(	heta)=Nmaxleft{
 max_{yin Y}sum_c	heta_c(R_c)_{yy},
 max_{zin Z}sum_c	heta_c^{-1}(S_c)_{zz}

ight}.
	ag{2}
]

Thus Gamma is an exactly defined feasible HLS-dual certificate and Adv^{+-}(f) <= T(theta).
The reported capture ratio is the reviewed numerical optimum divided by T(theta), so 1 is exact
capture and smaller is worse. This dual tightness diagnostic is not itself an adversary lower-bound
proof.

## 2. P2 known-point fits

For each point, theta was optimized independently by the globally convex exponential-cone program
obtained from (2), using CLARABEL. This is deliberately an oracle-best upper envelope for the family:
a single smooth theta(N,q,tau) profile cannot improve any row.

| (N,q,t) | tau | theta_sp | theta_2 | theta_sat | family T | true L33 optimum | capture optimum/T |
|---|---:|---:|---:|---:|---:|---:|---:|
| (3,3,0) | 1 | 1.504781 | — | 1.494081 | 3.848659 | 2.418246 | 62.83% |
| (4,3,0) | 1 | 2.287484 | — | 2.018436 | 5.141333 | 2.712159 | 52.75% |
| (6,3,0) | 1 | 4.802923 | — | 3.098859 | 7.888590 | 3.349772 | 42.46% |
| (7,3,0) | 1 | 7.019188 | — | 3.806230 | 9.337179 | 3.631736 | 38.90% |
| (5,4,0) | 2 | 3.444603 | — | 2.298259 | 7.758314 | 3.334237 | 42.98% |
| (5,4,1) | 0 | 2.558367 | 1.608713 | 1.921773 | 7.225891 | 3.312520 | 45.84% |

The tau=0 repetition-two class is genuinely used: it has aggregate cross-kernel rank 8 at (5,4,1),
coming from four multiplicity-two singular clusters. Nevertheless, separating it does not rescue
capture. The q=3 degradation is monotone on the four known points. Five rows are no better than the
approximately 60% BS scale named in the stop rule, and all six miss the >90% target badly.

The convex solver returned optimal on five rows and optimal_inaccurate on (5,4,1); the evaluated
feasible objective differs from the solver objective there by 1.02e-11, immaterial to the 45.84%
capture conclusion. Raw fits and all theta values are in known_fits.json and known_fits.log.

## 3. Kill diagnosis

The failed assumption is not PSD, feasibility, or the existence of a simple leading singular
direction. Those properties hold exactly. The failure is the **satellite compression**:

1. fixing the entire YES--NO block to the reciprocal-Hamming orbit kernel C_{yz}=1/d(y,z) removes
   the fine joint-histogram freedom seen in the extracted optimizer;
2. balancing only spine, tau=0 repetition-two, and pooled residual satellites cannot tune the many
   same-label PSD-completion orbitals independently;
3. the rapidly falling q=3 capture shows that a cross-N alignment by singular multiplicity is not
   the sector alignment required by the optimizer.

Accordingly this particular three-class closed-form family is stopped at P2. A redesign would need
multiple explicit cross-label joint-histogram kernels (or an equivalent finer sector label), not
merely more balance weights on the same reciprocal-Hamming C.

This is a kill of the tested family, not an independently reviewed refutation of the broad L1 route.
DAG rule 6 therefore leaves KSUM.B4b.L1 at OPEN with pending-review.

## 4. P3/P4 gate record

The gate file predictions.txt records P3_NOT_ENTERED, predictions=NONE, and
held_out_l33_solves=NOT_RUN. In particular, this pass did not solve (4,4,0) or (4,5,0). Because P2
failed, no all-(N,q) feasibility/value lemma or exponent-shaped proof plan was registered.

## 5. Reproducibility

Driver: ksum/tools/ksum_l1p1_polar_family.py.  
Raw log: ksum/artifacts/logs_ksum_L1p1_20260719/known_fits.log.  
Machine-readable fits: ksum/artifacts/logs_ksum_L1p1_20260719/known_fits.json.  
Gate record: ksum/artifacts/logs_ksum_L1p1_20260719/predictions.txt.  
Commands and hashes: ksum/artifacts/logs_ksum_L1p1_20260719/COMMANDS.txt and SHA256SUMS.txt.

## 6. Limitations

- The L33 values are high-accuracy numerical optima, not exact algebraic decimals.
- Singular-value class identification is numerical at tolerance 10^{-8}; exact representation
  labels were not derived.
- No optimizer uniqueness, rational certificate, or asymptotic norm bound was proved.
- This HLS-dual feasible family gives upper bounds on Adv^{+-}; it is a structure/tightness test, not
  by itself a lower-bound witness.
- No held-out solve, k>=3 instance, non-cyclic group, or exponent fit was performed.
- No independent review was performed in this pass.
