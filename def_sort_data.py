def sort_data(**kwargs):
    # Сортируем данные по ключам и возвращаем в виде списка кортежей
    return sorted(kwargs.items())

# Пример использования:
print(sort_data(name='Alex', age=30, city='New York'))
# [('age', 30), ('city', 'New York'), ('name', 'Alex')]
