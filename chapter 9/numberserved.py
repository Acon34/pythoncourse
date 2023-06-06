class Restaurant:
    def __init__(self, name, rtype):
        self.name = name
        self.rtype = rtype
        self.numberserved = 0

    def describe(self):
        print(f'{self.name} is a {self.rtype} restaurant')

    def open(self):
        print(f'{self.name} is open')

    def set_number_served(self, customers):
        self.numberserved = customers


restaurant = Restaurant('Italos', 'Pizzaria')
print(restaurant.numberserved)
restaurant.set_number_served(30)
print(restaurant.numberserved)
