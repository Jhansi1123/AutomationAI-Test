import pytest

def run_tests():
    pytest_args = [
        "scripts/",
        "--html=reports/test_report.html",
        "--self-contained-html",
        "--log-file=logs/execution.log"
        print("Hello, This is First PR request !")
    ]
    pytest.main(pytest_args)

if __name__ == "__main__":
    run_tests()
