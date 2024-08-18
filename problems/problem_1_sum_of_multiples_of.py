# https://projecteuler.net/problem=1

def multiples_of(lst: list[int], max_val) -> list[int]:
    return [n for n in range(max_val) if any(n % i == 0 for i in lst)]


def sum_of_multiples_of(lst, n):
    return sum(multiples_of(lst, n))


print(sum_of_multiples_of([3, 5], 1000))
