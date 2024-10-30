def filter_high_severity(bugs):
    return list(filter(lambda bug: bug["severity"] == "high", bugs))