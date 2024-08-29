# https://projecteuler.net/problem=32
from itertools import permutations
from time import time


def join_digits(t: tuple) -> int:
    return int(''.join([str(i) for i in t]))


def pandigital_products():
    arrangements = [(a, b, c) for a in range(1, 8) for b in range(1, 8) for c in range(1, 8) if a + b + c == 9]
    results = []
    for perm in permutations(range(1, 10)):
        for a, b, _ in arrangements:
            mltd = join_digits(perm[0: a])
            mltr = join_digits(perm[a: a + b])
            product = join_digits(perm[a + b:])
            if mltd * mltr == product:
                results.append((mltd, mltr, product))

    return results


now = time()
all_products = pandigital_products()
result = sum({p for _, _, p in all_products})
# for r in all_products:
#     print(r)
print(result, f"{round(time() - now, 2)} seconds")
