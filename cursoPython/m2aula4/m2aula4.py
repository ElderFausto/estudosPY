"""
def parte 4
"""

variavel = 'valor'


def func():
    print(variavel)


def func2():
    variavel = 'outro valor'
    print(variavel)


func()
func2()

print(variavel)

#########################################################


def func():
    outra_variavel = 'elder'
    return outra_variavel


def func2(dia):
    print(dia)


var = func()
func2(var)
