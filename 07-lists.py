# https://youtu.be/chPhlsHoEPo?t=5891

# las listas se pueden crear manualmente

colors = ['red', 'blue', 'green']
print(colors)

# ó con la función constructor list()
# se debe utilizar con doble paréntesis (tupla)

numbersList = list((1, 2, 3, 4))
print(numbersList)

# range(inicio, cantidad) Crea una lista según un rango


r = list(range(1, 10))
print(r)

# terminal [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Acceder a elementos de la lista según el índice

print(colors[1])
# blue

# IMPORTANTE. Al igual que en los strings se puede utilizar índices inversos

print(colors[-1])
# green

# Verificar si un elemento esta en la lista con el comando 'in'

print('green' in colors)
# True

# Modificar elemento
colors[2] = 'violet'
print(colors)

# Métodos lists

# append() => agrega 1 elemento al final

colors.append('yellow')
print(colors)

# extend([]) => Agrega varios elementos en forma de lista

colors.extend(['brown', 'pink'])

print(colors)

# insert(index, value) Inserta elementos en la posición deseada

colors.insert(1, 'black')
print(colors)

#pop() elimina el último elemento o el índice deseado
colors.pop()
colors.pop(1)

print(colors)

# remove() elimina el elemento deseado según el valor insertado

colors.remove('red')
print (colors)

# clear() vacía la lista

# sort() ordena elementos (por defecto según código ascii)
colors.sort()

# ordenar al revés

colors.sort(reverse = True)
print(colors)

