def create_counter():
    count = 0  # Инициализация счетчика

    def counter():
        nonlocal count  # Используем nonlocal для доступа к переменной count
        count += 1  # Увеличиваем счетчик
        return count  # Возвращаем текущее значение счетчика

    return counter  # Возвращаем замыкание-счетчик

# Пример работы
counter = create_counter()
print(counter())  # вернет "1"
print(counter())  # вернет "2"
print(counter())  # вернет "3"
counter2 = create_counter()
print(counter2())  # вернет "1"
print(counter2())  # вернет "2"

