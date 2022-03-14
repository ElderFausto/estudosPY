"""
dicionario em python

"""

d1 = {
    'str' : 'valor',
    123: 'outro valor',
    (1, 2, 3, 4) : 'Tupla',
}

print(d1)

#################################################

clientes = {
    'cliente1': {
        'nome': 'elder',
        'sobrenome': 'fausto'
    },
    'cliente2': {
        'nome': 'silva',
        'sobrenome': 'nascimento'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
