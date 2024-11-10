class Group:
    members = []  # атрибут класса, который является пустым списком

class Student:
    course = "Data Science"  # атрибут класса Student

# Создаем студентов
s1 = Student()
s1.name = "Иван"
s1.surname = "Иванов"
s1.semester = 1

s2 = Student()
s2.name = "Лев"
s2.surname = "Сергеев"
s2.semester = 1

# Добавляем студентов в список members класса Group
Group.members.append(s1)
Group.members.append(s2)

# Записываем значение атрибута members класса Group в переменную result
result = Group.members

# Вывод для проверки
print(result) # [<__main__.Student object at 0x103c397f0>, <__main__.Student object at 0x103c39820>]
print(s1.name, s1.surname, s1.semester) # Иван Иванов 1

result_0 = isinstance(result[0], Student)
print(result_0) # True

result_1 = isinstance(result[1], Student)
print(result_1) # True