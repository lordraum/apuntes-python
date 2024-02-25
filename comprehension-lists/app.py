numbers = [1, 2, 3, 4]

#for x in numbers:
    #print(x*2)

# expression = print(x*2)
# item = x
# iterable = numbers

# list comprehension fórmula
# newlist = [expression for item in iterable if condition == True]

doubleNumbers = [x*2 for x in numbers]

doubleNumbersMinorToFour =  [x*2 for x in numbers if x < 4]

print(doubleNumbersMinorToFour)

# el item en solitario como expresoón reemplaza método append

def addPares(x):
    return [a for a in x if a % 2 == 0]
# Se añade (a) al array en cada iteración en que el módulo de a en 2 es igual a 0.

# Ejemplo con función lambda
pairsToArray = lambda x: [a for a in x if a % 2 == 0]

print(addPares([3, 6, 8, 5, 46,]))
print(pairsToArray([3, 6, 8, 5, 46,]))

enteros = [1, 2, 4, 7]
cuadrados = lambda x: [y**2 for y in x]

print(cuadrados([1, 4, 16, 49]))



     



