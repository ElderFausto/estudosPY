"""
funções (def) *args **kwargs
def parte 3
"""


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5, 6]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2)


################################################################

def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    print(nome)


lista = [1, 2, 3, 4, 5, 6]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Elder', sobrenome='Fausto')
