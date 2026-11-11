#!/usr/bin/env python3
"""Deterministic independent checker for the round-54 instances certificates.

Run with Python's standard library only.  The checker reconstructs the three
codes and schedules instead of trusting inputs.json; reconstructs every retained
fault effect and all 10,296 full-Pauli assignments instead of trusting
fault_effects.json; derives each spacetime effect in two directions; exhaustively
checks all lighter signature subsets; and replays every upper witness through a
separate full-symplectic circuit simulator.  Four required negative controls must
all be rejected before success is printed.
"""
import copy
import hashlib
import json
import pathlib
import sys
from collections import defaultdict

HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import model as M

EXPECTED_SCOPE={
 "CIRCDIST.sat.instances claim":(422,"sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3","CERTIFIED*"),
 "finite-prefix-window-closure implication":(1310,"sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05","CERTIFIED*"),
 "CIRCDIST.sat.window claim":(1261,"sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4","PROVED"),
 "CIRCDIST.sat.transfer claim":(3663,"sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33","PROVED"),
 "CIRCDIST.sat root claim":(1357,"sha256:513496daac6fa18bf96d1f2b6cf8768929eb62e45e103df1123479aadeeb7572","CERTIFIED*")}
PREFIX={"surface_standard_d5":[5,5,5,5,5],"surface_classD_d5":[4,3,3,3,3],"BB_18_4_4_NI":[3,3,3,3]}
RESULT={"surface_standard_d5":{"d_infinity":5,"R_stab":1},"surface_classD_d5":{"d_infinity":3,"R_stab":2},"BB_18_4_4_NI":{"d_infinity":3,"R_stab":1}}
HOOKS={"surface_standard_d5":{"X":{"vertical":0,"horizontal":8,"other":0},"Z":{"vertical":8,"horizontal":0,"other":0}},"surface_classD_d5":{"X":{"vertical":8,"horizontal":0,"other":0},"Z":{"vertical":0,"horizontal":8,"other":0}}}
MECH_DEFS={
 "hook_generator":"projected one-round elementary generator with residual data component weight at least 2",
 "no_hook_configuration":"every selected projected generator has residual weight at most 1",
 "measurement_class_generator":"projected one-round elementary generator with zero residual data component E=0",
 "needs_measurement_configuration":"contains at least one measurement-class generator",
 "single_round_configuration":"all occupied locations have one common round index",
 "mixed_multi_round_configuration":"occupied locations use at least two distinct rounds"}

COUNTS=defaultdict(int)

def load(name):
    return json.loads((HERE/name).read_text(encoding="utf-8"))

def canonical_hash(text):
    frozen=text.replace("\r\n","\n").strip()
    return "sha256:"+hashlib.sha256(frozen.encode("utf-8")).hexdigest()

def check_scope(scope):
    assert scope["schema"]=="circdist.sat.instances.scope.v1"
    assert len(scope["records"])==len(EXPECTED_SCOPE)
    got={r["label"]:r for r in scope["records"]};assert set(got)==set(EXPECTED_SCOPE)
    for label,(chars,digest,level) in EXPECTED_SCOPE.items():
        r=got[label];t=r["text"].replace("\r\n","\n").strip()
        assert len(t)==r["characters"]==chars
        assert canonical_hash(t)==r["sha256"]==digest
        assert r["canonical_level"]==level
        COUNTS["scope_records"]+=1

def check_detector_metadata(inputs):
    assert inputs["fault_model"]=={
      "cost":"number of occupied named locations","cnot":"all 15 nonidentity two-qubit Paulis after each gate",
      "idle_and_post_preparation":"all 3 nonidentity one-qubit Paulis","record":"one classical flip",
      "boundaries":"ideal data initialization and ideal terminal readout","rounds":"verbatim, disjoint locations, no cross-round compression",
      "R_domain":"R >= 1","aggregation":"minimum over Z-memory and X-memory sectors"}
    assert inputs["detectors"]=={
      "upper_replay":"all Definition-2.7 full-family initial/consecutive/terminal differences and partial-family interior consecutive differences",
      "canonical":"Definition 3.5 Z space and section-8.1 mirror",
      "bridge":"value equality only; detector-set equality is not asserted"}

