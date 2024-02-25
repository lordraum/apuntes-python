numbers = [1, 2, 3, 4]

# for x in numbers:
# print(x*2)

# expression = print(x*2)
# item = x
# iterable = numbers

# list comprehension fórmula
# newlist = [expression for item in iterable if condition == True]

doubleNumbers = [x*2 for x in numbers]


def dblNumLessFour(x): return [a*2 for a in x if a < 4]


print(dblNumLessFour(numbers))

# Reemplazar append
# El método append() viene ímplicito en la función
# Se utiliza una segunda variable que se va agregando al array en cada iteración


def addPares(x):
    return [a for a in x if a % 2 == 0]


# Ejemplo con función lambda
def pairsToArray(x): return [a for a in x if a % 2 == 0]

# Ejemplo con operador ternario y destructuring

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


print(addPares([3, 6, 8, 5, 46,]))
print(pairsToArray([3, 6, 8, 5, 46,]))

enteros = [1, 2, 4, 7]
def cuadrados(x): return [y**2 for y in x]


print(cuadrados([1, 4, 16, 49]))
