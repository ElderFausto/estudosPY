nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

idade_menor = 18
idade_maior = 70

idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} não pode pegar o emprestimo')
