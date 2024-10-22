def create_report(sales_data, stats_function):
    # Получаем статистику, используя функцию stats_function
    total_revenue, total_quantity = stats_function(sales_data, revenue=True, quantity=True)

    # Вычисляем средний доход
    if total_revenue is not None:
        avg_revenue = total_revenue / len(sales_data)
    else:
        avg_revenue = 0

    # Формируем строку с отчетом
    report = f"Средний доход за данный период составил {avg_revenue:.1f}.\n"

    # Добавляем информацию о количестве проданных единиц товаров
    if total_quantity is not None:
        report += "Количество проданных единиц каждого товара:\n"
        for item, quantity in total_quantity.items():
            report += f"{item}: {quantity}\n"

    return report.strip()
