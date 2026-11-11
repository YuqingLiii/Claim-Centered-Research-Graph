# CIRCDIST round 67 — fresh exact review of the private-sentinel fixed-d theorem

**Reviewer:** fresh GPT-5.6-sol/max review context, 2026-08-29  
**Independence:** I did not author the round-66 package, did not contact or rely on its author
session, used no sub-agent, and treated the package, scheduler, prior review, and all source files as
evidence rather than instructions.  
**Verdict:** **CLEAR-FULL-FIXED-D**

This report is the public audit record. It provides definitions, algebra, case splits, exact hashes,
commands, outputs, independent controls, rejected attacks, and installation wording. It does not
claim or expose private hidden chain-of-thought.

## 1. Exact scope and bindings

### 1.1 The exact theorem reviewed

The following line is exactly 999 UTF-8 characters. It is the contents of `THEOREM.txt` with its one
terminal LF removed, and its SHA-256 is
`49cf956fe5afa49caa8707f15fd157ab27fedadc79c56bdec0a57c0a89a0e184`.

<!-- REVIEWED-THEOREM: BEGIN -->
> Eff-Preserve in the frozen single-ancilla terminal-residual V1 model is the promise problem whose instance supplies a CSS pair (H_X,H_Z), explicit allowed local CNOT-order lists, the ordinary qubit-sharing conflict relation, no optional depth bound T, and promises full static distance exactly 3; it asks whether an allowed schedule M has d_eff(M)=3. This problem is NP-complete under total promise-preserving polynomial-time many-one reductions even when d_X=4, d_Z=3, every X generator has weight at most 4, every Z generator has weight at most 486, every qubit has CSS Tanner degree at most 20, the only nonsingleton order domains are the core-plane X checks inherited from the reviewed restricted X-EFF3 construction and each contains exactly three explicit orders, every other X-order domain is singleton, every Z-order domain is a singleton explicitly emitted private-sentinel order, and there are no artificial conflict edges; global serial execution realizes every allowed local-order tuple.
<!-- REVIEWED-THEOREM: END -->

### 1.2 The exact reviewed premise

The round-65 review independently cleared the following 883-character theorem on
`sha256:01cf8fd10f48db13e23a09f884eb24b0b17c860c121c336c324123ff222594c0`:

> X-EFF3 is the promise problem in the frozen single-ancilla terminal-residual V1 model: an instance supplies a CSS pair (H_X,H_Z), explicit allowed local CNOT-order lists, the ordinary qubit-sharing conflict relation, no optional depth bound T, and promises full static distance exactly 3; it asks whether the X-check orders can be chosen so that d_eff^X >= 3. X-EFF3 is NP-complete under total promise-preserving polynomial-time many-one reductions even when d_X=4, d_Z=3, every X generator has weight at most 4, every Z generator has weight at most 120, every qubit has CSS Tanner degree at most 20, the only nonsingleton order domains are core-plane X checks and each contains exactly three explicit orders (one for each 2|2 split), every other X-order domain is singleton, every Z-order domain is the singleton increasing-support order, and there are no artificial conflict edges.

I use this exact theorem as a reviewed premise, not the round-64 author's self-assessment. I also
retain the round-65 `F-NO-INHERITANCE` boundary until the new Z theorem is proved below.

### 1.3 The unchanged target claim

The YAML-parsed, stripped canonical claim is exactly 390 characters and has
`sha256:7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf`:

> Eff-Preserve with a fixed small constant d is NP-complete under structural restrictions (bounded stabilizer weight, bounded Tanner degree, few allowed local CNOT orders per check) — with the restriction boundary corrected by the round-1 recon to (d = 3 with order-domain >= 3) or (d >= 4 with binary order-domain), since d = 3 with two allowed orders per check reduces to 2-SAT and is in P.

The exact theorem proves the first arm of that disjunctive boundary: fixed `d=3`, bounded domain
three on the Boolean-carrying checks, and singleton domains elsewhere. It does not claim the
separate `d>=4`/binary arm, and the canonical wording and the already-reviewed classification route
do not require both arms conjunctively.

## 2. Materials, package seals, and current state

