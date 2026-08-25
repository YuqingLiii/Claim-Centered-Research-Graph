# Blind independent review of the frames-1 claims

Role: fresh independent reviewer under DAG_PROTOCOL rules 6 and 7  
Date: 2026-07-19  
Required comparison files: se/artifacts/se_frames1_20260719.md and se/artifacts/se_frames1_review_20260719.md

## Part A — frozen blind derivation

**Freeze declaration.** Everything in Part A was written and frozen at **2026-07-19 19:00:18 -04:00**, before I opened either required comparison file. I had received only the setting and four claims inline. I did not inspect either comparison file, nor their associated proposer/prior-review log directories, while deriving or testing Part A. Part B is appended only after this freeze.

### A1. Definitions, quantifiers, and complete type audit

Write \(U=A\sqcup B\), \(A^\circ=A\setminus\{1\}\), and

\[
d_\lambda=f^\lambda,\qquad
d_\xi=f^\kappa f^\nu c,
\qquad \mathcal C=P_\xi V_\lambda.
\]

All claims are quantified over exactly the admissible strict sectors defined in the supplied setting: \(q=2n\), \(j\ge1\), \(a+b=j\), the displayed shapes are partitions, the three stated stability inequalities hold, and \(c=c_{\alpha\beta}^{\theta}>0\). Thus “strict” and “admissible” are resolved locally.

The ambient \(V_\lambda\) has dimension \(d_\lambda\). The map

\[
P_\xi:V_\lambda\longrightarrow V_\lambda
\]

is the orthogonal central-isotypic projector for \(H=S_{A^\circ}\times S_B\), has rank \(d_\xi\), and has image

\[
\mathcal C\cong(V_\kappa\boxtimes V_\nu)\otimes\mathbb C^c
\]

with factor dimensions \(f^\kappa,f^\nu,c\); \(H\) acts trivially on \(\mathbb C^c\).

For \(D\subseteq U\), \(m=q-|D|\),

\[
\Pi_D=\frac1{m!}\sum_{g\in K_D}\rho_\lambda(g):
V_\lambda\longrightarrow V_\lambda
\]

is an orthogonal projector with image \(V_\lambda^{K_D}\) and rank

\[
\dim V_\lambda^{S_m}=f^{\lambda/(m)},
\]

the number of standard tableaux of the skew shape after removing the one-row partition \((m)\), interpreted as zero when \((m)\not\subseteq\lambda\). Thus its rank is \(f^\theta\) when \(|D|=j\), and \(f^{\lambda/(q-j-1)}\) when \(|D|=j+1\).

Consequently \(\Pi_DP_\xi\) and \(P_\xi\Pi_DP_\xi\) are endomorphisms of \(V_\lambda\). The former has effective domain \(\mathcal C\), dimension \(d_\xi\), and range in \(V_\lambda^{K_D}\); the latter has effective domain and codomain \(\mathcal C\), so is \(d_\xi\times d_\xi\). Every sum in Claims 2–4 is in \(\operatorname{End}(V_\lambda)\); each compressed sum is equivalently in \(\operatorname{End}(\mathcal C)\), again \(d_\xi\times d_\xi\). All dimensions retain the LR factor \(c\).

### A2. Independent proof of Claim 1

Let \(I=D\cap A^\circ\), \(J=D\cap B\), \(r=|I|\), \(s=|J|\). The subgroup

\[
L_D=S_{A^\circ\setminus I}\times S_{B\setminus J}
\cong S_{n-1-r}\times S_{n-s}
\]

lies in \(K_D\), whether or not \(1\in D\). Its averaging projector \(Q_D:V_\lambda\to V_\lambda\) restricts, on the typed carrier decomposition, as

\[
Q_D|_{\mathcal C}
=Q_{\kappa,r}\otimes Q_{\nu,s}\otimes I_c:
(V_\kappa\boxtimes V_\nu)\otimes\mathbb C^c
\longrightarrow
(V_\kappa\boxtimes V_\nu)\otimes\mathbb C^c.
\]

