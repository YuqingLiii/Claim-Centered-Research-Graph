# Independent amendment review: repaired absolute-unbounded chain

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q2_probability_review`.

Independence declaration: this reviewer authored neither the proposer proofs nor the repaired
canonical objects. This amendment rechecks only the repairs requested by
`ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md`. It does not modify proposer artifacts,
canonical nodes, levels, generated views, or the prior immutable review.

## 1. Executive verdict

All four requested repairs **PASS**:

1. the Collins--Youn assumption now exposes the trace-zero coefficient hypothesis and exact norm
   interface used by the proof;
2. the Fukuda assumption now exposes Lemma 6.2, its exponent-zero cases, extension dimensions and
   source locator;
3. the repaired general pair-to-self claim now says constant **gap loss** and only
   linear-logarithmic dimension overhead, exactly matching the local proof; and
4. the absolute-unbounded theorem now has its own atomic outcome, while the invalid partial route
   on the full-size root is retained as retired provenance and removed from the root's completion
   basis.

The three premise nodes, the new atomic route implication, and the new atomic outcome claim are
eligible for `PROVED` promotion in the dependency order listed in Section 8. `HEXT.goal` is not
eligible for any promotion and must remain `OPEN`.

## 2. Exact repaired and new objects

Repository-normalized hashes recomputed from the current YAML are:

| object | exact hash | amendment verdict |
|---|---|---|
| `HEXT.finite-dimensional-unbounded-gap` claim | `sha256:1c62d358652bad37148e75956362e3f31c46c886eb7616620bceecc342ef40d2` | PASS |
| `HEXT.moe-to-holevo-transfer` claim | `sha256:b0e4b8570c8fc050c7d7a3b5f8527a0aa9594221f8e5112aff2b7492039a373f` | PASS |
| repaired `HEXT.pair-to-self` claim | `sha256:191443c198801c324a9a44716cfca413543230365292511b0924db6ce14137a2` | PASS |
| new `HEXT.absolute-unbounded-finite-dimensional-defects` claim | `sha256:acb04888dd0949c4d2a4163705880b5e9b2f131b386879fc93ddeccc21599940` | PASS |
| new `product-haar-with-finite-transfers` route implication | `sha256:692f1214cfdfc66668e98a60bb4d14aa86d3601c14979d10c3a8c420e524fd59` | PASS |
| `HEXT.goal` claim | `sha256:d0536aa01a3da8110034a57e85e61ff49d1ac8fe1737dba0e910016b0f580261` | remain `OPEN` |
| retired `HEXT.goal/finite-unbounded-route` implication | `sha256:3a1fac337de0f1d3061be345463ea90c9248100a70331d062f9f9b5a757bcdde` | retirement PASS; no promotion |

The current file hashes at review time were:

| file | SHA-256 |
|---|---|
| `HEXT.finite-dimensional-unbounded-gap.yaml` | `524f2ef23e5acfda3975bf3163c82aa92b79259890aa375ca68f869b943e883e` |
| `HEXT.moe-to-holevo-transfer.yaml` | `94ba1b2d38885dc2aa36992877eb377a64ec5e998a563f94a5f7da9189a57525` |
| `HEXT.pair-to-self.yaml` | `ababe2c586c4ad5380786f6d73d35bfc70dd6cdd88ff5a1339a200ad028fd86e` |
| `HEXT.absolute-unbounded-finite-dimensional-defects.yaml` | `da9a43b5939e2ca4257f794d51d052ca23ac6197edaca16bbdfeb88005f1f666` |
| `HEXT.goal.yaml` | `53b72ab95803eb0728198d421b86b24194618b743c1ad4eac90dff042cce2942` |
| `ABSOLUTE_UNBOUNDED_OUTCOME_ASSEMBLY_20260830.md` | `719a1cbe4fd9749dd8a1ad73cd34063c0323063933206315c94c8f12859fa81d` |
| prior independent review | `2211f84786a5b8ce229fde604e5552fa4a53c006a6f3b6cf03061568cc1ffaa2` |

## 3. Finding AUR-A01 — repaired Collins--Youn interface PASS

The canonical assumption now quantifies fixed integers `m>=1,J>=1`, defines the direct-product
words `u_v`, restricts to scalar coefficient matrices `a in M_(m^J)(C)` satisfying `Tr(a)=0`, uses
the Hilbert--Schmidt norm, and records the exact bound

`m^(J/2) sqrt((1+9/m)^J-1) ||a||_2`.

This matches Collins--Youn Theorem 3.3 at the cited local PDF pages and is precisely the external
interface used by the finite-net and complement argument. The Bordenave--Collins assumption still
records fixed generator/leg counts, independent Haar tuples on separate tensor legs, strong
convergence in probability, and the direct-product free-group limit. The proof uses it only at
`m>e^18`, well inside its source scope.

The claim text did not change, so the prior mathematical review remains bound to the same claim
hash. This amendment closes only the source-interface blocker.

**Verdict:** PASS and authorize promotion of
`HEXT.finite-dimensional-unbounded-gap` at
`sha256:1c62d358652bad37148e75956362e3f31c46c886eb7616620bceecc342ef40d2`
to `PROVED`, after linking this finding and retaining the nonconstructive/no-dimension-rate
caveats as scope limitations rather than unresolved premises.

## 4. Finding AUR-A02 — registered Fukuda interface PASS

The new node-level assumption accurately states Fukuda Lemma 6.2 for finite channels with output
dimensions `k,k'`, explicitly quantifies `m,n in N union {0}`, gives