I read the current `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, repository/circdist/proof-DAG/operations
READMEs, the entire 141,777-byte scheduler, the frozen problem definition and terminal-residual
model dossier, the current fixed-d/root/upper/sigma2 nodes and classification route, every file in
the round-64 package, the entire round-65 independent review, and every file in the round-66
package.

### 2.1 Round-66 seal

The external digest of the raw `SHA256SUMS.txt` bytes is exactly

```text
2c3f3e46d1eaa50989b7afed0c89c745f734039f9dae956946269314a12e75e8
```

`shasum -a 256 -c SHA256SUMS.txt` returned `OK` for all 17 listed payloads. The package contains
18 files and 133,007 bytes including the manifest itself. The checked payload hashes are:

| payload | SHA-256 |
|---|---|
| `ATTACK_LEDGER.md` | `0d2664b4954f1cdb366e8d184c1888c4e3219336e875ccadd3ae1746a78adfdb` |
| `COMMANDS.txt` | `20c06bcfad851949bc2b6cca166589b0c31c2f13803aa3814ea5683e526b3177` |
| `COUNTEREXAMPLE.json` | `d2318eeab4e87eeb964acff8eecab5db58b814d913b7dcdc5ef8a8612c5dedc9` |
| `DISPATCHER_LICENSE.txt` | `757128accebf72d598b3b9f23d370b8b058b539c067d44c6b1daccd44535c39c` |
| `FINAL_AUDIT.txt` | `8e2d9c697431911753b0206dd119ae8e8224d6a339f6607a65ec6c9ae60f084e` |
| `LICENSED_X_THEOREM.txt` | `6e722b47728b958a08fe555a6831a0cbd4f5ba855822314fa3133fc1e1b4d792` |
| `MANIFEST.md` | `16404e206d06deaf186bb18ba63db5f0de3187076413069105f5952b4bb22f41` |
| `PROCESS_LEDGER.txt` | `847f30ec3266d5444fded69a5784e30bc5c70ccf365a4798c7329b782f99e3b9` |
| `README.md` | `5c2d33dde6060649a1aa78c4be8d0761296c097e2230f1465605407b577cf028` |
| `SOURCE_BINDINGS.txt` | `cf21532e14e5f5c8ab8fbb866793fe90b2a0a499403c22fdc2e624ea5f33f1ae` |
| `THEOREM.txt` | `0b184c505c31760d7f333fdba019ea583c7686d55ab5796d126eb0dc2857f6ee` |
| `construction.py` | `4a882e62d4ba78ca8da4b9989e2433c28f9daec0a106ced9e6cfea7970daa88d` |
| `make_counterexample.py` | `5b6a8f225289e9202364a2505230bbf05327e6356b7d96fee6bdd4e33cc1630b` |
| `requirements.txt` | `1781d27a9425ff4047cea80e44547a84d1d6227f18c57f635b758e64cc43b2be` |
| `verifier_output.json` | `d5d160987d45edaed4faef0d2986115c733b54ade899d131a9d0912c27cb8165` |
| `verify.py` | `fdffcd30e30200c711308a13801909fbf30b3b20afe4697ee134007588ab2011` |
| `z_companion.py` | `5f619ed61212ebd5382f1a842fc270054cff653764fded751429fe095e0ecb8c` |

### 2.2 Round-64 and round-65 bindings

The round-64 external manifest digest is
`17b539c0d7d16cb85d7df083579e5f74d5fba8578f84c250f861eae8efab0a17`.
All seven listed payloads passed, and the package is 8 files / 66,914 bytes. The round-66
`construction.py` is byte-identical to the sealed round-64 copy. The independent round-65 review is
36,970 bytes with
`sha256:5a9cd8d600871515f85151691e24bd92b3573e9cb79ccdca697f5af01730de54`.
It contains the exact 883-character premise, not a paraphrase.

### 2.3 Current-state drift and authority

The protocols, frozen definitions, root, upper, sigma2, and round-65 review still have their bound
hashes. The current scheduler is
`b94b70fc7ee9c5c3c911a2c9b51da4ce8752f5bd4c1a687558365e0de54fd840`, and the current fixed-d
node file is `e98ba467e29b091d9ff390efcec809880a396d4880100d80b6c322960c80d06d`.
Those two raw files postdate the author seal because the dispatcher linked round 66 and authorized
round 67. The canonical claim bytes are unchanged at `7adfe7...e91cf`. The current authoritative
states at review entry were:

| object | level |
|---|---|
| `CIRCDIST.cplx.upper` | `PROVED` |
| `CIRCDIST.cplx.fixed-d` | `CONJECTURED` |
| `CIRCDIST.cplx.sigma2` | `OPEN` |
| `CIRCDIST.cplx#classification-assembly` | `PROVED` as a conditional implication only |
| `CIRCDIST.cplx` | `CONJECTURED` |

No legacy `research/circdist` file was used as canonical state.

## 3. Frozen model and the exact terminal columns

All spaces below are over `F_2`. For a CSS pair, put

```text
S_X=row(H_X),  N_X=ker(H_Z),  L_X=N_X\S_X,
S_Z=row(H_Z),  N_Z=ker(H_X),  L_Z=N_Z\S_Z.
```

For a check order `(q_1,...,q_w)`, an ancilla fault after gate `i` has proper physical suffix

```text
T_i=e_(q_(i+1))+...+e_(q_w),              1 <= i <= w-1.
```

The full support `T_0` is the check stabilizer. A data-side same-sector component contributes
`e_(q_i)`, and a joint hook/data component is

```text
T_i+e_(q_i)=T_(i-1).
```

Thus zero, data singletons, proper suffixes, and full supports exhaust a one-location sector
residual. The proper prefix `P_i=e_(q_1)+...+e_(q_i)` is quotient-equivalent to `T_i` because
`P_i+T_i` is the check row. Preparation residuals are full supports; measurement flips have zero
terminal data residual. A Z-check is the X/Z and control/target mirror. Cross-sector output of a
CNOT fault is at most a data singleton, never a second hook.

Full supports can be deleted from a candidate: adding a same-sector stabilizer does not change a
logical coset. Two copies of the same terminal vector cancel. These observations address the
full-row ambiguity and explain why prefix representatives are exact rather than a different fault
model.

The ratified terminal-residual bridge gives

```text
d_eff(M)=min(d_eff^X(M),d_eff^Z(M)).
```

At static distance three, `d_eff>=3` is exactly the absence of a one- or two-location nontrivial
logical in either sector. Static distance alone does not control a pair of long hooks; that is the
gap the sentinel transform must close.

## 4. The block-contiguous attack and raw counterexample

### 4.1 Every lifted cut

For an old Z row ordered `(q_1,...,q_W)`, let `A_t=e_(q_1)+...+e_(q_t)`, and let `R` repeat each old
bit on the three copies. In the block order

```text
(q_1,0),(q_1,1),(q_1,2),...,(q_W,0),(q_W,1),(q_W,2),
```

the prefix at cut `3t+r` is exactly

```text
r=0: R(A_t),
r=1: R(A_t)+e_(q_(t+1),0),
r=2: R(A_t)+e_(q_(t+1),0)+e_(q_(t+1),1).
```

The two inner X checks on an old qubit give copy syndrome

```text
delta(x_0,x_1,x_2)=(x_0+x_1,x_0+x_2).
```

Exact block cuts have syndrome zero. Partial cuts can cancel only at the same old qubit; equal copy
subsets cancel, while complementary subsets differ by the full repeated block. A hook/data event is
the adjacent cut. Therefore the lifted block-order question reduces to the old boundary-prefix
one/two-column CSP. Repetition transports that CSP; it does not solve it.

### 4.2 Smallest nonempty source instance

