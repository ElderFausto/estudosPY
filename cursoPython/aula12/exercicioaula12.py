numero = input('Digite um numero: ')

if numero.isdigit():
    numero = int(numero)
    if numero %2 == 0:
        print(f'Seu {numero} é par!')
    else:
        print(f'Seu {numero} é impar!')

else:
    print('Isso nao é um numero inteiro')


######################################################


horas = input('Digite um horario (00:00-23:00h): ')


if horas.isdigit():

    if horas >= 0 and  horas < 11:
        print('Bom dia!')
    elif horas >= 12 and horas <= 17:
        print('Boa tarde')
    elif horas >= 18 and horas <= 24:
        print('Boa noite')
    else:
        print('Esse horario nao existe!')

else:
    print('Isso não é um numero!')
#########################################################

user = input('Digite seu nome: ')

if len(user) <= 4:
    print('Seu nome é curto!')
elif len(user) >= 5 and len(user) <=6:
    print('Seu nome é normal ')
else:
    print('Seu nome é muito grande!')

