# Project-specific mathematical checkers

Every Python file in this directory is linked from at least one k-Sum claim
node. These programs support the mathematics rather than repository
maintenance. They provide exact finite-instance checks, numerical stress
tests, and counterexamples or obstruction certificates for candidate proof
routes. Shared DAG validation code remains in the repository-level `tools/`
directory.

The `l2p*` programs test successive level-two constructions and their failure
modes, the `l2r*` programs check exact moment and dual obstructions, and the
`l3*` program audits a representation-theoretic finite case. A checker remains
here when its result supports either a surviving route or a retained failed
route in the public graph.