The valid formula `(x_0 OR x_1 OR x_2)` has one clause and is smallest in the source family. Its
`C_0` has `n=64`, 37 independent X rows, and 21 independent Z rows. Under increasing old-qubit
orders:

```text
row 0: [5,7,9,11,13,15,17,19,21,23], cut after 8 blocks;
row 9: [16,17,18,19],                   cut after 2 blocks.
```

The physical lifted suffixes are supported on copies of `[21,23]` and `[18,19]`; their XOR is
`R(v)` for

```text
v=[18,19,21,23].
```

Independent multiplication gives no nonzero `H_X` syndrome row. The old `H_Z` RREF pivots are

```text
[0,1,2,4,5,8,12,16,20,24,25,28,32,36,40,44,45,48,52,56,60],
```

and `v` reduces to the same nonzero support. Hence `v` is an old nontrivial Z logical, and `R(v)`
is a lifted nontrivial Z logical. The physical suffix representative has weight 12. Quotienting
each suffix by its full row gives the package's first encountered weight-24 prefix representative

```text
[15,16,17,21,22,23,27,28,29,33,34,35,
 39,40,41,45,46,47,48,49,50,57,58,59].
```

Both representatives have zero syndrome, nonzero Z quotient class, and the same class.

The raw restricted-support calculation also recomputes exactly:

```text
21/21 single-row supports: quotient dimension 0;
210 unordered two-row unions: 14 have positive quotient dimension.
```

For rows `(0,3)`, the restricted normalizer and stabilizer-intersection dimensions are 4 and 2, so
the quotient has dimension 2; `[5,7,9,10,14,15]` is a witness. For rows `(0,9)`, the dimensions are
3 and 2, so the quotient has dimension 1. This directly rejects the support-local shortcut.

### 4.3 Scope of the refutation

The package's seeded block-order control is safe on this finite formula. I reproduced it. The
package counts 606 columns because it includes 21 harmless full-support stabilizer columns; my
independent audit omits those and counts 585. Both give `safe=true`. This is evidence that the raw
witness refutes the canonical **increasing** block order, not every block order. I found no
all-orders inference in the exact theorem, and the positive construction below does not use one.

## 5. Imported X construction, repetition, and companion

The reviewed `K_X` map has three total branches: malformed strings map to the repeated K4-NO block
direct-summed with `G_neq3`; valid empty formulas map to `G_neq3`; valid nonempty formulas map to
`R_3(C_0(F)) direct-sum G_neq3`. Its private-base construction gives `d_X(C_0)=4`; repetition gives

```text
ker(H_Z^R)=pi^(-1)(ker H_Z),
S_X^R=ker(pi)+lift_0(S_X),
ker(H_X^R)={R(z):z in ker H_X},
S_Z^R={R(z):z in S_Z}.
```

Thus X quotient and distance are preserved, Z weights in the logical quotient are tripled, and
`k` is preserved. The companion has ranks `(5,5)`, `k=2`, exact `(d_X,d_Z)=(4,3)`, with
representatives `[0,1,4,5]` and `[0,1,8]`. Direct sums split normalizers and stabilizers, so every
reviewed branch before the new decoration has exact `(d_X,d_Z)=(4,3)` and static distance 3.

I do not reopen the independently cleared SAT gadget theorem here. I do independently prove below
that the new transform preserves precisely the syndrome and quotient objects that theorem uses.

## 6. The private-sentinel transform

Let `C=(H_X,H_Z)` be an output of `K_X`. For every emitted nonzero Z generator `z_r` of weight
`W_r`, set `L_r=W_r+2`, allocate disjoint row-private triples

```text
B_(r,j)=(a_(r,j),b_(r,j),c_(r,j)),  0 <= j < L_r,
```

and define

```text
u_(r,j)=a_(r,j)+b_(r,j),
v_(r,j)=a_(r,j)+c_(r,j),
g_(r,j)=a_(r,j)+b_(r,j)+c_(r,j),
tilde(z_r)=z_r+sum_j g_(r,j).
```

The new X rows are the old rows and all `u,v`; the new Z rows are all decorated rows and all `g`.
The reduction's emitted Z rows are nonzero: base-coordinate rows have weight four, every retained
point coordinate occurs, the K4 coordinate rows are nonzero, and all companion rows are nonzero.
Thus the implementation's `W>=1` assertion is total on every reduction branch.

### 6.1 CSS commutation

Old X rows miss all markers and commute with `z_r`. A marker X row meets its own `g` in two qubits
and its decorated row in the same two qubits; it misses every other Z row because marker families
are private. Every intersection is even. This proves CSS commutation without a row-independence
assumption.

### 6.2 Exact row spaces and ranks

The row operation

```text
tilde(z_r)+sum_j g_(r,j)=z_r
```

gives the direct row-space decompositions

```text
S_X' = S_X direct-sum (direct sum over blocks span{ab,ac}),
S_Z' = S_Z direct-sum (direct sum over blocks span{abc}).
```

If `L=sum_r L_r`, this yields

```text
n'=n+3L,
rank(H_X')=rank(H_X)+2L,
rank(H_Z')=rank(H_Z)+L,
k'=k.
```

These formulas remain valid with duplicate or dependent emitted old rows. My independent control
added a duplicate companion Z row and a nonzero dependent row. The old list then had 9 emitted rows
of rank 5; with `L=66`, the transformed ranks were exactly `(137,71)`, `k=2`, CSS held, and the
579-column Z audit was safe.

### 6.3 Both logical-quotient isomorphisms and distances

On one triple,

```text
ker[abc]=span{ab,ac},
ker[ab;ac]=span{abc}.
```

Consequently

```text
N_X' = N_X direct-sum (direct sum span{ab,ac}),
N_Z' = N_Z direct-sum (direct sum span{abc}).
```

Quotienting by the row spaces cancels the marker summands and gives canonical isomorphisms

