from Property import TypicalProperty
from Property import AirportProperty
from Property import DiceChargeProperty
from Field import PayField
from Field import ChanceField
from Field import GoToJailField
from Field import PropertyField
from Field import Field
from GUI import gui_main
from Game import Game

import sys

possible_actions = []

board = [
    Field(0, "Start"),
    PropertyField(1, TypicalProperty("", 10, 60, "brown", 50)),
    ChanceField(2, "Kasa Społeczna"),
    PropertyField(3, TypicalProperty("", 10, 60, "brown", 50)),
    PayField(4, "Podatek Dochodowy", 200),
    PropertyField(5, AirportProperty("", 25, 200, "airport")),
    PropertyField(6, TypicalProperty("", 10, 100, "light blue", 50)),
    ChanceField(7, "Szansa"),
    PropertyField(8, TypicalProperty("", 10, 100, "light blue", 50)),
    PropertyField(9, TypicalProperty("", 10, 120, "light blue", 50)),
    Field(10, "Więzienie"),
    PropertyField(11, TypicalProperty("", 10, 140, "pink", 50)),
    PropertyField(12, DiceChargeProperty("", 10, 120, "dicecharge")),
    PropertyField(13, TypicalProperty("", 10, 140, "pink", 50)),
    PropertyField(14, TypicalProperty("", 10, 160, "pink", 50)),
    PropertyField(15, AirportProperty("", 25, 200, "airport")),
    PropertyField(16, TypicalProperty("", 10, 180, "orange", 50)),
    ChanceField(17, "Kasa Społeczna"),
    PropertyField(18, TypicalProperty("", 10, 180, "orange", 50)),
    PropertyField(19, TypicalProperty("", 10, 200, "orange", 50)),
    Field(20, "Parking"),
    PropertyField(21, TypicalProperty("", 10, 220, "red", 50)),
    ChanceField(22, "Szansa"),
    PropertyField(23, TypicalProperty("", 10, 220, "red", 50)),
    PropertyField(24, TypicalProperty("", 10, 240, "red", 50)),
    PropertyField(25, AirportProperty("", 25, 200, "airport")),
    PropertyField(26, TypicalProperty("", 10, 260, "yellow", 50)),
    PropertyField(27, TypicalProperty("", 10, 260, "yellow", 50)),
    PropertyField(28, DiceChargeProperty("", 10, 120, "dicecharge")),
    PropertyField(29, TypicalProperty("", 10, 260, "yellow", 50)),
    GoToJailField(30, "Idź do więzienia"),
    PropertyField(31, TypicalProperty("", 10, 300, "green", 50)),
    PropertyField(32, TypicalProperty("", 10, 300, "green", 50)),
    ChanceField(33, "Kasa Społeczna"),
    PropertyField(34, TypicalProperty("", 10, 320, "green", 50)),
    PropertyField(35, AirportProperty("", 25, 200, "airport")),
    ChanceField(36, "Szansa"),
    PropertyField(37, TypicalProperty("", 10, 350, "dark blue", 50)),
    PayField(38, "Domiar Podatkowy", 100),
    PropertyField(39, TypicalProperty("", 10, 400, "dark blue", 50)),
    ]

if __name__ == "__main__":
    game = Game(board)
    gui_main(game, sys.argv)
    