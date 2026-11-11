# Read-only amendment review: centered Werner canonical integration

Date: 2026-08-30

Reviewer: independent Codex integration-audit context `/root/centered_scope_bridge`.

Independence declaration: this reviewer did not author the three canonical nodes audited here,
the centered-moment assembly, or its mathematical independent review. This is a read-only
post-registration audit under `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`. No YAML, generated view,
or existing review was changed.

## 1. Executive verdict

The three-node decomposition is structurally right:

1. `HEXT.werner-centered-reversal-return-bound` owns the exact trace/reversal and return estimate;
2. `HEXT.same-tuple-werner-centered-bound-large-m` owns the fixed-`m>e^18`, fixed-`eta>=0`
   probabilistic centered theorem; and
3. `HEXT.same-tuple-real-werner-sector-large-m` owns the downstream two-dimensional coefficient
   consequence.

The exact registered claim hashes are all correct. The large-`m` route and real-Werner route hashes
also match the statements previously reviewed. The identity dimensions and `A/m` normalization are
consistent: `I_(d^2)` is the centered output identity, `I_(m^2)` is the coefficient-space identity,
and the deterministic spectral equivalence uses exactly the target `A/m`.

There is one required completion-level repair and one evidence-closure repair:

- the current large-`m` route implication at `sha256:e073...` imports the explicit witnesses
  `D=32768,alpha=43` from inside the proof of an existential premise claim. It must be replaced by
  the independently approved existential-interface implication at `sha256:0c09...`, or the graph
  must first expose those constants in a new exact public premise node; and
- the final mathematical review is presently unlinked, so evidence closure reports it as an
  orphan. Its applicable findings must be linked during integration.

Apart from those repairs, the registration **PASSES**. In particular, a `PROVED` route implication
with one unresolved premise is legal: route-implication review and premise completion are separate
obligations. The real-Werner parent correctly remains `CONJECTURED`, so no completion level has
propagated across the unresolved centered premise.

## 2. Immutable inspected objects

| object | SHA-256 |
|---|---|
| `nodes/HEXT.werner-centered-reversal-return-bound.yaml` | `8f0bdb644e210e9441fa204752d408a61f8e73141b3a9c28f42e4ea29030a52f` |
| `nodes/HEXT.same-tuple-werner-centered-bound-large-m.yaml` | `139940e947d9e76acd0c67894ac491b614358aa7577b8d581539fffc055e4d0b` |
| `nodes/HEXT.same-tuple-real-werner-sector-large-m.yaml` | `787307f6b8e0b03674727fe6fb693e3368fa7b13547571cecfc930a489ff2548` |
| broad centered node | `50df56947e1e82be1757ab67e62a9e724e2094ad4735f36ebc4e97989dc517c2` |
| arbitrary-Hermitian same-tuple node | `e01981d247a4d459b13ac22d92efd7f580607624a437244944d0c21808aa4871` |
| prior scope review | `94a1b6ab1d536fefda48dfab3c1a35d4cff276668b1fa8ac67272733eb3ae0b7` |
| final mathematical review | `9a688594b6572f4b22a29079a1c6462df643ea82fb730a2d5ddda431fa91c2d3` |
| reviewed shortened assembly | `1a5979c3d9e341d9ba540110b11628fccd441bfc8ecf87901a04743d538c6c64` |

Repository-normalized statement hashes recomputed from the current YAML are:

| object | exact hash | audit verdict |
|---|---|---|
| reversal/return claim | `sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a` | exact match; PASS |
| large-`m` centered claim | `sha256:d882dca3c30783b1a7d9f6a6cec79a66317b23ea26800fe2a2306263d1eb6670` | exact match; PASS |
| current large-`m` route implication | `sha256:e073d6e258a2e06b513bcd2c7a71c7bcf19023d14314ec469ef4b3065f83c319` | exact match; mathematical PASS but protocol interface repair required |
| real-Werner-sector claim | `sha256:ad940ef6f776d5a94f7ecb3e679332863bdac1efde961c34ac3dc4ec855b0411` | exact match; PASS |
| real-Werner route implication | `sha256:78bcb08e2f33b40bf8abd232ca2b51b4238da7abffd878bd7008cf9672141126` | exact match; PASS |

