nums = [1, 2, 3, 4, 5, 6]
from functools import reduce

is_par_or_inpar = ["Par" if n % 2 == 0 else "Inpar" for n in nums]

pares = reduce(lambda x, y: x + ["Par"] if y % 2 == 0 else x, nums, [])

""" for n in numbers:
    numbers_x_2.append(n * 2) """

#(reduce(lambda x, y: x + y, lst))

print(is_par_or_inpar, pares)