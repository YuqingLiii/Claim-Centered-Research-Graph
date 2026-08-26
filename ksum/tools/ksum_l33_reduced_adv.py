"""L33: isotypic/Wedderburn-reduced dual Adv+/- SDP for cyclic 2-Sum.

The unreduced HLS matrix is indexed by (input, queried position).  Cross-position
blocks occur in neither the affine constraints nor the objective, so setting them
to zero is exact.  Averaging the remaining block diagonal matrix under
G=S_n x C(sigma), sigma(a)=t-a, leaves one input block A=M_0; the other M_i are
position conjugates and A commutes with H=S_{n-1} x C(sigma).

To expose the multiplicity (Wedderburn) blocks without the failed incumbent's
regular representation, the code forms a deterministic generic self-adjoint
element T of the real group algebra R[H].  Every H-invariant A commutes with T, so
A is block diagonal in T's eigenspaces.  Restricting to that block diagonal cone is
lossless: group averaging supplies an optimum in it.  Generic group-algebra
eigenvalues repeat exactly by irreducible multiplicity; the resulting PSD block
sizes are those multiplicities (with an irrep-dimension number of repeated blocks).
Full G orbit representatives deduplicate the equality and objective constraints.

Usage:
  python tools/ksum_l33_reduced_adv.py N Q T [--solver SCS] [--eps 1e-4]
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import sys
import time

import cvxpy as cp
import numpy as np
import scipy
import scipy.linalg


def centralizer_of_sigma(q, target):
    sigma = tuple((target - a) % q for a in range(q))
    out = []
    for p in itertools.permutations(range(q)):
        if all(p[sigma[a]] == sigma[p[a]] for a in range(q)):
            out.append(np.asarray(p, dtype=np.int16))
    return out


def two_sum_labels(inputs, q, target):
    n = inputs.shape[1]
    lab = np.zeros(len(inputs), dtype=np.int8)
    for i in range(n):
        for j in range(i + 1, n):
            lab |= ((inputs[:, i] + inputs[:, j]) % q == target)
    return lab


def lex_indices(arr, q):
    n = arr.shape[1]
    place = q ** np.arange(n - 1, -1, -1, dtype=np.int64)
    return arr @ place


def swap_indices(inputs, q):
    m, n = inputs.shape
    swaps = np.empty((n, m), dtype=np.int64)
    for i in range(n):
        moved = inputs.copy()
        moved[:, [0, i]] = moved[:, [i, 0]]
        swaps[i] = lex_indices(moved, q)
    return swaps


def canonical_pair_codes(inputs, left, right, q, centralizer, chunk=128):
    """Canonical G-orbit codes for ordered pairs of inputs."""
    n = inputs.shape[1]
    base = n + 1
    python_weights = [base**k for k in range(q * q)]
    if python_weights[-1] * q * q > np.iinfo(np.int64).max:
        out = np.empty((len(left), len(right)), dtype=object)
        for ia, a in enumerate(left):
            for ib, b in enumerate(right):
                best = None
                for p in centralizer:
                    code = sum(
                        python_weights[int(p[inputs[a, k]]) * q + int(p[inputs[b, k]])]
                        for k in range(n)
                    )
                    best = code if best is None or code < best else best
                out[ia, ib] = best
        return out
    weights = np.asarray(python_weights, dtype=np.int64)
    out = np.empty((len(left), len(right)), dtype=np.int64)
    right_inputs = inputs[right]
    for lo in range(0, len(left), chunk):
        hi = min(len(left), lo + chunk)
        left_inputs = inputs[left[lo:hi]]
        best = np.full((hi - lo, len(right)), np.iinfo(np.int64).max, dtype=np.int64)
        for p in centralizer:
            pl = p[left_inputs]
            pr = p[right_inputs]
            code = np.zeros_like(best)
            for k in range(n):
                code += weights[pl[:, None, k] * q + pr[None, :, k]]
            np.minimum(best, code, out=best)
        out[lo:hi] = best
    return out


def pair_orbit_representatives(inputs, left, right, q, centralizer, chunk=128):
    """One ordered-pair representative per full-G orbit."""
    reps = {}
    for lo in range(0, len(left), chunk):
        lchunk = left[lo : lo + chunk]
        codes = canonical_pair_codes(
            inputs, lchunk, right, q, centralizer, chunk=max(1, len(lchunk))
        )
        unique, first = np.unique(codes.ravel(), return_index=True)
        for code, pos in zip(unique.tolist(), first.tolist()):
            if code not in reps:
                ia, ib = divmod(pos, len(right))
                reps[code] = (int(lchunk[ia]), int(right[ib]))
    return [reps[k] for k in sorted(reps)]


def canonical_input_codes(inputs, q, centralizer):
    n = inputs.shape[1]
    base = n + 1
    weights = np.asarray([base**k for k in range(q)], dtype=np.int64)
    best = np.full(len(inputs), np.iinfo(np.int64).max, dtype=np.int64)
    for p in centralizer:
        moved = p[inputs]
        code = np.zeros(len(inputs), dtype=np.int64)
        for k in range(n):
            code += weights[moved[:, k]]
        np.minimum(best, code, out=best)
    return best


def input_orbit_representatives(inputs, q, centralizer):
    codes = canonical_input_codes(inputs, q, centralizer)
    _, first = np.unique(codes, return_index=True)
    return sorted(first.tolist())


def cluster_eigenvalues(values, rel_tol=2e-8):
    if not len(values):
        return []
    scale = max(1.0, float(np.max(np.abs(values))))
    gaps = np.flatnonzero(np.diff(values) > rel_tol * scale) + 1
    return [x for x in np.split(np.arange(len(values)), gaps) if len(x)]


def group_algebra_blocks(inputs, q, centralizer):
    """Eigenspaces of a deterministic generic self-adjoint element of R[H]."""
    m, n = inputs.shape
    cols = np.arange(m, dtype=np.int64)
    rng = np.random.default_rng(33020260718)
    tmat = np.zeros((m, m), dtype=np.float64)

    pos_perms = list(itertools.permutations(range(1, n)))
    pos_weights = rng.normal(size=len(pos_perms)) / math.sqrt(len(pos_perms))
    for perm, weight in zip(pos_perms, pos_weights):
        moved = inputs.copy()
        if n > 1:
            moved[:, 1:] = inputs[:, perm]
        mapping = lex_indices(moved, q)
        tmat[mapping, cols] += weight

    alpha_weights = (
        np.sqrt(2.0) * rng.normal(size=len(centralizer)) / math.sqrt(len(centralizer))
    )
    for p, weight in zip(centralizer, alpha_weights):
        mapping = lex_indices(p[inputs], q)
        tmat[mapping, cols] += weight

    tmat = 0.5 * (tmat + tmat.T)
    values, vectors = scipy.linalg.eigh(
        tmat, overwrite_a=True, check_finite=False, driver="evd"
    )
    clusters = cluster_eigenvalues(values)
    blocks = [vectors[:, c].copy() for c in clusters]
    spreads = [
        float(values[c[-1]] - values[c[0]]) if len(c) > 1 else 0.0 for c in clusters
    ]
    gaps = np.diff([float(np.mean(values[c])) for c in clusters])
    info = {
        "position_group_order": len(pos_perms),
        "alphabet_group_order": len(centralizer),
        "spectral_blocks": len(blocks),
        "block_dims": [int(qb.shape[1]) for qb in blocks],
        "max_within_cluster_spread": max(spreads, default=0.0),
        "min_between_cluster_gap": float(np.min(gaps)) if len(gaps) else None,
        "eigen_residual": float(
            max(
                np.linalg.norm(tmat @ qb - qb * np.mean(values[c]), ord=2)
                for qb, c in zip(blocks, clusters)
            )
        ),
    }
    return blocks, info


def stabilizer_generator_mappings(inputs, q, centralizer):
    """Permutation mappings generating S_{n-1} x C(sigma)."""
    m, n = inputs.shape
    mappings = []
    names = []
    for i in range(1, n - 1):
        moved = inputs.copy()
        moved[:, [i, i + 1]] = moved[:, [i + 1, i]]
        mappings.append(lex_indices(moved, q))
        names.append(f"position_swap_{i}_{i+1}")
    identity = np.arange(m)
    for k, p in enumerate(centralizer):
        mapping = lex_indices(p[inputs], q)
        if not np.array_equal(mapping, identity):
            mappings.append(mapping)
            names.append(f"alphabet_{k}")
    return mappings, names


def align_isotypic_copies(blocks, generator_maps):
    """Collapse equivalent spectral copies to one multiplicity block per irrep."""
    count = len(blocks)
    adjacency = [[] for _ in range(count)]
    max_schur_residual = 0.0
    edge_count = 0
    for mapping in generator_maps:
        inverse = np.argsort(mapping)
        transformed = [qb[inverse] for qb in blocks]
        for a, qa in enumerate(blocks):
            for b, pqb in enumerate(transformed):
                if qa.shape[1] != pqb.shape[1]:
                    continue
                intertwiner = qa.T @ pqb
                norm = np.linalg.norm(intertwiner)
                if norm <= 2e-9:
                    continue
                ul, singular, vr = np.linalg.svd(intertwiner)
                polar = ul @ vr
                scalar = float(np.mean(singular))
                max_schur_residual = max(
                    max_schur_residual,
                    float(np.linalg.norm(intertwiner - scalar * polar)),
                )
                adjacency[a].append((b, polar))
                adjacency[b].append((a, polar.T))
                edge_count += 1

    assigned = [None] * count
    families = []
    repetitions = []
    for root in range(count):
        if assigned[root] is not None:
            continue
        dim = blocks[root].shape[1]
        assigned[root] = np.eye(dim)
        queue = [root]
        members = []
        while queue:
            a = queue.pop()
            members.append(a)
            for b, polar in adjacency[a]:
                if assigned[b] is None:
                    assigned[b] = assigned[a] @ polar
                    queue.append(b)
        families.append([blocks[j] @ assigned[j].T for j in members])
        repetitions.append(len(members))
    if any(x is None for x in assigned):
        raise RuntimeError("failed to align every spectral block")
    return families, {
        "isotypic_block_dims": [int(family[0].shape[1]) for family in families],
        "irrep_dimensions_repetitions": repetitions,
        "spectral_copy_edges": edge_count,
        "max_schur_polar_residual": max_schur_residual,
    }


def coefficient_for_entry(block, u, v):
    coeff = np.outer(block[u], block[v])
    return 0.5 * (coeff + coeff.T)


def coefficient_for_family(family, u, v):
    return sum(coefficient_for_entry(block, u, v) for block in family)


def solve_instance(args):
    start = time.perf_counter()
    n, q, target = args.n, args.q, args.target % args.q
    inputs = np.asarray(list(itertools.product(range(q), repeat=n)), dtype=np.int16)
    labels = two_sum_labels(inputs, q, target)
    sigma = [(target - a) % q for a in range(q)]
    tau = sum(1 for a in range(q) if sigma[a] == a)
    centralizer = centralizer_of_sigma(q, target)
    expected = math.factorial(tau) * 2 ** ((q - tau) // 2) * math.factorial(
        (q - tau) // 2
    )
    if len(centralizer) != expected:
        raise RuntimeError(f"centralizer size mismatch: {len(centralizer)} != {expected}")

    print(
        f"INSTANCE n={n} q={q} t={target} inputs={len(inputs)} "
        f"yes={int(labels.sum())} no={int((1-labels).sum())} tau={tau} "
        f"|C(sigma)|={len(centralizer)}",
        flush=True,
    )
    print(
        "RUNTIME "
        f"python={sys.executable} version={platform.python_version()} "
        f"numpy={np.__version__} scipy={scipy.__version__} cvxpy={cp.__version__} "
        f"solvers={cp.installed_solvers()}",
        flush=True,
    )
    print("COMMAND " + " ".join([sys.executable, *sys.argv]), flush=True)

    yes = np.flatnonzero(labels)
    no = np.flatnonzero(1 - labels)
    t0 = time.perf_counter()
    eq_reps = pair_orbit_representatives(
        inputs, yes, no, q, centralizer, chunk=args.chunk
    )
    diag_reps = input_orbit_representatives(inputs, q, centralizer)
    print(
        f"FULL_G_ORBITS equality={len(eq_reps)} diagonal={len(diag_reps)} "
        f"build_s={time.perf_counter()-t0:.3f}",
        flush=True,
    )

    t0 = time.perf_counter()
    blocks, block_info = group_algebra_blocks(inputs, q, centralizer)
    block_dims = block_info["block_dims"]
    print(
        f"WEDDERBURN spectral_blocks={len(blocks)} block_dims={block_dims} "
        f"sum_dims={sum(block_dims)} max_spread="
        f"{block_info['max_within_cluster_spread']:.3e} min_gap="
        f"{block_info['min_between_cluster_gap']} build_s={time.perf_counter()-t0:.3f}",
        flush=True,
    )

    swaps = swap_indices(inputs, q)
    t0 = time.perf_counter()
    generator_maps, generator_names = stabilizer_generator_mappings(
        inputs, q, centralizer
    )
    families, isotypic_info = align_isotypic_copies(blocks, generator_maps)
    true_block_dims = isotypic_info["isotypic_block_dims"]
    variables = [
        cp.Variable((dim, dim), symmetric=True, name=f"isotypic_{k}")
        for k, dim in enumerate(true_block_dims)
    ]
    objective_bound = cp.Variable(nonneg=True, name="adv_pm")
    constraints = [var >> 0 for var in variables]
    print(
        f"COMMUTANT generators={len(generator_maps)} true_block_dims={true_block_dims} "
        f"repetitions={isotypic_info['irrep_dimensions_repetitions']} "
        f"schur_residual={isotypic_info['max_schur_polar_residual']:.3e} "
        f"build_s={time.perf_counter()-t0:.3f}",
        flush=True,
    )
    if args.analyze_only:
        analysis = {
            "n": n, "q": q, "target": target, "tau": tau,
            "centralizer_order": len(centralizer),
            "equality_constraint_orbits": len(eq_reps),
            "diagonal_constraint_orbits": len(diag_reps),
            "wedderburn_block_dims": true_block_dims,
            "spectral_copy_block_dims": block_dims,
            "wall_seconds": time.perf_counter() - start,
            "status": "ANALYZE_ONLY_NO_SOLVE",
        }
        print("ANALYSIS_JSON " + json.dumps(analysis, sort_keys=True), flush=True)
        return analysis

    t0 = time.perf_counter()
    for a, b in eq_reps:
        terms = []
        differing = np.flatnonzero(inputs[a] != inputs[b])
        for family, var in zip(families, variables):
            coeff = np.zeros(var.shape, dtype=np.float64)
            for i in differing:
                coeff += coefficient_for_family(family, swaps[i, a], swaps[i, b])
            terms.append(cp.sum(cp.multiply(coeff, var)))
        constraints.append(sum(terms) == 1)

    for a in diag_reps:
        terms = []
        for family, var in zip(families, variables):
            coeff = np.zeros(var.shape, dtype=np.float64)
            for i in range(n):
                for aligned in family:
                    row = aligned[swaps[i, a]]
                    coeff += np.outer(row, row)
            terms.append(cp.sum(cp.multiply(coeff, var)))
        constraints.append(sum(terms) <= objective_bound)
    print(
        f"AFFINE_BUILD equality={len(eq_reps)} diagonal={len(diag_reps)} "
        f"seconds={time.perf_counter()-t0:.3f}",
        flush=True,
    )

    problem = cp.Problem(cp.Minimize(objective_bound), constraints)
    solve_kw = {"verbose": args.verbose}
    if args.solver.upper() == "SCS":
        solve_kw.update(eps=args.eps, max_iters=args.max_iters)
    tsolve = time.perf_counter()
    problem.solve(solver=args.solver.upper(), **solve_kw)
    solve_seconds = time.perf_counter() - tsolve
    wall_seconds = time.perf_counter() - start
    value = None if objective_bound.value is None else float(objective_bound.value)
    print(
        f"RESULT Adv_pm={value} status={problem.status} solver={args.solver.upper()} "
        f"eps={args.eps} solve_s={solve_seconds:.3f} wall_s={wall_seconds:.3f}",
        flush=True,
    )
    audit = None
    if args.audit and all(var.value is not None for var in variables):
        natural = sum(
            aligned @ np.asarray(var.value) @ aligned.T
            for family, var in zip(families, variables)
            for aligned in family
        )
        natural = 0.5 * (natural + natural.T)
        min_eig = float(np.linalg.eigvalsh(natural)[0])
        commutator = 0.0
        for mapping in generator_maps:
            commutator = max(
                commutator,
                float(np.max(np.abs(natural[np.ix_(mapping, mapping)] - natural))),
            )
        equality_residual = 0.0
        for a in yes:
            for b in no:
                differing = np.flatnonzero(inputs[a] != inputs[b])
                lhs = sum(natural[swaps[i, a], swaps[i, b]] for i in differing)
                equality_residual = max(equality_residual, abs(float(lhs) - 1.0))
        diagonal_violation = 0.0
        for a in range(len(inputs)):
            lhs = sum(natural[swaps[i, a], swaps[i, a]] for i in range(n))
            diagonal_violation = max(diagonal_violation, float(lhs) - float(value))
        audit = {
            "natural_min_eigenvalue": min_eig,
            "max_generator_invariance_residual": commutator,
            "max_full_equality_residual": equality_residual,
            "max_full_diagonal_violation": diagonal_violation,
        }
        print("FULL_AUDIT " + json.dumps(audit, sort_keys=True), flush=True)
    result = {
        "n": n, "q": q, "target": target, "tau": tau,
        "centralizer_order": len(centralizer), "inputs": len(inputs),
        "yes": int(labels.sum()), "no": int((1-labels).sum()),
        "equality_constraint_orbits": len(eq_reps),
        "diagonal_constraint_orbits": len(diag_reps),
        "wedderburn_block_dims": true_block_dims,
        "spectral_copy_block_dims": block_dims,
        "wedderburn": {**block_info, **isotypic_info},
        "stabilizer_generators": len(generator_maps),
        "solver": args.solver.upper(),
        "eps": args.eps, "max_iters": args.max_iters,
        "status": problem.status, "value": value,
        "solve_seconds": solve_seconds, "wall_seconds": wall_seconds,
        "python": sys.executable, "python_version": platform.python_version(),
        "numpy_version": np.__version__, "scipy_version": scipy.__version__,
        "cvxpy_version": cp.__version__,
        "command": " ".join([sys.executable, *sys.argv]), "audit": audit,
    }
    print("RESULT_JSON " + json.dumps(result, sort_keys=True), flush=True)
    return result


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("n", type=int)
    p.add_argument("q", type=int)
    p.add_argument("target", type=int, nargs="?", default=0)
    p.add_argument("--solver", default="SCS")
    p.add_argument("--eps", type=float, default=1e-4)
    p.add_argument("--max-iters", type=int, default=200000)
    p.add_argument("--chunk", type=int, default=128)
    p.add_argument("--verbose", action="store_true")
    p.add_argument("--audit", action="store_true")
    p.add_argument("--analyze-only", action="store_true")
    return p.parse_args()


if __name__ == "__main__":
    try:
        solve_instance(parse_args())
    except Exception as exc:
        print(f"FATAL {type(exc).__name__}: {exc}", flush=True)
        raise
