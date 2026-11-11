# Exact mixed-sector reduction in the frozen Gross conventions

Let a named mixed Pauli mechanism be represented by its CSS components
`(N_X,N_Z)`, where `N_X` and `N_Z` are subsets of the common 360-name
universe and a name in both components is one physical `Y`-type location.
Its physical named weight is

```text
|N_X union N_Z|.
```

The frozen propagation model is CSS-linear.  The X and Z detector syndromes
are the syndromes of the two components, and the mixed logical action is the
ordered pair of their logical actions.  Therefore:

1. an undetected mixed mechanism has zero syndrome in each component;
2. a nontrivial mixed logical action has a nontrivial X or Z component; and
3. for either component `S`, `|N_S| <= |N_X union N_Z|`.

Consequently, every undetected nontrivial mixed mechanism of total named
weight at most 10 contains an undetected nontrivial same-sector mechanism of
named weight at most 10.  A schedule for which both complete unrestricted
direct-360 sector queries are checked UNSAT therefore also has no mixed
mechanism of that weight.  Conversely, a positive mixed mechanism cannot
exclude a schedule that its nontrivial same-sector component does not already
exclude.

For combinations drawn from the reviewed post-iteration-136 selector spans,
the checked full-span theorems show that any such component with a new named
mask is absent; a component with an installed mask supplies no new exclusion.

This reduction uses the common name universe and frozen CSS decomposition. It
does not assert that the reviewed selector spans contain every physical
mechanism, and it does not extend the order-6 or span results to another
schedule, frontier, non-CSS model, higher fault-weight bound, or arbitrary
mechanism family.
