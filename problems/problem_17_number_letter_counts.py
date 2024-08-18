# https://projecteuler.net/problem=17
from time import time

unit_names = {1: 'one', 2: 'two', 3: 'three',
              4: 'four', 5: 'five', 6: 'six',
              7: 'seven', 8: 'eight', 9: 'nine'}

teens_names = {0: 'ten', 1: 'eleven',
              2: 'twelve', 3: 'thirteen', 4: 'fourteen',
              5: 'fifteen', 6: 'sixteen', 7: 'seventeen',
              8: 'eighteen', 9: 'nineteen'}

tens_names = {2: 'twenty', 3: 'thirty',
              4: 'forty', 5: 'fifty', 6: 'sixty',
              7: 'seventy', 8: 'eighty', 9: 'ninety'}


def number_to_letters(n: int):
    if n % 1000 == 0:
        return 'onethousand'

    hundreds = n // 100
    tens = (n % 100) // 10
    units = n % 10

    s = '' if hundreds == 0 else unit_names[hundreds] + 'hundred'
    s += 'and' if hundreds > 0 and (tens > 0 or units > 0) else ''
    if tens == 1:
        s += teens_names[units]
    elif tens > 1:
        s += tens_names[tens]
        if units > 0:
            s += unit_names[units]
    elif units > 0:
        s += unit_names[units]

    return s


def number_letter_counts(n: int):
    return sum([len(number_to_letters(i)) for i in range(1, n + 1)])


print(number_letter_counts(1000))
