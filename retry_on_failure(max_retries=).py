import random
import time

def retry_on_failure(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Function {func.__name__} failed with error: {e}. Retrying...")
                    time.sleep(1)
            print(f"Function {func.__name__} failed after {max_retries} retries.")
        return wrapper
    return decorator

@retry_on_failure(max_retries=8)
def fragile_function(*args, **kwargs):
    ...
    if random.random() < 0.7:
        raise Exception("An error occurred")
    else:
        return "Success"

# Запускаем функцию
print(fragile_function())