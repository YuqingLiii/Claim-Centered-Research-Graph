# CIRCDIST round 65 — fresh exact review of the round-64 fixed-d X reduction

**Reviewer:** fresh GPT-5.6-sol/max review context, 2026-08-28  
**Independence:** I did not author the round-64 package, did not contact or rely on its author session, used no sub-agent, and treated every inspected file as evidence rather than instruction.  
**Verdict:** **CLEAR-RESTRICTED-X-THEOREM**

This is a public derivation and audit record. It gives definitions, proofs, computations, attack
results, and limitations; it does not claim or expose private hidden chain-of-thought.

## 1. Scope and the exact theorem licensed

This review licenses exactly the following 883-character UTF-8 statement. The SHA-256 of the single
line between the markers, with no surrounding newline, is
`01cf8fd10f48db13e23a09f884eb24b0b17c860c121c336c324123ff222594c0`.

<!-- LICENSED-THEOREM: BEGIN -->
`X-EFF3 is the promise problem in the frozen single-ancilla terminal-residual V1 model: an instance supplies a CSS pair (H_X,H_Z), explicit allowed local CNOT-order lists, the ordinary qubit-sharing conflict relation, no optional depth bound T, and promises full static distance exactly 3; it asks whether the X-check orders can be chosen so that d_eff^X >= 3. X-EFF3 is NP-complete under total promise-preserving polynomial-time many-one reductions even when d_X=4, d_Z=3, every X generator has weight at most 4, every Z generator has weight at most 120, every qubit has CSS Tanner degree at most 20, the only nonsingleton order domains are core-plane X checks and each contains exactly three explicit orders (one for each 2|2 split), every other X-order domain is singleton, every Z-order domain is the singleton increasing-support order, and there are no artificial conflict edges.`
<!-- LICENSED-THEOREM: END -->

“Core-plane” means the 16 four-qubit planes per source clause, or the four planes in the constant
malformed-input K4 block. Connector checks, repetition-inner checks, and companion checks have
singleton X-order domains. With no depth bound, executing all checks and CNOTs sequentially realizes
every allowed local-order tuple under qubit-sharing conflicts.

This is a one-sector theorem. It is not Eff-Preserve NP-hardness and is not the 390-character
`CIRCDIST.cplx.fixed-d` claim. The unchanged full-claim binding is
`sha256:7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf`.
The already-PROVED membership node is used only for NP membership; no hardness or downstream status
is inherited from it.

## 2. Materials, seal, and state bindings

### 2.1 Sealed package

I inspected every line of all eight files in
`circdist/artifacts/circdist_cplx_fixed_d_x_reduction_round64_20260828/`. The external seal is the
hash of `SHA256SUMS.txt`:

```text
17b539c0d7d16cb85d7df083579e5f74d5fba8578f84c250f861eae8efab0a17  SHA256SUMS.txt
```

`shasum -a 256 -c SHA256SUMS.txt` returned `OK` for all seven manifest-listed payloads. The manifest
does not list itself, so the digest above is the necessary external binding.

| file | bytes | lines | SHA-256 |
|---|---:|---:|---|
| `PROCESS_LEDGER.txt` | 761 | 11 | `f859e9f6f2f12398c7245ae577535786ae5926fc1d6d2d365a341dcc3dc5599a` |
| `README.md` | 20,689 | 357 | `0606b8b6377fae42a20f606250f7186258cccbd9d04aa7a4ca288cd6371639b5` |
| `SOURCE_BINDINGS.txt` | 4,974 | 56 | `bb04df47c033d692abea9a2b0624da533fb2ea4c63873d5652b90aa2fb35946a` |
| `construction.py` | 7,635 | 206 | `4a882e62d4ba78ca8da4b9989e2433c28f9daec0a106ced9e6cfea7970daa88d` |
| `requirements.txt` | 37 | 1 | `5a41d27f1367ff315d29437fb668020a77e29b96453aece9e2c1d15ef386929b` |
| `verifier_output.txt` | 27,588 | 1,500 | `4f7c3a56dbe6307f450ff88db941902e6853e8b877bdff2d44b8be35c3a897ca` |
| `verify.py` | 4,656 | 100 | `053a581a5a0a27a07040711bcc983f64c1f9b6e8555d3806e3c747e183619e1c` |
| `SHA256SUMS.txt` | 574 | 7 | external seal above |

The package is standard-library-only. No package byte changed during this review.

### 2.2 Current protocols and canonical dependencies