```text
N_X'/S_X' ~= N_X/S_X,
N_Z'/S_Z' ~= N_Z/S_Z.
```

Every marker component of a normalizer is a marker stabilizer, so it can be removed without
altering old support. Conversely an old minimum logical extends with zero marker support. Therefore

```text
d_X(D_Z(C))=d_X(C)=4,
d_Z(D_Z(C))=d_Z(C)=3,
```

and full static distance remains exactly 3. This is an equality proof in both directions, not a
rank-only inference.

## 7. Exact singleton orders and marker-path lemmas

For old support `(d_0,...,d_(W-1))` in increasing emitted-qubit order and `L=W+2`, the decorated Z
row's sole order is

```text
a_0,a_1,
a_2,d_0,a_3,d_1,...,a_(W+1),d_(W-1),
b_0,c_0,b_1,c_1,...,b_(L-1),c_(L-1).
```

Each marker Z row uses `(a_j,b_j,c_j)`. For total X-order emission I fix the displayed orders
`(a_j,b_j)` for `u_(r,j)` and `(a_j,c_j)` for `v_(r,j)`. The package code does not serialize a
whole target instance, but these singleton lists make the mathematical emitter literal. Either
orientation of a weight-two row has a singleton reduced hook, so no argument depends on this
tie-break.

For marker vector `x` on one triple, define

```text
kappa(x)=(x_a+x_b,x_a+x_c),
alpha=(1,1), beta=(0,1), gamma=(1,0).
```

The complete proper-prefix state path has an explicit closed form:

1. after `a_0`, blocks `{0}` are `alpha`;
2. after `a_1`, blocks `{0,1}` are `alpha`;
3. after `a_(i+2)` and again after the following `d_i`, blocks `{0,...,i+2}` are `alpha`;
4. after `b_j`, blocks `<j` are zero, block `j` is `beta`, and blocks `>j` are `alpha`;
5. after `c_j`, blocks `<=j` are zero and blocks `>j` are `alpha`.

The last `c_(L-1)` is the full row endpoint and is not a proper prefix.

### M1 — no zero proper state

Every opening state contains an `alpha`. During closing, either a later `alpha` or the current
`beta` remains until the excluded final endpoint. Thus every proper decorated hook is detected by
some marker X row.

### M2 — exact repeated states

Opening states are strictly increasing initial segments except that an old data gate changes no
marker bit. Closing states are distinguished by the first nonzero block and whether it is `alpha`
or `beta`. A nonempty initial `alpha` segment cannot equal a nonempty terminal `alpha` segment, and
no opening state contains `beta`. Therefore two distinct proper prefixes have equal marker syndrome
iff they are the two adjacent cuts after `a_(i+2)` and after `d_i`. Their marker vectors are
identical and their old projections differ by exactly `e_(d_i)`.

### M3 — singleton-block states

Exactly three proper cuts have marker syndrome in one block: after `a_0` (`alpha` in block 0, old
projection zero), after `c_(L-2)` (`alpha` in the last block, old projection `z_r`), and after
`b_(L-1)` (`beta` in the last block, old projection `z_r`). No such state is `gamma`.

I enumerated these formulas independently for every `W=1,...,120`, the full weight range used by
the reduction: 29,640 proper prefixes, exactly 7,260 expected duplicate-state groups, and exactly
360 singleton-block states. There was no extra equality or endpoint case.

## 8. Complete one/two-location Z classification

Modulo full-support stabilizers, the nonzero terminal columns are:

| type | column |
|---|---|
| `D_o` | old-data singleton |
| `D_m` | marker-data singleton |
| `G` | proper marker-row hook, represented by prefix `a` or `a+b` |
| `R` | proper decorated-row hook |

Joint CNOT hook/data errors are adjacent prefixes by Section 3, so this table is exhaustive.

### 8.1 One column

An `R` column has nonzero marker syndrome by M1. A nonstabilizer `D_m` or `G` column has nonzero
marker syndrome. A `D_o` column cannot be a nontrivial old Z logical because `d_Z=3`. No one-column
mechanism exists.

### 8.2 Two decorated hooks

Different source rows have disjoint private marker syndrome, so they cannot cancel. For the same
row, cancellation forces the M2 adjacent pair; its XOR has zero marker part and old part one data
singleton. Static `d_Z=3` excludes a nontrivial logical. This includes boundary cuts: the full row
is a stabilizer, and the final proper cut still has the nonzero `beta` state.

### 8.3 Decorated hook plus old data

Old data has zero marker syndrome and M1 makes the decorated syndrome nonzero. The pair is detected.

### 8.4 Decorated hook plus marker-only column

A marker-only column occupies one block. Cancellation is possible only at an M3 state in that same
block. Equal `kappa` values differ by an element of `ker(kappa)=span{abc}`. Completed blocks are
also full `abc` stabilizers. The residual old part is zero or the full old generator `z_r`, so the
entire undetected pair lies in the new Z stabilizer space. A marker check can cancel a main-hook
syndrome only in this harmless endpoint configuration.

### 8.5 No decorated hook

Marker columns in different blocks have disjoint nonzero syndrome. In one block, equal syndrome
means their XOR is zero or `abc`, a stabilizer. Marker plus old data is detected. Two old-data
columns cannot be a nontrivial logical at static `d_Z=3`.

This exhausts all one/two-location cases, including cross-row overlap on old data, dependent/full
rows, preparation residuals, and joint CNOT residuals. Therefore the emitted Z tuple has
`d_eff^Z>=3`. The preserved companion logical `[0,1,8]` is three ordinary old-data columns, so
`d_eff^Z<=3`; hence `d_eff^Z=3` exactly.

### 8.6 Independent pair table

On the decorated companion, my implementation enumerated 450 nonstabilizer columns and all 101,025
unordered pairs. There was no bad singleton and no logical undetected pair. The counts below expose
the cancellations rather than reporting only a Boolean:

