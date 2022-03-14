cpf = '16899535009'
novo_cpf = cpf [:-2]        # elimina os dois ultimos digitos do CPF
reverso = 10                # contador reverso
total = 0

for index in range (19):
    if index > 8:           # primeiro indice vai de 0 a 9
        index -= 9          # sao os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso     # valor total da mutiplicacao

    reverso -= 1            # decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if cpf == novo_cpf:
    print('Valido')
else:
    print('Invalido')
