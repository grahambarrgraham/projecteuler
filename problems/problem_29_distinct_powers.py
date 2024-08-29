# https://projecteuler.net/problem=29
from time import time


def distinct_powers(n: int):
    return {a ** b for a in range(2, n + 1) for b in range(2, n + 1)}


now = time()
print(len(distinct_powers(100)))
