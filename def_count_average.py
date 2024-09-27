def calculate_average(*args):
    if len(args) == 0:
        return 0  # Возвращаем 0, если нет данных
    return sum(args) / len(args)  # Среднее значение без округления