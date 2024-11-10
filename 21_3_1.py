class Student:
    course = "Data Science"

# Создаем экземпляр класса
s1 = Student()

# Добавляем локальные атрибуты
s1.name = "Иван"
s1.surname = "Иванов"
s1.semester = 1

# Записываем локальные атрибуты экземпляра s1 в переменную result
result = s1.__dict__
print(result)
print(Student().course)