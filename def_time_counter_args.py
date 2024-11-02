
import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() -- start_time
        print(f'Функция {func.__name__} отработала за {work_time} секунд')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        return res
    return wrapper

@timeit
def prime_numbers(n):
    ...

for i in range(1, 10000, 2000):
    prime_numbers(i)

# Функция prime_numbers отработала за 0.0 секунд
# args: (1,)
# kwargs: {}
# Функция prime_numbers отработала за 0.001998424530029297 секунд
# args: (2001,)
# kwargs: {}
# Функция prime_numbers отработала за 0.00800180435180664 секунд
# args: (4001,)
# kwargs: {}
# Функция prime_numbers отработала за 0.015002727508544922 секунд
# args: (6001,)
# kwargs: {}
# Функция prime_numbers отработала за 0.029001951217651367 секунд
# args: (8001,)
# kwargs: {}