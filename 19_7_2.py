def sales_stats(sales_data, **kwargs):
    total_revenue = None
    total_quantity = None

    # Если был передан аргумент revenue=True
    if 'revenue' in kwargs and kwargs['revenue']:
        total_revenue = sum(quantity * price for _, quantity, price in sales_data)

    # Если был передан аргумент quantity=True
    if 'quantity' in kwargs and kwargs['quantity']:
        total_quantity = {}
        for item, quantity, _ in sales_data:
            if item in total_quantity:
                total_quantity[item] += quantity
            else:
                total_quantity[item] = quantity

    # Если ни один ключевой аргумент не был распознан, вернуть None, None
    if total_revenue is None and total_quantity is None:
        return (None, None)

    return (total_revenue, total_quantity)

# sales_data = [('Apple', 10, 0.5), ('Orange', 5, 0.6)]

# print(sales_stats(sales_data, revenue=True))
# # (8.0, None)

# print(sales_stats(sales_data, quantity=True))
# # (None, {'Apple': 10, 'Orange': 5})

# print(sales_stats(sales_data, revenue=True, quantity=True))
# # (8.0, {'Apple': 10, 'Orange': 5})
