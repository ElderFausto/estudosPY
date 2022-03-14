"""
tuplas em python
"""

t1 = 1, 2, 3, 4,5, 'a', 'b'
t2 = 'c', 'd', 'e', 6
t3 = t1 + t2

t1 = list(t1)
t1[0] = 1.1
print(t1)