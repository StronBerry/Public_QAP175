import random
from functools import wraps

def retry_if_result_is_none(times=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                result = func(*args, **kwargs)
                if result is not None:
                    return result
            return None  # Если ни один вызов не вернул значение, отличное от None
        return wrapper
    return decorator

# Пример использования декоратора
@retry_if_result_is_none(times=2)
def test_function():
    return random.choice([None, "Passed"])

# Тестирование
print(test_function())  # Попробует получить "Passed" за 2 попытки, иначе вернет None
