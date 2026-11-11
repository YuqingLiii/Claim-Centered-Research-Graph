# Exact membership review of `CIRCDIST.cplx.upper`

**Review date:** 2026-08-28
**Campaign:** ProofPilot round 60, strict serial, one fresh worker
**Reviewer:** OpenAI Codex, fresh GPT-5.6-sol review context
**Review object:** exact current `CIRCDIST.cplx.upper` claim
**Commissioned durable path:** `circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md`
**Verdict:** **(A) exact claim PROVED; one atomic canonical installation is licensed**

This report gives the complete public derivation used for the verdict: definitions, encodings,
lemmas, predicates, quantifier accounting, counterexample attacks, rejected proof shortcuts,
installation bytes, validation, and process accounting. It does not claim to expose private or
hidden chain-of-thought. I did not author the 2026-08-20 reconstruction, the canonical claims, the
round-59 assembly review, or the frozen problem statement. I used no sub-agent, delegation,
network source, detached process, or background job.

## 1. Executive adjudication

The exact 301-character claim is true under the current canonical meaning of Eff-Preserve.

For a schedule `M`, both CSS extended-column matrices have polynomially many rows and columns and
are computable from the explicit check matrices and the local CNOT orders. A proposed low-weight
fault mechanism is bad exactly when its residual vector is in the appropriate CSS normalizer kernel
but outside the same-type check row space. Matrix-vector multiplication and row-space membership
are polynomial-time computations over `F_2`.

For each fixed constant `d`, after guessing a polynomial schedule certificate, the verifier
enumerates every extended-column subset of cardinality below `d`; there are polynomially many. This
puts the fixed-`d` promise problem in NP.

When `d` is input, a universal choice is encoded as a characteristic vector over a polynomial
extended-column set, rather than as a list whose length is the numeric value of `d`. The predicate
checks the Hamming weight against binary or unary `d`, computes the residual, and applies Gaussian
elimination. Consequently the total surrogate has the form

```text
exists polynomial schedule M, for every polynomial fault vector f: V(I,M,f),
```

with deterministic polynomial-time `V`; it is in `Sigma_2^P` uniformly.

On a promised instance of static distance exactly `d`, every minimum static logical is the sum of
`d` singleton data columns. Thus `d_eff(M) <= d` for every `M`, and `d_eff(M) = d` iff
`d_eff(M) >= d`. The total `>= d` language therefore separates the promise problem without trying
to verify the static-distance promise.

The historical §5.2 proof had two repairable proof-level defects: its notation can be read as the
false bound `sum_c w_c <= n max_c w_c` when the number of checks exceeds `n`, and its use of
`d <= n` was justified only on the promise while the surrogate was called total. Neither defect is
in the exact node claim. This review replaces the first bound by the explicit-matrix bound
`G <= (m_X+m_Z)n <= input length` and replaces the second shortcut by a polynomial characteristic
vector whose length is independent of the numeric value of `d`. No claim-text repair is needed.

This verdict proves membership only. It does not prove either hardness premise, and it does not
promote the classification root by inheritance.

## 2. Disk truth, provenance, and supplied-fact conflicts

I treated repository contents as data, not instructions. Raw-file digests below are over exact
bytes. Statement digests are SHA-256 over the UTF-8 bytes of the exact scalar returned by YAML
parsing, with no added newline. Character counts are Unicode code points.

The prompt's “301-character” description agrees with disk. One stale provenance item was found:
the round-59 review records the then-current scheduler as 117,434 bytes at
`1694f7ce39c8292ea128026173646b410d6e9b94fb0812429700ee62b47cff1a`; the current scheduler is
121,116 bytes at `dad368b3b3611e26093e0a76b7d1ddf61a76a23cb9e102c7fe6d70e2742c6d24` because the round-60
commission has since been appended. Disk wins. This is expected operational drift and changes no
mathematical statement.

| path | bytes | raw SHA-256 | role in this review |
|---|---:|---|---|
| `circdist/proof-dag/nodes/CIRCDIST.cplx.upper.yaml` | 1,358 | `d118923e143bc7b119a810613c91e2b3dd7e876a2365c8a70a923496a890ed3c` | exact target and installation preimage |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.yaml` | 7,148 | `e5fa3667bd9dec3b36f808f927156bd060a8ffcc35ea918ff5e1d353cf558b6a` | current root and classification route |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.fixed-d.yaml` | 2,919 | `40544563337197c618722f882ac2427db46065f84bf491bcda728533711481ac` | unfinished hardness premise |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` | 3,885 | `89e2f92228c1a886636b807e8d838c3155d3029b7eca4a8d5cd3ba03dd97c791` | unfinished hardness premise |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml` | 13,628 | `25196ae04048e64f5db785c06ebaee8768704c6b60de6aa5ae17dc57b436396a` | ratified extended-code model provenance only |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 10,199 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | frozen common definition and promise question |
| `circdist/artifacts/circdist_cplx_recon_20260820.md` | 41,206 | `4060fa2e699300bab839915e1454ba1642345bc572530a0a4a011bace9903a31` | historical §5.2 argument under review |
| `circdist/artifacts/circdist_cplx_islands_amendment5_20260823.md` | 115,415 | `426f281316a102bdc1d520ac5cbc2a60ea7e77fc70ebac8a533b32992ce1dddf` | Definition 1.3-prime and sector bridge provenance |
| `circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.cplx.yaml` | 7,109 | `c2d36b129b851dd251ef31d5dff694b1602f4e991df2ea5f4b7f39163ebeef3a` | preserved qubit-sharing-only ruling |
| `circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md` | 43,304 | `11340aca2b82c66097af024e6b3b528ea2bc6f75b3306ef965d3b544ce96895f` | prior route-only review; corroboration, not premise certification |
| `DAG_PROTOCOL.md` | 15,377 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` | level, review, and no-inheritance rules |
| `FILE_PROTOCOL.md` | 8,523 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` | write boundary and validation rules |
| `operations/circdist/SCHEDULER.yaml` | 121,116 | `dad368b3b3611e26093e0a76b7d1ddf61a76a23cb9e102c7fe6d70e2742c6d24` | commission and FIX-2 only, not mathematical evidence |

