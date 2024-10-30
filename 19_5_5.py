# Глобальные переменные для отслеживания количества тестов
tests_run = 0
tests_failed = 0


def test_case_generator():
    case_id = 0

    def run_test(test):
        global tests_run, tests_failed
        nonlocal case_id  # Указываем, что мы будем изменять переменную case_id из внешней области

        case_id += 1  # Увеличиваем уникальный идентификатор теста
        tests_run += 1  # Увеличиваем количество выполненных тестов

        if not test():  # Запускаем тест и проверяем его результат
            tests_failed += 1  # Увеличиваем количество проваленных тестов

        return case_id  # Возвращаем уникальный идентификатор теста

    return run_test

# Создаем генератор тестов
run_test_case = test_case_generator()

# Примеры тестовых функций
def test_pass():
    return True

def test_fail():
    return False

# Запуск тестов
print(run_test_case(test_pass))  # Уникальный ID теста, например, 1
print(run_test_case(test_fail))   # Уникальный ID теста, например, 2
print(run_test_case(test_pass))   # Уникальный ID теста, например, 3

# Проверка глобальных переменных
print("Total tests run:", tests_run)       # 3
print("Total tests failed:", tests_failed)  # 1
