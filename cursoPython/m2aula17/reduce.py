from m2aula17 import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)


soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
print(soma_precos / len(produtos))


soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades)
print(soma_idades / len(pessoas))
