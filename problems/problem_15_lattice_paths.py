# https://projecteuler.net/problem=15
from time import time


def lattice_paths(n: int):
    s = {0: [1 for _ in range(n + 1)]}
    for i in range(1, n + 1):
        s[i] = [1]
        for j in range(1, n + 1):
            s[i].append(s[i][j - 1] + s[i - 1][j])
    return s[n][n]


now = time()
print(lattice_paths(20), f"{time() - now} seconds")
