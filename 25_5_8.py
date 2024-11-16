class IntDataFrame:
    def __init__(self, data):
        # Преобразуем все элементы в целые числа, отрезая дробную часть
        self.column = [int(x) for x in data]

    def count(self):
        # Возвращаем количество ненулевых элементов
        return sum(1 for x in self.column if x != 0)

    def unique(self):
        # Возвращаем количество уникальных элементов
        return len(set(self.column))
# Создаём объект класса IntDataFrame
df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

# Выводим результат
print(df.column)
# Вывод: [4, 4, 3, 0, 2, 0, 4]

# Подсчитываем количество ненулевых элементов
print(df.count())
# Вывод: 5

# Подсчитываем количество уникальных элементов
print(df.unique())
# Вывод: 4
