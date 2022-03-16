from m2aula17 import produtos, pessoas, lista


nomes = map(lambda p: p['idade'], pessoas)

for pessoa in nomes:
    print(pessoa)
