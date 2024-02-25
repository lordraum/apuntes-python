lista = [1, 2, 3, 4, 5]

def pares(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

print(pares(lista))

