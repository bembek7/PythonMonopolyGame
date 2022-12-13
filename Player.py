from Game import Game
from Property import Property
# pieniądze
# lista posiadlosci
class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._cash = 1500
        self._position = 0
        self._properties = []
        self._in_jail = False

    def get_position(self):
        return self._position

    def set_position(self, newposition):
        self._position = newposition
    
    def get_in_jail(self):
        return self._in_jail

    def set_in_jail(self, setjail):
        self._in_jail = setjail

    def get_name(self):
        return self._name

    def pay(self, amount):
        if self._cash - amount >= 0:
            self._cash = self._cash - amount
        return True
    # wymuszenie zastawu/sprzedaży

    def get_amount_of_type(self, type):
        result = 0
        for property in self._properties:
            if property.get_type() == type:
                result += 1
        return result

    def buy_property(self, property : Property):
        self._properties.append(property)
        self.pay(property.get_price())

    def move(self, result, game = Game):
        board_places = game.get_board_length()
        if self._position + result >= board_places:
            self._cash += 200
        if self._position + result < 0:
            self._position = board_places + self._position + result
        self._position = (self._position + result) % board_places