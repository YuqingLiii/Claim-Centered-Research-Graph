#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model as M
from outer import OuterScheduler

C1 = [19,14,10, 6,13,7, 11,8,3, 24,35,5, 18,30,16, 12,31,4,
      20,0,21, 9,2,17, 25,1,23, 28,27,32, 33,22,15, 29,34,26]
C2 = [16,10,14, 6,1,8, 13,9,5, 23,35,12, 17,32,11, 18,34,4,
      20,0,22, 7,2,15, 26,3,24, 30,25,27, 33,21,19, 29,31,28]
HUNT1 = [21,13,3,4,14,6,11,8,5,24,35,10,25,31,19,12,32,9,
         27,1,18,7,2,15,17,0,23,28,16,33,34,22,20,29,30,26]


def dump(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')


def sha_obj(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load_context(args):
    px = M.expand_pool(args.w12x, M.HX, M.HZ)
    pz = M.expand_pool(args.w12z, M.HZ, M.HX)
    lx = M.logical_basis(px, M.HX)
    lz = M.logical_basis(pz, M.HZ)
    assert M.rank([sum(((M.popcount(x & z) & 1) << j) for j,z in enumerate(lz)) for x in lx], 12) == 12
    return px, pz, lx, lz


def sectors(times, lx, lz):
    return {'Xerr': M.Sector('Xerr', times, lz),
            'Zerr': M.Sector('Zerr', times, lx)}


def control_schedule(name):
    if name == 'C1': return M.schedule_from_T(C1)
    if name == 'C2': return M.schedule_from_T(C2)
    if name == 'hunt1': return M.schedule_from_T(HUNT1)
    if name == 'published': return M.candidate_serial_schedule()
    raise ValueError(name)


def command_audit(args):
    px,pz,lx,lz = load_context(args)
    out = {'model': M.model_metadata(px,pz,lx,lz), 'schedules': {}}
    for name in ('published','hunt1','C1','C2'):
        t = control_schedule(name)
        a = M.audit_schedule(t)
        ss = sectors(t,lx,lz)
        out['schedules'][name] = {'audit': a,
          'columns': {k: {'count': len(s.columns),
                          'distinct_residual_supports': len(set(c.support for c in s.columns[144:])),
                          'orders_sha256': sha_obj(s.orders)} for k,s in ss.items()}}
    dump(args.output,out)


def command_effective(args):
    px,pz,lx,lz=load_context(args)
    t=control_schedule(args.schedule)
    sec=sectors(t,lx,lz)[args.sector]
    pool=px if args.sector=='Xerr' else pz
    pre = None
    if args.schedule=='C1' and args.sector=='Zerr' and args.W==10:
        w=M.c1_named_certificate(sec);w['raw_selected_indices']=w['selected']
        pre={'status':'SAT','method':'hunt3-C1-normalized-direct-360-certificate',
             'complete_for_absence':False,'witness':w}
    elif args.prefilter:
        pre=M.fast_w12_adversary(sec,pool)
    result=pre if pre and pre['status']=='SAT' else M.effective_adversary(sec,args.W,args.solver,args.conf_budget,args.proof)
    out={'schedule':args.schedule,'schedule_audit':M.audit_schedule(t),
         'prefilter':pre,'result':result}
    dump(args.output,out)


def command_repair(args):
    px,pz,lx,lz=load_context(args)
    t=control_schedule(args.schedule)
    sec=sectors(t,lx,lz)[args.sector]
    pool=px if args.sector=='Xerr' else pz
    pre=None
    if args.schedule=='C2':
        w=M.c2_repair_certificate(sec)
        pre={'status':'SAT','method':'hunt3-C2-explicit-same-round-certificate',
             'complete_for_absence':False,'witness':w}
    elif args.prefilter:
        pre=M.canonical_same_round_repair0(sec,pool,args.prefilter_limit)
    result=pre if pre and pre['status']=='SAT' else M.repair_adversary(sec,args.solver,args.conf_budget,10,args.proof)
    out={'schedule':args.schedule,'schedule_audit':M.audit_schedule(t),
         'prefilter':pre,'result':result}
    dump(args.output,out)


def command_outer(args):
    o=OuterScheduler(require_interleaved=not args.allow_noninterleaved)
    if args.fix:
        o.fix_schedule(control_schedule(args.fix))
    out=o.solve(args.timeout_ms)
    if out.get('compressed_schedule'):
        out['compressed_schedule_sha256']=sha_obj(out['compressed_schedule'])
    dump(args.output,out)


def command_cegar(args):
    px,pz,lx,lz=load_context(args)
    outer=OuterScheduler(require_interleaved=True)
    ledger=[]
    for it in range(args.iterations):
        step={'iteration':it}
        so=outer.solve(args.outer_timeout_ms)
        step['outer']={k:v for k,v in so.items() if k!='compressed_schedule'}
        if so['status']!='SAT':
            ledger.append(step); break
        times=so['compressed_schedule']
        step['schedule_sha256']=sha_obj(times)
        step['schedule']=times
        ss=sectors(times,lx,lz)
        blocked=False
        for lab in ('Xerr','Zerr'):
            pool=px if lab=='Xerr' else pz
            pre=M.fast_w12_adversary(ss[lab],pool)
            adv=pre if pre['status']=='SAT' else M.effective_adversary(ss[lab],10,args.solver,args.conf_budget,False)
            step.setdefault('effective',{})[lab]=adv
            if adv['status']=='SAT':
                wit=adv['witness']
                atoms=M.effective_block_atoms(ss[lab],wit)
                assert M.block_holds(times,atoms)
                trace={'type':'effective','sector':lab,'schedule_sha256':step['schedule_sha256'],
                       'witness':wit,'atoms':atoms}
                trace_sha=sha_obj(trace)
                outer.add_block(atoms,f"eff-{it}-{lab}",trace_sha)
                step['block']={'type':'effective','sector':lab,'atoms':atoms,
                               'atom_count':len(atoms),'trace_sha256':trace_sha,
                               'soundness_replay':True}
                blocked=True
                break
            if adv['status']!='UNSAT':
                step['stop_reason']=f"effective adversary {lab} did not decide"
                break
        if blocked:
            ledger.append(step); continue
        if step.get('stop_reason'):
            ledger.append(step); break
        # Reaching this point requires certified UNSAT in both <=10 adversaries.
        for lab in ('Xerr','Zerr'):
            pool=px if lab=='Xerr' else pz
            pre=M.canonical_same_round_repair0(ss[lab],pool,args.repair_prefilter_limit)
            rep=pre if pre['status']=='SAT' else M.repair_adversary(ss[lab],args.solver,args.repair_conf_budget,10,False)
            step.setdefault('repair',{})[lab]=rep
            if rep['status']=='SAT':
                wit=rep['witness']
                atoms=M.repair_block_atoms(ss[lab],wit)
                assert M.block_holds(times,atoms)
                trace={'type':'repair0','sector':lab,'schedule_sha256':step['schedule_sha256'],
                       'witness':wit,'atoms':atoms}
                trace_sha=sha_obj(trace)
                outer.add_block(atoms,f"repair-{it}-{lab}",trace_sha)
                step['block']={'type':'repair0','sector':lab,'atoms':atoms,
                               'atom_count':len(atoms),'trace_sha256':trace_sha,
                               'soundness_replay':True}
                blocked=True
                break
            if rep['status']!='UNSAT':
                step['stop_reason']=f"repair adversary {lab} did not decide"
                break
        ledger.append(step)
        if step.get('stop_reason') or not blocked:
            # no block means all three adversary negations in both sectors returned UNSAT.
            break
    out={'architecture':'exact-full-864-edge-outer/direct-360-effective/arbitrary-round-repair0',
         'iterations_requested':args.iterations,'iterations_completed':len(ledger),
         'solver':args.solver,'effective_conf_budget':args.conf_budget,
         'repair_conf_budget':args.repair_conf_budget,'ledger':ledger,
         'outer_blocks':outer.blocks}
    dump(args.output,out)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--w12x',required=True);p.add_argument('--w12z',required=True)
    sp=p.add_subparsers(dest='cmd',required=True)
    a=sp.add_parser('audit');a.add_argument('--output',required=True);a.set_defaults(fn=command_audit)
    a=sp.add_parser('effective');a.add_argument('--schedule',choices=['published','hunt1','C1','C2'],required=True);a.add_argument('--sector',choices=['Xerr','Zerr'],required=True);a.add_argument('-W',type=int,default=10);a.add_argument('--solver',default='cadical195');a.add_argument('--conf-budget',type=int);a.add_argument('--proof',action='store_true');a.add_argument('--prefilter',action='store_true');a.add_argument('--output',required=True);a.set_defaults(fn=command_effective)
    a=sp.add_parser('repair');a.add_argument('--schedule',choices=['published','hunt1','C1','C2'],required=True);a.add_argument('--sector',choices=['Xerr','Zerr'],required=True);a.add_argument('--solver',default='cadical195');a.add_argument('--conf-budget',type=int);a.add_argument('--proof',action='store_true');a.add_argument('--prefilter',action='store_true');a.add_argument('--prefilter-limit',type=int,default=1000);a.add_argument('--output',required=True);a.set_defaults(fn=command_repair)
    a=sp.add_parser('outer');a.add_argument('--fix',choices=['published','hunt1','C1','C2']);a.add_argument('--allow-noninterleaved',action='store_true');a.add_argument('--timeout-ms',type=int,default=30000);a.add_argument('--output',required=True);a.set_defaults(fn=command_outer)
    a=sp.add_parser('cegar');a.add_argument('--iterations',type=int,default=10);a.add_argument('--outer-timeout-ms',type=int,default=30000);a.add_argument('--solver',default='cadical195');a.add_argument('--conf-budget',type=int,default=100000);a.add_argument('--repair-conf-budget',type=int,default=200000);a.add_argument('--repair-prefilter-limit',type=int,default=1000);a.add_argument('--output',required=True);a.set_defaults(fn=command_cegar)
    args=p.parse_args();args.fn(args)
if __name__=='__main__':main()
