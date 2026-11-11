# Independent adversarial review: finite-dimensional absolute-unbounded chain

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q2_probability_review`.

Independence declaration: this reviewer did not author the canonical nodes, the proposer proof
artifacts, or the proposer adversarial audit reviewed here. This is a read-only mathematical and
protocol audit under `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`. No proposer artifact, canonical
node, existing review, generated view, or evidence level was modified.

## 1. Executive verdict

The mathematical core of the absolute-unbounded construction **passes**:

1. for fixed `m,J`, Bordenave--Collins strong convergence can be uniformized over the finite-
   dimensional traceless coefficient sphere by a finite net;
2. this produces the claimed global, all-input side entropy lower bound;
3. the conjugate Bell input gives the stated product upper bound;
4. choosing an integer `m>e^18` and then increasing `J` gives finite-dimensional p=1 MOE pair
   defects unbounded in absolute size;
5. Fukuda Lemma 6.2 explicitly includes the exponent-zero cases and therefore transfers the
   numerical pair defect exactly to one-shot Holevo defect; and
6. for the equal-Holevo conjugate pair, the direct-sum conversion loses at most one bit, so the
   finite-dimensional same-channel Holevo defect is also absolutely unbounded.

The current canonical chain nevertheless **does not qualify for completion-level promotion**.
There are three exact-interface blockers:

- `HEXT.finite-dimensional-unbounded-gap` omits the load-bearing `tr(a)=0` hypothesis from its
  machine-visible Collins--Youn assumption;
- `HEXT.moe-to-holevo-transfer` has no machine-visible assumption for Fukuda Lemma 6.2; and
- `HEXT.pair-to-self` claims constant additive qubit overhead for the general balancing
  construction, while its own proof establishes only overhead linear in the original logarithmic
  dimensions. Constant overhead is valid for the equal-Holevo special case used here, not for the
  exact general claim currently written.

There is also a route-placement blocker. The exact `HEXT.goal/finite-unbounded-route` implication
states that it settles only the absolute-unbounded subquestion and **not** the full-size extensive
subquestion. Under `DAG_PROTOCOL.md`, a route implication must establish the parent claim actually
written. It therefore cannot be promoted as a completed route of the full-size root. The proved
partial result needs its own atomic outcome node. `HEXT.goal` must remain `OPEN`.

## 2. Exact objects reviewed

Repository-normalized statement hashes are:

| object | exact statement hash | verdict |
|---|---|---|
| `HEXT.finite-dimensional-unbounded-gap` claim | `sha256:1c62d358652bad37148e75956362e3f31c46c886eb7616620bceecc342ef40d2` | mathematical PASS; canonical assumption repair required |
| `HEXT.moe-to-holevo-transfer` claim | `sha256:b0e4b8570c8fc050c7d7a3b5f8527a0aa9594221f8e5112aff2b7492039a373f` | mathematical PASS; machine-visible assumption missing |
| `HEXT.pair-to-self` claim | `sha256:ab44daaaad29356785282792eb6f2ddd3d2c0af8a8328ea6f2360be2eebee375` | BLOCK: overhead clause is not proved and conflicts with artifact |
| `HEXT.goal` claim | `sha256:d0536aa01a3da8110034a57e85e61ff49d1ac8fe1737dba0e910016b0f580261` | remain `OPEN` |
| `HEXT.goal/finite-unbounded-route` implication | `sha256:3a1fac337de0f1d3061be345463ea90c9248100a70331d062f9f9b5a757bcdde` | mathematical partial-result PASS; BLOCK as route to this parent |

The inspected canonical file hashes at review time were:

| file | SHA-256 |
|---|---|
| `proof-dag/nodes/HEXT.finite-dimensional-unbounded-gap.yaml` | `35f7687e68c1ba4669ef4398b7090799e00f61616e499f989b479be66fb726a1` |
| `proof-dag/nodes/HEXT.moe-to-holevo-transfer.yaml` | `f8f5a3242f7ab66c7bd5efd25326df07abfe51368f50c1f14628f21b9b7a0a48` |
| `proof-dag/nodes/HEXT.pair-to-self.yaml` | `b41d48a4af7c56f1fc1bd32631f66e6016a4886c6d014b90a7d69a523e8d93ea` |
| `proof-dag/nodes/HEXT.goal.yaml` | `3c4a503fd2b5495ca26c5e244a980249f48458e695b880783cb10a540e8a1ab3` |

The principal proof and source files were:

| file | SHA-256 |
|---|---|
| `artifacts/FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md` | `47c0fbe2fe49370923977627040f08f82eddfb409b239012e9ce3cdc6a25814f` |
| `artifacts/MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md` | `02b3f8a59ec1e7d34817cb41258584adeac55960a351ad97c24e28fab98d13a6` |
| `artifacts/PAIR_TO_SELF_REDUCTION_2026-08-29.md` | `a6899bd93f5339995d2f24bbb625a14abacf3d795100f9f7c836193518e081b6` |
| Collins--Youn local PDF | `70c97a9e4c17218e17f159e00f3bc554011fa6f87b8966be494c97af0d726714` |
| Bordenave--Collins local PDF | `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac` |
| Fukuda local PDF | `bbb6248128249479273ae62d697f7e7db9043af851b4f77a7428dffac485e917` |
| Fukuda--Wolf local PDF | `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7` |

The local primary PDFs were read at the cited theorem pages, rather than relying only on the
project's prose summaries.

## 3. Finding AU-IR-01 — source theorems and assumptions

### Collins--Youn

Theorem 3.3, local PDF p. 11, states that for `a in M_(m^J)(C)` **with `tr(a)=0`**,

`||sum_(v,w) a_(v,w) u_v^* u_w||`

`<= m^(J/2) sqrt((1+9/m)^J-1) ||a||_2`.

This is exactly the theorem used in Step 1. The artifact correctly restricts to traceless
coefficients. The canonical assumption does not: it says only that Theorem 3.3 bounds the
coefficient operator. The omission is material, because the theorem is not an unrestricted
coefficient estimate. The direct-proof node therefore does not yet make all of its load-bearing
external input machine-visible.

Required repair: replace the assumption statement by the displayed theorem with the quantified
integers, the direct-product generators `u_v`, the `tr(a)=0` hypothesis, the Hilbert--Schmidt norm,
and the exact constant. The node claim itself need not change.

### Bordenave--Collins

Theorem 9.2 and Eq. (69), local PDF pp. 62--63, use independent Haar unitaries `U_(i,j)` placed on
separate tensor legs and prove strong convergence in probability, for every fixed generator count
and fixed number of legs, to the regular representation of the direct product of free groups.
The current assumption records the needed fixed-parameter quantifiers, random model, probability
mode, and limiting group. It is adequate for this proof.

**Verdict for this finding:** the source use is mathematically sound, but
`HEXT.finite-dimensional-unbounded-gap` cannot be promoted until the Collins--Youn assumption is
repaired. This finding is bound to claim hash
`sha256:1c62d358652bad37148e75956362e3f31c46c886eb7616620bceecc342ef40d2`.

## 4. Finding AU-IR-02 — finite-net uniformization really is all-input

For fixed `m,J`, the traceless Hilbert--Schmidt unit sphere in `M_(m^J)` is compact and finite
dimensional. The coefficient-to-operator maps in both the finite and limiting representations
have Lipschitz constant at most `m^J`, since there are `m^(2J)` coefficients and
`sum |a_(v,w)| <= m^J ||a||_2`. Strong convergence applies to each element of a finite net, and a
finite union bound gives one event on which all net points converge. The common Lipschitz bound
then extends the estimate to every traceless coefficient matrix.

The quantifier order is correct:

`fix m,J,eta; take D -> infinity; obtain probability -> 1; choose one finite successful D and tuple`.

No uniform event over varying `J` is asserted or needed for absolute unboundedness. For each target
gap one first selects a finite `J`, then a finite `D`. This proves existence but supplies no rate
for `D(J)`.

The complement calculation also has the required global scope. For every density matrix `S`,
`X=L^c(S)-I/q` is Hermitian and traceless, duality applies the uniform coefficient estimate to
that `X`, and `S >= S_2` yields the entropy lower bound. Restriction to pure inputs only occurs
after this global estimate, when channel/complement nonzero spectra are equated. Thus the proof is
not merely a selected-input or finite-net-of-inputs argument.

**Verdict for this finding:** PASS for the mathematical claim at hash
`sha256:1c62d358652bad37148e75956362e3f31c46c886eb7616620bceecc342ef40d2`,
subject to Finding AU-IR-01's canonical-assumption repair.

## 5. Finding AU-IR-03 — Bell witness, positivity, and absolute unboundedness

For each layer, the `m` equal-index labels all produce the same Bell vector because
`(U tensor bar(U))|Omega>=|Omega>`. Merging those labels produces probabilities `1/m` and
`1/m^2` with multiplicities one and `m^2-m`; the Shannon entropy is exactly
`2 log_2(m)-(log_2 m)/m`. Tensoring the `J` Bell inputs makes the output a product across layers,
so the joint entropy upper bound is `J` times the one-layer bound.

After subtracting the two side bounds, the coefficient is

`c_m=(log_2 m)/m-2 log_2(1+9/m)`.

The inequalities `ln(1+9/m)<9/m` and `ln m>18` imply `c_m>0`. Choosing any fixed integer
`m>e^18`, then increasing finite `J`, and finally choosing a successful finite `D` gives defects
at least `J c_m/2`. This is a valid finite-dimensional existence proof for every requested finite
gap.

The proof's optional `m=J=2^30` calculation is also arithmetically consistent and yields a lower
bound above two bits for sufficiently large finite `D`; it is not an explicit matrix witness.

**Verdict for this finding:** PASS at the same finite-dimensional-unbounded claim hash, with no
dimension-rate or explicitness extrapolation.

## 6. Finding AU-IR-04 — Fukuda transfer, including exponent zero

Fukuda Lemma 6.2, local PDF pp. 11--12, states explicitly for
`m,n in N union {0}` that

`chi(tilde(Phi)^m tensor tilde(Omega)^n)`

`= log_2(k^m (k')^n)-S_min(Phi^m tensor Omega^n)`.

Therefore the uses `(m,n)=(1,1),(1,0),(0,1)` are authorized by the primary source; absent tensor
factors are not a project-invented convention. Subtracting the latter two equations from the first
cancels both logarithmic terms and preserves the numerical MOE pair defect exactly.

Equation (6.10) maps `L(C^(k^2) tensor C^l)` to `L(C^k)`, so the local dimension budget is also
correct: the extension adds `2 log_2 k` input qubits and leaves the output dimension `k`. This is
linear overhead in the original logarithmic dimensions.

The exact canonical claim is mathematically correct. But this route-free direct proof imports
Fukuda Lemma 6.2 and has no `assumptions` block. Under the protocol, the theorem's exact statement,
scope, source path, and locator must be registered at node level.

**Verdict for this finding:** mathematical PASS at claim hash
`sha256:b0e4b8570c8fc050c7d7a3b5f8527a0aa9594221f8e5112aff2b7492039a373f`,
but no promotion until the machine-visible Fukuda assumption is added and an amendment confirms
the repair.

## 7. Finding AU-IR-05 — pair-to-self algebra passes; exact overhead claim does not

The direct-sum identity

`chi(A direct-sum B)=log_2(2^chi(A)+2^chi(B))`

is correctly proved in the local artifact and agrees with Fukuda--Wolf Proposition 1(4). The
balancing identity `chi(A tensor Delta_K)=chi(A)+log_2 K`, preservation of the cross gap, four-block
expansion of `T tensor T`, and log-sum-exp lower bound are all correct.

For a general balanced ratio `a/b in [1/2,2]`,

`w=2ab/(a+b)^2 >= 4/9`,

so the general same-channel lower bound is

`chi(T tensor T)-2chi(T) >= g-log_2(9/4)`.

If `chi(N)=chi(M)`, no balancing channel is used, `w=1/2`, and the sharper special bound is

`chi(T tensor T)-2chi(T) >= g-1`.

The exact canonical claim nevertheless says the *general* construction has “only constant
additive qubit overhead.” Its proof says instead

`log_2 K < |chi(N)-chi(M)|+1`

and bounds this by a quantity linear in the original logarithmic output dimensions. In a family,
that is generally `O(m)`, not `O(1)`. The final direct sum itself adds at most one qubit beyond the
larger balanced branch, but the preceding classical balancing side channel need not.

This is not cosmetic: the exact node claim and its own dimension-bookkeeping section assert
different asymptotic overheads. Two valid repairs are available:

1. change the general claim to “only linear overhead in the original logarithmic dimensions”; or
2. split out an equal-Holevo special node asserting the `g-1` bound and at most one additional
   direct-sum qubit, which is the only interface needed by the present conjugate construction.

**Verdict for this finding:** BLOCK promotion of exact claim hash
`sha256:ab44daaaad29356785282792eb6f2ddd3d2c0af8a8328ea6f2360be2eebee375`.
The gap inequalities pass, but the overhead clause does not.

## 8. Finding AU-IR-06 — the scoped absolute-unbounded chain is valid

Replacing each product-Haar side by a complementary channel preserves the individual and joint
minimum output entropies: on pure inputs a channel and a chosen complement have the same nonzero
output spectrum, and a tensor product of chosen complements is a complement of the product
channel. The replacement also preserves equal output dimensions and equality of the two side
minimum entropies.

After Fukuda transfer,

`chi(tilde(L))=log_2 k-S_min(L)` and
`chi(tilde(R))=log_2 k-S_min(R)`,

so the two one-shot Holevo quantities are equal. Consequently this construction uses the symmetric
`g-1` direct-sum corollary, not the general `g-log_2(9/4)` bound and not the potentially large
classical balancing channel. The direct sum adds at most one qubit beyond equal-dimension branches.

It follows that the following scoped proposition is proved mathematically:

> Finite-dimensional p=1 MOE pair defects, finite-dimensional Holevo pair defects, and
> finite-dimensional two-copy same-channel Holevo defects are unbounded in absolute size.

The construction does **not** prove full-size extensivity. Strong convergence is invoked only after
`J` is fixed, and the selected matrix size `D(J)` is uncontrolled. The obtained gap is `Omega(J)`
while the primitive input logarithmic dimension includes `J log D(J)`. No `Omega(full log size)`
conclusion follows.

**Verdict for this finding:** PASS for the displayed scoped proposition only. This finding does not
license any full-size, regularized self-leakage, all-copy, or explicit-family claim.

## 9. Finding AU-IR-07 — `finite-unbounded-route` is attached to the wrong parent

The exact route implication at
`sha256:3a1fac337de0f1d3061be345463ea90c9248100a70331d062f9f9b5a757bcdde`
ends by saying that it settles the absolute-unbounded subquestion “but not the stronger
full-size-extensive subquestion.” The parent `HEXT.goal` claim explicitly asks for the full-size
`Omega(m)` problem as well as the absolute subquestion.

`DAG_PROTOCOL.md`, node-level audit item 4, requires that “the implication proves the parent claim
actually written.” An argument that expressly proves only one subquestion cannot be a completed
route to the combined full-size parent. This remains true even if every premise is later promoted.

Required graph repair:

- create a separate atomic outcome node whose exact proposition is the scoped statement in
  Finding AU-IR-06;
- attach the finite-unbounded route to that node;
- use the equal-Holevo pair-to-self interface, or repair the current general pair-to-self node;
- keep the absolute-unbounded result as non-completing progress evidence for `HEXT.goal`; and
- keep `HEXT.goal` and all full-size routes `OPEN` unless a separate cost-controlled proof passes.

**Verdict for this finding:** BLOCK promotion of `HEXT.goal/finite-unbounded-route` in its current
location. This is a protocol/interface failure, not a refutation of the absolute-unbounded
mathematics. `HEXT.goal`, hash
`sha256:d0536aa01a3da8110034a57e85e61ff49d1ac8fe1737dba0e910016b0f580261`,
must not be upgraded.

## 10. Promotion matrix

| object | promotion authorized now? | exact reason / repair |
|---|---:|---|
| `HEXT.finite-dimensional-unbounded-gap` | no | add exact trace-zero Collins--Youn assumption, then amendment-review the unchanged claim |
| `HEXT.moe-to-holevo-transfer` | no | register Fukuda Lemma 6.2, including `m,n>=0`, dimensions and locator, then amendment-review |
| `HEXT.pair-to-self` | no | repair general overhead to linear-logarithmic, or split the equal-Holevo `g-1` constant-overhead atom |
| `HEXT.goal/finite-unbounded-route` | no | rehome to a separate absolute-unbounded outcome; it does not imply the current parent |
| `HEXT.goal` | no | full-size `Omega(m)` remains unresolved |

After those exact repairs, a short independent amendment may authorize the first two direct-proof
nodes and the new equal-Holevo/absolute-unbounded chain without redoing the already passed algebra.

## 11. Scope limitations

This review establishes no explicit matrices and no computable threshold for `D`. It establishes
no probability statement uniform in a growing depth, no fixed-partner theorem, no same-tuple
all-copy leakage bound, no regularized positive rate for one fixed primitive channel, and no
Hayden--Penington full-size extensive violation. The reviewed product-Haar construction uses
independent Haar tuples on different tensor legs and must not be conflated with the separate
same-tuple Werner or SU(3) certificate programs.

No hidden or private chain of thought was used as evidence; the findings above are based only on
the public artifacts, canonical interfaces, primary-source statements, and displayed derivations.

## 12. Validation record

The following read-only checks were run from the repository root after writing this report:

- `python3 tools/proof_dag_check.py --problem holevo-extensive-violation` — PASS, 144 canonical
  node files structurally valid;
- `python3 tools/check_holevo_three_question_scope.py` — PASS, three independent Holevo projects
  and no WHGAP canonical dependency;
- `PYTHONPATH=tools python3 -m unittest tools.test_dag_contracts tools.test_release_contracts` —
  PASS, 38 tests; and
- `python3 tools/evidence_closure_check.py --problem holevo-extensive-violation` — expected single
  failure because this new immutable review is not yet linked from a canonical assessment. The
  integrator must link only the applicable blocked/pass findings during the repair; the review must
  not be linked as if it authorized the current claims or route for promotion.
