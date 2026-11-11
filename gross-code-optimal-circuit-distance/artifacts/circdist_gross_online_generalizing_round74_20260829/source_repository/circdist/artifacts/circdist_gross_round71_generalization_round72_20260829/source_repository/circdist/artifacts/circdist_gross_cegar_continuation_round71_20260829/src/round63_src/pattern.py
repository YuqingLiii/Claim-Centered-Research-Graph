#!/usr/bin/env python3
"""Deterministic certificates for global single-residual order clauses.

This module is deliberately finite and transparent.  It enumerates all 6! local
orders.  It never treats the weight-12 pool as an absence oracle.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter

import model as M


PERMS = tuple(itertools.permutations(range(6)))


def canonical_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def holds(atoms, positions):
    return all(positions[M.edge_tuple(a)[2]] < positions[M.edge_tuple(b)[2]]
               for a, op, b in atoms)


def sector_single_certificates(label, checks, pool, edge_kind):
    clauses = []
    deletion_controls = []
    per_check = []
    for check, row in enumerate(checks):
        bad = {}
        for support in itertools.combinations(row, 3):
            sm = M.mask(support)
            witness_index = next((i for i, logical in enumerate(pool)
                                  if logical & sm == sm), None)
            if witness_index is not None:
                bad[sm] = witness_index
        assert len(bad) == 10

        orders = []
        for perm in PERMS:
            order = tuple(row[i] for i in perm)
            pos = {q: i for i, q in enumerate(order)}
            orders.append((order, pos, M.mask(order[3:]) in bad))

        check_clauses = []
        for sm, witness_index in sorted(bad.items()):
            suffix = set(M.bits(sm))
            other = set(row) - suffix
            exact = tuple(sorted((M.edge_key(edge_kind, check, q), '<',
                                  M.edge_key(edge_kind, check, r))
                                 for q in other for r in suffix))
            assert len(exact) == 9

            # Python integers are 720-bit truth tables.  A conjunction is sound
            # exactly when its intersection with the good-order mask is empty.
            atom_masks = []
            good_mask = 0
            for oi, (_, pos, is_bad) in enumerate(orders):
                if not is_bad:
                    good_mask |= 1 << oi
            for atom in exact:
                am = 0
                for oi, (_, pos, _) in enumerate(orders):
                    if holds((atom,), pos):
                        am |= 1 << oi
                atom_masks.append(am)
            universe = (1 << len(orders)) - 1
            chosen = None
            for size in range(10):
                for indices in itertools.combinations(range(9), size):
                    region = universe
                    for i in indices:
                        region &= atom_masks[i]
                    if region & good_mask == 0:
                        chosen = indices
                        break
                if chosen is not None:
                    break
            assert chosen is not None
            atoms = tuple(exact[i] for i in chosen)
            assert len(atoms) == 5

            # Every selected pool word has physical weight 12.  For an order in
            # the region, R(check, suffix3) plus singleton columns V xor suffix
            # has cost 1+9=10 and exactly reconstructs V.
            region_orders = []
            suffix_witnesses = {}
            for oi, (order, pos, _) in enumerate(orders):
                if holds(atoms, pos):
                    local_suffix = M.mask(order[3:])
                    assert local_suffix in bad
                    vi = bad[local_suffix]
                    logical = pool[vi]
                    singles = M.bits(logical ^ local_suffix)
                    assert M.popcount(logical) == 12 and len(singles) == 9
                    region_orders.append(oi)
                    suffix_witnesses[str(local_suffix)] = {
                        'pool_index': vi,
                        'singleton_columns': singles,
                    }

            controls = []
            for removed, atom in enumerate(atoms):
                trial = atoms[:removed] + atoms[removed + 1:]
                corrupt = next((oi for oi, (_, pos, is_bad) in enumerate(orders)
                                if (not is_bad) and holds(trial, pos)), None)
                assert corrupt is not None
                controls.append({'removed_atom': atom,
                                 'exposed_good_order': list(orders[corrupt][0])})
                deletion_controls.append({
                    'sector': label,
                    'check': check,
                    'support': M.bits(sm),
                    'removed_atom': atom,
                    'exposed_good_order': list(orders[corrupt][0]),
                })

            clause = {
                'sector': label,
                'check': check,
                'exact_suffix_support': M.bits(sm),
                'exact_atom_count': 9,
                'atoms': atoms,
                'atom_count': len(atoms),
                'region_order_count': len(region_orders),
                'region_orders_sha256': canonical_sha(region_orders),
                'suffix_witnesses': suffix_witnesses,
                'canonical_pool_index': witness_index,
                'deletion_controls': controls,
            }
            clauses.append(clause)
            check_clauses.append(clause)

        caught_bad = caught_good = total_bad = 0
        for order, pos, is_bad in orders:
            hit = any(holds(c['atoms'], pos) for c in check_clauses)
            total_bad += int(is_bad)
            caught_bad += int(is_bad and hit)
            caught_good += int((not is_bad) and hit)
        assert (total_bad, caught_bad, caught_good) == (360, 360, 0)
        per_check.append({'check': check, 'clauses': len(check_clauses),
                          'bad_orders': total_bad, 'bad_orders_caught': caught_bad,
                          'good_orders_caught': caught_good})

    public_clauses = [{k: c[k] for k in ('sector', 'check', 'exact_suffix_support',
                                         'atoms', 'region_order_count',
                                         'region_orders_sha256', 'suffix_witnesses')}
                      for c in clauses]
    return {
        'sector': label,
        'checks': len(checks),
        'raw_exact_suffix_patterns': len(clauses),
        'generalized_clauses': len(clauses),
        'atom_histogram': dict(Counter(str(c['atom_count']) for c in clauses)),
        'local_orders_per_check': len(PERMS),
        'order_cases_checked': len(checks) * len(PERMS),
        'bad_orders_per_check': 360,
        'good_orders_per_check': 360,
        'all_bad_orders_caught': all(x['bad_orders_caught'] == 360 for x in per_check),
        'no_good_order_caught': all(x['good_orders_caught'] == 0 for x in per_check),
        'atom_deletion_controls': len(deletion_controls),
        'clauses_sha256': canonical_sha(public_clauses),
        'deletion_controls_sha256': canonical_sha(deletion_controls),
    }


def build_global_single_summary(pool_x, pool_z):
    sectors = [
        sector_single_certificates('Xerr', M.Xchecks, pool_x, 'X'),
        sector_single_certificates('Zerr', M.Zchecks, pool_z, 'Z'),
    ]
    return {
        'schema': 'circdist-gross-global-single-order-clauses-v1',
        'semantics': ('Each listed antecedent is a conjunction of strict within-check edge '
                      'comparisons. Every local order satisfying it has a suffix-three '
                      'support completable with nine singleton columns to a frozen '
                      'weight-12 logical, so its negation is a sound W<=10 outer block.'),
        'complete_for': 'single residual plus weight-12 pool completion only',
        'not_complete_for': 'direct-360 effective absence',
        'sectors': sectors,
        'totals': {
            'raw_exact_suffix_patterns': sum(s['raw_exact_suffix_patterns'] for s in sectors),
            'generalized_clauses': sum(s['generalized_clauses'] for s in sectors),
            'order_cases_checked': sum(s['order_cases_checked'] for s in sectors),
            'atom_deletion_controls': sum(s['atom_deletion_controls'] for s in sectors),
        },
    }
