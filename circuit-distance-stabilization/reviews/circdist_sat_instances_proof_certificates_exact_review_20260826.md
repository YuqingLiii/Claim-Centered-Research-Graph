# `CIRCDIST.sat.instances` proof certificates — fresh exact completion review

**Date:** 2026-08-26  
**Round:** strict-serial ProofPilot round 55  
**Reviewer status:** independent; I did not author the package, used no sub-agent or delegated process, and imported neither packaged Python module in the clean-room checker  
**Package:** `circdist/artifacts/circdist_sat_instances_proof_certificates_20260826/`  
**Durable write license:** this report only

## Executive decision

| object | exact text | current level | review verdict | licensed installed level |
|---|---:|---:|---:|---:|
| route `finite-prefix-window-closure` | 1,310 characters, `sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05` | `CERTIFIED*` | **PROVED** | `PROVED` |
| node `CIRCDIST.sat.instances` | 422 characters, `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3` | `CERTIFIED*` | **PROVED** | `PROVED` |
| root `CIRCDIST.sat` | 1,357 characters, `sha256:513496daac6fa18bf96d1f2b6cf8768929eb62e45e103df1123479aadeeb7572` | `CERTIFIED*` | **not adjudicated** | **no change licensed** |

The route and node decisions are separate. The exact unchanged route is proved because its finite inputs are now proof-quality, independently regenerated certificates and its sole premise is the current exact `PROVED` window claim. The exact unchanged node is proved because that route plus the three selected explicit schedules satisfies every existential and attribution clause. No claim or implication repair is required. I expressly forbid any byte change to either exact string in this installation.

The sealed author package is complete, internally consistent, independently reproducible, and adversarially resistant within its exact model. Simulation is corroboration only; the licensed lower direction is finite exhaustive proof and the licensed upper direction is full physical Pauli replay.

## 1. Authority, protocols, and exact current state

I read the complete governing protocols, the complete scheduler, the four named canonical nodes, the frozen problem/rescope definitions, the prior instances dossier and independent review, the exact window proof/review and downstream rebind, the transfer proof definitions/amendment, the bridge-fold review, and the current transfer completion review. The current source fingerprints were:

| source | bytes | SHA-256 |
|---|---:|---|
| `DAG_PROTOCOL.md` | 15377 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | 8523 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `operations/circdist/SCHEDULER.yaml` | 106910 | `f3441fdaf4b33f25416c01929e8d0dd50d6b48dadcb65d15f4567a28e1b6e4ae` |
| `circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml` | 17808 | `e778686cc3299e0dfd7ded364b76969b5b90cfd04e2a6b5408e9f0aca2f46d0b` |
| `circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml` | 9411 | `c687130d56bf4777e1bc7c60b32556458ea989feb994be39245c07c98aafe8a6` |
| `circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml` | 11534 | `4a81a52d19187f7ccd8a7eca333475edd5860778f02f678028c82e5ea9c45592` |
| `circdist/proof-dag/nodes/CIRCDIST.sat.yaml` | 20458 | `0c4c93cb518c0d6f11ca30e3906debbeb175169a9c69efd2532f850de7c88775` |

The hash-normalization rule is SHA-256 of the YAML-loaded scalar's UTF-8 bytes, without synthetic whitespace. Direct recomputation produced:

- instances claim: exactly 422 characters/bytes, `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`;
- route implication: exactly 1,310 characters/bytes, `sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05`;
- window claim: 1,261 characters, `sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4`, current `PROVED`;
- transfer claim: 3,663 characters, `sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33`, current `PROVED`;
- root claim: 1,357 characters, `sha256:513496daac6fa18bf96d1f2b6cf8768929eb62e45e103df1123479aadeeb7572`, current `CERTIFIED*` and outside this adjudication.

The package's `source_audit.json` records the author-time instances-node file hash `b1e309ce0095d4250c903830e831875f532d5a257d654ae511574f3d2f97d4fe`; the current file hash is `e778686cc3299e0dfd7ded364b76969b5b90cfd04e2a6b5408e9f0aca2f46d0b`. This is expected because the dispatcher later linked the package and updated current review prose. I did not treat the stale whole-file source hash as a match. I instead rebound the still byte-exact claim and implication and checked all current assessment/premise state directly.

## 2. Finding F-SEAL — package seal and verifier

The package contains exactly 13 regular files, with no symlink or special-file escape:

```text
LEDGER.md
README.md
SHA256SUMS
WITNESS_INDEX.md
certificates.json
fault_effects.json
inputs.json
model.py
repository_validation.txt
scope_claims.json
source_audit.json
verifier_output.txt
verify.py
```

`SHA256SUMS` has SHA-256 `059fed32fbe931378e0dd2f3cab2a6e3baa0d38767da6bc7b5ee590cffdf7e85`. It contains one unique safe entry for each of the other 12 files and intentionally excludes itself. There is no uncovered regular file, duplicate entry, absolute/parent path, or file outside the package. Independent parsing and `shasum -a 256 -c` both passed:

```text
9e935086c01eb3e78792a10184975abc93a2d3e5b79a2fa7967187ac5aeb88c0  ./LEDGER.md
c8ebf6634a7f07caf1748ec53bf7b31a46d21d8af4d95d9b2b42f7dd1ce5f2ff  ./README.md
9ca8f815218ab0422338877e3ac3c18e0e89d5d25f14dc7aecca17e572ed1ee0  ./WITNESS_INDEX.md
03fcb3abb5a8f36da0e8ff7915217bf9cad55a1d65fef3e41f6b47eed63f622b  ./certificates.json
2c8246f8d9d8264674adc05fff90d28fc75370b265899516db16c46718d63f6f  ./fault_effects.json
173717a59bdfaf39b509f0432284aa80bcb29b1653d1b11b3ad428a2c453133a  ./inputs.json
bd0313d11b57bb50e9a95a0e92a83df63115e1981a657bd2695d78726278b1e8  ./model.py
050a45e0e5eb99b6014cc072fe8971f756b9a47e9e57fcfc3ffa78693fa77c30  ./repository_validation.txt
23cf6d711afd4ade20223ae150efb2b6b2eb39e8cf37f434d6eccdd6118996a5  ./scope_claims.json
ff97612abaa548e5e5f3346e7186dfcc09f2755cdd6578e1099f329187f2f312  ./source_audit.json
0aa4fa7c262dc3cd183e4061281b2e724c32027e33acde6b3d76c769106f6aac  ./verifier_output.txt
b6731701e72f2c0eb2c9dac80a13fee9d1c56c081b71924db33c62234ea62cf0  ./verify.py
```

The verifier was run in the foreground with bytecode disabled. Its independently observed totals were:

```text
scope hashes                 5/5
input audits                 3/3; 268 gates
full assignments             10,296
projected generators         2,382
sector/R cells               28/28
lower exclusions             78
forward/backward comparisons 30,060
restricted subsets           354
measurement supermodels      28
full-Pauli upper replays      102
aggregate checks             14/14
packaged negative controls   4/4
result                       PASS
```

I invoked each packaged negative control separately. Tampering an upper witness, deleting a projected effect, increasing an optimum, and dropping detector-boundary metadata each reached the intended assertion failure. Thus `verify.py` does not merely return its captured `verifier_output.txt`.

## 3. Finding F-INPUT — exact clean-room input reconstruction

I rebuilt the CSS matrices and schedules from the frozen definitions and serialized incidences, rather than importing `model.py`.

| instance | independent code audit | exact schedule | legality and occupancy | canonical selection |
|---|---|---|---|---|
| standard surface | `n=25`, `rank H_X=rank H_Z=12`, `k=25-12-12=1`; enumeration of kernel representatives outside the opposite row space gives `d_X=d_Z=5` | depth 4, 80 gates, 20 per layer; `piX=(NW,NE,SW,SE)`, `piZ=(NW,SW,NE,SE)` | every one of 80 incidences occurs once; no qubit collision; all `(MC)` parities zero | zero-based uniform-`S4 x S4` member 1; package and canonical selected instance agree |
| class-D surface | same `[[25,1,5]]` matrix and distances | depth 4, 80 gates, 20 per layer; `piX=(NW,SW,NE,SE)`, `piZ=(NW,NE,SW,SE)` | every incidence once; conflict-free; all `(MC)` parities zero | zero-based member 2, legal class D/hook-misaligned; package and canonical selected instance agree |
| BB NI | `n=18`, nine X and nine Z rows, both ranks 7, `k=18-7-7=4`; exhaustive `2^11` kernel enumeration gives `d_X=d_Z=4` | depth 12, 108 gates, 9 per layer; X layers `A0,A1,A2,B0,B1,B2`, then Z layers `Bt0,Bt1,Bt2,At0,At1,At2` | every one of 108 incidences once; conflict-free; all `(MC)` parities zero | exact `BB_18_4_4_NI` selected schedule |

For the surface family I enumerated all `4! x 4! = 576` global order pairs: exactly 96 are conflict-free and exactly 16 are also measurement-consistent. The selected indices and orders above are exact, not family averages. `(MC)` was checked as

```text
c_ab = #{q in supp(a) intersect supp(b): t(q->b) < t(a->q)} mod 2 = 0
```

for every X/Z row pair. The BB all-X-before-all-Z ordering remains consistent because every X/Z overlap is even. Dependent BB rows were retained as nine detector coordinates; they were used at rank seven only for `k`, quotient, and distance calculations.

Full one-round fault coverage was reconstructed exactly:

| instance/sector | CNOT / idle / post-prep / record locations | full assignments | projected generators | serialized full/projected hashes independently matched |
|---|---:|---:|---:|---|
| each surface sector/schedule | `80 / 36 / 24 / 24` | 1,404 | 312 | yes |
| each BB sector | `108 / 216 / 18 / 18` | 2,340 | 567 | yes |

Across both sectors this is `4*1,404 + 2*2,340 = 10,296` full assignments and `4*312 + 2*567 = 2,382` projected generators. The 15 CNOT Paulis, three one-qubit Paulis, and one record flip were all present; initialization and terminal readout were correctly absent as fault locations.

## 4. Finding F-MODEL — physical model, CSS projections, detectors, and boundaries

