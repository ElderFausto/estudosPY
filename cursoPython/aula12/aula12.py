usuario = input('Qual seu user?: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Faltam caracteres')
else:
    print('Usuario aceito')