The structural checker reports all 141 project nodes valid. At the start of this audit the
centered-route evidence-closure failure was the unlinked
`WERNER_CENTERED_MOMENT_FINAL_CONDITIONAL_ASSEMBLY_INDEPENDENT_REVIEW_20260830.md`. After this
read-only report was written, this amendment is necessarily also unlinked until the integrator
applies its findings. The checker additionally reports two concurrently created source-bound
certificate tools outside this three-node audit; this report makes no finding about them.

## 3. Finding WCCIA-01 — reversal/return atom PASS

The atom is genuinely self-contained at its intended interface:

- `A_(v,a)=U_v^*U_a` implies `A_(v,a)^*=U_a^*U_v`;
- removing `v=a` is exactly the subtraction `R_U-I_(d^2)/m`;
- the second tensor trace is the complex conjugate of the block-reversed forward product;
- the `m^(-2N)` normalization, factor `2d^2`, and base `(3m-4)/m^2` agree with the reviewed
  return calculation; and
- the node-level Akemann--Ostrand assumption states the exact external theorem, scope `m>=2`,
  representation, source note, and bibliographic locator.

Its exact claim passed Finding WCMF-IR-08 of the final mathematical review. The current
`CONJECTURED` level is conservative and legal.

**Repair instruction:** link
`WERNER_CENTERED_MOMENT_FINAL_CONDITIONAL_ASSEMBLY_INDEPENDENT_REVIEW_20260830.md`, Finding
`WCMF-IR-08`, with reviewed hash
`sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a`; then promote the node to
`PROVED`, remove the discharged review caveat/frontier, and append a level-change event. Do not add
an artificial empty-premise route.

## 4. Finding WCCIA-02 — large-`m` claim PASS; current route needs one repair

The node claim correctly binds every symbol needed by the probability statement:

- `U_j^(d)` varies with `d` and consists of independent Haar unitaries in `U(d)`;
- `R_U` is an operator on `C^d tensor C^d`;
- `I_(d^2)/m` therefore has the correct identity dimension;
- `A=1+9(1+eta)^2/m` and
  `H=sqrt((A^2-1)(1-m^(-2)))` are explicit; and
- the order of quantifiers is every fixed integer `m>e^18`, every fixed `eta>=0`, then
  `d->infinity`.

The premise list contains the seven atoms approved in Finding WCMF-IR-08:

1. `HEXT.werner-centered-reversal-return-bound`;
2. `HEXT.werner-two-boundary-constellation-count`;
3. `HEXT.werner-admissible-equality-component-genus-bound`;
4. `HEXT.werner-two-component-low-genus-return-separation`;
5. `HEXT.werner-two-component-nonreturn-weighted-count`;
6. `HEXT.werner-monotone-weingarten-tail-summability`; and
7. `HEXT.werner-constellation-euler-deficit`.

This list is complete and not under-specified. In particular, do **not** duplicate
`HEXT.werner-contraction-skeleton-ribbon-injection`, the planar node, the minimal-Catalan node, or
the positive-genus node. Their load-bearing claims are already machine-visible below the aggregate
connected and disconnected atoms, and the final reviewer explicitly checked the exhaustive
contraction-skeleton interface. The cyclic-reversal collision and surgery nodes are not used by
the final absolute assembly.

The only defect is the public-interface mismatch identified in Finding WCMF-IR-10. The current
route text uses `32768,43`, whereas its listed connected-count premise publicly asserts only the
existence of `D,alpha` with `D<sqrt(18m)`. A parent route imports the public premise claim, not a
stronger witness hidden inside that premise's proof dossier.

**Preferred repair instruction:** replace only the route implication by the exact
existential-interface text in Section 3.4 of the final mathematical review, whose reviewed hash is

`sha256:0c09e4e2f6afb70b6364c7e69b7e1892fa113826a91dc1474ceaa824bb58a937`.

Keep the seven premises unchanged. Change the route review link from the old `e073...` scope-only
binding to the final review findings `WCMF-IR-01--WCMF-IR-10`, bound to `0c09...`. Preserve the
prior scope review as historical/supplemental evidence, but it cannot remain the completion hash
for a changed implication. Append the required route-level change event.

