# https://projecteuler.net/problem=6


def sum_square_difference(n):
    sum_of_squares = sum([i * i for i in range(1, n + 1)])
    sum_of_range = sum([i for i in range(1, n + 1)])
    square_of_sum = sum_of_range * sum_of_range
    return square_of_sum - sum_of_squares


print(sum_square_difference(100))
