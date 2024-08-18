# https://projecteuler.net/problem=14
from time import time


def collatz_seq_len(n: int):
    total = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        total += 1
    return total


def largest_collatz_sequence(max_start: int):
    max_seq_len = 0
    max_seq_num = None
    for i in range(1, max_start):
        collatz_len_i = collatz_seq_len(i)
        if collatz_len_i > max_seq_len:
            max_seq_len = collatz_len_i
            max_seq_num = i

    return max_seq_num


now = time()
print(largest_collatz_sequence(1000000), f"{time() - now} seconds")
