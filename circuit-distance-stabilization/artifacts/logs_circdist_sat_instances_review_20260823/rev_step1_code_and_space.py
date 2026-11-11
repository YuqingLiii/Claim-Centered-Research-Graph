"""Step 1: independently rebuild the rotated surface code and the uniform schedule space.
Checks: H_X H_Z^T = 0, k, d_X, d_Z, |A|, |B|, and the 576 -> 96 legal -> 16 legal+(MC) counts.
Also identifies the standard and class-D members and their hook geometry."""
import itertools
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import rev_core as C


def code_report(d, exhaustive_distance=True):
    code = C.rotated_surface(d)
    hx = code.hx_rows()
    hz = code.hz_rows()
    # CSS commutation
    bad = 0
    for a in hx:
        for b in hz:
            if C.popcount(a & b) % 2:
                bad += 1
    rx = C.rank_f2(hx, code.n)
    rz = C.rank_f2(hz, code.n)
    k = code.n - rx - rz
    print("d=%d  n=%d  |A|=%d  |B|=%d  rank H_X=%d  rank H_Z=%d  k=%d  anticommuting pairs=%d"
          % (d, code.n, len(hx), len(hz), rx, rz, k, bad))
    # weight profile
    from collections import Counter
    print("   X-check weights:", dict(Counter(C.popcount(a) for a in hx)),
          " Z-check weights:", dict(Counter(C.popcount(b) for b in hz)))
    # logical validity
    XL, ZL = code.xlog[0], code.zlog[0]
    okx = all(C.popcount(XL & b) % 2 == 0 for b in hz)
    okz = all(C.popcount(ZL & a) % 2 == 0 for a in hx)
    print("   X_L commutes with all Z-checks: %s ; Z_L commutes with all X-checks: %s ; |X_L^Z_L|=%d (odd required)"
          % (okx, okz, C.popcount(XL & ZL)))
    if exhaustive_distance:
        kerHZ = C.kernel_basis(hz, code.n)      # v with H_Z v = 0  -> X-type logicals
        kerHX = C.kernel_basis(hx, code.n)
        dX = C.min_weight_coset(kerHZ, code.n, lambda v: C.popcount(v & ZL) % 2 == 1)
        dZ = C.min_weight_coset(kerHX, code.n, lambda v: C.popcount(v & XL) % 2 == 1)
        print("   d_X=%s  d_Z=%s  (exhaustive over the %d-dim kernels)" % (dX, dZ, len(kerHZ)))
    return code


def schedule_space(code, d):
    perms = list(itertools.permutations(C.CORNERS))
    legal = []
    legal_mc = []
    for piX in perms:
        for piZ in perms:
            sch = C.uniform_schedule(code, piX, piZ)
            if not C.is_legal(sch):
                continue
            legal.append((piX, piZ))
            ok, _ = C.mc_holds(sch)
            if ok:
                legal_mc.append((piX, piZ))
    print("d=%d : %d candidates -> %d legal -> %d legal AND (MC)"
          % (d, len(perms) ** 2, len(legal), len(legal_mc)))
    return legal_mc


def hook_geometry(code, piX, piZ, d):
    """residual of an ancilla fault after its 2nd CNOT = last two data qubits in that order.
    misaligned iff that pair is PARALLEL to the logical it can shortcut:
    X-hooks vertical (X_L is a column) ; Z-hooks horizontal (Z_L is a row)."""
    def orient(pairs):
        vert = horiz = 0
        for (q1, q2) in pairs:
            r1, c1 = divmod(q1, d)
            r2, c2 = divmod(q2, d)
            if c1 == c2:
                vert += 1
            elif r1 == r2:
                horiz += 1
        return vert, horiz
    xp, zp = [], []
    for supp, cs in code.xchecks:
        if len(cs) < 4:
            continue
        order = [cs[nm] for nm in piX]
        xp.append((order[2], order[3]))
    for supp, cs in code.zchecks:
        if len(cs) < 4:
            continue
        order = [cs[nm] for nm in piZ]
        zp.append((order[2], order[3]))
    xv, xh = orient(xp)
    zv, zh = orient(zp)
    xmis = (xv == len(xp) and len(xp) > 0)     # vertical X-hook parallel to vertical X_L
    zmis = (zh == len(zp) and len(zp) > 0)     # horizontal Z-hook parallel to horizontal Z_L
    return xmis, zmis, (xv, xh, zv, zh), len(xp)


if __name__ == "__main__":
    codes = {}
    for d in (3, 5):
        codes[d] = code_report(d)
    codes[7] = code_report(7, exhaustive_distance=False)
    print()
    for d in (3, 5, 7):
        lm = schedule_space(codes[d], d)
        if d == 5:
            print("  the 16 legal+(MC) members at d=5, with hook geometry:")
            for i, (piX, piZ) in enumerate(lm):
                xm, zm, counts, npairs = hook_geometry(codes[d], piX, piZ, d)
                cls = {(False, False): "A aligned/aligned", (False, True): "B X-al,Z-mis",
                       (True, False): "C X-mis,Z-al", (True, True): "D both misaligned"}[(xm, zm)]
                print("   [%2d] piX=%-16s piZ=%-16s  X-hooks(v,h)=%s Z-hooks(v,h)=%s  -> %s"
                      % (i, ",".join(piX), ",".join(piZ), counts[:2], counts[2:], cls))
    print()
    # the two schedules the artifact names
    for name, piX, piZ in (("STANDARD", ("NW", "NE", "SW", "SE"), ("NW", "SW", "NE", "SE")),
                           ("CLASS-D ", ("NW", "SW", "NE", "SE"), ("NW", "NE", "SW", "SE"))):
        for d in (3, 5, 7):
            sch = C.uniform_schedule(codes[d], piX, piZ)
            ok, info = C.mc_holds(sch)
            xm, zm, counts, npairs = hook_geometry(codes[d], piX, piZ, d)
            print("%s d=%d : legal=%s  (MC)=%s  bulk weight-4 X-checks=%d  X-hooks(v,h)=%s Z-hooks(v,h)=%s"
                  % (name, d, C.is_legal(sch), ok, npairs, counts[:2], counts[2:]))
