# Crear subclase (padre)

class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def saludar(self):
        print(f'Hola mi nombre es {self.name} tengo {self.age} años')

user1 = Persona('David', 39)

user1.saludar()

# Crear subclase (hijo)
# Clase(SubClase)
# super() hereda las propiedades del padre al hijo (clase a subclase)

class Alumno(Persona):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def alerta(self):
        print(f'El alumno {self.name} pertenece al curso {self.course} tiene {self.age} años')    

alumno1 = Alumno('David', 39, 'POO en python')

alumno1.alerta()

print((alumno1))