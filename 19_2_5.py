def is_palindrome(s):
    # Базовый случай: если длина строки 0 или 1, это палиндром
    if len(s) <= 1:
        return True
    # Если первый и последний символы не совпадают, это не палиндром
    elif s[0] != s[-1]:
        return False
    # Рекурсивный случай: проверка внутренней подстроки
    else:
        return is_palindrome(s[1:-1])

# Примеры работы функции
print(is_palindrome('racecar'))  # True
print(is_palindrome('gong'))     # False
