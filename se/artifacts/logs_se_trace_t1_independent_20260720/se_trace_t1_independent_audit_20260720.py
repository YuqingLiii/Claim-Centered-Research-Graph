#!/usr/bin/env python3
"""Independent exact audit for SE.denom.Phi.legal.trace.t1.

This implementation does not import the supplied eta or bigate programs.
It independently computes partitions, hook dimensions, LR coefficients,
the printed per-tail scalar condition, and the correctly summed Hölder
condition over an exact tame-sector range.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from pathlib import Path


def partitions(total: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def is_partition(shape: tuple[int, ...]) -> bool:
    return all(x > 0 for x in shape) and all(
        shape[i] >= shape[i + 1] for i in range(len(shape) - 1)
    )


@lru_cache(None)
def hook_dim(shape: tuple[int, ...]) -> int:
    shape = tuple(x for x in shape if x)
    if not shape:
        return 1
    hooks = 1
    for row, width in enumerate(shape):
        for col in range(width):
            hooks *= width - col + sum(x > col for x in shape[row + 1 :])
    return factorial(sum(shape)) // hooks


@lru_cache(None)
def lr_coefficient(
    alpha: tuple[int, ...], beta: tuple[int, ...], theta: tuple[int, ...]
) -> int:
    """Exact LR coefficient by lattice-word semistandard tableaux."""
    if sum(alpha) + sum(beta) != sum(theta):
        return 0
    if not beta:
        return int(alpha == theta)
    inner = alpha + (0,) * (len(theta) - len(alpha))
    if len(inner) > len(theta) or any(inner[r] > theta[r] for r in range(len(theta))):
        return 0
    cells = sorted(
        [(r, c) for r, width in enumerate(theta) for c in range(inner[r], width)],
        key=lambda cell: (cell[0], -cell[1]),
    )
    table: dict[tuple[int, int], int] = {}
    count = 0

    def visit(k: int, used: list[int]) -> None:
        nonlocal count
        if k == len(cells):
            count += 1
            return
        r, c = cells[k]
        for value in range(1, len(beta) + 1):
            if used[value - 1] >= beta[value - 1]:
                continue
            if (r, c + 1) in table and value > table[r, c + 1]:
                continue
            if (r - 1, c) in table and value <= table[r - 1, c]:
                continue
            new_used = used.copy()
            new_used[value - 1] += 1
            if any(new_used[i] < new_used[i + 1] for i in range(len(beta) - 1)):
                continue
            table[(r, c)] = value
            visit(k + 1, new_used)
            del table[(r, c)]

    visit(0, [0] * len(beta))
    return count


def removable_tails(q: int, j: int, theta: tuple[int, ...]):
    ell = q - j
    out = []
    for row, width in enumerate(theta, start=1):
        following = theta[row] if row < len(theta) else 0
        if width <= following:
            continue
        reduced = list(theta)
        reduced[row - 1] -= 1
        reduced = tuple(x for x in reduced if x)
        delta = ell - width + row
        tau = (ell,) + reduced
        out.append(
            {"row": row, "width": width, "delta": delta, "tau": tau, "f_tau": hook_dim(tau)}
        )
    return out


def audit_sector(
    n: int,
    j: int,
    theta: tuple[int, ...],
    a: int,
    alpha: tuple[int, ...],
    b: int,
    beta: tuple[int, ...],
):
    q = 2 * n
    lam = (q - j,) + theta
    kappa = (n - 1 - a,) + alpha
    nu = (n - b,) + beta
    c = lr_coefficient(alpha, beta, theta)
    checks = {
        "q=2n": q == 2 * n,
        "j>=1": j >= 1,
        "a+b=j": a + b == j,
        "shape_sizes": sum(theta) == j and sum(alpha) == a and sum(beta) == b,
        "lambda_partition": is_partition(lam),
        "kappa_partition": is_partition(kappa),
        "nu_partition": is_partition(nu),
        "long_child": q - j - 1 >= theta[0],
        "stable_left": n - 1 - a >= theta[0],
        "stable_right": n - b >= theta[0],
        "LR_positive": c > 0,
    }
    tails = removable_tails(q, j, theta)
    delta_min = min(t["delta"] for t in tails)
    m = comb(j, a)
    n_phys = comb(n - 1, j)
    n_query = comb(q - 1, j)
    f_product = hook_dim(alpha) * hook_dim(beta)
    f_lambda = hook_dim(lam)
    btheta = Fraction(comb(q, j) * hook_dim(theta), f_lambda)
    branch_rows = []
    for tail in tails:
        printed_ratio = Fraction(
            m * tail["f_tau"] * (delta_min + 1),
            (tail["delta"] + 1) * n_query * f_product,
        )
        eta = btheta * Fraction(tail["f_tau"], n_query * (tail["delta"] + 1))
        branch_rows.append(
            tail
            | {
                "eta": eta,
                "printed_ratio": printed_ratio,
                "printed_pass": printed_ratio <= 1,
            }
        )
    summed_ratio = Fraction(delta_min + 1, n_query * f_product) * sum(
        Fraction(t["f_tau"], t["delta"] + 1) for t in tails
    )
    return {
        "n": n,
        "q": q,
        "j": j,
        "theta": theta,
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta,
        "lambda": lam,
        "kappa": kappa,
        "nu": nu,
        "c": c,
        "m": m,
        "N_phys": n_phys,
        "N_query": n_query,
        "T": m * n_phys * f_product,
        "f_alpha_f_beta": f_product,
        "B_theta": btheta,
        "delta_min": delta_min,
        "tails": branch_rows,
        "summed_ratio": summed_ratio,
        "summed_pass": summed_ratio <= 1,
        "checks": checks,
        "admissible": all(checks.values()),
        "tame": n >= 3 * j,
        "strict_tame": n > 3 * j,
    }


def as_json(value):
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, list):
        return [as_json(x) for x in value]
    if isinstance(value, dict):
        return {k: as_json(v) for k, v in value.items()}
    return value


GATES = [
    (3, 1, (1,), 1, (1,), 0, ()),
    (3, 1, (1,), 0, (), 1, (1,)),
    (4, 1, (1,), 1, (1,), 0, ()),
    (4, 1, (1,), 0, (), 1, (1,)),
    (4, 2, (2,), 0, (), 2, (2,)),
    (4, 2, (2,), 1, (1,), 1, (1,)),
    (4, 2, (1, 1), 0, (), 2, (1, 1)),
    (4, 2, (1, 1), 1, (1,), 1, (1,)),
    (4, 2, (1, 1), 2, (1, 1), 0, ()),
]


def scan(n_max: int):
    sector_count = 0
    c_ge_2_count = 0
    printed_failures = []
    summed_failures = []
    for n in range(3, n_max + 1):
        for j in range(1, n // 3 + 1):
            for theta in partitions(j):
                for a in range(j + 1):
                    b = j - a
                    for alpha in partitions(a):
                        for beta in partitions(b):
                            row = audit_sector(n, j, theta, a, alpha, b, beta)
                            if not row["admissible"] or not row["tame"]:
                                continue
                            sector_count += 1
                            if row["c"] >= 2:
                                c_ge_2_count += 1
                            for tail in row["tails"]:
                                if not tail["printed_pass"]:
                                    printed_failures.append(
                                        {
                                            "sector": row,
                                            "failing_tail": tail,
                                        }
                                    )
                            if not row["summed_pass"]:
                                summed_failures.append(row)
    return {
        "n_max": n_max,
        "sector_count": sector_count,
        "c_ge_2_sector_count": c_ge_2_count,
        "printed_failure_count": len(printed_failures),
        "summed_failure_count": len(summed_failures),
        "first_printed_failure": printed_failures[0] if printed_failures else None,
        "first_printed_failure_strict_tame": next(
            (x for x in printed_failures if x["sector"]["strict_tame"]), None
        ),
        "first_summed_failure": summed_failures[0] if summed_failures else None,
        "first_summed_failure_strict_tame": next(
            (x for x in summed_failures if x["strict_tame"]), None
        ),
    }


def describe_sector(prefix: str, row: dict, lines: list[str]) -> None:
    lines.append(
        f"{prefix} n={row['n']} q={row['q']} j={row['j']} theta={row['theta']} "
        f"a={row['a']} alpha={row['alpha']} b={row['b']} beta={row['beta']} "
        f"c={row['c']} admissible={row['admissible']} tame={row['tame']} "
        f"m={row['m']} N_phys={row['N_phys']} N_query={row['N_query']} "
        f"B={row['B_theta']} T={row['T']} delta_min={row['delta_min']}"
    )
    for t in row["tails"]:
        lines.append(
            f"  tail row={t['row']} width={t['width']} tau={t['tau']} "
            f"delta={t['delta']} f_tau={t['f_tau']} eta={t['eta']} "
            f"printed_ratio={t['printed_ratio']} "
            f"printed={'PASS' if t['printed_pass'] else 'FAIL'}"
        )
    lines.append(
        f"  corrected_summed_ratio={row['summed_ratio']} "
        f"summed={'PASS' if row['summed_pass'] else 'FAIL'}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--n-max", type=int, default=36)
    args = parser.parse_args()

    gates = [audit_sector(*g) for g in GATES]
    assert len(gates) == 9
    assert all(g["admissible"] and g["c"] == 1 for g in gates)
    assert all(all(t["printed_pass"] for t in g["tails"]) for g in gates)

    killer = audit_sector(9, 3, (2, 1), 2, (2,), 1, (1,))
    larger = audit_sector(12, 4, (4,), 2, (2,), 2, (2,))
    corrected_killer = killer
    corrected_counterexample = audit_sector(18, 6, (4, 2), 2, (2,), 4, (4,))
    assert killer["admissible"] and killer["tame"] and killer["c"] == 1
    assert all(t["printed_pass"] for t in killer["tails"])
    assert larger["admissible"] and larger["tame"] and larger["c"] == 1
    assert any(not t["printed_pass"] for t in larger["tails"])
    assert corrected_counterexample["admissible"] and corrected_counterexample["tame"]
    assert not corrected_counterexample["summed_pass"]

    scan_result = scan(args.n_max)
    first = scan_result["first_printed_failure"]["sector"]
    assert (first["n"], first["j"], first["theta"], first["a"], first["alpha"], first["b"], first["beta"]) == (
        12, 4, (4,), 2, (2,), 2, (2,)
    )
    first_sum = scan_result["first_summed_failure"]
    assert (first_sum["n"], first_sum["j"], first_sum["theta"], first_sum["a"], first_sum["alpha"], first_sum["b"], first_sum["beta"]) == (
        18, 6, (4, 2), 2, (2,), 4, (4,)
    )

    payload = {
        "method": "independent hook/LR exact arithmetic; no supplied audit code imported",
        "gates": gates,
        "killer": killer,
        "larger_minimal_printed_counterexample": larger,
        "minimal_corrected_summed_counterexample": corrected_counterexample,
        "scan": scan_result,
    }
    args.json.write_text(json.dumps(as_json(payload), indent=2) + "\n", encoding="utf-8")

    lines = ["SE TRACE T1 INDEPENDENT EXACT AUDIT"]
    for i, gate in enumerate(gates, 1):
        describe_sector(f"GATE_{i}", gate, lines)
    describe_sector("KILLER", killer, lines)
    describe_sector("LARGER_MINIMAL_PRINTED_COUNTEREXAMPLE", larger, lines)
    describe_sector("MINIMAL_CORRECTED_SUMMED_COUNTEREXAMPLE", corrected_counterexample, lines)
    lines.append(
        f"SCAN n=3..{args.n_max} sectors={scan_result['sector_count']} "
        f"c>=2_scalar_sectors={scan_result['c_ge_2_sector_count']} "
        f"printed_failures={scan_result['printed_failure_count']} "
        f"summed_failures={scan_result['summed_failure_count']}"
    )
    strict_printed = scan_result["first_printed_failure_strict_tame"]
    strict_sum = scan_result["first_summed_failure_strict_tame"]
    if strict_printed:
        s = strict_printed["sector"]
        t = strict_printed["failing_tail"]
        lines.append(
            f"FIRST_STRICT_TAME_PRINTED_FAIL n={s['n']} j={s['j']} theta={s['theta']} "
            f"a={s['a']} alpha={s['alpha']} b={s['b']} beta={s['beta']} "
            f"tail_tau={t['tau']} ratio={t['printed_ratio']}"
        )
    if strict_sum:
        lines.append(
            f"FIRST_STRICT_TAME_SUMMED_FAIL n={strict_sum['n']} j={strict_sum['j']} "
            f"theta={strict_sum['theta']} a={strict_sum['a']} alpha={strict_sum['alpha']} "
            f"b={strict_sum['b']} beta={strict_sum['beta']} ratio={strict_sum['summed_ratio']}"
        )
    lines.append("VERDICT printed universal branchwise scalar claim = REFUTED")
    lines.append("VERDICT corrected full-tail summed Holder sufficient condition = FALSE uniformly")
    lines.append("NOTE failure of either sufficient scalar condition does not refute T-b itself")
    lines.append("NOTE c>=2 identity-level carrier gate remains UNTESTED")
    args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
