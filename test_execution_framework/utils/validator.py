def validate_result(expected, actual):
    if expected == actual:
        return True
    else:
        print(f"[Validator] ❌ Expected: {expected}, Got: {actual}")
        return False