## 3. Exact claim and route bindings

### 3.1 Target claim

**Node:** `CIRCDIST.cplx.upper`
**Current level:** `CONJECTURED`
**Length:** 301 characters, 301 UTF-8 bytes
**SHA-256:** `1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1`

```text
Eff-Preserve is in NP for every fixed constant d (schedule certificate plus polynomial fault enumeration), and in Sigma_2^P when d is part of the input (exists-schedule forall-fault with a polynomial Gaussian-elimination acceptance predicate; the distance promise handled by a total ">= d" surrogate).
```

The proof below establishes this exact sentence. Parenthetical phrases are treated as asserted proof
content, not informal motivation.

### 3.2 Current root claim, bound but not proved here

**Length:** 556 characters, 556 UTF-8 bytes
**SHA-256:** `0d9572ec3c4b58be6c824c1445c8bb6c3db76736a73aea9111d5c39586984c60`

```text
The promise decision problem Eff-Preserve (input CSS check matrices H_X, H_Z with promised static distance d, a CNOT interaction/conflict graph, and an optional depth bound T; question whether a legal schedule M with d_eff(M) = d exists) is classified with proof, comprising NP-completeness for a fixed small constant d under stated structural restrictions (bounded stabilizer weight and Tanner degree, few allowed local CNOT orders per check), and a tight polynomial-hierarchy classification (candidate Sigma_2^P-completeness) when d is part of the input.
```

### 3.3 Current classification implication, bound but not re-promoted

**Route:** `CIRCDIST.cplx#classification-assembly`
**Current level:** `PROVED`
**Length:** 220 characters, 220 UTF-8 bytes
**SHA-256:** `b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30`

```text
Membership plus fixed-d hardness gives NP-completeness for fixed d; membership plus hierarchy hardness gives the tight PH classification for input d; together they are the claimed classification. Assembly is bookkeeping.
```

Promoting the membership premise does not complete this AND-route because two premises remain
unfinished.

### 3.4 Other classification premises, bound to prevent inheritance mistakes

| node | exact claim length | UTF-8 bytes | claim SHA-256 | current level |
|---|---:|---:|---|---|
| `CIRCDIST.cplx.fixed-d` | 390 | 392 | `7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf` | `CONJECTURED` |
| `CIRCDIST.cplx.sigma2` | 113 | 113 | `9e76a1224bea068a1910bdabe189fab022282cca9a2d85df538612db79305a29` | `OPEN` |

Exact fixed-`d` claim:

```text
Eff-Preserve with a fixed small constant d is NP-complete under structural restrictions (bounded stabilizer weight, bounded Tanner degree, few allowed local CNOT orders per check) — with the restriction boundary corrected by the round-1 recon to (d = 3 with order-domain >= 3) or (d >= 4 with binary order-domain), since d = 3 with two allowed orders per check reduces to 2-SAT and is in P.
```

Exact hierarchy-hardness claim:

```text
Eff-Preserve with d as part of the input is Sigma_2^P-hard (hence, with CIRCDIST.cplx.upper, Sigma_2^P-complete).
```

Neither statement is proved or reviewed for promotion here.

## 4. Formal input, promise, and language conventions

### 4.1 Explicit input and size measure

A syntactically well-formed instance `I` contains:

1. explicit binary matrices `H_X in F_2^(m_X x n)` and `H_Z in F_2^(m_Z x n)` with a common `n`;
2. a positive integer threshold `d`, encoded in binary or unary;
3. the required single-ancilla CNOTs, one for every `1` entry of the two matrices, identified by
   sector, check-row index, and data-qubit index;
4. optional explicitly listed or polynomial-time decidable allowed local-order data; and
5. an optional positive depth bound `T`, encoded in binary or unary.

The canonical 2026-08-23 ruling fixes conflicts to qubit sharing: two CNOTs conflict exactly when
they share their check ancilla or their data qubit. If the serialized input retains a conflict-graph
field, a total parser may require it to equal this derived relation; malformed disagreement is
rejected. The upper-bound proof would also survive an explicitly represented arbitrary conflict
relation because checking its edges is polynomial, but no such variant is needed or licensed.

Let `s=|I|` be input bit length and

```text
G_X = number of 1 entries in H_X,
G_Z = number of 1 entries in H_Z,
G   = G_X + G_Z.
```

Because the matrices are explicit, `G <= (m_X+m_Z)n <= s` up to fixed serialization overhead. This
is the correct polynomial bound. It does not assume `m_X+m_Z <= n`; dependent and duplicate check
rows are allowed.

Syntactic validation checks matrix dimensions, binary coefficients, positive `d`, the CSS
commutation condition `H_X H_Z^T=0`, and the finite encodings just described. It is polynomial.
This is not the static-distance promise check.

### 4.2 Promise pair

Put

```text
S_X = row(H_X),     C_X = ker(H_Z),     L_X = C_X \ S_X,
S_Z = row(H_Z),     C_Z = ker(H_X),     L_Z = C_Z \ S_Z.
```

CSS commutation gives `S_X subseteq C_X` and `S_Z subseteq C_Z`. For `k>0`, define

```text
d_X = min{|v| : v in L_X},
d_Z = min{|v| : v in L_Z},
d_static = min(d_X,d_Z).
```

The promise is `k>0` and `d_static=d`. The promise pair is

```text
YES = {I : promise(I) and exists legal M with d_eff(M)=d},
NO  = {I : promise(I) and every legal M has d_eff(M)<d}.
```

If no legal schedule exists, a promise-satisfying instance is in `NO`. Computing or verifying
`d_static=d` is deliberately absent from the verifier.

For a promise problem, “in NP” or “in `Sigma_2^P`” is used in the standard separator sense: there
is a total language in the class that contains every promised YES instance and no promised NO
instance. The proof constructs that language explicitly. Under the equivalent promise-verifier
convention, the same machines restricted to the promise give the result.

### 4.3 The total surrogate

For every syntactically well-formed instance, including off-promise instances, define

