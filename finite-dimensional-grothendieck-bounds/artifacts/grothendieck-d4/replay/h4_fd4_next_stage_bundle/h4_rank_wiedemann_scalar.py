#!/usr/bin/env python3
"""
h4_rank_wiedemann_scalar.py

Deterministic-seed exact Wiedemann lower-rank certificate backend over GF(24001).

This is a mathematically rigorous FALLBACK rank certificate for the canonical
moment-to-K operator A.  It uses
    B = A^T D A
where D is a deterministic blockwise diagonal congruence/weighting generated
from the seed.  For every choice of D,
    rank(B) <= rank(A).

For deterministic u,v, form
    s_k = u^T B^k v.
Berlekamp-Massey gives the exact minimal recurrence degree d of this scalar
sequence.  That degree is <= degree(minpoly(B)) <= rank(B)+1.  Hence

    rank(A) >= rank(B) >= d-1.

Therefore a recurrence degree >= 746798 proves
    rank(A) >= 746797,
which together with the exact equality-supported upper bound rank(A)<=746797
would close the rank.

CERTIFICATE
===========
The certificate JSON stores:
  p, seed, sequence s_0,...,s_{2L-1}, BM connection polynomial C,
  recurrence degree d, and claimed lower bound d-1.

The standalone --verify mode:
  * recomputes BM from the stored exact sequence;
  * checks every stored recurrence identity over GF(p);
  * checks d-1 equals the claimed rank lower bound.

This verifies the algebraic conclusion from the sequence.  To audit that the
sequence itself came from the canonical A, rerun --generate against the pinned
operator inputs and compare sequence SHA-256.

The implementation is checkpointable.  It is intentionally scalar Wiedemann
(block size one); this makes the compact certificate/verifier completely
transparent.  A true multi-RHS block-Wiedemann backend would reduce the number
of B applications but needs a matrix-polynomial minimal-generator verifier.

Python 3.9+.
"""

import sys, json, hashlib, argparse
from pathlib import Path
import numpy as np

P = 24001
TARGET_RANK = 746797
TARGET_RECURRENCE_DEGREE = TARGET_RANK + 1


def die(x):
    raise SystemExit("ERROR: " + str(x))


def inv(a):
    return pow(int(a) % P, P - 2, P)


def bm(sequence):
    """Berlekamp-Massey over GF(P), returns C with C[0]=1."""
    s = [int(x) % P for x in sequence]
    C = [1]
    B = [1]
    L = 0
    m = 1
    b = 1
    for n in range(len(s)):
        d = s[n]
        for i in range(1, L + 1):
            d = (d + C[i] * s[n - i]) % P
        if d == 0:
            m += 1
            continue
        T = C[:]
        coef = d * inv(b) % P
        need = len(B) + m
        if len(C) < need:
            C += [0] * (need - len(C))
        for j in range(len(B)):
            C[j + m] = (C[j + m] - coef * B[j]) % P
        if 2 * L <= n:
            L = n + 1 - L
            B = T
            b = d
            m = 1
        else:
            m += 1
    if len(C) < L + 1:
        C += [0] * (L + 1 - len(C))
    return [int(x) % P for x in C[:L + 1]]


def recurrence_ok(seq, C):
    L = len(C) - 1
    for n in range(L, len(seq)):
        z = int(seq[n]) % P
        for i in range(1, L + 1):
            z = (z + int(C[i]) * int(seq[n - i])) % P
        if z:
            return False, n, z
    return True, None, None


def deterministic_vec(n, seed, tag):
    # xorshift64* deterministic generator; reduction mod P.
    x = (int(seed) ^ (0x9E3779B97F4A7C15 * (tag + 1))) & ((1 << 64) - 1)
    out = np.empty(n, dtype=np.int64)
    for i in range(n):
        x ^= (x >> 12)
        x ^= (x << 25) & ((1 << 64) - 1)
        x ^= (x >> 27)
        x &= ((1 << 64) - 1)
        y = (x * 2685821657736338717) & ((1 << 64) - 1)
        out[i] = y % P
    return out


def load_operator(args):
    # Imported lazily so --verify has no heavy dependencies.
    from h4_K_linear_operator_modp_batched import OperatorBatched
    blocks = [int(x) for x in args.blocks.split(",")] if args.blocks else list(range(1,21))
    return OperatorBatched(args.system, args.nogap, args.specdir, args.cachedir, blocks)


def block_weights(O, seed):
    """
    Deterministic positive/nonzero modular weighting D on each symmetric block.
    D(Y)_ij = a_i a_j Y_ij (congruence by diagonal a).
    This preserves symmetry and is invertible on each full matrix space.
    """
    out = []
    for bi, b in enumerate(O.blocks):
        k = int(b["meta"]["m_K"])
        a = deterministic_vec(k, seed, 1000 + bi)
        a[a == 0] = 1
        out.append(a)
    return out


def apply_B(O, x, weights):
    Ys = O.A(x)
    WY = []
    for Y, a in zip(Ys, weights):
        # congruence D(Y)=diag(a) Y diag(a)
        WY.append((a[:, None] * (Y % P) * a[None, :]) % P)
    return O.AT(WY) % P


