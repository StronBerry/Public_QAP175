from functools import wraps

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function {func.__name__} raised an exception: {e}")
    return wrapper

# Пример использования декоратора
@handle_exceptions
def test_function():
    raise ValueError("Some value error")

# Тестирование
test_function()
