def fibonacci(n):
    a, b = 0, 1  # Начальные числа последовательности Фибоначчи
    for _ in range(n):
        yield a
        a, b = b, a + b  # Обновляем значения для следующего числа последовательности

# Пример использования
fibonacci_generator = fibonacci(27)
for number in fibonacci_generator:
    print(number)