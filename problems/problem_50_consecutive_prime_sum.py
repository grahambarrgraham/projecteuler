# https://projecteuler.net/problem=50
from time import time

from problems.problem_7_find_nth_prime import is_prime


def primes_below(n):
    i = 2
    while i < n:
        if is_prime(i):
            yield i
        i += 1


def consecutive_prime_sum(n):
    primes = list(primes_below(n))
    primes_set = set(primes)
    prime_sum_sequences = []
    for i in range(len(primes)):
        seq = []
        sum_ = 0
        for j in range(len(primes) - i):
            nxt = primes[i + j]
            seq.append(nxt)
            sum_ += nxt
            if sum_ > n:
                break
            if sum_ in primes_set:
                prime_sum_sequences.append(seq.copy())
    return sorted(prime_sum_sequences, key=lambda s: len(s), reverse=True)


if __name__ == "__main__":
    now = time()
    result = consecutive_prime_sum(1000000)
    print(sum(result[0]), f"{round(time() - now, 2)} seconds")
