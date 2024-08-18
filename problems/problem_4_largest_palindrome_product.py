# https://projecteuler.net/problem=4

def is_palindrome(n: int):
    s = str(n)
    return s == s[::-1]


def palindromes(min_, max_):
    return [n for n in range(min_, max_) if is_palindrome(n)]


def product_of_two_3_digit_numbers(n):
    for i in range(100, 999):
        if n % i == 0 and len(str(n // i)) == 3:
            return True
    return False


def largest_palindrome_product(min_, max_):
    return max([p for p in palindromes(min_, max_) if product_of_two_3_digit_numbers(p)])


print(largest_palindrome_product(100 * 100, 999 * 999))