def expected_instance_map():
    return {iid:(code,sch,Rmax) for iid,code,sch,Rmax in M.make_instances()}

def check_inputs(inputs):
    assert inputs["schema"]=="circdist.sat.instances.exact_inputs.v1"
    check_detector_metadata(inputs)
    known=expected_instance_map();stored={x["id"]:x for x in inputs["instances"]}
    assert set(stored)==set(known) and len(inputs["instances"])==3
    contexts={}
    for iid,(code,sch,Rmax) in known.items():
        x=stored[iid]
        # This exact equality pins every check row, logical row, gate, layer,
        # ancilla/data label, schedule order, and BB polynomial/layout datum.
        assert x["code"]==code and x["schedule"]==sch and x["first_d_rounds"]==Rmax
        ca=M.validate_code(code);sa=M.validate_schedule(code,sch)
        assert x["expected_code_audit"]==ca and x["expected_schedule_audit"]==sa
        assert ca["k"]>=1 and sch["depth"]>=1 and not sa["mc_bad"]
        if iid.startswith("surface"):
            assert ca["n"]==25 and ca["rank_x"]==ca["rank_z"]==12 and ca["k"]==1 and ca["d_X"]==ca["d_Z"]==5
            assert sorted(ca["x_check_weights"])==sorted(ca["z_check_weights"])==[2]*4+[4]*8
            fam=M.schedule_family_audit(code,sch);hooks=M.hook_geometry(code,sch)
            assert fam==x["expected_family_audit"]=={"candidates":576,"legal":96,"legal_mc":16,"member_index":sch["origin"]["member_index"]}
            assert hooks==x["expected_hook_geometry"]==HOOKS[iid]
            assert sa["gates"]==80 and sa["per_layer"]==[20]*4
        else:
            assert ca["n"]==18 and ca["rank_x"]==ca["rank_z"]==7 and ca["k"]==4 and ca["d_X"]==ca["d_Z"]==4
            assert ca["x_check_weights"]==ca["z_check_weights"]==[6]*9
            assert ca["x_qubit_degrees"]==ca["z_qubit_degrees"]==[3]*18
            assert x["expected_family_audit"] is None and x["expected_hook_geometry"] is None
            assert sa["gates"]==108 and sa["per_layer"]==[9]*12
            assert {g["kind"] for g in sch["gates"] if g["t"]<6}=={"X"}
            assert {g["kind"] for g in sch["gates"] if g["t"]>=6}=={"Z"}
        assert x["expected_sector_prefixes"]=={"Z":PREFIX[iid],"X":PREFIX[iid]}
        assert x["expected_aggregate_prefix"]==PREFIX[iid] and x["expected_result"]==RESULT[iid]
        contexts[iid]={"code":code,"schedule":sch,"Rmax":Rmax}
        COUNTS["instances"]+=1;COUNTS["gates"]+=len(sch["gates"])
    return contexts

def check_effect_payload(payload,contexts):
    assert payload["schema"]=="circdist.sat.instances.fault_effects.v1"
    assert set(payload["instances"])==set(contexts)
    for iid,c in contexts.items():
      code,sch=c["code"],c["schedule"]
      for sector in ("Z","X"):
        fs=M.one_round_faults(code,sch,sector);full,logs,_=M.full_checks_and_logs(code,sector);m=len(full);k=len(logs)
        pub=[M.public_fault(f,sector,code["n"],m,k) for f in fs]
        cat=M.full_fault_projection_catalog(code,sch,sector,fs);cov=M.physical_alphabet_coverage(code,sch,sector)
        got=payload["instances"][iid][sector]
        assert got["coverage"]==cov
        assert got["projected_generators"]==pub and got["projected_generators_sha256"]==M.sha_obj(pub)
        assert got["full_fault_assignments"]==cat and got["full_fault_assignments_sha256"]==M.sha_obj(cat)
        assert len(pub)==cov["projected_generators"] and len(cat)==cov["full_nonidentity_assignments"]
        # The multiplicity identities prove the full 15/3 menus project onto
        # exactly pbits={0,1,2,3}/{0,1}; no Pauli assignment is silently lost.
        assert cov["two_qubit_projection_multiplicities"]=={"0":3,"1":4,"2":4,"3":4}
        assert cov["one_qubit_projection_multiplicities"]=={"0":1,"1":2}
        c.setdefault("faults",{})[sector]=fs
        COUNTS["projected_generators"]+=len(pub);COUNTS["full_fault_assignments"]+=len(cat)