### 4.1 Full occupied-location Pauli model

A configuration assigns at most one nonidentity element at a named location and costs the number of occupied locations. At a CNOT location the 15 nonidentity two-qubit Paulis form `F_2^4` after adjoining identity; at one-qubit locations the three Paulis form `F_2^2`; at a record location the flip forms `F_2`. Clifford propagation and record readout are linear.

Same-location multiplication is therefore exact. Starting from any collision-permitting elementary multiset, multiply all assignments at one location. The effect is unchanged, and the number of terms drops by one if the product is nonidentity or by two if it is identity. Repetition produces a legal occupied-location configuration of no larger cost. The reverse inequality is immediate because every configuration is a multiset. Hence the two minimum weights are equal. This argument would fail for an incomplete local alphabet or nonuniform Pauli costs; neither extension is licensed.

### 4.2 Sector projection and full-Pauli lower safety

For Z memory, keep each Pauli's X component and Z-check record flips, and delete its Z component and X-check record flips. The full local group supplies the pure projected Pauli at the same location, so occupied weight cannot increase. Selected-sector record flips, terminal data-X, and logical-Z parity are preserved; opposite-sector records become zero. The X-memory mirror is identical with X/Z swapped.

If a full physical Pauli fault of weight `<d` were undetectable logical, at least one CSS logical quotient component would be nonzero. Projecting to that sector gives a sector configuration of weight no larger, silent against the full-family chain and the opposite deterministic directions. Thus lower exclusion in both sector projections excludes every full Pauli logical of smaller weight. Conversely, each upper is replayed as an actual full Pauli assignment on distinct locations. The lower direction may safely use a supermodel; the upper direction never does.

### 4.3 Canonical detectors and value-only bridge

With accumulated class `sigma_0=0`, per-round residual increment `E_r`, and own-record flip `u_r`, set

```text
sigma_(r+1) = sigma_r + E_r
f_r = H sigma_r + u_r
D_0 = f_0
D_r = f_r + f_(r-1), 1 <= r < R
D_R = H sigma_R + f_(R-1)
```

These are exactly `m_-1=0`, the `R` real records, and the ideal terminal virtual record. The clean-room direct propagation and the independently coded local formula agreed on all 30,060 elementary spacetime effects. Dropping the actual `D_0` and `D_R` slices admitted spurious weight-one logical signatures in **all 28 cells**, making the boundary convention load-bearing and exposing off-by-one errors.

Definition 3.5 first takes deterministic parities and then those whose **value** is constant over the prepared logical-basis family. The full measured-family chain spans its sector half, including terminal stabilizer rows. Dependent opposite-family check combinations add round-zero redundancy detectors. A pure sector projection flips none of those opposite records, so it annihilates the missing directions. This proves equality of the Definition-2.7 and Definition-3.5 minimum values in Z memory and, by the directly checked section-8.1 mirror, in X memory. It does not prove detector-set equality or arbitrary-split invariance.

For BB, the nine rows of rank seven leave two redundancy directions in each family. They were retained in canonical full-Pauli upper replay and in the value-bridge audit. No row was silently discarded merely because it was dependent.

## 5. Finding F-EFFECT — independent forward/backward reconstruction

The clean-room checker propagated every listed full assignment forward through the exact CNOT order and independently derived the same generator backward from the detector/observable parity. It then tiled the one-round effect into each copied round using the equations above. Checks included:

- exact sector labels and X/Z mirror rather than accepting symmetric serialized values;
- every preparation, CNOT, idle, and record location and every allowed Pauli;
- both endpoint detector slices and all interior differences;
- no reuse of an R=1 cell as evidence for larger R;
- independent regeneration of effect-class and backward-map digests;
- full canonical and Definition-2.7 silence at each explicit upper;
- distinct physical witness locations and no concealed same-location collision;
- nonzero terminal logical quotient, including all `2^4-1` BB nonzero logical signatures.

No forward/backward disagreement, omitted location, wrong sector, or boundary-index discrepancy survived. The fresh checker SHA-256 was `2c10fd7a32fdb278320b32348cccac06283dc70cc4d26aaf8ba4de386c7adc9e`; its source was scratch-only and was deleted under the write boundary, while its algorithm and exact totals are transcribed here.

## 6. Finding F-28 — all 28 exact distance cells

Every line below was regenerated without importing package code. `classes` is the deduplicated nonzero `(detector,logical)` signature set. `pairs` counts independently compared forward/backward elementary spacetime effects. Each lower entry gives exact split, binomial combination counts, retained states/buckets, and catalog digest. Each upper is an actual full-Pauli replay with distinct locations.