| pair type | all pairs | undetected | nontrivial logical |
|---|---:|---:|---:|
| `D_m+D_m` | 11,628 | 0 | 0 |
| `D_m+D_o` | 1,836 | 0 | 0 |
| `D_m+G` | 15,606 | 102 | 0 |
| `D_m+R` | 27,999 | 21 | 0 |
| `D_o+D_o` | 66 | 0 | 0 |
| `D_o+G` | 1,224 | 0 | 0 |
| `D_o+R` | 2,196 | 0 | 0 |
| `G+G` | 5,151 | 0 | 0 |
| `G+R` | 18,666 | 21 | 0 |
| `R+R` | 16,653 | 0 | 0 |

The 144 undetected pairs are precisely stabilizer coincidences. This table is corroboration of the
universal case proof, not an extrapolation.

## 9. Preservation of the reviewed X theorem

### 9.1 Old syndrome and quotient relations

For an old X residual `x`, a decorated row measures

```text
<x,tilde(z_r)>=<x,z_r>,
```

and every marker Z row measures zero. Hence two old values have equal new syndromes iff they had
equal old syndromes. From the direct row-space decomposition, two old vectors differ by a new X
stabilizer iff they differ by an old X stabilizer. Both the syndrome partition and quotient
partition are therefore preserved in both directions; there is no accidental old logical or
stabilizer relation.

Every old X row, its local-order domain, and every old terminal value is unchanged. Consequently an
old unsafe pair remains unsafe after decoration.

### 9.2 New marker X hooks and data columns

A new marker X row has weight two. Modulo its full row, its only proper hook is a marker singleton;
all new marker data columns are also singletons. An old row has weight at most four, so every old
proper hook has a representative of weight at most two modulo its full row. Therefore:

* new singleton plus old data/hook has a representative of weight at most three;
* two new singletons have a representative of weight at most two.

Since the transformed code has `d_X=4`, no such undetected sum is a nontrivial X logical. Adding a
full-support stabilizer changes nothing. Thus a safe old tuple remains safe, and together with the
previous paragraph:

```text
old X tuple is safe  iff  its singleton marker-X extension is safe.
```

This is valid for every allowed old tuple, not only a satisfying witness.

### 9.3 Independent controls

I exhaustively checked all `3^5=243` companion X tuples. Exactly 144 were safe before decoration,
exactly 144 were safe afterward, and there were zero iff mismatches. On the one-clause-plus-companion
branch, I compared 582 old values comprising every old data singleton and every nonempty proper
subset of every old X row. The new/old syndrome partitions had 138 classes, the quotient partitions
had 160 classes, both maps were bijective, and 1,521 new marker singletons created zero pair attacks.

## 10. Uniform constants, total emission, and schedule realizability

Before decoration, the reviewed output has `w_X<=4`, `w_Z<=120`, and Tanner degree at most 20. A
decorated row has

```text
W+3(W+2)=4W+6 <= 486
```

qubits. Marker Z rows have weight 3 and marker X rows weight 2. Old-qubit incidences are unchanged.
A marker `a` meets two X and two Z rows, total degree 4; `b,c` meet one X and two Z rows, degree 3.
Thus `w_X<=4`, `w_Z<=486`, and Tanner degree `<=20` are exact uniform bounds.

For a valid nonempty source with `m` clauses and `V<=3m`, `C_0` has 64m qubits and at most
`V+18m<=21m` emitted Z rows. Each old column has at most four Z incidences. After repetition and the
companion,

```text
sum_r W_r <= 768m+37,
number of Z rows <= 21m+7,
L=sum_r(W_r+2) <= 810m+51.
```

The transform adds at most `3L<=2430m+153` qubits. Every sparse matrix, row list, and explicit order
list therefore has linear size in `m`; dense output is still polynomial. Every order length is at
most 486. Core X checks have exactly three explicit orders, and every other domain is the literal
singleton fixed above. The malformed and empty branches are constant size.

The package's Python is a proof checker/builder, not a serialized total Karp writer. That is an
implementation boundary, not a mathematical gap: all emission loops and tie-breaks are explicit,
and the already-reviewed source parser uses arbitrary-precision/token-count guards. In particular,
a huge valid empty-formula header is not rejected for fixed-word overflow.

There is no `T` and no artificial conflict edge. Given any allowed local-order tuple, prepare,
execute, and measure one complete check circuit at a time in emitted order. This globally serial
schedule respects every local order and every ordinary qubit-sharing conflict. Thus local choices
are never made inconsistent by global timing.

## 11. Total Karp reduction and NP membership

Let `K_X` be the exact reviewed total map and define

```text
K=D_Z o K_X.
```

The source language is the total byte-string version of Tovey `(3,4)-SAT`: malformed strings are
NO; a valid formula has three distinct variables per clause and occurrence at most four. The
parser checks token count before any loop indexed by a header and uses arbitrary-length integer or
digit-string comparisons.

### 11.1 Malformed strings

`K_X` emits `R_3(K4-NO) direct-sum G_neq3`. The old K4 X obstruction has zero safe choices among
81 tuples; decoration preserves it by the X iff. Static parameters remain `(4,3)`, and the new Z
tuple is safe. Therefore the target is a promised NO instance.

### 11.2 Valid empty formulas

`K_X` emits `G_neq3`. Its fixed X tuple is safe; its decorated extension is X-safe by the iff and
Z-safe by Section 8. The companion logical gives `d_eff=3`, so the target is YES, matching the
empty CNF.

### 11.3 Valid nonempty formulas — completeness

If `F` is satisfiable, the reviewed reduction supplies an old tuple with `d_eff^X>=3`. Extend it
by the new singleton X domains and the unique Z tuple. Sections 8 and 9 give both sector distances
at least 3. Sector splitting gives `d_eff>=3`; the three-data-column companion logical gives
`d_eff<=3`. Hence `d_eff=3` and the target is YES.

### 11.4 Valid nonempty formulas — soundness

