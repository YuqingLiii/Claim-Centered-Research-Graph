.PHONY: audit validate lean-se lean-ksum

audit:
	python3 tools/test_dag_contracts.py
	python3 tools/evidence_closure_check.py
	python3 tools/lean_dag_check.py --selftest

validate:
	python3 tools/proof_dag_check.py --problem all
	python3 tools/lean_dag_check.py --problem se
	python3 tools/lean_dag_check.py --problem ksum

validate-channel-additivity-violations:
	python3 tools/proof_dag_check.py --problem channel-additivity-violations

validate-werner-holevo-capacity-threshold:
	python3 tools/proof_dag_check.py --problem werner-holevo-capacity-threshold

validate-circuit-distance-stabilization:
	python3 tools/proof_dag_check.py --problem circuit-distance-stabilization

validate-circuit-versus-effective-distance:
	python3 tools/proof_dag_check.py --problem circuit-versus-effective-distance

validate-gross-code-optimal-circuit-distance:
	python3 tools/proof_dag_check.py --problem gross-code-optimal-circuit-distance

validate-distance-preserving-schedule-complexity:
	python3 tools/proof_dag_check.py --problem distance-preserving-schedule-complexity

validate-ksum:
	python3 tools/proof_dag_check.py --problem ksum

validate-se:
	python3 tools/proof_dag_check.py --problem se

validate-finite-dimensional-grothendieck-bounds:
	python3 tools/proof_dag_check.py --problem finite-dimensional-grothendieck-bounds

validate-group-orbit-bell-matrices:
	python3 tools/proof_dag_check.py --problem group-orbit-bell-matrices

lean-se:
	cd se/lean && lake build

lean-ksum:
	cd ksum/lean && lake build