```text
L_>= = { I : exists legal M with d_eff(M) >= d }.
```

Malformed input strings are rejected. This is a total language; no static-distance oracle is used.
Its behavior where `d_static != d`, or where `k=0` and the logical set is empty, need not agree with
the equality question because those inputs are off promise.

The rest of the proof first places `L_>=` in the two classes and then proves agreement on the
promise.

## 5. Polynomial schedule certificates

### Lemma 5.1 — every legal schedule has a polynomial encoding

Each required CNOT is already identified by an input check-row and data-qubit pair. A certificate
records either the order of the support positions for each check or, equivalently when `T` is
present, a time label for every required gate from which each local order is read. Listing support
positions costs `O(G log(n+1))` bits.

If `T` is absent, every tuple of local orders has a canonical legal realization: execute all `G`
CNOTs sequentially in the listed orders. No pair then conflicts. Global times need not be guessed.

If `T` is present, suppose a legal schedule uses occupied times
`t_1<...<t_r` in `{1,...,T}`. Replace every `t_i` by its rank `i`. Equality of times, strict temporal
order, local CNOT order, and every qubit-sharing conflict are preserved. Also `r<=G` and `r<=T`.
Thus a witness can use labels in `{1,...,min(G,T)}` and costs `O(G log(G+1))` bits even when binary
`T` has a huge numeric value. Empty layers never need to be encoded.

Combining local order and timing fields yields a polynomial certificate.

### Lemma 5.2 — schedule legality is polynomial-time decidable

The verifier checks:

1. every required CNOT appears exactly once and no other gate appears;
2. the induced order for each check is a permutation of its matrix-row support and, if an allowed
   domain is supplied, belongs to that explicitly represented or polynomially decidable domain;
3. every time is positive and at most `T` when `T` is present; and
4. no two equal-time CNOTs share a check ancilla or data qubit.

Sorting by gate ID and by `(time,qubit)` or using tables makes these checks polynomial in `s` and
certificate length. Any additional canonical measurement-consistency parity condition, if included
in “legal,” is also a finite parity check on the schedule and does not change the bound. An
implicitly specified order oracle with no polynomial membership algorithm would fail to define the
claimed ordinary decision problem; that is not the current encoding.

## 6. Polynomial extended-code construction and both CSS sectors

For a check `c` of weight `w_c` with local order
`pi_c=(q_1,...,q_w)`, put

```text
S_i(pi_c) = {q_(i+1),...,q_w},       1 <= i <= w-1.
```

Define a slot-indexed X-sector matrix `Gamma_X(M)` with `n` rows and the columns

```text
{e_q : 1<=q<=n} union
{chi_(S_i(pi_c)) : c is an X check, 1<=i<=w_c-1},
```

and define `Gamma_Z(M)` by swapping X and Z. Keeping equal columns in different slots or deduplicating
them gives the same minimum distance; the slot-indexed form makes the universal string length
input-determined. The column counts are

```text
K_X = n + sum_(X checks c) max(w_c-1,0) <= n+G_X,
K_Z = n + sum_(Z checks c) max(w_c-1,0) <= n+G_Z.
```

Hence both matrices have polynomial dimensions and can be built in polynomial time.

### Lemma 6.1 — these are exactly the relevant terminal residual generators

For an X-check ancilla, an X component after its `i`th CNOT propagates through the remaining CNOTs
to the proper suffix `S_i`. A data-side X component gives `e_(q_i)`. Their sum is the preceding
suffix `S_(i-1)`, with `S_0=supp(c)`. A preparation fault can give the full check support; that is a
row of `H_X`, hence an X stabilizer. A measurement flip gives zero terminal data residual. Z
components on the data give singleton Z residuals. The Z-check case is the exact mirror because
the ancilla is the CNOT target. Idle-data faults give singletons, and a Y component can contribute
to both sectors.

Therefore every relevant one-fault sector component is zero, a singleton, a proper suffix, or a
same-sector check row. Conversely every displayed singleton or proper suffix is realized by a
standard finite Pauli fault. Global interleaving changes syndrome records but does not change these
terminal data columns: data Paulis can propagate to later ancillas, but fresh ancillas never carry
them back to a different data qubit.

Zero columns never help. If a selected full-support stabilizer column occurs in a combination that
lands in `L_X`, deleting that column adds a vector of `S_X` and leaves the result in the same
nonzero logical coset while reducing the count. Duplicate equal columns selected twice cancel over
`F_2` and can both be deleted. Thus omitting zero/full-support columns and optionally deduplicating
preserves the minimum.

This also addresses joint faults. An undetectable nontrivial terminal Pauli `X(x)Z(z)` has
`x in L_X` or `z in L_Z`; it cannot have both components trivial. At one CNOT location at most one
sector obtains a multi-qubit hook, while the other obtains zero or a singleton. The standard full
local Pauli menu is closed under products, so multiple choices at one location can be merged without
increasing weight. Hence the extended-code minimum is the minimum of the two sector minima. This is
the Definition-1.3-prime convention already ratified in the project; the argument here is included
so the membership proof does not rely on a label alone.

### Lemma 6.2 — algebraic characterization of `d_eff`

For `sigma in {X,Z}`, let `H_sigma` be the same-type check matrix, `H_bar_sigma` the opposite-type
check matrix, and `Gamma_sigma` the matrix above. Define

```text
D_sigma(M) = min { |f| : f in F_2^(K_sigma),
                         H_bar_sigma Gamma_sigma(M) f = 0,
                         Gamma_sigma(M) f notin row(H_sigma) },
```

with `min emptyset = infinity`. Then

```text
d_eff(M) = min(D_X(M),D_Z(M)).
```

The first condition is undetectability. The second excludes the same-type stabilizer row space and
therefore says that the residual is a nontrivial logical. An extra `v!=0` test is unnecessary because
zero is always in the row space.

Dependent check rows and duplicate generators cause no problem: the definition uses row spaces,
not row-list uniqueness, and Gaussian elimination computes those spaces correctly.

### Lemma 6.3 — static-distance ceiling

