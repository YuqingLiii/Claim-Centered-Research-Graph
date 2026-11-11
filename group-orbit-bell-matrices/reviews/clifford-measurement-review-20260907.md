# Independent review of the explicit Clifford measurement construction

Date: 2026-09-07 (America/New_York).
Reviewer: a separate Codex review agent using the inherited model,
delegated task `/root/orbit_d3_envelope`. The tool context does not provide
an independently verifiable exact model version. This is author-independent,
same-model-family review in a non-fresh context, not an external human or
different-model review. The reviewer did not author or modify the 2026-08-29
Clifford, balance, or extremizer proofs, their checker, or the audited nodes.
The reviewer previously authored the D3 envelope, which is not a dependency
here. Earlier review/literature tasks in this context are not concealed.

Reviewed stage: `/private/tmp/grothorb-classical-20260907-R0Shtu`.
All project-relative paths below are within `grothendieck-group-orbit/`.

Scope: the exact current `GROTHORB.measurements` claim and its sole active
`clifford-realization` route, including the feasible-weight-to-unit-vector
interface of its established `GROTHORB.extremizer-classification` premise.
No node, author file, or generated view was modified. This report supplies
review evidence, not an automatic node promotion.

## Exact statement binding

Hashes are SHA-256 of UTF-8 encoded YAML-decoded `claim.strip()` and
`implication.strip()`, preserving internal whitespace.

| Finding | Exact target | Reviewed SHA-256 | Verdict |
| --- | --- | --- | --- |
| F1 | `GROTHORB.measurements.claim` | `9c0bdccd36c869618ea053986796b1ad618a29b2ea76f4d583ea9a595bc6e419` | PASS |
| F2 | `GROTHORB.measurements.routes.clifford-realization.implication` | `d482793b04b0dfa5cff4f265631dae4e2c58d2eb70fc5617a63058c77defc077` | PASS |

F1 exact statement:

> If a feasible balance weight H for a nonzero transitive equivariant Bell matrix has rank s, its associated extremizer has an explicit quantum realization on a maximally entangled state using local dichotomic Clifford observables, with local Hilbert-space dimension 2^floor(s/2).

F2 exact statement:

> Map each real unit vector x to the Hermitian involution Gamma(x) in a Clifford representation and use its transpose on Bob's side. The maximally entangled trace identity reproduces every inner-product correlator.

The supporting classification claim has hash
`5cbc9e0d89f69f0929510b7592b1480185c5efcf320a3b619d3da4f41c5d02e3`, matching the current node's
`reviews/spectral-classification-repair-review-20260907.md`, Finding F3.
The current node marks the spectrahedral route PROVED and preserves the
retired, REFUTED commutant-classification route. This review uses no
commutant-only classification or averaging argument.

## Materials inspected

Both root protocols were read completely. The two audited/premise YAML
files, `artifacts/clifford-measurement-construction-20260829.md` (all
CL-T1--T6), `tools/check_clifford_generators.py` (complete),
`artifacts/clifford-exact-check-20260829.txt`,
`artifacts/complete-extremizer-classification-20260829.md` (complete),
`artifacts/balanced-rank-theorem-draft-20260829.md` (complete),
the classification repair review (complete), and its linked positioning
and exploration notes were read. Relevant generated dependency-view entries
were checked; they are navigation evidence, not mathematical premises.
All raw input hashes appear below and in the rerun record.

The all-rank argument below was checked independently of finite output.
The existing classification review is corroborating established-premise
evidence; the particular forward interface actually needed here is also
rederived explicitly in F1.

## F1 — Exact measurements claim: PASS

### 1. Feasible weight, rank, and unit-vector interface

Use the paired top singular bases from GOC-T1:
`U^T U=V^T V=I_r`, `AV=sigma U`, with positive row/column counts
m,n and `sigma>0`. Feasibility means
`H>=0`, `diag(VHV^T)=1_n`, and
`diag(UHU^T)=(n/m)1_m`.
Taking the first trace gives `tr(H)=n>0`; hence its rank s satisfies
`1<=s<=r`. There is no missing rank-zero Clifford case.

A real PSD factorization `H=TT^T` can be chosen with T of width s
and column rank s. Then
`Y=VT`, `X=sqrt(m/n)UT` have row squared norms respectively
`1_n` and `(m/n)(n/m)1_m=1_m`. Their rows are real vectors in
R^s, and Y has rank s since V has orthonormal columns. The score is
`sqrt(m/n) sigma tr(H)=sigma sqrt(mn)`, the universal spectral
upper bound. Thus every feasible H supplies exactly the associated
extremizing vector strategy required by the target. This forward argument
does not require invariant H, irreducibility, or a simple top singular value.

### 2. Tensor order and every generator-pair case, for arbitrary s

