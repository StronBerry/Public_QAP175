prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

# Преобразуем цены в евро
prices_in_euro = list(map(lambda price: price * exchange_rate, prices_in_usd))