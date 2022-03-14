"""
zip - unindo iteraveis
zip_longest - itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['olinda', 'recife', 'salvador', 'joao pessoa']
estados = ['PE', 'PE', 'bahia']

cidades_estados = zip(
    indice,
    cidades,
    estados,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

