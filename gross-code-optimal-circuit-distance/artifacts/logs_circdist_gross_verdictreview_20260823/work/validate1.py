"""Validation V1 of the d_ext certifier: with the residual set switched OFF the problem reduces to
the gross code's own minimum logical weight, which is known exactly to be 12."""
import numpy as np, time
from gross import HX, HZ, NG, zcheck_nb, xcheck_nb
import dext, pool as poolmod

orders = [[q for q, s, i in zcheck_nb(g)] for g in range(NG)]     # arbitrary; unused when off
ctx, Hstab = dext.sector_ctx(orders, 'Z')
for W in (11, 12):
    sat, wit, el, ncls = dext.query(ctx, W, Hstab, use_residuals=False)
    print(f"[no residuals] W = {W}: {'SAT' if sat else 'UNSAT'}  ({el:.1f}s, {ncls} clauses)")
    if sat:
        print("   witness:", wit[3])

ctxX, HstabX = dext.sector_ctx([[q for q, s, i in xcheck_nb(g)] for g in range(NG)], 'X')
for W in (11, 12):
    sat, wit, el, ncls = dext.query(ctxX, W, HstabX, use_residuals=False)
    print(f"[no residuals, X sector] W = {W}: {'SAT' if sat else 'UNSAT'}  ({el:.1f}s)")
