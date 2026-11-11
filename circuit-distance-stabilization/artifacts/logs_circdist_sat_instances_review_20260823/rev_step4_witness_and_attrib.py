"""Step 4:
 (A) audit the witnesses PRINTED IN THE ARTIFACT (transcribed by hand from the .md, treated as
     data) against my own independently built circuit + forward replay;
 (B) the (C1) aggregation witness: member [0] (class B) must have d_R^Z = 5, d_R^X = 3 at d=5;
 (C) mechanism attribution: restricted exact minima (single-round / no-hook / need-meas);
 (D) alternative-convention recompute of the headline cell.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rev_core as C
import rev_cap

CLASSD = (("NW", "SW", "NE", "SE"), ("NW", "NE", "SW", "SE"))
CLASSB = (("NW", "NE", "SW", "SE"), ("NW", "NE", "SW", "SE"))     # member [0] of step-1 listing


def gate_exists(sch, t, c, tg):
    return any((cc == c and tt == tg) for (cc, tt, k, i) in sch.layers[t])


# ---------------------------------------------------------------- (A)
def audit_printed():
    print("=" *78)
    print("(A) AUDIT OF THE WITNESSES PRINTED IN artifacts/circdist_sat_instances_20260823.md")
    print("=" * 78)
    # --- headline witness, sec 4.4, rotated surface d=5 class D, Z-sector, R=2, weight 3
    code = C.rotated_surface(5)
    sch = C.uniform_schedule(code, *CLASSD)
    wit = [("cnot", 0, 1, (27, 5), (1, 0)),      # round 0, layer 1, X on control (hook)
           ("cnot", 1, 1, (33, 21), (1, 0)),     # round 1, layer 1, X on control (hook)
           ("cnot", 1, 0, (11, 44), (1, 1))]     # round 1, layer 0, X on control and target
    print("\n[A1] sec 4.4 headline witness (d=5 class D, Z, R=2):")
    ok = True
    for (_, r, t, (c, tg), p) in wit:
        e = gate_exists(sch, t, c, tg)
        print("     gate (%d,%d) present in layer %d of MY schedule: %s" % (c, tg, t, e))
        ok &= e
    if ok:
        silent, obs, nloc, nfl = C.audit_witness(sch, 2, "Z", wit)
        print("     REPLAY: distinct locations=%d  all detectors silent=%s  observable=%s"
              "  -> undetectable=%s logical=%s" % (nloc, silent, obs, silent, any(obs)))
        print("     VERDICT: %s" % ("CONFIRMED weight-3 undetectable logical"
                                    if (silent and any(obs) and nloc == 3) else "*** FAILS ***"))
    # --- BB witness, sec 5.3, R=1, weight 3, observable pattern (0,1,1,0)
    import rev_bb
    bcode = rev_bb.build_code()
    bsch = rev_bb.schedule_NI(bcode)
    bwit = [("cnot", 0, 3, (21, 12), (1, 0)),
            ("cnot", 0, 0, (18, 0), (1, 0)),
            ("cnot", 0, 3, (20, 11), (0, 1))]
    print("\n[A2] sec 5.3 BB [[18,4,4]] witness (Z, R=1, claimed pattern (0,1,1,0)):")
    ok = True
    for (_, r, t, (c, tg), p) in bwit:
        e = gate_exists(bsch, t, c, tg)
        print("     gate (%d,%d) present in layer %d of MY schedule: %s" % (c, tg, t, e))
        ok &= e
    if ok:
        silent, obs, nloc, nfl = C.audit_witness(bsch, 1, "Z", bwit)
        print("     REPLAY: distinct locations=%d  silent=%s  observable pattern=%s"
              % (nloc, silent, obs))
        print("     NOTE: the observable PATTERN depends on the choice of logical representatives,"
              " which the artifact fixes in bb_full.log; only 'some lambda flipped' is convention-free.")
        print("     VERDICT: %s" % ("CONFIRMED weight-3 undetectable logical"
                                    if (silent and any(obs) and nloc == 3) else "*** FAILS ***"))


# ---------------------------------------------------------------- (B)
def aggregation_witness():
    print("\n" + "=" * 78)
    print("(B) (C1) AGGREGATION WITNESS: class B (member [0]) must separate the sectors at d=5")
    print("=" * 78)
    code = C.rotated_surface(5)
    sch = C.uniform_schedule(code, *CLASSB)
    print("    piX=%s piZ=%s legal=%s (MC)=%s" % (",".join(CLASSB[0]), ",".join(CLASSB[1]),
                                                  C.is_legal(sch), C.mc_holds(sch)[0]))
    for R in (1, 2, 3, 4, 5, 6, 7):
        vals = {}
        for sector in ("Z", "X"):
            inst = C.Instance(sch, R, sector)
            w, _ = C.min_weight_exhaustive(inst, 4)
            if w is None:
                st, w2, _ = rev_cap.feasible_at_most(inst, 4)
                w = ">4" if st == "INFEASIBLE" else w2
            vals[sector] = w
        print("    R=%d  d_R^Z=%s  d_R^X=%s   (per-sector reading would give %s ; "
              "min-over-sectors gives %s)" % (R, vals["Z"], vals["X"], vals["Z"], vals["X"]))


# ---------------------------------------------------------------- (C)
def residual_of(sch, sector, label):
    """data-qubit residual (x-part for Z-memory, z-part for X-memory) at the END of the fault's
    own round, plus whether the fault flips any record of that round."""
    code = sch.code
    nq = sch.nq
    x = [0] * nq; z = [0] * nq
    if label[0] == "rec":
        return 0, 0, True
    if label[0] == "cnot":
        _, r, t0, (c, tg), (pc, pt) = label
        ins = {(t0,): [("cnot", c, tg, pc, pt)]}
    elif label[0] == "idle":
        _, r, t0, q, p = label
        ins = {(t0,): [("single", q, p)]}
    else:
        _, r, q, p = label
        t0 = -1
        ins = {(-1,): [("single", q, p)]}
    for ev in ins.get((-1,), []):
        _, q, p = ev
        if p & 1: x[q] ^= 1
        if p & 2: z[q] ^= 1
    recflip = 0
    for t in range(sch.T):
        for (ctl, tgt, kind, ci) in sch.layers[t]:
            x[tgt] ^= x[ctl]
            z[ctl] ^= z[tgt]
        for ev in ins.get((t,), []):
            if ev[0] == "cnot":
                _, c, tg, pc, pt = ev
                if pc & 1: x[c] ^= 1
                if pc & 2: z[c] ^= 1
                if pt & 1: x[tg] ^= 1
                if pt & 2: z[tg] ^= 1
            else:
                _, q, p = ev
                if p & 1: x[q] ^= 1
                if p & 2: z[q] ^= 1
    for i in range(sch.na):
        if z[sch.anc_x(i)]:
            recflip = 1
    for i in range(sch.nb):
        if x[sch.anc_z(i)]:
            recflip = 1
    res = sum(1 for q in range(code.n) if (x[q] if sector == "Z" else z[q]))
    return res, recflip, False


def attribution(d, sched, Rs, cap):
    print("\n" + "=" * 78)
    print("(C) MECHANISM ATTRIBUTION by restricted exact minima  (d=%d, cap=%d)" % (d, cap))
    print("=" * 78)
    code = C.rotated_surface(d)
    sch = C.uniform_schedule(code, *sched)
    for R in Rs:
        for sector in ("Z",):
            inst = C.Instance(sch, R, sector)
            resw = {}
            for (dm, om, lab) in inst.columns:
                if (dm, om) not in resw:
                    resw[(dm, om)] = residual_of(sch, sector, lab)
            base_st, base_w, _ = rev_cap.feasible_at_most(inst, cap)
            # single-round: all faults in one round
            sr = None
            for r0 in range(R):
                st, w, _ = rev_cap.feasible_at_most(
                    inst, cap, restrict=lambda it, r0=r0: label_round(it[1]) == r0)
                if st == "FEASIBLE" and (sr is None or w < sr):
                    sr = w
            # no-hook: only faults whose one-round residual has weight <= 1
            st, nh, _ = rev_cap.feasible_at_most(
                inst, cap, restrict=lambda it: resw[it[0]][0] <= 1)
            nh = nh if st == "FEASIBLE" else ">%d" % cap
            print("    R=%d %s  d_R=%s | single-round=%s | no-hook=%s"
                  % (R, sector, base_w, sr if sr is not None else ">%d" % cap, nh))
            print("       => every minimum witness spans >=2 rounds : %s"
                  % ((sr is None) or (sr > base_w)))
            print("       => every minimum witness uses a hook fault : %s"
                  % (isinstance(nh, str) or nh > base_w))


def label_round(lab):
    return lab[1]


# ---------------------------------------------------------------- (D)
def alt_convention():
    print("\n" + "=" * 78)
    print("(D) ALTERNATIVE-CONVENTION RECOMPUTE of the headline cell (d=5 class D)")
    print("=" * 78)
    code = C.rotated_surface(5)
    sch = C.uniform_schedule(code, *CLASSD)
    print("    layer occupancies (C2 idle-compression check):",
          [len(l) for l in sch.layers], "-> no globally idle layer:",
          all(len(l) > 0 for l in sch.layers))
    for R, wm in ((1, 5), (2, 4), (3, 4)):
        inst = C.Instance(sch, R, "Z")
        base, _ = C.min_weight_exhaustive(inst, wm)
        # ALT-1: drop the absolute round-0 detector D_{b,0} (unknown-initialisation reading)
        drop0 = [inst.det_id[("b", i, 0)] for i in range(inst.n_full)]
        mask = 0
        for k in drop0:
            mask |= 1 << k
        alt1 = MaskedInstance(inst, mask)
        w1, _ = C.min_weight_exhaustive(alt1, wm)
        # ALT-2: drop the terminal detector D_{b,R} (no terminal closure)
        dropR = [inst.det_id[("b", i, R)] for i in range(inst.n_full)]
        mask2 = 0
        for k in dropR:
            mask2 |= 1 << k
        alt2 = MaskedInstance(inst, mask2)
        w2, _ = C.min_weight_exhaustive(alt2, wm)
        # ALT-3: also include D_{a,0} (treating the round-0 X record as absolute)
        print("    R=%d  d_R (Def 2.7 as written) = %s | drop D_{b,0} -> %s | drop D_{b,R} -> %s"
              % (R, base, w1, w2))
        print("         (searches capped at weight %d; 'None' means > that cap)" % wm)


class MaskedInstance:
    def __init__(self, inst, dropmask):
        self.ndet = inst.ndet
        self.nobs = inst.nobs
        keep = ~dropmask
        self.columns = [(dm & keep, om, lab) for (dm, om, lab) in inst.columns]

    def classes(self):
        seen = {}
        for dm, om, lab in self.columns:
            if dm == 0 and om == 0:
                continue
            if (dm, om) not in seen:
                seen[(dm, om)] = lab
        return seen


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "A"):
        audit_printed()
    if what in ("all", "B"):
        aggregation_witness()
    if what in ("all", "D"):
        alt_convention()
    if what in ("all", "C"):
        attribution(5, CLASSD, [1, 2, 3], 5)
