import random

def generate_test_data(n=5, min_value=1, max_value=10):
    return [random.randint(min_value, max_value) for _ in range(n)]

# Пример использования функции:
print(generate_test_data())  # Например, [6, 6, 5, 10, 10]
print(generate_test_data(n=3, min_value=-5, max_value=5))  # Например, [3, 4, 3]
