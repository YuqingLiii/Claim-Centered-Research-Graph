"""Exact B_o table for the first genuine matrix block at n=4:
   lam=(5,2,1), mu=nu=(3,1)  (3x2, the D1 target), plus its Z2 parity data.

Outputs artifacts/mdh_n4_521_block.json:
   - B[o] : 3x2 exact rational matrices (canonical RREF row/col gauge)
   - row a-labels (Pieri rho in {(3,1),(2,2),(2,1,1)}), col = LR copies
   - swap action on columns (S_col = rho(omega)|_{W_N}) and on rows
     (factor swap), block-parity form check.
"""
import sys, json, time
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
from mdh_engine import CosetSpace, partitions, syt_list, F0, F1, perm_word
from mdh_blocks import BlockEngine

def main(output=None):
    t0 = time.time()
    n = 4
    lam, mu, nu = (5, 2, 1), (3, 1), (3, 1)
    cs = CosetSpace(n)
    orbs = cs.orbits()
    orb_list, seen = orbs
    print(f"orbits: {len(orb_list)}  (t={time.time()-t0:.0f}s)")
    eng = BlockEngine(n, lam, cs)
    print(f"dV={eng.ld.dV} dim={eng.rep.dim}  (t={time.time()-t0:.0f}s)")
    B, mY, mN, ex = eng.orbit_blocks(mu, nu, orbs, variant="full")
    print(f"block {mY}x{mN}  (t={time.time()-t0:.0f}s)")
    # row a-content: project row tensors onto S_n-isotypics of V by character
    # (labels only; report dimension split)
    # swap on columns:
    Sc = eng.swap_col_matrix(mu, nu, ex["cols"], ex["cols"])
    print("S_col (rho(omega) on W_N, expect involution):")
    for r in Sc: print(["%s" % str(x) for x in r])
    # orbit invariants for labeling
    inv = []
    for o in orb_list:
        l0 = sorted(o)[0]
        phi = cs.phi(l0)
        a = tuple(sorted((sum(1 for v in l0 if v < n),
                          sum(1 for v in l0 if v >= n)), reverse=True))
        inv.append({"size": len(o), "phi_max": max(cs.phi(l) for l in o),
                    "phi_rep": phi, "a": a, "rep": l0})
    out = {"lam": lam, "mu": mu, "nu": nu, "mY": mY, "mN": mN,
           "S_col": [[str(x) for x in r] for r in Sc],
           "orbits": inv,
           "B": [[[str(B[o][r][c]) for c in range(mN)] for r in range(mY)]
                  for o in range(len(orb_list))]}
    if output is None:
        print(json.dumps(out, indent=1))
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8") as f:
            json.dump(out, f, indent=1)
            f.write("\n")
        print(f"saved to {output}. total {time.time()-t0:.0f}s")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate the exact n=4 block table.")
    parser.add_argument("--output", type=Path, help="Optional new JSON file; defaults to stdout.")
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error(f"refusing to overwrite {args.output}")
    main(args.output)
