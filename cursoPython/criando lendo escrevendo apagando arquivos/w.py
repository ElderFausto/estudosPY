file = open('abc.txt', 'w+')

file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')

"""
file.seek(0, 0)
print('lendo linhas: ')
print(file.read())
print('################')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#############')

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()
"""

with open('abc.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')

    file.seek(0)
    print(file.read())
