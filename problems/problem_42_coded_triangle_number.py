# https://projecteuler.net/problem=42
from pathlib import Path
from time import time

from problems.problem_12_higest_divisable_triangle_number import triangle_number_gen


def is_triangle_word(word, triangle_nums):
    i = sum([ord(w) - ord('A') + 1 for w in word])
    return i in triangle_nums


def triangle_numbers_to_n(n):
    gen = triangle_number_gen()
    result = []
    for i in range(n):
        result.append(next(gen))
    return result


def coded_triangle_numbers(word_list):
    t = triangle_numbers_to_n(500)
    return [w for w in word_list if is_triangle_word(w, t)]


if __name__ == "__main__":
    now = time()
    f = Path(__file__).parent.joinpath("input/0042_words.txt").open()
    words = [a[1:-1] for a in f.read().split(',')]
    triangle_words = coded_triangle_numbers(words)
    print(len(triangle_words), f"{round(time() - now, 2)} seconds")
