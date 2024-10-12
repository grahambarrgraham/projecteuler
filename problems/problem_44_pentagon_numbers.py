# https://projecteuler.net/problem=44
from itertools import combinations
from time import time


def pentagon_numbers_gen():
    n = 1
    while True:
        yield (n * (3 * n - 1)) // 2
        n += 1


def generate_n(gen, n):
    result = []
    for i in range(n):
        result.append(next(gen))
    return result


def pentagon_numbers():
    p_numbers = generate_n(pentagon_numbers_gen(), 10000)
    p_numbers_set = set(p_numbers)
    pairs = combinations(p_numbers[:2500], 2)
    return [(j, k) for j, k in pairs if abs(k - j) in p_numbers_set and j + k in p_numbers_set]


if __name__ == "__main__":
    now = time()
    p_j, p_k = pentagon_numbers()[0]
    print(abs(p_k - p_j), f"{round(time() - now, 2)} seconds")
