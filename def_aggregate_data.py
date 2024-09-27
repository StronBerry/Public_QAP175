def aggregate_data(*args, **kwargs):
    sum_numbers = 0
    count_strings = 0

    # Обрабатываем позиционные аргументы
    for arg in args:
        if isinstance(arg, (int, float)):  # Если это число, добавляем к сумме
            sum_numbers += arg
        elif isinstance(arg, str):  # Если это строка, увеличиваем счетчик строк
            count_strings += 1

    # Обрабатываем именованные аргументы
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Если значение — число, добавляем к сумме
            sum_numbers += value
        elif isinstance(value, str):  # Если значение — строка, увеличиваем счетчик строк
            count_strings += 1

    return sum_numbers, count_strings


# Пример использования:
print(aggregate_data(1, 2, 'test1111','test1', error_count=3, test_id='test2'))  # (6, 2)
