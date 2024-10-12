# https://projecteuler.net/problem=48
from functools import cache
from time import time

from problems.problem_3_largest_prime_factor import prime_factors


def self_powers(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i ** i
    return acc


if __name__ == "__main__":
    now = time()
    result = str(self_powers(1000))[-10:]
    print(result, f"{round(time() - now, 2)} seconds")
