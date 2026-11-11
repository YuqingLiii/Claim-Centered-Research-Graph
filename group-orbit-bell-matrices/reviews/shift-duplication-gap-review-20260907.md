# Review of the strict shifted-duplication comparison

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact C10 claim and route `exact-comparison`,
with the reviewer-independence limitations disclosed below. The full-root
value is `20/3`, the doubled half-root value is `6`, and the gap is `2/3`.

## Independence and inspected scope

The reviewer did not author the C10 node/dossier, the C9 half-root proof,
or either author checker. The reviewer previously checked C7 independently
and authored its frozen D3-envelope review. Earlier in the same context,
the reviewer wrote a literature note containing the general block
normalization between half and full roots. Therefore this review does
**not** provide independent discovery of that normalization idea, and it
is not a fresh-context review. The explicit C10 permutation, assembled
premises, and numerical comparison were checked afresh. Same-model role
separation, shared context, and a common Python environment remain limits.

The reviewer read the current C10, C7, and C9 YAML statements; the complete
`shift-duplication-gap-20260907.md` (GAP-1--GAP-2); the complete
`d3-half-shift-value-20260907.md` (HS-1--HS-4); the C9 checker and author
run; and the completed `antipodal-half-shift-review-20260907.md`, especially
F2. The earlier C7 report and statement hashes were verified unchanged.
The C9 result was not assumed while its review was pending: its hand proof
was checked, its author checker was rerun, and a separate direct integer
calculation verified the comparison point before the completed C9 review
was used in the assembly.

The scope is precisely the stated D3 matrices and `lambda=1/3`.
No verdict is issued about novelty, arbitrary shifts, a general-r formula,
or optimal Grothendieck bounds. No earlier frozen review, author material,
or node was edited. This is not proof-assistant formalization or a
cross-model review.

## Frozen materials and exact replay

All following paths are relative to `grothendieck-group-orbit/`.

