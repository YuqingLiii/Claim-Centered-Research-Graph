# Independent review: Q1 upstream dependency closure and quantifiers

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Independence and scope

I did not author the canonical nodes or proposer artifacts reviewed here. I previously reviewed the
dephasing Weyl preservation and direct-transfer layer in a separate immutable report; the main
agent subsequently promoted both exact objects to `PROVED`. This second review asks only whether
those promotions close any higher route or root, and whether the existential/universal quantifiers
compose without changing witnesses or scopes.

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full. I inspected the current canonical Q1 DAG,
the Hastings, pair-to-self, fixed-channel, direct-transfer and root nodes, the local proof artifacts,
Hastings Theorem 1 on local PDF page 2, Shor's regularized Holevo formula on local PDF page 3, and
Fukuda--Wolf Propositions 1 and 2 on local PDF pages 1--3. I used no web source.

This review does not revisit the internal Weyl entropy proof, does not review the universal Shor
equivalence node, and does not address Q2, Q3, special additive classes, quantum capacity, private
capacity, or any capacity-threshold project. It changes no canonical evidence level.

## Executive verdict

The new `PROVED` Weyl layer is necessary but **not sufficient by itself** to promote the Q1 root.
The current root route still has two `CONJECTURED` premises:

```text
HAEQ.hastings-moe-counterexample
HAEQ.pair-to-self-reduction
```

The root route implication also uses the finite-dimensional HSW regularization formula to pass from
`chi(T tensor T)>2chi(T)` to `C(T)>chi(T)`, but that external theorem is not machine-visible in the
route's `assumptions`. A prose source inside `proof.sources` is not a substitute for an assumption
entry under the DAG protocol.

The mathematical quantifier chain itself is correct:

```text
exists finite MOE-violating pair
  -> exists finite extended Holevo-violating pair
  -> exists finite self-violating channel T
  -> C(T)>chi(T).
```

It never proves that the original Hastings channel is the Holevo witness, and it does not prove
nonadditivity for every channel.

Exact status recommendations are:

1. the Hastings existential node passes source and quantifier review and is eligible for `PROVED`;
2. the pair-to-self claim and algebra pass, but its canonical external assumption must first be
   repaired to state the exact Fukuda--Wolf direct-sum identity and cite the primary PDF directly;
3. the fixed-channel regularization claim is mathematically sound but currently lacks a
   machine-visible HSW assumption and is not needed as a root premise if the smaller theorem is
   registered directly on the root route; and
4. the root route and root node remain below completion tier until both premises are `PROVED`, the
   route-level HSW assumption is registered, and the exact repaired assembly is accepted.

## Immutable inputs

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| root node YAML | `3d7aa68632cd3619ee6d4a48fedbd12930b250ce81a55ac9a52f256068e66390` |
| Hastings node YAML | `e0f5cf3dbb920c66febc17388e5c92137d8a8b4bf94215df927c65862fb02533` |
| pair-to-self node YAML | `62c8cbc7f5c8ddc86a418d51a1dd909c1f067cab534045782f913d7dff3f8fa2` |
| fixed-channel node YAML | `89d87f35e8f5154c006f4e048417fb2b278026be44ff09367d8a687c8667cc00` |
| promoted direct-transfer node YAML | `87cd0c183db924362287880779b0f992dd2fea607dba1f7761ec765e8dda0e43` |
| promoted Weyl-preservation node YAML | `505011ea5e90ecedaf6a95ed3628fbb94d56aecaaad9a3da3ec5819b3ff1083b` |
| pair-to-self proof artifact | `720c0cb33faaa1a0c4e5addfa94e857ee1ce81215d7fd2ac1909c50d8abd0e98` |
| primary-source audit artifact | `3f812edfee361cd76cbe79d4d522be0b167148ab0178e02d171cd786bcac984e` |
| fixed-channel proof artifact | `e33394e599441a015d7e95a5e654152465261034937eb73c9463779ed20393a5` |
| Hastings local PDF | `b303560e5794e9b12b7c7f4145b4cd7958a6dd8ab83b61eb7947befca3348b98` |
| Shor local PDF | `300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6` |
| Fukuda--Wolf local PDF | `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7` |
| Weyl/direct-transfer independent review | `caede3873b1e5ea6872f891d909d8a701f3f82a5f9bd9b180135009952d19bb7` |

