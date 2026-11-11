"""T3a -- pin down the rotated-surface LAYOUT CONVENTION by the published funnel.

The dossier reports 576 -> 96 legal -> 16 legal AND (MC), identical at d=3,5,7.
My first reconstruction gave 24 -> 0, so my boundary weight-2 corner convention
differs.  The genuine ambiguity: a weight-2 boundary check is HALF a plaquette,
and which two corner LABELS its two qubits carry depends on whether the virtual
plaquette lies outside the top/bottom (qubits are S.. or N..) or outside the
left/right (qubits are .E or .W).  Enumerate that ambiguity and see which
convention -- if any -- reproduces 96 / 16.
"""
import sys
from itertools import permutations, product
sys.path.insert(0, '/private/tmp/claude-501/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from xval import Code, legal, mc_violations, CORNERS, code_distance


def build_surface(d, parity, top_ns, bot_ns, left_ew, right_ew, xy_boundary):
    """parity: 0/1 which interior colour is Z.
       top_ns: 'S' means top-boundary qubits are the SOUTH corners of a virtual
               plaquette sitting above them; 'N' the other reading.  etc.
       xy_boundary: 'X_tb' = X checks on top/bottom, Z on left/right; else swapped.
    """
    def q(r, c):
        return r * d + c
    xchecks, zchecks = {}, {}
    xcorn, zcorn = {}, {}
    for r in range(d - 1):
        for c in range(d - 1):
            sup = {'NW': q(r, c), 'NE': q(r, c + 1),
                   'SW': q(r + 1, c), 'SE': q(r + 1, c + 1)}
            if (r + c) % 2 == parity:
                zchecks['Z_%d_%d' % (r, c)] = list(sup.values())
                zcorn['Z_%d_%d' % (r, c)] = sup
            else:
                xchecks['X_%d_%d' % (r, c)] = list(sup.values())
                xcorn['X_%d_%d' % (r, c)] = sup
    tb, lr = (xchecks, zchecks) if xy_boundary == 'X_tb' else (zchecks, xchecks)
    tbc, lrc = (xcorn, zcorn) if xy_boundary == 'X_tb' else (zcorn, xcorn)
    tag_tb = 'X' if xy_boundary == 'X_tb' else 'Z'
    tag_lr = 'Z' if xy_boundary == 'X_tb' else 'X'
    for c in range(0, d - 1, 2):
        nm = '%s_top_%d' % (tag_tb, c)
        tb[nm] = [q(0, c), q(0, c + 1)]
        tbc[nm] = {top_ns + 'W': q(0, c), top_ns + 'E': q(0, c + 1)}
    for c in range(1, d - 1, 2):
        nm = '%s_bot_%d' % (tag_tb, c)
        tb[nm] = [q(d - 1, c), q(d - 1, c + 1)]
        tbc[nm] = {bot_ns + 'W': q(d - 1, c), bot_ns + 'E': q(d - 1, c + 1)}
    for r in range(1, d - 1, 2):
        nm = '%s_left_%d' % (tag_lr, r)
        lr[nm] = [q(r, 0), q(r + 1, 0)]
        lrc[nm] = {'N' + left_ew: q(r, 0), 'S' + left_ew: q(r + 1, 0)}
    for r in range(0, d - 1, 2):
        nm = '%s_right_%d' % (tag_lr, r)
        lr[nm] = [q(r, d - 1), q(r + 1, d - 1)]
        lrc[nm] = {'N' + right_ew: q(r, d - 1), 'S' + right_ew: q(r + 1, d - 1)}
    xl = [q(r, 0) for r in range(d)]
    zl = [q(0, c) for c in range(d)]
    code = Code(d * d, xchecks, zchecks, zl, xl, name='rs d=%d' % d)
    code._xcorn, code._zcorn = xcorn, zcorn
    return code


def usched(code, piX, piZ):
    S = {}
    for c in code.xnames:
        cm = code._xcorn[c]
        S[c] = [(cm[l], t) for t, l in enumerate(piX) if l in cm]
    for c in code.znames:
        cm = code._zcorn[c]
        S[c] = [(cm[l], t) for t, l in enumerate(piZ) if l in cm]
    return S


def funnel(code):
    nl = nm = 0
    mem = []
    for piX in permutations(CORNERS):
        for piZ in permutations(CORNERS):
            S = usched(code, piX, piZ)
            if not legal(code, S):
                continue
            nl += 1
            if not mc_violations(code, S):
                nm += 1
                mem.append((piX, piZ))
    return nl, nm, mem


def main():
    print("Searching the layout-convention space for the published funnel 96 -> 16")
    print("(requiring: valid CSS code, code distance = d, funnel at BOTH d=3 and d=5)")
    print()
    hits = []
    for parity, tns, bns, lew, rew, xyb in product(
            (0, 1), ('N', 'S'), ('N', 'S'), ('E', 'W'), ('E', 'W'), ('X_tb', 'Z_tb')):
        c3 = build_surface(3, parity, tns, bns, lew, rew, xyb)
        if c3.validate() != ['OK'] or code_distance(c3) != 3:
            continue
        l3, m3, _ = funnel(c3)
        if (l3, m3) != (96, 16):
            continue
        c5 = build_surface(5, parity, tns, bns, lew, rew, xyb)
        if c5.validate() != ['OK'] or code_distance(c5) != 5:
            continue
        l5, m5, _ = funnel(c5)
        hits.append((parity, tns, bns, lew, rew, xyb))
        print("  HIT parity=%d top=%s bot=%s left=%s right=%s bnd=%-5s "
              "| d3: %d->%d  d5: %d->%d"
              % (parity, tns, bns, lew, rew, xyb, l3, m3, l5, m5))
    print()
    print("total conventions reproducing 96/16 at both d : %d" % len(hits))


if __name__ == '__main__':
    main()
