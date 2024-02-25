# La función __str__ permite que el objeto se imprima como string en pantalla

class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
    def details(self):
        print(f'my {self.name} is {self.colour}')
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

apple = Fruit('apple', 'red')
apple.details()
print(apple)