Put q=floor(s/2), D=2^q. Read each tensor string left to right as q
ordered computational-basis tensor factors, with the X or Y in slot j.
Every Pauli factor is Hermitian and squares to I; tensor products inherit
both properties, so every generator is a D-dimensional Hermitian involution.

For distinct generators, the exhaustive cases are:

- Same slot j: the pair is X versus Y. All other factors agree, and
  `XY=-YX` supplies exactly one minus sign.
- Different slots j<k: in slot j the first string has X/Y and the second
  has Z. This is the sole anticommuting pair of factors. Earlier slots
  are matching Z; later slots either include an identity on one side
  or otherwise commute. The two full strings anticommute.
- Odd extra generator `Z^(tensor q)): against any X/Y-slot string,
  only that slot anticommutes. Thus it anticommutes with all preceding
  2q generators.
- Identical generators have anticommutator 2I, by their squared identity.

For s=1, q=0: the empty tensor product is the scalar [1], and the only
required anticommutator is `[1][1]+[1][1]=2[1]`. There are no distinct
pairs to check. For even s there is no extra generator; for odd s>=3
the extra generator adds no tensor factor, so the dimension remains D,
not 2D. No faithful representation of the entire abstract complex
Clifford algebra is demanded; the explicit matrices satisfying the
relations suffice.

The one-sentence pair explanation in CL-T2 describes the different-slot
case, not the same-slot X/Y case literally. CL-T1 already states the Pauli
anticommutation needed for that remaining case, as shown above. This is
a nonblocking expositional imprecision, explicitly recorded here rather
than silently rewriting the author's text. No substantive mathematical
repair is required.

### 3. Trace orthogonality and real linear combinations

For a=b, `tr(Gamma_a Gamma_a)=D`. For a!=b, cyclicity and
anticommutation give
`tr(Gamma_a Gamma_b)=-tr(Gamma_b Gamma_a)=-tr(Gamma_a Gamma_b)`,
hence zero. This verifies the stated normalized trace identity without
depending on a convention about the phase of a Pauli string.

For all real v, Hermiticity is preserved by the real linear combination
`Gamma(v)=sum_a v_a Gamma_a`. Expanding its square and pairing the
off-diagonal terms yields `Gamma(v)^2=||v||^2 I_D`.
For unit v the observable is Hermitian and involutive. The two effects
`(I_D+Gamma(v))/2` and `(I_D-Gamma(v))/2` are orthogonal projections
summing to the identity, defining a valid binary projective measurement.

Here, as in CL-T3's explicit wording, eigenvalues are **in** {-1,+1};
both eigenspaces need not be nonzero. In particular s=1 gives deterministic
scalar observables ±1 and D=1. The state formula then has no nontrivial
entanglement; it is the maximally entangled state for that one-dimensional
local space. The claim does not impose nondegenerate outcomes or positive
entanglement, which would exclude this edge case.

One-generator traces are not assumed zero at s=1: its trace is 1.
For s>=2 the Pauli strings are traceless, but only the product trace
identity is load-bearing.

### 4. Transpose and maximally entangled state

For arbitrary complex matrices M,N, direct computational-basis expansion
of the stated normalized vector gives
`D^-1 sum_(k,l) M_kl N_kl=tr(MN^T)/D`.
The transpose is not an adjoint. For a Hermitian involution G,
`(G^T)^*=G^T` and `(G^T)^2=(G^2)^T=I`, so Bob's
`Gamma(y)^T` is still a Hermitian involution even though Y-Pauli
strings are imaginary. Applying the identity with
`M=Gamma(x), N=Gamma(y)^T` gives
`tr(Gamma(x)Gamma(y))/D=x dot y`.
It reproduces every labeled correlator, hence the Bell score, with no
complex-conjugation sign error.

The dimensions of the displayed matrices and both local state factors are
exactly `2^floor(s/2)`. This proves existence of the stated realization.
It does not assert that no other realization in smaller physical dimension
exists, even for an H of minimum feasible rank.

## F2 — Clifford-realization route, assembled: PASS

The sole listed premise gives the real unit-vector factor model. F1.1
checks the exact needed interface directly, including positivity of s,
rectangular normalizations and attainment. F1.2--4 establish the route's
map into Hermitian involutions and its transpose/trace conclusion for all
such vectors, with the exact dimension required by the parent. Therefore
the implication establishes the unchanged parent claim from the stated
premise, not merely from a tested collection of H or small dimensions.

No additional unresolved theorem is used in this route: the Pauli identities,
tensor multiplication, real PSD factorization and the state expansion are
written algebraic constructions. For source attribution, the standard
vector-to-Clifford correspondence is explicitly described in
[Slofstra, arXiv:1007.2248, Section 2.4, Theorem 2.5 and the following
paragraph](https://arxiv.org/pdf/1007.2248), which attributes it to
Tsirelson. This original paper was checked online. No unverified theorem
number in Tsirelson's original is claimed. The present review proves the
specific Pauli convention independently rather than importing that source
as an unrecorded load-bearing theorem.

The older GO-T7 ceiling bound is safe but weaker; CL-T2--5 and GOC-T7
supply the current floor formula. Historical author-level status statements
in old prose are not treated as present canonical assessments. Neither the
retired commutant route nor any supposed physical-rank minimality is used.

## Exact rerun and checker audit

New rerun record:
`artifacts/clifford-measurement-review-rerun-20260907.txt`,
SHA-256 `52365718203908131b4d2bf5446bc84c3ef5a3cfce288c1f93db41658aae7e74`.

The unchanged author command exited 0 for s=1,...,9, with D respectively
1,2,2,4,4,8,8,16,16. Its code checks Hermiticity, transposed Hermiticity,
generator squares, all ordered anticommutators and product traces, and
the square of Gamma(1,2,...,s). The tensor-loop indexing matches CL-T2.

The author's use of Python complex is not a general exact Gaussian-integer
implementation: its components are binary64. For the present run it is
nevertheless exact. Generator entries have integer real/imaginary parts;
the test linear combination has each component bounded in magnitude by
`sum_(a=1)^9 a=45`. A complex multiplication has component magnitude at
most `2*45^2=4050`, and a length-at-most-16 sum is bounded by 64800,
far below 2^53. All products and partial sums are representable integers;
there is no rounding or tolerance in this bounded computation.

An independent check, whose complete source and command are preserved in
the rerun artifact, instead constructs matrices by their action on basis
bit strings and uses pairs of Python integers for every matrix operation.
It cross-checks the tensor order and independently checks all 285 ordered
generator pairs, Bob's squared involution, direct state-sum correlators,
individual traces, and two mixed integer-vector identities for s=1,...,9.
It also confirms the untransposed Y/Y state numerator is -D, so the
transpose-sensitive test is nonvacuous. All checks pass.

The initial reviewer script used `int.bit_count()`, unavailable in the
local Python 3.9.6, and stopped before testing s=1. That compatibility failure
and its exact one-expression repair are retained in the run record. It is
not hidden, and it is not an author-proof failure or counterexample.

Neither finite run supplies the all-s proof; that is F1's exhaustive algebraic
case analysis. This is not formal proof-assistant verification, robustness
analysis, self-testing, or a claim of minimum physical Hilbert dimension.

## Raw input-file SHA-256 snapshot

```text
d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095  DAG_PROTOCOL.md
6a2ea1af9bd14a4eaa8d158e304aee5e82cf907497addb17c2771782a4e6a329  FILE_PROTOCOL.md
aad42bce01452d668ebebf0020f6dbc5702c7a3548e15084e6336bc23530709f  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.measurements.yaml
1dbac3b4479ed340529a0140b1f42840b089c52676beedc2e5996a34fcb8f234  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.extremizer-classification.yaml
23024138fe8577a78c8767afee62ba8c4f73b36e1d46fa33bd4fd625e021842b  grothendieck-group-orbit/artifacts/clifford-measurement-construction-20260829.md
b52a22592bf30e6896c459b8700aac99d07d4034cb0dc099a5be787753e27d7c  grothendieck-group-orbit/tools/check_clifford_generators.py
b4985d87c4b1f8dabb0f6ce6e04669c2e40cd531f9cf407f167211f7d3de5497  grothendieck-group-orbit/artifacts/clifford-exact-check-20260829.txt
44ac28ada792471f5ff014f763a94da16929ac2f6d99df01b2a056f52a47cd99  grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md
c6b7bd87193b34ad6e5c05d20971fba2722ba202c3e87e2bd6717a951d5dfef4  grothendieck-group-orbit/artifacts/balanced-rank-theorem-draft-20260829.md
0b2d2f2980932519da758a050531571f8fbcf15b3a7bb16855e1d891dab071a4  grothendieck-group-orbit/reviews/spectral-classification-repair-review-20260907.md
310ed176e035bba8c0b57d90680656a6a50b3b3e1ab8b83d1448468ae2a93473  grothendieck-group-orbit/artifacts/group-orbit-literature-positioning-20260907.md
bfcf8c92aa62106e659e950bd52d4d9120d730ee952e913c445092eeb7db5873  grothendieck-group-orbit/artifacts/group-orbit-exploration-20260907.md
3bc90a10b8adcc3b149c1fe2b31b12e984ff3a1fecae3102b1c8b2f32dd32903  grothendieck-group-orbit/proof-dag/GRAPH.mmd
da90f36a54946536ea8e17553c74d72242df32e3e3691c984736c55b1a708683  grothendieck-group-orbit/proof-dag/NODE_INDEX.md
```

F1 and F2 are both PASS for the exact statements above. No blocking defect
was found; the two nonblocking exposition/arithmetic qualifications are
retained explicitly. Linking this review, updating levels, and regenerating
views remain separate coordinator operations.

