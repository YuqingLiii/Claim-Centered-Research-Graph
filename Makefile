.PHONY: audit validate validate-se validate-ksum lean-se lean-ksum

audit:
	python3 tools/test_dag_contracts.py
	python3 tools/evidence_closure_check.py
	python3 tools/lean_dag_check.py --selftest

validate: validate-se validate-ksum

validate-se:
	python3 tools/proof_dag_check.py --problem se
	python3 tools/lean_dag_check.py --problem se

validate-ksum:
	python3 tools/proof_dag_check.py --problem ksum
	python3 tools/lean_dag_check.py --problem ksum

lean-se:
	cd se/lean && lake build

lean-ksum:
	cd ksum/lean && lake build
