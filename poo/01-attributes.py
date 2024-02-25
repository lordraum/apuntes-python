# Declarar clase

class Fruit:
    def __init__(self):
        self.name = 'apple'
        self.colour = 'red'

myFruit = Fruit()

# Acceder y/o reasignar el atributo del objeto

myFruit.colour = 'green'
print(myFruit.name, myFruit.colour)