Here \(Q_{\kappa,r}:V_\kappa\to V_\kappa\) projects onto \(S_{n-1-r}\)-fixed vectors and has rank \(f^{\kappa/(n-1-r)}\); \(Q_{\nu,s}:V_\nu\to V_\nu\) projects onto \(S_{n-s}\)-fixed vectors and has rank \(f^{\nu/(n-s)}\); \(I_c:\mathbb C^c\to\mathbb C^c\) has rank \(c\). Hence the tensor map has rank

\[
f^{\kappa/(n-1-r)}f^{\nu/(n-s)}c.
\]

This explicitly audits the multiplicity space: no \(f^\theta\)-dimensional frame is being identified with a \(c\)-dimensional space.

Since \(\kappa_1=n-1-a\), if \(r<a\) then \(n-1-r>\kappa_1\); the row \((n-1-r)\) is not contained in \(\kappa\), so \(f^{\kappa/(n-1-r)}=0\). Similarly, \(\nu_1=n-b\), and \(s<b\) implies \(n-s>\nu_1\), so \(f^{\nu/(n-s)}=0\). Either wrong-color inequality therefore gives

\[
Q_DP_\xi=0:V_\lambda\to V_\lambda.
\]

For subgroup averages \(L_D\le K_D\) implies \(\Pi_DQ_D=\Pi_D\), because right multiplication by \(L_D\) permutes the \(K_D\)-summands. Thus

\[
\Pi_DP_\xi=\Pi_DQ_DP_\xi=0:V_\lambda\to V_\lambda,
\]

and left multiplication by \(P_\xi\) gives \(P_\xi\Pi_DP_\xi=0\). The proof is independent of \(|D|\), hence covers the stated sizes \(j,j+1\), on every one of the \(c\) LR directions.

**Verdict on Claim 1: CONFIRMED.** The analytic statement is proved for arbitrary \(c>0\).

### A3. Independent proof of Claim 2

For a \(j\)-subset \(D\subseteq U\), put \(t=\mathbf1_{\{1\in D\}}\). Then

\[
r+s+t=j=a+b.
\]

After compression, Claim 1 kills every term with \(r<a\) or \(s<b\). If \(t=1\), simultaneous survival would give \(r+s\ge a+b=j\), contradicting \(r+s=j-1\). If \(t=0\), it gives \(r+s\ge j\) while \(r+s=j\), so \(r=a,s=b\). The only surviving compressed summands are therefore \(D=I\sqcup J\) with \(I\subseteq A^\circ, |I|=a\) and \(J\subseteq B, |J|=b\). Deleting the zero terms proves Claim 2 in \(\operatorname{End}(V_\lambda)\), equivalently on the \(d_\xi\)-dimensional carrier.

The colored sum is substituted for the central sum only after both carrier compressions are present and the discarded terms have been proved zero.

**Verdict on Claim 2: CONFIRMED.** It inherits Claim 1’s all-\(c\) proof.

### A4. Independent proof of Claim 3

Here \(D\subseteq U\setminus\{1\}\), \(|D|=j\), so \(r+s=j=a+b\), while \(|D\cup\{1\}|=j+1\). Claim 1 kills the compression of \(\Pi_{D\cup\{1\}}\) unless \(r\ge a,s\ge b\). Equality of the sums forces \(r=a,s=b\). Hence precisely the stated \(I\sqcup J\) terms survive, proving the identity in \(\operatorname{End}(V_\lambda)\), equivalently in the \(d_\xi\times d_\xi\) carrier block.

**Verdict on Claim 3: CONFIRMED.** It also holds uniformly in \(c\).

### A5. Independent proof of Claim 4

Set

\[
F_j=\sum_{\substack{D\subseteq U\\|D|=j}}\Pi_D:
V_\lambda\to V_\lambda.
\]

Conjugation by \(S_q\) permutes the \(j\)-subsets and sends \(\Pi_D\) to \(\Pi_{gD}\). Thus \(F_j\) commutes with the irreducible \(S_q\)-action, and Schur’s lemma gives \(F_j=xI_{V_\lambda}\). Each summand has trace \(f^\theta\): the trivial \(S_{q-j}\)-multiplicity in \(V_\lambda\downarrow S_{q-j}\) is \(f^{\lambda/(q-j)}=f^\theta\), since deleting the full first row leaves \(\theta\). Tracing on the \(f^\lambda\)-dimensional space gives

