"""Minimum number of CNOT layers for ANY legal + measurement-consistent gross-code SEC
(no constraint on the within-check orders).  This is the depth question the paper's Eq. (3)
lower bound (8 = 6 CNOT layers + prep + measure) leaves open once (MC) is imposed."""
import sys, time
from realize2 import solve
from sched import check_legal, mc_violations
from cascade import REPS
from gross import NG
sig = [REPS[0]] * NG
for T in (6, 7, 8, 9):
    res, ncls, el = solve(sig, sig, T, use_mc=True, use_class=False)
    if res is None:
        print(f"any-order, T={T}: UNSAT ({ncls} clauses, {el:.1f}s)")
    else:
        tX, tZ = res
        print(f"any-order, T={T}: SAT ({ncls} clauses, {el:.1f}s) legal={check_legal(tX,tZ,T)} "
              f"MCviol={mc_violations(tX,tZ)[0]}")
        break
    sys.stdout.flush()
