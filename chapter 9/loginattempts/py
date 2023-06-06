class User:
    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.login_attempts = 0

    def describe(self):
        print(f'Name: {self.name}\n'
              f'Last name: {self.surname}\n'
              f'Age: {self.age}')

    def greet(self):
        print(f'Hello {self.name} happy {self.age} birthday')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


andreas = User('Andreas', 'Constandinou', 18)
print(andreas.login_attempts)
andreas.increment_login_attempts()
print(andreas.login_attempts)
andreas.reset_login_attempts()
print(andreas.login_attempts)