If `F` is unsatisfiable, every old X tuple has a one/two-column nontrivial mechanism. Every target
tuple restricts to one old tuple, and the exact syndrome/quotient embeddings preserve that
mechanism. Hence every target tuple has `d_eff^X<3`, so none has `d_eff=3`. The target is NO.

Every branch halts, emits a promised instance, and has polynomial output. This is a total
promise-preserving many-one reduction, so the restricted problem is NP-hard.

NP membership is exactly the fixed-`d` specialization of current PROVED
`CIRCDIST.cplx.upper`, claim hash
`1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1`.
With `d=3`, a verifier guesses the polynomial local-order certificate, checks explicit-domain and
qubit-sharing legality, constructs both polynomial terminal-column matrices, and enumerates all
coefficient supports of size 0, 1, or 2. Gaussian elimination decides syndrome zero and row-space
nonmembership. The total `>=3` separator agrees with equality on the promised static-distance-3
instances. Bounded weights, degrees, explicit domains, and absent `T` only restrict this PROVED
input class. Combining membership and hardness proves the exact 999-character theorem.

## 12. Why the theorem entails the canonical claim

The theorem supplies all restrictions conjunctively, with absolute constants:

| canonical phrase | exact theorem witness |
|---|---|
| fixed small constant | `d=3` |
| bounded stabilizer weight | `w_X<=4`, `w_Z<=486` |
| bounded Tanner degree | degree `<=20` |
| few local orders | cardinality 1 or 3 |
| corrected `d=3` boundary | core domains exactly 3; no binary-hardness claim |
| NP-complete | total promise-preserving Karp hardness plus PROVED fixed-d NP membership |

The exact theorem is therefore stronger and more explicit than the unchanged 390-character claim
within its `d=3` arm. It changes neither the claim bytes nor the restriction boundary. It proves no
result for `d=3` with two orders, no separate `d>=4` binary theorem, no `d_circ` result, no optional
depth-bound theorem, and no arbitrary-conflict-graph theorem.

This closes only `CIRCDIST.cplx.fixed-d`. The root route still has the OPEN
`CIRCDIST.cplx.sigma2` premise. `CIRCDIST.cplx` must remain `CONJECTURED`; the PROVED conditional
classification-assembly implication does not propagate a level, and there is no inheritance.

## 13. Code, manifests, and exact replay

The round-66 code imports only one another and the Python standard library. It launches no
subprocess or network operation. I copied both sealed packages outside the repository and ran with
`PYTHONDONTWRITEBYTECODE=1`.

```text
PYTHONDONTWRITEBYTECODE=1 python3 make_counterexample.py > counterexample.rebuilt.json
cmp COUNTEREXAMPLE.json counterexample.rebuilt.json
```

Result: byte-identical, SHA-256
`d2318eeab4e87eeb964acff8eecab5db58b814d913b7dcdc5ef8a8612c5dedc9`.

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify.py > verifier.replayed.json
```

Result: byte-identical on Python 3.9.6, `verdict=PASS`, 20/20 individual `PASS`, SHA-256
`d5d160987d45edaed4faef0d2986115c733b54ade899d131a9d0912c27cb8165`.
The checks cover exact texts, companion parameters/witnesses, one-clause shape and low-Z search,
the increasing-order failure, exact raw JSON rebuild, the all-orders caveat, transform ranks/CSS,
marker paths, exact one/two-column Z audits on three branches, constants, old-X partitions, K4,
and the grouped-opening negative control.

The round-64 replay was also byte-identical: `PASS`, 164/164, Python 3.9.6, SHA-256
`4f7c3a56dbe6307f450ff88db941902e6853e8b877bdff2d44b8be35c3a897ca`.

I parsed every scalar in the three raw JSON outputs: 737 leaves in `COUNTEREXAMPLE.json`, 297 in
the round-66 verifier output, and 724 in the round-64 output. Finite agreement is corroboration;
Sections 3–12 are the universal proof.

## 14. Independent controls and rejected attacks

I wrote a separate 472-line / 18,611-byte standard-library checker outside the repository. It
imports none of the package implementation. Its SHA-256 was
`5df396bc4bb733c750f10dc4441483a3cbf459b1c27f9815d0677d6f202f2431`.
It exited zero in 1.29 seconds and produced JSON/stdout SHA-256
`04c215722adba12e824451e7b755df5362dbc5126e7b32d67ea6569b7ea1d69d`.

| attack/control | result |
|---|---|
| Rebuild raw rows, cuts, syndromes, row spaces | exact; old logical `[18,19,21,23]`, physical lifted suffix weight 12 |
| Recompute all restricted row unions | 0/21 single obstructions; 14/210 pair obstructions |
| Treat increasing-order witness as all-orders | rejected; seed-0 tuple is safe on this finite instance |
| Exhaustive M1–M3 over all used row weights | 29,640 prefixes, no discrepancy |
| Companion private transform | `(n,L,r_X,r_Z,k)=(165,51,107,56,2)`, 450-column Z audit safe |
| Duplicate/dependent emitted Z rows | rank identities, `k=2`, CSS, and 579-column Z audit all pass |
| Every companion X tuple before/after | 243 checked, 144 safe each side, zero iff mismatch |
| One-clause old-X partition and new singleton attack | 582 old values, 1,521 marker singletons, zero split/merge/attack |
| Marker check cancels a main hook | only 42 companion `R+(D_m or G)` undetected pairs; all stabilizers |
| Group all openings before old data | rejected as unsafe; exposes `[0,1,8]` |
| Share marker families across rows 2,4,5 | still CSS but unsafe; hooks at cuts 8 of rows 4 and 5 expose `[0,2,5,6]` |

The shared-family mutation is a new negative control. It shows that row privacy is load-bearing,
not cosmetic. The dependent-row positive control separately shows that privacy does not require
old generator independence.

Implementation limitations are explicit and nonblocking: there is no serialized total parser or
target writer; `sentinel_state_audit` checks M1/M2-style path properties but not the full M3
consequence by itself; and finite exact-distance enumeration is impossible on the largest output.
The proof supplies the total parser contract, literal order emitter, M3 derivation, and quotient
isomorphisms. No conclusion relies on filling those proof obligations by finite extrapolation.

## Finding F-FULL-FIXED-D

The complete 999-character theorem at
`sha256:49cf956fe5afa49caa8707f15fd157ab27fedadc79c56bdec0a57c0a89a0e184` is correct under the
frozen single-ancilla terminal-residual V1 model. The private-sentinel transform is polynomial and
total on every reviewed reduction branch; preserves CSS, rank, `k`, both logical quotients and
exact `(d_X,d_Z)=(4,3)`; has the stated universal safe Z orders; preserves the reviewed X-safe iff;
meets `w_X<=4`, `w_Z<=486`, Tanner degree `<=20`, explicit absolute order-domain bounds, ordinary
conflicts and serial realizability; and composes with the reviewed total Karp map and PROVED NP
upper bound.

The theorem entails the unchanged canonical 390-character claim at
`sha256:7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf` through its `d=3`,
domain-three arm.

## Finding F-NO-INHERITANCE-R67

This review proves no hierarchy-hardness result. `CIRCDIST.cplx.sigma2` remains `OPEN`, so
`CIRCDIST.cplx` remains `CONJECTURED`. Neither the PROVED classification implication nor this
fixed-d finding licenses a parent-level change.

## 15. Exact dispatcher installation license

**Blessed now, not installed here.** Subject only to confirming that the three exact statement
hashes above are still unchanged at installation time, the dispatcher is licensed to make one
fixed-d completion update. The sole evidence-level change authorized by this report is:

```text
CIRCDIST.cplx.fixed-d: CONJECTURED -> PROVED
```

The dispatcher must not change the fixed-d claim text. It must retain the round-66 author package
as evidence and add this review under `assessment.basis.reviews` with exactly:

```yaml
- path: circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md
  kind: review
  scope: >-
    Fresh independent exact review of the sealed round-66 999-character private-sentinel theorem,
    including the raw block-order counterexample and caveat, terminal-column model, M1-M3 and every
    one/two-fault Z case, CSS/rank/k and both quotient isomorphisms, exact distances, preservation of
    the independently reviewed X-safe iff, uniform constants and explicit order semantics, total
    malformed/empty/nonempty Karp branches, NP membership, theorem-to-claim entailment, independent
    controls, and the no-inheritance boundary.
  locator: Finding F-FULL-FIXED-D
  reviewed_hash: sha256:7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf
