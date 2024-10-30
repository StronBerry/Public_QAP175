def filter_api_tests(test_cases):
    return list(filter(lambda test: test["type"] == "API", test_cases))
