# https://projecteuler.net/problem=24
from itertools import permutations

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = permutations(l, len(l))
for i in range(1000000 - 1):
    next(p)

print(''.join([str(i) for i in next(p)]))
