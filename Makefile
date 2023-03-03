all_tests:
	pytest tests

unit_tests:
	pytest tests/unit

integration_tests:
	pytest tests/integration

tests_coverage:
	coverage run -m pytest

tests_coverage_report:
	coverage report

tests_coverage_html:
	coverage html

pursuit_profile:
	python3 -m run