\[
xf^\lambda=\binom qj f^\theta,\qquad
F_j=\frac{\binom qj f^\theta}{f^\lambda}I_{V_\lambda}.
\]

This accounts separately for the \(1/(q-j)!\) projector normalization, \(\binom qj\) subsets, invariant rank \(f^\theta\), and scalar normalization \(1/f^\lambda\).

For the pinned operator, set

\[
T_j=\sum_{\substack{D\subseteq U\setminus\{1\}\\|D|=j}}
\Pi_{D\cup\{1\}}:V_\lambda\to V_\lambda.
\]

The \(S_{q-1}\) fixing \(1\) permutes the terms, so \(T_j\) is \(S_{q-1}\)-central. The multiplicity-free branching rule gives the typed decomposition

\[
V_\lambda\downarrow S_{q-1}
=\bigoplus_{\tau\nearrow\lambda}V_\tau,
\]

with \(\dim V_\tau=f^\tau\), so \(T_j\) is scalar on each child. The stability assumption makes

\[
\tau_0=(q-j-1,\theta)
\]

a valid child of dimension \(f^{\tau_0}\). Restricted to it, each summand averages an \(S_{q-j-1}\) subgroup and has trace

\[
f^{\tau_0/(q-j-1)}=f^\theta.
\]

There are \(\binom{q-1}{j}\) summands, so the scalar on \(V_{\tau_0}\) is

\[
\frac{\binom{q-1}{j}f^\theta}{f^{\tau_0}}.
\]

**Verdict on Claim 4: CONFIRMED.** It has no LR-multiplicity branch.

### A6. Exact-rational matrix gates

#### Construction and value-versus-formula statement

The code independently constructs \(V_\lambda\) as the standard-polytabloid column space in the tabloid permutation module. Exact integral representation matrices come from an invertible pivot-row minor. It builds \(P_\xi\) from the character central idempotent of \(S_{n-1}\times S_n\); characters are traces of separately constructed smaller Specht modules. Each \(\Pi_D\) is a literal subgroup average. Arithmetic is exact over \(\mathbb Q\); residuals use literal matrix equality, never tolerances.

- Claims 1–3: these gates exercise independent constructions of the operators, not A2’s branching-rank formula or A3–A4’s counting derivation. They corroborate the identities and values, but do not independently validate each printed proof step.
- Claim 4: independently averaged free and pinned matrices are compared to the stated hook-length scalars. The pinned matrix is built directly in \(V_{\tau_0}\).
- The optional \(c=2\) stretch exercises only the local fixed-factor vanishing in A2, not a full carrier identity.

#### Mandatory results

| Case | Sector \((a,\alpha;b,\beta)\) | \((\kappa,\nu;c)\) | \(d_\lambda\) | expected / actual \(d_\xi\) | wrong \(D\)'s | C1 | C2 | C3 |
|---|---|---|---:|---:|---:|---|---|---|
| \((3,6,1),\theta=(1)\) | \((1,(1);0,())\) | \(((1,1),(3);1)\) | 5 | 1 / 1 | 10 | PASS | PASS | PASS |
| \((3,6,1),\theta=(1)\) | \((0,();1,(1))\) | \(((2),(2,1);1)\) | 5 | 2 / 2 | 6 | PASS | PASS | PASS |
| \((4,8,2),\theta=(2)\) | \((0,();2,(2))\) | \(((3),(2,2);1)\) | 20 | 2 / 2 | 50 | PASS | PASS | PASS |
| \((4,8,2),\theta=(2)\) | \((1,(1);1,(1))\) | \(((2,1),(3,1);1)\) | 20 | 6 / 6 | 30 | PASS | PASS | PASS |

For C1, PASS means every wrong-profile \(D\) of both sizes \(j\) and \(j+1\) gave exactly \(\Pi_DP_\xi=0\). For C2 and C3 it means the complete compressed left-minus-right matrix was exactly zero.

