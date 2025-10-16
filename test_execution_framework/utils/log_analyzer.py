import re

def analyze_log(file_path="logs/execution.log"):
    errors, warnings = [], []
    with open(file_path, "r") as log_file:
        for line in log_file:
            if re.search(r"ERROR|FAILED", line):
                errors.append(line.strip())
            elif "WARNING" in line:
                warnings.append(line.strip())

    print("\n[Log Analyzer] 🔍 Execution Log Analysis")
    print("Errors Found:", len(errors))
    for e in errors:
        print("   ❌", e)
    print("Warnings Found:", len(warnings))
    for w in warnings:
        print("   ⚠️", w)

    return {"errors": errors, "warnings": warnings}
