"""
count - itertools
"""

from itertools import count

contador = count()
lista =['luiz', 'joao', 'maria', 'jose', 'silva']

lista = zip(contador, lista)
print(list(lista))