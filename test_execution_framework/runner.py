import pytest

def run_tests():
    pytest_args = [
        "scripts/",
        "--html=reports/test_report.html",
        "--self-contained-html",
        "--log-file=logs/execution.log",
    ]
    pytest.main(pytest_args)

if __name__ == "__main__":
    run_tests()
