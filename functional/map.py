
lista = [1, 2, 3, 4, 5]
myList = [2, 4, 6, 8, 10]

# ejemplo
resultados = list(map(lambda x: x ** 2, lista))
print((resultados))  # [1, 4, 9, 16, 25]

# ejemplo con función
def addOneToListElement(lst):
    return list(map(lambda x: x + 1, lst))

print(addOneToListElement(myList))