Every singleton `e_q` is a column of each sector matrix. If `v` is a minimum static X logical, the
sum of the singleton columns on `supp(v)` equals `v`, so `D_X(M)<=|v|=d_X`. The mirror gives
`D_Z(M)<=d_Z`. Therefore, for every schedule and without needing to compute the distance,

```text
d_eff(M) <= min(d_X,d_Z) = d_static.
```

On the promise `d_static=d`, this yields

```text
d_eff(M)=d  iff  d_eff(M)>=d.
```

This proves the separator agreement rather than assuming the frozen common inequality.

## 7. The polynomial Gaussian-elimination predicate

Let `K=max(K_X,K_Z)`. A universal string contains a sector bit `sigma`, a `K`-bit coefficient vector
`f`, and fixed padding if the chosen complexity-machine format requires a common polynomial length.
It is well formed when every bit beyond `K_sigma` is zero. Its weight is the Hamming weight of the
first `K_sigma` bits.

For well-formed `(sigma,f)`, compute

```text
v = Gamma_sigma(M) f  over F_2.
```

Define

```text
Bad(I,M,sigma,f) :=
    (|f| < d) and
    (H_bar_sigma v = 0) and
    (v notin row(H_sigma)).
```

The row-space test may be performed by row-reducing `H_sigma` and reducing `v`, or by testing

```text
rank(stack(H_sigma,v)) > rank(H_sigma).
```

All coefficients are single bits; row operations are XOR. Matrix construction, multiplication,
Hamming-weight computation, comparison with binary or unary `d`, and Gaussian elimination take
polynomial bit time. This is one uniform deterministic predicate for all matrix sizes and all `d`.
No field elements of growing representation size occur.

To quantify over all bit strings, define

```text
V(I,M,u) := Syntax(I) and Legal(I,M) and
            (MalformedFault(u) or not Bad(I,M,decoded(u))).
```

Malformed universal choices are harmless; otherwise an irrelevant encoding could reject every
schedule. Malformed schedules are not harmless: `Legal` is outside that disjunction, so no invalid
existential string can witness membership. This placement is load-bearing.

By Lemma 6.2,

```text
d_eff(M) >= d  iff  for every universal u, V(I,M,u),
```

for every syntactically valid `I` and legal `M`.

### Large thresholds and available locations

The universal vector has length `K`, not numeric length `d`, so binary `d` causes no blow-up. If
`d>K_sigma`, every coefficient vector in that sector has weight below `d`; the predicate checks all
of them. If a logical combination exists, one is found and the schedule fails. If none exists, that
sector distance is infinity and the inequality is true. On a `k>0` CSS code, singleton columns give
a logical combination of weight at most `n`, so any `d>n` fails the surrogate for every legal
schedule. For `k=0`, both logical sets are empty and `d_eff=infinity`; accepting a legal schedule
for finite `d` is a coherent off-promise convention.

Thus thresholds larger than the number of available generator slots and both binary/unary
encodings are handled by the exact same predicate. No promise-only `d<=n` shortcut is required.

## 8. Fixed-constant `d`: NP membership

Fix any positive constant `d_0`. The NP verifier does the following on an input in the fixed-`d_0`
slice:

1. reject malformed syntax or a supplied threshold different from `d_0`;
2. guess the schedule certificate from §5;
3. verify legality;
4. build `Gamma_X(M)` and `Gamma_Z(M)`; and
5. in each sector enumerate every coefficient-vector support of cardinality
   `j=0,...,d_0-1`, rejecting if it satisfies the bad-logical predicate.

The number enumerated is

```text
sum_(j=0)^(d_0-1) binom(K_X,j) + sum_(j=0)^(d_0-1) binom(K_Z,j)
    <= 2 sum_(j=0)^(d_0-1) K^j = O(K^(d_0-1)).
```

The exponent depends on the fixed language parameter `d_0`, not on input size. Each test is
polynomial by §7, so verification after the guess is polynomial. The accepted total slice is in
NP. By Lemma 6.3 it agrees with equality Eff-Preserve on static-distance-`d_0` promise inputs.
This holds for every fixed constant, including `d_0=1`: only the empty coefficient vector is checked,
and it is trivial.

Restrictions such as bounded check weight, bounded Tanner degree, or a few explicitly represented
local orders only shrink the input family and add polynomial certificate checks; they do not weaken
membership.

## 9. Input `d`: uniform `Sigma_2^P` membership

The schedule string has polynomial length by §5. The universal string has length at most
`1+max(K_X,K_Z)` plus fixed polynomial padding by §7. `V` is deterministic polynomial time.
Therefore

```text
I in L_>=
iff exists polynomial-length M, for every polynomial-length u: V(I,M,u).
```

This is the machine definition of a uniform `Sigma_2^P` language. The threshold comparison reads
the encoded `d`; no machine, advice string, circuit family, or enumeration is specialized to its
numeric value. Optional `T` remains inside the polynomial legality predicate and adds no quantifier
alternation.

By Lemma 6.3, `L_>=` contains every promised YES instance and no promised NO instance. Eff-Preserve
with input `d` is therefore in `Sigma_2^P` as a promise problem.

## 10. Adversarial attacks and edge-case decisions

