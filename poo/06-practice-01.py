class Product:
    def __init__(self, name, price, active):
        self.name = name
        self.price = price
        self.active = active
    def clientCall(self):
        shippingPrice = 8000
        total = shippingPrice + self.price
        if self.active == True:
            print(f'El artículo {self.name} cuesta ${self.price}, el valor del domicilio es ${shippingPrice}, para un total de ${total}')
        else:
            print(f'El artículo {self.name} no está a la venta en estos momentos')

cajaFelizDia = Product('Caja Feliz Día', 50000, False)

cajaFelizDia.clientCall()

