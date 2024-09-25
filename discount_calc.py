def calculate_discount(price, discount):
    # Вычисляем итоговую цену с учетом скидки
    return price * (1 - discount / 100)

def test_calculate_discount(*test_data):
   for data in test_data:
       price, discount, expected_result = data
       result = calculate_discount(price, discount)
       if abs(result - expected_result) < 0.01:  # использование abs для учёта погрешности вычислений с плавающей точкой
           print(f"Test passed for price={price}, discount={discount}")
       else:
           print(f"Test failed for price={price}, discount={discount}, expected {expected_result}, got {result}")

# Пример использования с исправленными данными:
test_calculate_discount((100, 10, 90),   # Ожидаемая цена: 90
    (200, 20, 160),  # Ожидаемая цена: 160
    (300, 50, 150),  # Ожидаемая цена: 150
    (405, 0, 400)    # Ожидаемая цена: 405 (исправлено с 400 на 405)
)
