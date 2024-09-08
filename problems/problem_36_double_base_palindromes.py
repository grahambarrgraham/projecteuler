# https://projecteuler.net/problem=36
from time import time


def is_palindrome(n: int):
    s = str(n)
    return s == s[::-1]


def is_palindrome_binary(n: int):
    s = str(bin(n))[2:]
    return s == s[::-1]


def double_base_palindromes(min_, max_):
    return [n for n in range(min_, max_) if is_palindrome(n) and is_palindrome_binary(n)]


now = time()
result = double_base_palindromes(0, 1000000)
# print(result)
print(sum(result), f"{time() - now} seconds")