The alternative repair allowed by Finding WCMF-IR-10 is to create a new exact connected-count atom
exposing `D=32768,alpha=43`, use it in place of the existential node, and keep `e073...`. That adds
an avoidable node; the existential-interface implication is cleaner.

After the reversal/return premise and all six existing premises are `PROVED`, the repaired
`0c09...` route and exact claim `d882...` may promote to `PROVED` with the final mathematical
review linked at both objects. The prior scope-review links remain appropriate as non-completion
quantifier evidence.

## 5. Finding WCCIA-03 — real-Werner consequence and conditional route PASS

The coefficient-sector conventions are correct:

- `Y` belongs to `M_(m^2)` and its identity is therefore `I_(m^2)`;
- `F_m` is the flip on `C^m tensor C^m` under the already proved spectral-reduction premise;
- the target is exactly `||M_U(Y)||_infinity <= (A/m)||Y||_2`; and
- `A`, the Haar tuple, and the fixed-parameter quantifiers are inherited from the explicitly named
  large-`m` centered node.

`M_U` and `F_m` are reachable definitions through the explicit
`HEXT.same-tuple-werner-spectral-reduction` premise and its linked exact artifact. Rewriting the
claim merely to repeat those definitions is unnecessary and would invalidate both existing exact
review hashes. The current notation is unambiguous in this graph.

The route implication is `PROVED` while the centered premise is unresolved. This is explicitly
legal under the DAG protocol: the truth of a route implication and the completion of its premises
are separate obligations and may be reviewed in either order. The node assessment remains
`CONJECTURED`, cites the route conditionally, and states the unresolved premise, so there is no
illegal automatic propagation.

The scope-review links at exact route hash `78bcb...` and claim hash `ad940...` are appropriate:
that review independently audited precisely this deterministic event-level implication and its
non-consequences. When the centered premise becomes `PROVED`, link Finding WCMF-IR-09 as the final
assembled-scope review and promote only this node. No new mathematical route is needed.

## 6. Finding WCCIA-04 — broad-node links PASS without overreach

The link from `HEXT.same-tuple-werner-centered-bound` to the large-`m` node is
`kind: node-evidence`, explicitly says “non-load-bearing,” and states that the strict
`m>e^18` subclaim cannot promote the broader all-fixed-`m` claim. This is exactly the allowed
non-load-bearing cross-reference. The broad node remains `CONJECTURED`.

The link from `HEXT.same-tuple-two-leg-scalar-strong-norm` to the real-Werner-sector node is also
`kind: node-evidence`, explicitly restricts itself to the real two-dimensional coefficient span,
and does not list the scoped node as a route premise. The general arbitrary-Hermitian node remains
`OPEN`. This is also protocol-correct.

Neither link reaches global physical `n=2`, any all-copy purity statement, the separate
absolute-unbounded construction, or the full-size root. No scope propagation beyond the reviewed
sector was found.

## 7. Exact integration order

1. Integrate Finding WCMF-IR-08 into the reversal/return atom and promote it to `PROVED`.
2. Replace the large-`m` route implication `e073...` by reviewed implication `0c09...`; leave its
   seven premises unchanged and add the final-review binding and event.
3. Promote the repaired large-`m` route and node using the final mathematical review at their exact
   hashes.
4. With both premises complete, link Finding WCMF-IR-09 and promote the real-Werner consequence;
   its already `PROVED` implication may remain unchanged.
5. Preserve both broad cross-references as non-load-bearing evidence and change no broader node
   level.
6. Regenerate `NODE_INDEX.md` and `GRAPH.mmd`, then run the project validator, all-project
   validator, evidence-closure checker, scope checker, and `git diff --check`.

Until steps 1--3 are done, the current graph is structurally valid but the centered integration is
not evidence-closed because the final mathematical review and this read-only amendment are not yet
linked. It is correct for the three node levels to remain `CONJECTURED`, `CONJECTURED`, and
`CONJECTURED` respectively, with only the downstream route implication at `PROVED`.
