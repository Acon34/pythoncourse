class User:
    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.surname = last_name
        self.age = age

    def describe(self):
        print(f'Name: {self.name}\n'
              f'Last name: {self.surname}\n'
              f'Age: {self.age}')

    def greet(self):
        print(f'Hello {self.name} happy {self.age} birthday')


andreas = User('Andreas', 'Con', 18)
christos = User('Christos', 'Koft', 18)

andreas.describe()
andreas.greet()

christos.describe()
christos.greet()