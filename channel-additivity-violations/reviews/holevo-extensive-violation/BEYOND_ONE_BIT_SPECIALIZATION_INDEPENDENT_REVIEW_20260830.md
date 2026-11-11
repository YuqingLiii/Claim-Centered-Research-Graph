# Independent review: strict beyond-one-bit specialization

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Scope and independence

I did not author `HEXT.beyond-one-bit`, its new route, or the absolute-unbounded premise. I read
`DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full. This review checks only the strict `G=1`
specialization, the three separate existential clauses, the completion basis, compatibility with
the isotropic one-bit certificate cap, and non-propagation to the full-size root.

## Immutable inputs and exact hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `HEXT.beyond-one-bit.yaml` | `4979da7484df2e21490fa7d2865d6c3aa479beb9552747f862a2e80aa236fdfe` |
| absolute-unbounded premise YAML | `38f1cdac34763aa84b634a99dcd5888a3254918c29fec0d9d39d67617257112d` |
| `HEXT.goal.yaml` | `15226339bee71fedbed78ea09c9cb1754c623208340fb0163db283500d11cda5` |
| absolute-unbounded assembly artifact | `719a1cbe4fd9749dd8a1ad73cd34063c0323063933206315c94c8f12859fa81d` |
| isotropic one-bit-cap artifact | `27eb3db5fb3c2e68b34b236c3b233b778560d97b8b5f9ba10ffcf664207551d5` |

The exact reviewed statement hashes independently recompute to:

| object | exact statement hash |
|---|---|
| `HEXT.beyond-one-bit` claim | `sha256:2542ce5b98fc9591048dcc2a597fb64825a106f1c215c416d9ce254c91199059` |
| route `absolute-unbounded-specialization` implication | `sha256:07ac64093012fa3ef2977b67a6e8dae42efa11d7675809c14dee4a6cbed12a4f` |
| proved premise claim | `sha256:acb04888dd0949c4d2a4163705880b5e9b2f131b386879fc93ddeccc21599940` |
| full-size root claim | `sha256:d0536aa01a3da8110034a57e85e61ff49d1ac8fe1737dba0e910016b0f580261` |

## Finding HEXT-B1-IR-01 -- PASS: strict `G=1` specialization and three clauses

The premise `HEXT.absolute-unbounded-finite-dimensional-defects` is currently `PROVED`. Its exact
claim states, for **every real `G>0`**, three separate finite-dimensional conclusions:

1. an MOE pair defect strictly greater than `G`;
2. a one-shot Holevo pair defect strictly greater than `G`; and
3. a same-channel two-copy Holevo defect strictly greater than `G`.

Substitution of the allowed target `G=1` gives strict `>1`, not `>=1`, in all three clauses. The
new affirmative claim preserves the existential quantifiers correctly. It does not require the
MOE pair, Holevo pair, and same-channel witness to be the same channels or have the same dimensions;
neither does the premise.

**Verdict:** the route implication at
`sha256:07ac64093012fa3ef2977b67a6e8dae42efa11d7675809c14dee4a6cbed12a4f`
PASSes. Because its sole premise is already `PROVED`, the route is eligible for proposer-side
promotion to `PROVED`.

## Finding HEXT-B1-IR-02 -- PASS: exact affirmative claim and completion basis

The exact target claim contains precisely the three conclusions obtained in Finding HEXT-B1-IR-01:
finite-dimensional MOE pair existence above one bit, finite-dimensional Holevo pair existence above
one bit, and one finite channel `T` with `chi(T tensor T)-2chi(T)>1`.

Its `assessment.basis.routes` lists only `absolute-unbounded-specialization`. The older
`unbounded-gap-route`, whose premises remain proposer-side, is visible for provenance but is not
load-bearing in the completion basis. Thus no unresolved premise is silently imported into the
new proof.

**Verdict:** the claim at
`sha256:2542ce5b98fc9591048dcc2a597fb64825a106f1c215c416d9ce254c91199059`
PASSes and becomes eligible for proposer-side `PROVED` after the specialization route is promoted.

## Finding HEXT-B1-IR-03 -- PASS: no conflict with the isotropic one-bit cap

The separate one-bit-cap artifact concerns only a single channel/conjugate-channel Bell witness
whose tested joint output is one isotropic state. It explicitly does not bound arbitrary joint
inputs, arbitrary channel pairs, or a tensor product of several nonidentical isotropic layers.

The absolute-unbounded construction escapes that scope by using products of distinct layers; its
total Bell output is a tensor product, not one isotropic state in the cap theorem's hypothesis. The
Holevo pair and same-channel clauses are then obtained by finite transfer reductions rather than by
claiming a single isotropic Bell certificate above one bit.

**Verdict:** PASS. “There exist defects above one bit” and “this restricted isotropic certificate
is capped by one bit” are logically compatible.

## Finding HEXT-B1-IR-04 -- PASS: no propagation to the full-size root

The specialization proves only a fixed absolute threshold. Even the stronger premise proves
absolute unboundedness without a rate in the full logarithmic input/output/environment size. The
root `HEXT.goal` additionally asks for an `Omega(m)` defect in that full primitive size, and its
completion routes still have open or conjectured load-bearing premises.

`HEXT.beyond-one-bit` is not a completing premise or route of `HEXT.goal`; the root separately
records the absolute-unbounded theorem only as non-load-bearing partial progress and remains
`OPEN`.

**Verdict:** PASS. This review authorizes no promotion of `HEXT.goal` and no full-size extensive
claim.

## Final staged disposition

1. Link this review to route `absolute-unbounded-specialization` at Finding HEXT-B1-IR-01 and exact
   implication hash `07ac6409...`, then promote that route.
2. Link it to `HEXT.beyond-one-bit` at Findings HEXT-B1-IR-02--04 and exact claim hash
   `2542ce5b...`, then promote the claim.
3. Leave `HEXT.goal` unchanged at `OPEN`.

No other route or canonical node is authorized for promotion by this review.