| Case | Free scalar/result | Pinned child | Pinned scalar/result |
|---|---|---|---|
| \((3,6,1),\lambda=(5,1)\) | \(6/5\), exact identity | \(\tau_0=(4,1)\), dimension 4 | \(5/4\), exact identity |
| \((4,8,2),\lambda=(6,2)\) | \(7/5\), exact identity | \(\tau_0=(5,2)\), dimension 14 | \(3/2\), exact identity |

#### Optional \(c=2\) stretch, with limitation

At \((n,q,j)=(7,14,6)\), the script enumerated

\[
c_{(2,1),(2,1)}^{(3,2,1)}=2,\qquad
\kappa=(3,2,1),\quad\nu=(4,2,1).
\]

It independently constructed \(V_{(3,2,1)}\) (dimension 16) and \(V_{(4,2,1)}\) (dimension 35), and obtained exact zero matrices for the \(S_4\)-fixed and \(S_5\)-fixed projectors. This supports A2’s two local “row too long” kill factors. It does **not** construct \(V_{(8,3,2,1)}\), \(P_\xi\), or a Claims 1–3 residual at \(c=2\); it therefore does not satisfy rule 7(b)’s \(c\ge2\) identity gate.

### A7. Failure-mode audit and promotion recommendation

- Normalizations: factorials, orbit sizes, invariant ranks, and irreducible-dimension divisions are audited in A2 and A5.
- Types: all maps act on \(V_\lambda\); compressed maps act on the \(f^\kappa f^\nu c\)-dimensional carrier; the local projector explicitly contains \(I_c\).
- Regimes: the assumptions and quantifiers are resolved in A1.
- Colored/full confusion: A3–A4 pass to colored sums only after compression and proved vanishing.
- Value/formula confusion: A6 identifies independent constructions and what they do not prove.
- Quantifiers: the proofs cover all admissible parameters and \(c>0\); the gates do not.

| Claim | Mathematical verdict | Highest recommended tier | Reason |
|---|---|---|---|
| 1 | **CONFIRMED** | **CERTIFIED\*** | Complete all-\(c\) proof and required \(c=1\) gates, but no full \(c\ge2\) identity residual. Rule 7(b) caps promotion. Caveat: analytic all-\(c\) proof independently reviewed; \(c\ge2\) carrier identity gate absent. |
| 2 | **CONFIRMED** | **CERTIFIED\*** | It depends on Claim 1 and has the same missing \(c\ge2\) identity regime. |
| 3 | **CONFIRMED** | **CERTIFIED\*** | It depends on Claim 1 and has the same missing \(c\ge2\) identity regime. |
| 4 | **CONFIRMED** | **PROVED** | Fresh complete proof, no LR-multiplicity branch, and exact independent gates at both commissioned sizes for both scalars. |

**Package recommendation:** mathematically all four claims are confirmed, but a joint node must remain **CERTIFIED\*** until a full \(c\ge2\) matrix residual for Claims 1–3 is archived. No DAG edits are made.

### A8. Reproducibility and frozen provenance

Commands:

    & '<machine-local-path-redacted>' 'se/artifacts/logs_se_w2blind_20260719/w2_blind_gates.py'
    & '<machine-local-path-redacted>' 'se/artifacts/logs_se_w2blind_20260719/w2_c2_stretch.py'

SHA-256:

    9e9498b025a4e2fb2ab902c01e18e3872a0371ede0a973ef22111e50f6606b24  se/artifacts/logs_se_w2blind_20260719/w2_blind_gates.py
    bbc4ea3d49d09dbb0ae1fc334ab3ea71a44bf4af446e90101f520673dce30183  se/artifacts/logs_se_w2blind_20260719/w2_blind_gates.log
    8bc472859d0dc8d3e4b2e741941c60bf793606e78ea76c5cc3a46d34218a5dba  se/artifacts/logs_se_w2blind_20260719/w2_c2_stretch.py
    ab4117504f979868e16a68aa9f532e7e87f1380de0bdc7eebb4d23483baa16ed  se/artifacts/logs_se_w2blind_20260719/w2_c2_stretch.log

