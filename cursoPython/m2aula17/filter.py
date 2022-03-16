from m2aula17 import produtos, pessoas, lista

"""
nova_lista = filter(lambda x: x > 5, lista)

print(list(nova_lista))
"""

nova_lista = filter(lambda p: p['preco'] > 2.1, produtos)

for produto in nova_lista:
    print(produto)