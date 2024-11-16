class User:
    def __init__(self, email: str, password: str, balance: float):
        self.email = email        # Атрибут для хранения email
        self.password = password  # Атрибут для хранения пароля
        self.balance = balance    # Атрибут для хранения баланса

    def login(self, email: str, password: str) -> bool:
        # Проверка совпадения email и пароля
        return self.email == email and self.password == password

    def update_balance(self, amount: float):
        # Обновление баланса (увеличение или уменьшение)
        self.balance += amount
# Создаём пользователя с email, паролем и балансом
user = User("gosha@roskino.org", "qwerty", 20_000)

# Пытаемся выполнить логин с неверным паролем
print(user.login("gosha@roskino.org", "qwerty123"))
# Вывод: False

# Пытаемся выполнить логин с правильным паролем
print(user.login("gosha@roskino.org", "qwerty"))
# Вывод: True

# Обновляем баланс
user.update_balance(200)  # Добавляем 200 к текущему балансу
user.update_balance(-500) # Вычитаем 500 из текущего баланса

# Выводим текущий баланс
print(user.balance)
# Вывод: 19700
