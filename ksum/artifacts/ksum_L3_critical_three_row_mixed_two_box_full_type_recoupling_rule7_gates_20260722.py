"""Independent finite gates for the mixed two-box full-type Rule-7 review.

The verdict is analytic.  These gates reconstruct the standard-space point maps and
exercise the complete rectangular 2 x 2 effect/equality identities at q=12=4a.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


TOL = 2.0e-10
RNG = np.random.default_rng(20260722)
MAX_MATRIX_RESIDUAL = 0.0


def opnorm(x: np.ndarray) -> float:
    return float(np.linalg.svd(x, compute_uv=False)[0]) if x.size else 0.0


def assert_close(name: str, lhs: np.ndarray | float, rhs: np.ndarray | float,
                 tol: float = TOL) -> None:
    global MAX_MATRIX_RESIDUAL
    err = float(np.linalg.norm(np.asarray(lhs) - np.asarray(rhs)))
    MAX_MATRIX_RESIDUAL = max(MAX_MATRIX_RESIDUAL, err)
    if err > tol:
        raise AssertionError(f"{name}: residual {err:.3e} > {tol:.3e}")


def assert_le(name: str, lhs: float, rhs: float, tol: float = TOL) -> None:
    if lhs > rhs + tol:
        raise AssertionError(f"{name}: {lhs:.12g} > {rhs:.12g}")


def orth_basis_projector(p: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((p + p.T) / 2)
    return vecs[:, vals > 0.5]


def null_basis(row: np.ndarray) -> np.ndarray:
    _, _, vh = np.linalg.svd(row.reshape(1, -1), full_matrices=True)
    return vh[1:].T


@dataclass
class PointModel:
    q: int
    a: int
    alpha_p: float
    alpha_m: float
    delta_p: float
    delta_m: float
    r_p: float
    r_m: float
    ip: list[np.ndarray]
    im: list[np.ndarray]
    pi_p: list[np.ndarray]
    pi_m: list[np.ndarray]
    xi_p: list[np.ndarray]
    xi_m: list[np.ndarray]
    x: list[np.ndarray]

    @property
    def dp(self) -> int:
        return self.pi_p[0].shape[0]

    @property
    def dm(self) -> int:
        return self.pi_m[0].shape[0]


def construct_point_model(q: int, a: int) -> PointModel:
    if q != 4 * a:
        raise ValueError("the cell gate uses q=4a")
    one = np.ones(q)
    p_v = np.eye(q) - np.outer(one, one) / q
    qv = orth_basis_projector(p_v)
    dv = q - 1
    ident = np.eye(dv * dv)

    # The global-standard copy J is an isometry on V, not on all of R^q.
    u_full = [math.sqrt(q / (q - 1)) * (np.eye(q)[:, z] - one / q)
              for z in range(q)]
    u = [qv.T @ uz for uz in u_full]
    jmap = np.zeros((dv * dv, dv))
    coef = (q - 1) / math.sqrt(q * (q - 2))
    for z in range(q):
        jmap += coef * np.outer(np.kron(u[z], u[z]), qv[z, :])
    assert_close("J isometry on V", jmap.T @ jmap, np.eye(dv))

    # Tensor-space irreducible projectors.
    swap = np.zeros_like(ident)
    for i in range(dv):
        for j in range(dv):
            swap[j * dv + i, i * dv + j] = 1.0
    p_sym = (ident + swap) / 2
    p_alt = (ident - swap) / 2
    tr = np.eye(dv).reshape(-1) / math.sqrt(dv)
    p_plus = p_sym - np.outer(tr, tr) - jmap @ jmap.T
    p_minus = p_alt
    bplus = orth_basis_projector(p_plus)
    bminus = orth_basis_projector(p_minus)
    expected_dp = q * (q - 3) // 2
    expected_dm = (q - 1) * (q - 2) // 2
    if bplus.shape[1] != expected_dp or bminus.shape[1] != expected_dm:
        raise AssertionError("carrier rank mismatch")
    print(f"PASS carrier ranks: d_plus={expected_dp}, d_minus={expected_dm}")

    eta = math.sqrt(2 / ((q - 1) * (q - 2)))
    p = math.sqrt(q * (q - 3) / ((q - 1) * (q - 2)))
    ip: list[np.ndarray] = []
    im: list[np.ndarray] = []
    for z in range(q):
        wz = null_basis(u[z])
        s = np.column_stack([
            (np.kron(u[z], wz[:, j]) + np.kron(wz[:, j], u[z])) / math.sqrt(2)
            for j in range(q - 2)
        ])
        alt = np.column_stack([
            (np.kron(u[z], wz[:, j]) - np.kron(wz[:, j], u[z])) / math.sqrt(2)
            for j in range(q - 2)
        ])
        plus_ambient = (s + eta * jmap @ wz) / p
        minus_ambient = alt
        assert_close(f"Iplus[{z}] isometry", plus_ambient.T @ plus_ambient,
                     np.eye(q - 2))
        assert_close(f"Iminus[{z}] isometry", minus_ambient.T @ minus_ambient,
                     np.eye(q - 2))
        assert_close(f"Iplus[{z}] carrier", p_plus @ plus_ambient, plus_ambient)
        ip.append(bplus.T @ plus_ambient)
        im.append(bminus.T @ minus_ambient)

    pi_p = [v @ v.T for v in ip]
    pi_m = [v @ v.T for v in im]
    xi_p = [np.eye(expected_dp) - v for v in pi_p]
    xi_m = [np.eye(expected_dm) - v for v in pi_m]
    x = [ip[z] @ im[z].T for z in range(q)]

    alpha_p = (q - 3) / (2 * (q - 2))
    alpha_m = (q - 1) / (2 * q)
    delta_p = (q - 3) / ((q - 1) * (q - 4))
    delta_m = (q - 1) / (q * (q - 3))
    assert_close("sum Pi_plus", sum(pi_p), np.eye(expected_dp) / alpha_p)
    assert_close("sum Pi_minus", sum(pi_m), np.eye(expected_dm) / alpha_m)
    assert_close("sum Xi_plus", sum(xi_p), np.eye(expected_dp) / delta_p)
    assert_close("sum Xi_minus", sum(xi_m), np.eye(expected_dm) / delta_m)
    assert_close("sum X", sum(x), np.zeros((expected_dp, expected_dm)))
    assert_close("transfer XX*", alpha_p * alpha_m * sum(v @ v.T for v in x),
                 alpha_m * np.eye(expected_dp))
    assert_close("transfer X*X", alpha_p * alpha_m * sum(v.T @ v for v in x),
                 alpha_p * np.eye(expected_dm))

    # Cell restriction amplitudes and the left/right alternating phase.
    d = a - 1
    c = math.sqrt(q * (a - 1) / (a * (q - 1)))
    h_l = list(range(a))
    h_r = list(range(a, 2 * a))
    z_l, z_r = h_l[0], h_r[0]
    v_l = math.sqrt(a / (a - 1)) * (
        np.eye(q)[:, z_l] - sum(np.eye(q)[:, j] for j in h_l) / a
    )
    v_r = math.sqrt(a / (a - 1)) * (
        np.eye(q)[:, z_r] - sum(np.eye(q)[:, j] for j in h_r) / a
    )
    # One unit standard vector in each opposite cell.
    y_r = (np.eye(q)[:, h_r[1]] - np.eye(q)[:, h_r[2]]) / math.sqrt(2)
    y_l = (np.eye(q)[:, h_l[1]] - np.eye(q)[:, h_l[2]]) / math.sqrt(2)
    vl, vr, yr, yl = (qv.T @ w for w in (v_l, v_r, y_r, y_l))

    def branch_coordinates(z: int) -> tuple[np.ndarray, np.ndarray]:
        wz = null_basis(u[z])
        return ip[z].T @ (bplus.T), im[z].T @ (bminus.T)

    pull_p_l, pull_m_l = branch_coordinates(z_l)
    pull_p_r, pull_m_r = branch_coordinates(z_r)
    phi_p_l = (np.kron(vl, yr) + np.kron(yr, vl)) / math.sqrt(2)
    phi_m_l = (np.kron(vl, yr) - np.kron(yr, vl)) / math.sqrt(2)
    phi_p_r = (np.kron(yl, vr) + np.kron(vr, yl)) / math.sqrt(2)
    phi_m_r = (np.kron(yl, vr) - np.kron(vr, yl)) / math.sqrt(2)
    # Compare norms and signs through the corresponding W_z coordinates.
    w_l = null_basis(u[z_l]).T @ yr
    w_r = null_basis(u[z_r]).T @ yl
    assert_close("left symmetric amplitude", pull_p_l @ phi_p_l, (c / p) * w_l)
    assert_close("left alternating amplitude", pull_m_l @ phi_m_l, c * w_l)
    assert_close("right symmetric amplitude", pull_p_r @ phi_p_r, (c / p) * w_r)
    assert_close("right alternating phase", pull_m_r @ phi_m_r, -c * w_r)

    r_p = c * c / (d * p * p)
    r_m = c * c / d
    assert_close("r_plus formula", r_p, (q - 2) / (a * (q - 3)))
    assert_close("r_minus formula", r_m, q / (a * (q - 1)))
    assert_close("alpha_plus r_plus", alpha_p * r_p, 1 / (2 * a))
    assert_close("alpha_minus r_minus", alpha_m * r_m, 1 / (2 * a))

    return PointModel(q, a, alpha_p, alpha_m, delta_p, delta_m,
                      r_p, r_m, ip, im, pi_p, pi_m, xi_p, xi_m, x)


def scaled_literal(rows: int, cols: int, target_gram_norm: float) -> np.ndarray:
    x = RNG.normal(size=(rows, cols))
    x *= math.sqrt(target_gram_norm) / opnorm(x)
    return x


def positive_contraction(dim: int, kappa: float) -> np.ndarray:
    q, _ = np.linalg.qr(RNG.normal(size=(dim, dim)))
    eig = np.sqrt(kappa + (1 - kappa) * RNG.random(dim))
    return q @ np.diag(eig) @ q.T


@dataclass
class Occurrence:
    rp: np.ndarray
    rm: np.ndarray
    c: np.ndarray
    sp: np.ndarray
    sm: np.ndarray


def occurrence(cp: int, cm: int, raw: int, model: PointModel,
               kappa: float) -> Occurrence:
    lp = scaled_literal(raw, cp, 0.61 * model.r_p / kappa)
    lm = scaled_literal(raw, cm, 0.57 * model.r_m / kappa)
    rp = lp.T @ lp
    rm = lm.T @ lm
    c = lp.T @ lm
    sp = np.eye(cp) - rp
    sm = np.eye(cm) - rm
    assert_le("Rplus cap", opnorm(rp), model.r_p / kappa)
    assert_le("Rminus cap", opnorm(rm), model.r_m / kappa)
    assert_le("cross Gram cap", opnorm(c), math.sqrt(model.r_p * model.r_m) / kappa)
    assert_le("Splus positive", -float(np.linalg.eigvalsh(sp)[0]), 0.0)
    assert_le("Sminus positive", -float(np.linalg.eigvalsh(sm)[0]), 0.0)
    return Occurrence(rp, rm, c, sp, sm)


def full_effect(model: PointModel, occ: Occurrence, z: int,
                sigma: float) -> np.ndarray:
    pp, pm = model.pi_p[z], model.pi_m[z]
    xp, xm = model.xi_p[z], model.xi_m[z]
    xx = model.x[z]
    tl = model.alpha_p * np.kron(pp, occ.rp) + model.delta_p * np.kron(xp, occ.sp)
    br = model.alpha_m * np.kron(pm, occ.rm) + model.delta_m * np.kron(xm, occ.sm)
    tr = sigma * math.sqrt(model.alpha_p * model.alpha_m) * np.kron(xx, occ.c)
    return np.block([[tl, tr], [tr.T, br]])


def block_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.block([
        [a, np.zeros((a.shape[0], b.shape[1]))],
        [np.zeros((b.shape[0], a.shape[1])), b],
    ])


def random_k(e0: int, e1: int, kappa: float) -> tuple[np.ndarray, np.ndarray]:
    b = RNG.normal(size=(e1, e0))
    h0 = positive_contraction(e0, kappa)
    h1 = positive_contraction(e1, kappa)
    k = h1 @ b @ h0
    assert_le("polar upper norm", opnorm(k), opnorm(b))
    assert_le("polar lower norm", kappa * opnorm(b), opnorm(k))
    return b, k


def effect_and_equality_gate(model: PointModel, dims: tuple[int, int, int, int],
                             label: str) -> None:
    e0p, e0m, e1p, e1m = dims
    kappa = 0.82
    o0 = occurrence(e0p, e0m, max(e0p, e0m) + 2, model, kappa)
    o1 = occurrence(e1p, e1m, max(e1p, e1m) + 2, model, kappa)
    bp, kp = random_k(e0p, e1p, kappa)
    bm, km = random_k(e0m, e1m, kappa)

    target0 = block_diag(np.eye(model.dp * e0p), np.eye(model.dm * e0m))
    target1 = block_diag(np.eye(model.dp * e1p), np.eye(model.dm * e1m))
    for sigma, side in ((1.0, "L"), (-1.0, "R")):
        f0 = [full_effect(model, o0, z, sigma) for z in range(model.q)]
        f1 = [full_effect(model, o1, z, sigma) for z in range(model.q)]
        assert_close(f"{label}/{side} sum F0", sum(f0), target0)
        assert_close(f"{label}/{side} sum F1", sum(f1), target1)
        assert_le(f"{label}/{side} F0 positivity", -float(np.linalg.eigvalsh(f0[0])[0]), 0.0,
                  5e-10)
        assert_le(f"{label}/{side} F1 positivity", -float(np.linalg.eigvalsh(f1[0])[0]), 0.0,
                  5e-10)

        t = block_diag(np.kron(np.eye(model.dp), kp),
                       np.kron(np.eye(model.dm), km))
        equality = sum(f1[z] @ t @ f0[z] for z in range(model.q))
        ep = (model.alpha_p * o1.rp @ kp @ o0.rp
              + model.alpha_m * o1.c @ km @ o0.c.T
              + model.delta_p * o1.sp @ kp @ o0.sp)
        em = (model.alpha_m * o1.rm @ km @ o0.rm
              + model.alpha_p * o1.c.T @ kp @ o0.c
              + model.delta_m * o1.sm @ km @ o0.sm)
        expected = block_diag(np.kron(np.eye(model.dp), ep),
                              np.kron(np.eye(model.dm), em))
        assert_close(f"{label}/{side} full equality formula", equality, expected, 8e-10)

        cut_row = model.dp * e1p
        cut_col = model.dp * e0p
        assert_close(f"{label}/{side} summed +- block", equality[:cut_row, cut_col:],
                     np.zeros((cut_row, model.dm * e0m)), 8e-10)
        assert_close(f"{label}/{side} summed -+ block", equality[cut_row:, :cut_col],
                     np.zeros((model.dm * e1m, cut_col)), 8e-10)
        one_value = f1[0] @ t @ f0[0]
        if opnorm(one_value[:cut_row, cut_col:]) < 1e-9:
            raise AssertionError("per-value cross block unexpectedly vanished")
        print(f"PASS {label}/{side} per-value cross block is nonzero before Schur sum")

        mb = max(opnorm(bp), opnorm(bm))
        bound_p = (model.delta_p + model.r_p / (model.a * kappa * kappa)) * mb
        bound_m = (model.delta_m + model.r_m / (model.a * kappa * kappa)) * mb
        assert_le(f"{label}/{side} Eplus norm bound", opnorm(ep), bound_p)
        assert_le(f"{label}/{side} Eminus norm bound", opnorm(em), bound_m)
        eps = max(bound_p, bound_m) / mb
        chosen_k = kp if opnorm(bp) >= opnorm(bm) else km
        chosen_e = ep if opnorm(bp) >= opnorm(bm) else em
        assert_le(f"{label}/{side} reverse-triangle retention",
                  (kappa - eps) * mb, opnorm(chosen_k - chosen_e), 2e-10)


def symbolic_scalar_gate() -> None:
    for a in (2, 3, 4, 16, 25, 64):
        q = 4 * a
        alpha_p = (q - 3) / (2 * (q - 2))
        alpha_m = (q - 1) / (2 * q)
        r_p = (q - 2) / (a * (q - 3))
        r_m = q / (a * (q - 1))
        assert_close(f"a={a} alpha+r+", alpha_p * r_p, 1 / (2 * a))
        assert_close(f"a={a} alpha-r-", alpha_m * r_m, 1 / (2 * a))
        dp = (q - 3) / ((q - 1) * (q - 4))
        dm = (q - 1) / (q * (q - 3))
        assert_close(f"a={a} private plus Schur scalar", q - 1 / alpha_p, 1 / dp)
        assert_close(f"a={a} private minus Schur scalar", q - 1 / alpha_m, 1 / dm)
    print("PASS scalar identities include the legal a=s^2>=16 regime")


def main() -> None:
    symbolic_scalar_gate()
    model = construct_point_model(q=12, a=3)
    effect_and_equality_gate(model, (1, 1, 1, 1), "c=1")
    effect_and_equality_gate(model, (2, 3, 3, 2), "c>1 unequal rectangular")
    print(f"MAX_MATRIX_RESIDUAL={MAX_MATRIX_RESIDUAL:.3e}")
    print("ALL_GATES_PASS")


if __name__ == "__main__":
    main()
