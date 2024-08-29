# https://projecteuler.net/problem=26
from time import time

from problems.problem_7_find_nth_prime import is_prime


def quadratic_prime_seq(a, b) -> list[int]:
    result = []
    z = b
    n = 1
    while is_prime(z):
        result.append(z)
        z = (n * n) + (a * n) + b
        n += 1
    return result


def quadratic_primes(n: int):
    all_coefficients = [(a, b) for a in range(-1 * n - 1, n) for b in range(1, n) if is_prime(b)]
    result = [((a, b), quadratic_prime_seq(a, b)) for a, b in all_coefficients]
    return sorted(result, key=lambda r: len(r[-1]))


now = time()
seqs = quadratic_primes(1000)
# for (a,b), seq in seqs:
#     print(a, b, len(seq), seq)
(a, b), _ = seqs[-1]
print(a * b, f"{round(time() - now, 2)} seconds")

# print(len(quadratic_prime_seq(-79, 1601)))
# print(len(quadratic_prime_seq(1, 41)))