def assignment_key(a,sector):
    if a["kind"]=="cnot":
        comp="X" if sector=="Z" else "Z"
        pb=(1 if a["pauli"][0]==comp else 0)|(2 if a["pauli"][1]==comp else 0)
        assert pb
        return ("cnot",a["t"],a["control"],a["target"],pb)
    if a["kind"] in ("idle","prep"):
        assert a["pauli"]==("X" if sector=="Z" else "Z")
        return (a["kind"],a["t"],a["qubit"],1)
    return ("record",a["family"],a["check"],1)

def check_witness(w,iid,sector,R,code,sch,fs):
    assert w["sector"]==sector and w["R"]==R and w["weight"]==len(w["assignments"])
    lookup={M.raw_fault_key(f):f for f in fs};selected=[]
    for a in w["assignments"]: selected.append(lookup[assignment_key(a,sector)])
    replay=M.replay_witness(code,sch,R,sector,w["assignments"])
    assert replay==w["expected_replay"] and M.sha_obj(replay)==w["replay_sha256"]
    assert replay["weight"]==w["weight"]==replay["distinct_locations"]
    assert replay["definition_2_7_silent"] and replay["canonical_silent"] and replay["sector_pure"] and replay["logical"]
    rounds=sorted(set(a["round"] for a in w["assignments"]));assert rounds
    props={"contains_hook_generator":any(f["hook"] for f in selected),
           "contains_measurement_class_generator":any(f["measurement"] for f in selected),
           "occupied_rounds":rounds,"round_count":len(rounds),"round_span":rounds[-1]-rounds[0]+1,
           "all_generators_no_hook":all(not f["hook"] for f in selected)}
    assert props==w["properties"]
    COUNTS["witness_replays"]+=1
    return props

def expected_opts(iid):
    return ((5,5,5) if iid=="surface_standard_d5" else ((None,4,5) if iid=="surface_classD_d5" else (3,3,4)))

