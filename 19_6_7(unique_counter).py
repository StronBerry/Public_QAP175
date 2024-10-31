def create_unique_checker():
    seen_values = set()  # Создаем множество для хранения уникальных значений

    def unique_checker(value):
        if value not in seen_values:  # Проверяем, встречалось ли значение
            seen_values.add(value)  # Если не встречалось, добавляем его в множество
            return True  # Возвращаем True
        return False  # Если встречалось, возвращаем False

    return unique_checker  # Возвращаем замыкание

# Пример работы
unique_checker = create_unique_checker()
print(unique_checker(5))   # True
print(unique_checker(5))   # False
print(unique_checker(10))  # True
