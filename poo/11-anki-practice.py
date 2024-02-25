class Instrument:
    def __init__(self, instName, instType):
        self.instName = instName
        self.instType = instType
    def showInfo(self):
        print(f'El instrumento se llama {self.instName} y su tipo es {self.instType}')

piano = Instrument('Piano', 'cuerda')
piano.showInfo()


