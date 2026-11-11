# CIRCDIST.sat.instances finite proof certificates — author package, 2026-08-26

## 0. Status and purpose

This directory is a **proposed proof-certificate package**, written by the round-54 certificate author. It does not edit or adjudicate a proof-DAG node, route, review, protocol, scheduler, or generated view. It does not award `PROVED`. A fresh independent reviewer must check the mathematical reduction, run the verifier, and decide whether the canonical proof-certificate gate is discharged.

The package replaces the load-bearing numerical-search step for the exact three selected instances with finite, deterministic proof objects. It serializes every code row, logical row, gate, named physical fault assignment, retained sector effect, upper witness, lower-exclusion audit record, and expected digest. The verifier uses only Python's standard library. It reconstructs the instances from formulas, derives every effect twice, exhaustively excludes every lighter signature subset, and replays every upper witness through a separate full-symplectic circuit simulator.

No prior solver exit code, MILP log, Stim result, or simulation verdict is accepted as a proof premise. Those archives are provenance and corroboration only.

## 1. Exact claims and route binding

The normalization rule is the repository rule: replace CRLF by LF, strip leading/trailing whitespace, encode UTF-8, then apply SHA-256. `scope_claims.json` contains the exact text, length, level observed at authorship, and digest.

| Record | Characters | SHA-256 | Observed level |
|---|---:|---|---|
| `CIRCDIST.sat.instances` claim | 422 | `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3` | `CERTIFIED*` |
| `finite-prefix-window-closure` implication | 1,310 | `sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05` | `CERTIFIED*` |
| `CIRCDIST.sat.window` claim | 1,261 | `sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4` | `PROVED` |
| `CIRCDIST.sat.transfer` claim | 3,663 | `sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33` | `PROVED` |
| `CIRCDIST.sat` root claim | 1,357 | `sha256:513496daac6fa18bf96d1f2b6cf8768929eb62e45e103df1123479aadeeb7572` | `CERTIFIED*` |

The exact 422-character target is:

> Determine or rigorously bound (d_infinity,R_stab) for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at least one explicitly specified qLDPC schedule, using two independent methods where feasible, and for each instance provide auditable minimum witnesses and a justified attribution among single-round hook/bulk, temporal-boundary, measurement-fault, and mixed multi-round mechanisms.

This package supplies the finite prefix, witness, and restricted-mechanism content consumed by the exact route. It imports only these two already-reviewed propositions:

1. The transfer/model result at `sha256:11079...a33`, including the sector projection, the Definition-3.5 canonical-space decomposition and section-8.1 mirror, the value-only Definition-2.7 bridge, dependent check rows, and the uniform full-Pauli occupied-location collision bridge.
2. The window result at `sha256:6c50...ccc4`, which says the first `d=min(d_X,d_Z)` values determine the infinite tail and `R_stab` in this exact domain.

The finite computations below do not use the window theorem. The theorem is applied only in Section 10 after the first-`d` values have been certified.

## 2. One-command verification

From this directory, in a clean Python 3 environment:

```sh
python3 -B verify.py
```

No package installation, network access, old artifact import, writable temporary directory, SAT solver, MILP solver, or Stim installation is used. `-B` prevents bytecode files. The captured successful output is in `verifier_output.txt`.

To verify the immutable package seal from this directory:

```sh
shasum -a 256 -c SHA256SUMS
```

`SHA256SUMS` covers every regular package file other than `SHA256SUMS` itself. Its reproducible rule is:

```sh
find . -type f ! -name SHA256SUMS -print | LC_ALL=C sort | while IFS= read -r f; do shasum -a 256 "$f"; done > SHA256SUMS
```

## 3. Certified results

Both sectors have the displayed prefix, so the aggregate minimum over sectors is the same row.

| Exact selected instance | Z-memory first-`d` prefix | X-memory first-`d` prefix | Aggregate prefix | Proposed finite conclusion after the PROVED window theorem |
|---|---|---|---|---|
| Rotated surface `[[25,1,5]]`, standard uniform member 1 | `5,5,5,5,5` | `5,5,5,5,5` | `5,5,5,5,5` | `(d_infinity,R_stab)=(5,1)` |
| Rotated surface `[[25,1,5]]`, legal class-D member 2 | `4,3,3,3,3` | `4,3,3,3,3` | `4,3,3,3,3` | `(d_infinity,R_stab)=(3,2)` |
| BB qLDPC `[[18,4,4]]`, non-interleaved `NI` | `3,3,3,3` | `3,3,3,3` | `3,3,3,3` | `(d_infinity,R_stab)=(3,1)` |

