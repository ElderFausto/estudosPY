"""
for / else em python
"""

variavel = ['elder', 'fausto', 'silva']

tem_e = False
for valor in variavel:
    if valor.startswith('e'):
        tem_e = True

if tem_e:
    print('Existe a letra "e"')
else:
    print('Nao existe a letra "e" ')