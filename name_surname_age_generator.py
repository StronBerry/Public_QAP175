import random

def generate_user_data(size, first_names, last_names, age_range):
    for _ in range(size):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        age = random.randint(age_range[0], age_range[1])
        yield (name, surname, age)

# Пример использования
first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]
user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])

for user in user_data_generator:
    print(user)
