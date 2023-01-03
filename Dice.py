import random


def basic_roll(number_of_dices, range_of_roll):
    result = 0
    for a in range(number_of_dices):
        result += random.randint(1, range_of_roll)
    return result
