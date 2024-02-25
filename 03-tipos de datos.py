# (f) type() muestra el tipo de dato
    # str = string
    # int = number
    # float = decimal
    # bool = booleans
    # list = lista
    # tuple = lista inmutable
    # dict = dictionary
    # set = set
    # NonType = undefined

# strings
    # se escriben entre comillas simples o dobles
type('hello world')
    # Para mostrar el tipo de dato en cmd hay que pasarle type() a print()
print(type('hello world'))
    # Concatenar strings con operador +
print('hello' +' ' 'world' ' ' 'concatenado')

# numbers => números exactos
    #   se escribe tal cuál sin comillas
print(30)
type(30)

# float => números con decimales
print(30.5)
type(30.5)

# booleans => True - False
print(True)
type(True)
print(False)
type(False)

# list => lista de datos => se agrupa con [] se separa con ,
    # Una lista puede contener cualquier tipo de dato y sus respectivas combinaciones
type([5,10,15,20,25])
print([5,10,15,20,25])

# Tuple => lista cuyos elementos no se pueden cambiar () ,
type((2,4,6,8))
print((2,4,6,8))

# dictionaries => agrupa datos de una misma entidad => {key:value,} => objeto
print(type({
    'name': 'David',
    'lastName': 'Gómez',
}))

# set => agrupa de una misma entidad pero sin nombrar las keys   
print(type({'Rosas y vino', '$50000', '$8500'}))
# none es un dato indefinido => None
print(type(None))

