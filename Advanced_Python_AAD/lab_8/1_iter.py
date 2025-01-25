from itertools import product

def get_cartesian_product(a, b):
    return list(product(a, b))

for el in get_cartesian_product([1, 2], [3, 4]):
    print(el)






#C:\Users\Александр\Documents\GitHub\Advanced_Python_AAD\lab_7