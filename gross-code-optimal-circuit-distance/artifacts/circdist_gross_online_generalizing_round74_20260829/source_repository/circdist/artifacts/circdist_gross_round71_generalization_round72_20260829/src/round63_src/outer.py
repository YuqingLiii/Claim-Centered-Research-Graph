#!/usr/bin/env python3
"""Exact full-space outer scheduler for the frozen 864 named Gross CNOT edges."""
from __future__ import annotations
import hashlib, time
import z3
import model as M


class OuterScheduler:
    def __init__(self, require_interleaved=True):
        self.s = z3.Solver()
        self.t = {e: z3.Int('t_' + e.replace(':', '_')) for e in M.ALL_EDGES}
        self.blocks = []
        for v in self.t.values():
            self.s.add(v >= 0, v < 864)
        # Every check ancilla and every data qubit has exactly its six incident named edges.
        for a, row in enumerate(M.Xchecks):
            self.s.add(z3.Distinct([self.t[M.edge_key('X', a, q)] for q in row]))
        for b, row in enumerate(M.Zchecks):
            self.s.add(z3.Distinct([self.t[M.edge_key('Z', b, q)] for q in row]))
        for q in range(M.N):
            inc = ([self.t[M.edge_key('X', a, q)] for a in M.Xof[q]] +
                   [self.t[M.edge_key('Z', b, q)] for b in M.Zof[q]])
            assert len(inc) == 6
            self.s.add(z3.Distinct(inc))
        # MC on every one of the 648 two-qubit overlaps.
        for a, b, sh in M.OVERLAPS:
            assert len(sh) == 2
            q0, q1 = sh
            self.s.add((self.t[M.edge_key('Z', b, q0)] < self.t[M.edge_key('X', a, q0)]) ==
                       (self.t[M.edge_key('Z', b, q1)] < self.t[M.edge_key('X', a, q1)]))
        if require_interleaved:
            xs = [self.t[e] for e in M.ALL_EDGES if e.startswith('X:')]
            zs = [self.t[e] for e in M.ALL_EDGES if e.startswith('Z:')]
            xmin, xmax, zmin, zmax = z3.Ints('xmin xmax zmin zmax')
            self.s.add(*[xmin <= x for x in xs], z3.Or([xmin == x for x in xs]))
            self.s.add(*[xmax >= x for x in xs], z3.Or([xmax == x for x in xs]))
            self.s.add(*[zmin <= z for z in zs], z3.Or([zmin == z for z in zs]))
            self.s.add(*[zmax >= z for z in zs], z3.Or([zmax == z for z in zs]))
            # Negations of all-X-before-all-Z and all-Z-before-all-X.
            self.s.add(xmax >= zmin, zmax >= xmin)

    def fix_schedule(self, times):
        for e in M.ALL_EDGES:
            self.s.add(self.t[e] == int(times[e]))

    def add_block(self, atoms, tag, trace_sha256=None):
        # A block is the negation of the conjunction that preserves a replayed mechanism.
        assert atoms
        z = []
        for a, op, b in atoms:
            assert op == '<' and a in self.t and b in self.t
            z.append(z3.Not(self.t[a] < self.t[b]))
        self.s.add(z3.Or(z))
        self.blocks.append({'tag': tag, 'atoms': atoms, 'atom_count': len(atoms),
                            'trace_sha256': trace_sha256})

    def solve(self, timeout_ms=30000):
        self.s.set(timeout=int(timeout_ms))
        formula = self.s.to_smt2()
        t0 = time.time()
        ans = self.s.check()
        elapsed = round(time.time() - t0, 6)
        out = {'status': str(ans).upper(), 'seconds': elapsed, 'timeout_ms': timeout_ms,
               'reason_unknown': self.s.reason_unknown() if ans == z3.unknown else None,
               'blocks': len(self.blocks), 'smt2_sha256': hashlib.sha256(formula.encode()).hexdigest(),
               'assertions': len(self.s.assertions()), 'edge_variables': len(self.t),
               'model_complete_requested': True}
        if ans != z3.sat:
            return out
        m = self.s.model()
        raw = {e: m.eval(v, model_completion=True).as_long() for e, v in self.t.items()}
        comp = M.compress_schedule(raw)
        audit = M.audit_schedule(comp, True)
        out['raw_used_values'] = len(set(raw.values()))
        out['compressed_schedule'] = comp
        out['audit'] = audit
        if not audit['ok']:
            out['status'] = 'VERIFIER_REJECTED'
        return out
