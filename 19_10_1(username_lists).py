from datetime import date, datetime
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    # Преобразуем строку с датой рождения в объект даты
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    today = date.today()
    # Вычисляем возраст
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adults = []
    for user in users:
        # Вычисляем возраст пользователя
        age = calculate_age(user['birth_date'])
        # Если возраст 18 или больше, добавляем в список взрослых
        if age >= 18:
            adults.append(user)
    return adults

def generate_username(first_name: str, last_name: str) -> str:
    # Берем первую букву имени и добавляем фамилию
    username = f"{first_name[0].lower()}.{last_name.lower()}"
    return username

print(calculate_age("2000-01-01"))  # 24
print(calculate_age("1995-12-31"))  # 28
print(calculate_age("1980-02-29"))  # 44
print(calculate_age("2005-07-09"))  # 19

users_data = [
    {'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'},
    {'first_name': 'Charlie', 'last_name': 'Brown', 'birth_date': '2010-06-15'}
]

print(filter_adults(users_data))
# Ожидаемый результат: [{'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'}]

print(generate_username("John", "Doe"))      # j.doe
print(generate_username("Alice", "Smith"))   # a.smith
print(generate_username("Eve", "Brown"))     # e.brown
