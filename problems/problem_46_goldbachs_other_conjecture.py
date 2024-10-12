# https://projecteuler.net/problem=46
from time import time

from problems.problem_60_prime_pair_sets import n_primes
from problems.problem_7_find_nth_prime import is_prime


def odd_composite_number_gen():
    n = 3
    while True:
        if (not is_prime(n)) and n % 2 != 0:
            yield n
        n += 1


def n_squared_goldbach_numbers(n):
    primes = list(n_primes(2, n + 2))
    squares = [2 * (i ** 2) for i in range(1, n + 1)]
    return sorted({p + s for p in primes for s in squares})


def goldbachs_other_conjecture():
    generator = odd_composite_number_gen()
    goldbach_nums = n_squared_goldbach_numbers(1000)
    while True:
        odd_composite = next(generator)
        if odd_composite not in goldbach_nums:
            return odd_composite


if __name__ == "__main__":
    now = time()
    result = goldbachs_other_conjecture()
    print(result, f"{round(time() - now, 2)} seconds")
