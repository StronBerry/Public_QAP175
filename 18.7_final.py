import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:
    students_marks[student] = {}
    # цикл по предметам
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks


# выводим меню с командами
def print_menu():
    print('''
    Список команд:
    1. Добавить оценки ученика по предмету
    2. Вывести средний балл по всем предметам по каждому ученику
    3. Вывести все оценки по всем ученикам
    4. Удалить оценку, предмет или ученика
    5. Редактировать оценку, предмет или ученика
    6. Вывести оценки для конкретного ученика
    7. Вывести средний балл по каждому предмету для определенного ученика
    8. Вывести 3 лучших учеников
    9. Выход из программы
    ''')


# Вывод 3 лучших учеников по всем предметам
def best_students():
    average_scores = {}
    for student in students:
        total_sum = 0
        total_count = 0
        for class_ in classes:
            total_sum += sum(students_marks[student][class_])
            total_count += len(students_marks[student][class_])
        average_scores[student] = total_sum / total_count

    # Сортируем учеников по среднему баллу и выводим 3 лучших
    top_students = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Топ-3 учеников по среднему баллу:")
    for student, avg_score in top_students:
        print(f'{student}: {avg_score:.2f}')


# Вывод 3 лучших учеников по предмету
def best_students_by_subject():
    subject = input('Введите предмет: ')
    if subject not in classes:
        print('ОШИБКА: предмет не найден.')
        return

    average_scores = {}
    for student in students:
        total_sum = sum(students_marks[student][subject])
        total_count = len(students_marks[student][subject])
        average_scores[student] = total_sum / total_count

    # Сортируем учеников по среднему баллу и выводим 3 лучших по предмету
    top_students = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)[:3]
    print(f"Топ-3 учеников по предмету {subject}:")
    for student, avg_score in top_students:
        print(f'{student}: {avg_score:.2f}')


while True:
    print_menu()
    command = int(input('Введите команду: '))

    # Добавление оценки
    if command == 1:
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))

        # Если ученик и предмет существуют
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    # Вывод среднего балла
    elif command == 2:
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum / marks_count:.2f}')
            print()

    # Вывод всех оценок
    elif command == 3:
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    # Удаление данных
    elif command == 4:
        print('1. Удалить оценку')
        print('2. Удалить предмет')
        print('3. Удалить ученика')

        delete_command = int(input('Выберите действие: '))

        # Удаление оценки
        if delete_command == 1:
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            if student in students_marks and class_ in students_marks[student]:
                print(f'Оценки: {students_marks[student][class_]}')
                mark_to_remove = int(input('Введите оценку, которую хотите удалить: '))
                if mark_to_remove in students_marks[student][class_]:
                    students_marks[student][class_].remove(mark_to_remove)
                    print(f'Оценка {mark_to_remove} удалена.')
                else:
                    print('Оценка не найдена.')
            else:
                print('ОШИБКА: неверное имя ученика или название предмета')

        # Удаление предмета
        elif delete_command == 2:
            class_ = input('Введите название предмета для удаления: ')
            if class_ in classes:
                classes.remove(class_)
                for student in students_marks:
                    if class_ in students_marks[student]:
                        del students_marks[student][class_]
                print(f'Предмет {class_} удален.')
            else:
                print('ОШИБКА: предмет не найден')

        # Удаление ученика
        elif delete_command == 3:
            student = input('Введите имя ученика для удаления: ')
            if student in students_marks:
                students.remove(student)
                del students_marks[student]
                print(f'Ученик {student} удален.')
            else:
                print('ОШИБКА: ученик не найден')

    # Редактирование данных
    elif command == 5:
        print('1. Редактировать оценку')
        print('2. Редактировать предмет')
        print('3. Редактировать ученика')

        edit_command = int(input('Выберите действие: '))

        # Редактирование оценки
        if edit_command == 1:
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            if student in students_marks and class_ in students_marks[student]:
                print(f'Оценки: {students_marks[student][class_]}')
                old_mark = int(input('Введите старую оценку: '))
                if old_mark in students_marks[student][class_]:
                    new_mark = int(input('Введите новую оценку: '))
                    index = students_marks[student][class_].index(old_mark)
                    students_marks[student][class_][index] = new_mark
                    print(f'Оценка {old_mark} изменена на {new_mark}.')
                else:
                    print('Оценка не найдена.')
            else:
                print('ОШИБКА: неверное имя ученика или название предмета')

        # Редактирование предмета
        elif edit_command == 2:
            old_class = input('Введите название предмета для редактирования: ')
            if old_class in classes:
                new_class = input('Введите новое название предмета: ')
                classes[classes.index(old_class)] = new_class
                for student in students_marks:
                    if old_class in students_marks[student]:
                        students_marks[student][new_class] = students_marks[student].pop(old_class)
                print(f'Предмет {old_class} изменен на {new_class}.')
            else:
                print('ОШИБКА: предмет не найден')

        # Редактирование ученика
        elif edit_command == 3:
            old_student = input('Введите имя ученика для редактирования: ')
            if old_student in students_marks:
                new_student = input('Введите новое имя ученика: ')
                students[students.index(old_student)] = new_student
                students_marks[new_student] = students_marks.pop(old_student)
                print(f'Ученик {old_student} изменен на {new_student}.')
            else:
                print('ОШИБКА: ученик не найден')

    # Вывод информации по всем парам предмет-оценка для определенного ученика
    elif command == 6:
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Оценки ученика {student}:')
            for class_, marks in students_marks[student].items():
                print(f'{class_}: {marks}')
        else:
            print('ОШИБКА: ученик не найден')

    # Вывод среднего балла по каждому предмету для определенного ученика
    elif command == 7:
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Средний балл по предметам для ученика {student}:')
            for class_, marks in students_marks[student].items():
                average = sum(marks) / len(marks)
                print(f'{class_}: {average:.2f}')
        else:
            print('ОШИБКА: ученик не найден')

    # Вывод 3 лучших учеников по всем предметам и по каждому предмету
    elif command == 8:
        print('1. Лучшие ученики по всем предметам')
        print('2. Лучшие ученики по конкретному предмету')
        subcommand = int(input('Введите команду: '))

        if subcommand == 1:
            best_students()
        elif subcommand == 2:
            best_students_by_subject()

    # Выход из программы
    elif command == 9:
        print('Выход из программы')
        break