```

Its updated summary must say that the exact 999-character theorem was independently cleared and
entails the unchanged claim, while the root remains unfinished because sigma2 is open. The
dispatcher may add caveats binding PROVED to the exact theorem/model and stating that the
disjunctive restriction boundary is met through the `d=3` arm only.

Both active node frontier entries `task-002` and `task-006` are completed and must be removed; if
no frontier remains, remove the `frontier` key. Do not erase their historical events or the held
scheduler records.

Append these two research events, with the existing author evidence and this review both linked:

```yaml
fixed-d-private-sentinel-reviewed-round67-2026-08-29:
  date: '2026-08-29'
  type: review-completed
  summary: >-
    Fresh independent round-67 exact review cleared the complete 999-character private-sentinel
    theorem on sha256:49cf956fe5afa49caa8707f15fd157ab27fedadc79c56bdec0a57c0a89a0e184
    and proved that it entails the unchanged 390-character fixed-d claim on
    sha256:7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf.
  sources:
  - path: circdist/artifacts/circdist_cplx_fixed_d_z_companion_round66_20260829
    kind: run
  - path: circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md
    kind: review
    locator: Finding F-FULL-FIXED-D

fixed-d-proved-round67-2026-08-29:
  date: '2026-08-29'
  type: level-change
  from: CONJECTURED
  to: PROVED
  summary: >-
    Promoted only CIRCDIST.cplx.fixed-d after the sealed author theorem and fresh independent exact
    review completed the d=3/domain-three fixed-d NP-completeness claim. CIRCDIST.cplx.sigma2 remains
    OPEN and CIRCDIST.cplx remains CONJECTURED; no parent level is inherited.
  sources:
  - path: circdist/artifacts/circdist_cplx_fixed_d_z_companion_round66_20260829
    kind: run
  - path: circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md
    kind: review
    locator: Finding F-FULL-FIXED-D
