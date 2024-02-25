# importar desde functools
from functools import reduce

lista = [1, 2, 3, 4, 5]

def suma(lst):
    # no es necesario utilizar list()
    return (reduce(lambda x, y: x + y, lst))

print(suma(lista))