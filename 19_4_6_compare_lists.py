def compare_test_results(expected_results, actual_results):
    return [expected == actual for expected, actual in zip(expected_results, actual_results)]
print(compare_test_results([True, False, True], [True, False, True]))