Every displayed sector value has both required proof directions:

* an explicit set of distinct named occupied locations with full Pauli assignments, zero replayed detectors, and nonzero logical class at the displayed weight; and
* an exhaustive lower certificate rejecting every smaller weight in a deliberately enlarged signature model.

The expanded locations for all 102 upper objects, including the 28 main distance witnesses and the restricted-mechanism witnesses, are in `WITNESS_INDEX.md`. The immutable machine objects and complete replay vectors are in `certificates.json`.

## 4. Exact codes and schedules

### 4.1 Rotated surface `[[25,1,5]]`

Data qubits are the 25 row-major sites `q=5r+c`, `0<=r,c<5`. The constructive plaquette/boundary rule in `model.py::surface_code` regenerates the serialized matrices exactly. The checker finds:

* 12 X-check rows and 12 Z-check rows;
* rank 12 in each family, including no independence assumption in the rank routine;
* `k=25-12-12=1`;
* four weight-2 and eight weight-4 rows in each family; and
* exhaustive quotient distances `d_X=d_Z=5`.

The distance calculation enumerates every vector in the appropriate kernel and rejects the full row span of the stabilizer family. It therefore checks the quotient definition directly, not merely the weight of the supplied logical representatives.

For a uniform schedule, each check uses the same corner order. The verifier scans all `24*24=576` pairs `(pi_X,pi_Z)`, performs a physical-qubit conflict test at every layer, then checks measurement consistency

```text
#{q in supp(X_a) intersect supp(Z_b) : t(q -> Z_b) < t(X_a -> q)} = 0 mod 2
```

for every X/Z check pair. It reconstructs `96` conflict-legal schedules and `16` schedules that are both conflict-legal and measurement-consistent. Member indices are zero-based in the deterministic Python permutation order of `(NW,NE,SW,SE)`.

The selected standard member 1 is

```text
pi_X = (NW,NE,SW,SE)
pi_Z = (NW,SW,NE,SE)
```

The selected class-D member 2 is

```text
pi_X = (NW,SW,NE,SE)
pi_Z = (NW,NE,SW,SE)
```

Both have depth 4, exactly 80 gates, and 20 gates in every layer. On each weight-4 check, the last two CNOTs give these hook orientations:

| Schedule | X checks | Z checks |
|---|---|---|
| Standard member 1 | 8 horizontal, 0 vertical | 0 horizontal, 8 vertical |
| Class-D member 2 | 0 horizontal, 8 vertical | 8 horizontal, 0 vertical |

Thus member 2 is the exact legal doubly hook-misaligned schedule used by the dossier, rather than an inferred or nearby layout.

### 4.2 BB qLDPC `[[18,4,4]]` and `NI`

The two 9-qubit blocks are indexed by `(i,j)` in `Z_3 x Z_3`, with

```text
A = 1 + y + x
B = 1 + y + x^2 y
H_X = [A | B]
H_Z = [B^T | A^T].
```

`inputs.json` stores all 18 check rows and a four-row logical basis in each Pauli family. The checker reconstructs the rows from the polynomials and finds:

* 9 given X rows and 9 given Z rows, all of weight 6;
* rank 7 in each family, so the two dependencies in each given family are retained rather than discarded;
* every data qubit has degree 3 in each check family;
* `k=18-7-7=4`; and
* exhaustive quotient distances `d_X=d_Z=4`.

The non-interleaved schedule is exactly 12 layers and 108 gates. Layers 0 through 5 contain all X-check CNOTs in the order `A0,A1,A2,B0,B1,B2`; layers 6 through 11 contain all Z-check CNOTs in the order `Bt0,Bt1,Bt2,At0,At1,At2`. Every layer contains 9 disjoint CNOTs. There is no omitted layer and no round compression. The same conflict and measurement-consistency checks pass.

## 5. Full physical fault alphabet and occupied-location cost

All locations are round-copied and distinct. Data initialization and terminal readout are ideal. A configuration costs the number of occupied locations, not the number of nonidentity Pauli factors.

At every CNOT location the catalog contains all 15 nonidentity two-qubit Paulis after the gate. At every idle or post-ancilla-preparation location it contains X, Z, and Y. Each X- and Z-record location admits one classical flip. The complete 10,296 assignment rows are serialized in `fault_effects.json`.

