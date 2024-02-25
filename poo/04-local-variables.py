# Declarar variables locales

# Método 1

class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
        self.exp_date = '05/12/2022'
    def details(self):
        print(f'expires on {self.exp_date}')

# Método 2

class Fruta:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
    def details(self):
        exp_date = '05/12/2022'
        print(f'The {apple.name} expires on {exp_date}')


apple = Fruit('apple', 'red')
apple.details()

banana = Fruta('banana', 'yellow')
banana.details()