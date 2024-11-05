from typing import List, Dict, Any, Set, Tuple

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    return [f"{user['first_name']} {user['last_name']}" for user in users]

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> Set[str]:
    emails1 = {user['email'].lower() for user in users1}
    emails2 = {user['email'].lower() for user in users2}
    return emails1 & emails2

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, Tuple[Any, ...]]:
    combined_data = {}
    for user in users:
        for key, value in user.items():
            if key in combined_data:
                combined_data[key].append(value)
            else:
                combined_data[key] = [value]
    # Преобразуем списки значений в кортежи
    for key in combined_data:
        combined_data[key] = tuple(combined_data[key])
    return combined_data

users_data = [
    {'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
    {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'},
    {'first_name': 'Anna', 'last_name': 'Smith', 'birth_date': '1988-03-08', 'email': 'anna.smith@example.com'},
    {'first_name': 'Emily', 'last_name': 'Brown', 'birth_date': '1993-11-28', 'email': 'emily_brown@hotmail.com'}
]

users_data_ext = [
    {'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}
]

print(convert_to_full_name(users_data))
# Ожидаемый результат: ['John Doe', 'Bob Johnson', 'Lev Sergeev', 'Anna Smith', 'Emily Brown']

print(find_matching_emails(users_data, users_data_ext))
# Ожидаемый результат: {'johndoe@gmail.com'}

print(combine_user_data(users_data))
# Ожидаемый результат:
# {
#     'first_name': ('John', 'Bob', 'Lev', 'Anna', 'Emily'),
#     'last_name': ('Doe', 'Johnson', 'Sergeev', 'Smith', 'Brown'),
#     'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01', '1988-03-08', '1993-11-28'),
#     'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com', 'anna.smith@example.com', 'emily_brown@hotmail.com')
# }
