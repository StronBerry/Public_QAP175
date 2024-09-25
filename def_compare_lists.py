def compare_lists(list1, list2, ignore_case=False):
    if ignore_case:
        # Приводим все элементы к нижнему регистру для сравнения без учета регистра
        list1_lower = [item.lower() if isinstance(item, str) else item for item in list1]
        list2_lower = [item.lower() if isinstance(item, str) else item for item in list2]
        # Сравниваем списки по приведенным значениям
        return [item for item, item_lower in zip(list1, list1_lower) if item_lower not in list2_lower]
    else:
        # Обычное сравнение без игнорирования регистра
        return [item for item in list1 if item not in list2]

# Пример использования функции:
print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"]))
# ["apple"]

print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"], ignore_case=True))
# []
