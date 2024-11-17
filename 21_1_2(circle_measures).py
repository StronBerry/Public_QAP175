class Circle:
    def __init__(self, radius):
        # Устанавливаем начальный радиус через сеттер, чтобы применить проверку
        self.radius = radius

    @property
    def radius(self):
        """Геттер для радиуса."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Сеттер для радиуса с проверкой."""
        if value <= 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Геттер для площади круга."""
        return 3.14 * (self.radius ** 2)

    @property
    def diameter(self):
        """Геттер для диаметра круга."""
        return 2 * self.radius
# Создадим экземпляр класса Circle с радиусом 5
circle_1 = Circle(5)
print(f"Радиус круга: {circle_1.radius}")
print(f"Площадь круга: {circle_1.area}")
print(f"Диаметр круга: {circle_1.diameter}")

# Изменим радиус круга на 10
circle_1.radius = 10
print(f"Площадь круга после изменения радиуса: {circle_1.area}")
print(f"Диаметр круга после изменения радиуса: {circle_1.diameter}")

# Попробуем установить отрицательный радиус
try:
    circle_1.radius = -5
except ValueError as ve:
    print(ve)

# Создадим экземпляр класса Circle с радиусом 15 для другого проекта
circle_2 = Circle(15)
print(f"Радиус другого круга: {circle_2.radius}")
print(f"Площадь другого круга: {circle_2.area}")
print(f"Диаметр другого круга: {circle_2.diameter}")
