# Создаём список дел
todo = []

# Считываем количество дел с консоли
n = int(input("Сколько у вас сегодня дел? "))

# Запрашиваем у пользователя дела и добавляем их в список
for i in range(n):
    todo.append(input(f"Введите дело №{i + 1}: "))

print("Список дел:")
for index, item in enumerate(todo):
    print(f'Дело {index + 1}: {item}')

print()

# Получаем номер дела для редактирования
index = int(input("Номер дела для редактирования: ")) - 1

# Узнаём новое описание дела
new_description = input(f"Новое описание дела №{index + 1}: ")

# Обновляем описание дела в списке
todo[index] = new_description

# Выводим обновлённый список дел
print("Обновлённый список дел:")
for index, item in enumerate(todo):
    print(f'Дело {index + 1}: {item}')

print()

# Удаляем дело по номеру
del todo[int(input("Введите номер дела для удаления: "))-1]

# Выводим список оставшихся дел
print("Оставшиеся дела:")
for index, item in enumerate(todo):
    print(f'Дело {index + 1}: {item}')