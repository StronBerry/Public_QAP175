import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало измерения времени
        result = func(*args, **kwargs)
        end_time = time.time()    # Конец измерения времени
        elapsed_time = int(end_time - start_time)  # Округляем до целого
        print(f"Function {func.__name__} took {elapsed_time} seconds to run")
        return result
    return wrapper

# Пример использования декоратора
@time_it
def test_function():
    time.sleep(2)

test_function()
