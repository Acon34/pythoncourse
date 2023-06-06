class Restaurant:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f'{self.name} is open')


class IceCreamStand(Restaurant):
    def __init__(self, name, *flavours):
        super().__init__(name)
        self.flavours = flavours

    def show_flavours(self):
        print(self.flavours)


PahitIce = IceCreamStand('Name', '1', '2', '3')
PahitIce.show_flavours()