Hashes below use the repository's exact frozen-statement convention.

## Exact reviewed objects

| object | exact statement hash |
|---|---|
| `HAEQ.hastings-moe-counterexample` claim | `sha256:e6f972b2ec4389be96a66d39628b67af0d0c053573a4184e5b63d2c897f14374` |
| `HAEQ.pair-to-self-reduction` claim | `sha256:0fc7daa37324f6e68dc4987f959c831fc4dc48ad8c6c4054df16a397d9143c9f` |
| `HAEQ.fixed-channel-regularization` claim | `sha256:ae6bd7c5b610c197e3a5c418633dab91b67e1f9ebc5e8e9c2991134799909b8f` |
| root route implication | `sha256:2b2940d578ed8f68e77161ff1b093258781ac2e90f365b97953b0f8206ad3d4d` |
| `HAEQ.goal` claim | `sha256:9e8fb7187a75cbc4455edea653a8c7f241bf0af92d3f8d9cb25094457dadea11` |

## Findings

### Finding Q1UD-01 -- PASS: the newly proved Weyl layer is closed but does not auto-propagate

`HAEQ.weyl-extension-moe-preservation` and both the route and claim of
`HAEQ.direct-moe-to-holevo-transfer` are now `PROVED` with exact review hashes. Their only
load-bearing relation is internally closed. Under the DAG protocol this does not automatically
promote a parent route: every other premise and the parent implication must be independently
complete.

The direct-transfer quantifier is universal over finite channel pairs. Applying it to the one
finite pair supplied by Hastings is legitimate. Its caveat that the extensions change the channels
prevents witness confusion and must remain load-bearing context in any root summary.

### Finding Q1UD-02 -- PASS: Hastings existential claim and quantifiers

Hastings Theorem 1, local PDF page 2, states that for sufficiently large finite `D`, and then
sufficiently large finite `N` depending on `D`, a Haar-random finite random-unitary channel
`E` has, with nonzero probability,

```text
Hmin(E tensor conjugate(E)) < Hmin(E) + Hmin(conjugate(E)).
```

The displayed equality to `2Hmin(E)` uses conjugation invariance. Nonzero probability on a finite
random-channel model implies existence of a deterministic finite-dimensional pair. This is exactly
the existential content of `HAEQ.hastings-moe-counterexample` at claim hash `e6f972...`; it says
neither that every large channel violates additivity nor that the same channel later witnesses
Holevo nonadditivity.

The canonical assumption is locatable through the source-audit artifact and accurately records the
order of quantifiers. Directly citing the primary PDF page would be cleaner but is not mathematically
necessary. This exact Hastings node is eligible for `PROVED` when this finding is linked.

### Finding Q1UD-03 -- mathematical PASS, protocol repair required: pair-to-self

Let `a=chi(N)`, `b=chi(M)`, and
`chi(N tensor M)=a+b+delta` with `delta>0`. Fukuda--Wolf Proposition 1(4) gives

```text
chi(direct_sum_i T_i) = log_2(sum_i 2^(chi(T_i))).
```

For `T=N direct_sum M`, the four flagged blocks of `T tensor T`, product-ensemble
superadditivity on the two diagonal blocks, and swap-unitary invariance on the two cross blocks give

```text
2^(chi(T tensor T))
 >= 2^(2a) + 2*2^(a+b+delta) + 2^(2b)
 >  (2^a+2^b)^2
 =  2^(2chi(T)).
```

Thus the exact claim at `0fc7...` is mathematically correct and finite-dimensional. Its existential
quantifier is also exactly the contrapositive content of Fukuda--Wolf Proposition 2(2).

The current assumption block is nevertheless not completion-ready. It says only that
direct-sum constructions “reduce universal strong additivity to self-additivity and preserve strict
failure,” while the local proof load-bearingly imports the exact Proposition 1(4) formula. The DAG
protocol requires that exact imported statement and scope to be machine-visible. The minimal repair
is to replace the assumption by:

```text
For every finite family of finite-dimensional channels T_i,
chi(direct_sum_i T_i)=log_2(sum_i 2^(chi(T_i))).
```

