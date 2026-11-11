# Exact restart license

This proposer package freezes an **unstarted** iteration 54 frontier:

```text
1,440 reviewed unary
+   20 round-62
+4,740 reviewed round-69 generalized
+  566 reviewed round-72 generalized
+  134 round-74 proposer generalized
+  108 exact dynamic
=7,008 installed blocks.
```

The exact files are:

- `restart/dynamic_blocks_iteration54.json.gz`;
- `restart/installed_generalized_terms_iteration54.json.gz`;
- `restart/online_mechanism_registry_iteration54.json.gz`;
- `restart/restart_state.json`.

Continuation is licensed only after a fresh independent exact review accepts this candidate package and its 134 generalized terms. A continuation must preserve the strict online sequence, generate both unrestricted direct sectors for every SAT outer, treat timeout/UNKNOWN as no conclusion, require candidate-specific DRAT/LRAT acceptance for absence, and enter repair only after dual checked absence.

This license is not canonical installation, root closure, or evidence of exhaustion.
