"""Step 2: independent exact d_R for rotated surface d=5.
Arms: class D (doubly hook-misaligned, the HEADLINE) and the standard schedule.
Method E: exhaustive meet-in-the-middle over distinct effect classes (no solver, no stim).
Method I: exact ILP (scipy/HiGHS) on my own spacetime matrix.
Every reported witness is re-audited by an independent forward replay (rev_core.audit_witness).
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rev_core as C

SCHEDS = {
    "classD": (("NW", "SW", "NE", "SE"), ("NW", "NE", "SW", "SE")),
    "standard": (("NW", "NE", "SW", "SE"), ("NW", "SW", "NE", "SE")),
}


def run(d, name, Rlist, wmax, do_ilp=True):
    code = C.rotated_surface(d)
    piX, piZ = SCHEDS[name]
    sch = C.uniform_schedule(code, piX, piZ)
    ok, info = C.mc_holds(sch)
    print("=== d=%d  %s  piX=%s piZ=%s  legal=%s (MC)=%s" %
          (d, name, ",".join(piX), ",".join(piZ), C.is_legal(sch), ok))
    out = {}
    for R in Rlist:
        for sector in ("Z", "X"):
            t0 = time.time()
            inst = C.Instance(sch, R, sector)
            ncls = C.count_classes(inst)
            w, wit = C.min_weight_exhaustive(inst, wmax)
            tag = "EXHAUSTIVE<=%d" % wmax
            if w is None:
                res_e = ">%d" % wmax
            else:
                res_e = str(w)
            line = ("  R=%d sector=%s  columns=%d classes=%d detectors=%d  E:%s"
                    % (R, sector, len(inst.columns), ncls, inst.ndet, res_e))
            if do_ilp:
                wi, witi = C.min_weight_ilp(inst)
                line += "  ILP:%s" % wi
                if w is not None and wi != w:
                    line += "   *** METHOD DISAGREEMENT ***"
                if wit is None and witi is not None:
                    wit = witi
                    w = wi
            line += "  [%.1fs]" % (time.time() - t0)
            print(line)
            if wit is not None:
                silent, obs, nloc, nflip = C.audit_witness(sch, R, sector, wit)
                print("     AUDIT weight=%d distinct_locations=%d detectors_all_silent=%s "
                      "observable=%s  -> undetectable=%s logical=%s"
                      % (w, nloc, silent, obs, silent, any(obs)))
                for lab in wit:
                    print("       ", lab)
            out[(R, sector)] = w
        if (R, "Z") in out and (R, "X") in out:
            zz, xx = out[(R, "Z")], out[(R, "X")]
            if zz is not None and xx is not None:
                print("  R=%d  d_R^Z=%s d_R^X=%s  min-over-sectors d_R=%s" % (R, zz, xx, min(zz, xx)))
    return out


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "classD"
    Rmax = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    wmax = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    ilp = (len(sys.argv) <= 4) or (sys.argv[4] != "noilp")
    run(5, which, list(range(1, Rmax + 1)), wmax, do_ilp=ilp)