- `surface_standard_d5/Z/R1`: **PASS**, `d_R=5`; detectors/logicals `24/1`; classes/pairs `77/312`; effect digest `742caa3fac6d88606fba1225d9a5b4121b9eaa21f9e35bed322d98ab4a55c37b`; backward digest `841c9ee193c16d799cedd320a294de45f0781749d3b6edb7a52fb700628fee1a`; lower: w1 split=0+1 combos=1x77 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=77x77 states=77 buckets=77 digest=b0277edf0b49bf790cda3a5b0fed0c28a73e5282ae60aeaee7f40f5ed0bcf948; w3 split=1+2 combos=77x2926 states=77 buckets=77 digest=b0277edf0b49bf790cda3a5b0fed0c28a73e5282ae60aeaee7f40f5ed0bcf948; w4 split=2+2 combos=2926x2926 states=2555 buckets=2555 digest=5b3816785b10142f259b3206845f5b30af77822aa4703a3b9184ef61b8c7dced; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `d57e5eef8c3594667c202d865e1ab445e90e8bc96e3f18b8a217820109a6e19b`.
- `surface_standard_d5/Z/R2`: **PASS**, `d_R=5`; detectors/logicals `36/1`; classes/pairs `133/624`; effect digest `d1d8761b916d0bfc520ac9b3d45ffce76eb5c88c578dad13cd2b5b06a9762bf5`; backward digest `cd114c1d112b67d758ebb2ecc1bc40b7325fa44e35ff3d0225450f2232c27e12`; lower: w1 split=0+1 combos=1x133 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=133x133 states=133 buckets=133 digest=a0753e7b6c4d56d25ff9b5b1da516491991f93055d94c19a3209d6c2d3220387; w3 split=1+2 combos=133x8778 states=133 buckets=133 digest=a0753e7b6c4d56d25ff9b5b1da516491991f93055d94c19a3209d6c2d3220387; w4 split=2+2 combos=8778x8778 states=7903 buckets=7903 digest=889f04f2f39fcbe1eeab1ef42cce991dbfa151a1e0e3520c3230ab2b73926b6f; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `d57e5eef8c3594667c202d865e1ab445e90e8bc96e3f18b8a217820109a6e19b`.
- `surface_standard_d5/Z/R3`: **PASS**, `d_R=5`; detectors/logicals `48/1`; classes/pairs `189/936`; effect digest `ac907741223442f84c6ea78bc07bdfb642d072a146a04d1fec1a92db4555def3`; backward digest `5907c84dbe0c636ee246fa8f848143eeb7321708258f3504078132fca0bf4d67`; lower: w1 split=0+1 combos=1x189 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=189x189 states=189 buckets=189 digest=7c21f0d9a9009325a58d32d28002acdf6c342bf98f3e2f9434b4ab5eed864bcb; w3 split=1+2 combos=189x17766 states=189 buckets=189 digest=7c21f0d9a9009325a58d32d28002acdf6c342bf98f3e2f9434b4ab5eed864bcb; w4 split=2+2 combos=17766x17766 states=16387 buckets=16387 digest=b3c20e6e94c3633e052ca458019a6c645944b722a100827685f65259142efb30; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `d57e5eef8c3594667c202d865e1ab445e90e8bc96e3f18b8a217820109a6e19b`.
- `surface_standard_d5/Z/R4`: **PASS**, `d_R=5`; detectors/logicals `60/1`; classes/pairs `245/1248`; effect digest `d8a4e81294f19064d6f37888fa8464c5973a34255f0b2e987aba30fb97fb8f3c`; backward digest `7de138e250e664a7ba21f44768e333dfb2d184c330724feae4a03fc56bf113bb`; lower: w1 split=0+1 combos=1x245 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=245x245 states=245 buckets=245 digest=0211e50839fa27a1299fd8b5b14cd09dfe02c5c68c7a859e359eaa51186d60dd; w3 split=1+2 combos=245x29890 states=245 buckets=245 digest=0211e50839fa27a1299fd8b5b14cd09dfe02c5c68c7a859e359eaa51186d60dd; w4 split=2+2 combos=29890x29890 states=28007 buckets=28007 digest=7340492cdd5e00b4d0220b86a8becb0c32a6230c55d23bfd48c3171ece93b4fa; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `d57e5eef8c3594667c202d865e1ab445e90e8bc96e3f18b8a217820109a6e19b`.
- `surface_standard_d5/Z/R5`: **PASS**, `d_R=5`; detectors/logicals `72/1`; classes/pairs `301/1560`; effect digest `a39201cec5ea666e8d4f7becba1c8a137fa23e5ca501f2b182f839b5d6bc8420`; backward digest `e1617d329d7b5854ef550102701bcf03d7f5aa03ce67e908768c9161b0c79d7a`; lower: w1 split=0+1 combos=1x301 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=301x301 states=301 buckets=301 digest=1d19abe5057a83bafdb8645ad86a619cafd995bf95b8a35c2ff7ee8d05b28cb7; w3 split=1+2 combos=301x45150 states=301 buckets=301 digest=1d19abe5057a83bafdb8645ad86a619cafd995bf95b8a35c2ff7ee8d05b28cb7; w4 split=2+2 combos=45150x45150 states=42763 buckets=42763 digest=9dcb5ee58e3e071e5bcbb0c8eaca40243c8de81c4ece6d6dc72c033ed5cb90f1; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `d57e5eef8c3594667c202d865e1ab445e90e8bc96e3f18b8a217820109a6e19b`.
- `surface_standard_d5/X/R1`: **PASS**, `d_R=5`; detectors/logicals `24/1`; classes/pairs `77/312`; effect digest `a7dc991d1dd1ec9990b26348fb398cf62d2a434a227548262d9b7ec528895719`; backward digest `a0df220e783bec71aa77bbd854474dc3f7216fc65ea805dd2dcd745a178e0b45`; lower: w1 split=0+1 combos=1x77 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=77x77 states=77 buckets=77 digest=608f6e0b33184cda354f0aadeff711eae0a4b0b50c6019344b0e2ee7ba4d4156; w3 split=1+2 combos=77x2926 states=77 buckets=77 digest=608f6e0b33184cda354f0aadeff711eae0a4b0b50c6019344b0e2ee7ba4d4156; w4 split=2+2 combos=2926x2926 states=2555 buckets=2555 digest=8bf07a1d43c95997fb67302f85ae22fc7dd53ddcac7048a7e349ab6e71cb3e95; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `c3acc512e1216980408e4cc48baf921d8cf99be984444d36df819dfffd0bb6ef`.
- `surface_standard_d5/X/R2`: **PASS**, `d_R=5`; detectors/logicals `36/1`; classes/pairs `133/624`; effect digest `2b9fb662a3ba087a0e5de02f5c9dffab906c389ebde2a6dbe2365740b43b7d47`; backward digest `bfbbe98fa01a5ffe3cd76b3d2c4f8c270a57d833a3fa02808c7a01196ac6dbb1`; lower: w1 split=0+1 combos=1x133 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=133x133 states=133 buckets=133 digest=1ea646f8759855c50a5e77afc7dd92e86b59e5d9c0e893b3d8d5a20531a37783; w3 split=1+2 combos=133x8778 states=133 buckets=133 digest=1ea646f8759855c50a5e77afc7dd92e86b59e5d9c0e893b3d8d5a20531a37783; w4 split=2+2 combos=8778x8778 states=7903 buckets=7903 digest=3569179cdb772a44bed9b5d48eefeae261f1192b2e5447f6e7ba5cf4dab93106; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `c3acc512e1216980408e4cc48baf921d8cf99be984444d36df819dfffd0bb6ef`.
- `surface_standard_d5/X/R3`: **PASS**, `d_R=5`; detectors/logicals `48/1`; classes/pairs `189/936`; effect digest `ec40607eae87a24ba4badedfc341876db48902cf8a956b305e906d82f28931f0`; backward digest `b59751105c07790bb6cdde353cb0c81135da4e9a01910260d1485f941b9d733f`; lower: w1 split=0+1 combos=1x189 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=189x189 states=189 buckets=189 digest=17a8c21660f41febbc1f2316dce4194d285d06c5c348631435c3c7ee195018b0; w3 split=1+2 combos=189x17766 states=189 buckets=189 digest=17a8c21660f41febbc1f2316dce4194d285d06c5c348631435c3c7ee195018b0; w4 split=2+2 combos=17766x17766 states=16387 buckets=16387 digest=7c30dae825ee566b9ba6894d753316e0f17bda9e12b9d6ebb55b6309ffd38f94; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `c3acc512e1216980408e4cc48baf921d8cf99be984444d36df819dfffd0bb6ef`.
- `surface_standard_d5/X/R4`: **PASS**, `d_R=5`; detectors/logicals `60/1`; classes/pairs `245/1248`; effect digest `4b645d6a1e33fb2660afe17cd789503ee68bb8c3c6b8611c1e59be8156f1f7c3`; backward digest `8d7531bb707b812b3b92bdbb9b94ccd0f718252234c2763a655eaaaa0cb49cc3`; lower: w1 split=0+1 combos=1x245 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=245x245 states=245 buckets=245 digest=50ca91140704d3a8bc3e092ed7966167cce25360acacf80aad8d7f609b5d2aae; w3 split=1+2 combos=245x29890 states=245 buckets=245 digest=50ca91140704d3a8bc3e092ed7966167cce25360acacf80aad8d7f609b5d2aae; w4 split=2+2 combos=29890x29890 states=28007 buckets=28007 digest=c60857815cd8317d6ae31f6a64a40b2fdcdea51ae6bf6d6d38fe1fc36cf38df3; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `c3acc512e1216980408e4cc48baf921d8cf99be984444d36df819dfffd0bb6ef`.
- `surface_standard_d5/X/R5`: **PASS**, `d_R=5`; detectors/logicals `72/1`; classes/pairs `301/1560`; effect digest `d0e748f546f2ec5bb0cb553f7e3b93dda6937acb9c07252b44d95a831c7c4728`; backward digest `e41e974cd8ea1d26761b7df5dc35612bc4050c72c8fd3b5cbbb96a0e86851b77`; lower: w1 split=0+1 combos=1x301 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=301x301 states=301 buckets=301 digest=fb1dbb5f581558411d142e8531bd9b9e4178fe95f1ef58fd9e5f0827c3ca09a5; w3 split=1+2 combos=301x45150 states=301 buckets=301 digest=fb1dbb5f581558411d142e8531bd9b9e4178fe95f1ef58fd9e5f0827c3ca09a5; w4 split=2+2 combos=45150x45150 states=42763 buckets=42763 digest=18a8ee4d855846a78aa1af2f8217f4abf965f4e66a1f591afe5680b7a91e0758; upper: weight `5`, distinct locations `5`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `c3acc512e1216980408e4cc48baf921d8cf99be984444d36df819dfffd0bb6ef`.
- `surface_classD_d5/Z/R1`: **PASS**, `d_R=4`; detectors/logicals `24/1`; classes/pairs `77/312`; effect digest `52797c86e64485b7cd2232dbfefeed11dc1ef023323dab883d395f736b865f5d`; backward digest `e5a3d0e4926e94dc144e73438b29153d333a7a11fdb6e051d43ba0f742a676ee`; lower: w1 split=0+1 combos=1x77 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=77x77 states=77 buckets=77 digest=10dc7e1742c64a3ed2cf36153844616ba6c9257a635b3d5a567a26968df3e195; w3 split=1+2 combos=77x2926 states=77 buckets=77 digest=10dc7e1742c64a3ed2cf36153844616ba6c9257a635b3d5a567a26968df3e195; upper: weight `4`, distinct locations `4`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `6ba61e8d005ef666139ccb1eb2cd6624b0808bc810d519dd077c2d80e7d13a95`.
- `surface_classD_d5/Z/R2`: **PASS**, `d_R=3`; detectors/logicals `36/1`; classes/pairs `133/624`; effect digest `c52c1881c91deba2e1d9b5ec83c78674ff832f50d5aa66a6d4e37fffec476052`; backward digest `18a97efc21f4a8b70a4d78bb5e274cb76302852d8a81015ee2b27ee57e89a924`; lower: w1 split=0+1 combos=1x133 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=133x133 states=133 buckets=133 digest=e045fcb49040ad4dbff2612d8c61f0347d3bf68221e10119f5aa939eedf012eb; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `9aa6e638c072e80f97bca7abe88043db07f2b37e08fad9fd9208ba959386ead3`.
- `surface_classD_d5/Z/R3`: **PASS**, `d_R=3`; detectors/logicals `48/1`; classes/pairs `189/936`; effect digest `873978256227284b000af2d921b1b5600f8cfa49a8f05e4a502993587158e476`; backward digest `bf2646fc48dbeca59ce17771071c51a37b0be7678a3e1d0767c7d2bf0b19cce6`; lower: w1 split=0+1 combos=1x189 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=189x189 states=189 buckets=189 digest=2cfd9838765c08dbb01ff38262d1dc720ad08b0bdb2af6925932de9ef71aa86c; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `9aa6e638c072e80f97bca7abe88043db07f2b37e08fad9fd9208ba959386ead3`.
- `surface_classD_d5/Z/R4`: **PASS**, `d_R=3`; detectors/logicals `60/1`; classes/pairs `245/1248`; effect digest `9dbb9a312e01203ab21c71c63be4250351859ba0ccba1264aef9172b3a4c2e95`; backward digest `fbc12f12f6730ea997812d1ae53adc43f5eea2543ae84b21528f710b337c6a17`; lower: w1 split=0+1 combos=1x245 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=245x245 states=245 buckets=245 digest=e21b9bd29285d9d7c311d3431dbff2836dc1ec60c405d3ecfc315a5900427949; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `9aa6e638c072e80f97bca7abe88043db07f2b37e08fad9fd9208ba959386ead3`.
- `surface_classD_d5/Z/R5`: **PASS**, `d_R=3`; detectors/logicals `72/1`; classes/pairs `301/1560`; effect digest `cacc59b916f5865ad36f18d29e581889060584e17c6fa78943f5e23698f414dc`; backward digest `3fe47a802691dfa8aacce0c25087ba5687682828783c06b84a30db102251bdb5`; lower: w1 split=0+1 combos=1x301 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=301x301 states=301 buckets=301 digest=bf39b54927717e8fea1f135a70a732de372321c7b7c84d20003c05685675bdc7; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `9aa6e638c072e80f97bca7abe88043db07f2b37e08fad9fd9208ba959386ead3`.
- `surface_classD_d5/X/R1`: **PASS**, `d_R=4`; detectors/logicals `24/1`; classes/pairs `77/312`; effect digest `79202ee4c8cd585ba71c1e63ed0ae2780565d2b5e049e8beb475327ab4369bcf`; backward digest `202fd3701ff1a36645909bafae84025c38ccec7b9afce185294eb2581fa658eb`; lower: w1 split=0+1 combos=1x77 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=77x77 states=77 buckets=77 digest=96266cd2c0a11c3ef8035262b41068fdcbc08bf14f7d41369736c716238b66d1; w3 split=1+2 combos=77x2926 states=77 buckets=77 digest=96266cd2c0a11c3ef8035262b41068fdcbc08bf14f7d41369736c716238b66d1; upper: weight `4`, distinct locations `4`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `579c7d539b12090fae5e14e21f82807d9e9ef1b9bf97691a7e67706d04724c98`.
- `surface_classD_d5/X/R2`: **PASS**, `d_R=3`; detectors/logicals `36/1`; classes/pairs `133/624`; effect digest `20ec0909a0a112612aac9475e7c320f4094b37e71f4ae634c727acf427e53942`; backward digest `4ef99b91f92bbf67fdf7af9b2800f79d34f273c8520e67ffb2c80378e8e2b0b9`; lower: w1 split=0+1 combos=1x133 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=133x133 states=133 buckets=133 digest=4b21e4aa5dee267b4b047198a40bf2fc57afc5dd8d37ac6ad7f96d5d0bd5cfa8; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `61bb1f4d5881f2754f7df410853bfb27337d09ec5489e433872358296f58df32`.
- `surface_classD_d5/X/R3`: **PASS**, `d_R=3`; detectors/logicals `48/1`; classes/pairs `189/936`; effect digest `d9927d6af0b3f0072fe38101b8357827038c3b45a46429a556bd824812f0c1b8`; backward digest `ed32b7a5ef730528055f1290d6d93baf30264a9e1dac136c22279cb33ded28a1`; lower: w1 split=0+1 combos=1x189 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=189x189 states=189 buckets=189 digest=a8c911f2c314a61163155b3344edf2cbb9299f9b2fbfd745b94f522370a7d986; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `61bb1f4d5881f2754f7df410853bfb27337d09ec5489e433872358296f58df32`.
- `surface_classD_d5/X/R4`: **PASS**, `d_R=3`; detectors/logicals `60/1`; classes/pairs `245/1248`; effect digest `7b2973482ef57f5e2f475beb757d092df78c9d08c19dc3a2d8562e3fed54190c`; backward digest `c8c4e2b470fd19f4c12699c14589bdf9f2938ea0b4d599268fae54c8ce7449d0`; lower: w1 split=0+1 combos=1x245 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=245x245 states=245 buckets=245 digest=572486939188fb7354227e6127b84d91d4fc488e9d893aee9b7d8627a44a7d69; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `61bb1f4d5881f2754f7df410853bfb27337d09ec5489e433872358296f58df32`.
- `surface_classD_d5/X/R5`: **PASS**, `d_R=3`; detectors/logicals `72/1`; classes/pairs `301/1560`; effect digest `66caf6e269ee8632572bfa04d130ed1994ccaf0e0437f055d887a60f3eefbbdf`; backward digest `12f59d5596a0bff2343ede451bf6a730005a60594d33a2c503a3bb43c4583479`; lower: w1 split=0+1 combos=1x301 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=301x301 states=301 buckets=301 digest=766714dac10013d8dd6dfa1dcdf7b6580303d5c5cacd6bdbc96bae1a44293ea2; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1]`, replay digest `61bb1f4d5881f2754f7df410853bfb27337d09ec5489e433872358296f58df32`.
- `BB_18_4_4_NI/Z/R1`: **PASS**, `d_R=3`; detectors/logicals `18/4`; classes/pairs `108/567`; effect digest `b70580635a44d9129c90d79afe5035ef6b29d371fb3f80957fead53fba10d513`; backward digest `72798bbc7d7f3a7b7ebf230ca18f705dc924ed5b8f3f763844e470c260e91dd8`; lower: w1 split=0+1 combos=1x108 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=108x108 states=108 buckets=108 digest=9392fa859fe5322ecf3a7e75ca4591bec4b92ae90dbcc09a2407a7e2d89d146b; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1, 1, 1, 1]`, replay digest `4ecb61875b01cdbdbd69c0bac80beb3c6eb965e2daf82ee72d9ade2fde21553d`.
- `BB_18_4_4_NI/Z/R2`: **PASS**, `d_R=3`; detectors/logicals `27/4`; classes/pairs `198/1134`; effect digest `92080a04dab787f98544aa189634dc021473586d9bfdd7289670f98f248bb195`; backward digest `110fc60b72168de8ecbc65fc48ddff4e1dc333d1ca6b7c1cb8e85474b92953d1`; lower: w1 split=0+1 combos=1x198 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=198x198 states=198 buckets=198 digest=e82b479e295620a76b49482eece5cc0c4cac15de5fc30ed6669298c3a6088156; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1, 1, 1, 1]`, replay digest `4ecb61875b01cdbdbd69c0bac80beb3c6eb965e2daf82ee72d9ade2fde21553d`.
- `BB_18_4_4_NI/Z/R3`: **PASS**, `d_R=3`; detectors/logicals `36/4`; classes/pairs `288/1701`; effect digest `ab12439ae8237167fc2cec58b5da66759314e006c3573b049df4747e75a72c89`; backward digest `861d6febe4f71dc60d1971c5a087e8a139aed4d125639d492f9374c339437133`; lower: w1 split=0+1 combos=1x288 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=288x288 states=288 buckets=288 digest=b8011137b94dd82deb5838df0097b4a7f294b75e8a61aacceba5afc7f1400411; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1, 1, 1, 1]`, replay digest `4ecb61875b01cdbdbd69c0bac80beb3c6eb965e2daf82ee72d9ade2fde21553d`.
- `BB_18_4_4_NI/Z/R4`: **PASS**, `d_R=3`; detectors/logicals `45/4`; classes/pairs `378/2268`; effect digest `0eac2dff8596528bf863f6ad77d8d78a1290ef811c43293ea894c5e7f7b59497`; backward digest `a7c29df982ee7d8ddd7f71b43b037dab2a979e664d2c5abdaf5432f459de5654`; lower: w1 split=0+1 combos=1x378 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=378x378 states=378 buckets=378 digest=bf8d10e7655a4171c3d4665cb43fa584ad73807fe785808d967d6b5c4f41bb4d; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[1, 1, 1, 1]`, replay digest `4ecb61875b01cdbdbd69c0bac80beb3c6eb965e2daf82ee72d9ade2fde21553d`.
- `BB_18_4_4_NI/X/R1`: **PASS**, `d_R=3`; detectors/logicals `18/4`; classes/pairs `108/567`; effect digest `090a33030f12762bab63510e07f24b824660590c5470ffd5ae536ebc4bf6f02a`; backward digest `0b5b882990fc05b60b04827ebbcd26bea7efab4a982ce448cf9c3c5ff6c2ef17`; lower: w1 split=0+1 combos=1x108 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=108x108 states=108 buckets=108 digest=b818422ef50158d4bf4beffaa5185b69c68a2d0d149d516590226095eb591817; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[0, 0, 1, 0]`, replay digest `6700c19684823367f75a38936f4933826259f1ca28d39d60cd687002414b4f4b`.
- `BB_18_4_4_NI/X/R2`: **PASS**, `d_R=3`; detectors/logicals `27/4`; classes/pairs `198/1134`; effect digest `62ad97dac7588b8f16e407b49f53d71e6d96e826ecc67dc9b76dca90ecbd8d27`; backward digest `e3ce6411aa7b15538a21676688ba4ab46baf11f31084dfd68654524f81ec9c58`; lower: w1 split=0+1 combos=1x198 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=198x198 states=198 buckets=198 digest=52c68b1f5fb0fabb045dae6bd46bc92b944f40befff10764044ef885b683b6d0; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[0, 0, 1, 0]`, replay digest `6700c19684823367f75a38936f4933826259f1ca28d39d60cd687002414b4f4b`.
- `BB_18_4_4_NI/X/R3`: **PASS**, `d_R=3`; detectors/logicals `36/4`; classes/pairs `288/1701`; effect digest `2f49e8892b9c40ccf5a4cfda927b65191fd35c6fa4abbfa448a46408fee9774a`; backward digest `3b2080b65d0b3729017093b165f6e7f2d26a412d6450e08bcb6ea05f63f9d4d0`; lower: w1 split=0+1 combos=1x288 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=288x288 states=288 buckets=288 digest=6b0419634a28e2208445d261f9e8435b5e21223eea0e6db4140d2c77a8314fed; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[0, 0, 1, 0]`, replay digest `6700c19684823367f75a38936f4933826259f1ca28d39d60cd687002414b4f4b`.
- `BB_18_4_4_NI/X/R4`: **PASS**, `d_R=3`; detectors/logicals `45/4`; classes/pairs `378/2268`; effect digest `e4b078b1639438dcaa6fc454c68c5f5a6b8ecc0cad9558efa3d2651a9a710741`; backward digest `62a24eb54359f5a0cb74d3160d8041f08239e4e553798582c20dee96a737bdf9`; lower: w1 split=0+1 combos=1x378 states=1 buckets=1 digest=0428d2c3979ad698c6f331ad2ca1dad91b0467219a2062f40a915aa580bd4d0e; w2 split=1+1 combos=378x378 states=378 buckets=378 digest=9db7e5c06a38f014ab5f09c2dc2231e8e1c4e9fa5cfd997ef46e7386c919b616; upper: weight `3`, distinct locations `3`, canonical/Definition-2.7 silent `True/True`, nonzero observable `[0, 0, 1, 0]`, replay digest `6700c19684823367f75a38936f4933826259f1ca28d39d60cd687002414b4f4b`.