def check_cell(cell,ctx):
    iid=cell["instance"];sector=cell["sector"];R=cell["R"];code=ctx["code"];sch=ctx["schedule"];fs=ctx["faults"][sector]
    assert cell["id"]==f"{iid}/{sector}/R{R}" and 1<=R<=ctx["Rmax"]
    full,logs,_=M.full_checks_and_logs(code,sector);m=len(full);k=len(logs);nd=(R+1)*m
    assert cell["detector_bits"]==nd and cell["logical_bits"]==k
    d=PREFIX[iid][R-1];assert cell["expected_distance"]==d
    cl=M.classes(fs,R,m,k);keys=sorted(cl)
    assert cell["effect_classes"]==len(keys) and cell["effect_classes_sha256"]==M.signature_digest(keys)
    backward=M.backward_map(code,sch,sector,R);pairs=[]
    for r in range(R):
      for f in fs:
        fw=M.signature(f,r,R,m,k);bw=backward[M.fkey(r,f)]
        assert fw==bw
        pairs.append([list(M.fkey(r,f)),str(bw)])
    pairs.sort(key=lambda x:json.dumps(x[0],separators=(",",":")))
    assert cell["forward_backward_pairs"]==len(pairs) and cell["backward_map_sha256"]==M.sha_obj(pairs)
    lower=[M.find_goal_stats(keys,w,nd) for w in range(1,d)]
    assert lower==cell["lower_exclusions"] and not any(x["logical_found"] for x in lower)
    mainprops=check_witness(cell["upper_witness"],iid,sector,R,code,sch,fs)
    assert cell["upper_witness"]["weight"]==d
    mech=cell["mechanisms"]
    # Single-round: union over every possible chosen round is exhausted by
    # checking the R exact signature menus separately.
    single_opt=5 if iid=="surface_standard_d5" else (4 if iid=="surface_classD_d5" else 3)
    assert mech["single_round"]["expected_optimum"]==single_opt
    single_rows=[]
    for rr in range(R):
      skeys=sorted(set(M.signature(f,rr,R,m,k) for f in fs)-{0})
      ex=[M.find_goal_stats(skeys,w,nd) for w in range(1,single_opt)]
      assert not any(x["logical_found"] for x in ex)
      single_rows.append({"round":rr,"effect_classes":len(skeys),"effect_classes_sha256":M.signature_digest(skeys),"lower_exclusions":ex})
      COUNTS["mechanism_subset_tests"]+=len(ex)
    assert single_rows==mech["single_round"]["per_round_lower_exclusions"]
    p=check_witness(mech["single_round"]["upper_witness"],iid,sector,R,code,sch,fs)
    assert mech["single_round"]["upper_witness"]["weight"]==single_opt and p["round_count"]==1
    # No-hook restriction.
    nhkeys=sorted(M.classes(fs,R,m,k,pred=lambda f:not f["hook"]))
    nhopt=5 if iid.startswith("surface") else 4
    assert mech["no_hook"]["expected_optimum"]==nhopt and mech["no_hook"]["effect_classes"]==len(nhkeys) and mech["no_hook"]["effect_classes_sha256"]==M.signature_digest(nhkeys)
    nhex=[M.find_goal_stats(nhkeys,w,nd) for w in range(1,nhopt)]
    assert nhex==mech["no_hook"]["lower_exclusions"] and not any(x["logical_found"] for x in nhex)
    p=check_witness(mech["no_hook"]["upper_witness"],iid,sector,R,code,sch,fs)
    assert mech["no_hook"]["upper_witness"]["weight"]==nhopt and p["all_generators_no_hook"]
    COUNTS["mechanism_subset_tests"]+=len(nhex)
    # Contains-measurement restriction.  Designating one flagged generator and
    # allowing all remaining signatures is a complete supermodel.
    flagged=[M.signature(f,r,R,m,k) for r in range(R) for f in fs if f["measurement"]]
    cap=5 if iid=="surface_standard_d5" else 3
    fg=M.flagged_goal_stats(keys,flagged,cap,nd)
    assert fg==mech["needs_measurement_class"]["lower_exclusion"] and not fg["logical_found"]
    if iid=="surface_standard_d5":
      assert "upper_witness" not in mech["needs_measurement_class"] and mech["needs_measurement_class"]["conclusion"]["strict_lower_bound"]==5
    else:
      assert mech["needs_measurement_class"]["exact_optimum"]==4
      p=check_witness(mech["needs_measurement_class"]["upper_witness"],iid,sector,R,code,sch,fs)
      assert mech["needs_measurement_class"]["upper_witness"]["weight"]==4 and p["contains_measurement_class_generator"]
    COUNTS["measurement_restriction_tests"]+=1
    # Mechanism consequences at the deliberately scoped witness reading.
    if iid=="surface_standard_d5":
      assert mainprops["round_count"]==1 and mainprops["all_generators_no_hook"]
    elif iid=="surface_classD_d5" and R==1:
      assert mainprops["round_count"]==1 and mainprops["contains_hook_generator"]
    elif iid=="surface_classD_d5":
      assert mainprops["round_count"]>=2 and mainprops["contains_hook_generator"]
    else:
      assert mainprops["round_count"]==1 and mainprops["contains_hook_generator"]
    COUNTS["lower_subset_tests"]+=len(lower);COUNTS["forward_backward_pairs"]+=len(pairs);COUNTS["cells"]+=1

def check_certificates(cert,contexts):
    assert cert["schema"]=="circdist.sat.instances.proof_certificates.v1" and cert["mechanism_definitions"]==MECH_DEFS
    cells={(x["instance"],x["sector"],x["R"]):x for x in cert["cells"]}
    expected={(iid,s,R) for iid,c in contexts.items() for s in ("Z","X") for R in range(1,c["Rmax"]+1)}
    assert set(cells)==expected and len(cert["cells"])==28
    for iid,c in contexts.items():
      sectors={}
      for sector in ("Z","X"):
        vals=[]
        for R in range(1,c["Rmax"]+1):
          check_cell(cells[(iid,sector,R)],c);vals.append(cells[(iid,sector,R)]["expected_distance"])
        assert vals==PREFIX[iid];sectors[sector]=vals
      aggregate=[min(a,b) for a,b in zip(sectors["Z"],sectors["X"])]
      assert aggregate==PREFIX[iid]
      # The exact PROVED window theorem fixes every R>=d to d_d.  Hence the
      # serialized first-d prefix determines both tail value and first stable R.
      dinf=aggregate[-1]
      rstab=next(r for r in range(1,len(aggregate)+1) if all(v==dinf for v in aggregate[r-1:]))
      derived={"sectors":sectors,"aggregate_prefix":aggregate,"result":{"d_infinity":dinf,"R_stab":rstab}}
      assert derived==cert["derived"][iid] and derived["result"]==RESULT[iid]
      COUNTS["aggregate_cells"]+=len(aggregate)
    return cells

