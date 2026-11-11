# D4 tools

`h4_exact_instance_checker.py` is the compact primary checker for the locally
closed witness chain.  It requires `numpy` and `h5py` and verifies the frozen
MAT-file hash, canonical integer matrix hash, exact sign value, exact
`Q(sqrt(5))` Gram identity, rank four, and exact vector value.  It does not run
an optimizer.  It also verifies `AP=lambda P` and an exact residual row-square
bound proving that `range(P)` is the strict top singular space of `A`.  It does
not claim the classical sign-vector upper bound.

The top level also contains replay programs extracted from preserved export
bundles. `bootstrap/` contains earlier instance-dependent programs recovered
from the source workspace. Their required source files are now under
`artifacts/frozen-instance/`; some large moment-map intermediates remain absent.

The normalized top-level replay programs also cover the exact H4 spectrum,
affine equality terminals, local cut-polytope no-go results, q-cell reduction,
and two independent-form fixed-support p-cut certificates. Programs requiring
scientific Python declare their dependencies in their module docstrings; the
proof-DAG and evidence validators themselves require only the repository root
requirements.