The resulting sector prefixes are exactly:

```text
standard Z/X: 5,5,5,5,5
class D Z/X:  4,3,3,3,3
BB NI Z/X:    3,3,3,3
```

### 6.1 Why the MITM lower certificate is exhaustive

Let a projected elementary class have signature `(D,L)`. Any configuration is an XOR of such signatures. Delete zero signatures and cancel equal signatures in pairs. Detector/logical effect is unchanged and weight only decreases, leaving a subset of distinct nonzero classes. Therefore a logical of weight `w<d_R` would produce a distinct class subset of some size at most `w`, and the certificates search every exact size `1,...,d_R-1`.

For target size `w`, the matcher enumerates combinations of sizes `a=floor(w/2)` and `b=w-a`, indexes one half by detector signature, and asks whether equal detector signatures have unequal/nonzero combined logical signature. The stated counts are recomputed as binomial coefficients and every left catalog is regenerated before its digest is compared. Allowing a class to occur in both halves or allowing location collisions enlarges the search space. Any real distinct subset has a disjoint half partition and is included; overlap can create only false positives. Thus `logical_found=false` in this supermodel is a sound lower exclusion. Class deduplication and cancellation do not discard a minimum logical: an equal-signature pair XORs to zero and can be removed.

This reasoning covers `k=4` BB because `L` is a vector and the accept condition is any nonzero combined logical vector, not a single hard-coded logical bit.

### 6.2 Recompute-versus-serialization attacks

