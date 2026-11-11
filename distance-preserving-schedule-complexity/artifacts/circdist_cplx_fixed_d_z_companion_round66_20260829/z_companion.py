"""Exact GF(2) model for the round-66 private-sentinel Z transform.

This file is standard-library-only.  Bit i of an int is physical qubit i.
It deliberately does not import any repository module.
"""

from dataclasses import dataclass

from construction import Code, in_span, rref


def parity(x):
    return bin(x).count("1") & 1


def weight(x):
    return bin(x).count("1")


def rank(rows, n):
    return len(rref(list(rows), n)[0])


@dataclass
class MatrixCode:
    n: int
    hx: list
    hz: list
    name: str = ""

    def css(self):
        return all(parity(x & z) == 0 for x in self.hx for z in self.hz)

    def parameters(self):
        rx = rank(self.hx, self.n)
        rz = rank(self.hz, self.n)
        return rx, rz, self.n - rx - rz


def from_code(c, name=""):
    assert isinstance(c, Code)
    return MatrixCode(c.n, list(c.hx), list(c.hz), name)


def direct_sum(a, b, name=""):
    shift = a.n
    return MatrixCode(
        a.n + b.n,
        list(a.hx) + [x << shift for x in b.hx],
        list(a.hz) + [z << shift for z in b.hz],
        name or (a.name + "+" + b.name),
    )


def repetition3_matrix(c, name=""):
    """The reviewed R_3 transform, directly on row masks."""
    hx = []
    for x in c.hx:
        y = 0
        for q in range(c.n):
            if (x >> q) & 1:
                y |= 1 << (3 * q)
        hx.append(y)
    for q in range(c.n):
        hx.append((1 << (3 * q)) | (1 << (3 * q + 1)))
        hx.append((1 << (3 * q)) | (1 << (3 * q + 2)))
    hz = []
    for z in c.hz:
        y = 0
        for q in range(c.n):
            if (z >> q) & 1:
                y |= 7 << (3 * q)
        hz.append(y)
    return MatrixCode(3 * c.n, hx, hz, name or ("R3(" + c.name + ")"))


def support(v, n):
    return [q for q in range(n) if (v >> q) & 1]


def block_contiguous_orders(old, lifted, old_orders=None):
    """Three-copy blocks in an explicitly supplied old-qubit order."""
    if old_orders is None:
        old_orders = [support(z, old.n) for z in old.hz]
    assert len(old_orders) == len(lifted.hz) == len(old.hz)
    ans = []
    for z, order in zip(old.hz, old_orders):
        assert sorted(order) == support(z, old.n)
        ans.append(tuple(3 * q + a for q in order for a in range(3)))
    return ans


@dataclass
class Decorated:
    code: MatrixCode
    z_orders: list
    old_n: int
    blocks_by_row: list
    decorated_row_indices: list
    marker_row_indices: list
    total_blocks: int


def decorate_z(code, name=""):
    """Private-sentinel transform D_Z from the proof.

    For an emitted Z row z of weight W, allocate L=W+2 private repetition
    triples.  Keep each triple's two X checks and weight-3 Z check, and replace
    z by z plus all L triple checks.  The returned local orders are singleton.
    """
    next_q = code.n
    blocks_by_row = []
    total_blocks = 0
    for z in code.hz:
        w = weight(z)
        assert w >= 1
        blocks = []
        for _ in range(w + 2):
            blocks.append((next_q, next_q + 1, next_q + 2))
            next_q += 3
            total_blocks += 1
        blocks_by_row.append(blocks)

    hx = list(code.hx)
    for blocks in blocks_by_row:
        for a, b, c in blocks:
            hx.append((1 << a) | (1 << b))
            hx.append((1 << a) | (1 << c))

    hz = []
    z_orders = []
    decorated_row_indices = []
    marker_row_indices = []
    for z, blocks in zip(code.hz, blocks_by_row):
        old_order = support(z, code.n)
        w = len(old_order)
        marker_sum = 0
        for a, b, c in blocks:
            marker_sum |= (1 << a) | (1 << b) | (1 << c)
        decorated_row_indices.append(len(hz))
        hz.append(z | marker_sum)
        order = [blocks[0][0], blocks[1][0]]
        for i, q in enumerate(old_order):
            order.extend((blocks[i + 2][0], q))
        for a, b, c in blocks:
            order.extend((b, c))
        assert len(order) == weight(hz[-1]) and len(set(order)) == len(order)
        z_orders.append(tuple(order))
        for block in blocks:
            marker_row_indices.append(len(hz))
            row = sum(1 << q for q in block)
            hz.append(row)
            z_orders.append(tuple(block))

    out = MatrixCode(next_q, hx, hz, name or ("DZ(" + code.name + ")"))
    return Decorated(out, z_orders, code.n, blocks_by_row,
                     decorated_row_indices, marker_row_indices, total_blocks)


def detector_columns(rows, n):
    cols = [0] * n
    for i, row in enumerate(rows):
        x = row
        q = 0
        while x:
            if x & 1:
                cols[q] |= 1 << i
            q += 1
            x >>= 1
    return cols


