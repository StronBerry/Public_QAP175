import random


def create_password_generator(length, symbols):
    def password_generator():
        return ''.join(random.choice(symbols) for _ in range(length))

    return password_generator


# Пример работы
symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password_generator = create_password_generator(10, symbols_for_password)
print(password_generator())  # Генерирует уникальный пароль
print(password_generator())  # Генерирует еще один уникальный пароль
