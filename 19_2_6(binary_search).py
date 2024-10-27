def binary_search(sorted_list, target):
    # Вспомогательная рекурсивная функция с указанием начальной и конечной позиции
    def search_recursive(low, high):
        # Базовый случай: если подсписок пуст, возвращаем False
        if low > high:
            return False

        # Определяем средний индекс
        mid = (low + high) // 2

        # Если средний элемент равен искомому значению, возвращаем True
        if sorted_list[mid] == target:
            return True
        # Если искомое значение меньше среднего элемента, ищем в левой половине
        elif target < sorted_list[mid]:
            return search_recursive(low, mid - 1)
        # Если искомое значение больше среднего элемента, ищем в правой половине
        else:
            return search_recursive(mid + 1, high)

    # Запуск рекурсивного поиска на всем диапазоне индексов
    return search_recursive(0, len(sorted_list) - 1)


# Примеры работы функции
print(binary_search([1, 3, 5, 7, 9, 11], 7))  # True
print(binary_search([1, 3, 5, 7, 9, 11], 6))  # False
