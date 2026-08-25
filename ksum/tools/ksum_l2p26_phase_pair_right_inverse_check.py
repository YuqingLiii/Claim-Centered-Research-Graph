"""Bounded checks for Phase-26 phase pairing and birth-edge inversion.

No support optimization or LP is performed.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


def adjacent_row_defect(D: int, lam_plus: float, lam_minus: float, beta: float) -> dict[str, float | int]:
    b = round(beta * D)
    m_plus = round(lam_plus * D)
    m_minus = round(lam_minus * D)
    # After exact cancellation of row b by a two-atom pair, this is the
    # absolute row-(b+1) residual divided by the plus atom's row-(b+1) value.
    defect = abs(1.0 - (m_minus - b) / (m_plus - b))
    return {"D": D, "b": b, "m_plus": m_plus, "m_minus": m_minus, "normalized_defect": defect}


def birth_adjacent_defect(D: int, s: int = 2) -> dict[str, float | int]:
    beta, lam_minus = 0.15, 0.55
    b = round(beta * D)
    m_plus = b + s
    m_minus = round(lam_minus * D)
    defect = abs(1.0 - (m_minus - b) / (m_plus - b))
    return {"D": D, "s": s, "normalized_defect": defect, "defect_over_D": defect / D}


def pascal_inverse_norm(M: int) -> dict[str, int]:
    # Rows/columns 1..M of P[b,m]=binom(m,b).  The inverse column at b=M
    # has coefficients (-1)^(M-m) binom(M,m), m=1..M.
    lower_bound = sum(math.comb(M, m) for m in range(1, M + 1))
    return {"M": M, "inverse_l1_lower_bound": lower_bound, "two_to_M_minus_one": 2**M - 1}


def exposed_path_example() -> dict[str, float]:
    c, alpha, beta = 1.0, 0.5, 0.15
    lam_star = beta / (1.0 - math.exp(-c * alpha))
    sigma_star = 0.8 * math.exp(-c * lam_star)
    second_derivative = -beta / (lam_star * (lam_star - beta))
    return {
        "c": c,
        "alpha": alpha,
        "beta": beta,
        "lambda_star": lam_star,
        "sigma_star": sigma_star,
        "phase_second_derivative": second_derivative,
    }


def main() -> None:
    path = Path(__file__)
    payload = {
        "driver_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "two_atom_adjacent_defect": [
            adjacent_row_defect(d, 0.35, 0.55, 0.15) for d in (100, 200, 400, 800)
        ],
        "birth_edge_adjacent_defect": [birth_adjacent_defect(d) for d in (100, 200, 400, 800)],
        "pascal_inverse": [pascal_inverse_norm(m) for m in (4, 8, 12, 16, 20)],
        "exposed_path": exposed_path_example(),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
