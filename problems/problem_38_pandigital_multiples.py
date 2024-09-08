# https://projecteuler.net/problem=38
from time import time

one_to_nine = [a for a in '123456789']


def is_pandigital(s) -> int:
    return sorted(s) == one_to_nine


def pandigital_multiples():
    results = []

    for i in range(1, 10000):
        counter = 1
        s = ''
        while len(s) < 9:
            p = i * counter
            s += str(p)
            counter += 1

        if len(s) == 9 and is_pandigital(s):
            results.append(int(s))

    return results


now = time()
result = pandigital_multiples()
print(result)
print(max(result), f"{round(time() - now, 2)} seconds")
