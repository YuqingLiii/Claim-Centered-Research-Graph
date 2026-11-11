#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, itertools, json, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'round63_src'
sys.path.insert(0, str(SRC))
import model as M
import pattern as P
from outer import OuterScheduler


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def sha_obj(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def dump(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')


def load_context():
    px = M.expand_pool(HERE / 'inputs/w12X.txt', M.HX, M.HZ)
    pz = M.expand_pool(HERE / 'inputs/w12Z.txt', M.HZ, M.HX)
    lx = M.logical_basis(px, M.HX)
    lz = M.logical_basis(pz, M.HZ)
    pairing = [sum(((M.popcount(x & z) & 1) << j) for j, z in enumerate(lz)) for x in lx]
    assert M.rank(pairing, 12) == 12
    return px, pz, lx, lz


def sectors(times, lx, lz):
    return {'Xerr': M.Sector('Xerr', times, lz),
            'Zerr': M.Sector('Zerr', times, lx)}


def global_single_records(label, checks, pool, edge_kind):
    records = []
    deletion_controls = []
    per_check = []
    for check, row in enumerate(checks):
        bad = {}
        for support in itertools.combinations(row, 3):
            sm = M.mask(support)
            vi = next((i for i, logical in enumerate(pool) if logical & sm == sm), None)
            if vi is not None:
                bad[sm] = vi
        assert len(bad) == 10
        orders = []
        for perm in P.PERMS:
            order = tuple(row[i] for i in perm)
            pos = {q: i for i, q in enumerate(order)}
            orders.append((order, pos, M.mask(order[3:]) in bad))
        good_mask = 0
        for oi, (_, _, is_bad) in enumerate(orders):
            if not is_bad:
                good_mask |= 1 << oi
        check_records = []
        for sm, witness_index in sorted(bad.items()):
            suffix = set(M.bits(sm))
            other = set(row) - suffix
            exact = tuple(sorted((M.edge_key(edge_kind, check, q), '<',
                                  M.edge_key(edge_kind, check, r))
                                 for q in other for r in suffix))
            atom_masks = []
            for atom in exact:
                am = 0
                for oi, (_, pos, _) in enumerate(orders):
                    if P.holds((atom,), pos):
                        am |= 1 << oi
                atom_masks.append(am)
            universe = (1 << 720) - 1
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
            assert chosen is not None and len(chosen) == 5
            atoms = tuple(exact[i] for i in chosen)
            region_orders = []
            suffix_witnesses = {}
            for oi, (order, pos, _) in enumerate(orders):
                if P.holds(atoms, pos):
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
                trial = atoms[:removed] + atoms[removed+1:]
                corrupt = next((oi for oi, (_, pos, is_bad) in enumerate(orders)
                                if (not is_bad) and P.holds(trial, pos)), None)
                assert corrupt is not None
                ctrl = {'removed_atom': atom,
                        'exposed_good_order': list(orders[corrupt][0])}
                controls.append(ctrl)
                deletion_controls.append({'sector': label, 'check': check,
                    'support': M.bits(sm), **ctrl})
            rec = {
                'sector': label, 'check': check,
                'exact_suffix_support': M.bits(sm),
                'exact_atom_count': 9,
                'atoms': atoms,
                'atom_count': len(atoms),
                'region_order_count': len(region_orders),
                'region_orders_sha256': P.canonical_sha(region_orders),
                'suffix_witnesses': suffix_witnesses,
                'canonical_pool_index': witness_index,
                'deletion_controls': controls,
            }
            records.append(rec)
            check_records.append(rec)
        total_bad = caught_bad = caught_good = 0
        for order, pos, is_bad in orders:
            hit = any(P.holds(c['atoms'], pos) for c in check_records)
            total_bad += int(is_bad)
            caught_bad += int(is_bad and hit)
            caught_good += int((not is_bad) and hit)
        assert (total_bad, caught_bad, caught_good) == (360, 360, 0)
        per_check.append({'check': check, 'clauses': len(check_records),
                          'bad_orders': total_bad, 'bad_orders_caught': caught_bad,
                          'good_orders_caught': caught_good})
    public = [{k: c[k] for k in ('sector','check','exact_suffix_support','atoms',
                                  'region_order_count','region_orders_sha256','suffix_witnesses')}
              for c in records]
    summary = {
        'sector': label, 'checks': len(checks),
        'raw_exact_suffix_patterns': len(records),
        'generalized_clauses': len(records),
        'atom_histogram': {'5': len(records)},
        'local_orders_per_check': 720,
        'order_cases_checked': len(checks)*720,
        'bad_orders_per_check': 360,
        'good_orders_per_check': 360,
        'all_bad_orders_caught': all(x['bad_orders_caught'] == 360 for x in per_check),
        'no_good_order_caught': all(x['good_orders_caught'] == 0 for x in per_check),
        'atom_deletion_controls': len(deletion_controls),
        'clauses_sha256': P.canonical_sha(public),
        'deletion_controls_sha256': P.canonical_sha(deletion_controls),
    }
    return records, summary


def replay_round62_blocks(data, lx, lz):
    assert len(data['ledger']) == len(data['outer_blocks']) == 20
    reports = []
    prior = []
    exclusion_count = 0
    for i, (step, block) in enumerate(zip(data['ledger'], data['outer_blocks'])):
        assert step['iteration'] == i
        times = {k: int(v) for k, v in step['schedule'].items()}
        assert M.audit_schedule(times, True)['ok']
        assert sha_obj(times) == step['schedule_sha256']
        label = block['tag'].split('-')[-1]
        sec = sectors(times, lx, lz)[label]
        witness = step['effective'][label]['witness']
        replay = sec.verify_effective_selection(witness.get('raw_selected_indices', witness['selected']), 10)
        assert replay['ok']
        atoms = [tuple(x) for x in block['atoms']]
        assert atoms == [tuple(x) for x in step['block']['atoms']]
        assert atoms == M.effective_block_atoms(sec, witness)
        assert len(atoms) == block['atom_count']
        assert M.block_holds(times, atoms)
        for old in prior:
            assert not M.block_holds(times, old)
            exclusion_count += 1
        prior.append(atoms)
        reports.append({'iteration': i, 'schedule_sha256': step['schedule_sha256'],
                        'sector': label, 'witness': replay,
                        'block_tag': block['tag'], 'block_atom_count': len(atoms),
                        'source_block_holds': True,
                        'prior_blocks_excluded': i})
    assert exclusion_count == 190
    return reports


def order_bindings(times, kind, checks):
    rows = []
    for a, row in enumerate(checks):
        order = sorted(row, key=lambda q: times[M.edge_key(kind, a, q)])
        rows.append({'check': a,
                     'order_qubits_earliest_first': order,
                     'order_edges_earliest_first': [M.edge_key(kind,a,q) for q in order],
                     'times_earliest_first': [times[M.edge_key(kind,a,q)] for q in order]})
    return rows


def build_candidate(outdir):
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    px,pz,lx,lz = load_context()
    sealed = json.loads((HERE / 'global_single_clauses.json').read_text())
    regenerated = P.build_global_single_summary(px,pz)
    assert all(regenerated[k] == sealed[k] for k in regenerated)
    assert set(sealed) == set(regenerated) | {'replay_wall_seconds'}
    rx,sx = global_single_records('Xerr', M.Xchecks, px, 'X')
    rz,sz = global_single_records('Zerr', M.Zchecks, pz, 'Z')
    assert [sx,sz] == sealed['sectors']
    records = rx + rz
    dump(outdir / 'global_single_clause_certificates.json', {
        'schema': 'circdist-gross-global-single-order-clauses-v1-full-ledger',
        'sealed_summary_sha256': hashlib.sha256((HERE/'global_single_clauses.json').read_bytes()).hexdigest(),
        'records': records,
        'records_sha256': sha_obj(records),
        'sectors': [sx,sz],
    })
    r62 = json.loads((HERE / 'round62_cegar20.json').read_text())
    r62_replay = replay_round62_blocks(r62,lx,lz)
    dump(outdir / 'round62_blocks_replay.json', {'replayed': r62_replay,
        'blocks': r62['outer_blocks'], 'block_count': len(r62['outer_blocks']),
        'prior_exclusions': 190})
    outer = OuterScheduler(True)
    for i, rec in enumerate(records):
        outer.add_block([tuple(a) for a in rec['atoms']], f'round63-global-single-{i}')
    for block in r62['outer_blocks']:
        outer.add_block([tuple(a) for a in block['atoms']], 'round62-'+block['tag'], block['trace_sha256'])
    assert len(outer.blocks) == 1460
    smt2 = outer.s.to_smt2()
    (outdir / 'candidate_outer.smt2').write_text(smt2)
    solved = outer.solve(120000)
    if solved['status'] != 'SAT':
        dump(outdir / 'candidate_outer_result.json', solved)
        raise RuntimeError('outer did not return SAT: '+solved['status'])
    times = solved.pop('compressed_schedule')
    audit = M.audit_schedule(times, True)
    assert audit['ok'] and audit['global_interleaved']
    holds_static = [i for i,r in enumerate(records)
                    if M.block_holds(times, [tuple(a) for a in r['atoms']])]
    holds_r62 = [i for i,b in enumerate(r62['outer_blocks'])
                 if M.block_holds(times, [tuple(a) for a in b['atoms']])]
    assert not holds_static and not holds_r62
    ss = sectors(times,lx,lz)
    columns = {}
    for label, sec in ss.items():
        columns[label] = [{
            'index': c.index, 'dimacs_primary_var': c.index+1,
            'name': c.name, 'kind': c.kind, 'check': c.check,
            'residual_kind': c.residual_kind,
            'support': M.bits(c.support), 'support_mask_hex': hex(c.support),
            'physical_support': M.bits(c.physical_support),
            'physical_support_mask_hex': hex(c.physical_support),
            'syndrome': M.bits(c.syndrome), 'syndrome_mask_hex': hex(c.syndrome),
            'u_options': [{'bits':M.bits(u),'mask_hex':hex(u)} for u in c.u_options],
        } for c in sec.columns]
    result = {
      'schema':'circdist-gross-clause-saturated-candidate-v1',
      'outer_result': solved,
      'schedule_sha256': sha_obj(times),
      'schedule_times': times,
      'schedule_times_sorted': [{'edge':e,'time':times[e]} for e in sorted(times)],
      'audit': audit,
      'order_bindings': {'X':order_bindings(times,'X',M.Xchecks),
                         'Z':order_bindings(times,'Z',M.Zchecks)},
      'retained_clause_scope': {
        'round63_global_single_clauses': len(records),
        'round62_sound_blocks': len(r62['outer_blocks']),
        'total_blocks_asserted': len(outer.blocks),
        'violated_antecedents_round63': len(holds_static),
        'violated_antecedents_round62': len(holds_r62),
        'exploratory_round63_pair_pattern_clauses_used': 0,
      },
      'outer_smt2_sha256': hashlib.sha256(smt2.encode()).hexdigest(),
      'model_metadata': M.model_metadata(px,pz,lx,lz),
      'pool_bindings': {
        'Xerr_pool_count':len(px),'Zerr_pool_count':len(pz),
        'Xerr_pool_sha256':sha_obj(px),'Zerr_pool_sha256':sha_obj(pz),
        'X_logical_basis':[{'bits':M.bits(v),'mask_hex':hex(v)} for v in lx],
        'Z_logical_basis':[{'bits':M.bits(v),'mask_hex':hex(v)} for v in lz],
        'X_logical_basis_sha256':sha_obj(lx),'Z_logical_basis_sha256':sha_obj(lz),
      },
      'columns': columns,
    }
    dump(outdir / 'candidate.json', result)
    return result, (px,pz,lx,lz)


class Encoder:
    def __init__(self, sector, candidate_sha):
        self.sector=sector; self.candidate_sha=candidate_sha
        self.vars=[]; self.var_by_name={}; self.clauses=[]
    def var(self,name,role,context):
        if name in self.var_by_name:
            return self.var_by_name[name]
        vid=len(self.vars)+1
        self.var_by_name[name]=vid
        self.vars.append({'id':vid,'name':name,'role':role,'context':context})
        return vid
    def add(self,lits,rule,context):
        assert all(isinstance(x,int) and x != 0 for x in lits)
        self.clauses.append({'id':len(self.clauses)+1,'lits':list(lits),
                             'rule':rule,'context':context})
    def xor_link(self,a,b,y,context):
        self.add([-y,a,b],'xor2_equivalence',context)
        self.add([-y,-a,-b],'xor2_equivalence',context)
        self.add([y,-a,b],'xor2_equivalence',context)
        self.add([y,a,-b],'xor2_equivalence',context)
    def xor_value(self,lits,prefix,context):
        assert lits
        if len(lits)==1: return lits[0]
        acc=lits[0]
        for step,x in enumerate(lits[1:],1):
            y=self.var(f'{prefix}.xor_aux.{step}','xor_auxiliary',
                       {**context,'step':step,'left':acc,'right':x})
            self.xor_link(acc,x,y,{**context,'step':step,'output':y})
            acc=y
        return acc
    def xor_constraint(self,lits,parity,prefix,context):
        if not lits:
            if parity: self.add([],'empty_xor_contradiction',context)
            return
        acc=self.xor_value(lits,prefix,context)
        self.add([acc if parity else -acc],'xor_terminal_value',{**context,'parity':parity})
    def atmost(self,x,k):
        n=len(x); assert 0<k<n
        s={}
        for i in range(1,n+1):
            for j in range(1,k+1):
                s[i,j]=self.var(f'card.s.{i}.{j}','cardinality_auxiliary',
                                {'counter':'prefix_at_least','prefix_length':i,'threshold':j})
        # i=1 bases
        self.add([-s[1,1],x[0]],'card_base_equivalence',{'i':1,'j':1})
        self.add([s[1,1],-x[0]],'card_base_equivalence',{'i':1,'j':1})
        for j in range(2,k+1):
            self.add([-s[1,j]],'card_impossible_base',{'i':1,'j':j})
        for i in range(2,n+1):
            xi=x[i-1]
            # s(i,1) <-> s(i-1,1) OR xi
            y=s[i,1]; a=s[i-1,1]
            self.add([-y,a,xi],'card_or_equivalence',{'i':i,'j':1})
            self.add([-a,y],'card_or_equivalence',{'i':i,'j':1})
            self.add([-xi,y],'card_or_equivalence',{'i':i,'j':1})
            for j in range(2,k+1):
                # y <-> a OR (b AND xi)
                y=s[i,j]; a=s[i-1,j]; b=s[i-1,j-1]
                self.add([-y,a,b],'card_recurrence_equivalence',{'i':i,'j':j})
                self.add([-y,a,xi],'card_recurrence_equivalence',{'i':i,'j':j})
                self.add([-a,y],'card_recurrence_equivalence',{'i':i,'j':j})
                self.add([-b,-xi,y],'card_recurrence_equivalence',{'i':i,'j':j})
            self.add([-s[i-1,k],-xi],'card_atmost_overflow_forbidden',{'i':i,'bound':k})


def column_public(sec, c):
    return {'index':c.index,'primary_var':c.index+1,'name':c.name,'kind':c.kind,
            'check':c.check,'residual_kind':c.residual_kind,
            'support':M.bits(c.support),'support_mask_hex':hex(c.support),
            'physical_support':M.bits(c.physical_support),
            'syndrome':M.bits(c.syndrome),'syndrome_mask_hex':hex(c.syndrome),
            'u_options':[{'bits':M.bits(u),'mask_hex':hex(u)} for u in c.u_options]}


def build_direct_cnf(sec, outprefix, candidate_sha, W=10):
    outprefix=Path(outprefix); outprefix.parent.mkdir(parents=True, exist_ok=True)
    enc=Encoder(sec.label,candidate_sha)
    x=[]
    for c in sec.columns:
        x.append(enc.var(f'select[{c.index}]','direct_column_selection',
                         {'column_index':c.index,'column_name':c.name}))
    assert x == list(range(1,361))
    syndrome_rows=[]
    for b in range(M.G):
        lits=[x[c.index] for c in sec.columns if (c.syndrome>>b)&1]
        syndrome_rows.append({'row':b,'literals':lits,'column_indices':[v-1 for v in lits]})
        enc.xor_constraint(lits,0,f'syndrome[{b}]',
                           {'family':'detector_syndrome','row':b})
    logical_rows=[]; lvars=[]
    for r,logical in enumerate(sec.logical_duals):
        lits=[x[c.index] for c in sec.columns if M.popcount(c.support & logical)&1]
        lv=enc.var(f'logical_parity[{r}]','logical_parity_output',
                   {'logical_dual_index':r,'logical_dual_support':M.bits(logical)})
        acc=enc.xor_value(lits,f'logical[{r}]',
                          {'family':'logical_parity','logical_dual_index':r})
        enc.add([-lv,acc],'logical_output_equivalence',{'logical_dual_index':r})
        enc.add([lv,-acc],'logical_output_equivalence',{'logical_dual_index':r})
        lvars.append(lv)
        logical_rows.append({'row':r,'logical_dual_support':M.bits(logical),
                             'logical_dual_mask_hex':hex(logical),
                             'literals':lits,'column_indices':[v-1 for v in lits],
                             'output_var':lv})
    enc.add(lvars,'logical_nonzero_disjunction',{'logical_outputs':lvars})
    enc.atmost(x,W)
    nvars=len(enc.vars); nclauses=len(enc.clauses)
    dimacs_lines=[f'c CIRCDIST Gross direct-360 {sec.label} W<={W}',
                  f'c candidate_sha256 {candidate_sha}',
                  'c variables 1..360 select the exact columns listed in the companion column dictionary',
                  f'p cnf {nvars} {nclauses}']
    dimacs_lines += [' '.join(map(str,c['lits']))+' 0' for c in enc.clauses]
    dimacs='\n'.join(dimacs_lines)+'\n'
    outprefix.with_suffix('.cnf').write_text(dimacs)
    dump(outprefix.with_suffix('.variables.json'), {
        'schema':'circdist-gross-direct360-variable-dictionary-v1',
        'sector':sec.label,'candidate_sha256':candidate_sha,
        'variable_count':nvars,'variables':enc.vars})
    with outprefix.with_suffix('.clauses.jsonl').open('w') as f:
        for c in enc.clauses:
            f.write(json.dumps(c,sort_keys=True,separators=(',',':'))+'\n')
    dump(outprefix.with_suffix('.columns.json'), {
        'schema':'circdist-gross-direct360-column-dictionary-v1',
        'sector':sec.label,'candidate_sha256':candidate_sha,
        'column_count':360,'columns':[column_public(sec,c) for c in sec.columns],
        'detector_rows':[{'row':i,'support':M.bits(v),'mask_hex':hex(v)}
                         for i,v in enumerate(sec.detrows)],
        'stabilizer_rows':[{'row':i,'support':M.bits(v),'mask_hex':hex(v)}
                           for i,v in enumerate(sec.stabilizers)],
        'logical_duals':[{'row':i,'support':M.bits(v),'mask_hex':hex(v)}
                         for i,v in enumerate(sec.logical_duals)],
        'syndrome_equations':syndrome_rows,
        'logical_equations':logical_rows,
    })
    body=''.join(' '.join(map(str,c['lits']))+' 0\n' for c in enc.clauses)
    summary={'schema':'circdist-gross-direct360-formula-summary-v1',
             'sector':sec.label,'candidate_sha256':candidate_sha,'W':W,
             'variables':nvars,'clauses':nclauses,
             'primary_selection_variables':360,
             'logical_output_variables':12,
             'formula_body_sha256':hashlib.sha256(body.encode()).hexdigest(),
             'dimacs_sha256':hashlib.sha256(dimacs.encode()).hexdigest(),
             'families':{
               'syndrome_xor_rows':72,'logical_parity_rows':12,
               'logical_nonzero_disjunctions':1,
               'cardinality_constraint':'exact prefix-threshold recurrence encoding of sum(select)<=10'},
             'complete_query':True,
             'excluded_restrictions': ['no pool restriction','no residual-pattern restriction',
               'no check-count restriction','no within-check order family restriction']}
    dump(outprefix.with_suffix('.summary.json'),summary)
    return summary


def build_all(outdir):
    outdir=Path(outdir)
    candidate,ctx=build_candidate(outdir/'candidate')
    px,pz,lx,lz=ctx
    times=candidate['schedule_times']
    ss=sectors(times,lx,lz)
    summaries={}
    for label in ('Xerr','Zerr'):
        summaries[label]=build_direct_cnf(ss[label],outdir/'direct360'/label,
                                          candidate['schedule_sha256'],10)
    # Meaningful known-SAT direct-360 control: hunt3 C1 / Zerr.
    C1=[19,14,10,6,13,7,11,8,3,24,35,5,18,30,16,12,31,4,
        20,0,21,9,2,17,25,1,23,28,27,32,33,22,15,29,34,26]
    c1times=M.schedule_from_T(C1)
    assert M.audit_schedule(c1times,True)['ok']
    c1sec=sectors(c1times,lx,lz)['Zerr']
    c1sha=sha_obj(c1times)
    c1summary=build_direct_cnf(c1sec,outdir/'controls'/'C1_Zerr',c1sha,10)
    c1named=M.c1_named_certificate(c1sec)
    assert c1named['ok']
    dump(outdir/'controls'/'C1_Zerr_expected_witness.json',{
      'schedule_T':C1,'schedule_sha256':c1sha,'schedule_audit':M.audit_schedule(c1times,True),
      'known_direct_witness':c1named,'formula_summary':c1summary})
    dump(outdir/'build_summary.json',{'candidate':candidate['schedule_sha256'],
        'direct':summaries,'control_C1_Zerr':c1summary})


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True)
    args=ap.parse_args(); build_all(args.output)
if __name__=='__main__': main()
