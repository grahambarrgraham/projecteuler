# https://projecteuler.net/problem=92
from time import time


def square_digits(n):
    return sum([int(i) * int(i) for i in str(n)])


def square_digit_chain(n):
    while n != 89 and n != 1:
        n = square_digits(n)
    return n


def count_square_digit_chains_below(n):
    result = 0
    for i in range(1, n):
        if square_digit_chain(i) == 89:
            result += 1
    return result


now = time()
print(count_square_digit_chains_below(10000000), f"{time() - now} seconds")