| attack or edge case | failure mode if ignored | exact disposition |
|---|---|---|
| Many dependent checks, `m_X+m_Z>n` | Historical `sum w_c <= n max w_c` can be false; take many duplicate rows. | Use `G<=explicit matrix bits`; schedule and column counts remain polynomial. |
| Binary `d` is exponentially large numerically | A padded list of `d-1` fault names is exponentially long. | Use a `K`-bit characteristic vector; compare its weight with binary `d`. |
| `d` exceeds every available slot count | A list encoding has no natural length or padding convention. | Quantify over all `K`-bit vectors; finite logical distance or infinity is decided exactly. |
| `d>n` off promise | The historical reason `d<=n` is unavailable for a total language. | No such assumption is used. Singleton columns make the answer false for `k>0`; `k=0` is coherently infinity. |
| Malformed universal string | Treating it as bad lets arbitrary padding refute every schedule. | `MalformedFault or not Bad`; malformed choices are harmless. |
| Malformed existential schedule | Treating every malformed object as harmless could create a witness. | `Legal(I,M)` is conjoined outside the malformed-fault disjunction. |
| No legal schedule | A universal statement over faults might become vacuously true for an invalid schedule. | No legal existential witness exists; total language and promised problem both answer NO. |
| Optional binary `T` with huge gaps | Literal time labels can look numerically unbounded. | Rank-compress occupied layers to at most `G`; legality and depth are preserved. |
| Tight `T` and parallel gates | Sequential normalization can destroy a valid depth bound. | Compress occupied layers, not gates; concurrency classes are preserved. |
| Qubit-sharing conflicts | Checking only same-check ancillas misses two checks using one data qubit. | Check both ancilla and data endpoints at every equal time. |
| Literal arbitrary conflict graph | Could change hardness and model identity. | Canonical parser uses derived qubit sharing. Membership would still hold for an explicit graph, but no variant is promoted. |
| Zero-weight or weight-one checks | The suffix range can underflow or invent hooks. | Use `max(w_c-1,0)`; empty or weight-one rows contribute no proper suffix. |
| Duplicate check rows or duplicate hook vectors | Counting slots might appear to lower distance. | Selecting equal columns twice cancels; a minimum uses at most one. Slot and deduplicated matrices have the same distance. |
| Full-support preparation residual | Omitting it without proof could miss a low-weight mechanism. | It lies in the same-type stabilizer row space; removing it preserves the logical coset and lowers weight. |
| Zero residual and `v!=0` | A redundant condition can conceal the real triviality test. | `v notin row(H_sigma)` already excludes zero. |
| X sector only | A Z logical can determine `d_eff`. | Build and universally check both mirror matrices; take the minimum. |
| A Y or two-qubit Pauli contributes to both sectors | Separate searches might miss a cheaper joint logical. | A nontrivial joint logical has at least one nontrivial sector; per-location propagation gives at most one hook and a singleton cross component; full Pauli closure gives the sector split. |
| Dependent stabilizer generators | Solving against a presumed basis can misclassify row-space membership. | Gaussian elimination is run on the given possibly dependent rows. |
| Off-promise `d_static>d` | Equality and `>=d` can disagree. | Allowed: `L_>=` is a separator, and agreement is claimed only when `d_static=d`. |
| Verifying the static-distance promise | This could import the hard distance problem and invalidate the upper verifier. | Never done; the promise is used only in the correctness proof. |
| `k=0` | Static distance may be undefined. | Such inputs are outside the finite-distance promise; total surrogate uses the natural empty-minimum value infinity. |
| `d=1` | “At most `d-1` faults” leaves only the empty choice. | Empty residual is in every row space, hence harmless; answer reduces to legal schedule existence as it should. |
| No required CNOTs | Time normalization and conflict loops could assume `G>0`. | The empty schedule is polynomial and legal when syntax permits; singleton columns still define `d_eff`. |
| Unary versus binary integers | A proof stated only in numeric-time complexity can be nonuniform. | All operations are polynomial in bit length; the same predicate handles either encoding. |
| Nonbinary coefficients or a larger field | Row-space and Pauli propagation formulas would change. | CSS qubits pin `F_2`; nonbinary matrix syntax is rejected. |
| Implicit allowed-order set with no decision algorithm | “Check the chosen order” would not be a polynomial predicate. | Current reading requires all orders or explicit/polynomially decidable order data; otherwise no ordinary encoded language has been specified. |
| Automatic route propagation | PROVED membership plus PROVED implication might be mistaken for a PROVED root. | The route is AND over three premises; fixed-d hardness remains `CONJECTURED`, hierarchy hardness `OPEN`, root `CONJECTURED`. |

No attack produced a counterexample to the exact claim.

## 11. Rejected proof approaches

1. **Rejecting every `d>n` solely because of the promise.** This can define a valid separator, and the
   round-59 review used that normalization, but it obscures the total surrogate's behavior. The
   characteristic-vector proof handles every threshold directly and is stronger.
2. **Encoding a fault as a list with exactly `d-1` slots.** Correct only after an off-promise cap on
   `d`; otherwise binary `d` breaks polynomial balance. Rejected in favor of `K` coefficients.
3. **Checking the static-distance promise inside the verifier.** Unnecessary and contrary to the
   reason the problem was made a promise problem. Rejected.
4. **Using only local-order tuples when a tight `T` is present.** A tuple may be unrealizable within
   `T`. Time labels and conflict checks are included.
5. **Replacing every timed schedule by a sequential one under `T`.** This can increase depth from
   `T` to `G`. Rank compression preserves concurrency instead.
6. **Treating a bad fault as merely nonzero and syndrome-free.** Stabilizers are nonzero and
   syndrome-free. Row-space exclusion is essential.
7. **Checking one CSS sector and invoking symmetry informally.** The input can be asymmetric. Both
   matrices and predicates are constructed explicitly.
8. **Assuming full-support and duplicate residuals “do nothing” without a coset argument.** Their
   removal is proved in Lemma 6.1.
9. **Inferring root completeness from this premise.** Forbidden by both logic and DAG protocol.

## Finding F-UPPER — exact membership claim

**Finding:** The unchanged 301-character `CIRCDIST.cplx.upper` claim at
`sha256:1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1` is **PROVED**.

**Scope checked:** exact claim bytes; explicit binary-matrix input size; schedule encoding;
qubit-sharing legality; absent and present optional `T`; rank compression; standard terminal
residual/hook construction; full-support and duplicate columns; both CSS sectors; dependent
checks; fixed-constant enumeration; input-`d` characteristic-vector encoding; polynomial
propagation and Gaussian elimination; malformed existential and universal choices; binary/unary
`d` and `T`; thresholds beyond available locations; static-distance ceiling; total `>=d`
separator; off-promise behavior; promise-class conventions; uniformity; and non-inheritance.

**Reason:** §§4–9 give a polynomial verifier for every fixed constant `d` and one uniform
`exists M forall f` polynomial predicate for input `d`; Lemma 6.3 proves that their total language
agrees with equality Eff-Preserve on the static-distance promise.

