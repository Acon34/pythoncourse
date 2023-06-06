class Restaurant:
    def __init__(self, name, rtype):
        self.name = name
        self.rtype = rtype

    def describe(self):
        print(f'{self.name} is a {self.rtype} restaurant')

    def open(self):
        print(f'{self.name} is open')


Italos = Restaurant('Italos', 'Pizzaria')
KFC = Restaurant('KFC', 'chicken')
McDonalds = Restaurant('McDonalds', 'fast food')

Italos.describe()
KFC.describe()
McDonalds.describe()
