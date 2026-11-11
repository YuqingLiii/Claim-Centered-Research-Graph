# Round114 theorem notes

## Mandatory iteration-192 result
The reviewed 71-root translation quotient is SAT. The retained assignment covers all 2,488,851 variables exactly once and satisfies all 11,906,732 clauses. Exact decoding gives a legal 864-edge, 500-layer frozen-family schedule: no resource conflict, all 648 MC overlap constraints, global interleaving, no reviewed block hit, no selector hit, and all 71 lex roots. Corrupt, truncated, reversed-lex, and missing-root controls reject as recorded.

The unrestricted direct Xerr and Zerr formulas are also SAT at weight 10. Independent standard-library reconstruction checks every clause and all 720 columns. Both mechanisms have zero detector syndrome, nonzero logical action, and canonical plus physical nonstabilizer support. Thus this candidate does not close branch A; repair is forbidden.

## CSS-duality lemma
Write a check as `g=(i,j)` in `Z_12 x Z_6`. Define `D(g)=-g`; on data qubits, `D(q)=72+(-q)` for `q<72` and `D(72+q)=-q`; and on named edges, `X:c:q` maps to `Z:-c:D(q)` and conversely. A residual name `R:c:k` maps across sectors to `R:-c:k`, with order position `k` unchanged. Exhaustive concrete checks establish `D^2=1`, `D T_delta D=T_-delta`, 144 distinct edge permutations, exact X/Z incidence and MC-overlap exchange, and stabilizer/detector/logical-quotient preservation. Therefore D transports every reviewed sound block and exact selector exclusion to a sound exclusion.

The input registry lacks 297,252 block and 25,164 selector D-images. Authorization requires every newly retained mechanism to have a free 72-element translation orbit. The package therefore installs exactly the free portion: 4,124 block orbits (296,928 blocks) and 349 selector orbits (25,128 selectors). It explicitly inventories and does not install nine size-36 block orbits (324 blocks) and one size-36 selector orbit (36 selectors). Because of that boundary, no order-144 quotient invariance is claimed; the exact order-72 translation quotient is retained.

The two mandatory direct parents and their two CSS-duals form four pairwise-disjoint, collision-free, free translation orbits (288 selectors); every dual physical mechanism is replayed on its transported legal schedule. This sound global mechanism exceeds the reviewed Round112 eight-parent increment, so the fallback batch was not activated.

## Root logic
No root branch is closed. Branch A lacks both required absence results because Xerr and Zerr are SAT. Branch B lacks a universal proof over all legal frozen-family schedules because the fresh iter193 quotient is unstarted. `CIRCDIST.gross` and `gap-via-lift` remain CONJECTURED and `D*_Gross` remains in `{11,12}`.