| Schedule | CNOT locations/round | idle locations/round | post-preparation locations/round | record locations/round | full nonidentity assignments/round |
|---|---:|---:|---:|---:|---:|
| Either surface schedule | 80 | 36 | 24 | 24 | 1,404 |
| BB `NI` | 108 | 216 | 18 | 18 | 2,340 |

For a Z-memory lower bound, retain the X component of every Pauli factor; for X-memory, retain its Z component. On a CNOT, the 15 assignments project with multiplicities `{zero:3, control:4, target:4, both:4}`. On a one-qubit location the three assignments project with multiplicities `{zero:1, retained:2}`. An opposite-family record flip projects to zero. The retained menus contain 312 generators per surface sector and 567 per BB sector.

This covers the full alphabet: CSS Clifford propagation keeps X and Z components independent; canonical detector space decomposes by sector; and a nonzero full logical failure is nonzero in at least one sector. Select that sector, retain its component at each occupied location, and delete zero projections. The detector values and selected logical value are unchanged and the location weight cannot increase. Consequently a lower exclusion in both projected sectors excludes every lighter full-Pauli failure. Explicit uppers use allowed full Paulis and distinct locations, so no converse approximation is used for them.

Same-location collisions do not create a gap. In the physical model their Pauli product is another allowed Pauli at that location and costs one. In the lower calculation we allow an even larger model, including combinations that could reuse a location; rejection in that supermodel is therefore safe.

## 6. Exact one-round effects and two derivations

Fix a sector. Let `H` be its full-family check matrix, let `L` be the opposite-type logical-observable matrix, and let one projected elementary fault have:

* residual data vector `E` after the round;
* own-family record-flip vector `u`;
* residual syndrome `s=H E`; and
* logical vector `lambda=L E`.

For Z memory this is the X component, Z-check records, `H_Z`, and Z logical observables. X memory is the exact mirror.

### 6.1 Forward derivation

`one_round_faults` initializes one retained component at the named post-gate, idle, post-preparation, or record location. It applies every later Clifford gate. For CNOT `c->t`, the retained updates are

```text
X sector component: x_t <- x_t + x_c
Z sector component: z_c <- z_c + z_t
```

over GF(2). It then reads the relevant ancillas, residual data, every given syndrome row, and every logical row. This produces all serialized `(E,u,s,lambda)` objects.

### 6.2 Backward derivation

`backward_map` does not call the forward routine. It labels terminal data with final-syndrome and logical coordinate masks, walks rounds and CNOT layers backward using the dual Clifford updates, inserts the exact record-difference tags at each boundary, and samples the tag present at every possible fault assignment. For every raw projected fault in every round, its backward tag must equal the forward spacetime signature below.

The successful verifier compares 30,060 such forward/backward pairs. This is an independent derivation of every load-bearing effect, not merely a checksum comparison to the old dossier.

### 6.3 Spacetime signature and all boundaries

For `R` rounds numbered `0,...,R-1`, full-family detector slices are numbered `0,...,R`, including the ideal initial and terminal boundaries. A fault in round `r` has exact signature

```text
phi_(r,R)(f) = detector(r,u) XOR detector(r+1,u XOR H E) XOR logical(lambda).
```

Thus every cell uses `(R+1)m` detector bits plus `k` logical bits. No detector row is silently removed for a dependent check. The upper replay also constructs the partial-family interior consecutive differences. Because the certified witnesses are sector-pure, full-family silence plus zero opposite-family records gives silence in the Definition-3.5 canonical decomposition; direct silence of the corresponding Definition-2.7 set is checked separately. This uses the bridge only in its proved value-only direction and never claims equality of detector spaces or arbitrary split invariance.

## 7. Rigorous lower certificates

For a fixed sector and `R`, let `K_R` be the set of distinct nonzero signatures `phi_(r,R)(f)` of all projected generators and rounds. The number of classes is shown in Section 8.

Any physical configuration of weight `w` XORs `w` elementary signatures. Delete zero signatures, and cancel equal signatures in pairs. The result is a subset of distinct classes with the same detector/logical effect and cardinality at most `w`. Therefore, if a physical undetectable logical of weight below `d` existed, some subset of `K_R` of size `1,...,d-1` would have zero detector part and nonzero logical part.

