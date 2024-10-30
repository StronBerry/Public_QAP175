def has_failures(test_res):
    return "fail" in test_res

def all_passed_or_skipped(test_res):
    return all(result in ["pass", "skip"] for result in test_res)

test_results = ["pass", "pass", "skip", "fail", "pass"]

print(has_failures(test_results))          # True
print(all_passed_or_skipped(test_results))  # False