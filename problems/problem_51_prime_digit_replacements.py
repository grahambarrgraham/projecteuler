# https://projecteuler.net/problem=51
from collections import Counter
from time import time

from problems.problem_7_find_nth_prime import is_prime


def find_same_digits(n: int):
    s = sorted(str(n))
    return [item for item, count in Counter(s).items() if count > 1]


def prime_replacements(n, a):
    for k in range(1, 10):
        candidate = int(str(n).replace(a, str(k)))
        if is_prime(candidate):
            yield candidate


def all_primes():
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


def prime_digit_replacements(target):
    for i in all_primes():
        for j in find_same_digits(i):
            if len(list(prime_replacements(i, j))) == target:
                return i


if __name__ == "__main__":
    now = time()
    print(prime_digit_replacements(8))
