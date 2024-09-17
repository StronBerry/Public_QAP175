# def check_password(password):
#     # Проверка длины пароля
#     if len(password) < 8:
#         print("Пароль должен быть не менее 8 символов")
#
#     # Проверка наличия заглавной буквы
#     if not any(char.isupper() for char in password):
#         print("Пароль должен содержать хотя бы одну заглавную букву")
#
#     # Проверка наличия строчной буквы
#     if not any(char.islower() for char in password):
#         print("Пароль должен содержать хотя бы одну строчную букву")
#
#     # Проверка наличия цифры
#     if not any(char.isdigit() for char in password):
#         print("Пароль должен содержать хотя бы одну цифру")
#
#
# # Пример использования
# check_password("_")
#
# # check_password('1')
# check_password('12345678')


def check_password(password):
   if len(password) < 8:
       print("Пароль должен быть не менее 8 символов")
   upper, lower, digit = False, False, False
   for char in password:
       if char.isupper():
           upper = True
       elif char.islower():
           lower = True
       elif char.isdigit():
           digit = True
   if not upper:
       print("Пароль должен содержать хотя бы одну заглавную букву")
   if not lower:
       print("Пароль должен содержать хотя бы одну строчную букву")
   if not digit:
       print("Пароль должен содержать хотя бы одну цифру")