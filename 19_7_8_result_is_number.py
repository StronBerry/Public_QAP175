from functools import wraps

def ensure_result_is_number(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result
        else:
            return None
    return wrapper

# Пример использования декоратора
import random

@ensure_result_is_number
def test_function():
    return random.choice(["Passed", 10, "Failed", 5.5])

# Тестирование
print(test_function())  # Вернет None, если результат - не число
print(test_function())  # Вернет 5.5 или 10, если результат - число
