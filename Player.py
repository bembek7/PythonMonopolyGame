from Property import Property
from Property import TypicalProperty
from Property import SpecialProperty
# pieniądze
# lista posiadlosci


class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._cash = 1500
        self._position = 0
        self._properties = []
        self._in_jail = False
        self._dir_of_colors = {
            "brown": 0,
            "light blue": 0,
            "pink": 0,
            "orange": 0,
            "red": 0,
            "yellow": 0,
            "green": 0,
            "dark blue": 0
        }

    def get_properties(self):
        return self._properties

    def get_cash(self):
        return self._cash

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

    def gain(self, amount):
        self._cash += amount

    def get_available_apartments():
        pass

    def pay(self, amount):
        if self._cash - amount >= 0:
            self._cash = self._cash - amount
        return True
    # wymuszenie zastawu/sprzedaży

    def deactivate_property(self, property_given):
        for property in self._properties:
            if property.get_name() == property_given and property.is_active():
                property.deactivate()
                self.gain(int(property.get_price() / 2))

    def get_amount_of_type(self, type):
        result = 0
        for property in self._properties:
            if isinstance(property, SpecialProperty):
                if property.get_type() == type:
                    result += 1
        return result

    def buy_property(self, property: Property):
        self._properties.append(property)
        if isinstance(property, TypicalProperty):
            self._dir_of_colors[property.get_color()] += 1
        self.pay(property.get_price())

    def move(self, result):
        board_places = 40
        if self._position + result >= board_places:
            self._cash += 200
        if self._position + result < 0:
            self._position = board_places + self._position + result
        self._position = (self._position + result) % board_places

    def can_buy_home(self):
        dir = {
            "brown": 2,
            "light blue": 3,
            "pink": 3,
            "orange": 3,
            "red": 3,
            "yellow": 3,
            "green": 3,
            "dark blue": 2
        }
        for key in self._dir_of_colors:
            if self._dir_of_colors[key] == dir[key]:
                return True
            return False