`chi(tilde(Phi)^m tensor tilde(Omega)^n)`

`= log_2(k^m(k')^n)-S_min(Phi^m tensor Omega^n)`,

and records that `tilde(Phi)` maps `L(C^(k^2) tensor C^l)` to `L(C^k)`, with the analogous map for
`Omega`. The local PDF locator covers Lemma 6.2 and Eqs. (6.9)--(6.17), including the construction
and the exponent-zero statement.

Thus all three substitutions `(1,1),(1,0),(0,1)`, exact logarithmic cancellation, and the linear
input-dimension overhead are supported by a machine-visible external interface.

**Verdict:** PASS and authorize promotion of `HEXT.moe-to-holevo-transfer` at
`sha256:b0e4b8570c8fc050c7d7a3b5f8527a0aa9594221f8e5112aff2b7492039a373f`
to `PROVED`, after linking this finding.

## 5. Finding AUR-A03 — repaired general pair-to-self claim PASS

The changed claim no longer says that the general balancing construction has constant dimension
overhead. It now asserts:

- the gap loss is the constant `log_2(9/4)`; and
- input/output logarithmic dimension overhead is at most linear in the original logarithmic
  dimensions.

Both clauses follow from the reviewed artifact. With
`K=ceil(2^|chi(N)-chi(M)|)`,

`log_2 K < |chi(N)-chi(M)|+1`

and `chi(Phi)<=log_2 dim(output(Phi))`; tensoring the balancing branch with `Delta_K` therefore
adds at most a linear amount in the original logarithmic dimensions. The final direct sum adds at
most one further qubit beyond the larger branch. The four-block identity and `w>=4/9` give the
constant gap loss independently of this dimension bookkeeping.

The equal-Holevo special case remains valid and sharper (`g-1`, no balancing channel), but it is
not needed to prove the new atomic route because the repaired general theorem suffices.

**Verdict:** PASS and authorize promotion of `HEXT.pair-to-self` at its new exact claim hash
`sha256:191443c198801c324a9a44716cfca413543230365292511b0924db6ce14137a2`
to `PROVED`, after linking this finding.

## 6. Finding AUR-A04 — new atomic route and outcome PASS

The new outcome has the correct quantifier order: for each real `G>0`, it may choose different
finite-dimensional witnesses for the three clauses. Set

`H=G+log_2(9/4)+1`.

The first premise provides an MOE pair defect greater than `H`; the second preserves it exactly as
a Holevo pair defect; and the third gives a same-channel defect at least

`H-log_2(9/4)=G+1>G`.

Applying the first premise separately at target `G` supplies the stated MOE clause. No uniform
dimension, common witness, explicit matrix, or dimension-growth rate is claimed. The route lists
all three load-bearing unresolved premise nodes and uses no unregistered external theorem.

