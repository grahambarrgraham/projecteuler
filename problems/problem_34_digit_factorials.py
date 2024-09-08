# https://projecteuler.net/problem=34
from functools import cache
from time import time


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


def digit_factorials():
    result = []
    for i in range(3, 100000):
        digits = [int(s) for s in str(i)]
        s = sum([factorial(d) for d in digits])
        if s == i:
            result.append(i)
    return result


now = time()
results = digit_factorials()
print(results)
print(sum(results), f"{round(time() - now, 2)} seconds")
