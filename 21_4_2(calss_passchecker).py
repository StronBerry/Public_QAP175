from typing import List

class PasswordChecker:
    def set_password_range(self, min_len: int, max_len: int):
        self.min_len = min_len
        self.max_len = max_len

    def check_passwords(self, passwords: List[str]) -> List[bool]:
        return [self.min_len <= len(password) <= self.max_len for password in passwords]

pc = PasswordChecker()
pc.set_password_range(6, 10)
print(pc.min_len, pc.max_len)  # 6 10
result = pc.check_passwords(['afaaffhkjllgg', 'affsbbaf', 'gafg', 'fajkfa'])
print(result) # [False, True, False, True]