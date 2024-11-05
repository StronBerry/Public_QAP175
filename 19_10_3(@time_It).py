import time
from typing import Callable

def time_it(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало измерения времени
        result = func(*args, **kwargs)  # Выполнение декорируемой функции
        end_time = time.time()  # Конец измерения времени
        execution_time = int(end_time - start_time)  # Округляем до секунд
        print(f"Execution time of '{func.__name__}': {execution_time} seconds")
        return result  # Возвращаем результат выполнения функции
    return wrapper


# Пример функции
def add_point(original_list: list, value):
    time.sleep(2)  # Задержка для демонстрации времени выполнения
    new_list = original_list[:]  # Создаем копию списка
    new_list.append(value)  # Добавляем элемент
    return new_list

# Применяем декоратор
@time_it
def add_point_with_timer(original_list: list, value):
    return add_point(original_list, value)

# Вызов функции
add_point_with_timer([1, 2, 3, 4, 5], 6)
# Примерный вывод: Execution time of 'add_point_with_timer': 2.000123 seconds
