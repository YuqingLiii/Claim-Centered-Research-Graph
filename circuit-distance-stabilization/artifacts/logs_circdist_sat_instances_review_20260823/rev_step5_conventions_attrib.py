"""Step 5: two adversarial convention probes + the mechanism-exclusion reproduction.

Probe 1 (surface): what if D_{a,0} existed too (round-0 X record treated as absolute)?
  Adding detectors can only RAISE d_R.  If it raised d_2 from 3 to 4 the R_stab>1 effect would
  be an artefact of Def 2.7's omission.  (Def 2.7 omits it because m_{a,0} is genuinely random
  in the Z-memory; the probe is a hostile 'what if', not a proposed correction.)

Probe 2 (BB, dependent checks): Def 2.7 omits the round-0 REDUNDANCY parities
  xor_{a in T} m_{a,0} for T in leftker(H_X).  For the surface code leftker = 0, so nothing is
  omitted; for BB [[18,4,4]] leftker has dimension 2, so two real round-0 detectors are omitted
  in EVERY round.  Does including them change (d_infinity, R_stab) = (3,1)?

Probe 3: mechanism exclusions -- single-round and no-hook restricted exact minima, reproduced
  exhaustively (no solver) for d=5 class D.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rev_core as C
import rev_bb
import rev_step4_witness_and_attrib as S4

CLASSD = (("NW", "SW", "NE", "SE"), ("NW", "NE", "SW", "SE"))


class ExtraDet:
    """wrap an Instance, appending extra detector rows given as (list of (fam,i,r) record keys)."""
    def __init__(self, inst, sch, extra_records):
        self.ndet = inst.ndet + len(extra_records)
        self.R = inst.R; self.sector = inst.sector
        self.nobs = inst.nobs
        base = inst.columns
        # recompute: a column's extra bits = parity of the records it flips.  We need per-column
        # record-flip info, so rebuild from labels via forward replay (independent path).
        self.columns = []
        recmaps = []
        for k, keys in enumerate(extra_records):
            recmaps.append((k, set(keys)))
        cache = {}
        for (dm, om, lab) in base:
            key = lab
            if key not in cache:
                cache[key] = record_flips(sch, inst.R, inst.sector, lab)
            flips = cache[key]
            add = 0
            for k, keys in recmaps:
                if len(flips & keys) % 2:
                    add |= 1 << (inst.ndet + k)
            self.columns.append((dm | add, om, lab))

    def classes(self):
        seen = {}
        for dm, om, lab in self.columns:
            if dm == 0 and om == 0:
                continue
            if (dm, om) not in seen:
                seen[(dm, om)] = lab
        return seen


def record_flips(sch, R, sector, label):
    """set of (fam,i,r) records flipped by the single elementary fault `label`."""
    code = sch.code
    nq = sch.nq
    x = [0] * nq; z = [0] * nq
    out = set()
    ins = {}
    recflip = None
    if label[0] == "cnot":
        _, r0, t0, (c, tg), (pc, pt) = label
        ins[(r0, t0)] = ("cnot", c, tg, pc, pt)
    elif label[0] == "idle":
        _, r0, t0, q, p = label
        ins[(r0, t0)] = ("single", q, p)
    elif label[0] == "prep":
        _, r0, q, p = label
        ins[(r0, -1)] = ("single", q, p)
    else:
        _, r0, fam, i = label
        recflip = (fam, i, r0)
    for r in range(R):
        for q in range(code.n, nq):
            x[q] = 0; z[q] = 0
        ev = ins.get((r, -1))
        if ev:
            _, q, p = ev
            if p & 1: x[q] ^= 1
            if p & 2: z[q] ^= 1
        for t in range(sch.T):
            for (ctl, tgt, kind, ci) in sch.layers[t]:
                x[tgt] ^= x[ctl]; z[ctl] ^= z[tgt]
            ev = ins.get((r, t))
            if ev:
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
                out.add(("a", i, r))
        for i in range(sch.nb):
            if x[sch.anc_z(i)]:
                out.add(("b", i, r))
    if recflip:
        out ^= {recflip}
    return out


def probe1():
    print("=" * 78)
    print("PROBE 1 (surface d=5 class D): add the omitted D_{a,0} detector (hostile what-if)")
    print("=" * 78)
    code = C.rotated_surface(5)
    sch = C.uniform_schedule(code, *CLASSD)
    for R in (1, 2, 3):
        inst = C.Instance(sch, R, "Z")
        base, _ = C.min_weight_exhaustive(inst, 4)
        extra = [[("a", i, 0)] for i in range(sch.na)]
        ext = ExtraDet(inst, sch, extra)
        ext.R = R; ext.sector = "Z"
        w, _ = C.min_weight_exhaustive(ext, 4)
        print("    R=%d  d_R (Def 2.7) = %s   with D_{a,0} added = %s" % (R, base, w))


def probe2():
    print("\n" + "=" * 78)
    print("PROBE 2 (BB [[18,4,4]], DEPENDENT checks): add the omitted round-0 redundancy parities")
    print("=" * 78)
    code = rev_bb.build_code()
    sch = rev_bb.schedule_NI(code)
    hx = code.hx_rows()
    n = code.n
    # leftker(H_X): subsets T of X-checks with xor of rows = 0
    na = len(hx)
    lk = []
    for m in range(1, 1 << na):
        v = 0; mm = m; i = 0
        while mm:
            if mm & 1:
                v ^= hx[i]
            mm >>= 1; i += 1
        if v == 0:
            lk.append(m)
    print("    |leftker(H_X)| = %d (dim %d) -> Def 2.7 omits %d independent round-0 X-redundancy"
          " parities" % (len(lk) + 1, len(bin(len(lk) + 1)) - 3, len(bin(len(lk) + 1)) - 3))
    # take an independent generating set of leftker as subsets
    gens = []
    seen = set()
    for m in sorted(lk, key=lambda t: bin(t).count("1")):
        if all((m ^ g) not in seen for g in gens) or not gens:
            gens.append(m); seen.add(m)
        if len(gens) >= 2:
            break
    for R in (1, 2, 3, 4):
        inst = C.Instance(sch, R, "Z")
        base, _ = C.min_weight_exhaustive(inst, 3)
        extra = []
        for g in gens:
            extra.append([("a", i, 0) for i in range(na) if (g >> i) & 1])
        ext = ExtraDet(inst, sch, extra)
        ext.R = R; ext.sector = "Z"
        w, _ = C.min_weight_exhaustive(ext, 3)
        print("    R=%d  d_R (Def 2.7) = %s   with round-0 redundancy detectors added = %s"
              % (R, base, w))


def probe3():
    print("\n" + "=" * 78)
    print("PROBE 3: mechanism exclusions for d=5 class D, reproduced EXHAUSTIVELY (no solver)")
    print("=" * 78)
    code = C.rotated_surface(5)
    sch = C.uniform_schedule(code, *CLASSD)
    for R in (1, 2, 3):
        inst = C.Instance(sch, R, "Z")
        base, _ = C.min_weight_exhaustive(inst, 5)
        # per-column round-residual weight -> hook classification
        resw = {}
        for (dm, om, lab) in inst.columns:
            if (dm, om) not in resw:
                resw[(dm, om)] = S4.residual_of(sch, "Z", lab)[0]
        # single-round restriction
        srbest = None
        for r0 in range(R):
            sub = Restricted(inst, lambda lab, r0=r0: lab[1] == r0)
            w, _ = C.min_weight_exhaustive(sub, 5)
            if w is not None and (srbest is None or w < srbest):
                srbest = w
        # no-hook restriction: only faults whose one-round residual has weight <= 1
        sub = Restricted(inst, None, keep=lambda key: resw[key] <= 1)
        nh, _ = C.min_weight_exhaustive(sub, 5)
        # need-meas: at least one fault with zero residual is REQUIRED -> compute the min over
        # configurations that use no measurement-type fault; if that equals d_R, no exclusion.
        sub2 = Restricted(inst, None, keep=lambda key: resw[key] >= 1)
        nomeas, _ = C.min_weight_exhaustive(sub2, 5)
        f = lambda v: (">5" if v is None else v)
        print("    R=%d  d_R=%s | single-round=%s | no-hook=%s | no-measurement-fault=%s"
              % (R, base, f(srbest), f(nh), f(nomeas)))
        print("       every min witness spans >=2 rounds : %s"
              % (srbest is None or srbest > base))
        print("       every min witness uses a hook fault: %s" % (nh is None or nh > base))
        print("       NO min witness needs a measurement fault: %s"
              % (nomeas is not None and nomeas == base))


class Restricted:
    def __init__(self, inst, labfilter, keep=None):
        self.ndet = inst.ndet; self.nobs = inst.nobs
        self.columns = []
        for (dm, om, lab) in inst.columns:
            if labfilter is not None and not labfilter(lab):
                continue
            if keep is not None and not keep((dm, om)):
                continue
            self.columns.append((dm, om, lab))

    def classes(self):
        seen = {}
        for dm, om, lab in self.columns:
            if (dm, om) not in seen:
                seen[(dm, om)] = lab
        return seen


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "1"):
        probe1()
    if which in ("all", "2"):
        probe2()
    if which in ("all", "3"):
        probe3()
