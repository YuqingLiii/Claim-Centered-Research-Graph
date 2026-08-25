#!/usr/bin/env python3
"""Exact audit for the T5 uniform physical T-a two-frame theorem."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

DEPENDENCIES = [
    "se/artifacts/logs_se_trace_t5_common_line_review_20260721",
    "se/artifacts/logs_se_trace_t5_carrier_dimension_review_20260722",
    "se/artifacts/logs_se_trace_t5_uniform_cge2_effective_rank_review_20260722",
    "se/artifacts/logs_se_trace_t5_long_cap_20260721",
    "se/artifacts/logs_se_trace_t5_tame_c2_rout_20260721",
    "se/artifacts/logs_se_trace_t5_tame_c2_rcol_20260721",
    "se/artifacts/logs_se_trace_t5_tame_c2_rcol_review_20260722",
    "se/artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722",
    "se/artifacts/logs_se_trace_t5_second_tame_c2_gate_review_20260722",
]


def frac(value) -> Q:
    return Q(str(value))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_manifest(folder: Path) -> dict:
    checked = 0
    for line in (folder / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        want, name = line.split(maxsplit=1)
        name = name.strip().lstrip("*")
        path = folder / name
        if not path.exists():
            path = ROOT / name
        assert path.is_file(), (folder, name)
        assert sha256(path) == want, (folder, name, "SHA mismatch")
        checked += 1
    assert checked
    return {"directory": str(folder.relative_to(ROOT)), "files": checked, "pass": True}


def fdim(shape) -> int:
    shape = tuple(shape)
    if not shape:
        return 1
    n = sum(shape)
    hooks = 1
    for row, width in enumerate(shape):
        for col in range(width):
            below = sum(col < other for other in shape[row + 1 :])
            hooks *= width - col + below
    return math.factorial(n) // hooks


def exact_sqrt(value: Q) -> Q:
    a = math.isqrt(value.numerator)
    b = math.isqrt(value.denominator)
    assert a * a == value.numerator and b * b == value.denominator
    return Q(a, b)


def simplex_frame_audit() -> dict:
    """Exact standard-module fixed-point frame: sum_s P_s=q/(q-1) I."""
    rows = []
    for q in range(3, 13):
        # Work on ambient Q^q; P_s=(q/(q-1)) u_s u_s^T and sum P_s is
        # q/(q-1) times the standard-space projector.
        u = []
        for s in range(q):
            u.append([Q(int(i == s)) - Q(1, q) for i in range(q)])
        total = [[Q(0) for _ in range(q)] for _ in range(q)]
        for vector in u:
            for i in range(q):
                for j in range(q):
                    total[i][j] += Q(q, q - 1) * vector[i] * vector[j]
        standard = [[Q(int(i == j)) - Q(1, q) for j in range(q)] for i in range(q)]
        B = Q(q, q - 1)
        assert total == [[B * standard[i][j] for j in range(q)] for i in range(q)]
        rows.append({"q": q, "B": str(B), "exact": True})
    return {"standard_fixed_point_frames": rows, "count": len(rows)}


def gate18() -> dict:
    rout = json.loads((ROOT / "se/artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.json").read_text())
    rin = json.loads((ROOT / "se/artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.json").read_text())
    long_rows = {tuple(x["mu"]): frac(x["d_squared"]) for x in rout["rows"] if x["branch"] == "long"}
    targets = {tuple(x["mu"]): x for x in rin["targets"]}
    n, j, a, c = 18, 6, 3, 2
    theta, alpha, beta = (3, 2, 1), (2, 1), (2, 1)
    T = math.comb(n - 1, j) * math.comb(j, a) * fdim(alpha) * fdim(beta)
    cap = frac(rin["actual_gates"]["T_a_cap"])
    B = exact_sqrt(cap / T)
    normalized = sum(Q(targets[mu]["f_mu"]) * d2 * frac(targets[mu]["r_mu"])
                     for mu, d2 in long_rows.items())
    archived = frac(rin["actual_gates"]["T_a"])
    assert normalized == archived
    raw_actual = Q(math.comb(j, a)) * normalized
    assert raw_actual > cap
    normalized_tb = frac(rin["actual_gates"]["T_b"])
    tb_cap = frac(rin["actual_gates"]["T_b_cap"])
    raw_tb = Q(math.comb(j, a)) * normalized_tb
    assert raw_tb < tb_cap
    assert max(long_rows.values()) == B
    assert all(d2 <= B for d2 in long_rows.values())
    dim_y = math.comb(n - 1, j) * fdim(theta)
    assert dim_y <= T // c and c * dim_y <= T
    return {
        "n": n, "c": c, "B": str(B), "max_d_long_squared": str(max(long_rows.values())),
        "output_frame_rows": len(long_rows), "all_d_long_squared_le_B": True,
        "T": T, "dim_Y": dim_y, "c_dim_Y_over_T": str(Q(c * dim_y, T)),
        "normalized_T_a_recomputed": str(normalized), "archived_misnormalized_T_a": str(archived),
        "raw_registered_T_a": str(raw_actual), "raw_minus_cap": str(raw_actual - cap),
        "raw_over_cap": str(raw_actual / cap), "raw_registered_T_a_fails": True,
        "raw_registered_T_b": str(raw_tb), "T_b_cap": str(tb_cap),
        "raw_registered_T_b_finite_gate_passes": True,
        "normalized_below_two_frame_rank_bound": normalized <= B * B * dim_y,
        "two_frame_rank_bound": str(B * B * dim_y),
    }


def gate19() -> dict:
    data = json.loads((ROOT / "se/artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.json").read_text())
    long_rows = {tuple(x["mu"]): frac(x["d_squared"]) for x in data["R_out"]["rows"] if x["branch"] == "long"}
    targets = {tuple(x["mu"]): x for x in data["R_in_and_gate"]["targets"]}
    target = data["target"]
    n, j, a, c = target["n"], target["j"], target["a"], target["LR_multiplicity"]
    theta, alpha, beta = tuple(target["theta"]), tuple(target["alpha"]), tuple(target["beta"])
    T = math.comb(n - 1, j) * math.comb(j, a) * fdim(alpha) * fdim(beta)
    cap = frac(data["R_in_and_gate"]["T_a_cap"])
    B = exact_sqrt(cap / T)
    normalized = sum(Q(targets[mu]["f_mu"]) * d2 * frac(targets[mu]["r_mu"])
                     for mu, d2 in long_rows.items())
    archived = frac(data["R_in_and_gate"]["T_a"])
    assert normalized == archived
    raw_actual = Q(math.comb(j, a)) * normalized
    assert raw_actual > cap
    normalized_tb = frac(data["R_in_and_gate"]["T_b"])
    tb_cap = frac(data["R_in_and_gate"]["T_b_cap"])
    raw_tb = Q(math.comb(j, a)) * normalized_tb
    assert raw_tb < tb_cap
    assert max(long_rows.values()) == B
    assert all(d2 <= B for d2 in long_rows.values())
    dim_y = math.comb(n - 1, j) * fdim(theta)
    assert c * dim_y <= T
    return {
        "n": n, "c": c, "B": str(B), "max_d_long_squared": str(max(long_rows.values())),
        "output_frame_rows": len(long_rows), "all_d_long_squared_le_B": True,
        "T": T, "dim_Y": dim_y, "c_dim_Y_over_T": str(Q(c * dim_y, T)),
        "normalized_T_a_recomputed": str(normalized), "archived_misnormalized_T_a": str(archived),
        "raw_registered_T_a": str(raw_actual), "raw_minus_cap": str(raw_actual - cap),
        "raw_over_cap": str(raw_actual / cap), "raw_registered_T_a_fails": True,
        "raw_registered_T_b": str(raw_tb), "T_b_cap": str(tb_cap),
        "raw_registered_T_b_finite_gate_passes": True,
        "normalized_below_two_frame_rank_bound": normalized <= B * B * dim_y,
        "two_frame_rank_bound": str(B * B * dim_y),
    }


def j1_audit() -> list[dict]:
    rows = []
    for n in range(3, 31):
        q = 2 * n
        B = Q(q, q - 1)
        T = n - 1
        dim_y = n - 1
        unbarred = B * B * (n - 2)
        barred = B * B * T * Q(2 * n - 3, 2 * n - 1)
        assert unbarred <= B * B * dim_y
        assert barred <= B * B * dim_y
        rows.append({"n": n, "B": str(B), "unbarred_T_a": str(unbarred),
                     "barred_T_a": str(barred), "rank_bound": str(B * B * dim_y)})
    return rows


def main() -> None:
    manifests = [verify_manifest(ROOT / path) for path in DEPENDENCIES]
    g18, g19 = gate18(), gate19()
    result = {
        "verdict": "REFUTED",
        "theorem": "The two-frame argument proves only T_a/m <= B_theta(q)^2 dim(Y); registered raw T_a has m=C(j,a) and fails at two tame c=2 gates",
        "operator_typing": {
            "C": "C=F_tilde L_h: carrier -> Y",
            "input_bound": "C^*C <= B_theta(q) I and rank(C)<=dim(Y)",
            "O0": "O0=Q_0 P_comp E: Y -> long-child output",
            "output_bound": "O0 O0^* <= E E^* = sum_L Pi_L = B_theta(q) I",
            "normalized_map": "Khat_0=O0 C=S_0 L_h/sqrt(m); fixed-mu blocks are f^mu |d_(0,mu)|^2 r_mu",
            "raw_physical_map": "S_0 L_h=sqrt(m) Khat_0; a_(0,mu)=m|d_(0,mu)|^2; registered T_a=m||Khat_0||_HS^2",
            "rank": "rank(K_0)<=rank(C)<=dim(Y)=C(n-1,j) f^theta",
            "LR_dimension": "c f^theta <= C(j,a) f^alpha f^beta, so dim(Y)<=T/c",
        },
        "excluded_surrogates": [
            "no global or isotype decreasing-spectrum von Neumann pairing",
            "no maximum over mu and no deletion of carrier/LR directions",
            "no raw color fold: F_tilde=F/sqrt(C(j,a)) is the reviewed physical common-line normalization",
            "no pointwise tail-from-long inference",
        ],
        "dependency_manifests": manifests,
        "exact_simplex_output_frame_audit": simplex_frame_audit(),
        "j1_closed_form_rows": j1_audit(),
        "tame_c2_gates": [g18, g19],
        "claim_scope": "every admissible physical sector for which the reviewed T5/common-line/fixed-set modules are defined; all positive LR multiplicities c",
        "T_b_normalization_consequence": "the same raw factor m multiplies tails; both finite c=2 gates still pass after correction, but the claimed uniform effective-rank proof bounds T_b/m and must be reopened",
    }
    out = HERE / "uniform_ta_two_frame.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    log = [
        "VERDICT REFUTED",
        "registered raw physical T-a fails at two exact tame c=2 gates; archived contractions omitted m=C(j,a)=20",
        f"dependency manifests PASS {sum(x['files'] for x in manifests)} files / {len(manifests)} packages",
        f"exact simplex output frames PASS {result['exact_simplex_output_frame_audit']['count']}/10",
        f"j=1 formulas PASS {len(result['j1_closed_form_rows'])}/28",
        f"tame c=2 n=18 raw T_a={g18['raw_registered_T_a']} > cap; ratio={g18['raw_over_cap']}",
        f"tame c=2 n=19 raw T_a={g19['raw_registered_T_a']} > cap; ratio={g19['raw_over_cap']}",
        "INVARIANTS PASS",
    ]
    (HERE / "uniform_ta_two_frame.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    print("\n".join(log))


if __name__ == "__main__":
    main()
