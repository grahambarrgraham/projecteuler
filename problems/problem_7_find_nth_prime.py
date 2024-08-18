# https://projecteuler.net/problem=7
from time import time


# taken from https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def find_nth_prime(n):
    primes = []
    i = 1
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes[-1]


if __name__ == "__main__":
    now = time()
    print(find_nth_prime(10001), f"{time() - now} seconds")
