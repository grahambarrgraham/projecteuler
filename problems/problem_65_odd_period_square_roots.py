# https://projecteuler.net/problem=65
from pathlib import Path

from problems.problem_18_maximum_path_sum_I import maximum_path_sum, read_input

with Path(__file__).parent.joinpath("input/0067_triangle.txt").open() as f:
    input_ = f.read()
    print(maximum_path_sum(read_input(input_)))