For each exact size `j`, the checker sets `a=floor(j/2)` and `b=j-a`. It enumerates every `a`-combination and every `b`-combination. Split each XOR into detector mask `D` and logical mask `O`. A zero-detector, nonzero-logical union exists exactly when the two halves have equal `D` and unequal `O`.

The two halves are deliberately permitted to overlap in a class. This enlarges the search space. An overlap cancels and yields a smaller subset, which is already included in the ascending lower tests. Hence a `logical_found=false` result in this enlarged meet-in-the-middle space is a rigorous physical exclusion. There is no randomized search, time limit, solver status, or unverified pruning rule.

For each test, `certificates.json` stores the split sizes, exact combination counts, detector-bucket count, effect-state count, and SHA-256 of the complete sorted left catalog. The verifier regenerates the catalog and requires exact equality. The digest is a seal, while acceptance rests on the regenerated enumeration.

## 8. All 28 distance cells

`classes` is the number of distinct nonzero spacetime effect signatures. `Excluded` gives every exact weight rejected by the lower proof object. Each row also has an explicit upper witness at `d_R`.

| Instance | Sector | R | classes | Excluded | `d_R` |
|---|---|---:|---:|---|---:|
| Standard surface | Z | 1 | 77 | 1–4 | 5 |
| Standard surface | Z | 2 | 133 | 1–4 | 5 |
| Standard surface | Z | 3 | 189 | 1–4 | 5 |
| Standard surface | Z | 4 | 245 | 1–4 | 5 |
| Standard surface | Z | 5 | 301 | 1–4 | 5 |
| Standard surface | X | 1 | 77 | 1–4 | 5 |
| Standard surface | X | 2 | 133 | 1–4 | 5 |
| Standard surface | X | 3 | 189 | 1–4 | 5 |
| Standard surface | X | 4 | 245 | 1–4 | 5 |
| Standard surface | X | 5 | 301 | 1–4 | 5 |
| Class-D surface | Z | 1 | 77 | 1–3 | 4 |
| Class-D surface | Z | 2 | 133 | 1–2 | 3 |
| Class-D surface | Z | 3 | 189 | 1–2 | 3 |
| Class-D surface | Z | 4 | 245 | 1–2 | 3 |
| Class-D surface | Z | 5 | 301 | 1–2 | 3 |
| Class-D surface | X | 1 | 77 | 1–3 | 4 |
| Class-D surface | X | 2 | 133 | 1–2 | 3 |
| Class-D surface | X | 3 | 189 | 1–2 | 3 |
| Class-D surface | X | 4 | 245 | 1–2 | 3 |
| Class-D surface | X | 5 | 301 | 1–2 | 3 |
| BB `NI` | Z | 1 | 108 | 1–2 | 3 |
| BB `NI` | Z | 2 | 198 | 1–2 | 3 |
| BB `NI` | Z | 3 | 288 | 1–2 | 3 |
| BB `NI` | Z | 4 | 378 | 1–2 | 3 |
| BB `NI` | X | 1 | 108 | 1–2 | 3 |
| BB `NI` | X | 2 | 198 | 1–2 | 3 |
| BB `NI` | X | 3 | 288 | 1–2 | 3 |
| BB `NI` | X | 4 | 378 | 1–2 | 3 |

The old dossier's phrase “78 distinct one-round effect classes” is not imported. Exact reconstruction gives 77 for either surface schedule and sector, agreeing with the dossier's own corrected table and canonical erratum.

## 9. Mechanism restrictions and attributions

The mechanism flags are formal properties of projected elementary generators:

* `hook`: the one-round residual `E` has Hamming weight at least 2;
* `no-hook configuration`: every selected generator has `wt(E)<=1`;
* `measurement-class`: `E=0`;
* `needs-measurement configuration`: contains at least one measurement-class generator;
* `single-round`: all occupied locations have one common round index; and
* `mixed multi-round`: at least two distinct round indices are occupied.

For `single-round`, the checker exhausts the restricted signature menu separately at every possible round position. For `no-hook`, it removes every hook generator and repeats the complete subset proof. Both restrictions have explicit matching upper witnesses.

For `needs-measurement`, designate one flagged elementary signature `f`, then allow the remaining `cap-1` effects to be arbitrary members of the full signature set. The checker enumerates all reachable XOR states in two halves and tests every distinct flagged signature. It permits overlaps and same-location conflicts, so it is again a supermodel. Every physical configuration containing one or more measurement-class faults designates one of them and lies inside it. Rejection through the cap is therefore rigorous. Where the restricted optimum is 4, an explicit flagged weight-4 witness supplies the upper direction.

