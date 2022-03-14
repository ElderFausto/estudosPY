
"""
frase = 'benedictus qui venit in nomine Domini'
t_frase = len(frase)
contador = 0

while contador < t_frase:
    print(frase[contador], contador)
    contador += 1
"""

frase = 'benedictus qui venit in nomine Domini'
t_frase = len(frase)
contador = 0
n_string = ''

while contador < t_frase:
    letra = frase[contador]
    if letra == 'n':
        n_string += 'N'
    else:
        n_string += letra
    contador += 1
print(n_string)