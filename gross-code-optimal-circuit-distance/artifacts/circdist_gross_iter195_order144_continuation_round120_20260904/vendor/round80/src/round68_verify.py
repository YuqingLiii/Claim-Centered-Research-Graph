#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'round63_src'))
import model as M


def sha_obj(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def dump(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def load_context():
    px=M.expand_pool(HERE/'inputs/w12X.txt',M.HX,M.HZ)
    pz=M.expand_pool(HERE/'inputs/w12Z.txt',M.HZ,M.HX)
    lx=M.logical_basis(px,M.HX); lz=M.logical_basis(pz,M.HZ)
    return px,pz,lx,lz

def sectors(times,lx,lz):
    return {'Xerr':M.Sector('Xerr',times,lz),'Zerr':M.Sector('Zerr',times,lx)}

def parse_dimacs(path):
    nvars=nclauses=None; clauses=[]
    for line in Path(path).read_text().splitlines():
        s=line.strip()
        if not s or s.startswith('c'): continue
        if s.startswith('p '):
            _,fmt,nv,nc=s.split(); assert fmt=='cnf';nvars=int(nv);nclauses=int(nc);continue
        vals=[int(x) for x in s.split()]; assert vals[-1]==0 and 0 not in vals[:-1]
        clauses.append(vals[:-1])
    assert nvars is not None and len(clauses)==nclauses
    assert max(abs(x) for c in clauses for x in c)<=nvars
    return nvars,clauses

def parse_assignment(log):
    status=None; lits=[]
    for line in Path(log).read_text(errors='replace').splitlines():
        if line.startswith('s '): status=line[2:].strip()
        if line.startswith('v '): lits += [int(x) for x in line[2:].split() if int(x)!=0]
    assert status=='SATISFIABLE'
    assignment={abs(x):(x>0) for x in lits}
    assert len(assignment)==len(lits)
    return status,assignment

def check_clauses(clauses,a):
    failed=[]
    for i,c in enumerate(clauses,1):
        if not any((lit>0)==a.get(abs(lit),False) for lit in c): failed.append(i)
    return failed

def mechanism(sec,selected):
    replay=sec.verify_effective_selection(selected,10)
    assert replay['ok']
    canonical=0; physical=0; faults=[]
    for j in selected:
        c=sec.columns[j]
        canonical ^= c.support; physical ^= c.physical_support
        if c.kind=='data':
            q=int(c.name.split(':')[1])
            faults.append({'column_index':j,'column_name':c.name,'elementary_fault':'data_singleton',
                           'data_support':[q],'schedule_dependency':'none'})
        else:
            order=sec.orders[c.check]
            expected_rep=M.mask(order[p] for p in M.RES_POS[c.residual_kind])
            expected_phys=M.mask(order[p] for p in M.PHYS_POS[c.residual_kind])
            assert c.support==expected_rep and c.physical_support==expected_phys
            ordered_edges=[sec.hedge(c.check,q) for q in order]
            ordered_times=[sec.times[e] for e in ordered_edges]
            assert ordered_times==sorted(ordered_times) and len(set(ordered_times))==6
            faults.append({'column_index':j,'column_name':c.name,
              'elementary_fault':'ancilla_hook_suffix', 'check':c.check,
              'residual_kind':c.residual_kind,
              'canonical_representative_support':M.bits(c.support),
              'physical_suffix_positions_zero_based':list(M.PHYS_POS[c.residual_kind]),
              'physical_suffix_support':M.bits(c.physical_support),
              'within_check_order_qubits':order,
              'within_check_order_edges':ordered_edges,
              'within_check_times':ordered_times})
    assert canonical==sum((1<<q) for q in replay['net_support'])
    psyn=sec.syndrome_of(physical)
    pnon=not M.inspan(physical,sec.stabilizers)
    ppar=[M.popcount(physical & l)&1 for l in sec.logical_duals]
    cpar=[M.popcount(canonical & l)&1 for l in sec.logical_duals]
    assert psyn==0 and pnon and ppar==cpar
    atoms=M.effective_block_atoms(sec,{'selected':selected})
    assert M.block_holds(sec.times,atoms)
    return {'sector':sec.label,'fault_count':len(selected),'selected_indices':selected,
      'selected_names':[sec.columns[j].name for j in selected],
      'canonical_replay':replay,
      'physical_net_support':M.bits(physical),'physical_net_weight':M.popcount(physical),
      'physical_syndrome':M.bits(psyn),'physical_nontrivial':pnon,
      'physical_logical_parities':ppar,'canonical_physical_parities_equal':ppar==cpar,
      'faults':faults,
      'sound_outer_block':{'semantics':'negation of the conjunction of listed strict comparisons; every schedule retaining the conjunction retains this exact direct mechanism',
                           'atoms':atoms,'atom_count':len(atoms),
                           'antecedent_holds_on_source_candidate':True}}

def verify_one(root,label,sec):
    cnf=root/'direct360'/f'{label}.cnf'; log=root/'solver'/f'{label}.solver.log'
    vard=json.loads((root/'direct360'/f'{label}.variables.json').read_text())
    cold=json.loads((root/'direct360'/f'{label}.columns.json').read_text())
    summ=json.loads((root/'direct360'/f'{label}.summary.json').read_text())
    nvars,clauses=parse_dimacs(cnf); status,a=parse_assignment(log)
    assert nvars==vard['variable_count']==summ['variables'] and len(a)==nvars
    assert len(clauses)==summ['clauses']
    assert hashlib.sha256(cnf.read_bytes()).hexdigest()==summ['dimacs_sha256']
    assert [v['id'] for v in vard['variables']]==list(range(1,nvars+1))
    assert len(cold['columns'])==360
    failed=check_clauses(clauses,a); assert not failed
    selected=[j for j in range(360) if a[j+1]]
    mech=mechanism(sec,selected)
    # Independent clause dictionary byte-for-byte reconstruction.
    dict_rows=[json.loads(line) for line in (root/'direct360'/f'{label}.clauses.jsonl').read_text().splitlines()]
    assert len(dict_rows)==len(clauses)
    assert [r['id'] for r in dict_rows]==list(range(1,len(clauses)+1))
    assert [r['lits'] for r in dict_rows]==clauses
    # Assignment and raw-witness negative controls.
    assert selected
    flipped=dict(a); flipped[selected[0]+1]=False
    flip_failed=check_clauses(clauses,flipped)
    assert flip_failed
    removed=sec.verify_effective_selection(selected[1:],10)
    assert not removed['ok']
    return {'status':status,'assignment_variables':len(a),'all_dimacs_clauses_satisfied':True,
      'failed_clause_count':0,'formula_summary':summ,'mechanism':mech,
      'negative_controls':{
       'flip_first_selected_primary':{'variable':selected[0]+1,'failed_clause_count':len(flip_failed),
                                      'first_failed_clause':flip_failed[0]},
       'remove_first_fault':removed}}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',required=True);ap.add_argument('--output',required=True)
    args=ap.parse_args();root=Path(args.root)
    cand=json.loads((root/'candidate/candidate.json').read_text());times={k:int(v) for k,v in cand['schedule_times'].items()}
    px,pz,lx,lz=load_context();ss=sectors(times,lx,lz)
    assert sha_obj(times)==cand['schedule_sha256']
    assert M.audit_schedule(times,True)==cand['audit']
    out={'schema':'circdist-gross-direct360-sat-raw-replay-v1','candidate_sha256':cand['schedule_sha256'],
         'schedule_audit':M.audit_schedule(times,True),'sectors':{}}
    for label in ('Xerr','Zerr'):
        out['sectors'][label]=verify_one(root,label,ss[label])
    out['repair_gate']={'entered':False,'reason':'both direct-360 queries are SAT; the commission permits arbitrary-round repair only after independently checked UNSAT in both sectors'}
    out['verdict']='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED'
    dump(args.output,out)
    print(json.dumps({'candidate':out['candidate_sha256'],
      'Xerr':{'status':out['sectors']['Xerr']['status'],'weight':out['sectors']['Xerr']['mechanism']['fault_count']},
      'Zerr':{'status':out['sectors']['Zerr']['status'],'weight':out['sectors']['Zerr']['mechanism']['fault_count']},
      'repair_entered':False},sort_keys=True))
if __name__=='__main__':main()