| Material | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.shift-duplication-gap.yaml` | `346a4914d5f8f9aedded95b05a27d8003142b2670dc3a08145a85aedf18333ff` |
| `proof-dag/nodes/GROTHORB.d3-shift-envelope.yaml` | `b6ae358b6f21e2a9b2a2993b441db9ca30256f6f09d5d54ce98aef834fe1ed96` |
| `proof-dag/nodes/GROTHORB.d3-half-shift-value.yaml` | `ff0e8978b86a7874264720194fb4a0719a28362190b44581a09e7ec078c0e334` |
| `artifacts/shift-duplication-gap-20260907.md` | `52d8189d8cb059a8ff50a802c37a902f904cb8dd110a102efe2132588ee33693` |
| `artifacts/d3-half-shift-value-20260907.md` | `41645cd84a2f70822e90b1ba41e984aaad54b61e16cd72503d229895fc28860a` |
| `tools/check_d3_half_shift_value.py` | `5209d8ff0c92b33dd2b581d718c4aad08abc2ee4038ea0b1c1de1dc89ef12a87` |
| `reviews/d3-envelope-review-20260907.md` | `ebc7c73ef64c6417f6d5ac4d6756a936d402fa74b9ae90d5dbf2b1400d53af18` |
| `reviews/antipodal-half-shift-review-20260907.md` | `7319bc9c80a02db1bc152bf862f50472ac5355d173e0f43066884b5f42904d49` |

The new [reviewer checker](../tools/check_shift_duplication_gap_review.py),
SHA-256 `a410b43c179ba4e6f7ae0309eddc4a64b57c45ed041587b10b436df3cb7a9daa`,
imports no author or earlier reviewer code. It checks every matrix entry,
enumerates all 4096 full-root Bob signs and all 64 half-root Bob signs at
the comparison point, and maximizes Alice exactly. Its results are
`max ||24(D(C)-I/3)t||_1=160` and
`max ||12(C-I/3)t||_1=36`. A fresh C9 author-checker replay also passes.

Commands and full outputs are frozen in
[reviewer rerun record](../artifacts/shift-duplication-gap-review-rerun-20260907.txt),
SHA-256 `5fbfa0335b8bade6713c22faabe9457a854d03285b8b70afd121f77ce40d1ad6`,
runs G1--G2. All mathematical input hashes in the table were unchanged
on rechecking before closeout. The separate C9 reviewer explicitly
confirmed its report frozen, and its reported file digest matched locally.

## F1. GROTHORB.shift-duplication-gap claim — PASS

`reviewed_hash: sha256:42ca35b7e34cad8f2c9527c0bf27cd279313da1375ee93dcdcb71a591ae722bf`

Exact parsed `claim.strip()`:

> Let U have rows e_i-e_j and e_i+e_j for 1<=i<j<=3, C=UU^T/4, and D(C)=(1/2)[C,-C;-C,C]. At lambda=1/3, beta_cl(D(C)-lambda I_12)=20/3 is strictly larger than 2*beta_cl(C-lambda I_6)=6.

The factors are consistent: writing `K=UU^T`,
`8D(C)=[K,-K;-K,K]`. Thus the full shifted integer matrix is
`24(D(C)-I/3)=3[K,-K;-K,K]-8I_12`, whereas the half shifted integer
matrix is `12(C-I/3)=3K-4I_6`. In G1 these are constructed separately
and exhaustively optimized without fractions inside the sign loops.
The exact maxima `160` and `36` normalize to `20/3` and `3`.
Doubling the latter yields `6`; subtracting gives the positive gap `2/3`.

There is no equality-preserving rescaling assumption hidden in this
comparison. The unrestricted full-root maximization includes all full
signs, while the half-root maximization includes all six-coordinate signs.
Independent Alice choices are eliminated by the exact l1 identity. Both
upper bounds and attainment are covered by the exhaustive finite maxima,
and the reviewed premise proofs supply further explicit witnesses.
Evidence: GAP-1--GAP-2; G1--G2; the premise findings used in F2 below.

## F2. Route exact-comparison — PASS

Target: `GROTHORB.shift-duplication-gap`, route `exact-comparison`.
Premises: `GROTHORB.d3-shift-envelope`, `GROTHORB.d3-half-shift-value`.

`reviewed_hash: sha256:c85fc4d43b22decda291f3e58ee4ab0d81de1654c8b864910b694e2adce749ab`

Exact parsed `implication.strip()`:

> Reordering the full roots as W=[U;-U] identifies A_3 with D(C) up to a simultaneous row and column permutation. Evaluating the full envelope at lambda=1/3 gives 20/3, whereas the half-root value gives twice 3, and 20/3>6.

With the dossier order `U=(12-,12+,13-,13+,23-,23+)`, define the
permutation matrix R by selecting, in order, the following one-based rows
of the original full-root W in dossier D3-1:

```text
(3,4,7,8,11,12,2,1,6,5,10,9).
```

Each original row occurs exactly once and `RW=[U;-U]`. Direct products
therefore give `R A_3 R^T=D(C)`; G1 checks all 144 entries. Since
`R I R^T=I`, the same holds after the identity shift. For any sign pair
`s,t`, the corresponding pair `Rs,Rt` is again a sign pair and preserves
the bilinear value. The inverse permutation proves equality of classical
maxima, not just an inequality in one direction.

The exact C7 premise has a completed PASS finding in
`d3-envelope-review-20260907.md`, F2, bound to current claim hash
`sha256:260cf713d4cd254ef432bf6fa2130718be433b157e0186f6f5cc386973b105d5`.
It applies at `lambda=1/3` because `1/4<=1/3<=1/2`, yielding
`8-4/3=20/3`. Its full-root normalization is exactly `WW^T/8`.

The exact C9 premise has a completed PASS finding in
`antipodal-half-shift-review-20260907.md`, F2, bound to current claim hash
`sha256:3905d276721ac794d0a04007c4ccaa948d1e392d904198da6899c70c81e24406`.
Its matrix and shift are exactly `UU^T/4-I_6/3`. In addition to reading
that review, this reviewer checked the hand certificate: signed endpoint
choices bijectively encode all 64 Bob vectors; occupancies are only
`(2,1,0)` or `(1,1,1)`, with the agreeing/canceling/balanced cases giving
integer l1 norms `36,24,36`. The all-ones pair attains 36. Thus C9 is
checked evidence, not an unresolved input silently assumed true.

The two reviewed results and the bijective permutation calculation imply
exactly F1. No general antipodal-shift theorem, literature claim, unshifted
base norm, or further classical conjecture is load-bearing. Operational
node levels were still OPEN in the inspected snapshots; this report
assesses the assembled implication after the premise reviews and does not
automatically modify those levels.

## Closeout and preservation

`reviewed_hash` is SHA-256 of UTF-8 after parsing YAML and applying
`claim.strip()` or `implication.strip()`; file digests are listed separately.
F1 and F2 are mathematical PASS findings for the exact recorded statements,
subject to the declared same-model and prior-context limitations.
The comparison disproves harmless doubling for this positive shift; it
does not challenge unshifted duplication or the shifted lower inequality.
Earlier frozen reports remain unchanged. This report and its new replay
artifacts are frozen on completion; node integration is left to the
coordinator.
