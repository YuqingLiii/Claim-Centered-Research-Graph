# CIRCDIST proof DAG

[Index](NODE_INDEX.md) · [Graph](GRAPH.mmd) · [Nodes](nodes/)

There are 16 stable node IDs and four explicit roots. Routes are AND-hyperedges;
different routes are alternatives. A route's implication and its premise claims
have separate assessments. No level is automatically propagated.

The governing contracts are [DAG_PROTOCOL.md](../../DAG_PROTOCOL.md) and
[FILE_PROTOCOL.md](../../FILE_PROTOCOL.md). Every completed assessment retains
the same reviewed hash as before migration. Mathematical wording edits require
their own approval and exact-statement review; rearranging files is not such a review.

Legacy events remain inside each node's linked original dossier. New research
events, when there is new research, are appended under `events` using the current
protocol; no migration or housekeeping event was fabricated.
