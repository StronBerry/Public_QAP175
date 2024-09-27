def check_data_format(**kwargs):
    for key, value in kwargs.items():
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            return False
    return True

# Пример использования:
print(check_data_format(uid=24891, age=30, height=180))       # True
print(check_data_format(uid=24191, age="30", height=156))     # False
