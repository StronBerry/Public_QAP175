def fobonacci(n):
    # Вспомогательная рекурсивная функция для вычисления n-го числа Фибоначчи
    def fibonacci(num):
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    # Создание списка с числами Фибоначчи до n-го
    series = [fibonacci(i) for i in range(n + 1)]
    return series


# Пример работы функции для ряда из 8 чисел
print(fobonacci(8))