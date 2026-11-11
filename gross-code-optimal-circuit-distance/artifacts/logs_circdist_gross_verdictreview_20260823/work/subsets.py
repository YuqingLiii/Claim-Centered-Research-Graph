"""How large must R be before d_ext(R) drops below 11?  The headline witness uses the residuals of
Z-checks 3, 9 and 15, so these are the informative subsets."""
import sys
from sched import make_phi
from cert import tiled_orders
from single import single_ctx
import dext
phi = make_phi(1, 2)
orders, _ = tiled_orders('Z', phi, (2, 2, 9))
for keep in ({3, 9}, {9, 15}, {3, 15}, {3, 9, 15}):
    ctx, Hstab = single_ctx(orders, 'Z', keep)
    sat, wit, el, ncls = dext.query(ctx, 10, Hstab)
    print('R = residuals of checks', sorted(keep), 'W=10:',
          ('SAT ' + str(wit[3])) if sat else 'UNSAT', '(%.1fs)' % el)
    sys.stdout.flush()
