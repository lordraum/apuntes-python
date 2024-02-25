# declarar un método
class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
    def details(self):
        print(f'my {self.name} is {self.colour}')

apple = Fruit('apple', 'red')
apple.details()