In addition to the four packaged negative controls, I mutated a scratch copy in seven ways. Each was rejected by recomputation:

| mutation | result |
|---|---|
| change a lower `logical_found` from false to true | assertion failure |
| alter `left_combinations` | assertion failure |
| alter a lower catalog digest | assertion failure |
| duplicate an upper physical location | assertion failure |
| omit one full Pauli assignment from the alphabet | assertion failure |
| relabel a witness with the wrong CSS sector | assertion failure |
| substitute an R=1 cell for R=2 while editing superficial fields | assertion failure |

This shows that verdict booleans, counts, digests, and witness replay fields are checked against regenerated objects. Hashes protect serialization but do not stand in for the exhaustive proof.

## 7. Finding F-MECHANISM — definitions and scoped attributions

The package definitions are exact:

```text
hook generator: projected one-round elementary generator with residual data weight >= 2
no-hook configuration: every selected projected generator has residual weight <= 1
measurement-class generator: projected generator with residual E=0
needs-measurement configuration: contains at least one measurement-class generator
single-round configuration: all occupied locations have one round index
mixed multi-round configuration: occupied locations use at least two distinct rounds
```

“Measurement-class” is an effect-class definition, not a claim that every generator in the class is literally a record-flip location. “Hook” likewise refers to residual data weight, not a uniqueness claim about a gate narrative.

The restricted proofs combine an explicit legal upper where existence is claimed with exhaustive strict lower directions:

| selected scope | unrestricted | single-round restricted | no-hook restricted | needs-measurement restricted | licensed attribution |
|---|---:|---:|---:|---:|---|
| standard, each sector, `R=1,...,5` | 5 | 5 | 5 | `>5` | a one-round no-hook/bare-bulk optimum exists; every optimum excludes measurement-class generators |
| class D, each sector, `R=1` | 4 | 4 | 5 | 4 | every optimum needs a hook; a single-round hook optimum exists; a measurement-containing optimum exists |
| class D, each sector, `R=2,...,5` | 3 | 4 | 5 | 4 | every optimum is mixed multi-round, hook-driven, and measurement-free; explicit mixed upper exists |
| BB NI, each sector, `R=1,...,4` | 3 | 3 | 4 | 4 | a single-round hook optimum exists; every optimum needs a hook and excludes measurement-class generators |

The “needs measurement” lower certificate designates one flagged `E=0` class and allows all remaining classes arbitrarily up to the cap. After cancellation, every configuration containing at least one flagged class occurs in this overlap/collision supermodel. Failure to find a logical is therefore a sound strict lower bound. The 28 supermodels and 354 restricted subset checks were regenerated.

No certificate proves uniqueness of an optimum mechanism, all-measurement participation at class-D `R=1`, or emptiness of temporal-boundary-labelled optima. The temporal-boundary caveat is retained. The bonus standard `d=7`, class-D `d=9`, and fitted family law are outside the exact existential claim discharge and are not promoted by this review.

## 8. Finding F-TAIL — finite-to-infinite derivation

The current window premise is already `PROVED` at its exact hash and covers each selected schedule: `k>=1`, conflict-free plus `(MC)`, fresh one-ancilla check extraction, ideal endpoints, verbatim uncompressed rounds, the complete uniform full-Pauli location group, aggregate two-sector distance, canonical detector spaces, and only the Definition-2.7 value bridge. The current transfer claim at its exact `PROVED` hash supplies the aligned finite-R model and collision/value bridges. Neither premise is promoted by inheritance here.

For code spatial distance `d`, the window claim gives `d_R=d_d=d_infinity` for every `R>=d`.

1. Standard has the reviewed first-five prefix `5,5,5,5,5`; the tail is 5, so `(d_infinity,R_stab)=(5,1)`.
2. Class D has `4,3,3,3,3`; the tail from `R=5` is 3, and the certified values at `R=2,3,4` are already 3, so `(3,2)`.
3. BB has the first-four prefix `3,3,3,3`; the tail is 3, so `(3,1)`.

The finite certificates, upper witnesses, and mechanism restrictions do not use the window theorem. The window theorem supplies only the infinite tail. This avoids circularity.

## 9. Adversarial attack and decision trail

| attack or rejected branch | disposition |
|---|---|
| trust `verifier_output.txt` or serialized verdicts | rejected; verifier rerun, independent clean-room recomputation, and mutations used |
| package manifest silently omits a payload | rejected; exact 13-file inventory and 12-entry self-excluding manifest |
| canonical source is accepted on stale author-time whole-file hash | rejected; current claim, implication, premise, and source hashes rebound directly |
| one CSS sector is mislabeled or silently omitted | rejected; both sectors reconstructed directly and full assignment hashes differ as expected |
| initial/terminal detector off-by-one | rejected; endpoint attack creates spurious weight-one logicals in all 28 cells |
| BB dependent rows are dropped | rejected; nine coordinates retained, ranks seven, two redundancy directions audited in each sector |
| a projected lower bound misses a full-Pauli logical | rejected by weight-nonincreasing sector projection and both-sector exclusion |
| collision-permitting lower search is too small | rejected; it is a supermodel and group multiplication proves the physical bridge |
| effect-class dedup loses multiplicity evidence | rejected; equal signatures cancel in pairs, yielding a no-heavier distinct subset |
| MITM overlapping halves produce a false negative | rejected; every physical subset has a disjoint partition; overlap only enlarges the searched set |
| reuse R=1 evidence for a larger R | rejected by direct R-dependent detector dimensions, pair counts/digests, and a mutation test |
| class-D `R>=2` could still be single-round/no-hook/measurement-containing at weight 3 | rejected by three strict restricted optima (4,5,4) and explicit mixed upper |
| standard/BB measurement exclusion is inferred from one chosen witness | rejected; the flagged supermodel proves every optimum excludes that class |
| “attribution” means unique mechanism or globally no temporal boundary | rejected; exact caveat retained |
| bonus `d=7`, `d=9`, or fitted law is needed | rejected; exact claim is existential and consumes only the three named schedules |
| route becomes PROVED merely because window is PROVED | rejected; finite proof inputs were independently reviewed before route promotion |
| node or root level follows automatically from route | rejected; node adjudicated separately; root expressly untouched |
| claim/implication precision repair | rejected as unnecessary; any byte change would lapse the exact reviews |

## 10. Trusted base and limitations

The trusted base is finite and explicit: the current protocol/YAML parser semantics; UTF-8 and SHA-256; the CPython 3 interpreter and ordinary integer/XOR/combinations operations; the frozen exact input incidences; elementary CSS row-space/quotient algebra; and the already-`PROVED` exact window and transfer claims at their current hashes. PyYAML is used for canonical/candidate parsing, while the sealed verifier itself is standard-library only. The clean-room implementation shares the serialized inputs and elementary mathematics but not package source code or verdict logic.

This is a computational proof certificate, not a Lean formalization of the 28 enumerations. Exhaustiveness is justified by the finite reduction above and corroborated by two independent implementations plus negative controls. I do not claim a proof of CPython or SHA-256. The scratch clean-room source cannot be retained because the commission licenses exactly one durable file; its hash, construction, totals, and attacks are recorded here.

The prior instances review supplies an additional independently authored engine and witness replay, satisfying “two independent methods where feasible.” The new package closes its earlier objection that simulation alone was insufficient. The window and transfer claims were checked for current hashes and exact applicability, with their load-bearing algebra re-read/re-derived; this review does not reopen their already completed global adjudications.

The extra raw-tree `verify_public_release.py` command is not an installation validator and failed for the existing private checkout's release-manifest/privacy inventory. The actual release/DAG/Lean contract selftests passed 14/14, 24/24, and 23/23. No public-release waiver is inferred.

## Finding F-ROUTE — exact route verdict

**Verdict: `PROVED`** for the unchanged 1,310-character implication at `sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05`.

The implication's finite values, witnesses, mechanism restrictions, detector/value bridge, and collision bridge now have proof-quality independent support. Its sole premise `CIRCDIST.sat.window` is `PROVED` at `sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4` and applies to all three selected schedules. The conditional conclusion follows exactly as in §8. This route verdict neither changes the node nor adjudicates the root.

## Finding F-NODE — exact node verdict

**Verdict: `PROVED`** for the unchanged 422-character claim at `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`.

The explicit standard, class-D, and BB schedules are legal witnesses for the claim's three existential arms; their exact `(d_infinity,R_stab)` pairs, minimum witnesses, and scoped mechanism attributions are proved. “Using two independent methods where feasible” is met by the prior clean-room engine, the sealed certificate engine, and this review's independently written checker/replay. The route is separately `PROVED`. No remaining frontier item is a premise of this exact claim.

## 11. Sole licensed atomic dispatcher installation

No alternative substantive wording is licensed. **Do not change `claim`, route `premises`, route `implication`, or route `proof`; do not edit the window, transfer, root, scheduler, protocols, tools, history, artifacts, or prior reviews.** Install the complete YAML below at `circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml`, regenerate only the derived `circdist/proof-dag/NODE_INDEX.md` and `GRAPH.mmd`, and run the validators in §12 atomically.

This serialization does all required state changes:

- node and route levels become `PROVED` separately;
- exact summaries and four caveats for each are installed;
- old exact review links are retained and the new hash-bound `Finding F-ROUTE`/`F-NODE` links are appended;
- the package run/evidence notes are updated from “pending” to independently reviewed without rewriting old evidence;
- `proof-certificate-gate` is removed and no `frontier` remains; bonus research is not a gate on this exact claim;
- all existing events remain; four events are appended for route review, route level change, node review, and node level change;
- `CIRCDIST.sat` remains untouched.

