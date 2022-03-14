"""
split - dividr uma string
join - juntar uma lista
enumerate - enumerar elementos da lista
"""

string = 'O brasil é o pais do futebol, e é 5x campeao mundial'
lista1 = string.split(' ')
lista2 = string.split(',')

palavra = ''
contagem = 0

############################################################################

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x')


string = 'o brasil é penta'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

###############################################################################

string = 'o brasil é penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)