def generate(args):
    O = load_operator(args)
    n = len(O.eff_to_global)
    u = deterministic_vec(n, args.seed, 1)
    v = deterministic_vec(n, args.seed, 2)
    weights = block_weights(O, args.seed)

    seq = []
    w = v.copy()
    checkpoint = Path(args.checkpoint)
    start = 0

    if checkpoint.exists() and args.resume:
        z = np.load(checkpoint)
        w = z["w"].astype(np.int64) % P
        seq = [int(x) for x in z["sequence"].tolist()]
        start = len(seq)

    for k in range(start, args.terms):
        seq.append(int(np.dot(u % P, w % P)) % P)
        if (k + 1) < args.terms:
            w = apply_B(O, w, weights)
        if args.checkpoint_every and (k + 1) % args.checkpoint_every == 0:
            np.savez_compressed(
                checkpoint,
                w=w.astype(np.uint16),
                sequence=np.asarray(seq, dtype=np.uint16),
            )
            print(json.dumps({
                "term_count": len(seq),
                "sequence_sha256": hashlib.sha256(
                    np.asarray(seq, dtype="<u2").tobytes()
                ).hexdigest(),
            }), flush=True)

    C = bm(seq)
    ok, bad_n, bad = recurrence_ok(seq, C)
    if not ok:
        die("BM recurrence self-check failed at %s residue %s" % (bad_n, bad))
    d = len(C) - 1
    lower = max(0, d - 1)

    cert = {
        "status": (
            "RANK_TARGET_PROVED"
            if lower >= TARGET_RANK
            else "PARTIAL_WIEDEMANN_LOWER_BOUND"
        ),
        "field_prime": P,
        "seed": int(args.seed),
        "operator": "B=A^T D A with deterministic invertible diagonal block congruences D",
        "blocks": [int(b["ir"]) for b in O.blocks],
        "sequence_length": len(seq),
        "sequence": seq,
        "connection_polynomial": C,
        "recurrence_degree": d,
        "rank_A_lower_bound": lower,
        "target_rank": TARGET_RANK,
        "target_recurrence_degree": TARGET_RECURRENCE_DEGREE,
        "sequence_sha256": hashlib.sha256(
            np.asarray(seq, dtype="<u2").tobytes()
        ).hexdigest(),
        "u_sha256": hashlib.sha256(u.astype("<u2").tobytes()).hexdigest(),
        "v_sha256": hashlib.sha256(v.astype("<u2").tobytes()).hexdigest(),
        "logical_implication": (
            "deg(sequence recurrence)<=deg(minpoly(B))<=rank(B)+1<=rank(A)+1"
        ),
    }
    raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
    out = Path(args.output)
    out.write_bytes(raw)
    disp = dict(cert)
    disp["output_path"] = str(out)
    disp["output_sha256"] = hashlib.sha256(raw).hexdigest()
    print(json.dumps(disp, indent=2, sort_keys=True))


def verify(path):
    raw = Path(path).read_bytes()
    x = json.loads(raw)
    if int(x["field_prime"]) != P:
        die("wrong prime")
    seq = [int(z) % P for z in x["sequence"]]
    C0 = [int(z) % P for z in x["connection_polynomial"]]
    C = bm(seq)
    if C != C0:
        die("stored connection polynomial != independently recomputed BM")
    ok, bad_n, bad = recurrence_ok(seq, C)
    if not ok:
        die("stored recurrence fails at %s residue %s" % (bad_n, bad))
    d = len(C) - 1
    lower = max(0, d - 1)
    if d != int(x["recurrence_degree"]):
        die("degree mismatch")
    if lower != int(x["rank_A_lower_bound"]):
        die("rank lower bound mismatch")
    sh = hashlib.sha256(np.asarray(seq, dtype="<u2").tobytes()).hexdigest()
    if sh != x["sequence_sha256"]:
        die("sequence SHA mismatch")
    out = {
        "status": "WIEDEMANN_CERTIFICATE_ALGEBRA_VERIFIED",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "recurrence_degree": d,
        "rank_A_lower_bound": lower,
        "target_rank_reached": lower >= TARGET_RANK,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("system")
    g.add_argument("nogap")
    g.add_argument("specdir")
    g.add_argument("cachedir")
    g.add_argument("--seed", type=int, default=20260829)
    g.add_argument("--blocks", default="", help="comma-separated blocks; empty means all 1..20")
    g.add_argument("--terms", type=int, default=64)
    g.add_argument("--checkpoint-every", type=int, default=8)
    g.add_argument("--checkpoint", default="wiedemann_checkpoint.npz")
    g.add_argument("--resume", action="store_true")
    g.add_argument("--output", default="wiedemann_certificate.json")
    v = sub.add_parser("verify")
    v.add_argument("certificate")
    args = ap.parse_args()
    if args.cmd == "generate":
        generate(args)
    else:
        verify(args.certificate)


if __name__ == "__main__":
    main()
