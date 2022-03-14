"""
Listas em python

fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.append('a')
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.insert(0, 'a')
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

l1 = [1, 2, 3]
l1.pop()
del(l1[0])

l1 = 1, 2, 3, 4, 5, 6
print(max(l1))
print(min(l1))

l5 = list(range(0,100, 2))
print(l5)