class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def saludar(self):
        print(f'Hola mi nombre es {self.name} tengo {self.age} años')
