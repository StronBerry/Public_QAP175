import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() -- start_time
        print(f'Функция {func.__name__} отработала за {work_time} секунд')
        return res
    return wrapper

@timeit
def large_sum(n):
    return sum(range(n))

@timeit
def prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n):
        isprime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isprime = False
        if isprime:
            primes.append(possiblePrime)
    return primes

test_data = 193700

prime_numbers = prime_numbers(test_data)
result = large_sum(test_data)

@timeit
def power_sum(n, p):
    """Функция возвращает сумму первых n чисел, возведенных в степень p."""
    return sum(i**p for i in range(n))

result = power_sum(10000, 2)
# Функция power_sum отработала за 0.002002239227294922 секунд
print(result)
# 333283335000