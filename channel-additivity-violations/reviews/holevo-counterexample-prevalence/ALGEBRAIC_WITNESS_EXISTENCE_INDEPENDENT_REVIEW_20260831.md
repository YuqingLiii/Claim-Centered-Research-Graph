# Independent adversarial review: algebraic p=1 witness existence and semidecision

Date: 2026-08-31

Reviewer: independent Codex review context `/root/q2_probability_review`.

## Independence declaration

I did not author the algebraic-witness artifacts, canonical node, route, or either premise. I
received the completed proposer materials only for read-only adversarial review. I did not modify
any proposer artifact, canonical YAML, assessment, event, frontier, or generated view. This
immutable report is the only project file created by the audit.

## 1. Scope and executive verdict

This review covers route `density-and-semidecision` and the claim of
`HCPREV.algebraic-witness-existence`. I interpret the mathematical core in its narrowest supported
sense: a finite-dimensional **minimum-output-entropy pair** defect at Renyi parameter `p=1`.
Holevo pair witnesses, same-channel witnesses, and transformed random laws are not needed for that
claim and are not part of the promotion verdict below.

The mathematical construction is sound in outline:

1. Gaussian-rational Cayley unitaries form an effective dense subset of each finite unitary group;
2. strict finite-dimensional MOE pair gaps survive a sufficiently close algebraic approximation;
3. explicit finite pure-state nets and directed entropy intervals give the rigorous lower
   certificate `L_N+L_M-U_(N tensor M)`; and
4. dovetailing terminates because one enumerated candidate has gap strictly greater than the
   requested rational target.

The current canonical dossier nevertheless **does not qualify for `PROVED`**. It has three
load-bearing interface defects:

- the exact claim does not define which additivity quantity, pair/self convention, gap sign, or
  entropy unit it asserts;
- it lists the broader Holevo-containing `HCPREV.product-haar-unbounded` premise although the
  exact MOE-only atom `HCPREV.product-haar-moe-unbounded` is the actual load-bearing theorem; and
- the route's effective certification step directly uses an entropy-continuity theorem and
  algebraic/sphere-net computability facts that are neither registered as route assumptions nor
  isolated as a reviewed premise. `HCPREV.open-set-stability` exposes qualitative persistence, not
  the complete effective certification interface used here.

The route and node must remain `CONJECTURED` until those repairs are made and independently
re-reviewed. This report does not change or close `HCPREV.explicit-witness-frontier` or
`HCPREV.goal`.

## 2. Protocol, immutable inputs, and exact hashes

`DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` were read in full. Their hashes were:

