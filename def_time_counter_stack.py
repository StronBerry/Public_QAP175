# import time
# def timeit(func):
#     call_stack = []
#     def wrapper(*args, **kwargs):
#         call_stack.append(None)
#         if len(call_stack) == 1:  # Если это изначальный вызов
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             work_time = time.time() -- start_time
#             print(f'Функция {func.__name__} отработала за {work_time} секунд')
#         else:  # Если это рекурсивный вызов
#             result = func(*args, **kwargs)
#         call_stack.pop()
#         return result
#
#     return wrapper
#
# @timeit
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# factorial(155)
# # Функция factorial отработала за 0.00095367431640625 секунд