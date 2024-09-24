def is_success_code(code):
    return 200 <= code <= 299

print(is_success_code(400))