with source `artifacts/primary-sources/fukuda-wolf-0704.1092.pdf`, Proposition 1(4), PDF pages
1--2. After that source-interface repair, this finding supports promotion of the unchanged claim
hash `0fc7...`; before it, the node must remain below completion tier.

### Finding Q1UD-04 -- conditional mathematical PASS, current protocol FAIL: root route

The exact route implication at `2b2940...` composes its three displayed premises correctly:

1. Hastings supplies one finite MOE-violating pair `(N,M)`.
2. The universal direct-transfer theorem constructs a new finite pair `(N',M')` with the same
   positive Holevo defect. No assertion about `chi(N)` or `chi(M)` is made.
3. The pair-to-self theorem constructs a finite channel `T` with
   `chi(T tensor T)>2chi(T)`.

These are existential choices nested under universal implications, so there is no illicit exchange
of `for all` and `there exists` and no requirement that any witness be preserved between steps.
The self-violation immediately refutes universal finite-dimensional Holevo additivity.

The last clause, `C(T)>chi(T)`, additionally uses the finite-dimensional HSW theorem

```text
C(T)=lim_(n->infinity) chi(T tensor n)/n,
```

together with product-ensemble superadditivity (equivalently Fekete) to obtain
`C(T)>=chi(T tensor T)/2>chi(T)`. Shor records the regularized Holevo formula on local PDF page 3.
This is an established external theorem, but the current root route has no `assumptions` block and
therefore hides a load-bearing external input from the canonical dependency interface.

The minimal repair is a route-level assumption with exactly the displayed finite-dimensional HSW
statement and source `artifacts/primary-sources/shor-quant-ph-0305035.pdf`, PDF page 3. Adding the
broader `HAEQ.fixed-channel-regularization` as a fourth premise is valid but unnecessary.

Even after that repair, the route cannot be `PROVED` until both the Hastings and repaired
pair-to-self premises are `PROVED`. With those conditions met, the exact unchanged implication hash
`2b2940...` passes this dependency-and-quantifier review.

### Finding Q1UD-05 -- PASS mathematically, not currently completion-ready: fixed-channel lemma

The proposer proof of `HAEQ.fixed-channel-regularization` has the correct quantifiers. For
`a_n=chi(N tensor n)`, product ensembles make `a_n` superadditive, the HSW theorem and Fekete give
`C(N)=sup_n a_n/n`, and `a_n>=na_1`. Hence `C(N)=a_1` if and only if every `a_n=na_1`.

However, the node has no canonical `assumptions` block for the HSW theorem, so the exact claim at
`ae6bd...` is not presently eligible for `PROVED`. This node is not a premise of the root route and
should not be added merely to close the easier implication needed there. If independently useful,
register the exact finite-dimensional HSW formula at node level and then use this finding for the
unchanged claim hash.

### Finding Q1UD-06 -- current root node remains CONJECTURED

The root claim at `9e8fb...` is the correct existential conclusion and does not say that every
channel is nonadditive. Once the repaired root route is `PROVED`, its claim follows exactly and no
additional fixed-channel all-copy statement is required. At the current snapshot, however, its
only route is not completion-ready for the reasons in Findings Q1UD-03 and Q1UD-04. The root must
therefore remain `CONJECTURED`.

No result in this dependency chain licenses an unrestricted statement about a specified original
channel, all channels, quantum capacity, private capacity, or the prevalence or size of violations.

## Exact promotion frontier

In dependency order:

1. **Now review-eligible:** promote only `HAEQ.hastings-moe-counterexample` at `e6f972...` after
   linking Finding Q1UD-02.
2. **One source-interface repair away:** repair the exact Fukuda assumption on
   `HAEQ.pair-to-self-reduction`; then the unchanged claim `0fc7...` is review-eligible.
3. **Optional and non-load-bearing:** register HSW at node level before promoting
   `HAEQ.fixed-channel-regularization` at `ae6bd...`.
4. **Still blocked:** register the minimal HSW assumption on the root route and ensure Hastings and
   pair-to-self are both `PROVED`; only then may route `2b2940...` and root claim `9e8fb...` be
   promoted in order.

The already proved Weyl preservation and direct transfer need no further review for this assembly.
