def format_date(date, format="dmy"):
    # Разделяем строку на компоненты: год, месяц и день
    year, month, day = date.split("-")

    # В зависимости от формата выводим дату
    if format == "dmy":
        return day + month + year
    elif format == "mdy":
        return month + day + year
    elif format == "ymd":
        return year + month + day
    else:
        # Возвращаем исходную строку, если формат неизвестен
        return date


# Пример использования функции:
print(format_date("2023-07-01"))  # 01072023 (по умолчанию dmy)
print(format_date("2023-07-01", format="dmy"))  # 01072023
print(format_date("2023-07-01", format="mdy"))  # 07012023
print(format_date("2023-07-01", format="ymd"))  # 20230701
print(format_date("2023-07-15", format="xyz"))  # 2023-07-15 (неизвестный формат)
