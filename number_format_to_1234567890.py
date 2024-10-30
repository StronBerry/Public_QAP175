phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
    # Фильтруем символы, оставляя только цифры
    return ''.join(filter(str.isdigit, number))

# Применяем функцию к каждому номеру в списке
formatted_numbers = list(map(format_phone_number, phone_numbers))
print(formatted_numbers)