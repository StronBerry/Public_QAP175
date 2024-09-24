# Функция для тестирования
def square(n):
    return n ** 2

# Функция test_function
def test_function(func, arg, expected_result):
    result = func(arg)  # Выполняем переданную функцию с переданным аргументом
    return result == expected_result  # Сравниваем результат с ожидаемым

# Пример использования
print(test_function(square, 3, 9))  # True, так как 3^2 = 9
print(test_function(square, 4, 20))  # False, так как 4^2 != 20
