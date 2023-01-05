from Property import TypicalProperty
from Property import AirportProperty
from Property import DiceChargeProperty
from Field import PayField
from Field import ChanceField
from Field import GoToJailField
from Field import PropertyField
from Field import DiceChargePropertyField
from Field import Field
from GUI import gui_main
from Game import Game

import sys

possible_actions = []

board = [
    Field(0, "Start"),
    PropertyField(1, TypicalProperty("Brown1", 2, 60, "brown", 50)),
    ChanceField(2, "Kasa Społeczna"),
    PropertyField(3, TypicalProperty("Brown2", 4, 60, "brown", 50)),
    PayField(4, "Podatek Dochodowy", 200),
    PropertyField(5, AirportProperty("Airport1", 25, 200, "airport")),
    PropertyField(6, TypicalProperty("Light Blue1", 8, 100, "light blue", 50)),
    ChanceField(7, "Szansa"),
    PropertyField(8, TypicalProperty("Light Blue2", 8, 100, "light blue", 50)),
    PropertyField(9, TypicalProperty("Light Blue3", 10, 120, "light blue", 50)),
    Field(10, "Więzienie"),
    PropertyField(11, TypicalProperty("Pink1", 10, 140, "pink", 100)),
    DiceChargePropertyField(12, DiceChargeProperty("DiceCharge1", 10, 150, "dicecharge")),
    PropertyField(13, TypicalProperty("Pink2", 10, 140, "pink", 100)),
    PropertyField(14, TypicalProperty("Pink3", 12, 160, "pink", 100)),
    PropertyField(15, AirportProperty("Airport2", 25, 200, "airport")),
    PropertyField(16, TypicalProperty("Orange1", 16, 180, "orange", 100)),
    ChanceField(17, "Kasa Społeczna"),
    PropertyField(18, TypicalProperty("Orange2", 16, 180, "orange", 100)),
    PropertyField(19, TypicalProperty("Orange3", 20, 200, "orange", 100)),
    Field(20, "Parking"),
    PropertyField(21, TypicalProperty("Red1", 22, 220, "red", 150)),
    ChanceField(22, "Szansa"),
    PropertyField(23, TypicalProperty("Red2", 22, 220, "red", 150)),
    PropertyField(24, TypicalProperty("Red3", 24, 240, "red", 150)),
    PropertyField(25, AirportProperty("Airport3", 25, 200, "airport")),
    PropertyField(26, TypicalProperty("Yellow1", 28, 260, "yellow", 150)),
    PropertyField(27, TypicalProperty("Yellow2", 28, 260, "yellow", 150)),
    DiceChargePropertyField(28, DiceChargeProperty("DiceCharge2", 10, 150, "dicecharge")),
    PropertyField(29, TypicalProperty("Yellow3", 32, 280, "yellow", 150)),
    GoToJailField(30, "Idź do więzienia"),
    PropertyField(31, TypicalProperty("Green1", 32, 300, "green", 200)),
    PropertyField(32, TypicalProperty("Green2", 32, 300, "green", 200)),
    ChanceField(33, "Kasa Społeczna"),
    PropertyField(34, TypicalProperty("Green3", 34, 320, "green", 200)),
    PropertyField(35, AirportProperty("Airport4", 25, 200, "airport")),
    ChanceField(36, "Szansa"),
    PropertyField(37, TypicalProperty("Dark Blue1", 45, 360, "dark blue", 200)),
    PayField(38, "Domiar Podatkowy", 100),
    PropertyField(39, TypicalProperty("Dark Blue2", 50, 400, "dark blue", 200)),
]

if __name__ == "__main__":
    game = Game(board)
    gui_main(game, sys.argv)
