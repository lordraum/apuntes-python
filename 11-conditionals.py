# https://youtu.be/chPhlsHoEPo?t=8421

# if, else, elif (else if)

x = 30

if x > 30:
    print('Eres mayor de 30 años')
elif x <30:
    print('Eres menor de 30 años')
else:
    print('Tienes 30 años')

name = 'Pepito'
lastName = 'López'

# condicionales anidados

if name == 'David':
    if lastName == 'Gómez':
        print(f'Tu nombre es {name} {lastName}')
    else:
        print(f'Tú nombre es {name}')
else:
    print('Tú nombre no lo sé')

# operadores lógicos, and, or, not

number = 5

if number > 2 and number < 10:
    print(f'{number} es mayor que 2 y menor que 10')

userCode = 1
nameUser = 'Jonás'

if userCode == 1 or userCode == 2:
    print(f'Welcome user {nameUser}')

stock = 5

if (not(stock == 0)):
    print('Todavía tienes inventario')



# https://youtu.be/chPhlsHoEPo?t=9232