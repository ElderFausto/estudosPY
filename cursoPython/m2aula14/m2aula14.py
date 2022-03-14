"""
count - itertools
"""

from itertools import count

contador = count()

for valor in contador:
    print(valor)

    if valor >= 10:
        break