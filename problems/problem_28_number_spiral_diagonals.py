# https://projecteuler.net/problem=28
from time import time


def number_spiral_diagonals(n: int):
    result = 1
    for i in range(3, n + 1, 2):
        # the top right diagonal is the sequence of odd squares
        result += (i * i * 4) - (6 * (i - 1))
    return result


now = time()
r = number_spiral_diagonals(1001)
print(r)