### A9. Exact order followed through the blind freeze

1. Received the setting and Claims 1–4 inline.
2. Listed repository guidance and artifact names while explicitly excluding both comparison files; did not open either.
3. Inspected only the designated blind log directory.
4. Derived A1–A5 independently.
5. Wrote the exact-rational standard-polytabloid gate.
6. Ran it with the required interpreter; after one timeout, memoized repeated subgroup averages and reran the same construction successfully.
7. Read DAG_PROTOCOL.md to apply rule-7 caps; still did not open either comparison file.
8. Wrote and ran the optional \(c=2\) local-factor gate.
9. Computed SHA-256 hashes for all four scripts/logs.
10. Wrote and froze Part A.

At this freeze point neither comparison file had been opened.

## Part B — post-freeze comparison

### B1. Files opened and integrity

Only after Part A had been frozen and its pre-comparison hash written did I open, in this order:

1. se/artifacts/se_frames1_20260719.md, SHA-256 d360c66fa9efc9f011b5b81b91b882997731e0454e2b7357e8cd8ce3a124442b.
2. se/artifacts/se_frames1_review_20260719.md, SHA-256 7936c298d526d15709a06cfd86d52de6e001e862f5d41ef6ba939b6b1e61cf84.

The hash of this report when it contained Part A only was

    ab5c8d288bdaa1e24a7805b840fde8f33d797123c345f833bea5927942e8c8ed

and was frozen separately in se/artifacts/logs_se_w2blind_20260719/partA_frozen.sha256 before either comparison file was opened.

### B2. Comparison with R1 §4

R1 §4 and Part A agree on all four claims and on their scope:

- R1 Lemma 4.1 uses the color-preserving subgroup inside \(H\cap K_D\), its average, and the “one-row partition fits” branching test. Part A A2 reaches the same conclusion and makes the multiplicity action more explicit as \(Q_{\kappa,r}\otimes Q_{\nu,s}\otimes I_c\), including its rank.
- R1 Theorem 4.2 removes query-containing free terms, then uses \(r+s=a+b\) to force \((r,s)=(a,b)\). Part A A3–A4 uses the same termwise counting.
- R1’s paragraph after (4.4) states the free and pinned scalars as consequences of centrality and ranks. Part A A5 expands this into separate Schur-lemma and child-trace proofs, including all domains and dimensions.
- Both explicitly warn that the colored sum replaces the full orbit sum only after carrier compression and termwise vanishing. Neither uses function support as a proxy for an operator identity.

I found no disagreement, missing normalization, or hidden restriction in R1 §4 relative to the inline claims. One small proof-style difference is that R1 invokes centrality of \(P_\xi\) to say it commutes with \(Q_D\); Part A only needs \(Q_DP_\xi=0\) on the carrier and \(\Pi_DQ_D=\Pi_D\). Both arguments are valid because \(L_D\le H\).

The gate constructions are genuinely different. R1 reports point-permutation, two-subset, and exterior-square ambient models (sizes 6, 8, and 28 in its table). Part A uses standard-polytabloid irreducibles of dimensions 5 and 20 and independently builds the \(H\)-central idempotents from character traces. The agreement is therefore cross-construction evidence, not a rerun of R1’s formulas or matrices.

### B3. Comparison with the prior review §3

The prior review §3 reaches exactly the same mathematical verdicts:

- \(\Pi_D=\Pi_DQ_D\) for the average over the color-preserving subgroup.
- Fixed vectors in \(V_\kappa\downarrow S_{n-1-r}\) and \(V_\nu\downarrow S_{n-s}\) are controlled by the skew-tableau multiplicities \(f^{\kappa/(n-1-r)}\) and \(f^{\nu/(n-s)}\).
- A row-length obstruction kills a wrong color, on all LR copies through \(I_c\).
- The free and pinned identities follow by the same \(r+s\) count.
- The two scalars follow from centrality and trace.