- `DAG_PROTOCOL.md`: `sha256:d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095`;
- `FILE_PROTOCOL.md`: `sha256:d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.

The current exact statement hashes are:

| object | exact hash | present verdict |
|---|---|---|
| `density-and-semidecision` implication | `sha256:85b9035d74a707bdde466d0b9d154a22617daf39260ee01fba0bc70b4e7c3167` | mathematical core PASS; canonical interface BLOCK |
| `HCPREV.algebraic-witness-existence` claim | `sha256:c66257c3a87568e457796774ecbfb5c07ca83a0c3077d9e913169587fd36abdb` | ambiguous; do not promote |

The relevant premise interfaces are:

| premise | exact claim hash | status | role in this proof |
|---|---|---|---|
| `HCPREV.product-haar-unbounded` | `sha256:e50f0b1cf0c3a7640ca404b494d7a0f8a3d1a8cdcbaf9e7ee6cb9967097a78a9` | `PROVED` | currently listed, but broader than needed and contains Holevo pushforwards |
| `HCPREV.product-haar-moe-unbounded` | `sha256:d440f868f357ab31ba91a26b622eb020b69f597a4f5c62e69c53661689c0bc9e` | `PROVED` | exact load-bearing strict finite MOE pair theorem |
| `HCPREV.open-set-stability` | `sha256:5e48fcbc53334cc32e190854c3339a1c042116b5da998f877b152d81c3dd4310` | `PROVED` | qualitative fixed-dimensional continuity/open-neighborhood theorem |

Reviewed file hashes were:

| file | SHA-256 |
|---|---|
| `proof-dag/nodes/HCPREV.algebraic-witness-existence.yaml` | `21f9849e1966de6e6a892401c37c43f02472a4dfb73c817964aa0d2b43a44d2e` |
| `artifacts/ALGEBRAIC_WITNESS_EXISTENCE_PROOF_20260829.md` | `63622cb8aa2cd6a47095f34493f3f0d9dcc6874ef90d6707bfb292027a445221` |
| `artifacts/ALGEBRAIC_WITNESS_ADVERSARIAL_AUDIT_20260830.md` | `3a03dcca167917fc553834d8323efff0ee43c3dd88b56f0ecf14b5fbd5a0356b` |
| Audenaert primary PDF | `dc2265209fd7fb86aa7ce03a541c15d8b9f5a29b70c281728650eef0ad87bdb7` |

I visually inspected Audenaert, Theorem 1, PDF p. 2. It states, for `d`-dimensional states and
`T=(1/2)||rho-sigma||_1`, the base-two bound

`|S(rho)-S(sigma)| <= T log_2(d-1)+H(T,1-T)`.

## 3. Finding HCP-AW-IR-01 - Gaussian-rational Cayley enumeration and density PASS

Let `A*=-A` have entries in `Q(i)` and define

`C(A)=(I-A)(I+A)^(-1)`.

`I+A` is automatically invertible. If `(I+A)v=0`, then `Av=-v`; but `<v,Av>` is purely imaginary
for a skew-Hermitian matrix while `-||v||^2` is negative real, a contradiction. Matrix inversion
over `Q(i)` stays in `Q(i)`, and direct multiplication gives `C(A)*C(A)=I`, so every enumerated
matrix is an exact Gaussian-rational unitary.

For a unitary `U` without eigenvalue `-1`, the inverse chart

`A=(I-U)(I+U)^(-1)`

is skew-Hermitian. Gaussian-rational skew-Hermitian matrices are entrywise dense in all
skew-Hermitian matrices, and the Cayley map is continuous on this chart. If `U` has eigenvalue
`-1`, an arbitrarily small scalar phase perturbation avoids the finite forbidden set of phases;
therefore the chart image is dense in all of `U(D)`, not merely in one closed component.

The set is effectively enumerable by dimension, common denominator, integer real/imaginary
numerators, and the skew-Hermitian constraints. For equal-weight random-unitary channels,

`||Ad_U-Ad_V||_diamond <= 2||U-V||_op`,

so entrywise convergence of a fixed finite tuple implies diamond convergence of its channels.
The conjugate tuple converges simultaneously. Each Kraus operator is
`m^(-1/2)U_i`; its entries are algebraic even though the scalar square root need not be Gaussian
rational.

**Verdict:** PASS. `I+A` needs no decision branch, the omitted `-1` boundary does not spoil
density, and the enumerated channel data are algebraic.

## 4. Finding HCP-AW-IR-02 - strict finite algebraic MOE pair witnesses PASS under a precise claim

The atomic MOE premise states in bits that, for every real target, some fixed-depth finite
product-Haar channel/conjugate-channel sample has a pair defect strictly larger than that target.
For rational `G>0`, choose a finite sample with

`Delta_S(N,bar(N))=S_min(N)+S_min(bar(N))-S_min(N tensor bar(N))>G`.

The difference `Delta_S-G` has a positive margin. Fixed-dimensional entropy continuity, together
with the finite-tuple diamond estimate above, gives a sufficiently small neighborhood in which the
gap remains above `G`. Cayley density supplies an exact algebraic tuple inside that neighborhood.
Thus a finite algebraic MOE pair witness with gap `>G` exists.

No Weyl extension, Holevo identity, flagged direct sum, pair-to-self loss, or pushforward random
law is needed for this conclusion. The paragraphs about those transformations in the proposer
artifacts are non-load-bearing to the narrow claim reviewed here. If a future claim explicitly
asserts Holevo pair or same-channel witnesses, it must state those quantities and list the exact
`PROVED` Weyl/flagged atoms and their transformed-law boundary.

**Verdict:** the existence implication PASSes for a base-two MOE pair claim. The current canonical
wording does not state that claim precisely enough for promotion.

## 5. Finding HCP-AW-IR-03 - explicit rational pure-state nets and S_min bounds are valid but underdocumented

Minimum output entropy may be minimized over pure inputs: for
`rho=sum_i p_i |psi_i><psi_i|`, entropy concavity gives

`S(N(rho)) >= sum_i p_i S(N(|psi_i><psi_i|)) >= min_i S(N(|psi_i><psi_i|))`.

Finite rational nets with a certified mesh can be constructed explicitly. Identify the complex
unit sphere with the real sphere `S^(r-1)`, `r=2d_in`, and use rational stereographic points

`sigma(t)=(2t/(1+||t||^2),(||t||^2-1)/(1+||t||^2)),  t in Q^(r-1)`,

together with the omitted north pole. The derivative norm is at most two. Given rational
`delta>0`, choose an integer `R` with `2/sqrt(1+R^2)<=delta/2` and a sufficiently fine rational
grid in `[-R,R]^(r-1)`. Grid images cover the bounded chart, and the north pole covers all
`||t||>=R`. This is a finite rational `delta`-net with a computably certified Euclidean mesh.

For unit vectors, pure-state trace distance obeys

`T(|psi><psi|,|phi><phi|)<=||psi-phi||_2`.

CPTP contraction and Audenaert therefore give a computable output entropy modulus
`omega_d(delta)` tending to zero. For a finite net `E_delta`, directed entropy intervals yield

`min_(phi in E_delta) lower(f_N(phi))-omega_d(delta) <= S_min(N)`

and

`S_min(N) <= min_(phi in E_delta) upper(f_N(phi))`.

The same construction is applied independently to the two single-channel input spheres and the
full joint input sphere; the latter includes entangled inputs. Consequently

`Delta_S(N,M) >= L_N+L_M-U_(N tensor M)`.

The sign is correct: lower bounds are used for both positive single-channel terms and an upper
bound for the subtracted joint minimum.

**Verdict:** the finite-net mathematics PASSes. The existing proposer artifacts merely say
“standard rational sphere parametrization” and do not give this covering-radius construction,
the pure-state reduction, or the input-distance conversion. These details must be added to the
public proof or isolated in a reviewed effective-certification premise before completion.

## 6. Finding HCP-AW-IR-04 - entropy interval computability is plausible but not yet an assembled proof interface

For algebraic Kraus matrices and a rational net vector, every output-density-matrix entry is
algebraic. A complete effective route can proceed by exact algebraic Hermitian spectral isolation,
or by rational Hermitian approximants plus certified operator-norm and eigenvalue perturbation
bounds. Positive isolated eigenvalue intervals admit directed logarithm intervals. An interval
touching zero is handled continuously: `-x log x` is nonnegative and has a computable upper bound
tending to zero with its upper endpoint. Thus `0 log 0=0` causes no decidability obstruction and
finite directed intervals for the total entropy can converge to the exact entropy.

However, the current public proof provides only the assertions “algebraic matrices have computable
eigenvalues” and “logarithms ... admit certified rational intervals.” It does not specify an exact
representation for algebraic entries, a root/eigenvalue isolation algorithm, an interval method
at zero, or a finite certificate verifier. No route assumption or atomic node exposes this
load-bearing effectivity theorem.

This matters because the qualitative claim of `HCPREV.open-set-stability` alone cannot imply that
the global minimum is semidecidable. An effective modulus and effective pointwise entropy
enclosures are strictly stronger interfaces than bare continuity/open-set persistence.

**Verdict:** no mathematical contradiction found, but the assembled canonical argument is
incomplete at the exact computability interface. This is a promotion blocker, not a refutation.

## 7. Finding HCP-AW-IR-05 - dovetail termination and certificate direction PASS conditionally

Enumerate candidate dimensions and finite Gaussian-rational Cayley tuples. For each candidate,
dovetail the three sphere-net meshes and every arithmetic precision. Define

`C_k=L_N(k)+L_M(k)-U_joint(k)`.

The net moduli tend to zero and pointwise entropy intervals shrink, so `C_k` converges to the true
MOE pair defect from a certified lower side; monotonicity of the sequence is unnecessary. If one
enumerated candidate has `Delta_S>G`, then for sufficiently advanced mesh and interval precision
`C_k>G`. Testing that strict rational inequality is decidable, so the corresponding dovetailed
branch halts and prints the algebraic channel pair, mesh data, entropy intervals, continuity
allowances, and final lower certificate.

No advance knowledge of the successful dimension, denominator, residual margin, or precision is
needed. Their absence means there is no useful time/space/size bound; it does not defeat eventual
termination.

**Verdict:** conditional PASS once Findings HCP-AW-IR-03 and HCP-AW-IR-04 are made into complete
public proof interfaces.

## 8. Finding HCP-AW-IR-06 - exact canonical repairs required before amendment review

The following is a minimal repair, not an instruction to claim more:

1. Rewrite the claim to define the quantity, sign, pair convention and units. A suitable narrow
   statement is:

   > For every rational `G>0` measured in bits, there exist finite-dimensional CPTP maps `N,M`
   > with algebraic Kraus entries such that
   > `Delta_S(N,M):=S_min(N)+S_min(M)-S_min(N tensor M)>G`. There is a Turing procedure which,
   > given `G`, eventually halts and prints such `N,M` together with a finite rational net/interval
   > certificate proving this strict global inequality. No dimension, denominator, certificate-size
   > or runtime bound is asserted.

2. Replace the unnecessarily broad premise `HCPREV.product-haar-unbounded` by the exact atomic
   premise `HCPREV.product-haar-moe-unbounded`. Keep `HCPREV.open-set-stability` only for the
   qualitative fixed-dimensional persistence it actually states.
3. Either create and independently prove an atomic effective-global-MOE-certification premise, or
   register every direct external/model input under this route. At minimum the route must expose:
   Audenaert's exact entropy modulus and base; pure-projector trace distance plus CPTP contraction;
   effective finite rational sphere nets with known mesh; and effective directed entropy intervals
   for algebraic positive semidefinite matrices, including intervals touching zero.
4. Expand the proof with the explicit entrywise-to-diamond bound, pure-state reduction,
   stereographic finite-cover construction, algebraic spectral/log interval representation,
   definitions of `L_N,L_M,U_joint`, and the dovetail convergence argument.
5. Mark all Holevo/Weyl/flagged/same-channel discussion as a non-load-bearing cross-reference, or
   remove it from this dossier. If those are desired conclusions, register separate exact claims
   and routes using the already `PROVED` Q2 transfer atoms and state the deterministic pushforward
   boundary.

These changes will alter at least the claim hash and canonical node hash. A fresh amendment review
must recompute all exact hashes and verify the repaired interfaces before any level change.

## 9. Promotion and scope boundary

No promotion is authorized by this review:

- route `density-and-semidecision` remains `CONJECTURED`;
- `HCPREV.algebraic-witness-existence` remains `CONJECTURED`;
- `HCPREV.explicit-witness-frontier` remains `OPEN`; and
- `HCPREV.goal` remains `OPEN`.

The theorem under review is computable existence. It does not exhibit a successful matrix tuple
now, prove that an implemented repository program has halted, provide a practical global
certificate, bound the successful dimension or denominator, or bound runtime. “Eventually prints”
is a termination theorem for an exhaustive procedure, not a currently printed explicit witness.

## 10. Checks and limitations

Without modifying proposer material, I:

- read both repository protocols in full;
- recomputed all exact target and premise hashes;
- inspected both `PROVED` premise dossiers and their independent review bindings;
- visually verified Audenaert Theorem 1 directly in the local primary PDF;
- reconstructed Cayley invertibility, density, enumerability, and algebraic Kraus data;
- supplied and checked an explicit rational stereographic finite-net construction;
- checked both directions of the `S_min` net bounds and the lower-gap certificate;
- audited algebraic entropy interval behavior at positive eigenvalues and at `0 log 0`;
- checked dovetail quantifiers under the strict `>G` margin; and
- enforced the MOE/Holevo, pair/self, transformed-law, explicitness, and resource-boundaries.

No actual successful algebraic tuple was generated or certified, and no practical search/runtime
claim was inferred. Only public source material and explicit derivations were used; hidden or
private chain of thought was neither requested nor used as evidence.