| Instance/cell range, both sectors | unrestricted | single-round optimum | no-hook optimum | needs-measurement result | Exact scoped attribution |
|---|---:|---:|---:|---:|---|
| Standard surface, R=1…5 | 5 | 5 | 5 | `>5` | A one-round bare/bulk no-hook minimum exists; every optimum excludes measurement-class generators. |
| Class-D surface, R=1 | 4 | 4 | 5 | 4 | A single-round hook minimum exists; measurement-class participation is possible at optimum. |
| Class-D surface, R=2…5 | 3 | 4 | 5 | 4 | Every minimum uses at least two rounds, every minimum needs a hook generator, and every minimum excludes measurement-class generators: mixed multi-round hook. |
| BB `NI`, R=1…4 | 3 | 3 | 4 | 4 | A single-round hook minimum exists; every optimum excludes measurement-class generators. |

These are the exact witness-level/restriction labels licensed by the route. They do **not** assert uniqueness of an optimum mechanism or global emptiness of temporal-boundary-labelled optima. All ideal initial and terminal boundary equations are present in every computation, but this package deliberately preserves the canonical route caveat against inferring “no temporal-boundary mechanism” from the restricted results.

## 10. From finite prefixes to `(d_infinity,R_stab)`

The already-PROVED window claim applies because each serialized instance has `k>=1`, depth at least one, conflict freedom, measurement consistency, one fresh ancilla per given check row, ideal boundaries, verbatim uncompressed rounds, the full uniform unit-cost Pauli group, both memory sectors, and the exact named detector conventions.

It gives `d_R=d_d=d_infinity` for every `R>=d`. Therefore:

* Standard surface: `d_5=5`, and every earlier prefix value is 5, so `d_infinity=5` and the least stable index is `R_stab=1`.
* Class-D surface: `d_5=3`; the prefix is `4,3,3,3,3`, so `d_infinity=3` and the least stable index is `R_stab=2`.
* BB `NI`: code distance is 4, `d_4=3`, and the prefix is constant 3, so `d_infinity=3` and `R_stab=1`.

No empirical extrapolation or fitted family law is used.

## 11. Clause-by-clause certificate map

| Claim/route clause | Proof object and checker path |
|---|---|
| Exact 422-character target and route binding | `scope_claims.json`; hard-coded length/hash checks in `check_scope` |
| Standard selected schedule member 1 | `inputs.json`; constructive surface code/schedule equality, 576/96/16 family audit, member-index check |
| Legal class-D selected member 2 | Same, plus exact swapped hook geometry and conflict/MC checks |
| BB `[[18,4,4]]` `NI` schedule | Constructive `A,B,H_X,H_Z`, rank/kernel quotient audit, exact 108-gate layer list |
| `k,d_X,d_Z`, check dependencies and logical compatibility | `validate_code`; exhaustive kernels and row-span quotient, all supplied logical rows checked against every quotient vector |
| Full Pauli alphabet and occupied-location cost | `fault_effects.json`; 10,296 exact assignments and projection pointers rebuilt by `full_fault_projection_catalog` |
| Every finite `d_R` lower bound | Per-cell effect set/digest and exact MITM catalogs in `certificates.json`; `check_cell` |
| Every finite `d_R` upper bound | Full assignments and replay vectors in `certificates.json`; `replay_witness` |
| Two independent finite derivations where feasible | Forward one-round propagation versus backward spacetime propagation for 30,060 pairs; separate full-symplectic upper replay; old independent archives retained only as corroboration |
| Mechanism attribution | Per-cell single-round, no-hook, and measurement-flagged exact restricted certificates plus explicit uppers |
| Aggregate minimum and first-`d` prefix | Both sectors checked independently; `check_certificates` takes their pointwise minimum |
| Infinite tail and stabilization index | Exact PROVED window claim hash plus deterministic tail/minimal-index calculation |
| No accidental convention drift | Exact detector metadata, `(R+1)m` boundary coordinates, full replay, value-only bridge wording, wrong-split negative control |

## 12. Trusted base and why it is sufficient

The finite certificate trusts:

1. ordinary exact integer, list, `itertools.combinations`, JSON, and SHA-256 behavior in the Python standard library;
2. the approximately 700-line `model.py` checker core and approximately 290-line `verify.py` orchestration, both included and sealed;
3. the public GF(2), Clifford, detector, projection, and meet-in-the-middle arguments stated in this README and checker comments; and
4. for route composition only, the exact PROVED transfer and window propositions at their displayed hashes.