def must_reject(name,fn):
    try: fn()
    except (AssertionError,KeyError,IndexError,ValueError,TypeError):
        COUNTS["negative_controls"]+=1;return
    raise AssertionError("negative control was accepted: "+name)

def negative_controls(inputs,effects,cells,contexts):
    # 1. Tamper a full-Pauli upper witness while retaining its claimed replay.
    c=copy.deepcopy(cells[("surface_standard_d5","Z",1)])
    a=c["upper_witness"]["assignments"][0]
    if a["kind"]=="cnot": a["pauli"]="ZI"
    elif a["kind"] in ("idle","prep"): a["pauli"]="Z"
    else: a["family"]="X"
    must_reject("tampered witness",lambda:check_witness(c["upper_witness"],c["instance"],c["sector"],c["R"],contexts[c["instance"]]["code"],contexts[c["instance"]]["schedule"],contexts[c["instance"]]["faults"][c["sector"]]))
    # 2. Drop one serialized projected effect; exact reconstruction must differ.
    e=copy.deepcopy(effects);e["instances"]["surface_standard_d5"]["Z"]["projected_generators"].pop()
    must_reject("dropped effect",lambda:check_effect_payload(e,copy.deepcopy({k:{kk:vv for kk,vv in v.items() if kk!="faults"} for k,v in contexts.items()})))
    # 3. Increase a claimed optimum while leaving its upper witness unchanged.
    c=copy.deepcopy(cells[("surface_classD_d5","Z",2)]);c["expected_distance"]+=1
    must_reject("altered optimum",lambda:check_cell(c,contexts[c["instance"]]))
    # 4. Substitute a detector split that drops the mandated boundary slices.
    i=copy.deepcopy(inputs);i["detectors"]["upper_replay"]="interior consecutive differences only (wrong split: initial and terminal slices dropped)"
    must_reject("wrong detector split",lambda:check_detector_metadata(i))

def main():
    scope=load("scope_claims.json");inputs=load("inputs.json");effects=load("fault_effects.json");cert=load("certificates.json")
    check_scope(scope);contexts=check_inputs(inputs);check_effect_payload(effects,contexts);cells=check_certificates(cert,contexts)
    negative_controls(inputs,effects,cells,contexts)
    print(f"PASS scope hashes: {COUNTS['scope_records']}/5")
    print(f"PASS exact code/schedule instances: {COUNTS['instances']}/3; serialized gates: {COUNTS['gates']}")
    print(f"PASS full physical assignments: {COUNTS['full_fault_assignments']}; retained projected generators: {COUNTS['projected_generators']}")
    print(f"PASS distance cells: {COUNTS['cells']}/28; lower exact-weight exclusions: {COUNTS['lower_subset_tests']}; forward/backward fault pairs: {COUNTS['forward_backward_pairs']}")
    print(f"PASS mechanism exclusions: subset tests {COUNTS['mechanism_subset_tests']}, measurement supermodel tests {COUNTS['measurement_restriction_tests']}; upper replays: {COUNTS['witness_replays']}")
    print(f"PASS aggregate first-d cells: {COUNTS['aggregate_cells']}/14; derived results: standard (5,1), class-D (3,2), BB-NI (3,1)")
    print(f"PASS negative controls: {COUNTS['negative_controls']}/4 (tampered witness, dropped effect, altered optimum, wrong detector split all rejected)")
    print("VERIFIER RESULT: PASS")

if __name__=="__main__": main()
