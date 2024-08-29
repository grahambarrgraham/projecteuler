# https://projecteuler.net/problem=22
from pathlib import Path

ord_a = ord('A')


def name_score(index, name):
    word_score = sum([ord(i) - ord_a + 1 for i in name])
    index_score = index + 1
    return index_score * word_score


def name_scores(names: list[str]):
    return sum(name_score(i, n) for i, n in enumerate(names))


with Path(__file__).parent.joinpath("input/0022_names.txt").open() as f:
    input_ = f.read().split(",")
    input_ = [n[1:-1] for n in input_]
    print(name_scores(sorted(input_)))