**Limits:** This finding is not a hardness result, a static-distance algorithm, a Circ-Preserve
result, an arbitrary-fault-model theorem, or a completion finding for `CIRCDIST.cplx`. Any change to
the exact target claim requires a new hash-bound review.

## Finding F-NO-INHERIT — unfinished classification content

After the licensed installation:

| object | licensed level |
|---|---:|
| `CIRCDIST.cplx.upper` | `PROVED` |
| `CIRCDIST.cplx#classification-assembly` implication | remains `PROVED` |
| `CIRCDIST.cplx.fixed-d` | remains `CONJECTURED` |
| `CIRCDIST.cplx.sigma2` | remains `OPEN` |
| `CIRCDIST.cplx` root | remains `CONJECTURED` |

The proof discharges only the upper premise. The classification route still lacks both hardness
premises, so no root assessment or root event is licensed.

## 12. Exact atomic canonical installation contract

### 12.1 Preconditions and write scope

The dispatcher may apply this contract only if all of the following still hold:

- target raw file SHA-256 is
  `d118923e143bc7b119a810613c91e2b3dd7e876a2365c8a70a923496a890ed3c`;
- target claim is 301 characters at
  `sha256:1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1`;
- root raw file is 7,148 bytes at
  `e5fa3667bd9dec3b36f808f927156bd060a8ffcc35ea918ff5e1d353cf558b6a`;
- classification implication remains at
  `sha256:b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30`;
- fixed-d and sigma2 claims remain at the hashes in §3.4; and
- this review exists at its commissioned path with `Finding F-UPPER`.

If any precondition fails, do not interpret or merge this contract; commission a fresh review.

Install exactly the full node bytes below. This is equivalent to replacing `assessment`, deleting
the completed `frontier` mapping, and appending the two exact `events`; it leaves the ID, role,
alias, and 301-character claim unchanged. No other canonical node or scheduler edit is licensed.

<!-- EXACT-UPPER-NODE:BEGIN -->
```yaml
id: CIRCDIST.cplx.upper
role: proof
aliases:
- EFFP-UPPER
claim: Eff-Preserve is in NP for every fixed constant d (schedule certificate plus polynomial fault enumeration),
  and in Sigma_2^P when d is part of the input (exists-schedule forall-fault with a polynomial Gaussian-elimination
  acceptance predicate; the distance promise handled by a total ">= d" surrogate).
assessment:
  level: PROVED
  caveats:
  - PROVED is bound only to the unchanged 301-character claim at sha256:1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1
    under the canonical qubit-sharing, single-ancilla CNOT Eff-Preserve model; it is about d_eff = d_ext(E(M)),
    not Circ-Preserve or d_circ.
  - The promise-class statement uses the total separator L_>= that rejects malformed syntax and otherwise asks
    whether some legal schedule has d_eff >= d. It never verifies the promised static distance. Equality with
    d_eff = d is asserted only on inputs whose CSS static distance is exactly the supplied positive d.
  - Binary or unary encodings of d and optional T are covered uniformly. The universal fault choice is a polynomial-length
    coefficient vector over the polynomial extended-column set, thresholds are compared in binary, malformed choices
    are harmless, and occupied time layers are rank-compressed to at most the number of required CNOTs.
  - This result proves membership only. It proves no fixed-d hardness, no input-d Sigma_2^P-hardness, no classification
    root, and no automatic level inheritance through CIRCDIST.cplx#classification-assembly.
  summary: Fresh strict-serial round-60 review supplies and adversarially checks a complete exact-claim proof. A legal
    schedule has polynomial encoding and verification; both CSS extended-column matrices are polynomially constructible;
    Gaussian elimination recognizes a bad low-weight X- or Z-sector mechanism; fixed d permits polynomial enumeration;
    and input d gives one uniform exists-schedule/forall-coefficient-vector predicate. The total >= d language separates
    the promise problem because singleton data columns prove d_eff(M) <= the static CSS distance for every schedule.
  basis:
    reviews:
    - path: circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md
      kind: review
      scope: Fresh independent exact-text review of the 301-character membership claim, including schedule size and
        qubit-sharing legality, optional-T normalization, the standard terminal-residual extended-code construction,
        both CSS sectors, fixed-d enumeration, uniform input-d quantifiers, Gaussian elimination, binary thresholds,
        malformed/off-promise inputs, the static-distance separator, and promise-versus-language conventions.
      locator: Finding F-UPPER
      reviewed_hash: sha256:1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1
    evidence:
    - path: circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.cplx.upper.yaml
      kind: text
      note: Immutable pre-migration record, including every original event, former summary and frontier;
        historical evidence, not an additional completion review.
    - path: circdist/artifacts/circdist_cplx_recon_20260820.md
      kind: text
      note: Historical Section 5.2 draft; its promise-only d <= n shortcut and input-size notation are repaired
        explicitly by the round-60 review rather than silently inherited.
    - path: circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md
      kind: text
      scope: Frozen Eff-Preserve promise question, common d_eff definition, and d_eff <= d_static inequality;
        the round-60 review independently derives the inequality used by the separator.
    - path: circdist/artifacts/circdist_cplx_islands_amendment5_20260823.md
      kind: text
      scope: Definition 1.3-prime and the terminal-residual extended-code/sector bridge; used as model provenance,
        with the membership predicate re-derived in the round-60 review.
    - path: circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md
      kind: text
      scope: Prior route-only review that recorded the d > n off-promise normalization, optional-T schedule encoding,
        and malformed-fault convention; corroborating evidence only, since it expressly did not adjudicate this premise.
events:
  upper-membership-reviewed-2026-08-28:
    date: '2026-08-28'
    type: review-completed
    summary: Fresh strict-serial independent review bound and proved the unchanged 301-character membership claim,
      repairing the historical proof's off-promise binary-d and input-size shortcuts and checking all schedule,
      fault, CSS-sector, Gaussian-elimination, promise, malformed-input and uniformity cases.
    sources:
    - path: circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md
      kind: review
      locator: Finding F-UPPER
  upper-membership-proved-2026-08-28:
    date: '2026-08-28'
    type: level-change
    from: CONJECTURED
    to: PROVED
    summary: Promoted only CIRCDIST.cplx.upper after exact-claim proof and independent adversarial review. The
      fixed-d hardness and input-d hierarchy-hardness premises and the CIRCDIST.cplx root remain unfinished;
      no downstream level changes by inheritance.
    sources:
    - path: circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md
      kind: review
      locator: Finding F-UPPER
```
<!-- EXACT-UPPER-NODE:END -->

