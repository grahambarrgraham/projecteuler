# https://projecteuler.net/problem=49
from itertools import combinations
from time import time

from problems.problem_60_prime_pair_sets import n_primes


def has_same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))


def numbers_with_same_digits(prime, four_digit_primes):
    return [p for p in four_digit_primes if has_same_digits(prime, p)]


def is_arithmetic_sequence(lst: list):
    return len({lst[i + 1] - lst[i] for i in range(len(lst) - 1)}) == 1


def flatten(xss):
    return [x for xs in xss for x in xs]


def prime_permutations():
    triplets = flatten([combinations(p, 3) for p in n_digit_prime_permutations(4) if len(p) > 2])
    return [t for t in triplets if is_arithmetic_sequence(t)]


def n_digit_prime_permutations(n):
    n_digit_primes = [p for p in n_primes(1000, 1100) if len(str(p)) == n]
    n_digit_primes_permutations = []
    seen = set()
    for i, prime in enumerate(n_digit_primes):
        if prime not in seen:
            permutations = numbers_with_same_digits(prime, n_digit_primes[i:])
            n_digit_primes_permutations.append(permutations)
            seen.update(permutations)
    return n_digit_primes_permutations


if __name__ == "__main__":
    now = time()
    result = prime_permutations()[-1]
    print(result, f"{round(time() - now, 2)} seconds")
