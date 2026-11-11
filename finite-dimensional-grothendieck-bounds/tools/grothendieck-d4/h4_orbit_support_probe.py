#!/usr/bin/env python3
"""Exact replay of the H4 witness-orbit support facts used in the cut audit.

Run from the repository root with a Python environment containing numpy and
h5py.  The script reuses the already audited signed-group constructor; all
comparisons and support counts are discrete/integer operations.
"""

import collections
import importlib.util
import json
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "grothendieck-d4/tools/h4_invariant_vanishing_probe.py"
MAT = ROOT / "grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")


def load_probe_module():
    spec = importlib.util.spec_from_file_location("h4_probe", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    probe = load_probe_module()
    with SYSTEM.open() as f:
        data = json.load(f)

    generators = [
        (
            np.asarray(g["perm"], dtype=np.uint16),
            np.asarray(g["sign"], dtype=np.int8),
        )
        for g in data["group"]["coxeter_generators"]
    ]
    group_p, group_s, _, _ = probe.generate_group(generators)

    with h5py.File(MAT, "r") as f:
        A = probe.exact_int_matrix(f["A"][()], "A")
        ax = probe.exact_sign_vector(f["ax"][()], "ax")
        by = probe.exact_sign_vector(f["by"][()], "by")

    target = int(ax @ A @ by)
    orbit = set()
    support_histogram = collections.Counter()

    for p, s in zip(group_p, group_s):
        # Pullback action.  The set obtained is identical to the pushforward
        # orbit because the enumerated group is closed under inverses.
        aa = s * ax[p]
        bb = s * by[p]
        if int(aa @ A @ bb) != target:
            raise AssertionError("signed action failed to preserve objective")
        orbit.add(aa.tobytes() + bb.tobytes())
        left = int(np.count_nonzero(aa != ax))
        right = int(np.count_nonzero(bb != by))
        support_histogram[(left, right)] += 1

    nonidentity = [
        (left + right, left, right)
        for left, right in support_histogram
        if left + right
    ]
    minimum = min(nonidentity)
    attaining_elements = sum(
        multiplicity
        for (left, right), multiplicity in support_histogram.items()
        if left + right == minimum[0]
    )

    result = {
        "signed_group_order": len(group_p),
        "signed_action_sha256": probe.group_sha(group_p, group_s),
        "objective_target": target,
        "distinct_strategy_pairs_in_orbit": len(orbit),
        "stabilizer_multiplicity_at_selected_pair": support_histogram[(0, 0)],
        "minimum_nontrivial_support": {
            "total": minimum[0],
            "left": minimum[1],
            "right": minimum[2],
            "attaining_group_elements": attaining_elements,
        },
        "global_complement_multiplicity": support_histogram[(300, 300)],
        "party_swap_support": {
            "left": int(np.count_nonzero(by != ax)),
            "right": int(np.count_nonzero(ax != by)),
        },
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