It does not trust a solver, floating-point arithmetic, random seed, opaque log, external package, old dirty working directory, or precomputed “PASS” bit. Inputs and certificates are treated as adversarial data: formulas reconstruct the inputs, effects are rebuilt twice, lower catalogs are recomputed, and full witnesses are replayed independently.

Dependent stabilizer generators are covered because every given row remains a detector coordinate while rank, span, and quotient routines use row reduction without an independence premise. Every boundary is covered by the `R+1` full-family slices and direct partial-family replay. Every physical Pauli is covered by the enumerated projection catalog. Collisions are covered by full group closure for physical configurations and by an overapproximating lower search. Both sectors are checked, then aggregated. All `R` required by the first-`d` window are explicit.

SHA-256 seals serialization but is not asked to prove a negative search result: the verifier recreates each searched catalog and compares the substantive counts and result before checking its digest.

## 13. Negative controls

A successful run must reject all four mutations:

1. change one Pauli in an upper witness while retaining the claimed replay;
2. delete one serialized projected effect;
3. increase a claimed optimum while retaining its old lower/upper objects; and
4. replace the required full boundary detector description with an interior-only wrong split.

`verify.py` fails closed if any mutation is accepted. The captured run reports `4/4` rejected.

## 14. Provenance audit, commands, and process hygiene

`source_audit.json` records the byte size and SHA-256 of the frozen definitions, protocols, current nodes, exact route/rebind reviews, full instances dossier/review, window proof/review, transfer proof/review, and bridge review inspected by the author.

The three archived checksum packages were rechecked without importing their verdicts:

| Archive | Manifest entries | Verified | Bytes |
|---|---:|---:|---:|
| Prior instances proposer archive | 247 | 247 | 3,076,961 |
| Prior independent-review archive | 29 | 29 | 97,395 |
| Stim cross-validation archive | 17 | 17 | 70,482 |

`LEDGER.md` records the authoring commands, corrected failed attempts, repository validators, FIX-2 process accounting, scratch cleanup, and surviving-process declaration. `repository_validation.txt` captures read-only repository checks. `verifier_output.txt` captures the self-contained proof verifier.

## 15. Limitations and field-level recommendations

This package certifies only the three exact schedules and the first-`d` cells needed by the exact route. It does not certify the proposed `d=7` standard arm, `d=9` family cell, the fitted law `d_R=max(d-R,(d+1)/2)`, arbitrary schedule families, nonuniform costs, compressed rounds, noisy boundaries, arbitrary detector splits, or an exclusive taxonomy of temporal-boundary mechanisms.

For the standard schedule, the needs-measurement restricted result is `>5`; no exact upper optimum beyond 5 is claimed because only exclusion at the unrestricted optimum is needed for attribution. For class-D and BB it is exactly 4 by matching lower and upper objects.

Proposed follow-up, subject to independent review:

* bind this package to the unchanged 422-character instances claim and unchanged 1,310-character route implication;
* independently inspect the physical-alphabet projection and lower-enumeration completeness proof, rerun both package commands, and adversarially mutate additional effects/witnesses; and
* only after that review, let the dispatcher decide any field-level route/node assessment, basis, frontier, or event changes.

Fresh independent review remains required. Nothing in this author package is a self-awarded canonical status change.

## 16. Package inventory

* `README.md` — public derivation, scope, certificate map, trusted base, and limitations.
* `model.py` — exact GF(2), constructive code/schedule, effect, enumeration, and replay core.
* `verify.py` — self-contained orchestrator and negative controls.
* `inputs.json` — exact matrices, logicals, gates, layouts, and expected structural audits.
* `fault_effects.json` — every full physical assignment and every retained one-round effect.
* `certificates.json` — all 28 distance cells, lower catalogs, mechanism restrictions, and upper objects.
* `WITNESS_INDEX.md` — readable expansion of all 102 upper objects.
* `scope_claims.json` — exact claim/route/premise/root texts and hashes.
* `source_audit.json` — inspected-source digests and old-archive checksum audit.
* `verifier_output.txt` — captured clean verifier run.
* `repository_validation.txt` — captured read-only repository validation.
* `LEDGER.md` — process, command, FIX-2, cleanup, and failure ledger.
* `SHA256SUMS` — immutable seal under the exclusion rule stated above.