Unlike the former root route, this implication proves the parent claim actually written. The node
caveats correctly exclude explicitness and full-size scaling.

**Verdict:** PASS for route implication
`sha256:692f1214cfdfc66668e98a60bb4d14aa86d3601c14979d10c3a8c420e524fd59`
and PASS for outcome claim
`sha256:acb04888dd0949c4d2a4163705880b5e9b2f131b386879fc93ddeccc21599940`.
The route may be promoted to `PROVED` after linking this finding. The outcome may be promoted to
`PROVED` only after the route implication and all three premise nodes are `PROVED` and are cited in
its completion basis.

## 7. Finding AUR-A05 — wrong-parent retirement PASS; full-size root stays OPEN

`HEXT.goal/finite-unbounded-route` remains present with its original implication hash, now carries
the prior independent review and exact hash binding, states the precise partial-result caveat, and
has a dated `retired` record. It has been removed from `HEXT.goal.assessment.basis.routes`.

The root links the new atomic outcome only as `kind: node-evidence`, expressly describing it as
non-completing progress. This is the correct relationship: absolute unboundedness is established,
but the fixed-depth convergence argument supplies no bound on `D(J)` and hence no defect lower
bound proportional to full primitive logarithmic size.

**Verdict:** retirement and rehoming PASS. Do not promote the retired route. Do not add the new
atomic outcome as a completing route premise for the full-size claim. Keep `HEXT.goal` at `OPEN`.

Collateral note: the still-`CONJECTURED` `matched-tensor-route` uses the older phrase “constant
overhead/loss.” The repaired general pair-to-self result gives constant gap loss but only
linear-logarithmic dimension overhead. Linear overhead is enough to preserve an `Omega(m)` scaling
when the original dimensions are `O(m)`, but that separate route implication should be reworded
before any future completion review. This does not affect the atomic absolute-unbounded chain.

## 8. Dependency-order promotion authorization

The integrator may perform the following exact sequence:

1. link Finding AUR-A01 and promote `HEXT.finite-dimensional-unbounded-gap` to `PROVED`;
2. link Finding AUR-A02 and promote `HEXT.moe-to-holevo-transfer` to `PROVED`;
3. link Finding AUR-A03 and promote `HEXT.pair-to-self` to `PROVED`;
4. link Finding AUR-A04 at the route assessment and promote
   `product-haar-with-finite-transfers` to `PROVED`;
5. after verifying all three premises and the route implication are `PROVED`, link the distinct
   claim-level part of Finding AUR-A04 and promote
   `HEXT.absolute-unbounded-finite-dimensional-defects` to `PROVED`; and
6. remove discharged review frontiers, append exact level-change events, regenerate views, and run
   structure/evidence/scope/contract checks.

This authorization applies only to the exact hashes in Section 2. It authorizes no change to
`HEXT.goal`, any full-size route, any all-copy leakage node, or any explicitness claim.

## 9. Limitations

The promoted atomic theorem would be a finite-dimensional existence result. It would still give
no printable matrices, no computable finite threshold for `D`, no uniform probability statement
as `J` grows, and no rate relative to full input/output/environment logarithmic size. It must not
be conflated with the same-tuple Werner/SU(3) certificate program or with Hayden--Penington
full-size extensivity.

Only public proof artifacts, canonical interfaces, and local primary-source statements were used
as evidence; hidden or private chain-of-thought material was neither requested nor used.

## 10. Validation record

Read-only checks run after writing this amendment:

- `python3 tools/proof_dag_check.py --problem holevo-extensive-violation` — PASS, 145 node files;
- `python3 tools/check_holevo_three_question_scope.py` — PASS, 163 canonical Holevo nodes across
  three independent projects and no WHGAP canonical dependency;
- `PYTHONPATH=tools python3 -m unittest tools.test_dag_contracts tools.test_release_contracts` —
  PASS, 38 tests; and
- `python3 tools/evidence_closure_check.py --problem holevo-extensive-violation` — expected sole
  failure for this newly written, not-yet-linked amendment. Linking its applicable findings during
  the authorized integration should close that orphan without changing the review itself.
