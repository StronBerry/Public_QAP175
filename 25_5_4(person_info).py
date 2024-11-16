class Person:
    def __init__(self, name=None, age=None, gender=None, occupation=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def set_attributes(self, attributes: dict):
        for key, value in attributes.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def show_card(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

p1 = Person()
p1.set_attributes({'name': 'Elon', 'age': 51, 'gender': 'Male', 'occupation': 'CEO', 'company': 'Tesla'})
p1.show_card()
# Вывод:
# Name: Elon
# Age: 51
# Gender: Male
# Occupation: CEO

p2 = Person(name='Mark', occupation='Expert')
p2.set_attributes({'name': 'Bob', 'occupation': 'Worker', 'company': 'StenWoods'})
p2.show_card()
# Вывод:
# Name: Bob
# Age: None
# Gender: None
# Occupation: Worker
