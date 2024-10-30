def generate_test_case():
    case_id = 0

    def next_case():
        nonlocal case_id  # Указываем, что мы хотим использовать переменную из внешней области
        case_id += 1
        return case_id

    return next_case
# Создаем генератор тест-кейсов
get_test_case_id = generate_test_case()

# Генерируем несколько идентификаторов тест-кейсов
print(get_test_case_id())  # 1
print(get_test_case_id())  # 2
print(get_test_case_id())  # 3
