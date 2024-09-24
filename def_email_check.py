def is_valid_email(email):
    # Проверяем наличие символа "@"
    if "@" not in email:
        return False

    # Разбиваем email на две части: до "@" и после
    local_part, domain_part = email.split("@", 1)

    # Проверяем наличие точки в доменной части
    if "." not in domain_part:
        return False

    # Проверяем отсутствие пробелов
    if " " in email:
        return False

    # Если все условия выполнены, возвращаем True
    return True


# Примеры использования
print(is_valid_email("user@example.com"))  # True
print(is_valid_email("user at example dot com"))  # False
