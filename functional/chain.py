# chain une y  convierte en iterable varios arrays

from itertools import chain
from functools import reduce

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def combineAndSum(a, b):
    return reduce(lambda x, y: x + y, chain(a, b))

print(combineAndSum(list1, list2))

names = ['David', 'Fernando']
lastNames = ['Gómez', 'Carrillo']

completeName = ' '.join(list(chain(names, lastNames)))

print(completeName)