The prior review candidly says its W2 derivation was chronologically contaminated because it saw R1’s short proof first; it therefore recommended leaving W2 pending until a clean rule-7(c) review. Part A supplies that clean chronology: its proof and gates were frozen and hashed before either R1 or the prior review was opened.

The prior review’s numerical W2 gate covered the two \(q=6,j=1\) sectors, whereas Part A additionally covers two \(q=8,j=2\) sectors as commissioned. Its \(c=2\) stretch formed the full structural tensor-zero matrices of size \(1120\); Part A’s cheaper stretch verifies only the two factor projectors of sizes 16 and 35. Both correctly state that this is not a non-\(H\)-normalizing compressed \(P_\xi\Pi_DP_\xi\) gate and hence does not remove the rule-7(b) cap.

### B4. Coincidence disclosure required by rule 7(c)

There is substantial coincidence of proof structure and notation:

| Item | Coincidence |
|---|---|
| Subgroup notation | Part A independently chose \(L_D\) for the color-preserving subgroup, exactly as R1 §4 and prior-review §3 do. |
| Averaging notation | Part A independently chose \(Q_D\) for its projector, again exactly matching both files. |
| Branching test | All three use \(\dim(V_\kappa)^{S_m}=f^{\kappa/(m)}\) and the criterion that the row \((m)\) fit in \(\kappa\), then repeat it for \(\nu\). |
| Multiplicity handling | All three identify the LR factor as a spectator \(I_c\); Part A displays the complete tensor-product map and rank. |
| Orbit count | All three split by whether the query is included and force \((r,s)=(a,b)\) from \(r+s=a+b\). |
| Scalar proof | Part A and prior-review §3 both use centrality plus trace; R1 states the same argument more tersely. |
| \(c=2\) stretch | Part A and the prior review both select \(\theta=(3,2,1)\), \(\alpha=\beta=(2,1)\), \(\kappa=(3,2,1)\), \(\nu=(4,2,1)\), and the \(S_4/S_5\) fixed-factor kills. This sector was suggested inline, but the exact factor-level implementation was independently chosen before reading the prior report. |

The symbols \(P_\xi,\Pi_D,r,s,a,b\) were already fixed in the inline claims and therefore are not evidence of anchoring. The additional matches \(L_D,Q_D\) and the exact proof sequence are real coincidences and are disclosed here. They arose before access to either comparison file, as certified by the Part-A hash and execution chronology. The route is also the direct subgroup-averaging proof naturally forced by the claim, so structural convergence is unsurprising; nevertheless, the notation-level match is too close to leave undisclosed.

There is no comparable coincidence in the gate implementation: Part A’s standard-polytabloid/character-idempotent construction differs materially from both reports’ permutation-model gates.

### B5. Final post-comparison verdict

Comparison revealed no counterexample and no change to the frozen mathematical verdicts:

- Claims 1–3: **CONFIRMED**, with recommended tier **CERTIFIED\*** because the actual \(c\ge2\) compressed identity regime remains untested at matrix level.
- Claim 4: **CONFIRMED**, with recommended tier **PROVED** as a standalone claim.
- Joint Claims 1–4 package: **CERTIFIED\*** with the explicit rule-7(b) caveat.

Relative to the prior review, this report removes only its rule-7(c) chronological blocker for W2. It does not remove the independent \(c\ge2\) identity-gate blocker. No DAG files were edited.

### B6. Complete exact order

1. Received only the inline setting and claims.
2. Avoided both comparison files and their associated source/review logs.
3. Derived the proof and type audit.
4. Built and ran the exact \(c=1\) matrix gates.
5. Read DAG_PROTOCOL only to apply the required review standard and ladder cap.
6. Built and ran the optional local \(c=2\) factor gate.
7. Wrote and froze Part A.
8. Computed the Part-A-only SHA-256 and wrote its frozen hash file.
9. Opened R1, se/artifacts/se_frames1_20260719.md.
10. Opened the prior review, se/artifacts/se_frames1_review_20260719.md.
11. Compared R1 §4 and prior-review §3 against frozen Part A, recorded all structural and notational coincidences, and appended Part B.
12. Left the proof DAG untouched.