```

Operationally, the dispatcher may settle scheduler action
`CIRCDIST.cplx.fixed-d@task-006-private-sentinel-exact-review`, set the scheduler's fixed-d mirror
to `PROVED/P=1`, move the action out of the ranked active set, spend the authorized round-67 box,
and reprice. The scheduler remains noncanonical. It may regenerate derived views and run the normal
structural/evidence/migration validations after the atomic node update.

No other node or route level is licensed. In particular:

```text
CIRCDIST.cplx.upper: unchanged PROVED
CIRCDIST.cplx.sigma2: unchanged OPEN
CIRCDIST.cplx#classification-assembly: unchanged PROVED conditional implication
CIRCDIST.cplx: unchanged CONJECTURED
```

## 16. FIX-2 process accounting, repository inventory, and cleanup

No sub-agent, detached job, background job, daemon, worker pool, solver server, notebook kernel,
compute handoff, or external mathematical worker was started. Every command was foreground and
awaited. All verdict-bearing computation has completed. A few tool batches launched independent
read-only shells concurrently; they were foreground/awaited, not detached, and are declared below.

### 16.1 Foreground command ledger through review creation

The desktop execution wrapper starts a foreground login shell plus the named direct children.
This is the complete semantic command ledger; ranges marked `R` are concurrent but fully awaited
read-only calls.

```text
P001-P006  repository/AGENTS/file/route reconnaissance; initial git status; package and target hashes.
R01        four read-only shells: DAG_PROTOCOL, FILE_PROTOCOL, CIRCDIST, CONTRIBUTING.
R02        five read-only shells: current circdist README and fixed-d/root/upper/sigma2 nodes.
P016-P021  frozen definitions, size inventory, full round-66 README, full round-65 review in chunks.
R03        four read-only shells covering every round-64 file.
R04        three read-only shells covering round-66 manifests, ledgers, exact texts and seals.
R05        three read-only shells covering all round-66 Python source.
P032       frozen-model locator scan.
R06        three read-only shells for the exact model/joint-residual/bridge ranges.
P036       Python exact theorem/X-theorem/canonical-claim length and hash binding.
R07        two concurrent foreground shasum verification shells, one per sealed package; both passed.
P039       Python scratch creation and copy of both packages outside the repository.
P040       foreground raw-counterexample rebuild/cmp/JSON/hash.
P041       foreground round-66 verifier replay and full 20-record inspection (14.0 s).
P042       foreground round-64 verifier replay/cmp and full 164-record inspection.
P043       Python full JSON leaf walk over all three sealed raw outputs.
P044       exploratory shared-marker mutation using package algebra; superseded by P046.
P045       scratch checker inventory/hash.
P046       independent no-package Python audit (1.29 s), writing only external scratch.
P047       read/hash of independent output.
P048-P050  scheduler chunk reads, full-byte YAML parse, and current operations/proof-DAG READMEs.
P051       current protocol/definition/node/review hashes.
P052       upper-review locator scan; an unquoted backtick in the shell pattern attempted one extra
           foreground child named `d`, which exited 127. The rg/sed read still completed; no result
           depends on the failed child, and P053 reread the exact ranges safely.
P053       exact upper-membership proof ranges.
P054       classification-route restriction/order-domain locator scan.
P055       package file/byte inventory.
P056       raw-certificate row/cut/pivot/union summary.
P057       authorized review-target absence and package-count check.
P058       package import/subprocess/network scan.
P059       Python pre-write detailed git-status hash; its sole foreground subprocess was `git status`.
```

The `apply_patch` calls that created the external scratch checker and this sole review file were
tool mutations, not reviewer-controlled OS workers. No command used `&`, `nohup`, `disown`, `tmux`,
`screen`, or a detached subprocess. No process was interrupted or killed because every computation
finished normally.

### 16.2 Repository and scratch state before final audit

The repository was already extensively dirty/untracked on entry. Immediately before creating this
review, `git status --short --untracked-files=all` had 1,470 entries; after excluding the authorized
review path, its byte hash was
`21cb5376b561f96ccfb83aa713e1212018b2d2ff3083f31f92c381518c0b2ed0`.
No pre-existing change was staged, reset, cleaned, edited, or adopted.

Repository writes by this review are restricted to exactly:

```text
circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md
```

All scratch is under `/tmp/circdist-round67-review-20260829` and will be deleted after the final
content/validation checks. The sealed packages were executed only from their scratch copies, so no
`__pycache__` or replay output was written into either repository package. The post-write
validation, final process scan, scratch deletion, and final inventory are recorded below after they
run.

### 16.3 Post-write final audit

The post-write phase used only the following foreground, fully awaited processes:

```text
P060       Python review existence/length/hash/required-marker check and tail read.
P061-R08   proof_dag_check.py --problem circdist (one of four concurrent read-only shells).
P062-R08   evidence_closure_check.py --problem circdist (one of four concurrent read-only shells).
P063-R08   check_circdist_migration.py (one of four concurrent read-only shells).
P064-R08   proof_dag_check.py --problem all (one of four concurrent read-only shells).
P065       evidence-closure help/source read; direct children were its Python and rg.
P066-P068  three read-only review chunk reads covering all 890 pre-ledger lines.
P069       Python repository/package/review inventory; sole child was foreground git status.
P070       Python relevant-worker process scan; sole child was foreground ps.
P071       Python deletion of the sole /tmp scratch tree and immediate absence check.
P072       final Python scratch/status/process scan; foreground children were git status and ps.
```

The exact validator outputs were:

```text
$ python3 tools/proof_dag_check.py --problem circdist
circdist: 16 node files structurally valid

$ python3 tools/evidence_closure_check.py --problem circdist
ERROR: circdist: unlinked evidence: circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md

$ python3 tools/check_circdist_migration.py
Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies

$ python3 tools/proof_dag_check.py --problem all
se: 85 node files structurally valid
ksum: 144 node files structurally valid
circdist: 16 node files structurally valid
```

The evidence-closure command's exit status was 1 for exactly the displayed new-review path and no
other path. This is the expected blessed-before-installed state: this task was forbidden to edit
the canonical fixed-d node, while Section 15 specifically licenses the dispatcher to link this
review there. It is not a theorem or structural failure. The dispatcher must rerun the checker
after installation and require exit zero.

The final repository audit found 1,471 status entries, exactly one of which was this authorized
untracked review. Removing that line reproduced the pre-write status byte hash exactly:

```text
21cb5376b561f96ccfb83aa713e1212018b2d2ff3083f31f92c381518c0b2ed0
```

The round-66 package remained exactly 18 files / 133,007 bytes with external seal
`2c3f3e46d1eaa50989b7afed0c89c745f734039f9dae956946269314a12e75e8`. The round-64 package
remained exactly 8 files / 66,914 bytes with external seal
`17b539c0d7d16cb85d7df083579e5f74d5fba8578f84c250f861eae8efab0a17`. Neither package contained
`__pycache__` or `*.pyc` residue.

P071 reported `before True` and `after False` for
`/tmp/circdist-round67-review-20260829`. P072 independently reported `scratch_exists False`, the
same filtered repository-status hash, and `relevant_lingering_processes 0`. Thus all reviewer
scratch is deleted, all declared computation is terminated, no detached/background process
exists, and the only repository write is this review. I did not commit or push.
