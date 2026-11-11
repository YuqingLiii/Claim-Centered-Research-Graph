#!/usr/bin/env python3
"""Replay the exact near-extremizer W_9 audit.

The substantive finite-field/biquadratic computation is shared with the
rank-one CG checker.  Its main routine now also certifies the closest
one-coordinate sign-flip shell and the exact ten-block ratio threshold.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


CHECKER = Path(__file__).with_name("h4_cg_rankone_identity_checker.py")
spec = importlib.util.spec_from_file_location("d4_cg_rankone_checker", CHECKER)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


if __name__ == "__main__":
    module.main()
