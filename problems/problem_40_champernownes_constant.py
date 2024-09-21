# https://projecteuler.net/problem=40
from time import time


def champernownes_fraction(n):
    i, fraction = 1, [a for a in '123456789']
    while len(fraction) < n:
        for d in range(0, 10):
            fraction.extend(str(i))
            fraction.append(str(d))
        i += 1
    return fraction


def champernownes_constant(n):
    result, i, f = 1, 1, champernownes_fraction(n)
    while i <= n:
        result *= int(f[i - 1])
        i *= 10
    return result


now = time()
print(champernownes_constant(1000000), f"{round(time() - now, 2)} seconds")
