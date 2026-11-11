from pathlib import Path
p=Path('/private/tmp/circdist-round118-iter194-order144-work/check_sat_order144_orbit_controls_round118.py')
s=p.read_text()
def rep(old,new):
 global s
 n=s.count(old)
 assert n==1,(n,old[:80])
 s=s.replace(old,new)
rep('''This checker is deliberately independent of the quotient builder.  It checks every
DIMACS clause, links every primary time bit to the decoded schedule, recomputes all
613,440 lex-recurrence values, enumerates the complete 72-image schedule orbit, and
constructs corrupt/truncated controls without copying the million-literal model.''','''This checker is deliberately independent of the quotient builder. It checks every
DIMACS clause, links every primary time bit to the decoded schedule, recomputes all
1,235,520 lex-recurrence values, enumerates the complete 144-image translation/CSS
schedule orbit with stabilizers, and constructs corrupt/truncated controls.''')
rep('''def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)
''','''def neg(g):
    i, j = divmod(int(g), M)
    return ((-i) % L) * M + ((-j) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def dq(q):
    q = int(q)
    return G + neg(q) if q < G else neg(q - G)
''')
rep('''def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"
''','''def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def de(edge):
    kind, check, qubit = edge.split(":")
    assert kind in ("X", "Z")
    return f"{'Z' if kind == 'X' else 'X'}:{neg(int(check))}:{dq(int(qubit))}"


def ge(edge, epsilon, delta):
    return te(de(edge), delta) if epsilon else te(edge, delta)
''')
rep('''    deltas = [(i, j) for i in range(L) for j in range(M)]
    images = []
    for delta in deltas:
        translated = {te(edge, delta): value for edge, value in times.items()}
        images.append({"delta": delta, "times": translated,
                       "vector": schedule_vector(translated, edges),
                       "sha256": canonical_sha(translated)})
    base_vector = schedule_vector(times, edges)
    least_vector = min(row["vector"] for row in images)
    assert base_vector == least_vector
    stabilizer = [row for row in images if row["vector"] == base_vector]
    distinct_images = {row["vector"] for row in images}
    assert len(distinct_images) * len(stabilizer) == len(deltas)
    ordered_distinct = sorted(distinct_images)
''','''    deltas = [(i, j) for i in range(L) for j in range(M)]
    elements = [(epsilon, delta) for epsilon in (0, 1) for delta in deltas]
    nonidentity = [(epsilon, delta) for epsilon, delta in elements
                   if not (epsilon == 0 and delta == (0, 0))]
    images = []
    for epsilon, delta in elements:
        transformed = {ge(edge, epsilon, delta): value for edge, value in times.items()}
        mapping = {edge: ge(edge, epsilon, delta) for edge in edges}
        images.append({"epsilon": epsilon, "delta": delta, "times": transformed,
                       "vector": schedule_vector(transformed, edges),
                       "sha256": canonical_sha(transformed),
                       "edge_map_sha256": canonical_sha(mapping)})
    image_by_element = {(row["epsilon"], tuple(row["delta"])): row for row in images}
    assert len(image_by_element) == 144
    assert len({row["edge_map_sha256"] for row in images}) == 144
    base_vector = schedule_vector(times, edges)
    least_vector = min(row["vector"] for row in images)
    assert base_vector == least_vector
    stabilizer = [row for row in images if row["vector"] == base_vector]
    distinct_images = {row["vector"] for row in images}
    assert len(distinct_images) * len(stabilizer) == len(elements)
    ordered_distinct = sorted(distinct_images)
''')
rep('''    trace_rows = trace["rows"]
    assert len(trace_rows) == 71
    recurrence_checks = 0
    root_checks = 0
    strict_roots = 0
    for row in trace_rows:
        delta = tuple(row["delta"])
        pairs = []
        for edge in edges:
            mapped = te(edge, delta)
            left_bits = metadata["time_bit_variables"][edge]
            right_bits = metadata["time_bit_variables"][mapped]
            for bit in range(9, -1, -1):
                pairs.append((int(left_bits[bit]), int(right_bits[bit])))
        suffix = bool(values[int(metadata["constant_variable"])])
        current = int(row["first_variable"])
        for xvar, yvar in reversed(pairs):
            required = recurrence(bool(values[xvar]), bool(values[yvar]), suffix)
            assert bool(values[current]) == required
            suffix = required
            current += 1
            recurrence_checks += 1
        assert current - 1 == int(row["last_variable"])
        assert int(row["root_variable"]) == int(row["last_variable"])
        assert suffix and bool(values[int(row["root_variable"])])
        root_checks += 1
        if base_vector != schedule_vector(images[deltas.index(delta)]["times"], edges):
            strict_roots += 1
''','''    trace_rows = trace["rows"]
    assert len(trace_rows) == metadata["symmetry_nonidentity_roots"] == 143
    assert [(int(r["epsilon"]), tuple(r["delta"])) for r in trace_rows] == nonidentity
    recurrence_checks = 0
    root_checks = 0
    strict_roots = 0
    edge_map_hash_checks = 0
    for row in trace_rows:
        epsilon, delta = int(row["epsilon"]), tuple(row["delta"])
        image = image_by_element[(epsilon, delta)]
        assert row["edge_map_sha256"] == image["edge_map_sha256"]
        edge_map_hash_checks += 1
        pairs = []
        for edge in edges:
            mapped = ge(edge, epsilon, delta)
            left_bits = metadata["time_bit_variables"][edge]
            right_bits = metadata["time_bit_variables"][mapped]
            for bit in range(9, -1, -1):
                pairs.append((int(left_bits[bit]), int(right_bits[bit])))
        suffix = bool(values[int(metadata["constant_variable"])])
        current = int(row["first_variable"])
        for xvar, yvar in reversed(pairs):
            required = recurrence(bool(values[xvar]), bool(values[yvar]), suffix)
            assert bool(values[current]) == required
            suffix = required
            current += 1
            recurrence_checks += 1
        assert current - 1 == int(row["last_variable"])
        assert int(row["root_variable"]) == int(row["last_variable"])
        assert suffix and bool(values[int(row["root_variable"])])
        root_checks += 1
        if base_vector != image["vector"]:
            strict_roots += 1
''')
rep('''    comparisons = []
    for delta in deltas[1:]:
        image = {te(edge, delta): value for edge, value in second_times.items()}
        comparisons.append((delta, second_vector <= schedule_vector(image, edges)))
    failed_roots = [delta for delta, holds in comparisons if not holds]
    assert len(failed_roots) == 1
''','''    comparisons = []
    for epsilon, delta in nonidentity:
        image = {ge(edge, epsilon, delta): value for edge, value in second_times.items()}
        comparisons.append(((epsilon, delta), second_vector <= schedule_vector(image, edges)))
    failed_roots = [element for element, holds in comparisons if not holds]
    assert len(failed_roots) == len(stabilizer)
    assert all(holds for element, holds in comparisons if element not in failed_roots)
''')
rep('''        "schema": "circdist-gross-round102-sat-orbit-controls-v1",''','''        "schema": "circdist-gross-round118-order144-sat-orbit-controls-v1",''')
rep('''            "recurrence_values_checked": recurrence_checks,
            "root_values_checked": root_checks,
''','''            "recurrence_values_checked": recurrence_checks,
            "root_values_checked": root_checks,
            "edge_map_hashes_checked": edge_map_hash_checks,
            "base_prefix_variables": int(metadata["base_variables"]),
            "base_prefix_clauses": int(metadata["base_clauses"]),
''')
rep('''            "group_order": len(deltas),''','''            "group_order": len(elements),''')
rep('''            "stabilizer_deltas": [list(row["delta"]) for row in stabilizer],''','''            "stabilizer_elements": [{"epsilon": row["epsilon"], "delta": list(row["delta"])}
                                    for row in stabilizer],''')
rep('''                "sole_failed_root_delta": list(failed_roots[0]),
                "other_70_nonidentity_roots_hold": True,
''','''                "failed_root_elements": [{"epsilon": e, "delta": list(d)} for e, d in failed_roots],
                "failed_root_count_equals_stabilizer_size": True,
                "all_other_nonidentity_roots_hold": True,
''')
p.write_text(s)
print({'status':'PASS','bytes':p.stat().st_size,'sha256':__import__('hashlib').sha256(p.read_bytes()).hexdigest()})
