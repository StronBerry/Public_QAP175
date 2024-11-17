class Student:
    def __init__(self, fio, group):
        self.fio = fio  # ФИО студента
        self.group = group  # Группа студента
        self.lecture_marks = []  # Оценки за лекции
        self.hw_marks = []  # Оценки за домашние задания

    def __str__(self):
        return (f"Студент {self.fio}: оценки на лекциях: {self.lecture_marks}; "
                f"оценки за д/з: {self.hw_marks}")


class Mentor:
    def __init__(self, fio, subject):
        self.fio = fio  # ФИО преподавателя
        self.subject = subject  # Предмет преподавания

    def set_mark(self, student, mark):
        """Абстрактный метод для установки оценки"""
        raise NotImplementedError


class Lector(Mentor):
    def set_mark(self, student, mark):
        """Лектор ставит оценку за лекции"""
        if isinstance(student, Student):
            student.lecture_marks.append(mark)

    def __str__(self):
        return f"Лектор {self.fio}: предмет {self.subject}"


class Reviewer(Mentor):
    def set_mark(self, student, mark):
        """Эксперт ставит оценку за домашнюю работу"""
        if isinstance(student, Student):
            student.hw_marks.append(mark)

    def __str__(self):
        return f"Эксперт {self.fio}: предмет {self.subject}"

# Проверяем взаимодействие классов Lector, Reviewer и Student
lector = Lector("Gusenko D.", "Physics")
reviewer = Reviewer("Golovanod A.", "Management")
student = Student("Zyablikov D.E.", "M3o-118B")

lector.set_mark(student, 4)
reviewer.set_mark(student, 5)

print(lector)       # Лектор Gusenko D.: предмет Physics
print(reviewer)     # Эксперт Golovanod A.: предмет Management
print(student)      # Студент Zyablikov D.E.: оценки на лекциях: [4]; оценки за д/з: [5]

# Проверяем, что класс Mentor абстрактный
try:
    mentor = Mentor("Gusenko D.", "Physics")
    mentor.set_mark(student, 4)
except NotImplementedError as e:
    print("Ошибка")  # Ошибка
