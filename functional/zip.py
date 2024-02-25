# zip() combina listas en tuplas según index

# misma longitud

def zippedList(a, b, c):
    return list(zip(a, b, c))

print(zippedList([1, 2], [3, 4], [5, 6]))

# diferente longitud

lista1 = [1, 2, 3]
lista2 = ['a', 'b']

resultado = list(zip(lista1, lista2))

print(resultado) # [(1, 'a'), (2, 'b')]

# *args acepta un número indefinido de argumentos

def combinar(*args):
    return zip(*args)

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

# Combinar dos listas
print(list(combinar(lista1, lista2)))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Combinar tres listas
print(list(combinar(lista1, lista2, lista3)))
# Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]