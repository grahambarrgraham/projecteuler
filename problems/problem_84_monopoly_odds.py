# https://projecteuler.net/problem=84
from collections import defaultdict
from random import Random, shuffle
from time import time

go_to_jail, jail, go = 30, 10, 0
c1, e3, h2 = 11, 24, 39
r1, r2, r3, r4 = 5, 15, 25, 35
u1, u2 = 12, 28
community_chest_squares = [2, 17, 33]
chance_squares = [7, 22, 36]
community_chest_deck = [go, jail] + [''] * 14
chance_deck = [go, jail, c1, e3, h2, r1, 'next railway', 'next railway', 'next utility', 'back 3'] + [''] * 6


class Deck:
    index: int = 0
    deck_list: list

    def __init__(self, deck_list):
        self.deck_list = deck_list.copy()
        shuffle(self.deck_list)

    def draw(self, square, num_squares):
        card = self.deck_list[self.index % len(self.deck_list)]
        self.index += 1
        if type(card) is int:
            return card
        elif card == '':
            return square
        elif card == 'back 3':
            nxt = square - 3
            return nxt if nxt >= 0 else nxt + num_squares
        elif card == 'next railway':
            # return square
            return r1 if square < r1 else r2 if square < r2 else r3 if square < r3 else r4 if square < r4 else r1
        elif card == 'next utility':
            return u1 if square < u1 else u2 if square < u2 else u1


def roll(r: Random, num_dice_faces):
    roll1 = r.randint(1, num_dice_faces)
    roll2 = r.randint(1, num_dice_faces)
    return roll1 + roll2, roll1 == roll2


def monopoly_odds(num_dice_faces=6, num_squares=40, iterations=1000000):
    rand = Random()
    chance = Deck(chance_deck)
    community_chest = Deck(community_chest_deck)
    landed = defaultdict(int)
    current_square = 0
    double_count = 0
    for i in range(iterations):
        m, is_double = roll(rand, num_dice_faces)
        double_count = double_count + 1 if is_double else 0
        if double_count > 2:
            double_count = 0
        else:
            current_square = (current_square + m) % num_squares
            if current_square == go_to_jail:
                current_square = jail
            elif current_square in community_chest_squares:
                current_square = community_chest.draw(current_square, num_squares)
            elif current_square in chance_squares:
                current_square = chance.draw(current_square, num_squares)
            landed[current_square] += 1

    landing_probability_dist = [(square, num_landings / (iterations / 100)) for square, num_landings in landed.items()]
    return sorted([(round(probability, 2), square) for square, probability in landing_probability_dist], reverse=True)


def modal_string(lst: list[int]):
    return ''.join([str(i).zfill(2) for i in lst])


now = time()
odds = monopoly_odds(num_dice_faces=4)
result = modal_string([square for _, square in odds[0:3]])
print(result, f"{round(time() - now, 2)} seconds")
