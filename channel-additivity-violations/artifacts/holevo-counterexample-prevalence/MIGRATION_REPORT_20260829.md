# Migration report — 2026-08-29

This problem was separated from the former combined additivity workspace so that every meaning of
“many counterexamples” is tracked without changing ambient spaces or quantifiers.

- Source root: `channel-capacity/additivity-gap/notes/chatgpt-four-rounds/`
- Historical files retained: `round-2-audit.md`, `round-2-counterexample-prevalence-raw.md`
- Destination names: `round-2-audit.md`, `round-2-raw.md`
- Canonical graph: six YAML claim nodes under `proof-dag/nodes/`
- Execution policy: further work is local Codex work; the web transcript is inert evidence only.

Verification compared both migrated files after CRLF/LF and terminal-blank-line normalization. Both
comparisons passed. Random-model probability, relative openness, full-space density, explicitness
and dimension thresholds remain distinct claims in the new DAG.
