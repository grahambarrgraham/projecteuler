# https://projecteuler.net/problem=43
from itertools import permutations
from time import time

from problems.problem_60_prime_pair_sets import n_primes


def has_sub_string_divisibility(s, primes):
    for i in range(len(s) - 3):
        sub = s[i + 1: i + 4]
        if int(sub) % primes[i] != 0:
            return False
    return True


def sub_string_divisibility():
    result = []
    primes = list(n_primes(2, 7))
    for perm in permutations(range(0, 10)):
        s = ''.join([str(i) for i in perm])
        if has_sub_string_divisibility(s, primes):
            result.append(int(s))
    return result


if __name__ == "__main__":
    now = time()
    print(sum(sub_string_divisibility()), f"{round(time() - now, 2)} seconds")
