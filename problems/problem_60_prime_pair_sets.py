# https://projecteuler.net/problem=60
from itertools import combinations
from time import time

from problems.problem_51_prime_digit_replacements import all_primes
from problems.problem_7_find_nth_prime import is_prime


# def is_prime_pair_set(n: set[int]):
#     c = [(str(a), str(b)) for a, b, in combinations(n, 2)]
#     return all([is_prime(int(a + b)) and is_prime(int(b + a)) for a, b, in c])


def is_prime_pair_set(n: set[int]):
    for a, b, in combinations(n, 2):
        a, b = str(a), str(b)
        if not is_prime(int(a + b)) or not is_prime(int(b + a)):
            return False
    return True


def is_prime_pair_set_2(s: set[int], n):
    b = str(n)
    for a in s:
        a, b = str(a), str(b)
        if not is_prime(int(a + b)) or not is_prime(int(b + a)):
            return False
    return True


def n_primes(start, n):
    i = start
    c = 0
    while c < n:
        if is_prime(i):
            c += 1
            yield i
        i += 1


def prime_pair_sets():
    result = []
    for c in combinations(n_primes(1, 500), 5):
        if is_prime_pair_set(c):
            result.append(c)
            # print(s, c)
    return result


def prime_pair_set_2(s):
    result = []
    for c in n_primes(1, 999999):
        if is_prime_pair_set_2(s, c):
            result.append(c)
            # print(s, c)
    return result


# print(prime_pair_sets())
# print(prime_pair_set_2({23, 311, 677, 827}))
# print(is_prime_pair_set_2({3, 7, 109, 673}, 29059))
# print(is_prime_pair_set_2({23, 311, 677, 827}, 29059))
# print(list(n_primes(125)))
now = time()
# result = prime_pair_sets(4)
# print(result)
print(prime_pair_sets(), f"{round(time() - now, 2)} seconds")
