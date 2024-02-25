import operations
print(operations.sum(5, 3))

import operations as ops
print(ops.subs(5, 2))

from operations import mult
print(mult(4, 3))

from operations import div as dv
print(dv(16, 4))

# from operations import * --> Importa todas las herramientas del módulo

print(dir(operations)) # --> Muestra todas las herramientas disponibles en el módulo

# Importar librerías

from math import pow, sqrt

print('potencia', pow(3, 2))
print('raíz cuadrada', sqrt(16))

# Importar módulo que se encuentra en otra carpeta

from nested_module.hello import saludar
print(saludar('Fer'))



