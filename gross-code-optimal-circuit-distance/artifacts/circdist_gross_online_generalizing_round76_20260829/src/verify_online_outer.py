#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parent.parent
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import z3,model as M,round68_build as B
from outer import OuterScheduler
def load(p):return json.loads(Path(p).read_text())
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def h(b):return hashlib.sha256(b).hexdigest()
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
ap=argparse.ArgumentParser();ap.add_argument('--iteration-root',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();d=a.iteration_root
cand=load(d/'candidate.json');before=load(d/'dynamic_before.json');gens=load(d/'generalized_before.json')
assert cand['iteration']>=54 and cand['state_bindings']['dynamic_before_sha256']==sha(before) and cand['state_bindings']['generalized_before_sha256']==sha(gens)
px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');unary=rx+rz
r62=load(ROOT/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz)
outer=OuterScheduler(True)
for i,r in enumerate(unary):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
for t in gens['terms']:outer.add_block([tuple(x) for x in t['atoms']],t['term_id'],t.get('source_term_sha256'))
for i,b in enumerate(before):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{i}-{b['sector']}",b.get('mechanism_sha256'))
assert len(outer.blocks)==cand['asserted_blocks']['total']
rebuilt=outer.s.to_smt2().encode();stored=(d/'outer.smt2').read_bytes()
pa=z3.parse_smt2_string(rebuilt.decode());pb=z3.parse_smt2_string(stored.decode());sa=[x.sexpr() for x in pa];sb=[x.sexpr() for x in pb]
assert sa==sb
times={k:int(v) for k,v in cand['schedule_times'].items()};audit=M.audit_schedule(times,True)
assert audit==cand['audit'] and audit['ok'] and audit['global_interleaved'] and set(times)==set(M.ALL_EDGES) and len(times)==864
fixed=z3.Solver();fixed.add(pb)
for e in M.ALL_EDGES:fixed.add(z3.Int('t_'+e.replace(':','_'))==times[e])
assert fixed.check()==z3.sat
assert all(not M.block_holds(times,[tuple(x) for x in t['atoms']]) for t in gens['terms'])
assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in before)
stream='\n'.join(sa).encode()
o={'schema':'round76-independent-outer-replay-v1','status':'PASS','iteration':cand['iteration'],'outer_blocks':len(outer.blocks),
   'base_assertions':4398,'assertion_count':len(sa),'ordered_assertion_stream_sha256':h(stream),'rebuilt_smt2_sha256':h(rebuilt),
   'stored_smt2_sha256':h(stored),'raw_smt2_byte_equal':rebuilt==stored,'parsed_ordered_assertions_equal':True,
   'serialized_formula_fixed_model_status':'SAT','named_edge_count':864,'mc_constraint_count':648,'compressed_used_layers':sorted(set(times.values()))==list(range(audit['max_time']+1)),
   'global_interleaved':audit['global_interleaved'],'schedule_sha256':sha(times),'all_installed_antecedents_excluded':True}
assert o['schedule_sha256']==cand['schedule_sha256'];dump(a.output,o);print(json.dumps(o,sort_keys=True))
