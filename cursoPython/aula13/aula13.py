"""
Formatção de valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:. (numero)f - quantidade de casas decimais (float)
:(caractere) (> ou< ou ^) (quantidade) (tipo - s, d ou f)

> - esquerda
< - direita
^ - centro

"""

num1 = 10
num2 = 3

divisao = num1 / num2
print(f'{divisao:.2f}')

num3 = 1150
print(f'{num3:0>10.2f}')

nome = 'elder'
sobrenome = 'fausto'
nome_formatado = '{1:#^50}'.format(nome, sobrenome) #0 == elder, 1 == fausto
print(nome_formatado)