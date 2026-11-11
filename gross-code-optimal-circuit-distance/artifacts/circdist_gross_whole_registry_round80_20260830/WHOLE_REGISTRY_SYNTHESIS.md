# Whole-registry synthesis and comparison

Four approaches were compared before the outer loop.

1. Installed-union prime implicates can be strong, but exact enumeration/proof extraction over 144 local checks was less feasible under the memory limit.
2. Multi-selector BDD/SAT universal projection is general, but a monolithic diagram risks obscuring raw selector provenance and proof memory.
3. Factorized GF(2) relations compress signatures well, but signature equality alone does not supply a physical selector for every retained tuple.
4. Exact star hitting-cuts over the complete raw pair truth preserve constructive selectors, permit an exhaustive/disjoint center partition, and support compact full-product proofs.

The fourth method was selected. Search examined 27,142 star seeds. Classification: raw sound=457; zero-domain rejected=2,461; unsound=0; non-synergistic=48,905; dominated-old=77; covered by the full evolving union=54; retained strict expansions=24; sound but not selected under the deterministic packaging budget=302. Budget exclusions are positive sound candidates, not absence results.

All 24 strict-outside witnesses are complete 144-check local-order assignments. Every stored selector stream is deterministic and binds center order, leaf order, canonical support, physical support, and fault count. See `whole_registry/hitting_synthesis/factorized_selector_proofs.json(.gz)`.
