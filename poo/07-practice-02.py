class Cancion:
    def __init__(self, nombre, genero, estado):
        self.nombre = nombre
        self.genero = genero
        self.estado = estado
    def theAlert(self):
        print(f'La canción del repertorio {self.nombre}, es del género {self.genero} y su correcta interpretación está en un {self.estado}%')

pueblitoViejo = Cancion('Pueblito viejo', 'Música andina colombiana', 90)

pueblitoViejo.theAlert()