def xor_columns(cols, v):
    ans = 0
    q = 0
    while v:
        if v & 1:
            ans ^= cols[q]
        q += 1
        v >>= 1
    return ans


def canonical(v, rb, piv):
    for r, p in zip(rb, piv):
        if (v >> p) & 1:
            v ^= r
    return v


def terminal_columns(rows, orders, n, sector):
    """Distinct-location terminal columns, including harmless support columns."""
    assert len(rows) == len(orders)
    out = [(1 << q, (sector, "data", q)) for q in range(n)]
    for ri, (row, order) in enumerate(zip(rows, orders)):
        assert set(order) == set(support(row, n)) and len(order) == weight(row)
        prefix = 0
        for cut, q in enumerate(order[:-1], 1):
            prefix ^= 1 << q
            # Prefix is quotient-equivalent to the physical suffix hook.
            out.append((prefix, (sector, "hook-prefix", ri, cut)))
        out.append((row, (sector, "support-stabilizer", ri)))
    return out


def two_fault_audit(code, sector, orders):
    """Exact one/two-column audit via (syndrome, stabilizer quotient) keys.

    A pair u,v is a nontrivial logical exactly when its detector syndromes are
    equal and its quotient classes differ.  This checks every pair without a
    quadratic loop.
    """
    if sector == "Z":
        stabilizers, detectors = code.hz, code.hx
    elif sector == "X":
        stabilizers, detectors = code.hx, code.hz
    else:
        raise ValueError(sector)
    rows = stabilizers
    rb, piv = rref(list(stabilizers), code.n)
    dcols = detector_columns(detectors, code.n)
    cols = terminal_columns(rows, orders, code.n, sector)
    seen = {}
    for v, label in cols:
        syn = xor_columns(dcols, v)
        cls = canonical(v, rb, piv)
        if syn == 0 and cls != 0:
            return {
                "safe": False,
                "kind": "one-column",
                "labels": [label],
                "logical_support": support(v, code.n),
                "logical_weight": weight(v),
            }
        if syn in seen and seen[syn][0] != cls:
            ucls, u, ulabel = seen[syn]
            logical = u ^ v
            return {
                "safe": False,
                "kind": "two-column",
                "labels": [ulabel, label],
                "logical_support": support(logical, code.n),
                "logical_weight": weight(logical),
                "class_xor_weight": weight(ucls ^ cls),
            }
        seen.setdefault(syn, (cls, v, label))
    return {
        "safe": True,
        "columns": len(cols),
        "syndrome_classes": len(seen),
        "stabilizer_rank": len(rb),
    }


def transformed_rowspace_expected(code, dec):
    """Check the exact rank/direct-sum identities of the transform."""
    out = dec.code
    rx0, rz0, k0 = code.parameters()
    rx1, rz1, k1 = out.parameters()
    L = dec.total_blocks
    return {
        "css": out.css(),
        "rank_before": [rx0, rz0, k0],
        "rank_after": [rx1, rz1, k1],
        "expected_after": [rx0 + 2 * L, rz0 + L, k0],
        "rank_identity": (rx1, rz1, k1) == (rx0 + 2 * L, rz0 + L, k0),
    }


def sentinel_state_audit(dec):
    """Check the universal marker-state path facts row by row.

    This is a finite structural assertion about the emitted order, not a
    substitute for the proof that the facts imply Z safety.
    """
    details = []
    for source_ri, (blocks, dri) in enumerate(zip(dec.blocks_by_row,
                                                  dec.decorated_row_indices)):
        order = dec.z_orders[dec.decorated_row_indices[source_ri]]
        block_of = {}
        role = {}
        for j, (a, b, c) in enumerate(blocks):
            block_of[a] = block_of[b] = block_of[c] = j
            role[a], role[b], role[c] = 0, 1, 2
        state = [(0, 0) for _ in blocks]
        seen = {}
        data_seen = []
        duplicate_deltas = []
        old_prefix = 0
        for cut, q in enumerate(order[:-1], 1):
            if q < dec.old_n:
                old_prefix ^= 1 << q
            else:
                j = block_of[q]
                bits = [0, 0, 0]
                # Reconstruct actual prefix bits of block j from order prefix.
                prefix_set = set(order[:cut])
                a, b, c = blocks[j]
                bits = [int(x in prefix_set) for x in (a, b, c)]
                state[j] = (bits[0] ^ bits[1], bits[0] ^ bits[2])
            key = tuple(state)
            assert any(x != (0, 0) for x in key)
            if key in seen:
                prev_old, prev_cut = seen[key]
                delta = old_prefix ^ prev_old
                duplicate_deltas.append((prev_cut, cut, weight(delta)))
                assert weight(delta) == 1
            else:
                seen[key] = (old_prefix, cut)
            data_seen.append(weight(old_prefix))
        details.append({
            "source_row": source_ri,
            "states": len(order) - 1,
            "unique_states": len(seen),
            "duplicate_state_deltas": duplicate_deltas,
            "all_duplicates_one_data": all(x[2] == 1 for x in duplicate_deltas),
        })
    return details