```yaml
id: CIRCDIST.sat.instances
role: outcome
aliases:
- SAT-INSTANCES
claim: Determine or rigorously bound (d_infinity,R_stab) for a standard surface-code schedule, a legal hook-misaligned surface-code
  schedule, and at least one explicitly specified qLDPC schedule, using two independent methods where feasible, and for each
  instance provide auditable minimum witnesses and a justified attribution among single-round hook/bulk, temporal-boundary,
  measurement-fault, and mixed multi-round mechanisms.
assessment:
  level: PROVED
  caveats:
  - 'Scope is exactly the three selected schedules: zero-based rotated-surface [[25,1,5]] standard member 1; zero-based rotated-surface
    [[25,1,5]] legal class-D hook-misaligned member 2 in the uniform S4 x S4 family; and BB [[18,4,4]] NI. This proves the
    existential claim, not all schedules in either surface family, a universal qLDPC result, the bonus d = 7/d = 9 cells,
    or the fitted family law.'
  - 'The finite proof covers exactly 28 sector/R cells: both CSS sectors at R = 1,...,5 for each selected surface schedule
    and R = 1,...,4 for BB NI. It uses ideal data boundaries, verbatim disjoint round locations, all named preparation/CNOT/idle/record
    locations, full local Pauli menus with uniform occupied-location cost, the full temporal detector chain including initial
    and terminal slices, dependent check rows, Definition 3.5 and its section-8.1 mirror, and only the value equality to Definition
    2.7.'
  - Mechanism attributions are scoped. Standard has a weight-5 one-round no-hook witness and every weight-5 optimum excludes
    measurement-class generators. Class D at R = 1 has optimum 4, every optimum requires a hook, and a measurement-containing
    optimum exists; at R = 2,...,5 its optimum 3 is necessarily multi-round, hook-requiring, and measurement-free. BB at R
    = 1,...,4 has a weight-3 single-round hook witness and every optimum requires a hook and excludes measurement-class generators.
    No uniqueness or global absence of temporal-boundary-labelled optima is proved.
  - The finite-to-infinite step alone consumes the exact PROVED CIRCDIST.sat.window claim at sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4,
    in the model aligned with the exact PROVED transfer claim at sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33.
    It yields standard (d_infinity,R_stab) = (5,1), class D (3,2), and BB NI (3,1). No CIRCDIST.sat root adjudication, edit,
    or promotion is licensed.
  summary: PROVED at sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3. Fresh independent strict-serial
    review reconstructed the three exact code/schedule inputs; checked ranks, distances, legality, measurement consistency
    and canonical selection; regenerated all 28 sector/R distance cells, 78 exhaustive lower exclusions, 102 distinct-location
    full-Pauli upper witnesses and every scoped mechanism restriction; audited the complete package seal, verifier and negative
    controls; and applied the exact PROVED window tail. The licensed results are standard (5,1), class D (3,2), and BB NI
    (3,1), with only the stated selected-instance and mechanism scopes.
  basis:
    routes:
    - finite-prefix-window-closure
    reviews:
    - path: circdist/reviews/circdist_sat_instances_review_20260823.md
      kind: review
      scope: Independent adversarial review (own engine written from the definitions, no proposer code read) — headline family
        re-verified by three methods + witness replay, legality/(MC) space rebuilt, convention-slip probes, qLDPC arm rebuilt
        with a closed-form re-derivation of the exhaustive by-product, standard d = 3,5 re-run, honesty checks; licenses CERTIFIED*
        with the stated caveat set. Logs SHA-summed (29 files), FIX-2 clean.
      locator: Per-arm verdicts
      reviewed_hash: sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3
    - path: circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md
      kind: review
      scope: 'Fresh independent strict-serial adversarial proof-certificate audit: verified the complete SHA256 seal and negative
        controls; reconstructed all selected inputs and schedules; independently regenerated both-sector full-boundary effects,
        every one of the 28 exact distance cells, all exhaustive lower certificates and all full-Pauli upper replays; audited
        collision, projection, detector-value, dependent-row, mechanism and finite-tail arguments; and licensed the unchanged
        exact claim as PROVED without adjudicating the root.'
      locator: Finding F-NODE
      reviewed_hash: sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3
    runs:
    - path: circdist/artifacts/circdist_sat_instances_proof_certificates_20260826
      kind: run
      scope: Sealed round-54 proof-certificate package with exact serialized inputs, complete SHA256 manifest, 28/28 finite
        distance certificates, 102 explicit distinct-location full-symplectic upper replays, exhaustive lower exclusions,
        direct forward/backward effects, scoped mechanism certificates, four packaged negative controls, and a standard-library
        verifier; independently regenerated and adversarially audited in the round-55 completion review.
      result: Independent manifest audit passed 12/12 covered files with SHA256SUMS self-excluded; packaged verifier passed
        28/28 cells, 78 lower exclusions, 30,060 forward/backward pairs, 354 restricted subsets, 28 measurement supermodels
        and 102 upper replays; four packaged and seven additional negative controls rejected; a clean-room checker importing
        no package code independently reproduced every load-bearing result.
    - path: circdist/artifacts/circdist_sat_instances_20260823.md
      kind: run
      scope: 'Wave-24 full three-arm computation (logs: artifacts/logs_circdist_sat_instances_20260823/, 247 files, SHA256SUMS):
        surface d = 3,5,7 standard + constructed hook-misaligned family (uniform S4 x S4 space, 576 -> 96 legal -> 16 legal+(MC),
        identical at d = 3,5,7); BB [[18,4,4]] qLDPC arm; per-cell witness audits and MILP mechanism exclusions; four independent
        implementations (own min-plus C engine, stim 1.16.0, own exact MILP/HiGHS, exhaustive-vs-criterion (W)).'
      result: 'Standard: (d, 1) at d = 3,5,7. Hook-misaligned: R_stab = 2/3/4 at d = 5/7/9 with d_R = max(d - R, (d+1)/2)
        fitted over 37 cells (conjectured law). BB [[18,4,4]]: (3, 1). 61/61 spacetime-matrix vs stim DEM signature checks;
        zero cross-method disagreements anywhere.'
    - path: circdist/artifacts/circdist_sat_recon_20260820.md
      kind: run
      scope: Rotated surface d=3,5,7 with Stim for R=1 through 12; four rotated-surface d=3 schedules with exact min-plus
        transfer for R=1 through 10; enumeration of 7,610 legal schedules across rotated-surface, Steane, and Shor test families.
      result: All recorded sequences were constant within their stated windows; the d=3 transfer values agreed with Stim.
        No qLDPC or completed hook-misaligned arm was included.
    evidence:
    - path: circdist/artifacts/circdist_sat_recon_20260820.md
      kind: text
    - path: circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.instances.yaml
      kind: text
      note: Immutable pre-migration record, including every original event, former summary and frontier; historical evidence,
        not an additional completion review.
    - path: circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_sat_instances_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_sat_instances_review_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_sat_instances_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_sat_instances_review_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
routes:
  finite-prefix-window-closure:
    premises:
    - CIRCDIST.sat.window
    implication: The instances dossier's reviewed finite computations establish, within their stated computed windows, the
      d_R values for the standard rotated-surface d = 5 schedule, the legal doubly hook-misaligned rotated-surface d = 5 schedule,
      and the BB [[18,4,4]] schedule; its audited minimum witnesses and restricted exact optimizations establish the scoped
      mechanism attributions required by this claim. These finite-window values, witnesses, and attributions do not use CIRCDIST.sat.window.
      The two records use the same listed full temporal-boundary detector coordinates; on the selected BB prefix, the extra
      redundancy detectors identified by S3-prime were independently added through R = d and did not change d_R. Under their
      shared uniform unit-cost full-Pauli fault model, the dossier's faulty-location minima equal the window theorem's elementary-fault
      minima because same-location faults may be replaced by their Pauli product while preserving the effect and never increasing
      weight. The premise CIRCDIST.sat.window then gives d_R = d_d = d_infinity for every R >= d, so the computed first-d
      prefixes determine d_infinity and R_stab for those three schedules. Conditional on that premise and subject to the node's
      existing scope caveats, these results establish every clause of the CIRCDIST.sat.instances claim.
    proof:
      sketch: Use the reviewed d = 5 standard prefix 5,5,5,5,5, the d = 5 class-D prefix 4,3,3,3,3, and the BB [[18,4,4]]
        prefix 3,3,3,3. Compare the listed full-boundary detector coordinates directly, use the selected-BB redundancy-detector
        probe through R = d, and apply the Pauli-product collision argument of transfer Lemma 2.9 to identify the two weight
        conventions. Then apply the exact window premise to extend each prefix, yielding (d_infinity,R_stab) = (5,1), (3,2),
        and (3,1). The dossier's finite witness replays and restricted optimizations supply the required scoped mechanism
        labels; do not use the window premise for those finite facts or for any conjectural family law or temporal-boundary-emptiness
        claim.
      sources:
      - path: circdist/artifacts/circdist_sat_instances_proof_certificates_20260826
        kind: run
      - path: circdist/artifacts/circdist_sat_instances_20260823.md
        kind: text
      - path: circdist/reviews/circdist_sat_instances_review_20260823.md
        kind: text
      - path: circdist/artifacts/circdist_sat_window_theorem_20260822.md
        kind: text
      - path: circdist/artifacts/circdist_sat_window_amendment1_20260822.md
        kind: text
      - path: circdist/artifacts/circdist_sat_transfer_proof_20260823.md
        kind: text
      - path: circdist/reviews/circdist_transfer_bridgefold_20260823.md
        kind: text
      - path: circdist/artifacts/circdist_sat_root_assembly_20260823.md
        kind: text
      - path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
        kind: text
    assessment:
      level: PROVED
      caveats:
      - 'RP-C1: This is PROVED only as the exact 1,310-character conditional implication at sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
        with sole premise CIRCDIST.sat.window. It proves the selected instances claim when the premise and reviewed finite
        certificates are combined; it does not adjudicate or promote CIRCDIST.sat.'
      - 'RP-C2: The tail step is licensed only under the exact PROVED CIRCDIST.sat.window claim at sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4:
        k >= 1 CSS codes, conflict-free and measurement-consistent one-ancilla extraction, ideal boundaries, verbatim uncompressed
        rounds, both CSS sectors, uniform unit-cost full Pauli groups, canonical Definition-3.5/section-8.1 detectors, and
        value-only Definition-2.7 equivalence.'
      - 'RP-C3: The finite inputs are the independently reviewed proof certificates for only the selected standard member
        1, class-D member 2, and BB NI schedule. The lower direction is exhaustive in an overlap/collision supermodel and
        each upper direction is a legal distinct-location full-Pauli replay. Serialized verdicts and digests are checked against
        regeneration and are not accepted as proof by themselves.'
      - 'RP-C4: Mechanism conclusions retain their restricted-optimization scopes: existence is asserted only where an explicit
        upper is supplied, universal exclusion only where a strict restricted lower bound is certified, and neither uniqueness,
        a universal family law, bonus d = 7/d = 9 results, nor global absence of temporal-boundary-labelled optima is inferred.'
      summary: PROVED at sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05. The unchanged exact implication
        combines independently regenerated finite proof certificates and scoped mechanism restrictions with the exact PROVED
        window premise. The first-d prefixes 5,5,5,5,5; 4,3,3,3,3; and 3,3,3,3 extend respectively to (d_infinity,R_stab)
        = (5,1), (3,2), and (3,1). This route decision is separate from the node decision and licenses no CIRCDIST.sat root
        change.
      basis:
        reviews:
        - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
          kind: review
          scope: Fresh independent audit of the finite-prefix/tail boundary, the three selected claim-discharge schedules,
            detector and weight-convention alignment, the Pauli-product collision argument, caveat propagation, exact serialization
            and hashing, and strict route-versus-node completion rules; archived numerical searches and the window theorem
            itself were not re-run or re-proved.
          locator: Finding F-ROUTE
          reviewed_hash: sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
        - path: circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md
          kind: review
          scope: Fresh strict-serial independent downstream audit of the repaired 1,261-character window premise against each
            selected finite instance, the finite-prefix/tail implication, all boundary, schedule, sector, detector and fault-model
            pins, quantifiers, hashes, old-review binding, IW-C0, and no-inheritance rules.
          locator: Finding F-INSTANCES-ROUTE
          reviewed_hash: sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
        - path: circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md
          kind: review
          scope: Fresh independent strict-serial route audit binding the unchanged 1,310-character implication to the exact
            current window premise and to independently regenerated finite distances, full-Pauli witnesses, exhaustive lower
            bounds, detector/collision bridges and scoped mechanism exclusions for exactly the three selected schedules; re-derived
            all finite-to-infinite pairs and enforced route/node/root separation.
          locator: Finding F-ROUTE
          reviewed_hash: sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
        evidence:
        - path: circdist/artifacts/circdist_sat_instances_proof_certificates_20260826
          kind: run
          locator: README.md and SHA256SUMS
          note: Load-bearing finite proof certificates independently regenerated and adversarially reviewed in the round-55
            exact review; complete manifest, clean-room recomputation, full witness replay and negative controls passed.
        - path: circdist/reviews/circdist_sat_instances_review_20260823.md
          kind: text
          locator: Section 7
          note: Historical CERTIFIED* review retained as prior independent computation and witness evidence. Its proof-quality
            blocker is closed only by the new sealed-package review and is not silently rewritten.
        - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
          kind: text
          locator: Limitations
          note: Historical exact-edge review retained for the dependency and convention analysis. Its stated need for proof-quality
            independently checkable certificates is satisfied by the new package review.
events:
  finite-prefix-window-route-added-2026-08-26:
    date: '2026-08-26'
    type: route-added
    route: finite-prefix-window-closure
    summary: Registered the previously documented window-to-instances dependency as route finite-prefix-window-closure with
      sole premise CIRCDIST.sat.window. The route separates reviewed finite computations and mechanism attributions from the
      premise-dependent infinite-tail inference; the claim text and node level did not change.
    sources:
    - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
  finite-prefix-window-route-reviewed-2026-08-26:
    date: '2026-08-26'
    type: review-completed
    route: finite-prefix-window-closure
    summary: Fresh independent exact-text review established the machine-visible dependency and reviewed the exact conditional
      implication. The reviewer recommended PROVED, but dispatcher adjudication retained CERTIFIED* because the implication
      consumes finite numerical and mechanism-exclusion evidence whose prior review expressly refused PROVED and whose proof-quality
      certificate gate remains open. CIRCDIST.sat.instances and CIRCDIST.sat.window remained CERTIFIED*, and no claim or root
      field changed.
    sources:
    - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
  window-premise-scope-rebound-2026-08-26:
    date: '2026-08-26'
    type: review-completed
    route: finite-prefix-window-closure
    summary: Fresh strict-serial independent review re-adjudicated the unchanged finite-prefix-window-closure implication
      against the repaired PROVED CIRCDIST.sat.window claim. All three selected schedules satisfy the exact premise domain
      and the implication hash remains unchanged. The completed window-premise frontier was removed, but IW-C0, the proof-certificate
      gate, the route level, and the node level remain unchanged.
    sources:
    - path: circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md
      kind: review
      locator: Finding F-INSTANCES-ROUTE
  proof-certificate-route-reviewed-2026-08-26:
    date: '2026-08-26'
    type: review-completed
    route: finite-prefix-window-closure
    summary: Fresh independent strict-serial review regenerated every load-bearing finite certificate and mechanism restriction,
      audited the physical/model bridges and exact PROVED window premise, and approved the unchanged route implication at
      sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05.
    sources:
    - path: circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
  finite-prefix-window-route-proved-2026-08-26:
    date: '2026-08-26'
    type: level-change
    route: finite-prefix-window-closure
    from: CERTIFIED*
    to: PROVED
    summary: Promoted only finite-prefix-window-closure after its finite proof inputs and exact conditional composition passed
      fresh independent adversarial review. This route event does not promote the node or CIRCDIST.sat root.
    sources:
    - path: circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
  proof-certificate-node-reviewed-2026-08-26:
    date: '2026-08-26'
    type: review-completed
    summary: Fresh independent strict-serial review checked the sealed package, all 28 sector/R cells, every lower and upper
      certificate, mechanisms, conventions, hashes, trusted base and exact claim binding, and found the exact selected-instance
      claim complete.
    sources:
    - path: circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md
      kind: review
      locator: Finding F-NODE
  instances-proved-2026-08-26:
    date: '2026-08-26'
    type: level-change
    from: CERTIFIED*
    to: PROVED
    summary: Promoted CIRCDIST.sat.instances only after both the exact finite-prefix-window-closure route and the unchanged
      exact claim passed fresh independent completion review. CIRCDIST.sat root remains untouched and receives no inherited
      promotion.
    sources:
    - path: circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md
      kind: review
      locator: Finding F-NODE
```

