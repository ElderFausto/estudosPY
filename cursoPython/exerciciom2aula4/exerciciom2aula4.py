def func1():
    return 'ola mundo'


def func2(funcao):
    return funcao()


executando = func2(func1)
print(executando)


###############################################

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'elder')
executando2 = mestre(saudacao, 'elder', saudacao='boa tarde!')
print(executando)
print(executando2)

