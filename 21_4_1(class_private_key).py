class User:
    def set_private_key(self, key: str):
        self.private_key = key

    def show_private_key(self):
        print(f"Приватный ключ пользователя: {self.private_key}")

user1 = User()
user1.set_private_key('uox00b_12x')
user1.show_private_key() # Приватный ключ пользователя: uox00b_12x