## 12. Disposable installation validation

The exact YAML above was installed only in `/tmp`, with a locator placeholder at this report path. Generated views were written only in that copy. Results:

```text
proof_dag_check --problem circdist --previous-state REAL --write-generated
  PASS: prior nodes, routes, and events retained; 16 nodes structurally valid
proof_dag_check --problem circdist
  PASS: 16 nodes structurally valid
proof_dag_check --problem all
  PASS: se 85, ksum 144, circdist 16 nodes structurally valid
evidence_closure_check --problem circdist
  PASS: 122 structured paths, project-local and linked
evidence_closure_check --problem all
  PASS: 122 structured paths, project-local and linked
check_circdist_migration.py
  PASS: 16 nodes, 143 original events, 728 byte-identical copies
duplicate-rejecting YAML load
  PASS: scheduler plus 16 nodes, 17/17
test_release_contracts.py
  PASS: 14/14
test_dag_contracts.py
  PASS: 24/24
lean_dag_check.py --selftest
  PASS: 23/23
git diff --no-index --check REAL_NODE CANDIDATE_NODE
  exit 1 solely because files differ; empty output, hence no whitespace diagnostic
git diff --check (real tree before report)
  PASS: exit 0, empty output
```

A full path-hash comparison found exactly the intended disposable differences: the candidate report placeholder was added; the instances node and the two generated views changed; zero other paths changed; window, transfer, and root nodes were byte-identical to current canonical files. Candidate parsing reconfirmed the exact 422/1,310 strings and hashes, both `PROVED` levels, both review locators/hashes, four appended events, and no frontier.

After the dispatcher installs the YAML, the real evidence-closure count should become 122. Before installation, this new report is necessarily an unlinked evidence file because the reviewer's write boundary forbids editing the node; that expected transient closure error is not permission for any other unlinked file.

## 13. FIX-2 command, process, write, and cleanup accounting

Every command was serial and synchronous. No process overlapped another. Every `exec_command` used one ephemeral foreground `zsh` wrapper; a listed Python, `rg`, `sed`, `cat`, `du`, `shasum`, or `git` executable was its only foreground child where applicable. All wrappers and children terminated before the next process. No PTY session, daemon, job-control background process, detached process, pipe to a persistent consumer, network process, or sub-agent was created.