The exact post-install node is 5,453 bytes at
`sha256:47260df53e4491c86e10f6ccdebadf47b1161d2533339fd9c499f389a8eb2321`.

After mechanical generated-view refresh in the validated disposable copy:

| generated view | old bytes / SHA-256 | new bytes / SHA-256 |
|---|---|---|
| `circdist/proof-dag/NODE_INDEX.md` | 1,153 / `1bde1879255297d24916b71d6ea1f69fa857b37278197258456a05700b4f5d62` | 1,148 / `102964595d79c68c16395d697df3d6eae8505a1e502661970ed5ed9d25b2a478` |
| `circdist/proof-dag/GRAPH.mmd` | 1,217 / `59c3aa68ba2b657cdfcc38e81f18ac859536ef0810b89391af2c0f3257aa82d5` | 1,212 / `0d9837f82d07cd03bcbf3e4ecca8058e735d6f000b9e647de42016ba61e8c4ae` |

Generated-view refresh is mechanical, required by protocol, and is not a second mathematical edit.
The dispatcher should run it in the same atomic installation and then run the validators in §14.

## 13. Independent semantic checks

A disposable Python program, written outside the repository from the algebra in §§4–7, exhaustively
computed row spaces, kernels, static logical sets, extended-column minima, and every threshold
predicate on 442 small CSS cases with `n=1,...,4`, including dependent rows and `k=0`. It also tested
rank compression on 1,000 deterministic random gapped schedules. The successful run printed:

```text
css_cases 442
static_bound_cases 300
k_zero_infinity_cases 142
threshold_equivalences 2379
time_compression_cases 1000
all_checks_passed
```

The 2,379 threshold comparisons included values through `n+3`, so thresholds beyond the number of
qubits were exercised. The program also included duplicate-column controls. These computations are
corroboration only; the verdict rests on the proofs above.

The first run failed before any verdict with
`AttributeError: 'int' object has no attribute 'bit_count'` because the host Python predates that
method. The script was corrected to use `bin(x).count('1')` and rerun successfully. Both attempts
and the correction are in the process ledger; no failed output is used as evidence.

## 14. Repository validation

### 14.1 Read-only baseline

