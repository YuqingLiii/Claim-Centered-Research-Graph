# Atomic absolute-unbounded outcome assembly

Date: 2026-08-30

Status: historical pre-amendment proposer-side graph-repair snapshot. At the time of this artifact,
the mathematics below had passed `ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md`, while
the new exact node and repaired premise interfaces still awaited a fresh hash-bound amendment
review. That review subsequently passed and the canonical atomic outcome was promoted to `PROVED`;
the node YAML is authoritative for its current status.

## 1. Exact scoped outcome

For every real `G>0`:

1. there are finite-dimensional channels `L,R` with

   `S_min(L)+S_min(R)-S_min(L tensor R)>G`;
2. there are finite-dimensional channels `A,B` with

   `chi(A tensor B)-chi(A)-chi(B)>G`; and
3. there is a finite-dimensional channel `T` with

   `chi(T tensor T)-2chi(T)>G`.

Thus finite-dimensional p=1 MOE pair defects, one-shot Holevo pair defects, and one-shot
same-channel two-copy Holevo defects are all unbounded in absolute size.

This is not a statement about defect divided by the full logarithmic input/output/environment
cost. It does not settle Hayden--Penington full-size extensivity.

## 2. Three-premise proof

Fix `G>0` and put

`H=G+log_2(9/4)+1`.

The premise `HEXT.finite-dimensional-unbounded-gap` supplies finite channels `L,R` whose p=1 MOE
pair defect is greater than `H`. The premise `HEXT.moe-to-holevo-transfer` constructs finite
Weyl-flag extensions `A,B` with exactly the same numerical Holevo pair defect. Hence their Holevo
pair defect is greater than `G`.

Apply `HEXT.pair-to-self` to `A,B`. Its repaired exact claim gives a finite channel `T` satisfying

`chi(T tensor T)-2chi(T) >= H-log_2(9/4) > G`.

The first conclusion follows by applying the first premise directly with target `G`. This proves
all three clauses without any dimension-rate estimate.

## 3. Why the full-size root route is retired

The historical route `HEXT.goal/finite-unbounded-route` explicitly concluded that it settled only
absolute unboundedness and not full-size extensivity. It therefore did not imply the full parent
claim under the DAG protocol. The present atomic outcome owns exactly the partial theorem that the
route actually proved. The historical route remains visible as retired provenance, while
`HEXT.goal` remains `OPEN`.

## 4. Repair ledger

Independent review required the following exact repairs before completion:

1. expose `Tr(a)=0` and the complete Collins--Youn coefficient estimate on
   `HEXT.finite-dimensional-unbounded-gap`;
2. register Fukuda Lemma 6.2, including exponent-zero cases and dimensions, on
   `HEXT.moe-to-holevo-transfer`;
3. replace the false general constant-dimension-overhead clause of `HEXT.pair-to-self` by the
   proved linear-logarithmic overhead statement; and
4. place the assembled conclusion on this atomic outcome rather than on the full-size root.

All four repairs were represented canonically at the time of this snapshot. They did not by
themselves authorize promotion, so the changed/new exact objects then required an amendment review.
That review subsequently passed; the canonical node YAML records the current `PROVED` status and
the binding review evidence.

## 5. Strict boundary

The construction is finite dimensional but nonconstructive in the matrix entries. For each fixed
product depth it selects a sufficiently large finite matrix dimension after a probability limit.
It supplies no computable threshold, no printable tuple, no fixed-partner theorem, no growing-depth
probability statement, no all-copy same-tuple estimate, and no `Omega` lower bound in the full
primitive logarithmic size.