1. P01: one foreground shell wrapper ran `pwd`, the initial `git status --short`, and the repository-local `AGENTS.md` search. Exit 0; no applicable `AGENTS.md` was found. The pre-existing dirty/untracked tree was recorded and not attributed to this review.
2. P02: `wc -l` on both protocols, scheduler, and four named nodes. Exit 0.
3. P03: `sed` reads of all of `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`. Exit 0.
4. P04: combined `cat` of the four named nodes. Exit 0; tool display truncated, so no conclusion relied on this process alone.
5. P05-P08: four separate foreground `cat` reads of window, transfer, instances, and root nodes. All exit 0 and closed P04's display truncation.
6. P09-P12: four separate `sed` ranges covering every line of `operations/circdist/SCHEDULER.yaml`. All exit 0.
7. P13: package `find`/`stat` inventory. Exit 0; 13 regular files, zero symlinks and zero special files.
8. P14-P15: `cat` reads of `SHA256SUMS`, `README.md`, `source_audit.json`, and `LEDGER.md`. Both exit 0.
9. P16: full `cat` of `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`. Exit 0.
10. P17-P18: two numbered `sed` ranges covering all 713 lines of packaged `model.py`. Both exit 0.
11. P19: scratch nonexistence test followed by `mkdir /tmp/circdist_sat_instances_r55_review_20260826`. Exit 0.
12. P20: independent standard-library Python manifest parser. Exit 0: 13 files, 12 uniquely covered, manifest self-excluded, no unsafe/duplicate/missing/extra entries, all hashes matched.
13. P21: `shasum -a 256 -c SHA256SUMS`. Exit 0: 12/12 `OK`.
14. P22: `env PYTHONDONTWRITEBYTECODE=1 python3 -B verify.py`. Exit 0 in 4.06 s: 28/28 cells, 78 lower exclusions, 30,060 forward/backward comparisons, 354 restricted subsets, 28 measurement supermodels, 102 upper replays, 14/14 aggregates, 4/4 negative controls, `PASS`.
15. P23-P26: four separate foreground Python invocations of the packaged negative controls. Each terminated normally after the intended `AssertionError`: tampered upper, deleted projected effect, increased optimum, and dropped boundary metadata were rejected.
16. P27: standard-library JSON schema/count summary over all package JSON. Exit 0.
17. P28: `rg` discovery of relevant frozen definitions and reviews. Exit 0; display truncated and was followed by targeted reads.
18. P29: full `cat` request for the prior instances dossier. Exit 0; display truncated and was followed by section reads.
19. P30: Python extraction of certificate attribution summaries. Exit 0.
20. P31: foreground creation, permission check, and SHA-256 of clean-room `clean_room.py` under scratch. Exit 0.
21. P32: first clean-room execution. Exit 1 before mathematical execution with a `SyntaxError` (one missing parenthesis at line 382). No verdict was produced.
22. P33: numbered inspection of the failing scratch lines. Exit 0.
23. P34: scratch-only syntax correction and rehash. Exit 0; final checker SHA-256 `2c10fd7a32fdb278320b32348cccac06283dc70cc4d26aaf8ba4de386c7adc9e`.
24. P35: corrected clean-room execution. Exit 0 in 4.63 s with `CLEAN_ROOM PASS`: exact 576/96/16 census, 10,296 full assignments, 2,382 projected generators, 28 cells, 30,060 pairs, 78 lower exclusions, 354 restricted subsets, 28 measurement checks, 102 witnesses, and all three infinite pairs.
25. P36: first alternate-boundary attack invocation. Exit 1 with an `IndexError` caused by an omitted scratch-script argument, before an attack result was produced.
26. P37: corrected alternate-boundary attack. Exit 0: dropping both genuine endpoint slices admitted spurious weight-one logical signatures in every one of 28 cells.
27. P38: seven additional mutation tests in one foreground Python process. Exit 0: all seven mutations were rejected.
28. P39: full `cat` of the prior independent instances review. Exit 0.
29. P40-P41: two `sed` ranges covering the complete current instances/window-edge exact review. Both exit 0.
30. P42: Python exact claim/route/premise/root length, hash, and level audit. Exit 0.
31. P43: `rg` discovery across transfer/window proof records. Exit 0; display truncation led to targeted reads.
32. P44: targeted `sed` reads of the complete load-bearing window definitions, boundary equations, detector bridge, monotonicity, finite-window proof, and stabilization definition. Exit 0.
33. P45: `rg` heading map of the transfer proof. Exit 0.
34. P46: targeted `sed` reads of transfer Definitions 2.7/2.8/3.5, Lemma 2.9, Proposition 3.7, and section 8.1 mirror. Exit 0.
35. P47: `rg` heading map of the current transfer end-to-end review. Exit 0.
36. P48-P50: three `rg` inventories locating current transfer, bridge, and downstream reviews. All exit 0.
37. P51: `wc -l` on the three reviews and package repository-validation record. Exit 0.
38. P52-P53: `rg` of canonical source links and heading maps. Both exit 0.
39. P54: `cat repository_validation.txt`. Exit 0; it exposed the author-time evidence-closure failure before package directory linking.
40. P55-P56: targeted `sed` reads of the current transfer review's complete mathematical proof, exact claim, completion contract, and downstream binding. Both exit 0.
41. P57: `sed -n 59,183p` of the bridge-fold review. Exit 0; Lemma 2.9, Proposition 3.7, and the mirror were read in full.
42. P58-P59: targeted `sed` reads of the downstream scope-rebind review's hashes, schedule audit, finite-tail derivation, findings, and exact install rules. Both exit 0.
43. P60-P61: `du -sh .` and `du -sh .git`. Both exit 0 (`80M`, `24M`).
44. P62: numbered full read of the current instances node. Exit 0.
45. P63-P64: event-schema `rg` followed by the governing protocol range. Both exit 0.
46. P65: foreground Python `copytree`, excluding `.git`, `__pycache__`, and `*.pyc`, to create the 56 MB disposable candidate. Exit 0 in 0.69 s.
47. P66: exploratory certificate query. Exit 1 with `KeyError: distance`; it made no mutation and was replaced by schema-aware reads.
48. P67: schema-aware certificate first-cell read. Exit 0.
49. P68: foreground Python candidate installer. Exit 0: unchanged 422/1,310-character strings, both candidate levels `PROVED`, frontier absent.
50. P69: `rg --files tools maintenance tests ...`. Exit 2 only because no `tests/` directory exists; discovered the relevant tools under `tools/` and `maintenance/`.
51. P70-P71: validator target discovery and full `Makefile` read. Both exit 0.
52. P72: `proof_dag_check.py --help` in the candidate. Exit 0.
53. P73: `proof_dag_check.py --problem circdist --previous-state <real-repo> --write-generated`. Exit 0: prior nodes/routes/events retained; 16 nodes valid.
54. P74-P75: proof-DAG checks for `circdist` and `all`. Both exit 0: 16; then 85/144/16 nodes valid.
55. P76-P77: evidence closure for `circdist` and `all`. Both exit 0: 122 structured paths, all linked/project-local.
56. P78: `check_circdist_migration.py`. Exit 0: 16 nodes, 143 original events, 728 byte-identical copies.
57. P79: custom duplicate-rejecting PyYAML loader over the scheduler and 16 node YAMLs. Exit 0: 17/17 files duplicate-free.
58. P80: `test_release_contracts.py`. Exit 0: 14/14 tests.
59. P81: `test_dag_contracts.py`. Exit 0: 24/24 tests.
60. P82: `lean_dag_check.py --selftest`. Exit 0: 23/23 assertions.
61. P83: extra `verify_public_release.py` on the raw private checkout copy. Exit 1 with the pre-existing class of public-manifest/privacy errors (unmanifested private artifacts, raw-tree paths, and a manifest digest mismatch). This command audits a built public-release tree, not this node installation; the applicable release contract selftest P80 passed. No error from P83 is used as a waiver for any DAG/evidence/install check.
62. P84: full real/candidate path-hash comparison plus semantic assertion. Exit 0: only the candidate review placeholder was added and only the candidate node plus its two generated views changed; window, transfer, and root remained byte-identical; exact claim/route strings and levels passed.
63. P85: `git diff --no-index --check` on real versus candidate node. Exit 1 because the files intentionally differ, with empty output; there were no whitespace diagnostics.
64. P86: real-tree `git diff --check`. Exit 0, empty output.
65. P87: pre-write full path/symlink SHA-256 manifest excluding `.git` and the licensed review. Exit 0: 2,823 paths, aggregate `8109124c2d8333c66145822b3034c4063fc9e363788f389a6e70c1df9d8d6b4a`; target absent.
66. P88-P93: schema-aware targeted reads of exact input, effect-coverage, mechanism-definition, source-audit, and current source hashes. Two exploratory shape errors (P88/P90: `AttributeError`) terminated before any mutation; their corrected successors exited 0 and supplied the tables in this review.
67. P94: this scratch-only report generator. It writes only `/tmp/.../review_draft.md`; no repository mutation. Its result is checked in P95.
68. P95: scratch draft audit: exact required headings, balanced fences, candidate YAML parse, exact 422/1,310-character hashes, two `PROVED` levels, review locators, event set, and no frontier. It also compares every non-review repository path with P87. Exit 0.
69. P96: the final sealing process copies the verified draft to the sole licensed durable path, verifies byte identity, deletes `/tmp/circdist_sat_instances_r55_review_20260826`, confirms scratch absence, and prints the review SHA-256. It uses no subprocess and terminates before return.
70. P97-P101 are read-only post-seal commands: exact report hash/heading/YAML checks, proof-DAG `circdist` and `all`, migration, `git diff --check`, and the final one-file boundary audit. Results are reported in the final response; the node cannot yet link this review because this commission forbids canonical edits.

**Durable write boundary:** only `circdist/reviews/circdist_sat_instances_proof_certificates_exact_review_20260826.md` is written. Canonical nodes, scheduler, protocols, generated views, prior evidence, history, package, and tools remain read-only. The pre-write manifest excluding `.git` and this path covers 2,823 paths with aggregate SHA-256 `8109124c2d8333c66145822b3034c4063fc9e363788f389a6e70c1df9d8d6b4a`.

**Scratch cleanup:** the single scratch root `/tmp/circdist_sat_instances_r55_review_20260826` contains the independent checker, failed/corrected scratch scripts, mutation copies, candidate repository, validation placeholder, manifest, generator, and draft. P96 deletes that root recursively, verifies it is absent, and leaves no scratch path. Failed P32, P36, P66, P69, P83, P85, P88, and P90 left no process running; their exact causes are disclosed above.

## 14. Final decision matrix

| decision | result |
|---|---|
| package SHA-256 seal | PASS; complete 12-of-12 payload coverage plus self-excluded manifest |
| exact code/schedule inputs | PASS for selected standard member 1, class-D member 2, BB NI |
| physical full-Pauli/collision/projection model | PASS at exact uniform occupied-location scope |
| canonical/value-only detector bridges and both boundaries | PASS; arbitrary splits excluded |
| forward/backward and fault alphabet | PASS, 30,060 comparisons and complete 10,296 assignment coverage |
| all 28 distance cells | PASS; explicit legal upper and exhaustive lower in every cell |
| mechanism attributions | PASS at the restricted scopes in §7; temporal-boundary caveat retained |
| finite-to-infinite pairs | PASS: `(5,1)`, `(3,2)`, `(3,1)` |
| route | **PROVED**, unchanged exact implication/hash |
| node | **PROVED**, unchanged exact claim/hash |
| root | not adjudicated; no edit or promotion licensed |
| claim/implication repair | forbidden and unnecessary |
| sole installation | complete atomic YAML in §11 only |
| write boundary/FIX-2 | one durable report; strict serial; all processes terminated; scratch deleted before return |
