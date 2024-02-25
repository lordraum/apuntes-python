# Las propiedades como argumentos

class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr

# Instanciar con las propiedades cómo parámetros

apple = Fruit('apple', 'red')
banana = Fruit('banana', 'yellow')
kiwi = Fruit('kiwi', 'green')

print(kiwi.colour)

# Ver todos los atributos de un objeto

print(dir(banana))