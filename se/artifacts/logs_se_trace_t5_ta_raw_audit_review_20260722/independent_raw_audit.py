#!/usr/bin/env python3
"""Independent definition-level audit of the T5 colour-fold normalization.

The exact tame c=2 contractions are rebuilt from the archived d^2 and q
tables.  The archived final T_a/T_b values are not used as arithmetic inputs.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
T3 = ROOT / "se/artifacts/logs_se_trace_t3_20260721/se_trace_t3_report_20260721.md"
COMMON = ROOT / "se/artifacts/logs_se_trace_t5_common_line_20260721/REPORT.md"
NODE = ROOT / "se/proof-dag/nodes/SE.denom.Phi.legal.trace.t5.md"
R18_OUT = ROOT / "se/artifacts/logs_se_trace_t5_tame_c2_rout_20260721/tame_c2_rout.npz"
R18_IN = ROOT / "se/artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.npz"
R18_JSON = ROOT / "se/artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.json"
R19 = ROOT / "se/artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate_witness.npz"
R19_JSON = ROOT / "se/artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722/second_gate.json"
DIRECT = ROOT / "se/artifacts/logs_se_trace_t5_c2_gate_20260721/se_trace_t5_c2_gate_factors.npz"
THETA32 = ROOT / "se/artifacts/logs_se_trace_t5_j5_theta32_resume_v4_20260722/theta32_certified11_v4.json"
THETA311 = ROOT / "se/artifacts/logs_se_trace_t5_j5_theta311_localdp_v1_20260722/theta311_certified13_v1.json"
THETA32_ENGINE = ROOT / "se/artifacts/logs_se_trace_t5_j5_theta32_resume_v4_20260722/theta32_localdp_exact.py"
THETA311_ENGINE = ROOT / "se/artifacts/logs_se_trace_t5_j5_theta311_localdp_v1_20260722/theta311_localdp_exact.py"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hook(shape: tuple[int, ...]) -> int:
    prod = 1
    for r, width in enumerate(shape):
        for c in range(width):
            prod *= width - c + sum(x > c for x in shape[r + 1 :])
    return math.factorial(sum(shape)) // prod


def fractions(num: np.ndarray, den: np.ndarray) -> list[list[Q]]:
    return [[Q(int(num[i, j]), int(den[i, j])) for j in range(num.shape[1])]
            for i in range(num.shape[0])]


def tame_gate(n: int) -> dict:
    j = a = b = 3
    j = 6
    m = math.comb(j, a)
    theta_dim = 16
    orbit = math.comb(n - 1, j)
    if n == 18:
        out = np.load(R18_OUT, allow_pickle=False)
        inp = np.load(R18_IN, allow_pickle=False)
        active = [tuple(int(x) for x in row if int(x)) for row in out["active_mu"]]
        fmu_stored = [int(x) for x in out["f_mu"]]
        d2 = fractions(out["d_squared_numerator"], out["d_squared_denominator"])
        amass = fractions(out["a_mass_numerator"], out["a_mass_denominator"])
        q = [Q(int(x), int(y)) for x, y in zip(inp["q_mu_numerator"], inp["q_mu_denominator"])]
        cap_a, cap_b = Q(51396202, 35), Q(51396202, 1015)
        archived_a, archived_b = Q(160582822829, 1705200), Q(67576575391, 445057200)
        source_hashes = {str(R18_OUT.relative_to(ROOT)): sha(R18_OUT), str(R18_IN.relative_to(ROOT)): sha(R18_IN)}
    else:
        witness = np.load(R19, allow_pickle=False)
        data = json.loads(R19_JSON.read_text(encoding="utf-8"))["R_in_and_gate"]
        active = [tuple(row["mu"]) for row in data["targets"]]
        fmu_stored = [int(row["f_mu"]) for row in data["targets"]]
        d2 = fractions(witness["d2_numerator"], witness["d2_denominator"])
        amass = [[m * x for x in row] for row in d2]
        q = [Q(int(x), int(y)) for x, y in zip(witness["q_mu_numerator"], witness["q_mu_denominator"])]
        cap_a, cap_b = Q(137582445, 64), Q(137582445, 1984)
        archived_a, archived_b = Q(204466088827, 1438400), Q(8391760923, 44590400)
        source_hashes = {str(R19.relative_to(ROOT)): sha(R19)}

    fmu = [hook(mu) for mu in active]
    assert fmu == fmu_stored
    assert all(amass[g][i] == m * d2[g][i] for g in range(4) for i in range(8))
    # q is the squared projection of the literal raw coherent fold.  Frobenius
    # reciprocity gives ||t_mu||^2 = C(p,j) f^theta/f^mu q_mu.
    t2 = [Q(orbit * theta_dim, fmu[i]) * q[i] for i in range(8)]
    r = [x / m for x in t2]
    divided = [sum(Q(fmu[i]) * d2[g][i] * r[i] for i in range(8)) for g in range(4)]
    raw = [sum(Q(fmu[i]) * amass[g][i] * r[i] for i in range(8)) for g in range(4)]
    raw_direct_equivalent = [sum(Q(fmu[i]) * d2[g][i] * t2[i] for i in range(8)) for g in range(4)]
    assert raw == raw_direct_equivalent
    assert raw == [m * x for x in divided]
    assert divided[0] == archived_a and sum(divided[1:], Q(0)) == archived_b
    assert raw[0] > cap_a
    assert sum(raw[1:], Q(0)) < cap_b
    return {
        "n": n, "j": j, "a": a, "b": b, "m": m,
        "active_mu": [list(x) for x in active], "f_mu": fmu,
        "q_mu": [str(x) for x in q], "t_norm_squared": [str(x) for x in t2],
        "r_mu": [str(x) for x in r],
        "archived_divided_T_a_rebuilt": str(divided[0]),
        "raw_T_a_rebuilt_from_a_mass_times_r": str(raw[0]),
        "raw_T_a_rebuilt_from_d_squared_times_t_squared": str(raw_direct_equivalent[0]),
        "T_a_cap": str(cap_a), "T_a_excess": str(raw[0] - cap_a),
        "T_a_ratio": str(raw[0] / cap_a), "T_a_verdict": "FAIL",
        "archived_divided_T_b_rebuilt": str(sum(divided[1:], Q(0))),
        "raw_T_b_rebuilt": str(sum(raw[1:], Q(0))), "T_b_cap": str(cap_b),
        "T_b_margin": str(cap_b - sum(raw[1:], Q(0))), "T_b_verdict": "PASS_SINGLE_GATE",
        "source_hashes": source_hashes,
    }


def direct_raw_gate() -> dict:
    w = np.load(DIRECT, allow_pickle=False)
    L = w["L_analysis_320x1120"]
    values = {}
    for name in ("long", "tail_1", "tail_2", "tail_3"):
        K = w[f"K_{name}_112x320"]
        raw = float(np.vdot(K @ L, K @ L).real)
        normalized = float(np.vdot((K / math.sqrt(20)) @ L, (K / math.sqrt(20)) @ L).real)
        values[name] = {"raw_matrix_HS2": raw, "normalized_matrix_HS2": normalized,
                        "raw_over_normalized": raw / normalized}
        assert abs(raw / normalized - 20.0) < 2e-12
    assert abs(values["long"]["raw_matrix_HS2"] - 58443 / 1024) < 2e-11
    return {"witness_sha256": sha(DIRECT), "m": 20, "branches": values,
            "convention": "archived direct physical K is the raw horizontal 20-colour stack"}


def definition_audit() -> dict:
    t3 = T3.read_text(encoding="utf-8")
    common = COMMON.read_text(encoding="utf-8")
    node = NODE.read_text(encoding="utf-8")
    assertions = {
        "T3_raw_fold_identity": "S_{h,\\gamma}S_{h,\\gamma}^*\n =mK_\\gamma" in t3,
        "T3_m_definition": "Put `m=binom(j,a)`" in t3,
        "common_fold_is_raw_sum": "(Fx)_L=\\sum_{D:I\\cup J=L}U_Dx_D" in common,
        "common_normalization_optional_only_if_absorbed": "optional factor `binom(j,a)^(-1/2)`" in common and "absorbed into `b_gamma`" in common,
        "common_a_is_raw_branch_norm": "a_{\\gamma\\mu}=\\|v_{\\gamma\\mu}\\|^2" in common,
        "canonical_claim_calls_pairings_physical": "prove the physical actual pairings" in node,
    }
    assert all(assertions.values()), assertions
    return {"assertions": assertions, "hashes": {str(x.relative_to(ROOT)): sha(x) for x in (T3, COMMON, NODE)},
            "conclusion": "registered physical S is raw; S/sqrt(m) is a different normalized map"}


def certificate_scope_audit() -> dict:
    checks = {
        "j2": (ROOT / "se/artifacts/logs_se_trace_t5_mixed_orbital_20260721/t5_mixed_j2_exact.py",
               ["M = (n - 1) * (n - 2)", "actual = sp.factor(M * fixed_sum)"]),
        "j3": (ROOT / "se/artifacts/logs_se_trace_t5_j3_orbital_20260721/t5_j3_orbital_exact.py",
               ["sp.binomial(n - 1, 3) * sp.binomial(3, a)", "actual = sp.factor(M * fixed_sum)"]),
        "j4_scalar": (ROOT / "se/artifacts/logs_se_trace_t5_j4_orbital_20260721/t5_j4_scalar_exact.py",
                      ["sp.binomial(n - 1, 4) * sp.binomial(4, a)", "actual = sp.factor(M * fixed_sum)"]),
        "j4_matrix": (ROOT / "se/artifacts/logs_se_trace_t5_j4_nonscalar_20260721/theta22_harmonic_exact.py",
                      ["math.comb(n - 1, 4) * math.comb(4, family[\"a\"])", "T = family[\"dimension\"] * M"]),
        "j5_scalar": (ROOT / "se/artifacts/logs_se_trace_t5_j5_c1_20260722/t5_j5_c1_exact.py",
                      ["sp.binomial(N - 1, J) * sp.binomial(J, a)", "actual = sp.factor(states * fixed_sum)"]),
        "j5_matrix": (ROOT / "se/artifacts/logs_se_trace_t5_j5_degree3_20260722/j5_degree3_exact.py",
                      ["sum(pair_count(nexpr,j,a,t)*v", "/(specht(alpha).dim*specht(beta).dim)", "j4_regression"]),
    }
    rows = []
    for layer, (path, needles) in checks.items():
        text = path.read_text(encoding="utf-8")
        passed = all(needle in text for needle in needles)
        assert passed, (layer, needles)
        rows.append({"layer": layer, "file": str(path.relative_to(ROOT)), "sha256": sha(path),
                     "raw_colour_orbit_factor_present": True})
    return {
        "rows": rows,
        "j1": "raw direct formulas; m=1, so raw and normalized coincide",
        "j2_to_j5": "orbital sums use M=C(n-1,j)C(j,a), or cancel that same raw M in a ratio to the raw cap; no missing-m defect found",
        "affected_T_a_scope": "the two tame c=2 final contraction verdicts and any later proof that identifies raw T_a with a normalized-fold norm; not the archived j1-j5 c=1 orbital certificates",
        "j5_full_colour_enumeration": j5_full_colour_enumeration(),
    }


def j5_full_colour_enumeration() -> dict:
    """Resolve whether local-DP pair_count contains N or mN targets."""
    p, j, a, b = 14, 5, 2, 3
    states = []
    for union in itertools.combinations(range(p), j):
        for left in itertools.combinations(union, a):
            left = tuple(left)
            states.append((left, tuple(x for x in union if x not in left)))
    reference = states[0]

    def typ(target):
        i, k = map(set, reference)
        ip, kp = map(set, target)
        return (len(i & ip), len(i & kp), len(k & ip), len(k & kp))

    counts: dict[tuple[int, int, int, int], int] = {}
    for target in states:
        counts[typ(target)] = counts.get(typ(target), 0) + 1

    def choose(n: int, r: int) -> int:
        return math.comb(n, r) if 0 <= r <= n else 0

    formula = {}
    for t in counts:
        u, v, w, x = t
        formula[t] = (choose(a, u) * choose(b, w) * choose(p - j, a - u - w)
                      * choose(a - u, v) * choose(b - w, x)
                      * choose(p - j - a + u + w, b - v - x))
    assert counts == formula
    N, m = math.comb(p, j), math.comb(j, a)
    assert len(states) == sum(counts.values()) == N * m == 20020

    audited = []
    selections = [
        (THETA32, "theta32_a2_alpha11_beta21", (1, 1), (2, 1)),
        (THETA311, "theta311_a2_alpha11_beta21", (1, 1), (2, 1)),
    ]
    n_symbol = sp.symbols("n")
    for path, key, alpha, beta in selections:
        row = json.loads(path.read_text(encoding="utf-8"))["families"][key]
        table = {tuple(ast.literal_eval(k)): sp.sympify(v, locals={"n": n_symbol}).subs(n_symbol, 15)
                 for k, v in row["signed_orbitals"].items()}
        assert set(table) == set(counts)
        fixed_sum = sp.factor(sum(counts[t] * table[t] for t in counts))
        dim_product = hook(alpha) * hook(beta)
        ratio = sp.Rational(row["direct_n15_ratio"])
        assert sp.factor(fixed_sum / dim_product - ratio) == 0
        # For a raw physical trace, the outer source-state orbit contributes
        # M=N*m and the cap contains the identical T=M*f^alpha*f^beta.
        # Thus M cancels once.  Multiplying the stored ratio by m would count
        # the colour orbit a second time.
        raw_ratio_by_full_sum = sp.factor((len(states) * fixed_sum) /
                                          (len(states) * dim_product))
        assert raw_ratio_by_full_sum == ratio
        audited.append({
            "artifact": str(path.relative_to(ROOT)), "family": key,
            "alpha": list(alpha), "beta": list(beta), "m": m, "N": N,
            "fixed_coloured_source": [list(reference[0]), list(reference[1])],
            "enumerated_coloured_targets": len(states), "pair_types": len(counts),
            "pair_count_sum": sum(counts.values()), "expected_mN": N * m,
            "fixed_sum_of_cap_normalized_physical_kernel": str(fixed_sum),
            "f_alpha_f_beta": dim_product, "archived_ratio": str(ratio),
            "raw_full_double_sum_ratio": str(raw_ratio_by_full_sum),
            "incorrect_extra_m_ratio": str(sp.factor(m * ratio)),
            "extra_m_diagnosis": "double-counts the colour factor already present in pair_count and T",
        })
    for engine in (THETA32_ENGINE, THETA311_ENGINE):
        text = engine.read_text(encoding="utf-8")
        assert "G.family_ratio" in text and "j5_degree3_20260722/j5_degree3_exact.py" in text
    return {
        "enumeration": "all coloured (I,J) targets for p=14,j=5,a=2",
        "N": N, "m": m, "mN": N * m, "pair_count_sum": sum(counts.values()),
        "formula_matches_all_pair_types": True, "families": audited,
        "theta32_and_theta311_use_same_family_ratio_engine": True,
        "verdict": "RAW_M_ALREADY_INCLUDED; DO_NOT_MULTIPLY_CERTIFICATE_RATIOS_BY_M",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()
    definitions = definition_audit()
    direct = direct_raw_gate()
    gates = [tame_gate(18), tame_gate(19)]
    certificates = certificate_scope_audit()
    result = {
        "date": "2026-07-22",
        "verdict": "CONFIRMED_REFUTATION",
        "definition_audit": definitions,
        "non_tame_direct_raw_matrix_gate": direct,
        "tame_c2_exact_recomputations": gates,
        "existing_T_a_certificate_scope": certificates,
        "T_a_adjudication": "registered raw physical T_a fails at n=18 and n=19; T5 and every route whose obligation is uniform (T-a) are refuted",
        "T_b_adjudication": "both corrected finite raw c=2 T_b gates pass, but the effective-rank/output-frame chain proves only raw T_b/m; uniform physical T-b must be reopened",
        "root_adjudication": "the counterexamples refute the sufficient T-a/T-b route, not the original SE lower-bound statement; T2 cannot remain a conjectured route to uniform T-a, but the SE root is not mathematically refuted by these data",
    }
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "VERDICT CONFIRMED_REFUTATION",
        "DEFINITION registered physical S is RAW; normalized S/sqrt(m) is different",
        "DIRECT non-tame c2 matrix witness raw/normalized=20 for all 4 branches PASS",
    ]
    for row in gates:
        lines.append(f"TAME n={row['n']} raw_Ta={row['raw_T_a_rebuilt_from_a_mass_times_r']} cap={row['T_a_cap']} FAIL "
                     f"raw_Tb={row['raw_T_b_rebuilt']} capTb={row['T_b_cap']} PASS_SINGLE_GATE")
    lines += [
        "T_B uniform effective-rank conclusion INVALID: proves raw T_b/m only; REOPEN",
        "T_A_CERTS j1-j5 c1 orbital certificates retain raw colour-orbit factor; UNAFFECTED",
        "IMPACT T5 REFUTED; T2 uniform-T-a route REFUTED; original SE root NOT REFUTED",
    ]
    args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
