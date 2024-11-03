import random
import time

def retry_on_failure(func):
    max_retries = 3
    def wrapper(*args, **kwargs):
        for _ in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Function {func.__name__} failed with error: {e}. Retrying...")
                time.sleep(1)  # В реальном кейсе нам чаще всего надо будет подождать нек-ое кол-во времени
        print(f"Function {func.__name__} failed after {max_retries} retries.")
    return wrapper

@retry_on_failure
def fragile_function(*args, **kwargs):
    if random.random() < 0.5:  # В 50% случаев функция будет "Ломаться"
        raise Exception("An error occurred")
    else:
        return "Success"

# Запускаем функцию
print(fragile_function())
print(fragile_function())
print(fragile_function())
print(fragile_function())
