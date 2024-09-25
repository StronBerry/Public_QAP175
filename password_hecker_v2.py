def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
    # Проверяем длину пароля
    if len(password) < min_length:
        return False

    # Флаги для проверки условий
    has_upper = any(c.isupper() for c in password) if require_upper else True
    has_lower = any(c.islower() for c in password) if require_lower else True
    has_digit = any(c.isdigit() for c in password) if require_digit else True

    # Возвращаем результат проверки всех условий
    return has_upper and has_lower and has_digit

print(is_valid_password("Password123"))
# True
print(is_valid_password("password"))
# False
print(is_valid_password("Password123", min_length=12))
# False
