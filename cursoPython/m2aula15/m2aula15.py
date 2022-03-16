"""
combinations, permutations and product - itertools

combinação - ordem nao importa
permutação - ordem importa
ambos nao repetem valores unicos
produto - ordem importa e repete valores unicos

"""

""" 

from  itertools import  combinations

pessoas = ['elder', 'fausto', 'silva', 'nascimento']

for grupo in combinations(pessoas, 2):
    print(grupo) 

"""

"""

from itertools import permutations

pessoas = ['elder', 'fausto', 'silva', 'nascimento']

for grupo in permutations(pessoas, 2):
    print(grupo)
    
"""

from itertools import product

pessoas = ['elder', 'fausto', 'silva', 'nascimento']

for grupo in product(pessoas, repeat=2):
    print(grupo)




