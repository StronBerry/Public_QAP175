class Model:
    def __init__(self):
        self.__name = None  # Приватный атрибут для хранения имени модели

    @property
    def name(self):
        """Геттер для имени модели."""
        return self.__name

    @name.setter
    def name(self, value):
        """Сеттер для имени модели."""
        if isinstance(value, str) and 3 <= len(value) <= 15:
            self.__name = value
        else:
            self.__name = None  # Устанавливается None, если значение некорректное

# Создаем экземпляр класса Model
m = Model()

# Проверяем начальное значение имени модели (должно быть None)
print(m.name)
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "AB"
print(m.name)
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "A" * 16
print(m.name)
# Выведет: None

# Устанавливаем корректное значение имени
m.name = "ValidModelName"
print(m.name)
# Выведет: ValidModelName
