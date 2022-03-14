"""
for in em python
iterando strings com for
função range (start=0, stop, step=1)

"""

for n in range(0,10,2):
    print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)