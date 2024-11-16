class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> bool:
        return (
            self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a
        )

    def get_triangle_area(self) -> float:
        if not self.is_triangle():
            return 0
        # Формула Герона
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())  # Вывод: True
print(t1.get_triangle_area())  # Вывод: 6.0

t2 = Triangle(a=10, b=5, c=5)
print(t2.is_triangle())  # Вывод: False
print(t2.get_triangle_area())  # Вывод: 0
