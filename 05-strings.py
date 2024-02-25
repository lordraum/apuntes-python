# https://youtu.be/chPhlsHoEPo?t=3776

myStr = 'Hello World'
myStrNum = '555'

# comentar varias líneas
# seleccionar ctrl k + ctrl c
# ctrl k + u para descomentar

#dir() nos muestra las propiedades y datos con los que puede trabajar un tipo de dato
# print(dir(myStr))

#los métodos se utilizan con la sintáxis del punto => string.method()

# .upper() mayúscula | .upper() minúscula | .capitalize() letra capital


print(myStr.upper())
print(myStr.lower())
print(myStr.capitalize())

# replace() par1 old, par2 new
print(myStr.replace('Hello', 'Whats up'))

# count() par1 character(s), cuenta los caracteres o grupo de caracteres que coinciden con la búsqueda
print(myStr.count('o'))

# starswith() par 1 character(s) devuelve True o False, según el string empiece con cierto(s) caracter(es)
# endswith() lo contrario a starswith()
print(myStr.startswith('Hello'))

# split() par => caracter que separa. Divide un string, por defecto separa con respecto a los espacios

print(myStr.split())
print(myStr.split(','))
# Devuelve una lista con los nuevos strings

# find() par => characters. Busca la posición del 1er caracter(es) que coincida
# la posición se cuenta desde 0

print(myStr.find('Hello'))

# la funcion len() devuelve la cantidad de caracteres del string
print(len(myStr))

# index() par character(s) => devuelve el índice del caracter.
print(myStr.index(' '))

# isnumeric(), isalpha(), devuelve True si el string es númerico o alfa numérico.
print(myStrNum.isnumeric())

# Acceder a los carácteres de un string
# string[index] admite valores negativos (cuenta desde el último caracter)
print(myStr[6])

# f-strins
# Facilita imprimir diferentes tipos de datos en una expresión
# se utiliza con la letra f, comillas y llaves
# print(f'mi string en pantalla {dato} ok!')

print(f'la frase: {myStr}, tiene {len(myStr)} caracteres')
print(f'la frase: {myStr}, tiene {len(myStr)} caracteres')
print(f'la frase: {myStr}, tiene {len(myStr)} caracteres')
print(f'la frase: {myStr}, tiene {len(myStr)} caracteres')
print(f'la frase: {myStr}, tiene {len(myStr)} caracteres')



