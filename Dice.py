import random

def basic_roll(self, number_of_dices, range):
    result = 0
    for a in number_of_dices:
        result += random.randint(0, range)
        return result