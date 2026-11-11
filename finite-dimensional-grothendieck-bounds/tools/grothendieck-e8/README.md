# E8 tools

`e8_certificate_checker.py` performs exact rational construction of the E8
roots, conversion to the simple-root coordinates, positive-root poset
enumeration, and the recorded extremal `F_k` checks.

`e8_dual_certificate_checker.py` is an independent implementation: it builds
the roots by Weyl-reflection closure, enumerates filters through their unique
minimal antichains, checks the tight-frame and Bell-matrix identities, and
constructs the explicit `A1+A6` sign witness attaining `6104`.

Both scripts use only exact integer/rational arithmetic.
