class User:
   def __init__(self, login, password, name, email=None, role=None):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role
       self.location = 'Moscow'

   def create_task(self, project, description):
       project.add_task(self, description)


user1 = User("JohnD", "mloz512qyt", "John Doe")
print(user1.__dict__)

# {'login': 'JohnD', 'password': 'mloz512qyt', 'name': 'John Doe', 'email': None, 'role': None, 'location': 'Moscow'}