I read `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, the current `circdist`, proof-DAG, reviews and operations
READMEs, `operations/circdist/SCHEDULER.yaml`, `CIRCDIST_PROBLEMS.md`, the canonical fixed-d, root,
upper and islands nodes, and the historical hook-model and Island-V failure records they reference.
The relevant current hashes are:

| object | current SHA-256 | observation |
|---|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` | matches package binding |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` | matches package binding |
| frozen problem definitions | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | matches package binding |
| `CIRCDIST.cplx.upper.yaml` | `47260df53e4491c86e10f6ccdebadf47b1161d2533339fd9c499f389a8eb2321` | matches; membership only |
| `CIRCDIST.cplx.yaml` | `e5fa3667bd9dec3b36f808f927156bd060a8ffcc35ea918ff5e1d353cf558b6a` | matches; root remains CONJECTURED |
| `CIRCDIST.cplx.islands.yaml` | `25196ae04048e64f5db785c06ebaee8768704c6b60de6aa5ae17dc57b436396a` | matches |
| `CIRCDIST.cplx.fixed-d.yaml` | `ae39fc6a159477bb6927d8a159eb7c9f899a29fd68271cdf26cb20aa7a4fac98` | post-seal round-64 link; claim unchanged |
| `operations/circdist/SCHEDULER.yaml` | `e62b7c49993873e68a80cf6dfe5a0a87dd40987f1965532b35f4142bea64282f` | post-seal round-64 settlement/round-65 authorization |

The package records earlier file hashes `405445...ac98` for fixed-d and `ab2e43...eff` for the
scheduler. That is expected temporal drift: the dispatcher linked the proposer package and then
authorized this review. I recomputed the canonical fixed-d `claim` after YAML folding: 390
characters and exactly `7adfe7...e91cf`. No mathematical statement drift occurred.

Protocol consequence: a fresh project review may bless an exact statement, but only a later
dispatcher action may install links or status changes. A completed implication never promotes an
unfinished premise or parent by inheritance.

## 3. Total source language and Karp map

### 3.1 Source theorem and syntax

The source is Tovey's `(3,4)-SAT`: every clause contains exactly three distinct variables and every
variable occurs in at most four clauses. Tovey proves this restriction NP-complete in *A simplified
NP-complete satisfiability problem*, Discrete Applied Mathematics 8 (1984), 85–89,
[DOI 10.1016/0166-218X(84)90081-7](https://doi.org/10.1016/0166-218X(84)90081-7). I independently
checked the paper scan and the [author's publication summary](https://sites.gatech.edu/craig-tovey/publications/),
which expressly records “no repeats in a clause,” easy at occurrence bound three, and hard at four.

Define a total byte-string language. Decode UTF-8; invalid UTF-8 is outside. After whitespace
splitting, require `p n m` and exactly `3m` literal tokens. `n,m` are canonical nonnegative decimal
integers (`0`, or a nonzero first digit followed by digits). Literal tokens are canonical nonzero
signed decimals; absolute indices lie in `1..n`; the three absolute indices in each clause are
distinct; global occurrence counts are at most four; no trailing token remains. A syntactically
valid string is in the language exactly when the encoded formula is satisfiable. Every malformed
string is a NO string.

The total parser must use arbitrary-length integer arithmetic or digit-string comparison. It first
counts tokens and rejects when `m > (token_count-3)/3`, before any loop indexed by `m`, and stores
occurrences only for variables actually seen. Thus a 200-digit `m` in a truncated input is rejected
in input-polynomial time, while a valid empty formula with a 200-digit `n` is accepted without an
array of size `n`. The package sentence treating “integer overflow in a bounded implementation” as
malformed must not be copied literally: rejecting a syntactically valid huge empty formula would
break completeness. This is a nonblocking implementation clarification because the abstract map
has the length-aware arbitrary-precision parser just given.

Adversarial parser run:

```text
valid_one ACCEPT m=1
valid_empty_huge_n ACCEPT m=0
huge_m_truncated REJECT
repeat_abs REJECT
leading_zero REJECT
negative_header REJECT
trailing REJECT
bad_utf8 REJECT
occurrence_five REJECT
occurrence_four ACCEPT m=4
```

### 3.2 Three total output branches

| input case | output | source/target agreement |
|---|---|---|
| malformed | three-copy transform of the fixed four-plane K4 block, direct-summed with `G_neq3` | promised X-EFF3 NO; matches source NO |
| valid, `m=0` | `G_neq3` alone, with its singleton safe X orders | promised X-EFF3 YES; the empty CNF is satisfiable |
| valid, `m>=1` | discard unused variables, renumber used variables by first occurrence, form `C_0(F)`, apply `R_3`, direct-sum `G_neq3` | YES iff `F` is satisfiable, proved below |

Unused-variable deletion preserves satisfiability. For nonempty valid input, `V<=3m`, and token
count bounds `m` by the input length. All vector coordinates, rows, and order lists are emitted by
fixed loops and XORs. Sparse output size is `O(m)`; even a dense matrix encoding is `O(m^2)`.
The optional all-pairs cap audit is `O(m^3)` bit operations. Hence every branch is a deterministic
polynomial-time promise-preserving many-one map.

## 4. Deterministic private-base construction

For a nonempty formula, let the point space have independent basis

```text
p_v                       for each used variable v,
q_t,1, q_t,2              for each clause t,
q_t,3 = q_t,1 + q_t,2.
```

The literal at position `r` uses the line
`{p_v,q_t,r,p_v+q_t,r}`. Basis support gives a complete collision classification:

1. `p_v`, `q_t,1`, and `q_t,2` are distinct basis vectors in disjoint coordinate classes.
2. `q_t,3` has the two clause coordinates for one `t`; different clauses have disjoint supports.
3. A private point `p_v+q_t,r` contains a variable coordinate and that clause's one- or two-coordinate
   tag. It is neither named nor equal to a private point with a different `(v,t,r)`.
4. Therefore the only repeated points are intended variable occurrences, the clause plane/gadget
   sharing of each `q_t,r`, and the five planes inside one gadget.

There are 16 planes per clause. Plane `i` gets a fresh independent base coordinate `b_i`; a line
`{u,v,u+v}` emits columns

```text
b_i, b_i+u, b_i+v, b_i+u+v.
```

Every column is nonzero and has base weight one. Within a plane the four point parts are distinct;
between planes the base tags differ. The XOR of two columns has base weight zero when their bases
agree and two otherwise, never the base weight one of a column. Thus there is no zero column,
duplicate column, or three-column zero sum. This is a cap proof, not a search.

The dimensions and sizes are exact:

```text
point dimension = V+2m
private bases   = 16m
D               = V+18m <= 21m
N_0             = 64m.
```

No random choice, rejection sampler, retry counter, fixed ambient dimension, or assertion is needed.
An implementation may retain the printed audit/fallback for defensive totality; the invariant above
makes the fallback unreachable on valid internal data.

## 5. CSS rows, local orders, and the weight-4 hook law

A core row is its plane's four qubits. At point `u`, its canonical `u`-pair is
`{b_i,b_i+u}`. A connector between equal-labelled pairs in planes `i,j` is

```text
{b_i,b_i+u,b_j,b_j+u}.
```

Both row types have zero column sum, so `H_X H_Z^T=0`. Duplicate `(i,j,u)` connectors are
deterministically suppressed.

For a core row emitted as `(q_0,q_1,q_2,q_3)=(b_i,b_i+u,b_i+v,b_i+u+v)`, its exact domain is
`pi_j=(q_0,q_j, then the two remaining q's in emitted-index order)` for `j=1,2,3`. These are one
canonical representative of each 2|2 split. A companion row uses the same convention and the
printed singleton choice `(0,1,0,0,0)`; a weight-2 inner row uses its emitted order. Connector
order `(b_i,b_j+u,b_i+u,b_j)` selects middle pair
`{b_i,b_j+u}`, whose syndrome is `b_i+b_j+u`. Inner and companion orders are fixed singletons.

Let `Q=F_2^N/S_X`, `lambda` be the quotient map, and `Log=ker(H_Z)/S_X`. Prefix/suffix duality is
the identity

```text
lambda(suffix_i) = lambda(prefix_i),
```

because their XOR is the check row. When `d_X>=4`, a weight-4 order has reduced hook weights
`1,2,1`; weight-2 checks have only a reduced singleton. With fault budget two, any mechanism
containing a reduced singleton has reduced weight at most three and cannot be a nonzero X logical.
The only cross-check candidate is therefore middle hook plus middle hook from two weight-4 checks.
For middle values `x,y`, it is an X mechanism exactly when

```text
H_Z x = H_Z y  and  x != y in Q.
```

Equivalently, checks selecting the same syndrome must select the same quotient class. This proves
unary safety, handles data-plus-hook and same-check pairs, and reduces X-EFF3 exactly to the stated
pair-consistency CSP. It also explains why a relation involving four middle values cannot itself
be a two-fault mechanism.

## 6. Formal-label separation and the Proposition-5 attack

### 6.1 The map

Let

```text
W = span{h} direct-sum span{r_g : g a literal gadget},
```

with all displayed generators independent. For a plane whose three point labels are `(x,y,x+y)`,
define the linear map `A:F_2^N -> W` on its disjoint qubits by

```text
A(e_b)=0,
A(e_(b+u))=x,
A(e_(b+v))=y,
A(e_(b+u+v))=x+y.
```

Every core row maps to zero. Every connector is the XOR of two equal-labelled canonical pairs, so
it also maps to zero. Hence `S_X subset ker(A)`.

For two core pairs with one syndrome, distinct displayed labels imply nonzero `A`-image of their
difference, so the difference is not in `S_X`. Conversely, equal displayed labels are connected by
the explicit within-gadget group chains, the per-point `0/h` name registry, or the clause-plane
`0` connection; complementary pairs in one plane differ by the core stabilizer. Thus equal labels
give the same quotient class. The result is the exact iff needed:

> Among core pair values at a common syndrome, quotient-class equality holds exactly when the
> displayed formal labels agree.

### 6.2 Exhaustion of other syndrome collisions

Core middle syndromes lie in the point subspace (base weight zero). A fixed connector's selected
syndrome has base weight two and equals `b_i+b_j+u`; equality with another such syndrome forces the
same unordered base pair and the same point, hence the same deduplicated connector. Repetition-inner
singletons have base weight one and are harmless by the reduced-weight law; the two inner checks of
one old qubit also represent equal quotient classes. The companion uses a disjoint syndrome block.
A zero-syndrome cross-component hook would have weight at most two and hence be a stabilizer because
both components have `d_X=4`; it cannot create a nontrivial cross-component pair.

The map survives repetition by setting `A'(e_(q,a))=A(e_q)` on all three copies: inner rows map to
zero. The exact quotient argument in Section 9 shows no old pair equality changes.

### 6.3 Old Proposition 5 is admitted, not reused

The old counterexample has four cosets of `L={0,1,2,3}` and two transverse cosets. Clean-room
enumeration gave

```text
P5 rx rz k dX dZ = (6, 5, 5, 4, 2)
P5 four_in_SX six_pair_merges = True 0
```

So the XOR of four `u`-pairs is in `S_X`, while all six pair differences are outside `S_X`.
This refutes the old Proposition-5 “only pairwise equalities” and “exactly the partition triples”
claims. The new proof never asserts `ker(A)=S_X`; four-term and other higher-arity elements of
`ker(A)` are allowed. They do not enlarge COPY/NEGATE or change either Karp direction because:

1. at fault budget two a schedule mechanism contains at most two middle hooks;
2. its syndrome must cancel pairwise; and
3. the only relevant question is equality of those two quotient classes, which `A` decides exactly.

This is a genuine bypass of the refuted proposition.

## 7. COPY/NEGATE semantics and both Karp directions

Write `0,h,r,h+r` as `0,1,2,3`, with `*` represented by `4`. The five plane triples are

```text
COPY:   (0,h,h) (0,r,r) (h,0,h) (h,h,0) (r,0,r)
NEGATE: (0,0,0) (0,h,h) (h,h,0) (h,h+r,r) (r,0,r).
```

A triple is served when at least one of its three point choices equals the selected point label.
Exhausting the `5^3` choices, with `*` standing for every outsider not printed at that point, gives

```text
COPY full satisfying triples   = (0,0,0), (h,h,r)
NEGATE full satisfying triples = (0,h,r), (h,0,h).
```

Thus COPY pins both external points to `{0,h}` and equates them; NEGATE pins and flips them. This is
an exact finite case split over a constant gadget, not evidence extrapolated from sampled formulas.

### Completeness (`F` satisfiable implies X-safe)

Set the class at `p_v` to `h` for TRUE and `0` for FALSE. A positive literal uses NEGATE; a negative
literal uses COPY. Therefore `q_t,r` is `0` exactly when that literal is true. Use the unique private
witness in the table. A satisfied clause has some `q_t,r=0`, so its `(0,0,0)` clause plane can select
that point. Each remaining plane chooses any served point. At a shared point all selected formal
labels agree; formal-label separation makes their quotient classes agree. Connector syndromes are
unique, inner checks are harmless, and the companion has its fixed safe schedule. The weight-4 law
therefore excludes every X mechanism of size one or two.

### Soundness (X-safe implies `F` satisfiable)

From a safe schedule, assign to each selected core syndrome its common quotient class. By separation
this has a unique formal label; assign `*` at an unselected point. Every plane selected one point,
so every gadget triple is served. The exact gadget case split forces every external `p_v,q_t,r`
to `0` or `h`, and enforces COPY/NEGATE. Per-point name connections identify all intended variable
occurrences. Read `v=TRUE` iff `p_v=h`. The clause plane must select one of its three points and has
formal label `0` there; the routed literal at that point is true. Every clause is satisfied.

Higher-arity stabilizer relations can shrink or correlate sums of four classes, but they cannot
make two distinct formal labels equal or allow a plane to evade its three printed disjuncts. Hence
they break neither direction.

## 8. K4 negative control and malformed totality

The malformed branch has four planes on one common line with label triples

```text
(0,0,0), (1,2,3), (2,3,1), (3,1,2).
```

At each of the three syndromes the four labels are pairwise distinct. Formal separation means two
planes cannot safely choose the same syndrome. Four checks have only three choices, so pigeonhole
gives NO. This is the true K4 obstruction, retained only as a constant negative output; the SAT
mechanism does not infer transitivity or hardness from K4.

Clean-room enumeration, independent of `verify.py`, returned:

```text
K4 rx rz k dX dZ = (4, 6, 6, 4, 2)
K4 schedules total safe = 81 0
```

After `R_3`, its distances are `(4,6)` and its X answer remains NO; direct sum with the companion
sets the full distances to `(4,3)` without repairing the K4 X obstruction. The malformed branch is
therefore a promised target NO instance.

## 9. CSS ranks, distances, repetition, and the exact X quotient

### 9.1 Main block before repetition

Every base vector `b_i` is itself a column, and subtracting it from `b_i+u` exposes every point-basis
coordinate used. Since every retained variable occurs and every clause plane exposes `q_t,1,q_t,2`,
the columns span all `D=V+18m` coordinates. Hence

```text
rank(H_Z) = V+18m.
```

There are `16m` core rows, six local connectors per literal gadget, `2(3m-V)` variable-name
connectors, and `3m` clause-point `0` connectors. Thus connector count is at most
`27m-2V` and

```text
rank(H_X) <= #X rows <= 43m-2V,
k_0 = 64m-rank(H_X)-rank(H_Z) >= 3m+V > 0.
```

The cap excludes kernel words of weights one through three, so `d_X>=4`. In every literal gadget,
take one formal-0 pair and one formal-h pair at its first point. Their disjoint four-qubit XOR has
zero `H_Z` syndrome and `A`-image `h`, so it lies outside `S_X`. Therefore `d_X=4` exactly.

Every qubit is in its plane's core row, so `ker(H_X)` has no weight-one word. Since `k_0>0`, a
Z logical exists and `d_Z(C_0)>=2` (the package needs only positivity).

### 9.2 Three-copy transform

Let `pi:F_2^(3N_0)->F_2^N_0` take parity in each three-copy block. Old X rows live on copy zero;
inner rows are `(q,0)+(q,1)` and `(q,0)+(q,2)`; each old Z row is repeated on all copies. Direct
calculation gives

```text
ker(H_Z') = pi^(-1)(ker(H_Z)),
S_X'      = ker(pi) + lift_0(S_X),
ker(H_X') = {repeat(z): z in ker(H_X)},
S_Z'      = {repeat(z): z in S_Z}.
```

The first two identities show that `pi` induces an isomorphism

```text
ker(H_Z')/S_X'  ~=  ker(H_Z)/S_X.
```

It is not merely an equality of dimensions: for any new X logical `x'`, `pi(x')` is an old X
logical and `wt(pi(x'))<=wt(x')`; lifting an old minimum logical to copy zero preserves weight.
Thus the full X quotient used by the reduction is preserved and `d_X'=d_X=4`.

The last two identities force Z words to be threefold repeats, giving
`d_Z'=3d_Z(C_0)>=6`. Ranks are

```text
rank(H_X') = 2N_0 + rank(H_X),
rank(H_Z') = rank(H_Z),
k'         = k_0.
```

### 9.3 Companion and direct sum

Independent exhaustive enumeration of the printed 12-qubit companion gave

```text
companion rx rz k dX dZ = (5, 5, 2, 4, 3)
companion witness bad_pairs = []
```

The singleton X split tuple is `(0,1,0,0,0)` in printed row order. Direct-sum ranks and logical
dimensions add, while each sector distance is the componentwise minimum. Therefore every nonempty
formula output and the malformed output has exactly `(d_X,d_Z)=(4,3)`; the empty output is the same
companion and has the same exact promise.

## 10. Uniform weights and Tanner degree

Before repetition, every X row has weight two or four. The `H_Z` coordinate rows have weights:

```text
private-base row: 4
clause-basis row: 2 + 10 + 10 = 22
variable row:     10*occ(v) <= 40.
```

Repetition triples these Z-row weights, hence at most 120, and does not increase X-row weight. The
companion has X weight four and Z weight at most six.

For Tanner degree, an old plane has one core incidence. At each of three points a plane has at most
two within-gadget chain edges, hence at most six local connector incidences. A literal plane can be
the registry hub for at most `occ(v)-1<=3` variable-name edges plus one clause-point edge; a clause
plane has at most three. Thus any plane qubit has at most ten connector incidences. Copy zero adds
two inner rows, and each H_Z column contains one base coordinate plus at most three point-basis
coordinates. The loose universal sum is

```text
1 core + 10 connectors + 2 inner + 4 Z incidences = 17 <= 20.
```

Other copies and the fixed blocks are smaller. The advertised degree 20 is therefore uniform.

The four-clause mixed-sign stress instance, with one variable at occurrence four, hit the structural
bounds as follows:

```text
instance m V P B D n0 rows0 = 4 9 17 64 81 256 154
connectors local name total bound = 72 18 90 90
CSS cap = True True
ranks rx rz k0 = 154 81 21
repetition ranks rx rz k = 666 81 21 expected_rx 666
row_weights_X_old_repmax = 4 4
row_weights_Z_old_repmax = 40 120
tanner_max total x z qubit = 11 10 1 12
formal_bad_rows pair_tests formal_bad_pairs = 0 570 0
aux_count_unique_all_noncore = 90 90 True
weight4_witness wt syndrome Aimage in_SX = 4 0 1 False
point_multiplicity_max = 20
```

## 11. Code, replay, and finite-evidence boundary

Running `python3 verify.py` in the package directory exited zero and returned 164/164 PASS. Parsing
the sealed JSON found 164 detail records, no non-PASS status, 37 formal-map row checks, and 105
actual-versus-formal pair-partition checks. Piping the fresh output directly to SHA-256 produced

```text
4f7c3a56dbe6307f450ff88db941902e6853e8b877bdff2d44b8be35c3a897ca  -
```

which is byte-identical to the sealed `verifier_output.txt`, including Python `3.9.6`.

The verifier checks the constant gadgets, a one-clause build, cap/CSS, formal pair partitions,
connector syndrome uniqueness, repetition commutation and size, companion distances/schedule, the
old Proposition-5 counterexample, and K4. `construction.py` is corroborating code, not a complete
serialized Karp implementation: it contains no total byte parser or target writer. `verify.py`
imports it, so this is a package-internal replay rather than a clean-room proof. Also, the local
variable `neq` in the K4 section is computed but not asserted; the stronger exhaustive 81-schedule
NO assertion is executed, so the dead variable changes no result.

The universal theorem rests on Sections 3–10, not on those finite tests. The tests do not prove all
formulas, all degrees, the parser, or the missing Z schedule, and neither the package nor this review
uses them that way.

## 12. Attack ledger

| attack | result |
|---|---|
| Old Proposition-5 “only/exactly” | Refuted again by an explicit four-term relation with 0/6 pair merges; new proof uses only pair separation via `A`. |
| Fixed-dimensional random placement | Removed. Independent point coordinates and one fresh base per plane give a deterministic cap in dimension `V+18m`. |
| Unintended private/named point collision | Excluded by basis-support case split. |
| Unintended equal-syndrome pair merge | Excluded universally because `S_X subset ker(A)` and distinct labels have nonzero `A` difference. |
| Equal intended labels fail to merge | Excluded by explicit connector/name chains and core complements. |
| Connector creates its own constraint | Its selected base-weight-two syndrome is unique; unary mechanisms are excluded by `d_X=4`. |
| Four-term relation becomes a schedule mechanism | Impossible at fault budget two; no pair equality or gadget disjunct is changed. |
| K4 transitivity silently reused | No. K4 is only the constant malformed NO; SAT uses the formal partition gadget. |
| Three-copy repetition changes the X quotient | No. `pi` induces the explicit quotient isomorphism and preserves X distance in both directions. |
| Cross-component zero-syndrome coupling | Any weight-at-most-two zero-syndrome value is an X stabilizer at `d_X=4`; no nontrivial cross pair. |
| Static distance inferred from only one sector | No. Repetition gives main `d_Z>=6`; companion pins exact full distance three. |
| Degree/weight grows with variable frequency | Tovey's occurrence-four bound gives Z weight 120 and name degree at most three per label. |
| Huge decimal header makes parser exponential | Avoided by token-count short circuit and arbitrary-precision/digit comparison. |
| Finite replay treated as universal proof | Rejected; replay is corroboration only. |
| Old `W=6,d_Z>=7` shortcut | Not used. Honest Z-generator bound here is 120, and effective-Z remains open. |

## 13. Exact residual and why fixed-d remains open

Static `d_Z=3` does not prove an effective Z schedule. A weight-120 Z check has many suffix hooks;
two such hook columns may sum to a nontrivial Z logical even though every static logical has weight
at least three. Neither the singleton increasing-support order nor any other uniformly bounded
per-row list is proved safe for the main repeated block.

The remaining premise is exactly:

> For every `R_3(C_0(F))`, give a polynomially emitted, uniformly bounded per-H_Z-row order list and
> one tuple with no one- or two-fault nontrivial Z mechanism; or replace `R_3` by a bounded-weight,
> bounded-degree inert-sector transform that preserves the same X quotient and has a proved safe Z
> schedule.

Until that is proved, the restricted X theorem is only a premise candidate. It proves neither
Eff-Preserve NP-hardness nor NP-completeness, changes no canonical level, and gives no license to
promote `CIRCDIST.cplx.fixed-d` or `CIRCDIST.cplx`.

## 14. Findings and verdict

### Finding F-X-EXACT

The exact theorem in Section 1 is mathematically complete. The total source language is NP-hard,
the Karp map is total and polynomial on malformed, empty and nonempty inputs, both directions hold,
the placement is deterministic, formal-label separation bypasses the old counterexample, and every
static/structural/order-domain promise is uniform. NP membership follows from the current PROVED
fixed-d membership result after restricting its fault check to the X sector.

**Verdict: CLEAR-RESTRICTED-X-THEOREM.**

### Finding F-NO-INHERITANCE

The package contains no effective-Z schedule theorem for the main `H_Z` rows. The exact fixed-d
claim and root therefore remain at their current levels. This finding is as load-bearing as the
clearance: omitting it would misstate the reviewed scope.

## 15. Planning estimates, not evidence

These numbers are planning judgments after the audit; they are not proof inputs and must not appear
as evidence levels.

| event | estimate |
|---|---:|
| restricted X theorem survives further exact scrutiny | **0.95** |
| full fixed-d claim closes through the remaining effective-Z premise for this route | **0.20** |

## 16. Dispatcher installation license

Blessed now, not installed here: a dispatcher may link **Finding F-X-EXACT** as the independent
review of the exact Section-1 restricted theorem and record task-005 as reviewed. It may also link
**Finding F-NO-INHERITANCE** and retain the effective-Z frontier. It may not change the fixed-d
claim, promote the fixed-d node or root, mark Eff-Preserve hardness proved, retire the Z premise, or
rewrite the sealed package. Fixed-d must remain honestly labelled `CONJECTURED` unless a separate
exact effective-Z theorem and its fresh review close the full claim.

## 17. Rejected audit branches and harness corrections

1. The old random cap/retry construction was rejected; the private-base proof replaces it.
2. The old Proposition-5 exclusivity statement was rejected by the explicit four-term witness.
3. The old K4-as-hardness intuition was rejected; only its constant NO consequence is used.
4. Treating fixed-word integer overflow as malformed was rejected; arbitrary-length parsing is
   required for a total Karp map.
5. A clean-room Python branch used `int.bit_count()` and exited 1 on Python 3.9 before any assertion.
   It was rerun with `bin(x).count("1")`; the successful output was
   `(rx,rz,k,d_X,d_Z)=(5,5,2,4,3)` for the companion,
   `(4,6,6,4,2)` and 0/81 safe schedules for K4, and `(6,5,5,4,2)` plus the four-term relation for
   the Proposition-5 witness.
6. A first parser harness accidentally escaped regex `\\Z` as a literal and rejected all cases.
   No result from it was used. The corrected `fullmatch` harness produced the Section-3 output.
7. Several combined read outputs were interface-clipped. Every affected file/range was re-read in
   isolated `sed` chunks; the 1,500-line verifier JSON was also parsed structurally and hash-bound.

## 18. FIX-2 process accounting and command inventory

No background or detached job, sub-agent, compute handoff, solver server, notebook kernel, or
long-lived worker was started. Every local command ran synchronously through a foreground shell and
returned before the next dependent action. No process was killed; the nonzero exits were the
expected no-`AGENTS.md` search, the pre-assertion `bit_count` compatibility failure, and P086's
expected no-live-process `pgrep` result. The web
source lookup used the read-only web tool and started no reviewer-controlled local OS process.

Before this artifact was written, 82 foreground command sessions were started. This is the complete
outer-command ledger; pipelines are explicitly marked and therefore declare their additional
foreground children.

```text
P001  pwd
P002  git status --short
P003  rg --files -g AGENTS.md ...                         [exit 1: no match]
P004  rg --files <sealed-package>
P005  rg --files | rg <protocol/fixed-d/readme patterns> [two foreground rg children]
P006  shasum -a 256 <package>/SHA256SUMS.txt
P007  shasum -a 256 -c SHA256SUMS.txt
P008  wc -lc <package>/*
P009-P019  sed reads: DAG_PROTOCOL; FILE_PROTOCOL; circdist/proof/review/operations READMEs;
           SCHEDULER; fixed-d/root/upper nodes; PROJECT.yaml
P020-P027  sed reads: both README chunks, construction.py, verify.py, SOURCE_BINDINGS,
           PROCESS_LEDGER, SHA256SUMS, requirements
P028-P031  sed re-reads: README tail and both construction chunks; cat verifier_output.txt
P032  wc -l on all current/historical model and failure inputs
P033-P038  sed reads: current READMEs, frozen problems, SAT rescope
P039  rg historical hook/Proposition-5/K4/order terms
P040  rg scheduler/protocol round-64, review, blessed/installed terms
P041-P042  sed complete prior Island-V review in two chunks
P043-P044  rg exact hook and Proposition-5/K4 terms
P045  shasum current protocols/scheduler/definitions/nodes
P046  python3 YAML claim-length/hash calculation
P047-P049  sed prior Island-V review in three isolated chunks
P050-P051  rg exact Definition-1.3/hook review locators
P052-P053  sed Island-V source construction/gadget ranges
P054-P055  sed old placement, connector, Z-bound and limitation findings
P056  rg Amendment-5 terminal-residual bridge
P057-P058  sed Amendment-5 review derivation ranges
P059-P060  rg exact hook/value law across amendment/writeup/reviews
P061  rg blessed/installed/honest terms | head             [foreground rg + head]
P062-P066  sed prefix-suffix, Lemma-V.1, its reviews, and amended bridge
P067  python3 verify.py
P068  python3 parse of sealed verifier_output.txt
P069  shasum sealed verifier_output.txt
P070  python3 mixed-sign occurrence-four structural stress audit (inline here-document)
P071  python3 clean-room companion/K4/P5 audit             [exit 1: bit_count unavailable]
P072  python3 verify.py | shasum -a 256                    [foreground python + shasum]
P073  corrected python3 clean-room companion/K4/P5 audit
P074  rg round-64/65 scheduler locators
P075  sed exact round-64/65 scheduler entries
P076  python3 parser harness with bad escaped anchor        [harness rejected]
P077  corrected python3 total-parser adversarial suite
P078  python3 COPY/NEGATE 5^3 enumeration
P079  python3 licensed-theorem length/hash calculation
P080  find sealed package -maxdepth 3 -print
P081  git status --short
P082  test review artifact absent before creation
```

The repository mutation was one `apply_patch` operation creating this file only. Post-write
validation/process-probe sessions are recorded below after execution:

```text
P083  python3 content validator: exit 0; theorem 883 characters with SHA-256
      01cf8fd10f48db13e23a09f884eb24b0b17c860c121c336c324123ff222594c0;
      all 19 required sections present; two consistent verdict-token occurrences. Its optional
      newline counter searched for the literal backslash-n and printed 0, so that subfield was
      rejected and superseded by P087; no assertion or mathematical result used it.
P084  find sealed package -type f -print | sort: exit 0; exactly the original eight files,
      no __pycache__ or other byproduct.
P085  git status --short: exit 0; same pre-existing top-level dirty/untracked shape as entry;
      circdist remains one already-untracked tree, and no tracked file changed in this review.
P086  pgrep -fl 'python3 verify.py|.../verify.py': exit 1 with empty output, the expected
      no-live-worker result.
P087  wc -lc this review before this ledger-finalization patch: exit 0; 677 lines, 35,145 bytes.
```

Total foreground command sessions: **87**. P005 and P061 each had two foreground pipeline children;
P072 had `python3` and `shasum` as two foreground pipeline children. All other sessions had the
single named utility/interpreter child (plus the execution shell). Three `apply_patch` mutations of
the same sole authorized file created it, finalized the post-write ledger, and corrected one ledger
sentence while making the canonical split representatives explicit; none started a
reviewer-controlled OS worker. The third was the last repository mutation. No OS process was
started after P087.

## 19. Repository inventory and cleanup

Repository writes by this review:

```text
circdist/reviews/circdist_cplx_fixed_d_x_reduction_exact_review_20260828.md
```

No other repository file was created, edited, removed, staged, reset, or cleaned. The repository was
already extensively dirty on entry; initial and pre-write `git status --short` agreed, and those
pre-existing changes were left untouched. A package-tree inventory after all Python imports still
contained exactly the original eight files and no `__pycache__`.

No scratch file or scratch directory was created, inside or outside the repository; cleanup is
therefore complete and vacuous. No volatile verdict-only log was discarded: every verdict-bearing
command output used above is quoted or summarized with its exact count/hash. Final live-process
accounting appears in Section 18.