All commands ran from the canonical repository with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`:

| command | result |
|---|---|
| `python3 -B tools/proof_dag_check.py --problem circdist` | exit 0; 16 node files structurally valid |
| `python3 -B tools/proof_dag_check.py --problem all` | exit 0; 85 SE, 144 ksum, 16 circdist nodes valid |
| `python3 -B tools/evidence_closure_check.py --problem circdist` | exit 0; 126 structured paths, all project-local and linked |
| `python3 -B tools/check_circdist_migration.py` | exit 0; 16 nodes, 143 original events, 728 byte-identical copies |
| `python3 -B tools/test_dag_contracts.py` | exit 0; 24 tests passed |

### 14.2 Disposable exact-contract candidate

A full repository copy outside the repository received only the exact node in §12 and a locator-bearing
placeholder at the commissioned review path. Then:

| command | result |
|---|---|
| `proof_dag_check.py --problem circdist --write-generated --previous-state <canonical>` | exit 0; prior nodes/routes/events retained; 16 nodes valid |
| `proof_dag_check.py --problem all --previous-state <canonical>` | exit 0; all three projects retained and valid |
| `evidence_closure_check.py --problem circdist` | exit 0; 127 structured paths, all project-local and linked |
| `check_circdist_migration.py` | exit 0; 16/143/728 preserved |
| `test_dag_contracts.py` | exit 0; 24 tests passed |

An all-file comparison found exactly three changed files—the target node and the two generated
views—and exactly one added file, this review path; no file was removed. Text hygiene checks found a
final newline and no trailing whitespace on each changed/added text file.

### 14.3 Negative control

In scratch only, the first nibble of the target review's `reviewed_hash` was changed from `1` to
`0`. The structural validator exited nonzero with the exact expected diagnostic:

```text
ERROR: CIRCDIST.cplx.upper.assessment.basis.reviews[0].reviewed_hash must equal sha256:1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1; the review must be bound to the current statement
```

The surrounding zsh command then attempted to assign the validator code to the reserved read-only
parameter `status`, so that shell exited before its planned restoration step. This did not touch the
repository. A separate foreground command restored the exact hash and reran the validator
successfully; the restored node returned to 5,453 bytes and the exact SHA-256 in §12. This shell
mistake is disclosed because FIX-2 accounting includes failed commands.

## 15. Limitations and no-overclaim rules

- The proof is for the current terminal-residual extended-code definition of `d_eff`, not the full
  detector-sensitive `d_circ` problem.
- The canonical legality relation is qubit sharing. Although explicit additional conflicts would
  preserve the membership upper bound, no alternate model is promoted.
- The standard finite Pauli/linear terminal-residual model is part of the problem definition. This
  report proves the complexity theorem inside that model; it is not experimental validation of a
  hardware compiler or noise model.
- Static distance is promised and never verified.
- The proof gives class membership, not an efficient practical algorithm: the fixed-`d` polynomial
  has degree depending on `d`, and the input-`d` theorem is a hierarchy upper bound.
- No hardness construction, restriction boundary, gadget, covering-radius transfer, or source-chain
  premise is checked here.
- Root and remaining premise levels stay as stated in Finding F-NO-INHERIT.

## 16. FIX-2 command, process, scratch, and mutation ledger

### 16.1 Execution model and process declaration

Exactly one reviewer session was used. No sub-agent was spawned. Every OS command was started in the
foreground and awaited. No command used `&`, `nohup`, detached mode, shell job control, a persistent
PTY session, multiprocessing, a solver, or a background driver. No network access was used. No
process is handed off.

The shell wrappers and their foreground children are completely represented by the ordered command
groups below. Ordinary short-lived shell builtins are included with their group; external children
such as `rg`, `sed`, `cat`, `python3`, `git`, and validator Python processes are named. Tool-service
infrastructure not launched by this reviewer is outside the OS-process declaration.

### 16.2 Complete executed command/activity ledger before sealing

1. `pwd`; `rg --files`; `sed` — located the repository and circdist files.
2. `rg --files` over parent paths; `rg` for FIX-2/protocol terms; `sed` — located current protocols and examples.
3. Five foreground `sed` reads — read `FILE_PROTOCOL.md`, `DAG_PROTOCOL.md`, operations README, and scheduler ranges.
4. `sed` — retried the scheduler tail range after the earlier combined output was too large.
5. `rg` — located round 60, target work item, and target node references in the scheduler.
6. Three `sed` reads — read target work item, auction, and exact round-60 commission.
7. Four `cat` processes — read upper, root, fixed-d, and sigma2 canonical nodes.
8. Two `rg | sed` pipelines — mapped headings and target terms in the frozen definition and reconstruction.
9. Four `sed` reads — read exact common-definition, Eff-Preserve, structural, and §5.2 ranges.
10. Three `sed` reads — read the prior round-59 exact review; tool output truncation was resolved by later targeted reads.
11. Three `rg` searches, two piped to `sed` — located the qubit-sharing ruling and related scope records.
12. `rg | sed` — located extended-code, residual, and sector-splitting definitions across circdist.
13. `cat` plus `rg | sed` — read the islands node and located the bridge dossier/review passages.
14. `sed` — read Amendment 5 §§1.2–1.6 exactly.
15. Three `sed` reads — read Model M, the amendment residual, and its focused review.
16. Three `cat`/`sed` reads — inspected a current direct-PROVED installation pattern and project review conventions.
17. Foreground `python3 -B` plus `git status --short` — recomputed exact file/claim/route hashes and recorded the large pre-existing dirty/untracked state; target absent.
18. Foreground `python3 -B` — created task scratch, wrote a 2,828-file manifest, and copied the repository outside `.git` into scratch.
19. `cat` wrote the disposable semantic checker; foreground `python3 -B` ran it and failed on unavailable `int.bit_count`.
20. Foreground `python3 -B` repaired only the scratch checker; a second foreground Python run passed all semantic checks.
21. Two `cat` writes created the scratch candidate node and placeholder review; foreground Python parsed and hashed the candidate.
22. Five separately awaited foreground Python validator processes ran the baseline checks in §14.1.
23. Five separately awaited foreground Python validator processes ran the candidate checks in §14.2, including generated-view refresh in scratch.
24. Foreground `python3 -B` compared every canonical/candidate file, hashed generated views, and checked text hygiene.
25. Scratch negative-control group: foreground Python changed one digest nibble; foreground validator rejected it; zsh then rejected assignment to read-only `status` and aborted the remainder.
26. Recovery group: foreground Python restored the digest; foreground validator passed; foreground Python rehashed the restored candidate.
27. `cat` wrote this report only to task scratch.

No command through item 27 wrote a repository file.

### 16.3 Sealing ledger and remaining predeclared commands

28. The first foreground Python seal checker verified the locator, exact YAML block, and exact claim
    fence, then rejected Markdown hard-break trailing spaces before copying the report. It exited by
    assertion; neither candidate nor repository was mutated.
29. One foreground Python process removed trailing spaces in the scratch report. A second foreground
    Python process rechecked the locator/YAML/claim/text hygiene and copied the full report over the
    scratch candidate placeholder; all checks passed.

30. One foreground Python process updated this scratch ledger to disclose command groups 28-29 and
    to predeclare the remaining immutable seal. No repository file was touched.

The remaining foreground-only seal is predeclared so the ledger remains complete:

31. Sync this now-final scratch report to the disposable candidate; recheck its exact YAML block and
    then rerun the candidate structural/all/evidence/migration/contract checks with the full report.
32. Compare the live repository with the initial manifest, assert protected hashes unchanged and the
    commissioned target still absent, and run a waited-for process audit.
33. Copy this finalized report exactly once to the commissioned durable path—the sole repository
    mutation authorized for this reviewer.
34. Hash and size the durable report; compare it byte-for-byte with the scratch report; verify every
    non-target repository file against the initial manifest.
35. Delete the entire task scratch tree with foreground Python `shutil.rmtree` and assert absence.
36. Run a final waited-for `ps` audit for the task slug and report artifact hash/size, validation,
    scratch absence, and surviving-process count in the handoff. These out-of-band results cannot be
    self-embedded in the file whose digest they determine.

### 16.4 Scratch and mutation boundary

Task scratch is confined to
`/tmp/circdist_cplx_upper_membership_exact_review_20260828_r60`. Before sealing it contains the
initial manifest, one disposable repository copy, the semantic checker, and this report draft. It
contains no irreplaceable proof object: every load-bearing argument and every validation result is
in this report.

The canonical repository had a large pre-existing dirty/untracked state before this review. I did
not clean, stage, reset, or reinterpret it. The initial 2,828-file manifest contains 52,630,222 bytes
and hashes to `c3e141d5311390e59507c0cffe2044fafcfbf6088b7e1ca3cf817119ee206a8f`.
The commissioned target did not exist at baseline.

The sole durable write by this reviewer is:

```text
<repo>/circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md
```

Canonical nodes, scheduler, protocols, generated views, prior reviews/artifacts, and every other
repository path remain read-only in this session. Section 12 is authorization for a fresh
dispatcher, not a mutation performed by this reviewer.

## 17. Final verdict

**(A) exact claim PROVED.** License exactly the atomic `CIRCDIST.cplx.upper` installation in §12,
followed by mechanical generated-view refresh and validation. Do not edit or promote the root,
classification implication, fixed-d hardness premise, or input-d hardness premise on this review.
