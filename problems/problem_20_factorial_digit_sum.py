# https://projecteuler.net/problem=20
from functools import reduce


def factorial(n: int):
    return reduce(lambda a, b: a * b, [i for i in range(1, n + 1)], 1)


def factorial_digit_sum(n: int):
    f = factorial(n)
    print(f)
    return sum([int(i) for i in str(f)])


print(factorial_digit_sum(100))
