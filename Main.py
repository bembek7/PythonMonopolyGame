from Game import Game
from Property import TypicalProperty
from Property import AirportProperty
from Property import DiceChargeProperty

possible_actions = []

board = [
    (0, "Start"),
    (1, TypicalProperty("", 10, 60, "brown", 50)),
    (2, "Kasa Społeczna", possible_actions[0]),
    (3, TypicalProperty("", 10, 60, "brown", 50)),
    (4, "Podatek Dochodowy", 200),
    (5, AirportProperty("", 25, 200, "airport")),
    (6, TypicalProperty("", 10, 100, "light blue", 50)),
    (7, "Szansa", possible_actions[0]),
    (8, TypicalProperty("", 10, 100, "light blue", 50)),
    (9, TypicalProperty("", 10, 120, "light blue", 50)),
    (10, "Więzienie"),
    (11, TypicalProperty("", 10, 140, "light blue", 50)),
    (12, DiceChargeProperty("", 10, 120, "dicecharge")),
    (13, TypicalProperty("", 10, 140, "light blue", 50)),
    (14, TypicalProperty("", 10, 160, "light blue", 50)),
    (15, AirportProperty("", 25, 200, "airport")),
    (16, TypicalProperty("", 10, 180, "orange", 50)),
    (17, "Kasa Społeczna", possible_actions[0]),
    (18, TypicalProperty("", 10, 180, "orange", 50)),
    (19, TypicalProperty("", 10, 200, "orange", 50)),
    (20, "Parking"),
    (21, TypicalProperty("", 10, 220, "red", 50)),
    (22, "Szansa", possible_actions[0]),
    (23, TypicalProperty("", 10, 220, "red", 50)),
    (24, TypicalProperty("", 10, 240, "red", 50)),
    (25, AirportProperty("", 25, 200, "airport")),
    (26, TypicalProperty("", 19, 10, 260, "yellow", 50)),
    (27, TypicalProperty("", 19, 10, 260, "yellow", 50)),
    (28, DiceChargeProperty("", 10, 120, "dicecharge")),
    (29, TypicalProperty("", 19, 10, 260, "yellow", 50)),
    (30, "Idź do więzienia", possible_actions[0]),
    (31, TypicalProperty("", 19, 10, 300, "green", 50)),
    (32, TypicalProperty("", 19, 10, 300, "green", 50)),
    (33, "Kasa Społeczna", possible_actions[0]),
    (34, TypicalProperty("", 19, 10, 320, "green", 50)),
    (35, AirportProperty("", 25, 200, "airport")),
    (36, "Szansa", possible_actions[0]),
    (37, TypicalProperty("", 19, 10, 350, "dark blue", 50)),
    (38, "Domiar Podatkowy", 100),
    (39, TypicalProperty("", 19, 10, 400, "dark blue", 50)),
    ]