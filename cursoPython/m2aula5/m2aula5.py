lista = [
    ['p1', 13],
    ['p2', 15],
    ['p3', 7],
    ['p4', 8],
    ['p5', 10]
]


def func(item):
    return item[1]


print(sorted(lista, key=lambda i: i[0], reverse=True))
print(sorted(lista, key=lambda i: i[1]))
print(lista)