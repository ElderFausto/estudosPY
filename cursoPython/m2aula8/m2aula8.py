perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 1+1?',
        'respostas': {'a': '1', 'b': '2', 'c': '3'},
        'resposta_certa': 'b'
    },

    'Pergunta 2': {
        'pergunta': 'Quanto é 2+1?',
        'respostas': {'a': '1', 'b': '2', 'c': '3'},
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2-1?',
        'respostas': {'a': '1', 'b': '2', 'c': '3'},
        'resposta_certa': 'a'
    }
}
print()

resposta_certa = 0
for qq, qr in perguntas.items():
    print(f'{qq}: {qr["pergunta"]}')

    print('Respostas: ')
    for rq, rr in qr ['respostas'].items():
        print(f'{rq}: {rr}')

    resposta_usuario = input('Digite sua resposta: ')

    if resposta_usuario == qr['resposta_certa']:
        print('Voce acertou')
        resposta_certa += 1
    else:
        print('Voce errou!')

    print()

qtd_questions = len(perguntas)
porcentagem_acerto = resposta_certa / qtd_questions * 100

print(f'Voce acertou {resposta_certa} respostas.')
print(f'Sua porcentagem de acertoi foi: {porcentagem_acerto}%')
